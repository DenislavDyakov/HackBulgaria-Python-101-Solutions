def iban_formatter(iban):
     result = []
     counter = 1

     for char in iban:
          if char == " ":
               continue

          result.append(char)

          if counter == 4:
               result.append(" ")
               counter = 0
          counter += 1

     return "".join(result)          


tests = [
     ("BG80BNBG96611020345678", "BG80 BNBG 9661 1020 3456 78"),
     ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
     ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
     ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54")
]

for iban, expected in tests:
     result = iban_formatter(iban)
     print(result == expected)
