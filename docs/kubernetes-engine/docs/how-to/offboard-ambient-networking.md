---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/offboard-ambient-networking/
title: Offboard ambient networking \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:53.730375+00:00
---

# Offboard ambient networking  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/offboard-ambient-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Offboard ambient networking Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note** : Before using GKE ambient networking, you must be added to an allowlist. Request access by filling out the [sign-up form](https://forms.gle/HhretawUX6GFFxq87). Allow 2 to 3 business days for your request to be processed. 

Follow these steps to safely disable and remove ambient networking from your cluster.

  1. Remove all ambient policies impacting your services, ensuring no policy enforces strict mTLS:
         
         kubectl delete gcpservertlspolicies -n ambient-test server
         kubectl delete gcpclienttlspolicies -n ambient-test server-mtls
         kubectl delete gcpauthzpolicy -n ambient-test --all
         

  2. Remove the label from the relevant namespace to disable traffic interception:
         
         kubectl label namespace ambient-test networking.gke.io/dataplane-mode-
         

  3. Verify that the annotation `ambient.networking.gke.io/redirection` is removed from all Pods in the Namespace:
         
         kubectl get pods -n ambient-test -o yaml | grep redirection
         

The output should be an empty response.

  4. Optionally, if you enabled Layer 4 metrics generation, remove the metrics label from the namespace:
         
         kubectl label namespace ambient-test networking.gke.io/ambient-network-metrics-
         

  5. Disable ambient networking at the cluster level to remove ambient components:
         
         gcloud beta container clusters update CLUSTER_NAME \
             --location=CLUSTER_LOCATION --no-enable-ambient-networking
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `CLUSTER_LOCATION`: the Compute Engine [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
