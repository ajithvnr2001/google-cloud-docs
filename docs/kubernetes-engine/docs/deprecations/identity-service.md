---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/identity-service/
title: Identity Service for GKE deprecation \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:24.112608+00:00
---

# Identity Service for GKE deprecation  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/identity-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Identity Service for GKE deprecation Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes the deprecation and shutdown of Identity Service for GKE, including the timeline and milestones and any migration steps that you must take. Identity Service for GKE isn't available in organizations that were created on or after July 1, 2025. In version 1.37 and later, GKE clusters don't support this feature in any organization.

This deprecation applies only to GKE clusters that run on Google Cloud. The _GKE Identity Service_ feature that's available in the connect gateway and for Google Distributed Cloud (software only) products isn't deprecated.

## Timeline and milestones

The following timeline describes the deprecation and shutdown schedule for Identity Service for GKE:

  1. **July 1, 2025** : Identity Service for GKE isn't supported in Google Cloud organizations that are created on or after this date.

  2. **July 1, 2026** : Identity Service for GKE is deprecated in version 1.36 and earlier. These versions can still use Identity Service for GKE until the [end of support date](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels) for the minor version.

Identity Service for GKE isn't supported in version 1.37 and later. You can't upgrade clusters that use Identity Service for GKE to version 1.37 or later.




## Blocked upgrades to version 1.37 and later

If you have clusters that use Identity Service for GKE, then GKE blocks automatic and manual cluster upgrades to version 1.37 or later.

Automatic upgrades remain paused until the end of standard support for the minor version. If your cluster is enrolled in the Extended channel, then automatic upgrades are paused until the end of extended support. When the minor version reaches the end of support date, GKE automatically upgrades the cluster to the next minor version. If Identity Service for GKE is still enabled in that cluster, authentication workflows will fail.

To upgrade your cluster to version 1.37 or later, you must disable Identity Service for GKE. To authenticate from external identity providers (IdPs), use Workforce Identity Federation. For more information, see Migrate from Identity Service for GKE.

## Migrate from Identity Service for GKE

If you rely on Identity Service for GKE to authenticate from third-party IdPs, then migrate to Workforce Identity Federation. Workforce Identity Federation supports multiple protocols, doesn't install components in the cluster, and is integrated with IAM.

The following table describes the difference in principal syntax between Workforce Identity Federation and Identity Service for GKE:

Identity Service for GKE syntax | Workforce Identity Federation syntax  
---|---  
`amal@example.com` | `principal://iam.googleapis.com/locations/global/workforcePools/full-time-employees/subject/amal@example.com`  
`sre-group` | `principalSet://iam.googleapis.com/locations/global/workforcePools/full-time-employees/group/sre-group`  
  
To migrate a cluster to use Workforce Identity Federation, follow these steps:

  1. Set up Workforce Identity Federation for your organization and external IdP. For instructions, see [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).

  2. Update the manifests for any RoleBindings and ClusterRoleBindings in your clusters to use the Workforce Identity Federation identifier syntax. Use one of the following options:

     * **Programmatic updates** : install and run the `gke-identity-service-migrator` tool. For instructions, see the [`GoogleCloudPlatform/gke-utilities` repository README](https://github.com/GoogleCloudPlatform/gke-utilities/tree/main).

This tool finds existing RBAC bindings that use the Identity Service for GKE syntax and creates new manifests that use the corresponding Workforce Identity Federation principal identifiers.

     * **Manual updates** : for every binding that references an authenticated user or group, create a separate copy of the object's manifest file that uses the Workforce Identity Federation identifier syntax.

  3. Apply the updated manifests for RoleBindings and ClusterRoleBindings to your cluster.

  4. Test that users can access the same resources when they authenticate using Workforce Identity Federation.

  5. Remove the obsolete RBAC bindings from your cluster.

  6. Disable Identity Service for GKE:
         
         gcloud container clusters update CLUSTER_NAME \
             --no-enable-identity-service
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
