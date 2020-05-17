import numpy as np
import matplotlib.pyplot as plt 

# set up parameters 
n_samples = 30
n_repeats = 1000
distribution_mean = 10

# figure preparation
fig, axs = plt.subplots(5, 2, constrained_layout=True)

# create and plot uniform and mean
uniform = np.random.rand(n_samples,n_repeats)*distribution_mean*2
plt.sca(axs[0,0])
plt.hist(uniform.flatten(), 50)
plt.title('Orig. distribution')
plt.sca(axs[1,0])
plt.hist(np.mean(uniform, axis=0), 50)
plt.title('Mean distribution')

# create and plot exponential and mean
exp = np.random.exponential(distribution_mean, size=(n_samples,n_repeats))
plt.sca(axs[0,1])
plt.hist(exp.flatten(), 50)
plt.title('Orig. distribution')
plt.sca(axs[1,1])
plt.hist(np.mean(exp, axis=0), 50)

# create and plot gamma and mean
gamma = np.random.gamma(distribution_mean, size=(n_samples,n_repeats))
plt.sca(axs[0,1])
plt.hist(exp.flatten(), 50)
plt.sca(axs[1,1])
plt.hist(np.mean(exp, axis=0), 50)

# create and plot gamma and mean
p = 0.5
n_flips = distribution_mean/p
binomial = np.random.binomial(n_flips, p, size=(n_samples,n_repeats))
plt.sca(axs[0,3])
plt.hist(binomial.flatten(), 50)
plt.sca(axs[1,3])
plt.hist(np.mean(exp, axis=0), 50)

plt.show()