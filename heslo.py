import random

operace = [ "+", "-", ":", "*"]
nahodna_operace = random.choice (operace)
index = operace.index (nahodna_operace)
print(f"chci pouzit operaci{nahodna_operace} na indexu {index} v poli")