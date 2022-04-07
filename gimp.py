def pixelise(x=100,y=100,n_colors=64):
  img=gimp.image_list()[0]
  pdb.gimp_image_scale(img,x,y)
  drw=pdb.gimp_image_active_drawable(img)
  if not(pdb.gimp_drawable_is_indexed(drw)):
    pdb.gimp_convert_indexed(img,0,0,n_colors,0,1,0)
  im=""
  pal=[]
  j = 0
  last = 0
  for i in range(x*y):
    v=list(pdb.gimp_image_pick_color(img,drw,i%x,i//x,1,0,0))[:-1]
    if v not in pal: pal.append(v)
    k = pal.index(v)
    if k==last and not n_colors - 2 + j>=255:
      j += 1
    else:
      if j==1:
        im+=chr(last)
      else:
        im+=chr(j + n_colors - 2)
        im+=chr(last)
      last = k
      j = 1
  if j==1:
    im+=chr(last)
  else:
    im+=chr(j + n_colors - 2)
    im+=chr(last)
  print("size = [%3s,%3s]" % (x,y))
  print("n_col =%3s" % (len(pal)))
  print("palette="+str(pal))
  print("s=")
  return im
