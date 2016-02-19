ghc genera.hs
ghc generatenet3.hs
ghc randomize.hs
rm -f *.hi
rm -f *.o

#generando pruebas
./genera 250 | ./randomize > my500.txt
./genera 500 | ./randomize > my1000.txt
./genera 1000 | ./randomize > my2000.txt

#escogiendo mejor alfa con 10 neuronas
./generatenet3 my500.txt 0.01 10 > ./alfa/alfa0.01.txt &
./generatenet3 my500.txt 0.05 10 > ./alfa/alfa0.05.txt &
./generatenet3 my500.txt 0.1 10 > ./alfa/alfa0.1.txt &
./generatenet3 my500.txt 0.2 10 > ./alfa/alfa0.2.txt &
./generatenet3 my500.txt 0.3 10 > ./alfa/alfa0.3.txt &
./generatenet3 my500.txt 0.5 10 > ./alfa/alfa0.5.txt &

wait
echo "Elija un alfa y corra run2.sh"
