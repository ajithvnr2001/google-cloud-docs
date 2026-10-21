---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/upgrades/
title: Blockchain Node Engine node upgrades and maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:37.226815+00:00
---

# Blockchain Node Engine node upgrades and maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/upgrades/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Blockchain Node Engine node upgrades and maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes processes and requirements regarding Blockchain Node Engine upgrades and maintenance windows.

## Node maintenance

Blockchain node maintenance occurs when the Blockchain Node Engine instance is updated. This includes:

  * Upgrades of blockchain client software itself (e.g. an Ethereum upgrade)
  * Updates to Blockchain Node Engine business logic. For example: 
    * New features
    * Bug fixes
    * Routine maintenance
    * GKE cluster software updates
  * Maintenance updates on the underlying infrastructure



## Node downtime

Although it is not common, node upgrades can cause downtime from as little as a minute or less to up to 40 minutes. In some cases, the node pod itself does not need to be restarted and there is no downtime.

**Tip:** To avoid downtime, provision multiple nodes across multiple locations to distribute the load.

## Maintenance windows

We plan to provide updates during regular windows as follows; however, there could also be unplanned urgent updates. We will provide as much notice as possible.

Location | Day | Time | Expected downtime  
---|---|---|---  
`us-central1` | First monday of each month (1) | 9 - 10AM PST | Minutes  
`europe-west1` | First monday of each month (1) | 10 - 11AM PST | Minutes  
`asia-east1` | First monday of each month (1) | 11AM - 12PM PST | Minutes  
(1) If it falls on a non-business day, the next business day.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
