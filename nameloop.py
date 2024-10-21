for x in range(1,51):
  if x < 10:
    nameval = '00' + str(x)
  else:
    nameval = '0' + str(x)
  #print(nameval)
  print('pdftoppm -jpeg projects/publishing/ctr/ctr' + nameval + '/fullcover_' + nameval + '_front.pdf converted/fullcover_' + nameval + '-front')
  print('pdftoppm -jpeg projects/publishing/ctr/ctr' + nameval + '/fullcover_' + nameval + '_rear.pdf converted/fullcover_' + nameval + '-rear')
