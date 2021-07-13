import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")

# The background of the image is removed and only the output only contains the car.
change_bg.color_bg("view1.jpeg",colors=(255,255,255),output_image_name="op1_car.jpg",detect="car")
change_bg.color_bg("view2.jpeg",colors=(255,255,255),output_image_name="op2_car.jpg",detect="car")
change_bg.color_bg("view3.jpeg",colors=(255,255,255),output_image_name="op3_car.jpg",detect="car")