import numpy as np
import matplotlib.pyplot as plt 

# set up parameters 
n_samples = 30
n_repeats = 1000
distribution_mean = 10
p = 0.5 # for binomial only

# create distributions
uniform = np.random.rand(n_samples,n_repeats)*distribution_mean*2
exp = np.random.exponential(distribution_mean, size=(n_samples,n_repeats))
gamma = np.random.gamma(distribution_mean, size=(n_samples,n_repeats))
n_flips = distribution_mean/p
binomial = np.random.binomial(n_flips, p, size=(n_samples,n_repeats))

all_distributions = [uniform, exp, gamma, binomial]
n_distributions = len(all_distributions)

# figure preparation
fig, axs = plt.subplots(n_distributions, 2, constrained_layout=True)

def plot_distribution(x, ax, n_bins=50):
    plt.sca(ax)
    plt.hist(x, n_bins)

# plot original distributions
idist = 0
for dist in all_distributions:
    plot_distribution(dist.flatten(), axs[idist,0])
    if idist == 0:
        plt.title('Orig. distribution')
    idist = idist + 1

# plot means of distributions
idist = 0
for dist in all_distributions:
    plot_distribution(np.mean(dist, axis=0), axs[idist,1])
    if idist == 0:
        plt.title('Mean distribution')
    idist = idist + 1

plt.show()