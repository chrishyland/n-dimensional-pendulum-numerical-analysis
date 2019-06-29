import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.linalg import solve_banded as solve
import os

class Chain:
    
    def __init__(self,n):
        """Creates a N-Chain
        
        Parameters
        ----------
        n        : Number of masses
        theta    : Angle
        omega    : Velocity
        alpha    : Acceleration
        dif      : Difference between neighbouring angles.
        L        : 2nd-order finite difference 
        z        : State vector (Equation 22)
        
        Methods
        -------
        call                             : Returns omega, alpha
        retrieve_cartesian_coordinates   : Returns x, z (Equation 6)
        retrieve_velocity                : Returns dx, dz (Equation 27)
        energy                           : Returns energy (Equation 25)
        hanging_state                    : Returns theta, omega
        
        """
        self.n = n
        
        self.theta = np.zeros(n)
        self.omega = np.zeros(n)
        self.alpha = np.zeros(n)
        self.tension = np.zeros(n)

        #Equation 17
        self.dif = np.zeros(n-1)
        self.sin = np.zeros(n-1)
        self.cos = np.zeros(n-1)
        
        # Equation 19
        self.L = np.zeros((3,n)) 
        self.L[1,1:] = np.full(n-1,2) 
        self.L[1,0] = 1
    
    
    def __call__(self, z):
        """
        Computes the next step in time of the system.
        """
        self.theta, self.omega = z[:self.n], z[self.n:] # equation 22

        self.dif = np.diff(self.theta) # equation 17
        self.sin, self.cos = np.sin(self.dif), -np.cos(self.dif) 

        self.tension = self.omega**2
        self.tension[0] += np.cos(self.theta[0])

        self.L[0,1:], self.L[2,:-1] = self.cos, self.cos
        solve( (1,1), self.L, self.tension, overwrite_b=True, overwrite_ab=False, check_finite=False)

        self.alpha[:-1] = self.sin * self.tension[1:]
        self.alpha[-1] = 0
        self.alpha[1:] -= self.sin * self.tension[:-1]
        self.alpha[0] -= np.sin(self.theta[0])
        
        return np.concatenate([self.omega, self.alpha])

    
    # self.retrieve_cartesian_coordinates()
    def retrieve_cartesian_coordinates(self, origin=True):
        """
        Retrieves the Cartesian coordinates of the system.
        """
        x, z = np.cumsum(np.sin(self.theta)), -np.cumsum(np.cos(self.theta))

        if origin:
            x, z = np.insert(x,0,0), np.insert(z,0,0)
        return x, z
       
        
    # self.retrieve_velocity()  
    def retrieve_velocity(self, origin=True):
        """
        Retrieves the velocity of the system.
        """
        dx, dz = np.cumsum(self.omega*np.cos(self.theta)), np.cumsum(self.omega*np.sin(self.theta))
        
        if origin:
            dx,dz = np.insert(dx,0,0), np.insert(dz, 0, 0)
        
        return dx, dz
    
    
    # self.energy()
    def energy(self, total=True):
        """
        Computes the energy of the system.

        Returns a scalar of amount of energy in system.
        """
        x, z = self.retrieve_cartesian_coordinates(origin=False)
        dx, dz = self.retrieve_velocity(origin=False)

        e = 0.5*(dx**2 + dz**2) + z
        
        if total: return np.sum(e)
        
        return e

    
    # self.hanging_state(a,b)
    def hanging_state(self,a,b):
        """
        Helper function for the construction of the initial state of the system.
        """
        self.theta, self.omega = np.pi - np.arctan2(a, np.linspace(-b,1-b,self.n)), np.zeros(self.n)
        return np.concatenate([self.theta, self.omega])
    
    
    
'============================================================================================================'
    
    
    
