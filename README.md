# Build an ML Pipeline for Short-Term Rental Prices in NYC
This is project #2 for the Udacity Machine Learning DevOps Engineer Nanodregree. In this project, I estimate the typical price for a given property based on the price of similar properties. The project uses NYC AirBNB data.

## Links to Weights and Biases and GitHub

Weights and Biases Project Link

```
https://wandb.ai/habiakl/short_term_rental_prices
```

GitHub Link (this very webpage you are in right now)

```
https://github.com/rgalvaog/nd0821-c2-build-model-workflow-starter
```

## Steps to run

For this project, you want to make sure you can run MLFlow, if you don't have it installed:

```
pip3 install mlflow
```

In your Python environment of choice, you can then run:

```
mlflow run https://github.com/rgalvaog/nd0821-c2-build-model-workflow-starter.git -v 1.0.1
```

Note: This is version 1.0.1, the latest version released so far. If you would like to load version 1.0.0, you may do that, but note there is a bug with geospacial data.

## Future Considerations
Future iterations of this model may apply xGBoost to the random forest, or compare it to additional algorithms such as LogReg.

## License

[License](LICENSE.txt)
