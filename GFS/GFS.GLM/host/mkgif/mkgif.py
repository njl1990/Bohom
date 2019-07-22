#-*- coding: UTF-8 -*-
import imageio
import os
def create_gif(image_list, gif_name):
  frames = []
  for image_name in image_list:
    frames.append(imageio.imread(image_name))
  # Save them as frames into a gif
  imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)
  return

def main():
  
  path = '/images'
  dirs = os.listdir(path)
  image_list=[]
  i=0
  max=300
  iterage=3
  while i<max:
    image_list.append('image_'+str(i)+'.jpg')
    i=i+3
    #image_list.append('/images/'+name)
  gif_name = 'create.gif'
  #gif_name = '/gif/create.gif'
  create_gif(image_list, gif_name)
if __name__ == "__main__":
  main()