class RK45():
    '''Runge-Kutta-Fehlberg time stepper
    
    Parameters
    ----------
    force   : Forcing function (Equation 23)
    state   : State vector (Equation 22)
    error   : 4th order RKF error
    iter    : Step iteration
    time    : Time passed
    
    Methods
    -------
    call    : Computes the next step based on the RK45 algorithm 
    tableu  : Returns coefficients from Butcher Tableu for RKF or Dorman-prince method
    
    '''
    def __init__(self, force, state, error=1e-16, iter=0, time=0, stages=6):
        self.force = force
        self.state = state
        self.error = error
        
        self.iter = iter
        self.time = time
        
        self._stages_ = stages
        self._karray_ = np.zeros((stages, len(self.state)))
    
    
    # self(dt)
    def __call__(self, dt, measure_error=True):
        """
        Makes one iteration of the system utilising the Runge-Kutta scheme.
        """
        f, x = self.force, self.state
        
        s, k = self._stages_, self._karray_
        a, b = self.tableu(dt)
        
        k[0] = f(x)
        
        # Runge-Kutta Evaluation
        for i in range(1, s):
            k[i] = f( x + a[i-1, :i].dot(k[:i]) )
        
        self.state += b[0].dot(k)
        
        if measure_error:
            self.error = np.max(np.abs(b[1].dot(k)))
        
        self.iter += 1
        self.time += dt
        
    def tableu(self, dt, s=6, p=2, rkh=True):
        """
        Butcher tableu for RK-Fehlberg or Dorman-prince method.
        """
        a = np.zeros((s-1, s-1))
        b = np.zeros((p, s))
        
        if rkh:
            # RK-Fehlberg
            a[0,0:1] = [1/4]
            a[1,0:2] = [3/32, 9/32]
            a[2,0:3] = [1932/2197, -7200/2197, 7296/2197]
            a[3,0:4] = [439/216, -8, 3680/513, -845/4104]
            a[4,0:5] = [-8/27, 2, -3544/2565, 1859/4104, -11/40]

            b[0] = [16/135, 0, 6656/12825, 28561/56438, -9/50, 2/55]
            b[1] = [25/216, 0, 1408/2565, 2197/4104, -1/5, 0]
        else:
            # Dorman-Prince Method
            a = np.zeros((s, s))
            b = np.zeros((p, s+1))            
            a[0,0:1] = [1/5]
            a[1, 0:2] = [3/40, 9/40]
            a[2, 0:3] = [44/45, -56/15, 32/9]
            a[3, 0:4] = [19372/6561, -25360/2187, 64448/6561, -212/729]
            a[4, 0:5] = [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656]
            a[5, 0:6] = [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84]
            
            b[0] = [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0]
            b[1] = [5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40]
        
        # Add up k's with b weights.
        b[1] -= b[0]
        
        # Weight by time step size.
        a *= dt
        b *= dt
        
        return a,b    
       
    
'============================================================================================================'
    
    
    
class chain_plot():
    '''Class to plot the N-chain
    
    Parameters
    ----------
    N   : Number of masses
    x   : X-coordinates of each mass
    y   : Y-coordinates of each mass
    
    Method
    ------
    call     : Creates an instantaneous plot 
    output   : Generates and saves a .png of plot
    setitem  : Modify aspects of plot
    File     : Return location and details of .png file
    '''
    
    def __init__(self, N, output=False, size=8):
    
        fig, ax = plt.subplots(figsize=(size, size))
        
        ax.tick_params(axis='both',
                       which='both',
                       bottom=False,
                       top=False,
                       labelbottom=False,
                       right=False,
                       left=False,
                       labelleft=False)
        ax.set_xlim([-(N+1), +(N+1)])
        ax.set_ylim([-N, 2])
        ax.set_aspect('equal')
        
        self.fig = fig
        self.ax = ax
        
        self.output=output
        self.dir = './'
        self.name = 'output'
        self.digits= 4
        self.fmt = '.png'
        self.dpi = 200
        self.count = 0
        self.clear = True
    
    
    # self(x, y)
    def __call__(self, x, y, color='red'):
        
        chain, = self.ax.plot(x,y,color=color, marker='o', linewidth=2)
        
        if self.output:
            file = self.file()
            if self.fmt == 'pdf': self.dpi = None
            self.fig.savefig(file, bbox_inches='tight', dpi=self.dpi)
            if self.clear: chain.remove()
            self.count += 1
    
    
    # self(item, val)
    def __setitem__(self, item, val):
        """
        Helper function for storing images.
        """
        if item == 'output': self.output = val
        
        if item == 'name': self.name = val
        
        if item == 'digits': self.digits = val
            
        if item == 'dir':
            self.dir = val
            try:
                os.mkdir(val)
            except:
                None
        if item == 'fmt':
            self.fmt = val
        
        if item == 'dpi':
            self.dpi = val
        
        if item == 'clear':
            self.clear = var
            
    
    # self.file()
    def file(self):
        
        num = ("{:0" + str(self.digits) + "d}")
        num = num.format(self.count)
        
        return self.dir + self.name + num + self.fmt
    
    