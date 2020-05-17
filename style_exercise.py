import numpy as np
import matplotlib.pyplot as plt 
HwMnySmplsDrwn=30
NmbrTmsDoSmplng =1000
DstrbMean4All=10
BnmlProb=0.5 # for binomial only
# create distributions
distr1=np.random.rand(HwMnySmplsDrwn,NmbrTmsDoSmplng)*30*2
distri2= np.random.exponential(DstrbMean4All,size=( HwMnySmplsDrwn,NmbrTmsDoSmplng))
distr3 =np.random.gamma( DstrbMean4All,size= (HwMnySmplsDrwn,NmbrTmsDoSmplng))
distribution4=np.random.binomial(DstrbMean4All /BnmlProb,BnmlProb ,size=( HwMnySmplsDrwn,NmbrTmsDoSmplng))
AllDst4Plttng=[distr1,distri2,distri2,distribution4]
# figure preparation
NewFigu4Plottig,Allax4Plttng=plt.subplots(len(AllDst4Plttng),2,constrained_layout=True)
def Fnc4plttngHstgrm(DtCmFrmDstrbtn,Ax4Plttng1,BnFrHstgrm=50):
  plt.sca(Ax4Plttng1)
  plt.hist(DtCmFrmDstrbtn,BnFrHstgrm)
# plot original distributions
i=0
for d in AllDst4Plttng:
  Fnc4plttngHstgrm(d.flatten(),Allax4Plttng[i,0])
  if i ==1:plt.title ('Mean distribution')
  i=i+1
# plot means of distributions
i=0
for d in AllDst4Plttng:
  Fnc4plttngHstgrm (np.mean(d,axis=0),Allax4Plttng[i,1])
  if i ==2:plt.title('Orig. distribution')
  i=i+1
plt.show()