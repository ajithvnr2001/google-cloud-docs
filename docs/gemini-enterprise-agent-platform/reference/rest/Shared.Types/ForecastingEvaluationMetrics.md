---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ForecastingEvaluationMetrics/
title: ForecastingEvaluationMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:14:13.724277+00:00
---

# ForecastingEvaluationMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ForecastingEvaluationMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ForecastingEvaluationMetrics Stay organized with collections  Save and categorize content based on your preferences. 

Metrics for forecasting evaluation results.

Fields  
  
`quantileMetrics[]` `object (`[QuantileMetricsEntry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ForecastingEvaluationMetrics#QuantileMetricsEntry)`)` The quantile metrics entries for each quantile. | `rootMeanSquaredError` `number` Root Mean Squared Error (RMSE). | `meanAbsoluteError` `number` Mean Absolute Error (MAE). | `meanAbsolutePercentageError` `number` Mean absolute percentage error. Infinity when there are zeros in the ground truth. | `rSquared` `number` Coefficient of determination as Pearson correlation coefficient. Undefined when ground truth or predictions are constant or near constant. | `rootMeanSquaredLogError` `number` Root mean squared log error. Undefined when there are negative ground truth values or predictions. | `weightedAbsolutePercentageError` `number` Weighted Absolute Percentage Error. Does not use weights, this is just what the metric is called. Undefined if actual values sum to zero. Will be very large if actual values sum to a very small number. | `rootMeanSquaredPercentageError` `number` Root Mean Square Percentage Error. Square root of MSPE. Undefined/imaginary when MSPE is negative. | JSON representation  
---  
      
    
    {
      "quantileMetrics": [
        {
          object ([QuantileMetricsEntry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ForecastingEvaluationMetrics#QuantileMetricsEntry))
        }
      ],
      "rootMeanSquaredError": number,
      "meanAbsoluteError": number,
      "meanAbsolutePercentageError": number,
      "rSquared": number,
      "rootMeanSquaredLogError": number,
      "weightedAbsolutePercentageError": number,
      "rootMeanSquaredPercentageError": number
    }  
  
## QuantileMetricsEntry

Entry for the Quantiles loss type optimization objective.

Fields  
  
`quantile` `number` The quantile for this entry. | `scaledPinballLoss` `number` The scaled pinball loss of this quantile. | `observedQuantile` `number` This is a custom metric that calculates the percentage of true values that were less than the predicted value for that quantile. Only populated when [optimizationObjective][google.cloud.aiplatform.publicfiles.trainingjob.definition.AutoMlForecastingInputs.optimization_objective] is minimize-quantile-loss and each entry corresponds to an entry in [quantiles][google.cloud.aiplatform.publicfiles.trainingjob.definition.AutoMlForecastingInputs.quantiles] The percent value can be used to compare with the quantile value, which is the target value. | JSON representation  
---  
      
    
    {
      "quantile": number,
      "scaledPinballLoss": number,
      "observedQuantile": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
