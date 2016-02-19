ghc generatenet3.hs
ghc generatenet3-2.hs
ghc randomize.hs
rm -f *.hi
rm -f *.o

#generando pruebas
./randomize 75 < iris.data > iris50.txt
./randomize 90 < iris.data > iris60.txt
./randomize 105 < iris.data > iris70.txt
./randomize 120 < iris.data > iris80.txt
./randomize 135 < iris.data > iris90.txt

echo -n "Deme alfa: "
read alfa

#neuronas-alfa-tamano-numero de prueba-dataset
let x="4"
while [ $x -lt 11 ]
do
echo "$x - $alfa - setosa"
./generatenet3 iris50.txt $alfa $x > ./data/1-$x-$alfa-50.txt &
./generatenet3 iris60.txt $alfa $x > ./data/1-$x-$alfa-60.txt &
./generatenet3 iris70.txt $alfa $x > ./data/1-$x-$alfa-70.txt &
./generatenet3 iris80.txt $alfa $x > ./data/1-$x-$alfa-80.txt &
./generatenet3 iris90.txt $alfa $x > ./data/1-$x-$alfa-90.txt &
wait
let x=($x+1)
done

#neuronas-alfa-tamano-numero de prueba-dataset
let x="4"
while [ $x -lt 11 ]
do
echo "$x - $alfa - todas contra todas"
./generatenet3-2 iris50.txt $alfa $x > ./data/2-$x-$alfa-50.txt &
./generatenet3-2 iris60.txt $alfa $x > ./data/2-$x-$alfa-60.txt &
./generatenet3-2 iris70.txt $alfa $x > ./data/2-$x-$alfa-70.txt &
./generatenet3-2 iris80.txt $alfa $x > ./data/2-$x-$alfa-80.txt &
./generatenet3-2 iris90.txt $alfa $x > ./data/2-$x-$alfa-90.txt &
wait
let x=($x+1)
done

rm iris*.txt
rm generatenet3
rm generatenet3-2
rm randomize
