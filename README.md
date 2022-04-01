# Lego Set Data
## All data scraped from brickset.com

# Notes
Theme grouped categories here: https://brickset.com/browse/sets
- In total this data took around 10 hours to get and parse, because of annoyances
in pulling from the API, cleaning, and organizing into pandas

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
  - dummy variables for everything except box (n-1 dummy variables for n categories)
  
# STATA
- ` reg retailPrice year pieces minifigs minAge Package_Foil Package_Polybag Package_Other`