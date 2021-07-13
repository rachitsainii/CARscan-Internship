import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
# The original background of the image is replaced by a new image called back.jpg
# for image named as view1.jpeg
change_bg.change_bg_img(f_image_path="view1.jpeg",b_image_path="back.jpg",output_image_name="op1.jpg") 
# for image named as view2.jpeg
change_bg.change_bg_img(f_image_path="view2.jpeg",b_image_path="back.jpg",output_image_name="op2.jpg")
# for image named as view3.jpeg
change_bg.change_bg_img(f_image_path="view3.jpeg",b_image_path="back.jpg",output_image_name="op3.jpg")

#This code converts the original background to greyscale but retains the color of the object(car in this case)
output = change_bg.gray_bg("view1.jpeg",output_image_name="o1.jpg")
output = change_bg.gray_bg("view2.jpeg",output_image_name="o2.jpg")
output = change_bg.gray_bg("view3.jpeg",output_image_name="o3.jpg")


