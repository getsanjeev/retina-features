A = imread('cube.jpg');
figure, imshow(A);

C = double(zeros(size(A,1),size(A,2)));
B = C;
D = C;
F = A;
% SHOWING A BINARY IMAGE IN SIMPLE FORM.
for i = 2:1:size(A,1)-1
    for j = 2:1:size(A,2)-1
        if(A(i,j)>128)
            B(i,j) = 255;
        else
            B(i,j) = 0;
        end
    end
end
figure, imshow(B);

% FLOYD STEINBERG ALGORITHM
A = double(A);
for i = 2:1:size(A,1)-1
    for j = 2:1:size(A,2)-1
        if(A(i,j) > 128)            
            C(i,j) = 255;
        else
            C(i,j) = 0;            
        end
            err = double(A(i,j) - C(i,j));            
            A(i,j+1) = A(i,j+1) + (7/16)*err;
            A(i+1,j-1) = A(i+1,j-1) + (3/16)*err;
            A(i+1,j) = A(i+1,j) + (5/16)*err;
            A(i+1,j+1) = A(i+1,j+1) + (1/16)*err;
    end
end
C = uint8(C);
figure, imshow(C);

% JARVIS JUDICE NINKE ALGORITHM

F = double(F);
for i = 2:1:size(F,1)-1
    for j = 2:1:size(F,2)-1
        if(F(i,j) > 128)            
            D(i,j) = 255;
        else
            D(i,j) = 0;            
        end
            err = double(F(i,j) - C(i,j));            
            F(i,j+1) = F(i,j+1) + (7/16)*err;
            F(i+1,j-1) = F(i+1,j-1) + (3/16)*err;
            F(i+1,j) = F(i+1,j) + (5/16)*err;
            F(i+1,j+1) = F(i+1,j+1) + (1/16)*err;
    end
end
D = uint8(D);
figure, imshow(D);



% C(i,j) = 0.299*red_1(i,j) + 0.587*green_1(i,j) + 0.114*blue_1(i,j);  

