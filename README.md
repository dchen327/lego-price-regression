# Lego Set Data
## All data scraped from brickset.com

# Notes
Theme grouped categories here: https://brickset.com/browse/sets

# Independent Variables (predicting price)
- piece count
- licensed vs unlicensed
- launch date
- age range
- number of minifigures
- packaging type
- length of instructions?

- themes? group by category?

# Questions
- licensed vs. unlicensed? (from grouped categories)

# API data pulling
- separate by date to get all data per page?
- get rid of GEAR (keychains/accessories), Duplo (pieces too big), Books (not Legos), Collectable Minifigures, Service Packs (motors, etc.)
- Drop where no price, no pieces
- Use min age only, set min age to 1 if not provided (1 datapoint)
- Replace NaNs in minifigs with 0
- Packaging category types: Box, Foil pack, Polybag, Blister pack, Other
  - grouped a lot of packaging types with low counts into Other
  
# STATA
- `reg retailPrice year pieces minifigs minAge Package_Box Package_Foil Package_Other
                         Package_Polybag`