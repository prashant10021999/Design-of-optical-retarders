import numpy as np
import transfer_matrix as tm

THz = 1e12 
deg = 180/np.pi

Quartz = tm.material( 1.54425, 1.55338, 0, 0, 'Quartz', materialType='uniaxial')

# Glan polarizer

thicknesses = [2.8*tm.mm]
materials   = [Quartz]
angles      = [0]
GP          = tm.Stack( thicknesses, materials, angles )

TransferMatrix = tm.stackTransferMatrix( GP, 474.684*THz,0*deg, 0*deg, 1.0, 1.0 )
A              = tm.Mueller( GP, 474.684*THz, 0*deg, 0*deg, reflected=False)

# Moving wedge
thick = [1.4*tm.mm]
mater   = [Quartz]
ang     = [1*np.pi/2]
Wed     = tm.Stack( thick, mater, ang )

TransferMatrix = tm.stackTransferMatrix( Wed, 474.684*THz,0*deg, 0*deg, 1.0, 1.0 )
B              = tm.Mueller( Wed, 474.684*THz, 0*deg, 0*deg, reflected=False)

# fixed wedge

thi = [1.4*tm.mm]
mat = [Quartz]
angu     = [1*np.pi/2]
fwed     = tm.Stack( thi, mat, angu )

TransferMatrix = tm.stackTransferMatrix( fwed, 474.684*THz,0*deg, 0*deg, 1.0, 1.0 )
C       = tm.Mueller( fwed, 474.684*THz, 0*deg, 0*deg, reflected=False)

M = C @ B @ A

print("Mueller_matrix_of_the_sample:")
print(M)
Si = np.array([[1], [1], [0],[0]]) #input stokes vector
So = np.dot(M, Si)
print("Output_stokes_vector:")
print(So)