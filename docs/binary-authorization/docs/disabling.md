---
url: https://docs.cloud.google.com/binary-authorization/docs/disabling/
title: Disable Binary Authorization (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:52.708014+00:00
---

# Disable Binary Authorization (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/disabling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Disable Binary Authorization (GKE) Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to disable Binary Authorization on a cluster running in Google Kubernetes Engine.

To disable Binary Authorization on a running cluster, follow these steps.

###  Console 

  1. Open the GKE page in the Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click the edit button for the name of the cluster where you want to modify. The button looks like a pencil.

  3. Set **Enable Binary Authorization** to **Disabled**.

![Disable Binary Authorization option](https://docs.cloud.google.com/static/binary-authorization/docs/images/disable-binary-authorization.png)

  4. Click **Save**.




###  gcloud 

Enter the following:
    
    
    gcloud beta container clusters update \
        --project=PROJECT_ID \
        **--binauthz-evaluation-mode=DISABLED** \
        --zone ZONE \
        CLUSTER_NAME
    

where:

  * PROJECT_ID is the ID of the project where the cluster is running
  * ZONE is the GKE zone (for example, `us-central1-a`)
  * CLUSTER_NAME is the name of the cluster you want to create (for example, `test-cluster`)



If you have CV enabled, running this command disables it. For more information, see [Manage CV platform policies](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
