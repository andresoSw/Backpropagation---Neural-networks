import System.Random
import System.Random.Shuffle
import System.Environment

main = do
  input <- getContents
  (x:_) <- getArgs
  g <- getStdGen
  let l = take 150 $ lines input
  putStr $ unlines $ take (read x) $ shuffle' l (length l) g
