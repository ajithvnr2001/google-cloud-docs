---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-23/
title: Kubernetes Ingress Beta APIs removed in GKE 1.23 \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:20:50.480638+00:00
---

# Kubernetes Ingress Beta APIs removed in GKE 1.23  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-23/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Kubernetes Ingress Beta APIs removed in GKE 1.23 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides information on the deprecation and removal of [beta Ingress API versions](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#ingress-v122) in the open source Kubernetes 1.22 release. GKE made a one-time exception for clusters created on version 1.21 or earlier to continue using the APIs until 1.23 for additional time to migrate. You must migrate your clusters to `Ingress` v1 APIs before version 1.22 [reaches end of life](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).

The deprecated Ingress beta APIs removed in Kubernetes version 1.22 are former beta APIs that have since graduated from Beta (`v1beta1`) to GA (`v1`). The GA APIs provide [longer-term compatibility guarantees](https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecating-parts-of-the-api) and should be used in place of the deprecated beta APIs.

All existing objects can be interacted with by using the GA APIs.

**Important:** Before upgrading to the version where the Ingress APIs are removed, you should update API clients and manifests to use the GA APIs.

### Ingress (available until 1.23 for clusters created on 1.21 or earlier)

The Beta API versions (`extensions/v1beta1` and `networking.k8s.io/v1beta1`) of `Ingress` are no longer served for GKE clusters running version 1.22 or later if the cluster was created on version 1.22 or later.

However, for clusters created on GKE version 1.21 or earlier and upgraded to 1.22 on the patch version 1.22.7-gke.300 or later, you can still use the Beta API versions until the cluster is upgraded to version 1.23. This is a one-time exception for older clusters to give you more time to migrate your clusters from using these API versions which are removed from the open-source Kubernetes in version 1.22.

Any clusters running GKE version 1.23 and later will no longer serve the deprecated `Ingress` beta APIs. Manifests using those API versions can no longer be applied. Previously persisted objects remain functional and can be viewed and updated using the new API versions, before and after upgrading to 1.23.

  * Migrate manifests and API clients to use the **networking.k8s.io/v1** API version.
  * Refer to the following table that describes the notable changes in the GA API version:

Field | Change  
---|---  
`spec.backend` | Renamed to `spec.defaultBackend`.  
backend `serviceName` | Renamed to `service.name`.  
`servicePort` | Numeric backend `servicePort` fields are renamed to `service.port.number`. String backend `servicePort` fields are renamed to `service.port.name`.  
`pathType` | Now required for each specified path. The value can be: `Prefix`, `Exact`, or `ImplementationSpecific`. To match the undefined `v1beta1` behavior, use `ImplementationSpecific`.  



The following manifests describe the same Ingress in `v1` and `v1beta1`:

### v1beta1 manifest
    
    
    apiVersion: networking.k8s.io/v1beta1
    kind: Ingress
    metadata:
      name: example
    spec:
      backend:
        serviceName: default-backend
        servicePort: 80
      rules:
      - http:
          paths:
          - path: /testpath
            backend:
              serviceName: test
              servicePort: 80
    

### v1 manifest
    
    
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: example
    spec:
      defaultBackend:
        service:
          name: default-backend
          port:
            number: 80
      rules:
      - http:
          paths:
          - path: /testpath
            pathType: ImplementationSpecific
            backend:
              service:
                name: test
                port:
                  number: 80
    

You can use the following query for clusters with Google Cloud Observability enabled to identify clients that access the Ingress `v1beta1` APIs:
    
    
    resource.type="k8s_cluster"
    resource.labels.cluster_name="$CLUSTER_NAME"
    protoPayload.authenticationInfo.principalEmail:("system:serviceaccount" OR "@")
    protoPayload.request.apiVersion=("extensions/v1beta1" OR "networking.k8s.io/v1beta1")
    protoPayload.request.kind="Ingress"
    NOT ("kube-system")
    

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

## Upgrading third-party components

[Deprecation insights](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations) might display results for third-party agents that make calls to deprecated APIs in your cluster.

To resolve these insights, try the following steps:

  1. Check with your third-party software provider for an updated version.
  2. Upgrade the third-party software to the latest version. If you cannot upgrade the software, you should test whether upgrading GKE to the version with the removed deprecated APIs would break your service.



We recommend that you perform this upgrade and the GKE version upgrade on a staging cluster to monitor for disruptions before you upgrade your production clusters.

## Preparing to upgrade to version 1.23

You do not need to delete and recreate any of your API objects. All existing persisted API objects can already be read and updated using the new API versions. However, we recommend that you migrate your clients and manifests before upgrading to Kubernetes 1.23. Learn more in the ["What to do" section of the _Kubernetes Deprecated API Migration Guide_](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#what-to-do).

You can [view deprecation insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations#view-deprecation-insights-recs) to determine if your cluster is using a Kubernetes feature or API that is deprecated. Look for insights and recommendations about Ingress beta API usage with the `DEPRECATION_K8S_1_22_V1BETA1_API` subtype. 

Deprecation insights are based on observed API calls to deprecated APIs by user agents, not the configuration of your Kubernetes objects.

**Warning:** If you do not update a client or manifest before the 1.23 upgrade, it will not be able to read/modify existing objects or create new objects. The client or manifest will only be able to read, modify, or create objects once you update it.

## Update clusters impacted by deprecations

To upgrade clusters impacted by deprecations, perform the following steps:

  1. Check which user agents use the deprecated APIs in the [deprecation insight](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations) or logs.
  2. Update the user agents that use the deprecated APIs to use supported API versions.
  3. Update any third-party software that calls deprecated APIs to the latest versions.
  4. Upgrade a test cluster and test your application in a testing environment before upgrading your production cluster to reduce the risk of disruptions when deprecated APIs are no longer available.
  5. After you update all of the user agents, GKE waits until it has no longer observed use of deprecated APIs for 30 days, and then unblocks automatic upgrades. Automatic upgrades proceed according to the [release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).
  6. If you can't update an affected user agent, upgrade a separate test cluster to check whether the upgrade causes disruptions. If the upgrade doesn't cause disruptions, you can [upgrade your cluster manually](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).



## Resources

More information is available in the OSS Kubernetes documentation:

  * [Kubernetes Blog: API removals for Kubernetes version 1.22](https://kubernetes.io/blog/2021/07/14/upcoming-changes-in-kubernetes-1-22/)
  * [Kubernetes 1.22 release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.22.md#removal-of-several-beta-kubernetes-apis)
  * [Kubernetes Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/#v1-22)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
