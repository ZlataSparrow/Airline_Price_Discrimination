## ✈️ Airline Pricing & Competition Modeling

### Econometric modeling of airline fares, market structure, and price discrimination

This project models how U.S. airlines adjust fares across markets with different levels of competition, income, and demand elasticity — uncovering clear evidence of third-degree price discrimination. Using econometric and simulation methods, I quantify how pricing power shifts across rich vs. non-rich, small vs. large, and luxury vs. standard destinations.

⸻

### Key Outcomes:

1. Wealthier and smaller markets pay higher fares, even on comparable routes
2. Competition lowers prices, but much less in rich or luxury destinations — demand is inelastic
3. Luxury routes (Aspen, Jackson Hole) show the strongest price insulation from competition
4. Elasticity-based markups confirm airlines exploit market segmentation (consistent with 3rd-degree price discrimination)
5. Counterfactual simulations show uniform competition would significantly reduce fares in premium markets

⸻

### Methods:

* Econometric Modeling (OLS and Interactions) — tested price sensitivity across markets
* Elasticity & Markup Estimation — derived competitive pricing power
* Counterfactual Simulations — modeled uniform competition to assess pricing outcomes
* Validation: cross-validation, coefficient stability, and HC3 heteroskedasticity-consistent standard error

### What is Shows:

* Real-world pricing analytics and market modeling
* Strong grasp of econometric inference and elasticity analysis
* Ability to translate models into business-relevant insights
* Reproducible, production-ready data science workflow


### Structure:

📦 AIRLINE_PRICE_DISCRIMINATION/
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