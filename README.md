# Ocean Protocol :: ETH Prediction Challenge

## Files description

- 1_get_predictions.ipynb - code for the ETH predictions generation. 
- 2_upload_predictions1.py - code for publishing predictions online, to private url.
- 2_upload_predictions2.py - code for sharing predictions actual, to judges via Polygon.
- 3_models_testing.ipynb - code with evaluating of different algorithms.
- Ocean_Presentation.pdf - final solution presentation.
- startup.py - initial script executed in every notebook when started.

## Challenge
Contestants are requested to submit the following:
1. Csv with the  predictions for ETH price over a 24-hour period, with first prediction on  from Mon Oct 17, 2022 at 1:00am UTC, and a prediction every hour on the hour after that, for 24 predictions total.
2. A report of 10-30 slides describing your approach, and insights you gained in making the predictions. Think of this as a “conference presentation” for your work.
3. Optional: add at least one slide presenting any challenges faced during the bounty and/or recommendations you may have.

(1) must be submitted as its own dataset in Ocean. The specific instructions are in the README (below).

## Challenge Datasets & Data Feeds
You can download the dataset from here: https://cexa.oceanprotocol.io/ohlc?exchange=binance&pair=ETH/USDT&period=1h   
This data feed returns ETH/USDT ohlc history: {open, high, low, close) over time, drawn from Binance.
It's over the most recent 500 hours: every hour, on the hour.

You can access pre-provided data through this README: https://bit.ly/3LFc5XP
