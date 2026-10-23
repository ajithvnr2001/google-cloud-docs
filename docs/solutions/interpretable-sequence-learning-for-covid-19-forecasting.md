---
url: https://docs.cloud.google.com/solutions/interpretable-sequence-learning-for-covid-19-forecasting/
title: Interpretable sequence learning for COVID-19 forecasting \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:58.371573+00:00
---

# Interpretable sequence learning for COVID-19 forecasting  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/interpretable-sequence-learning-for-covid-19-forecasting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Interpretable sequence learning for COVID-19 forecasting Stay organized with collections  Save and categorize content based on your preferences. 

This document proposes a novel approach that integrates machine learning into compartmental disease modeling to predict the progression of COVID-19. Our model is explainable by design because it explicitly shows how different compartments evolve and it uses interpretable encoders to incorporate covariates and improve performance. Explainability is valuable to help ensure that the model's forecasts are credible to epidemiologists and to instill confidence in end users such as policy makers and healthcare institutions. Our model can be applied at different geographic resolutions, and we demonstrate it for states and counties in the United States. We show that our model provides more accurate forecasts than state-of-the-art alternatives and that it provides qualitatively meaningful explanatory insights.

## Overview

This document outlines the following:

  * Review proposed compartmental model for COVID-19.
  * Understand the model design choices made in order to use the covariates needed to accurately predict COVID-19.
  * Discuss the learning mechanisms developed to improve generalization while learning from limited training data.
  * Review several experiments to compare our model to other publicly available COVID-19 models.
  * Understand the potential limitations and failure cases of our model to guide those who might use the techniques to build forecasting systems that can affect public health decisions.



To read the full white paper, click the button:

[Download the PDF](https://storage.googleapis.com/covid-external/COVID-19ForecastWhitePaper.pdf)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
