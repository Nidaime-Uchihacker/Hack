#!/usr/bin/python

SAVEDIR = "/home/cam/NID"

import pygame, sys
import pygame.camera
import time, random

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (640,480))

while True:
   print "Taking a shot:",
   cam.start()
   image = cam.get_image()
   cam.stop()

   timestamp = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
   filename = "%s/%s.jpg" % (SAVEDIR, timestamp)
   print "saving into %s" % filename

   pygame.image.save(image, filename)
   time.sleep(random.randrange(10) * 60)
