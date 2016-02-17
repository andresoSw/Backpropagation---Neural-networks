import System.Random
import System.Environment

isInCircle :: (Double,Double) -> Double -> (Double,Double) -> Bool
isInCircle (xc,yc) r (x,y) = (x - xc)**2 + (y - yc)**2 <= r**2

separa divisor x = (filter divisor x, filter (not.divisor) x)

generarPatrones (maxX,maxY) number divisor gen gen2 =
  (take number yes, take number nos)
  where
    coords = zip (randomRs (0,maxX) gen) (randomRs (0,maxY) gen2)
    (yes,nos) = separa divisor coords

main = do
  g1 <- getStdGen
  g2 <- newStdGen
  (x:_) <- getArgs
  let circle = isInCircle (10,10) 7
  let (yes,nos) = generarPatrones (20,20) (read x) circle g1 g2
  putStr $ unlines $ map (\(x,y) -> (show x) ++ " " ++ (show y) ++ " 1") yes
  putStr $ unlines $ map (\(x,y) -> (show x) ++ " " ++ (show y) ++ " -1") nos