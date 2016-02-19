echo -n "Deme alfa: "
read alfa

#neuronas-alfa-tamano-numero de prueba-dataset
let x="2"
while [ $x -lt 11 ]
do
echo "$x - $alfa - my"

octave dibujo2.m ./data/$x-$alfa-2000-*-*.txt $x-$alfa-2000
let x=($x+1)
done
