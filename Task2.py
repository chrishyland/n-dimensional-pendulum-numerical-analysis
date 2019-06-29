import numpy as np
import matplotlib.pyplot as plt
import time


def plot_properties(property_analyse,f,state,stepper,N,compare=False,x=True,z=True):
    '''Plotting function to analyse dynamics as a function of time and space
    
    Set up
    ------
    f = Chain(N)
    z = f.hanging_state(a, b)
    stepper = RK45(f,z)
    
    
    Parameters
    ----------
    position, velocity, energy, N, a, b
    x       : analyse x-directional property
    z       : analyse z-directional property
    compare : analyse both x and z together 
    
    '''

    T, dt, freq = 100, 0.01, 100
    X = np.zeros((1+int(T/dt)//freq, 2, N+1))
    V = np.zeros((1+int(T/dt)//freq, 2, N+1))
    E = np.zeros((1+int(T/dt)//freq, 1, N+1))
    X[0][:] = f.retrieve_cartesian_coordinates()
    V[0][:] = f.retrieve_velocity()
    E[0] = f.energy()
        
    while stepper.time < T:
        stepper(dt)
        if stepper.iter % freq == 0: 
            out = stepper.iter//freq
            X[out][:] = f.retrieve_cartesian_coordinates()
            V[out][:] = f.retrieve_velocity()
            E[out] = f.energy()

    
    if property_analyse == 'position':
        
        if compare:
        
            for i,j,name in zip([1,2,3],[1,N//2,-1],['Start positions', 'Middle positions', 'End positions']):
                
                f = plt.figure(figsize=(15,8))
                ax = f.add_subplot(3,1,i)
                ax.plot(X[:,0,j], linewidth=2)
                ax.plot(X[:,1,j], linewidth=2)
                ax.tick_params(axis='both', labelsize=10)
                ax.set_xlabel('Time',fontsize=15)
                ax.set_ylabel('Position',fontsize=15)
                ax.set_title(name,fontsize=15)
                ax.legend(["x(t)", "z(t)"],fontsize=15)
                
            plt.tight_layout()
                
        else:
            
            if x and z:
                number = [0,1]
                names = ['X positions for N = %i' %(N), 'Z positions for N = %i' %(N)]
            if x and (not z):
                number = [0]
                names = ['X positions for N = %i' %(N)]
            if (not x) and z:
                number = [1]
                names = ['Z positions for N = %i' %(N)]
                
            for i,name in zip(number,names):
                
                f = plt.figure(figsize=(15,8))
                ax = f.add_subplot(2,1,i+1)
                ax.plot(X[:,i,1], linewidth=2)
                ax.plot(X[:,i,N//2], linewidth=2)
                ax.plot(X[:,i,-1], linewidth=2)
                ax.tick_params(axis='both', labelsize=10)
                ax.set_xlabel('Time',fontsize=15)
                ax.set_ylabel('Position',fontsize=15)
                ax.set_title(name,fontsize=15)
                ax.legend(["start(t)", "middle(t)", "end(t)"],fontsize=15)
                
            plt.tight_layout()
        
    if property_analyse == 'velocity': 
        
        if compare:
                
            for i,j,name in zip([1,2,3],[1,N//2,-1],['Start positions', 'Middle positions', 'End positions']):
                
                f = plt.figure(figsize=(15,8))
                ax = f.add_subplot(3,1,i)
                ax.plot(V[:,0,j], linewidth=2)
                ax.plot(V[:,1,j], linewidth=2)
                ax.tick_params(axis='both', labelsize=10)
                ax.set_xlabel('Time',fontsize=15)
                ax.set_ylabel('Velocity',fontsize=15)
                ax.set_title(name,fontsize=15)
                ax.legend(["dx(t)", "dz(t)"],fontsize=15)
                
            plt.tight_layout()
                    
        else:
            
            if x and z:
                number = [0,1]
                names = ['X-velocity for N = %i' %(N), 'Z-velocity for N = %i' %(N)]
            if x and (not z):
                number = [0]
                names = ['X-velocity for N = %i' %(N)]
            if (not x) and z:
                number = [1]
                names = ['Z-velocity for N = %i' %(N)]
                
            for i,name in zip(number,names):
                
                f = plt.figure(figsize=(15,8))
                ax = f.add_subplot(2,1,i+1)
                ax.plot(V[:,i,1], linewidth=1)
                ax.plot(V[:,i,N//2], linewidth=1)
                ax.plot(V[:,i,-1], linewidth=1)
                ax.tick_params(axis='both', labelsize=10)
                ax.set_xlabel('Time',fontsize=15)
                ax.set_ylabel('Velocity',fontsize=15)
                ax.set_title(name,fontsize=15)
                ax.legend(["start(t)", "middle(t)", "end(t)"],fontsize=15)
                
            plt.tight_layout()

                    
    if property_analyse == 'energy': 
        
        f = plt.figure(figsize=(15,8))
        ax = f.add_subplot(1,1,1)
        ax.plot(E[:,0,1], linewidth=2)
        ax.tick_params(axis='both', labelsize=10)
        ax.set_xlabel('Time',fontsize=15)
        ax.set_ylabel('Energy',fontsize=15)
        ax.set_title('Energy of Chain',fontsize=15)  
        plt.tight_layout()


    
'================================================================================='


def plot_histogram(values, title):
    
    plt.hist(values)
    plt.ylabel('Frequency')
    plt.title(f"{title} histogram")
    
    
'================================================================================='
    
    
def compute_moving_average(N, values):
    """ Computes the N-moving average for the array of values, for len(values) >= N.
    
    Parameters
    ----------
    N        : scalar
    values   : numpy array of floats.
    
    """
    if len(values) < N:
        raise Exception("Array value passed in is too small.")
    
    return sum(values[-N:])/N

   


