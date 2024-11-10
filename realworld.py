import numpy as np
from matplotlib import pyplot as plt


from SRT3 import MPS_SCPS, MPS_SCPS_robust
from PIL import Image

from utils.PSUtils.eval import evalsurfaceNormal

def runmap( num_lights,object):
        
        
        N_path = f"utils/PSUtils/sample/{object}/gtnest.npy"
        mask_path = f"utils/PSUtils/sample/{object}/mask.npy"
    
        print(num_lights)
        
        L_path = f'utils/PSUtils/sample/{object}/light_{num_lights}.npy'
        
        L_dir = np.load(L_path)
        # print(L_dir.shape)
        mask = np.load(mask_path)
        # print(mask)
        N_gt = np.load(N_path)
        # print(N_gt.shape)

        h, w = mask.shape
        f = len(L_dir)
       
        print(mask.shape)
         
        if num_lights == 4:
                
                filenames = [
                    f"utils/PSUtils/sample/{object}/{object}11.png",
                    f"utils/PSUtils/sample/{object}/{object}9.png",
                    f"utils/PSUtils/sample/{object}/{object}4.png",
                    f"utils/PSUtils/sample/{object}/{object}2.png"
                ]
                
        elif num_lights == 12:
                
                filenames = [
                    f"utils/PSUtils/sample/{object}/{object}{i}.png"
                    for i in range(12)
                ]
                
        else:
                raise ValueError("Unsupported number of lights. Only 4 or 12 are supported.")
            
           
        images = []    
        for filename in filenames:
                image = np.array(Image.open(filename), dtype=np.float64)
                images.append(image)
            
            
        img_set = np.stack(images, axis=-1)
    
    

        
        
        
        
       
                
                

        
        method_set = ['Fact']
        for method in method_set:
                [N_est, reflectance] = MPS_SCPS.run_MPS_SCPS(img_set, mask, L_dir, method)
                
                [error_map, MAE, MedianE] = evalsurfaceNormal(N_gt, N_est, mask,'real')
                print('MAE-')
                print(MAE)
                # img_avg = error_map
                # #img_avg = N_est
                # plt.imshow(img_avg, cmap='jet')
                # plt.title('Average of All Spectral Bands')
                # plt.show()
                
                  
                     
    
        return N_est, error_map   

#alter these 3 params to get results
    

num_lights = 12
object = 'relief'




num_iter = 1

errmap = None
normals = None
rend_img = None
for i in range(num_iter):
 
 seed = 50 + i
 
 z,w = runmap(num_lights,object)
#  print(x)
#  mae = mae + x
 if i==0:
    # errmap = y
    normals = z
    rend_img = w
 else:
    # errmap = errmap + y
    normals = normals + z 
    rend_img = rend_img + w  


# error_map = errmap/num_iter
n_est = normals/num_iter
rendered_img = rend_img/num_iter


img_avg = n_est
                

plt.imshow(img_avg, cmap='brg')
plt.title('Normal Estimates')
plt.show()

img_avg = rendered_img
                

plt.imshow(img_avg, cmap='jet')
plt.title('Error Map')
plt.show()






