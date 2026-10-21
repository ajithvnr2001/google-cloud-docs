---
url: https://docs.cloud.google.com/data-studio/google-analytics-4-sampling/
title: Google Analytics 4 sampling \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:23.235269+00:00
---

# Google Analytics 4 sampling  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/google-analytics-4-sampling/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Google Analytics 4 sampling Stay organized with collections  Save and categorize content based on your preferences. 

Google Analytics applies sampling techniques to large data sets to improve the performance of its reports. [Learn more about Google Analytics 4 sampling.](https://support.google.com/analytics/answer/13331292)

## View sampled Google Analytics data in Data Studio

Data Studio uses the same sampling behavior as Google Analytics. If a chart in Data Studio creates an ad hoc request for data in Google Analytics, standard sampling rules will come into play. The actual sampling rate is determined by Google Analytics at the time of the data request. You can't change this rate in Data Studio.

**Note:** Including today's date may have sampling implications. If data appears to be sampled in Data Studio but not in Google Analytics, make sure that you're comparing the exact same date range and consider removing today from the date range.

## Sampling and Google Analytics 360

Google Analytics 360 provides higher sampling rates than standard Analytics. Data Studio supports these higher sampling rates for Google Analytics 360 users.

## Limits of data sampling display in Data Studio

Data sampling display in Data Studio have the following limitations:

  * Data Studio doesn't indicate if data from Google Analytics is sampled.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
