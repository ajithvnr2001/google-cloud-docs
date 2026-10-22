---
url: https://docs.cloud.google.com/cluster-director/docs/troubleshoot/known-issues/
title: Cluster Director known issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:02.920985+00:00
---

# Cluster Director known issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/troubleshoot/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Cluster Director known issues Stay organized with collections  Save and categorize content based on your preferences. 

This document describes known issues that you might run into while you use Cluster Director, as well as how to troubleshoot them.

## Cluster operations fail with gcloud CLI versions earlier than 550.0.0

If you try running a cluster operation by using the gcloud CLI with a version earlier than 550.0.0, then the operation fails. To resolve this issue, update the gcloud CLI to version 550.0.0 or later:

  * **Cloud Shell** : if you use the Cloud Shell, then no action is required. The Cloud Shell automatically uses the latest gcloud CLI version.

  * **Local shell** : if you use the gcloud CLI on a local development environment, then complete the following steps:

    1. Check the gcloud CLI version:
           
           gcloud version
           

    2. If the gcloud CLI uses a version earlier than 550.0.0, then update it to the latest version:
           
           gcloud components update
           

If you want to update the gcloud CLI to a specific version, then use the previous command with the `--version` flag.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
