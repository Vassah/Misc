main = interact wordCount
     where wordCount input = show (length (words (lines input))) ++ "\n"