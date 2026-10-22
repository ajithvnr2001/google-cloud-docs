---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/
title: Expand Istio property replica counts to avoid problems when draining Istio nodes \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:01.328627+00:00
---

# Expand Istio property replica counts to avoid problems when draining Istio nodes  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/expand-replica-count-to-drain-istio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Expand Istio property replica counts to avoid problems when draining Istio nodes Stay organized with collections  Save and categorize content based on your preferences. 

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This document is applicable for Apigee hybrid users only. 

When draining Istio pods some nodes may not drain because they have a replica count of `1`, while `3` or more replicas are required. In order to avoid this, you should set the minimum replica count for each property to at least `3`. 

When backing up and draining Istio nodes you may see errors like: 
    
    
    kubectl drain` failed to evict and reschedule pods to another node due to PodDisruptionBudget definitions:
    ===
    NAMESPACE NAME MIN AVAILABLE MAX UNAVAILABLE ALLOWED DISRUPTIONS AGE
    istio-system istio-ingressgateway 1 N/A 2 5d11h
    istio-system istio-pilot 1 N/A 2 5d11h
    ===

For `istio-ingressgateway` and `istio-pilot` you can set the `istio.ingressgateway.replicaCountMin` and `istio.pilot.replicaCountMin` properties to **`3`** or higher. See the [ Configuration properties reference, `istio`](https://docs.cloud.google.com/apigee/docs/hybrid/latest/config-prop-ref#istio). 

For other `istio` components (that don't have a `replicaCountMin` property), see [ Manually upgrading a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) in the GKE documentation or [ IstioOperator Options](https://istio.io/latest/docs/reference/config/istio.operator.v1alpha1/) in the Istio documentation. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
