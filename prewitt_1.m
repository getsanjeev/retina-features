A = imread('einstein.jpg');
A = rgb2gray(A);
B = A ;
C = A ;
D = A ;
figure, imshow(B);
A = double(A);
rows = size(A,1);
coloumns = size(A,2);
for i = 2:1:rows-1
    for j = 2:1:coloumns-1
        B(i,j) = -1*A(i-1,j-1) + A(i-1,j+1) + -1*A(i,j-1) + A(i,j+1) + -1*A(i+1,j-1) + A(i+1,j+1);
    end
end

B = uint8(B);

for i = 2:1:rows-1
    for j = 2:1:coloumns-1
        C(i,j) = -1*A(i-1,j-1) + -1*A(i-1,j) + -1*A(i-1,j+1) + A(i+1,j-1) + A(i+1,j) + A(i+1,j+1);
    end
end

C = uint8(C);

D = B + C;
figure, imshow(D);

for i = 2:1:rows-1
    for j = 2:1:coloumns-1
       if(D(i,j) > 100)
           D(i,j) = 255;
       else
           D(i,j) = 0;
       end
    end
end
figure, imshow(D);