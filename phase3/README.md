# Ocean Data Challenge :: ETH Prediction Round 3

## Files description

- 1_get_predictions.ipynb - notebook for the ETH predictions generation. 
- 2_uploading.ipynb - notebook for publishing predictions in the Arweave and send the asset to Ocean.
- 3_check_predictions.ipynb - notebook with checking prediction results (executing 12 hours after)
- helpers.py - utilities functions from Ocean: https://github.com/oceanprotocol/predict-eth/blob/main/predict_eth/helpers.py
- startup.py - initial script executed in every notebook when started (libraries loading).
- REPORT.md - solution approach description.


## Challenge
Submission deadline is Feb 19, 2023 at 23:59 UTC
Contestants are requested to submit the following:
1. A .csv file with ETH price predictions over a 12-hour period, with the first prediction presenting the price on Monday February 20, 2023 at 1:00am UTC and a prediction for every hour on the hour after that, for 12 predictions total.
2. A report of 10-15 slides describing your approach, difficulties encountered and challenges faced while using the Ocean library and/or recommendations you may have. Think of this as a “conference presentation” for your work.
3. Use the proper flow to submit your prediction. This includes storing the predictions onto Arweave, publishing the predictions on Ocean Market and sharing the datatoken to the judges for accessing such predictions.

## README
For making and submitting predictions, the following README has the instructions: https://bit.ly/predicteth3-readme

The README links to some data feeds and AI modeling approaches that you may find useful.
