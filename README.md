# ImageNumworks
<h3>Dessine n’importe quelle image sur la calculatrice!!</h3>
<p>Pour cela:</p>
<ol>
<li>Ouvrez votre image avec Gimp et ouvrez la console python-fu (Filtres &gt; Python - Fu &gt; Console)</li>
<li>Copiez-collez ce programme dans la console:<br>
<pre>def pixelise(x=100,y=100,n_colors=64):
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
    if k==last and not n_colors - 2 + j&gt;=255:
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
  return im</pre> <br>
Puis appuyez 2 fois sur Entrée pour que s'affiche les <code>&gt;&gt;&gt;</code> qui signifient que vous pouvez entrer une instruction</li>
<li>Exécutez la fonction  en rentrant en paramètres les dimensions de l'image et le nombre de couleurs. Par exemple<br>
<code>&gt;&gt;&gt; pixelise(100,100,64)</code><br>
<b>Protip:</b> Privilégiez le nombre de pixels au nombre de couleurs, ce sera plus joli</li>
<li>Remplacez dans le programme, de <code>size =</code>  (inclus) jusqu'à <code>r=</code> (exclus), attention cependant à enlever le retour à la ligne juste après <code>s=</code>
</li>
<li>Importez-le sur votre calculatrice!<br>
<i>Vous pouvez changer la taille de l'image en changeant la valeur de r (attention cependant à la laisser entière)</i>
</li>
</ol>
