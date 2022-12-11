# Ocean Data Challenge :: ETH Prediction Round 2

## Files description

- data/ - directory with input data and output predictions.
- 1_get_predictions.ipynb - code for the ETH predictions generation. 
- 2_upload_file.py - code for publishing predictions online, to private url.
- 3_share_to_ocean.py - code for sharing predictions, to judges via Polygon.
- startup.py - initial script executed in every notebook when started.
- REPORT.md - solution approach description.
- develop/1_get_data.ipynb - script with getting hourly ETH/USD prices for the last 2 years.
- develop/2_train_rnn.ipynb - script with training recurrent neural networks.
- develop/models/ - directory with saved models in h5 format.
- develop/pictures/ - directory with pictures.


## Challenge
Submission deadline is Dec 11, 2022 at 23:59 UTC.
Contestants are requested to submit the following:
1. A .csv file with ETH price predictions over a 12-hour period, with first prediction on Monday December 12, 2022 at 1:00am UTC and a prediction every hour on the hour after that, for 12 predictions total. This must be submitted as its own dataset in Ocean via the instructions provided in the README below.
2. A report of 10-15 slides describing your approach, difficulties encountered and insights you gained in making the predictions. Think of this as a “conference presentation” for your work.
3. At least one slide presenting any challenges faced while using the Ocean library and/or recommendations you may have.

## README
For making and submitting predictions, the following README has the instructions: https://bit.ly/ethpredict2_readme

You can use any data you wish - static data or streams, free or priced, raw data or feature vectors, published in Ocean or not. The README links to some data feeds and AI modeling approaches that you may find useful.
