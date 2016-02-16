import NeuralNetwork
import System.Environment
import System.Random

test2 :: (Eq a) => [a] -> [a] -> Double
test2 x y = (foldl (\n b -> if b then n+1 else n) (0 :: Double) $ zipWith (==) x y)/(fromIntegral $ length y)

main = do
  g1 <- getStdGen
  let n1 = fromRandomList 2 [8,1] $ randomRs (0,0.5) g1
  (x:tasa:_) <- getArgs
  test <- readFile x
  let parce =  map (\y->(init y, [last y])) $ map (map read) $ map words $ lines test :: [([Double],[Double])]
  let parce2 = map (\x@(y,[g])->if g == -1 then (y,[0.0]) else x) parce
  let input = map fst parce2
  let out = map snd parce2
  let net = bp (read tasa) (n1) parce2
  let solved = map (\n->map (solve n) input) net :: [[[Double]]]
  let prog = map (\c->test2 c out) $ map (map (map (\x->if x>=(0.5 :: Double) then (1 :: Double) else (0 :: Double)))) $ solved
  let error = map (map (\x-> x/fromIntegral(length out))) $map (foldr (zipWith (+)) (repeat 0)) $ map (zipWith (zipWith (\x y -> (x-y)**2)) out) solved
  putStr $ unlines $ map (show) $ zip [0..] $ zipWith (\n r-> (n,r)) prog error -- $ zipWith (\n r-> (n,r)) error net
