%yfile=input("Ingrese arvido con resultados.")
%xfile=input("Ingrese arvido con iniciales.")

arg_list = argv ();
yfile = arg_list{1};
xfile = arg_list{2};
name = arg_list{3};

fid=fopen(yfile) %# open the file for reading

%#Loop through the file reading one line at a time
i=0;
while ~feof(fid)
   i=i+1;
   y(i,1)=str2num(fgetl(fid));
end

fid=fopen(xfile) %# open the file for reading

%#Loop through the file reading one line at a time
i=0;
while ~feof(fid)
   i=i+1;
   [t c]=sscanf(fgetl(fid),"%f %f");
   x(i,1)=t(1);
   x(i,2)=t(2);
end

c = 1;
for i = 1:100
for j = 1:100
z(i,j) = y(c,1);
c=c+1;
end
end

figure;
imagesc(x(1:100,2),x(1:100,2),z); 
saveas(gcf,strcat("./img/",strcat(name,"-2D-real.png")));
figure;
surf(x(1:100,2),x(1:100,2),z); 
saveas(gcf,strcat("./img/",strcat(name,"-3D-real.png")));

for i = 1:100
for j = 1:100
if (z(i,j) >= 0.5)
 zz(i,j) = 1;
else
 zz(i,j) = 0;
end
end
end

figure;
imagesc(x(1:100,2),x(1:100,2),zz); 
saveas(gcf,strcat("./img/",strcat(name,"-2D-dis.png")));
figure;
surf(x(1:100,2),x(1:100,2),zz); 
saveas(gcf,strcat("./img/",strcat(name,"-3D-dis.png")));
