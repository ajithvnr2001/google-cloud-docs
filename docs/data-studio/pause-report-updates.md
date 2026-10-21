---
url: https://docs.cloud.google.com/data-studio/pause-report-updates/
title: Pause report updates \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:19:22.263037+00:00
---

# Pause report updates  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/pause-report-updates/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Pause report updates Stay organized with collections  Save and categorize content based on your preferences. 

By default, adding a component to a report or modifying a component's data settings causes Data Studio to request data. You can temporarily turn off data requests while editing your report by pausing updates.

Pausing updates lets you edit your report while minimizing the number of data requests, potentially saving on query costs. When you're done configuring the report's components, you can resume updates to see the data.

## Pause updates

To pause updates on your reports, follow these steps:

  1. Edit your report.
  2. In the toolbar, click ![](https://docs.cloud.google.com/static/data-studio/images/gmpausegmgrey60024dp-2023-04-21.png)**Pause updates**.



![](https://docs.cloud.google.com/static/data-studio/images/pause-updates-20260122.png)

While updates are paused, any changes that you make to the data settings for a component, such as adding or removing fields, or using any chart interactions, such as cross-filtering or sorting, will pause that component. Paused components display the message "Chart has pending changes." You can continue to configure a component while it's paused, but you'll only see style changes applied.

## Resume updates

When you're ready to view the data in your components again, in the toolbar, click ![](https://docs.cloud.google.com/static/data-studio/images/gmplayarrowgmgrey60024dp-2023-04-21.png)**Resume updates**.

## Limits and notes

Note the following while pausing updates:

  * Pausing updates applies to the entire report.
  * Pausing updates only pauses data requests. You can still make stylistic changes to the report.
  * Pausing updates only applies to your view of the report. Other collaborators on the report will see chart updates as usual unless they also pause updates.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
