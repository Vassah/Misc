let rec fact a =
  if a <= 1 then 1 else a * fact ( a - 1);;