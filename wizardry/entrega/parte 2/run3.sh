echo -n "Deme alfa: "
read alfa

#neuronas-alfa-tamano-numero de prueba-dataset
let x="2"
while [ $x -lt 11 ]
do
echo "$x - $alfa - my"
./evalua ./data/$x-$alfa-2000-1-my.txt 10000.txt > test1.txt &
./evalua ./data/$x-$alfa-2000-2-my.txt 10000.txt > test2.txt &
./evalua ./data/$x-$alfa-2000-3-my.txt 10000.txt > test3.txt &
./evalua ./data/$x-$alfa-2000-4-my.txt 10000.txt > test4.txt &
./evalua ./data/$x-$alfa-2000-5-my.txt 10000.txt > test5.txt &
wait
octave dibujo.m test1.txt 10000.txt $x-$alfa-2000-1-my &
octave dibujo.m test2.txt 10000.txt $x-$alfa-2000-2-my &
octave dibujo.m test3.txt 10000.txt $x-$alfa-2000-3-my &
octave dibujo.m test4.txt 10000.txt $x-$alfa-2000-4-my &
octave dibujo.m test5.txt 10000.txt $x-$alfa-2000-5-my &
wait
let x=($x+1)
done


let x="2"
while [ $x -lt 11 ]
do
echo "$x - $alfa - prof"
./evalua ./data/$x-$alfa-2000-1-prof.txt 10000.txt > test1.txt &
./evalua ./data/$x-$alfa-2000-2-prof.txt 10000.txt > test2.txt &
./evalua ./data/$x-$alfa-2000-3-prof.txt 10000.txt > test3.txt &
./evalua ./data/$x-$alfa-2000-4-prof.txt 10000.txt > test4.txt &
./evalua ./data/$x-$alfa-2000-5-prof.txt 10000.txt > test5.txt &
wait
octave dibujo.m test1.txt 10000.txt $x-$alfa-2000-1-prof &
octave dibujo.m test2.txt 10000.txt $x-$alfa-2000-2-prof &
octave dibujo.m test3.txt 10000.txt $x-$alfa-2000-3-prof &
octave dibujo.m test4.txt 10000.txt $x-$alfa-2000-4-prof &
octave dibujo.m test5.txt 10000.txt $x-$alfa-2000-5-prof &
wait
let x=($x+1)
done

rm test*.txt
