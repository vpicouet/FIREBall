PRO collapseit


;    HISTORY: 
;               N. Lingner, March 2011

;    PURPOSE:   Combine images to find median 
;               

;             Desktop/Caltech/ISTOS_Spring2011/data/110131

;             How many images? What are the image-numbers... (fill in n-times)




    many = 10
 im_sz_x = 1072  ; x size of the array (top right corner)
 im_sz_y = 1072  ; y size of the array (top right corner)

 comb0 = fltarr(im_sz_x, im_sz_y, many)

 for i=705,714 do comb0[*,*,714-i] =  mrdfits('image0'+trim(string(i))+'.fits',0,hdr,/unsigned,/silent)              


   MEDARR,comb0,Median0
    
   roi  = Median0[630:860,540:1040]
   pre  = Median0[10:560,540:1040]
   post = Median0[1120:1500,540:1040]
   
   med_roi  = median(roi)
   med_pre  = median(pre)
   med_post = median(post)
   
   print, "At around -65C"
   print, "Median of the Image Area:     "+ string(med_roi)
   print, "Median of the Pre-Scan Area:  "+ string(med_pre)
   print, "Median of the Post-Scan Area: "+ string(med_post)
   print," "
   
   mwrfits,Median0,'Averaged0.fits',[hdr],/create,/bscale,/silent
   
STOP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;   


 comb1 = fltarr(im_sz_x, im_sz_y, many)

 for i=235,264 do comb1[*,*,264-i] =  mrdfits('image0'+trim(string(i))+'.fits',0,hdr,/unsigned,/silent)              


   MEDARR,comb1,Median1
    
   roi  = Median1[630:860,540:740]
   pre  = Median1[10:560,540:740]
   post = Median1[1100:1500,540:1040]
   
   med_roi  = median(roi)
   med_pre  = median(pre)
   med_post = median(post)

   print, "At around -122C"   
   print, "Median of the Image Area:     "+ string(med_roi)
   print, "Median of the Pre-Scan Area:  "+ string(med_pre)
   print, "Median of the Post-Scan Area: "+ string(med_post)
   print, ""
      
   ;mwrfits,Median1,'Averaged1.fits',[hd],/create,/bscale,/silent
   
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;   

    many = 30
 im_sz_x = 1503  ; x size of the array (top right corner)
 im_sz_y = 1200  ; y size of the array (top right corner)

 comb2 = fltarr(im_sz_x, im_sz_y, many)

 for i=265,294 do comb2[*,*,294-i] =  mrdfits('image0'+trim(string(i))+'.fits',0,hdr,/unsigned,/silent)              


   MEDARR,comb2,Median2
    
   roi  = Median2[630:860,540:740]
   pre  = Median2[10:560,540:740]
   post = Median2[1100:1500,540:1040]
   
   med_roi  = median(roi)
   med_pre  = median(pre)
   med_post = median(post)

   print, "At -122C"   
   print, "Median of the Image Area:     "+ string(med_roi)
   print, "Median of the Pre-Scan Area:  "+ string(med_pre)
   print, "Median of the Post-Scan Area: "+ string(med_post)
   print, " "
      
   ;mwrfits,Median2,'Averaged2.fits',[hd],/create,/bscale,/silent

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;   

    many = 30
 im_sz_x = 1503  ; x size of the array (top right corner)
 im_sz_y = 1200  ; y size of the array (top right corner)

 comb3 = fltarr(im_sz_x, im_sz_y, many)

 for i=295, 324 do comb3[*,*,324-i] =  mrdfits('image0'+trim(string(i))+'.fits',0,hdr,/unsigned,/silent)              


   MEDARR,comb3,Median3
    
   roi  = Median3[630:860,540:740]
   pre  = Median3[10:560,540:740]
   post = Median3[1100:1500,540:1040]
   
   med_roi  = median(roi)
   med_pre  = median(pre)
   med_post = median(post)

   print, "At around -119.3C"   
   print, "Median of the Image Area:     "+ string(med_roi)
   print, "Median of the Pre-Scan Area:  "+ string(med_pre)
   print, "Median of the Post-Scan Area: "+ string(med_post)
   print, " "
      
   ;mwrfits,Median3,'Averaged3.fits',[hd],/create,/bscale,/silent
   
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;   

    many = 30
 im_sz_x = 1503  ; x size of the array (top right corner)
 im_sz_y = 1200  ; y size of the array (top right corner)

 comb4 = fltarr(im_sz_x, im_sz_y, many)

 for i=325,354 do comb4[*,*,354-i] =  mrdfits('image0'+trim(string(i))+'.fits',0,hdr,/unsigned,/silent)              


   MEDARR,comb4,Median4
    
   roi  = Median4[630:860,540:740]
   pre  = Median4[10:560,540:740]
   post = Median4[1100:1500,540:1040]
   
   med_roi  = median(roi)
   med_pre  = median(pre)
   med_post = median(post)

   print, "At -119.3C"   
   print, "Median of the Image Area:     "+ string(med_roi)
   print, "Median of the Pre-Scan Area:  "+ string(med_pre)
   print, "Median of the Post-Scan Area: "+ string(med_post)
   print, " "
      
   mwrfits,Median4,'Averaged4.fits',[hd],/create,/bscale,/silent

 ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;   

    many = 30
 im_sz_x = 1503  ; x size of the array (top right corner)
 im_sz_y = 1200  ; y size of the array (top right corner)

 comb5 = fltarr(im_sz_x, im_sz_y, many)

 for i=385,414 do comb5[*,*,414-i] =  mrdfits('image0'+trim(string(i))+'.fits',0,hdr,/unsigned,/silent)              


   MEDARR,comb5,Median5
    
   roi  = Median5[630:860,540:740]
   pre  = Median5[10:560,540:740]
   post = Median5[1100:1500,540:1040]
   
   med_roi  = median(roi)
   med_pre  = median(pre)
   med_post = median(post)

   print, "At -119C"   
   print, "Median of the Image Area:     "+ string(med_roi)
   print, "Median of the Pre-Scan Area:  "+ string(med_pre)
   print, "Median of the Post-Scan Area: "+ string(med_post)
   print, " "
      
   ;mwrfits,Median5,'Averaged5.fits',[hd],/create,/bscale,/silent
   
END   
    
