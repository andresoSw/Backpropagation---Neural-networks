apt-get install haskell-platform
cabal install random-shuffle-0.0.4
cabal install Matrix
ghc randomize.hs
use: ./randomize <input.file>

# generacion de n numero de casos
./genera 10

# randomize de los casos de prueba
./genera 10 | ./randomize

#genera todas las combinaciones de puntos para los pares x,y entre 0 y 20, con 0.2 de step
ghc steps.hs
./steps