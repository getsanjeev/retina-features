disp('Linear Regression Model');
%n = input('Enter the no of features in your model: ');
N = 2;
X = zeros(1,N);
THETA = zeros(2,1);
para1 = [1 2 4 4 5 6 7 8 9 10];
para2 = [1 2 4 4 5 6 7 8 9 10 ];
result = [2 4 8 8 10 12 14 16 18 20];
k = 0;
temp1 = 0;
temp2 = 0;
    for b = 1:10
        k = k+1;
        %disp({para1(k),para2(k)});
        H = THETA'*[para1(k); para2(k)]; 
        disp({'H:',H});
        temp1 = temp1 + ((0.001)/10)*((H-result(k))*para1(b));
        temp2 = temp2 + ((0.001)/10)*((H-result(k))*para2(b));
        disp({'temp1:', temp1, 'temp2:',temp2});
        THETA(1) = THETA(1)-temp1;
        THETA(2) = THETA(2)-temp2;
        disp({THETA(1),THETA(2)});
    end



