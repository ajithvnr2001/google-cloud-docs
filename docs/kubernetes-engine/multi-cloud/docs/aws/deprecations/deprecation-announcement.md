---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement/
title: GKE on AWS deprecation announcement \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:40.002920+00:00
---

# GKE on AWS deprecation announcement  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  GKE on AWS deprecation announcement Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS will no longer be supported on March 17, 2027.

## What this means

Google will cease maintenance and contracted support for GKE on AWS from March 17, 2027.

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

To migrate from GKE on AWS to another Kubernetes distribution, keep the following points in mind:

  1. Deploy new Kubernetes clusters with the same configurations as your GKE on AWS clusters. To ensure identical configurations across your old and new clusters, you can use [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) or another GitOps solution.
  2. Identify the workloads that you want to migrate to the new GKE on AWS cluster.
  3. Deploy a single workload on your new cluster and update the DNS settings to enable your old GKE on AWS cluster to point to the same workload on the new cluster.
  4. Test the new workload.
  5. Repeat the preceding two steps for all the workloads that you want to deploy on the cluster.
  6. After all workloads are migrated and tested, [delete your GKE on AWS clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/delete-cluster).



## Contact Cloud Customer Care

Your account's lead customer engineer is your best contact point for deprecation support. Alternatively, you can [file a support case](https://console.cloud.google.com/support) through Google Cloud console or contact [Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures#manage_a_support_case).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
