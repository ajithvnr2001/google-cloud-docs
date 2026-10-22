---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/sar-system-limits/
title: Learn about system limits \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:38.990261+00:00
---

# Learn about system limits  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/sar-system-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Learn about system limits Stay organized with collections  Save and categorize content based on your preferences. 

This page details the tested system limits that apply to System Artifact Registry (SAR) for the current release version of Google Distributed Cloud (GDC) air-gapped appliance.

**Note:** Actual limits may be higher. This page documents what is tested and qualified explicitly.

## Learn about SAR scalability

The SAR system supports GDC release artifacts for one year according to the following release schedule:

  * A patch version upgrade is released each month.
  * A minor version upgrade is released every four months.



You reach the storage quota when the server goes beyond one year, or when the previous release schedule is changed. The server supports a quota increase if there are resources available in the cluster.

## Supported individual artifact size

SAR supports serving individual artifacts up to a size of 30GB without failing. Some of the actions available include pulling and pushing the system artifacts.

## Offered availability

SAR offers an availability of more than 99.5% for the monthly uptime percentage, excluding planned maintenance windows.

The availability metric is monitored in the Artifact Registry General Health Dashboard on Grafana.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
