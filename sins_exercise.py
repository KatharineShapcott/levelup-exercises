import numpy as np
import matplotlib.pyplot as plt 

n_bins = 40

# create distributions
uniform = np.random.rand(30,1000)*10*2
distribution_names = ['exponential', 'gamma']
for name in distribution_names:
    exec('%s=np.random.%s(10,size=(30,1000))'% (name, name))
binomial = np.random.binomial(30/0.5, 0.6, size=(10,1000))

all_distributions = eval('[uniform, %s, %s, binomial]'% (distribution_names[0], distribution_names[1]))
n_distributions = len(all_distributions)

# figure preparation
fig, axs = plt.subplots(n_distributions, 2, constrained_layout=True)

def hist(x, ax):
    global n_bins
    n_bins = n_bins+10
    plt.sca(ax)
    plt.hist(x, n_bins)

# plot original distributions
idist = 0
for dist in all_distributions:
    hist(dist.flatten(), axs[idist,0])
    if idist == 0:
        plt.title('Orig. distribution')
    idist = idist + 1

# plot means of distributions
tmp_function = lambda x:np.mean(x,axis=0)
idist = 0
for dist in all_distributions:
    hist(tmp_function(dist), axs[idist,1])
    if idist == 0:
        plt.title('Mean distribution')
    idist = idist + 1

plt.show()