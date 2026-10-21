---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/automatic-commitment-renewal/
title: Troubleshoot automatic commitment renewal \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:20.842233+00:00
---

# Troubleshoot automatic commitment renewal  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/automatic-commitment-renewal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot automatic commitment renewal Stay organized with collections  Save and categorize content based on your preferences. 

To troubleshoot issues when you [renew commitments automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically), use the following information.

## Invalid values for auto-renew

The following error occurs when you try to create or update the auto-renew setting for a commitment.
    
    
    INVALID_FIELD_VALUE
    

This error occurs if you don't pass a value or you pass an invalid value for auto-renew.

To resolve this error, pass valid values for auto-renew. The following list shows the valid values for auto-renew:

  * **gcloud CLI** : `--auto-renew`, `--no-auto-renew`
  * **Compute Engine API** : `true`, `false`



## Resource not available for auto-renew

The following error occurs when you try to update the auto-renew setting for a commitment.
    
    
    RESOURCE_NOT_READY_WITH_DETAILS
    

This error occurs if you try to update the auto-renew setting on a commitment that is in one of the following states: Creating, Expired, Cancelled.

To resolve this error, only update the auto-renew setting on a commitment when it is in the Active state.

## What's next

  * [Learn how to renew commitments automatically](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
