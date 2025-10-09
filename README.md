# ✈️ Airline Pricing & Competition Modeling

## Econometric modeling of airline fares, market structure, and price discrimination

In this project, I dig into how U.S. airlines actually price their tickets. Some routes have tons of competition. Others are basically monopolies. Some serve business travelers with corporate cards, others serve families hunting for deals. Airlines know all this — and they price accordingly.
I use data and econometrics to figure out what's really driving fares: competition, local income, how sensitive people are to price changes. Then I build models to predict prices and run simulations to see what would happen if market conditions changed.

⸻

### Key Objectives

1. Do airlines charge more in wealthy markets?
2. How does competition influence fares?
3. Can we detect third-degree price discrimination?

### Data

The Project is based on the Airline Origin and Destination Survey (DB1B) — a 10% sample of all U.S. airline tickets collected quarterly by the Bureau of Transportation Statistics (BTS), captures information about passenger itineraries, fares, carriers, and routes.

* Source: U.S. Department of Transportation, Bureau of Transportation Statistics — DB1B Dataset
* Years: 2011 and 2016
* Frequency: Quarterly (Q1–Q4)
* Size: ~3 million itineraries per quarter (≈500K route-level observations after aggregation)
* Granularity: Route × Carrier × Quarter

More about data can be found here: [README_Airlines_Tickets.txt](data/README_Airlines_Tickets.txt)

### Methods

* Econometric Modeling (OLS & interactions) — analyzes how prices respond to market conditions
* Elasticity & Markup Analysis — measures pricing power and demand sensitivity
* Counterfactual Simulations — tests “what-if” pricing under uniform competition
* Model Validation — ensures robustness via cross-validation, coefficient stability, and HC3 errors

### Key Outcomes

1. Wealthier and smaller markets pay higher fares, even on comparable routes
2. Competition lowers prices, but much less in rich or luxury destinations — demand is inelastic
3. Luxury routes (Aspen, Jackson Hole) show the strongest price insulation from competition
4. Elasticity-based markups confirm airlines exploit market segmentation (consistent with 3rd-degree price discrimination)
5. Counterfactual simulations show uniform competition would significantly reduce fares in premium markets

### What This Shows:

**How to model real-world pricing strategy using actual market data**
**Economic intuition paired with technical execution — elasticity, market power, competitive dynamics**
**The ability to move from regression output to actionable business insight**
**Clean, reproducible code that bridges data science and economics**

⸻

### Structure:
```
 AIRLINE_PRICE_DISCRIMINATION/
├── data/
│   ├── Airline_tickets_data.pkl               # Raw airline tickets data (loaded from G Drive)
│   ├── Airlines_tickets_data_EDA_ready.pkl    # Cleaned dataset used for EDA (loaded from G Drive)
│   ├── Airlines_tickets_data_ready.pkl        # Final modeling dataset (loaded from G Drive)
│   ├── Airports_data_raw_add.pkl              # Supplemental airport data (loaded from G Drive)
│   ├── Airports_data_raw.csv                  # Original airport-level dataset 
│   ├── README_AIRLINES_TICKETS_DATA.txt   # Airline Tickets Data documentation
│
├── notebooks/
│   ├── 01_Data_Prep.ipynb                     # Data cleaning, variable creation, feature engineering
│   ├── 02_EDA.ipynb                           # Exploratory analysis of competition, fares, and market structure
│   ├── 03_Market_Price_Discrimination.ipynb   # Econometric modeling, elasticity estimation, and counterfactual simulations
│
└── README.md                                  # Project documentation
```
