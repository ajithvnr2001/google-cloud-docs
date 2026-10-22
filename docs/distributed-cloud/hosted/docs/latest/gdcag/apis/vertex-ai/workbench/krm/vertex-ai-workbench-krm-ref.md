---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/workbench/krm/vertex-ai-workbench-krm-ref/
title: Vertex AI Workbench KRM API reference \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:14.677052+00:00
---

# Vertex AI Workbench KRM API reference  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/workbench/krm/vertex-ai-workbench-krm-ref/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Vertex AI Workbench KRM API reference Stay organized with collections  Save and categorize content based on your preferences. 

## Packages

  * aiplatform.gdc.goog/v1



## aiplatform.gdc.goog/v1

Package v1 contains API schema definitions for the aiplatform.gdc.goog v1 API group.

### Resource Types

  * Notebook
  * NotebookList



#### Notebook

`Notebook` is the Schema for the Notebooks API.

_Appears in:_ \- NotebookList

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.gdc.goog/v1`  
`kind` _string_ | `Notebook`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _NotebookSpec_ |   
`status` _NotebookStatus_ |   
  
#### NotebookCondition

_Appears in:_ \- NotebookStatus

Field | Description  
---|---  
`type` _string_ | The type of the condition. There are three possible values, `Running`, `Waiting`, and `Terminated`.  
`lastProbeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#time-v1-meta)_ | The time when the Notebook was last probed.  
`reason` _string_ | A string that contains the reason the container is in its current state.  
`message` _string_ | A string that contains a detailed message the container is in its current state.  
  
#### NotebookError

`NotebookError` represents an error that occurred while updating Notebook resources.

_Appears in:_ \- NotebookStatus

Field | Description  
---|---  
`errorMessage` _string_ | A string that contains a detailed message that describes the `Pod` state.  
`code` _string_ | A string that contains the error code of the `Pod` in its current state, such as `VTXWB-E0000`.  
  
#### NotebookList

`NotebookList` contains a list of `Notebook` instances.

Field | Description  
---|---  
`apiVersion` _string_ | `aiplatform.gdc.goog/v1`  
`kind` _string_ | `NotebookList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Notebook array_ |   
  
#### NotebookSpec

`NotebookSpec` defines the desired state of the Notebook.

_Appears in:_ \- Notebook

Field | Description  
---|---  
`template` _NotebookTemplateSpec_ | A specification for a Notebook instance that describes the desired state of the Notebook's workload in the cluster.  
  
#### NotebookStatus

`NotebookStatus` defines the observed state of the Notebook.

_Appears in:_ \- Notebook

Field | Description  
---|---  
`conditions` _NotebookCondition array_ | Deprecated, use `Notebook` CR `Events`. An array of `NotebookCondition` objects.  
`readyReplicas` _integer_ | The number of `Pods` created by the `StatefulSet` controller with their `Condition` set to `Ready`.  
`containerState` _[ContainerState](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#containerstate-v1-core)_ | Deprecated, use `NotebookStatus.Phase`. The state of the underlying container. For more information, refer to https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#containerstate-v1-core.  
`phase` _string_ | A string that contains the current `Pod` phase.  
`reason` _string_ | A string that contains the reason the `Pod` is in its current state.  
`podUnavailableTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#time-v1-meta)_ | If the Notebook is not currently running or the controller failed to query pod status, the time when the Notebook pod was first observed to not be running.  
`error` _NotebookError_ | The last error to occur while updating Notebook resources. This field is empty on success.  
  
#### NotebookTemplateSpec

`NotebookTemplateSpec` defines the desired state of the cluster.

_Appears in:_ \- NotebookSpec

Field | Description  
---|---  
`spec` _[PodSpec](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#podspec-v1-core)_ | Defines the containers, environment variables for the container, and other properties such as the scheduler name and security context. For more information, refer to https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#podspec-v1-core.  
`userCluster` _string_ | `UserCluster` is the name of the user cluster where the Notebook workload is created. The cluster must have sufficient resources to run the workload specified in `PodSpec`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
