import imageio
import urllib.request
import cv2
from time import sleep
from sys import argv

fname = "num_1.gif"
frame = int(argv[1])

## Read the gif from disk to `RGB`s using `imageio.miread` 
gif = imageio.mimread(fname)
nums = len(gif)
print(f"Working on frame {frame}")

# convert form RGB to BGR 
imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]
img = imgs[frame]



points = []


def p_loc(event, x, y, flags, param):
    global img
    c = False
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(x, y)
        c = True
    if event == cv2.EVENT_RBUTTONDOWN:
        points.pop()
        c = True

    if c:
        img = imgs[frame]
        pts = points.copy()
        while len(pts) > 1:
            img = cv2.line(img, pts[0], pts[1], (0, 255, 0), 2)
            pts.pop(0)


cv2.namedWindow('gif')

cv2.setMouseCallback('gif', p_loc)

while True:
    
    cv2.imshow("gif", img)
    if cv2.waitKey(100)&0xFF == ord('q'):
        break


with open(f"points/f{frame}.py", "w") as f:
    f.write(f"frame_{frame} = [\n")
    for x, y in points:
        f.write(f"({x}, {y}),\n")
    f.write("]")


cv2.destroyAllWindows()
