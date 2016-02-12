import qualified Data.Matrix as A
import NeuralNetwork

x = (A.matrix 1 1 $ (\(i,_)->fromIntegral i)) :: A.Matrix Double

test = [([1,2,3],[sigmoid 6]),([-4,-5,-6],[sigmoid (-15)]),([7,8,9],[sigmoid 24]),([0,0,0],[sigmoid 0])] :: [([Double],[Double])]
testnet = empty 3 [3,1] :: NN Double
xx = A.matrix 3 1 (\(i,_)->fromIntegral (i+6)) :: A.Matrix Double
new = bp 0.5 testnet test (\_->False) 10000

testnet2 = empty 3 [3,2,3,1] :: NN Double
new2 = bp 0.5 testnet2 test (\_->False) 10000

yy = A.matrix 3 1 (\(i,_)-> -1 * fromIntegral (i+3)) :: A.Matrix Double
zz = A.matrix 3 1 (\(i,_)-> fromIntegral 0) :: A.Matrix Double

mysum = fromList [[[0,0.5],[0,0.5]],[[0,1,1]]] :: NN Double

mysum2 = fromList [[[1,1]]] :: NN Double

ex = fromList [[[0.35,0.15,0.20],[0.35,0.25,0.30]],[[0.6,0.4,0.45],[0.6,0.5,0.55]]] :: NN Double
exin = [0.05,0.1]

main = do
  putStrLn $ show $ solve' new xx
  putStrLn $ show $ solve' new2 xx
  putStrLn $ show $ solve' new yy
  putStrLn $ show $ solve' new2 yy
  putStrLn $ show $ solve' new zz
  putStrLn $ show $ solve' new2 zz