I=double(imread('bimage3.bmp')) / 255;

figure;
imshow(I); 
title('Source image');

PSF=fspecial('motion', 54, 65);
[J1, P1]=deconvblind(I, PSF);
figure;
imshow(J1);
title('Recovered image'); 