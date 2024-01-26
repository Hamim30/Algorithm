def msr():
    img_list = os.listdir(PATH)
    for i in img_list:
        print(i)
        image = read_show("dt2",i,show=False)
        msrcr_img = MSRCR(image,config.SIGMA_LIST,config.ALPHA,config.BETA,config.G,config.OFFSET)
        cv2.imwrite(f'dt2_msr/{i}',msrcr_img)
msr()
