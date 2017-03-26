clc;
close all;
a=imread('einstein.jpg');
b=im2double(a);
M=b;
L=b;
figure, imshow(b);
title('Original Image');
[m,n]=size(a);
for i=1:m-2
    for j=1:m-2
        L(i,j)=-1*b(i,j)+0+0+1*b(i+1,j+1);
    end
end
figure, imshow(L)
title('Robert    Gx');

for i=1:m-2
    for j=1:m-2
        M(i,j)=0-1*b(i,j+1)+1*b(i+1,j)+0;
    end
end
figure, imshow(M)
title('Robert    Gy')


N=M+L;
figure, imshow(N);
title('Robert    Gx+Gy');


