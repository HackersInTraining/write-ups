from PIL import Image #Pillow is a python library to work with images and image modifications


i = Image.open("warp_speed.5978d1405660e365872cf72dddc7515603f657f12526bd61e56feacf332cccad.jpg")
i.getdata()

print(i.format, i.size, i.mode)
result = Image.new("RGB", (1200, 1200))


def roll(image, delta, y):#rolls stripes of 8 pixels sideways. basically it moves everything sideways and the part that's off the image is put on the other side
    "Roll an image sideways"
    print(y)
    xsize, ysize = image.size
    ybase = y
    ysize = y+8
    print(0, ybase, delta, ysize)

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, ybase, delta, ysize))
    part2 = image.crop((delta, ybase, xsize, ysize))

    image.paste(part2, (0, ybase, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, ybase, xsize, ysize))

    return image

def interleave(image, resultImg, delta, x):#we use the roll function defined earlier to interleave the leftmost part into the rightmost part
    xsize, ysize = image.size
    for y in range(0, 30):
        # we crop the stripes we'll interleave.. and yes they are the same because they are on the same stripes, one is just 504 pixel to the side
        part1 = image.crop((0, y*8, xsize, y*8+8))
        part2 = image.crop((0, y*8, xsize, y*8+8))
        # we define the squares where we will put them. Keep in mind that at the moment it is not rolled. We'll have two squares that are the same
        ybase1 = y*16
        yend1 = ybase2 = y*16+8
        yend2 = y*16+16
        # now we paste it on the result image
        resultImg.paste(part1, (0, ybase1, xsize, yend1))
        resultImg.paste(part2, (0, ybase2, xsize, yend2))
        # and roll the stipe that is to the side.
        roll(resultImg, x, ybase2)


#first part where we roll the stripes of 8 px each
for y in range(0, 32):
    roll(i, 8 * y, y*8)

#now we interleave the stripes
interleave(i, result, 8, 504)

#rotate for a cleaner result
i2 = result.rotate(90, expand = True)
i2.save("result.jpg")
i2.show()
