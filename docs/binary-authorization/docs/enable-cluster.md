---
url: https://docs.cloud.google.com/binary-authorization/docs/enable-cluster/
title: Enable enforcement on an existing cluster \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:57.457303+00:00
---

# Enable enforcement on an existing cluster  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/enable-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Enable enforcement on an existing cluster Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to enable Binary Authorization enforcement on an existing Google Kubernetes Engine (GKE) cluster. 

## Before you begin

Before you use this guide do the following:

  1. Create a [standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) GKE cluster. To learn more about creating standard clusters, see [Create a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster) or [Create a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).
  2. [Enable the Binary Authorization API](https://docs.cloud.google.com/binary-authorization/docs/enabling).



## Enable enforcement

To enable enforcement, perform the following steps:

### Console

  1. In the Google Cloud console, go to the GKE page:

[Go to GKE](https://console.cloud.google.com/kubernetes/list).

  2. In the **Kubernetes clusters** list, click the name of your cluster.

  3. Under **Security** , in the row for **Binary authorization** , click the edit icon (_edit_).

  4. In the **Edit Binary Authorization** dialog, select the **Enable Binary Authorization** checkbox and click **Save changes**.




### gcloud

For a zonal cluster, enter the following command:
    
    
    gcloud container clusters update NAME \
        --zone ZONE \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE
    

Replace the following:

  * `NAME`: the name of the GKE cluster on which you want to enable Binary Authorization.
  * `ZONE`: the zone where the cluster resides.



Clusters can have both Binary Authorization enforcement and CV monitoring enabled. To change CV monitoring and enforcement settings, set `--binauthz-evaluation-mode` to one of the following values: 

  * `POLICY_BINDINGS`: enables only CV monitoring and disables an existing enforcement policy if there is one
  * `PROJECT_SINGLETON_POLICY_ENFORCE`: enables only enforcement and disables CV monitoring if it was previously enabled
  * `POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE`: enables both enforcement and CV monitoring



For more information on CV policy and cluster management, see [Manage CV platform policies](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies). 

Alternatively, for a regional cluster, enter the following command:
    
    
    gcloud container clusters update NAME \
        --region REGION \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE
    

Replace the following:

  * `NAME`: the name of the GKE cluster on which you want to enable Binary Authorization.
  * `REGION`: the region where the cluster resides.



Clusters can have both Binary Authorization enforcement and CV monitoring enabled. To change CV monitoring and enforcement settings, set `--binauthz-evaluation-mode` to one of the following values: 

  * `POLICY_BINDINGS`: enables only CV monitoring and disables an existing enforcement policy if there is one
  * `PROJECT_SINGLETON_POLICY_ENFORCE`: enables only enforcement and disables CV monitoring if it was previously enabled
  * `POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE`: enables both enforcement and CV monitoring



For more information on CV policy and cluster management, see [Manage CV platform policies](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies). 

**Note:** It can take a few minutes for the policy to take effect.

## What's next

  * [Require attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations)
  * [Deploy container images](https://docs.cloud.google.com/binary-authorization/docs/deploying-containers)
  * [View events in Cloud Audit Logs](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
