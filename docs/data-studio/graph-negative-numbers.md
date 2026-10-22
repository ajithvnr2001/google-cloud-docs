---
url: https://docs.cloud.google.com/data-studio/graph-negative-numbers/
title: Graph negative numbers \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:17.247587+00:00
---

# Graph negative numbers  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/graph-negative-numbers/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Graph negative numbers Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** As of 2019-01-16, the default value for Axis min is (auto), so you'll only need to change this for older charts. The previous default Axis min setting was "0."

To display metrics with negative values in a chart, set the **Axis min** option to **(auto)** :

  1. Edit your report.
  2. Select the chart.
  3. Select the STYLE panel.
  4. Locate the main axis settings: for default charts, this will be the left axis, but could also be right or bottom, depending on how you've customized your chart.
  5. Change the **Axis min** value to **(auto)** by deleting the current setting.



Here's an example of how charts look with Axis min 0 versus Axis min (auto):

![Six column charts organized into two columns of three charts. The first column displays charts with the Axis Min set to 0, and the second column displays charts with the Axis Min set to auto.](https://docs.cloud.google.com/static/data-studio/images/axis-min-auto-2019-01-17.png)

  1. Data in the top charts contains mixed negative and positive values. 
     1. Charts on the left are set to use **Axis min: 0**.
     2. Charts on the right use **Axis min: (auto)**.
     3. Note how the last two dimension values ("  Green  " and "  Blue  ") appear in the charts.
  2. Data in the middle charts only contains positive values. In this case, there is no difference between 0 and (auto) settings.
  3. Data in the bottom charts only contains negative values. Here, using the (auto) setting on the right provides the correct visualization.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
