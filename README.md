# ✈️ Airline Pricing & Competition Modeling

## Econometric modeling of airline fares, market structure, and price discrimination
This project investigates how airlines adjust fares across different markets to uncover evidence of price discrimination and market power.

⸻

### Key Objectives

1. Do airlines charge more in wealthy markets?
2. How does competition influence fares?
3. Can we detect third-degree price discrimination?

### Methods

* Econometric Modeling (OLS & interactions) — analyzes how prices respond to market conditions
* Elasticity & Markup Analysis — measures pricing power and demand sensitivity
* Counterfactual Simulations — tests “what-if” pricing under uniform competition
* Model Validation — ensures robustness via cross-validation, coefficient stability, and HC3 errors

### Data

The Project is based on the Airline Origin and Destination Survey (DB1B) — a 10% sample of all U.S. airline tickets collected quarterly by the Bureau of Transportation Statistics (BTS), captures information about passenger itineraries, fares, carriers, and routes.

* Source: U.S. Department of Transportation, Bureau of Transportation Statistics — DB1B Dataset
* Years: 2011 and 2016
* Frequency: Quarterly (Q1–Q4)
* Size: ~3 million itineraries per quarter (≈500K route-level observations after aggregation)
* Granularity: Route × Carrier × Quarter


### Key Outcomes:

1. Wealthier and smaller markets pay higher fares, even on comparable routes
2. Competition lowers prices, but much less in rich or luxury destinations — demand is inelastic
3. Luxury routes (Aspen, Jackson Hole) show the strongest price insulation from competition
4. Elasticity-based markups confirm airlines exploit market segmentation (consistent with 3rd-degree price discrimination)
5. Counterfactual simulations show uniform competition would significantly reduce fares in premium markets

⸻

### What  Shows:

* Real-world pricing analytics and market modeling
* Strong grasp of econometric inference and elasticity analysis
* Ability to translate models into business-relevant insights
* Reproducible, production-ready data science workflow


### Structure:
```
 AIRLINE_PRICE_DISCRIMINATION/
├── data/
│   ├── Airline_tickets_data.pkl               # Raw airline tickets data (loaded from G Drive)
│   ├── Airlines_tickets_data_EDA_ready.pkl    # Cleaned dataset used for EDA (loaded from G Drive)
│   ├── Airlines_tickets_data_ready.pkl        # Final modeling dataset (loaded from G Drive)
│   ├── Airports_data_raw_add.pkl              # Supplemental airport data (loaded from G Drive)
│   ├── Airports_data_raw.csv                  # Original airport-level dataset 
│   ├── README_AIRLINES_TICKETS_DATA.txt.txt   # Airline Tickets Data documentation
│
├── notebooks/
│   ├── 01_Data_Prep.ipynb                     # Data cleaning, variable creation, feature engineering
│   ├── 02_EDA.ipynb                           # Exploratory analysis of competition, fares, and market structure
│   ├── 03_Pricing_Rich_Markets.ipynb          # Econometric modeling, elasticity estimation, and counterfactual simulations
│
└── README.md                                  # Project documentation
```
