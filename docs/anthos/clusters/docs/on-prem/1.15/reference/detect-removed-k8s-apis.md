---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/detect-removed-k8s-apis/
title: Detect removed Kubernetes APIs \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:34.141692+00:00
---

# Detect removed Kubernetes APIs  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/detect-removed-k8s-apis/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Detect removed Kubernetes APIs Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/reference/detect-removed-k8s-apis)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/reference/detect-removed-k8s-apis)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



There are several Kubernetes versions that have removed APIs. If you upgrade a Google Distributed Cloud cluster to a new Kubernetes version, and your workloads use any APIs that have been removed, your workloads could be disrupted. Follow the steps given here to determine whether your workloads use any of the removed APIs for a given Kubernetes version before you upgrade your cluster.

You can see a list of deleted APIs in each Kubernetes version in [this doc](https://kubernetes.io/docs/reference/using-api/deprecation-guide/).

## Determine if the API deletion affects you

**Note:** the steps below require that Cloud Audit Logs is enabled and audit logs are streamed to [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs).

To determine if the Kubernetes Service Accounts you use make calls to any deleted APIs, run the supplied query in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface):

  1. In the Google Cloud console, go to the **Logs Explorer** page in the **Logging** menu.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, enter the following query:
         
         resource.labels.cluster_name = "CLUSTER_NAME" AND
         logName = "projects/PROJECT_ID/logs/externalaudit.googleapis.com%2Factivity" AND
         protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:kube-system:") AND
         protoPayload.authenticationInfo.principalEmail!~("system:serviceaccount:gke-system:") AND
         protoPayload.authenticationInfo.principalEmail!~("kube-admin") AND
         protoPayload.authenticationInfo.principalEmail!~("kubernetes-admin") AND
         labels."k8s.io/removed-release"="KUBERNETES_MINOR_VERSION"
         

The output from this query shows if any of your Kubernetes Service Accounts make deleted API calls in the given KUBERNETES_MINOR_VERSION, for example, 1.25.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
