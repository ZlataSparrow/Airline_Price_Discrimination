
Airline Price Discrimination Dataset – Variable Descriptions

This dataset combines information from the U.S. Department of Transportation’s DB1B Airline Origin and Destination Survey with supplemental airport-level data. Each observation represents a unique airline–route–quarter–year combination and includes ticket prices, passenger counts, carrier market shares, and geographic information for both origin and destination airports.

The dataset enables analysis of airline competition, market power, and pricing behavior — including studies of price discrimination, route dominance, and market concentration in U.S. domestic air travel markets.

Below is a detailed description of all variables included in the dataset.

⸻

origin — 3-letter airport code of the origin airport.
finaldest — 3-letter airport code of the final destination airport.
return — Indicator whether the itinerary is a round trip (1) or one-way (0).
year — Year of the ticket data (for example, 2011 or 2016).
quarter — Quarter of the year (1 to 4).
airports — String listing all airports in the itinerary (for example, DTW-MSP-DTW).
return_sym — Flag showing if the return route is symmetric (same path back).
stops — Number of stops on the route (0 = direct).
avgprice — Average ticket price for that route in U.S. dollars.
itinfare — Total fare paid for the itinerary.
passengers — Number of passengers on that route during the given period.

shareAA, shareDL, shareUA, shareWN, shareNK, shareB6, shareVX, etc. — Market share (proportion of passengers or tickets) of each airline on that route.
sharelargest — Market share of the largest carrier in the market (indicator of market dominance). This is the percentage of all passengers in a market who flew with the biggest airline in that market.If one airline carries most people, sharelargest is high. If passengers are split between many airlines, sharelargest is lower.
share16 — Combined share of the top 16 airlines (aggregate concentration measure).

treated — Indicator variable for whether the market is part of a treatment or policy group (used in experiments or causal inference models).
smallmkt — Indicator for small or low-volume markets.
code_O, code_D — Internal identifiers for origin and destination airports.
icao_O, icao_D — ICAO 4-letter codes for origin and destination airports.
airport_O1, airport_D1 — Alternative or cleaned airport identifiers after merging datasets.

latitude_O, longitude_O, elevation_O — Geographic coordinates and elevation of the origin airport.
latitude_D, longitude_D, elevation_D — Geographic coordinates and elevation of the destination airport.
time_zone_O, time_zone_D — Time zone of the origin and destination airports.
city_code_O, city_code_D — City codes for origin and destination airports.
city_O, city_D — City names for origin and destination airports.
state_O, state_D — State codes for origin and destination airports.
county_O, county_D — County names for origin and destination airports.
country_O, country_D — Country names for origin and destination airports.
type_O, type_D — Type of airport (commercial, regional, private, etc.).
name_O, name_D — Full names of origin and destination airports.
url_O, url_D — Reference URLs for the origin and destination airport data sources.

⸻

Dataset summary:

This dataset represents route-level and airport-level information for the U.S. domestic airline market. Each observation corresponds to a specific route–airline–quarter–year combination. It merges fare, passenger, and market-share data with detailed airport attributes such as location, elevation, time zone, and administrative codes. The dataset supports economic and data science analyses of airline pricing, competition, and consumer welfare.