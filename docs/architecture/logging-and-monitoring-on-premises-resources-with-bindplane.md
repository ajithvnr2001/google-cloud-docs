---
url: https://docs.cloud.google.com/architecture/logging-and-monitoring-on-premises-resources-with-bindplane/
title: Log and monitor on-premises resources with BindPlane \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:37.762283+00:00
---

# Log and monitor on-premises resources with BindPlane  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/logging-and-monitoring-on-premises-resources-with-bindplane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Log and monitor on-premises resources with BindPlane Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-02 UTC

[Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring) provide advanced logging and monitoring services for Google Cloud. Cloud Logging and Cloud Monitoring support logging and monitoring for Google Cloud and Amazon Web Services (AWS), and support logging and monitoring for hybrid and on-premises resources with [BindPlane by observIQ](https://observiq.com/solutions). This solution describes the considerations and design patterns for using Logging, Monitoring, and BindPlane to provide logging and monitoring services for on-premises resources.

This series is intended for people in DevOps who are interested in logging or monitoring their hybrid or on-premises resources.

Using Logging, Monitoring, and BindPlane can provide a powerful way to consolidate your logging and monitoring either as a part of a transition to Google Cloud or as part of a strategy to centralize logging and monitoring for your apps and infrastructure. For example, you might want to use a single tool for your logging and monitoring needs to simplify work for your DevOps and SRE teams, to reduce costs, or to standardize tooling. Or, you might want to monitor your on-premises resources through Logging and Monitoring if you've deployed Google Cloud apps and infrastructure and need to monitor both your Google Cloud and your remaining on-premises apps and infrastructure.

This series consists of the following two parts:

  * [Log on-premises resources with BindPlane](https://docs.cloud.google.com/architecture/logging-on-premises-resources-with-bindplane): Read about how Cloud Logging supports logging from on-premises resources.
  * [Monitor on-premises resources with BindPlane](https://docs.cloud.google.com/architecture/monitoring-on-premises-resources-with-bindplane): Read about how Cloud Monitoring supports monitoring of on-premises resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-02 UTC."],[],[]] 
