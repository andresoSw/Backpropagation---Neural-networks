step bajo alto paso = [bajo,(bajo+paso)..alto]
replace _ _ [] = []
replace r y (x:xs)
  | r == x = y:(replace r y xs)
  | otherwise = x:(replace r y xs)

main = do
  let my100 = map (\x->x/10) $ step 2 200 2
  putStr $ unlines $ map (replace (',' :: Char) (' ' :: Char)) $ map (tail.init) $ map show $ (\x y -> (x,y)) <$> my100 <*> my100