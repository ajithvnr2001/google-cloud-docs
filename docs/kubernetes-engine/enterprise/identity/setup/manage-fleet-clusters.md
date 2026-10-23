---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/manage-fleet-clusters/
title: Disable fleet-level authentication management \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:57.296315+00:00
---

# Disable fleet-level authentication management  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/manage-fleet-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Disable fleet-level authentication management Stay organized with collections  Save and categorize content based on your preferences. 

This document provides details on how you can disable fleet-level authentication management for a cluster and fleet.

## Disable fleet-level management for a cluster

To disable fleet-level management for a cluster, run the following command:
    
    
    gcloud container fleet identity-service delete --membership=CLUSTER_NAME

where `CLUSTER_NAME` is your cluster's unique name within the fleet.

## Disable fleet-level management for the entire fleet

To disable fleet-level authentication management, do the following:

### Console

  1. In the Google Cloud console, go to the **GKE Identity Service** page.

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/identityservice)

  2. Click remove_circle_outline **Disable GKE Identity Service**.

  3. In the confirmation dialog, click **Disable**.




### gcloud

Run the following command:
    
    
    gcloud container fleet identity-service disable
    

After disabling the feature for your fleet, you can no longer view or update any cluster's authentication state at the fleet level in the Google Cloud console or by using `gcloud`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
