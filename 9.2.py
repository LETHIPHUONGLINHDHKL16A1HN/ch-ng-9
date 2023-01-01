#tính năm âm lịch
def  tinh_can ( nam ):
      nếu  nam % 10  ==  0 :
            trả về  'Canh'
      elif  nam % 10 == 1 :
            trả lại  'Tân'
      elif  nam % 10 == 2 :
            trả về  'Nhâm'
      elif  nam % 10 == 3 :          
            trả lại  'Quý'
      elif  nam % 10 == 4 :
            return  'Giáp'
      elif  nam % 10 == 5 :
            trả về  'Ất'
      elif  nam % 10 == 6 :
            trả lại  'Bính'
      elif  nam % 10 == 7 :
            trở lại  'Đinh'
      yêu tinh  nam % 10 == 8 :
            trở lại  'Mậu'
      khác :
            return  'Ký'
def  tinh_chi ( nam ):
      nếu  nam % 12 == 0 :
            trả lại  'Thân'
      nếu  nam % 12 == 1 :
            trả lại  'Dậu'
      nếu  nam % 12 == 2 :
            return  'Tuất'
      nếu  nam % 12 == 3 :
            trả lại  'Hợi'
      nếu  nam % 12 == 4 :
            trả về  'Tý'
      nếu  nam % 12 == 5 :
            trở lại  'Sửu'
      nếu  nam % 12 == 6 :
            return  'Dần'
      nếu  nam % 12 == 7 :
            trở lại  'Mão'
      nếu  nam % 12 == 8 :
            return  'Thìn'
      nếu  nam % 12 == 9 :
            trở lại  'Tỵ'
      nếu  nam % 12 == 10 :
            return  'Ngọ'
      khác :
            trả lại  'Mùi'
x = int ( input ( 'Nhập năm:' ))
print ( 'Năm' , x , 'là năm:' , tinh_can ( x ), tinh_chi ( x ))