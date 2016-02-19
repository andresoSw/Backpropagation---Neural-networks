echo -n "Deme alfa: "
read alfa

#neuronas-alfa-tamano-numero de prueba-dataset
let x="2"
while [ $x -lt 11 ]
do
echo "$x - $alfa - my"
./generatenet3 my2000.txt $alfa $x > ./data/$x-$alfa-2000-1-my.txt &
./generatenet3 my2000.txt $alfa $x > ./data/$x-$alfa-2000-2-my.txt &
./generatenet3 my2000.txt $alfa $x > ./data/$x-$alfa-2000-3-my.txt &
./generatenet3 my2000.txt $alfa $x > ./data/$x-$alfa-2000-4-my.txt &
./generatenet3 my2000.txt $alfa $x > ./data/$x-$alfa-2000-5-my.txt &
wait
let x=($x+1)
done


let x="2"
while [ $x -lt 11 ]
do
echo "$x - $alfa - prof"
./generatenet3 datos_P1_RN_EM2016_n2000.txt $alfa $x > ./data/$x-$alfa-2000-1-prof.txt &
./generatenet3 datos_P1_RN_EM2016_n2000.txt $alfa $x > ./data/$x-$alfa-2000-2-prof.txt &
./generatenet3 datos_P1_RN_EM2016_n2000.txt $alfa $x > ./data/$x-$alfa-2000-3-prof.txt &
./generatenet3 datos_P1_RN_EM2016_n2000.txt $alfa $x > ./data/$x-$alfa-2000-4-prof.txt &
./generatenet3 datos_P1_RN_EM2016_n2000.txt $alfa $x > ./data/$x-$alfa-2000-5-prof.txt &
wait
let x=($x+1)
done
