from PIL import Image
import glob
import os

all_normal=glob.glob('Normal Lymphnode_files\*')
all_reactive=glob.glob('Reactive hyperplasia_files\*')

for i in range(len(all_normal)):
    normal_file=glob.glob(all_normal[i]+'\*')
    
    reactive_file=glob.glob(all_reactive[i]+'\*')

    normal_check=list(map(lambda a:a.split('\\')[-1],normal_file))
    reactive_check=list(map(lambda a:a.split('\\')[-1],reactive_file))
    
    for i in range(len(normal_file)):
   
        if normal_check[i] in reactive_check:

    
            image1=Image.open(normal_file[i])
            image2=Image.open(reactive_file[i])
            image1=image1.resize((255,255))
            image2=image2.resize((255,255))
            img_=Image.blend(image1,image2,0.5)
            path=normal_file[i].split('\\')[-2]
        
        
            m_dir=r'D:\assign\Assing_ment_1\processed_images'+'\\'+path
            check_folder=os.path.isdir(m_dir)
            if not check_folder:
                os.mkdir(m_dir)
        
        
            img_.save(m_dir+'\\'+normal_check[i])
