%yfile=input("Ingrese arvido con resultados.")
%xfile=input("Ingrese arvido con iniciales.")

arg_list = argv ();

figure
hold on
for a = 1:10

fid=fopen(arg_list{a})

i=0;
while ~feof(fid)
   i=i+1;
   [t c]=sscanf(fgetl(fid),"%f %f [%f]");
   if i<10001
   x(i,1)=t(3);
   end
end

if a<6
plot(0:9999,x,'b')
else
plot(0:9999,x,'r')
end

end

saveas(gcf,strcat("./img/",strcat(arg_list{11},"-error.png")));
