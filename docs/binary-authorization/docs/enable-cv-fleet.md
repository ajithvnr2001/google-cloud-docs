---
url: https://docs.cloud.google.com/binary-authorization/docs/enable-cv-fleet/
title: Enable continuous validation at fleet level \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:47.164106+00:00
---

# Enable continuous validation at fleet level  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/enable-cv-fleet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Enable continuous validation at fleet level Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you are using [fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) with your Google Kubernetes Engine clusters, then you can enable continuous validation (CV) as a fleet-default configuration. This means that every new GKE on Google Cloud cluster [registered during cluster creation](https://docs.cloud.google.com/anthos/fleet-management/docs/register/gke#register_your_cluster) will have CV enabled on the cluster. You can find out more about fleet default configuration in [Manage fleet-level features](https://docs.cloud.google.com/anthos/fleet-management/docs/manage-features).

## Before you begin

  1. [Enable Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).
  2. Enable the GKE API.

[Enable GKE API](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)

  3. [Update the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components) to version 457.0.0 or later.

  4. [Create your platform policies](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies).




## Enable on a new fleet

To enable CV on a new fleet, run the following command:
    
    
    gcloud container fleet create \
        --binauthz-evaluation-mode=POLICY_BINDINGS \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID
    

Replace the following:

  * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored
  * `POLICY_ID`: the policy ID



You can also create a new fleet with multiple platform policies:
    
    
    gcloud container fleet create \
        --binauthz-evaluation-mode=POLICY_BINDINGS \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID_1 \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID_2
    

## Enable on an existing fleet

If you have an existing fleet, you can enable CV. However, enabling CV for an existing fleet doesn't affect workloads in existing fleet member clusters. If you want existing workloads to have CV enabled, you need to [enable the feature on individual clusters](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies#update-cluster-platform-policy).

To enable CV on an existing fleet, run the following command:
    
    
    gcloud container fleet update \
        --binauthz-evaluation-mode=POLICY_BINDINGS \
        --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID
    

Replace the following:

  * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored
  * `POLICY_ID`: the policy ID



## Disable

Disabling CV only affects workloads in new fleet member clusters. If you want existing workloads to have CV disabled, you need to [disable the feature on individual clusters](https://docs.cloud.google.com/binary-authorization/docs/disabling).

To disable CV on any new member clusters, run the following command:
    
    
    gcloud container fleet update \
        --binauthz-evaluation-mode=DISABLED
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
