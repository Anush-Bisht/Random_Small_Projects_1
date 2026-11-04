import pyscreenshot

# image = pyscreenshot.grab()
# image.show()
# image.save("SCREENSHOT.png")

# TAKING SCREENSHOT FOR PARTS
image = pyscreenshot.grab(bbox=(10, 10, 500, 500))
image.show()
image.save("PARTICAL_SCREENSHOT.png")