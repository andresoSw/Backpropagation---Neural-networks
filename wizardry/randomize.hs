import System.Random
import System.Random.Shuffle

main = do
  input <- getContents
  g <- getStdGen
  let l = lines input
  putStr $ unlines $ reverse $ shuffle' l (length l) g