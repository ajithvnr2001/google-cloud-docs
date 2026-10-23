---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/troubleshooting/
title: Troubleshoot Network Analyzer \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:13.472931+00:00
---

# Troubleshoot Network Analyzer  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Troubleshoot Network Analyzer Stay organized with collections  Save and categorize content based on your preferences. 

Use the following guidance to troubleshoot common issues with Network Analyzer.

## The Network Analyzer console only has empty tables, no insights

Network Analyzer detects invalid or suboptimal configuration issues in your project. There is a difference between **analysis that was not run** and **analysis discovered no issues**. If the **last run time** shows a recent timestamp, it means the analysis was done but no issues were found. Otherwise, it indicates a problem that the system did not trigger the analysis to run.

## The insights I saw yesterday did not appear today in Network Analyzer

Insights might not appear due to one of the following reasons:

  * The insight has already been fixed. To verify, change the filter by status **Fixed** and verify if the insight appears in that list.
  * The insight's first report time is not within the time range you are querying. By default, when you open the console, in the upper right corner, you see **All insights**. You can see all the insights. If you select a custom time range, it is possible the insight you are looking for is discovered outside of the time range.



## The GKE is not publishing the network insights

If the Google Kubernetes Engine (GKE) cluster is in error state, you will not see the network insights or there might be delay in triggering the insight. We recommend resolving the reason due to which the GKE cluster is in error state. Once the error is resolved, the insights will be triggered. For more information, see [Detect invalid configurations](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/detect-invalid-configuration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
