import System.IO
import Data.Char (isDigit, digitToInt)
import Data.List (isPrefixOf, elemIndex)
import Data.List.Split (splitOn)

-- @ # $ % &
-- - + = * /
symbols = "@#$%&+-*/="
directions :: [(Int, Int)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

--check :: [String] -> [Bool]
-- check all the cells around current entry and check if there is a chaspecial character in there
-- -- first write it for one cell and apply it to the list in a separate function
-- --need to account for the errors that will come up, particularly when checking a cell along the borders, 
--
--
-- i wish I knew monads here. then I could use that to do the error  accounting. 
-- -- but now I'll prolly have to resort to just manually settainf if elses
--
--goinf from the list of bools to to a list of numbers
--map,lambdas, takewhiles and such, pattern matching!
-- partNums :: [[Bool]] -> [String] -> [Int]
-- takewhile isdigit, 
-- HOLY, COOL CONCEPT INCOMING: take the "derivative" of the [[bool]] list BOOM
-- operation :: Bool -> Bool -> Bool -> Bool   -- only considering non-boundary elements (because boundary elts should stay as they are)
-- operation a b c = b && ( a /= b || b /= c)  -- if T && boundary then T, otherwise F
-- boolDerivative:: [Bool] -> [Bool]   -- ooh, do I make it left der, right, or 2s?
-- boolDerivative (a:b:[]) = a:b:[]
-- boolDerivative (a:b:[c]) = a:(operation a b c):[c]
-- boolDerivative (a:b:cs) = a:boolDerivative((operation a b):cs) -- not do anything to a, not do anything to cs, if a F & b T then b T, aTbTbF, aFbFbF, aTbFbF
-- boolDerivative (a:b:c:ds) = a:(operation a b c):(boolDerivative b:c:ds)
-- ok so this list should return the boundaries of the numbers, so given the list I'l take 3 inputs? the character, whether it satisfies a bunch of conitions (isdigit, is surrounded by special characters, aand that might be it?),  which i might just make that a function actuallly, and then use the boundary list to... what will i do with that ahgain? i wanted to say just use takewhile but that just not work since ill be going through the list and then when i come across digits go through the list ,like  go adead, and thanks to this being haskell i probably wont mess with the latter inputs butmaybe ill make too many lists? 
-- -- ok wait, restart:going through the list, eicher using map or comprehensions, and using conditions like isdigit and the "is it near a special symbol" function ill create 
--
-- -- where was I? oh yeah, have the s the char, have a function that tells me this is a good digit, then I can, or rather i want / need to make a 
-- so much of who we are and what we become is a function of.... like, , ok, I like the deathmatch song,  but  but so much of what I like about it is in the lyrics and subjectmatter, wihch I was desperately lookinf for in songs at some point, but never found. now eventually I came across this nong, and leoved it, but looking at it objectively, it really do ok not that   it isn't so much of the type of music i lke. it's very poppy, very upbeat and all that. I would have loved it if
{-
FFFFTTTTFFFF
FFFFTFFTFFFF

TTTFFFFTTTTT
TFTFFFFTFFFT
  bT bF
aT F  F
aF T  F
== not (a or not b)
-}
isSymbol :: [String] -> Int -> Int -> Bool
isSymbol l i j = elem (l !! i !! j) symbols

-- symBool :: [String] -> [Bool]
-- symBool l = [isSymbol l i j | i <- [0..length l - 1], j <- [0..length (l !! i) - 1]]
-- all hail chatGPT, what I was trying to implement for hours done in seconds, and so elegantly to boot

isValidIndex :: [String] -> Int -> Int -> Bool
isValidIndex l i j =    i >= 0 && i < length l && j >= 0 && j < length (l !! i)

checkSurrounding :: [String] -> Int -> Int -> Bool
checkSurrounding l i j =
    any (\(dx, dy) -> isValidIndex l (i + dx) (j + dy) && isSymbol l (i + dx) (j + dy)) directions
    -- GENIUS! effectively just set a border of Falses around the actual list! fuckin beautiful!!!!
symBooList :: [String] -> [[Bool]]
symBooList l = [[checkSurrounding l i j | j <- [0..length (l !! i) - 1]] | i <- [0..length l - 1]]

{- sometihngelse l i j
    | i == 0 && j == 0  = 
    | i == length l && j == length head l   = True -}
demo = ["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."]
boolChar :: Bool -> Char
boolChar x = if x then 'T' else 'F'
boolString :: [Bool] -> String
boolString l = map boolChar l
sumo = map boolString $ symBooList demo

{- connectedDigitsToInts :: [String] -> [Int]
connectedDigitsToInts = map read . concatMap groupDigits

groupDigits :: String -> [String]
groupDigits [] = []
groupDigits (x:xs)
  | isDigit x = let (digits, rest) = span isDigit (x:xs)
                in concat digits : groupDigits rest
  | otherwise = [x] : groupDigits xs -}

main :: IO()
main = do
    handle <- openFile "demo3.txt" ReadMode
    contents <- hGetContents handle
    -- let answer = sum $ map gamePower $ lines contents
    putStrLn contents
    let grid = lines contents
    mapM_ putStrLn sumo         -- wtf is up with monads man
    hClose handle
