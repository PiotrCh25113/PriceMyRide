# Price My Ride

**Price My Ride** is a Streamlit application designed to help users estimate the value of a vehicle based on historical data from 2015.

## Features

- **Vehicle Valuation**: Estimate price based on Make, Model, Body Type, Year, Trim, and Mileage.
- **Interactive Interface**: Simple dropdowns and input fields for easy data entry.
- **Instant Prediction**: Uses a pre-trained Machine Learning model to generate real-time estimates.
- **Automated Deployment**: Integrated GitHub Actions for Docker builds and Azure deployment updates.

## Project Structure

```text
PriceMyRide/
├── .github/
│   └── workflows/         # CI/CD configurations
├── models/
│   └── estimate_veh_price.joblib  # Trained estimation model
├── utils/
│   └── constants.py       # Lists for makes, models, bodies, trims
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
