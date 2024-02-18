import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import time
import math

# Load images 

HH=mpimg.imread('1.bmp')
HH=HH/255

N=HH.shape[0]
M=HH.shape[1]

x=int(M/2)
y=int(N/2)

HV=mpimg.imread('2.bmp')
HV=HV/255

VH=mpimg.imread('3.bmp')
VH=VH/255

VV=mpimg.imread('4.bmp')
VV=VV/255

PH=mpimg.imread('5.bmp')
PH=PH/255

PV=mpimg.imread('6.bmp')
PV=PV/255

MH=mpimg.imread('7.bmp')
MH=MH/255

MV=mpimg.imread('8.bmp')
MV=MV/255

RH=mpimg.imread('9.bmp')
RH=RH/255

RV=mpimg.imread('10.bmp')
RV=RV/255

LH=mpimg.imread('11.bmp')
LH=LH/255

LV=mpimg.imread('12.bmp')
LV=LV/255

HP=mpimg.imread('13.bmp')
HP=HP/255

HM=mpimg.imread('14.bmp')
HM=MH/255

VP=mpimg.imread('15.bmp')
VP=VP/255

VM=mpimg.imread('16.bmp')
VM=VM/255

PP=mpimg.imread('17.bmp')
PP=PP/255

PM=mpimg.imread('18.bmp')
PM=PM/255

MP=mpimg.imread('19.bmp')
MP=MP/255

MM=mpimg.imread('20.bmp')
MM=MM/255

RP=mpimg.imread('21.bmp')
RP=RP/255

RM=mpimg.imread('22.bmp')
RM=RM/255

LP=mpimg.imread('23.bmp')
LP=LP/255

LM=mpimg.imread('24.bmp')
LM=LM/255

HR=mpimg.imread('25.bmp')
HR=HR/255

HL=mpimg.imread('26.bmp')
HL=HL/255

VR=mpimg.imread('27.bmp')
VR=VR/255

VL=mpimg.imread('28.bmp')
VL=VL/255

PR=mpimg.imread('29.bmp')
PR=PR/255

PL=mpimg.imread('30.bmp')
PL=PL/255

MR=mpimg.imread('31.bmp')
MR=MR/255

ML=mpimg.imread('32.bmp')
ML=ML/255

LL=mpimg.imread('33.bmp')
LL=LL/255

RL=mpimg.imread('34.bmp')
RL=RL/255

LR=mpimg.imread('35.bmp')
LR=LR/255

RR=mpimg.imread('36.bmp')
RR=RR/255

print('loaded images')

# Calculate the matrix elements

m00=HH+HV+VH+VV
prom=np.mean(m00)
m00=m00/prom
m00=np.single(m00)
mu00 = np.mean(m00)

m01=HH+HV-VH-VV
m01=m01/prom
m01=np.single(m01)
mu01 = np.mean(m01)

m02=PH+PV-MH-MV
m02=m02/prom
m02=np.single(m02)
mu02 = np.mean(m02)

m03=RH+RV-LH-LV
m03=m03/prom
m03=np.single(m03)
mu03 = np.mean(m03)

m10=HH-HV+VH-VV
m10=m10/prom
m10=np.single(m10)
mu10 = np.mean(m10)

m11=HH-HV-VH+VV
m11=m11/prom
m11=np.single(m11)
mu11 = np.mean(m11)

m12=PH-PV-MH+MV
m12=m12/prom
m12=np.single(m12)
mu12 = np.mean(m12)

m13=RH-RV-LH+LV
m13=m13/prom
m13=np.single(m13)
mu13 = np.mean(m13)

m20=HP-HM+VP-VM
m20=m20/prom
m20=np.single(m20)
mu20 = np.mean(m20)

m21=HP-HM-VP+VM
m21=m21/prom
m21=np.single(m21)
mu21 = np.mean(m21)

m22=PP-PM-MP+MM
m22=m22/prom
m22=np.single(m22)
mu22 = np.mean(m22)

m23=RP-RM-LP+LM
m23=m23/prom
m23=np.single(m23)
mu23 = np.mean(m23)

m30=HR-HL+VR-VL
m30=m30/prom
m30=np.single(m30)
mu30 = np.mean(m30)

m31=HR-HL-VR+VL
m31=m31/prom
m31=np.single(m31)
mu31 = np.mean(m31)

m32=PR-PL-MR+ML
m32=m32/prom
m32=np.single(m32)
mu32 = np.mean(m32)

m33=LL-RL-LR+RR
m33=m33/prom
m33=np.single(m33)
mu33 = np.mean(m33)

print('matrix calculated')

# Mean matrix from the experimental matrix

experimental_mean_matrix=np.array([[np.mean(m00), np.mean(m01), np.mean(m02), np.mean(m03)],\
                        [np.mean(m10), np.mean(m11), np.mean(m12), np.mean(m13)],\
                        [np.mean(m20), np.mean(m21), np.mean(m22), np.mean(m23)],\
                        [np.mean(m30), np.mean(m31), np.mean(m32), np.mean(m33)]])
print(experimental_mean_matrix)

# Subplot of the Mueller matrix elements
fig, ax_list = plt.subplots(4, 4)
mlist = [m00, m01, m02, m03,
          m10, m11, m12, m13,
          m20, m21, m22, m23,
          m30, m31, m32, m33]

for ax, m in zip(ax_list.flat, mlist):
    im = ax.imshow(m,  cmap='gray', vmin=-1, vmax=1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.label_outer()

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)
fig.suptitle('Recovered matrix sample polarizer')
plt.show()
