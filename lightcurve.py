# lightcurve.py
#   objects for dealing with light curves

# 210709    working on the freq axis.  messily introduced variables for bw, dt etc - need to tidy scope
# 210706    working fft version.  discard the sine fit - inaccurate
#           duplicate obs fixed, linear interpolation working, but crude.
#           need smoothing?
#           fft picks out peaks in the curves.  Need to work out the axes.
# 210705    moved code into class LightCurve.
#           need to deal with duplicated in LightCurve.interpolate()



import csv
import matplotlib.pyplot as plt
from scipy import optimize, fft
from scipy.interpolate import interp1d
import numpy as np

class LightCurve:
    jd_obs = []         # observation (unprocessed) JD
    jd_proc = []        # pre-processed JD
    mag = []            # observation (unprocessed) magnitude
    mag_proc = []       # pre-processed magnitude
    fft_mag = []    
    n_obs = []          # number of observations 
    n_interp = []       # number of points, after interpolation
    dt = []             # interpolated time resolution
    T = []             # total observation time
    df = []             # interpolated freq resolution
    BW = []             # total bandwidth
#   star              start name

    def loadbaacurve(self):
        # for Middle Room PC
        #vssdir='C:\\Users\\cjohn\\OneDrive\\Astronomy\\variablestars\\data_baa'
        # for Study PC
        vssdir='C:\\Users\\User\\OneDrive\\Astronomy\\variablestars\\data_baa'

        #vssfile='Z UMA_20210619_100143.csv'
        #vssfile='Z UMA_20210629_133403.csv'
        vssfile='TX DRA_20210709_152330.csv'
        #vssfile='AH DRA_20210621_221943.csv'
        self.star=vssfile.split('_')[0]
        print(self.star)
        vssfullpath = vssdir + '\\' + vssfile

        #jd = []
        #mag = []

        jdmodifier = 2400000.0  #discard first N digits of jd here

        with open(vssfullpath) as csvfile:
            baaread = csv.DictReader(csvfile, delimiter=',')
            for row in baaread:
        #        print(row['Julian Date'], row['Magnitude'])
                self.jd_obs.append(float(row['Julian Date'])-jdmodifier)
                self.mag.append(float(row['Magnitude']))

        self.n_obs = len(self.jd_obs)

    def datasummary(self):
        # beginnings of a data summary
        # currently the scope of these variables is messy - some local some in object.
        self.T = float(self.jd_obs[0] - self.jd_obs[-1])
        
        print('JD start   :    ' + str(self.jd_obs[-1]))
        print('JD end     :    ' + str(self.jd_obs[0]))
        print('n_obs      :    ' + str(self.n_obs) )
        print('T (dy)     :    ' + str( self.T ) )

        #plot observations per 100 days
        jdbin = int((self.jd_obs[0] - self.jd_obs[-1]) / 100) # 100day bins
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(1,1,1)
        plt.hist(self.jd_obs, jdbin)
        plt.xlabel('days')
        plt.ylabel('n_obs (per 100 days)')
        plt.title(self.star)
        fig1.show()


    def preproc(self, demean, interp):
        # remove non-unique values and assuign to _proc variables
        [self.jd_proc, uniqueval_idx] = np.unique(self.jd_obs, True)
        self.mag_proc = [self.mag[ii] for ii in uniqueval_idx]
        print(len(self.jd_proc), len(self.mag_proc))

        #demean
        if demean == True:
            self.mag_proc = self.mag_proc - np.mean(self.mag_proc)

        #interpolate
        dt_interp = self.interpolate(4)
        return dt_interp


    def interpolate(self, interp_by):
        # cubic interpolation to (interp_by) times the data size
        if interp_by == 1:
            jd_interp = self.jd_proc
            mag_interp = self.mag_proc
        else:
            # need a better interpolation method here and/or smoothing
            jd_interp = np.linspace(self.jd_proc[1], self.jd_proc[-1], \
                                         interp_by * len(self.mag_proc), endpoint=True)
            ff = interp1d(self.jd_proc, self.mag_proc, kind='linear')
            mag_interp = ff(jd_interp)
            self.jd_proc = jd_interp
            self.mag_proc = mag_interp
            self.nobs_interp = len(self.mag_proc)
            #return dt_interp
            print("self.T ")
            print(self.T)
        
            print(type(self.T))
            print("self.nobsinterp ")
            print(type(self.nobs_interp))
            # return the interpolated dt
            return (float(self.T) / float(self.nobs_interp)) 

    def plotmag(self):
        
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(1,1,1)
        ax1.plot(self.jd_obs, self.mag, '.', \
                 self.jd_proc, self.mag_proc, '-')
        print(len(self.jd_obs), len(self.mag))
        print(len(self.jd_proc), len(self.mag_proc))
        ax1.set_title(self.star)
        fig1.show()

        
    def plotfft(self, dt_interp):
        BW = 1/dt_interp
        df = BW / self.nobs_interp
        fig2 = plt.figure()
        freq_axis = np.arange(0, BW, df)
        self.fft_mag = np.abs(fft.fft(self.mag_proc))
        print(len(freq_axis))
        print(len(self.fft_mag))
        
        ax1 = fig2.add_subplot(1,1,1)
        ax1.plot(freq_axis, self.fft_mag)
        plt.xlabel('Frequency (cycles/day)')
        plt.ylabel('n_obs (per 100 days)')

        fig2.show()

    
lc = LightCurve()
lc.loadbaacurve()
lc.datasummary()
dt_interp = lc.preproc(True, 4)
lc.plotmag()
lc.plotfft(dt_interp)

