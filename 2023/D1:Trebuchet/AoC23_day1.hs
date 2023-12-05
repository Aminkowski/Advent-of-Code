import System.IO
import Data.Char (isDigit, digitToInt)
import Data.List (isPrefixOf, elemIndex)
import Data.Maybe (fromMaybe, fromJust)


sam = ['s', 'a', 'm', '3', 'p', '4', 'l', 'e']
fnum :: [Char] -> Int
fnum [x] = digitToInt x
-- fnum (x:xs) = if (isDigit x) then x else fnum xs
fnum (x:xs) 
    | isDigit x         = digitToInt x 
    | wordCond (x:xs)   = wordToNum (x:xs)
    | otherwise         = fnum xs

lnum :: [Char] -> Int
-- lnum xs = fnum $ reverse xs
lnum [x] = digitToInt x
lnum xs 
    | isDigit (last xs)         = digitToInt $ last xs
    | rwordCond (reverse xs)    = rwordToNum $ reverse xs
    | otherwise                 = lnum $ init xs


numsSpelled = ["one", "two", "three", "four", 
    "five", "six", "seven", "eight", "nine"]

example = "fivelittlepiggies"
startsWithWord :: String -> [Bool]
startsWithWord line = map (flip isPrefixOf line) numsSpelled

wordCond :: String -> Bool
wordCond line = or $ startsWithWord line

wordToNum :: String -> Int
wordToNum line = succ $ fromJust $ elemIndex True $ startsWithWord line

numsSpelledRev = map reverse numsSpelled

rstartsWithWord :: String -> [Bool]
rstartsWithWord line = map (flip isPrefixOf line) numsSpelledRev

rwordCond :: String -> Bool
rwordCond line = or $ rstartsWithWord line

rwordToNum :: String -> Int
rwordToNum line = succ $ fromJust $ elemIndex True $ rstartsWithWord line


calibrationValue :: String -> Int
calibrationValue line = (fnum line) * 10 + (lnum line)

main :: IO()
main = do
    handle <- openFile "AoC23_input1.txt" ReadMode
    contents <- hGetContents handle
    let calibrationValues = map calibrationValue (lines contents)
    print $ sum calibrationValues
    hClose handle
