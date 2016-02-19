import NeuralNetwork
import System.Environment
import System.Random

isInCircle :: (Double,Double) -> Double -> (Double,Double) -> Bool
isInCircle (xc,yc) r (x,y) = (x - xc)**2 + (y - yc)**2 <= r**2

mycircle x y = if (isInCircle (10,10) 7 (x,y)) then 0 else 1

main = do
  (x:y:_) <- getArgs
  redtext <- readFile x >>= \x -> return (last $ lines x)
  let net = fromList $ read redtext :: NN Double
  casestxt <- readFile y
  let cases = map (map read) $ map words $ lines casestxt
  putStr $ unlines $ map unwords $ map (map show) $ map (solve net) cases

