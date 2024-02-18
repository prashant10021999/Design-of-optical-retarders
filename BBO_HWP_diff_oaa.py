import numpy as np
import transfer_matrix as tm

THz = 1e12 
deg = 180/np.pi

BBO = tm.material( 1.6672, 1.5496, 0, 0, 'BBO', materialType='uniaxial')

thicknesses = [2690.476e-6*tm.mm]
materials   = [BBO]

for i in range(0,17):
   angles      = [i*np.pi/8]
   hwp         = tm.Stack( thicknesses, materials, angles )

   TransferMatrix = tm.stackTransferMatrix( hwp, 474.083*THz,0*deg, 0*deg, 1.0, 1.0 )
   M        = tm.Mueller( hwp, 474.083*THz, 0*deg, 0*deg, reflected=False)
   Jones          = tm.Jones( hwp, 474.083*THz, 0*deg, 0*deg, reflected=False)

   print("Mueller_matrix_of_the_sample for angle", f"{i}(pi/8)", "is:")
   print(M)
   # print("Jones:")
   # print(Jones)

   # Si = np.array([[1], [1], [0],[0]]) #input stokes vector
   # So = np.dot(M, Si)
   # print("Output_stokes_vector for angle", f"{i}(pi/8)", "is:")
   # print(So)