---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-26/
title: Kubernetes 1.26 deprecated APIs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:41.334419+00:00
---

# Kubernetes 1.26 deprecated APIs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-26/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Kubernetes 1.26 deprecated APIs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to prepare clusters for upgrades to GKE version 1.26. You can find API clients making calls to [deprecated APIs removed in 1.26](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#changelog-since-v1250) and update those clients to use GA APIs. For more detailed information, see the [Kubernetes deprecated API migration guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-26).

**Important:** After March 30, 2024—when [1.25 reaches end of standard support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels)— GKE begins to automatically upgrade clusters still using version 1.25 and deprecated APIs (removed in version 1.26) to version 1.26. GKE will stop [pausing automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with) after March 30, 2024 for clusters still using [deprecated APIs removed in version 1.26](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-26). We recommend that you upgrade your clusters to version 1.26 as soon as possible as GKE minor versions that have reached end of support will no longer receive security patches and bug fixes. To learn more about the GKE minor version lifecycle, see [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).

## Removed APIs in version 1.26

The deprecated APIs in Kubernetes version 1.26 are either Beta APIs that have graduated to GA (for example `v2`) or from one Beta version to another (for example, `v1beta1` to `v1beta2`). The GA APIs provide [longer-term compatibility guarantees](https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecating-parts-of-the-api) and should be used in place of the deprecated Beta APIs.

All existing objects for APIs that have graduated to new versions can be interacted with by using the updated APIs.

**Important:** Before upgrading to 1.26, you should update API clients and manifests to use the updated APIs.

### Flow control resources

The `flowcontrol.apiserver.k8s.io/v1beta1` API version of FlowSchema and PriorityLevelConfiguration is no longer served as of v1.26.

Migrate manifests and API clients to use the `flowcontrol.apiserver.k8s.io/v1beta3` API version, available since v1.26. All existing persisted objects are accessible using the new API. 

### HorizontalPodAutoscaler

The `autoscaling.apiserver.k8s.io/v2beta2` API version of HorizontalPodAutoscaler is no longer served as of v1.26.

Migrate manifests and API clients to use the `autoscaling.apiserver.k8s.io/v2` API version, available since v1.23. All existing persisted objects are accessible using the new API. 

## Preparing to upgrade to version 1.26

You do not need to delete and recreate any of your API objects. All existing persisted API objects for APIs that graduated to GA can already be read and updated using the new API versions.

However, we recommend that you migrate your clients and manifests before upgrading to Kubernetes 1.26. To learn more, see [Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#what-to-do).

You can [view deprecation insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations#view-deprecation-insights-recs) to determine if your cluster is using Kubernetes 1.26 deprecated APIs. GKE generates deprecation insights when user agents call deprecated APIs, not from the configuration of your Kubernetes objects.

**Warning:** If you do not update a client or manifest before the 1.26 upgrade, it will not be able to read/modify existing objects or create new objects. The client or manifest will only be able to read, modify, or create objects once you update it.

## Find clusters using deprecated APIs

You can find which clusters are using deprecated APIs from [deprecation insights](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations). Deprecation insights also provide information such as which API clients are calling the deprecated APIs in your cluster.

You can also use audit logs to find which clients are making calls to deprecated APIs.

### Locate API clients making write calls to deprecated APIs

For clusters with Google Cloud Observability enabled, you can use the following [Admin Activity audit log](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging#viewing_logs) query to show the use of deprecated APIs by user agents that are not Google-managed:
    
    
    resource.type="k8s_cluster"
    labels."k8s.io/removed-release"="DEPRECATED_API_MINOR_VERSION"
    protoPayload.authenticationInfo.principalEmail:("system:serviceaccount" OR "@")
    protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:kube-system:")
    

Replace `DEPRECATED_API_MINOR_VERSION` with the minor version where the deprecated API is removed, for example `1.22`.

Admin Activity audit logs are automatically enabled for GKE clusters. With this query, the logs show user agents making write calls to the deprecated APIs. 

### Locate API clients making read calls to deprecated APIs

By default, audit logs show only write calls to the deprecated APIs. To also show read calls to deprecated APIs, configure Data Access audit logs.

**Caution:** If you enable additional audit logs, this might incur additional [logging costs](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary). The volume of ingested Data Access audit logs counts toward the Cloud Logging [logs ingestion quota](https://docs.cloud.google.com/logging/quotas#api-limits).

Follow the instructions to [Configure Data Access audit logs with the Google Cloud console](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console). In the Google Cloud console, select the Kubernetes Engine API. In the Log Types tab in the information panel, select `Admin Read` and `Data Read`.

With these logs enabled, you can now use the original query to see both read calls and write calls to the deprecated APIs.

### Upgrading third-party components

[Deprecation insights](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations) might display results for third-party agents that make calls to deprecated APIs in your cluster.

To resolve third-party agents calling deprecated APIs, we recommend the following best practices:

  1. Check with your third-party software provider for an updated version.
  2. Upgrade the third-party software to the latest version. If you cannot upgrade the software, you should test whether upgrading GKE to the version with the removed deprecated APIs would break your service.



We recommend that you perform this upgrade and the GKE version upgrade on a staging cluster to monitor for disruptions before you upgrade your production clusters.

## Update clusters impacted by deprecations

To upgrade clusters impacted by deprecations, perform the following steps:

  1. Check which user agents use the deprecated APIs in the logs.
  2. Update the user agents that use the deprecated APIs to use supported API versions.
  3. Update any third-party software that calls deprecated APIs to the latest versions.
  4. Upgrade a test cluster and test your application in a testing environment before upgrading your production cluster to reduce the risk of disruptions when deprecated APIs are no longer available.
  5. If you can't update an affected user agent, upgrade a separate test cluster to check whether the upgrade causes disruptions. If the upgrade doesn't cause disruptions, you can [upgrade your cluster manually](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).

  6. After you update all of the user agents, GKE waits until it has no longer observed use of deprecated APIs for 30 days, and then unblocks automatic upgrades. Automatic upgrades proceed according to the [release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).




## Resources

More information is available in the OSS Kubernetes documentation:

  * [Kubernetes Blog: Kubernetes Removals and Major Changes In 1.26](https://kubernetes.io/blog/2022/11/18/upcoming-changes-in-kubernetes-1-26)
  * [Kubernetes 1.26 release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md#changelog-since-v1250)
  * [Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-26)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
