---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/deleted-apis-kubernetes/
title: Detect removed Kubernetes APIs \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:01.942057+00:00
---

# Detect removed Kubernetes APIs  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/deleted-apis-kubernetes/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Detect removed Kubernetes APIs Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/deleted-apis-kubernetes)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/deleted-apis-kubernetes)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



There are several Kubernetes releases that have deprecated and removed APIs. If you upgrade a Google Distributed Cloud cluster to a new Kubernetes version, and your workloads use any APIs that have been removed, your workloads can be disrupted. Follow the steps in this document to determine whether your workloads use any of the removed APIs for a given Kubernetes version before you upgrade your cluster.

For a list of removed APIs by Kubernetes release, see [Deprecated API Migration Guide](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) in the Kubernetes documentation.

## Determine if the API deletion affects you

The following steps require that your Google Distributed Cloud clusters have cluster [audit logging](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/audit-logging) enabled and that audit logs are streamed to [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs), which is the default behavior.

To determine if the Kubernetes Service Accounts you use make calls to any deleted APIs, run the supplied query in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface):

  1. In the Google Cloud console, go to the **Logs Explorer** page in the **Logging** menu.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, enter the following query:
         
         resource.labels.cluster_name = "CLUSTER_NAME" AND
         logName = "projects/PROJECT_ID/logs/externalaudit.googleapis.com%2Factivity" AND
         protoPayload.authenticationInfo.principalEmail:("system:serviceaccount" OR "@") AND
         protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:kube-system:") AND
         protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:cert-manager:") AND
         protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:capi-kubeadm-bootstrap-system:") AND
         protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:capi-kubeadm-bootstrap-system-webhook:") AND
         protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:capi-system:") AND
         protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:capi-system-webhook:") AND
         labels."k8s.io/removed-release"="KUBERNETES_MINOR_VERSION"
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster that contains the workloads that you're checking.

     * `PROJECT_ID`: the ID of the Google Cloud project that your cluster uses for logs and metrics (`clusterOperations.projectID`). 

     * `KUBERNETES_MINOR_VERSION`: the minor Kubernetes version, such as 1.25, that has removed APIs.

The output from this query shows if any of your Kubernetes Service Accounts make calls to API that have been removed for the given Kubernetes minor release.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
