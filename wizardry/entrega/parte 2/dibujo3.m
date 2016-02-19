%yfile=input("Ingrese arvido con resultados.")
%xfile=input("Ingrese arvido con iniciales.")

arg_list = argv ();

figure
hold on

[tam _]=size(arg_list)
cstring='rgbcmyk'

for a = 1:tam-1

fid=fopen(arg_list{a})

i=0;
while ~feof(fid)
   i=i+1;
   [t c]=sscanf(fgetl(fid),"%f %f [%f]");
   if i<10001
   x(i,1)=t(3);
   end
end

plot(0:9999,x,cstring(mod(a,7)+1))

end

saveas(gcf,strcat("./img/",strcat(arg_list{tam},"-error.png")));
