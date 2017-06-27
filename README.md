#make picture more green and fuzzy
##USAGE
Usage: python green.py source_pic [option]
-h or --help: show this usage
-r or --resize: resize the picture. Default: (0, 0) not resize. Format:(h, w) 
-c or --compress: compress picture. Default: 30. Format:(0, 100]
-g or --green: make picture more green times. Default: 20. Format: [0, oo)
-s or --save: location save the work. Default: Script path and named green+filename. Format: Full path.
##DEPEND ON
numpy+mkl
pillow
scipy(depend on numpy+mkl)
