import System.IO
import Data.Char (isDigit, digitToInt)
import Data.List (isPrefixOf, elemIndex)
import Data.List.Split (splitOn)


sample = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

separators :: Char -> Bool
separators a = a == ';' || a == ':'

parse1 :: String -> String
parse1 [] = []
parse1 (l:ls) = if separators l then [] else l:parse1 ls
parse2 :: String -> [String]
parse2 [] = [[]]
parse2 (l:ls) = if separators l then [[],ls] else [l:((parse2 ls) !! 0),((parse2 ls) !! 1)]
-- parse3 :: [String] -> [String]
-- parse3 [[]] = [[]]
-- parse3 ((l:ls):ws) = if separators l then [[],ls,ws] else [l:((parse2 ls) !! 0),((parse2 ls) !! 1),ws]
-- listID ls = map digitToInt $ stringID ls
splitID :: String -> [String]
splitID ls = splitOn ": " ls
splitSamples :: String -> [String]
splitSamples ls = splitOn "; " ls
splitColors :: String -> [String]
splitColors ls = splitOn ", " ls
splitQuant :: String -> [String]
splitQuant ls = splitOn " " ls

ccolorToVec :: [String] -> (Int, Int, Int)
ccolorToVec (l:ls)
    | l == "red"    = (read (head ls), 0, 0)
    | l == "green"  = (0, read (head ls), 0)
    | l == "blue"   = (0, 0, read (head ls))
colorToVec :: [String] -> (Int, Int, Int)
colorToVec = ccolorToVec . reverse

quantToVec = colorToVec . splitQuant

vecSum :: (Int, Int, Int) -> (Int, Int, Int) -> (Int, Int, Int)
vecSum (a, b, c) (x, y, z) = (a+x, b+y, c+z)
vlSum :: [(Int, Int, Int)] -> (Int, Int, Int)
vlSum [v] = v
vlSum [v,w] = vecSum v w
vlSum (v:vs) = vecSum v $ vlSum vs

samplesToVecs ls = map vlSum $ map (map quantToVec) $ map splitColors $ splitSamples ls

vecMax :: (Int, Int, Int) -> (Int, Int, Int) -> (Int, Int, Int)
vecMax (a, b, c) (x, y, z) = (max a x, max b y, max c z)
vlMax :: [(Int, Int, Int)] -> (Int, Int, Int)
vlMax [v] = v
vlMax [v,w] = vecMax v w
vlMax (v:vs) = vecMax v $ vlMax vs

samplesToTheMax ls = vlMax $ samplesToVecs ls

getID :: String -> Int
getID ls = read $ dropWhile (not . isDigit) ls

gamesToMax (a:b:[]) = (getID a, samplesToTheMax b)
gamesToMax' = gamesToMax . splitID

bagContents = (12,13,14)
possible :: (Int, Int, Int) -> (Int, Int, Int) -> Bool
possible (a,b,c) (x,y,z) = a >= x && b >= y && c >= z

possibleIDs :: (Int, (Int,Int,Int)) -> Int
possibleIDs (id, vec) = if (possible bagContents vec) then id else 0

possibleGame = possibleIDs . gamesToMax' 

power :: (Int, Int, Int) -> Int
power (a,b,c) = a*b*c
outPower (a, v) = power v
gamePower = outPower . gamesToMax'

main :: IO()
main = do
    handle <- openFile "input2.txt" ReadMode
    contents <- hGetContents handle
    -- putStrLn contents
    -- let answer = sum $ map possibleGame $ lines contents
    let answer = sum $ map gamePower $ lines contents
    print answer
    hClose handle
