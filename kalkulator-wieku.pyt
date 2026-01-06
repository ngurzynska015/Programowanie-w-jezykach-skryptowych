
from datetime import datetime

rok_urodzenia = 2008
biezacy_rok = datetime.now().year
wiek = biezacy_rok - rok_urodzenia

print(f"Rok urodzenia {rok_urodzenia}")
print(f"Bieżący rok {biezacy_rok}")
print(f"Wiek {wiek}")
