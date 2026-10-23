---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement/
title: GKE on Azure deprecation announcement \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:42.384869+00:00
---

# GKE on Azure deprecation announcement  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GKE on Azure deprecation announcement

GKE on Azure will no longer be supported on March 17, 2027.

## What this means

Google will cease maintenance and contracted support for GKE on Azure from March 17, 2027.

The following schedule lists the significant dates in this shutdown.

  * **March 17, 2025** : Maintenance mode starts.

    * Google continues to fix bugs and resolve CVEs during this phase.
    * Google support contracts continue as before.
    * No new functionality will be added except as needed to fix bugs.
  * **March 17, 2027** : Product no longer supported.

    * No further upgrades or bug fixes occur.
    * APIs will be disabled.



## What you should do now

We recommend that you migrate to GKE or another Kubernetes distribution before March 17, 2027. To continue using Google Cloud features, you can use [GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached).

To migrate from GKE on Azure to another Kubernetes distribution, keep the following points in mind:

  1. Deploy new Kubernetes clusters with the same configurations as your GKE on Azure clusters. To ensure identical configurations across your old and new clusters, you can use [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) or another GitOps solution.
  2. Identify the workloads that you want to migrate to the new GKE on Azure cluster.
  3. Deploy a single workload on your new cluster and update the DNS settings to enable your old GKE on Azure cluster to point to the same workload on the new cluster.
  4. Test the new workload.
  5. Repeat the preceding two steps for all the workloads that you want to deploy on the cluster.
  6. After all workloads are migrated and tested, [delete your GKE on Azure clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/delete-cluster).



## Contact Cloud Customer Care

Your account's lead customer engineer is your best contact point for deprecation support. Alternatively, you can [file a support case](https://console.cloud.google.com/support) through Google Cloud console or contact [Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures#manage_a_support_case).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
