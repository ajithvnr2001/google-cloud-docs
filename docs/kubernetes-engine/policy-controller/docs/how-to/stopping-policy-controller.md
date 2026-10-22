---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/stopping-policy-controller/
title: Stop Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:39.304468+00:00
---

# Stop Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/stopping-policy-controller/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Stop Policy Controller Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to disable Policy Controller. If you want to uninstall Policy Controller instead of temporarily disabling it, see [Uninstalling Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller#uninstalling).

If Policy Controller is causing issues in your cluster, you can temporarily disable the webhook:
    
    
    gcloud container fleet policycontroller suspend \
        --memberships=MEMBERSHIP_NAME
    

Replace `MEMBERSHIP_NAME` with the membership name of the registered cluster to disable Policy Controller on. You can specify multiple memberships separated by a comma.

You can then re-enable Policy Controller. This will cause the operator to regenerate the webhook configuration, which will reconfigure the API server to use Policy Controller as an admission webhook:
    
    
    gcloud container fleet policycontroller enable \
      --memberships=MEMBERSHIP_NAME
    

## What's next

  * [Use Policy Controller metrics](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-metrics)
  * [Troubleshoot Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/troubleshoot-policy-controller)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
