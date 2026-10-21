---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/krm/vertex-ai-prediction-krm-ref/
title: KRM API prediction.aiplatform.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:56.022899+00:00
---

# KRM API prediction.aiplatform.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/krm/vertex-ai-prediction-krm-ref/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API prediction.aiplatform.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## prediction.aiplatform.gdc.goog/v1

Package v1 contains API Schema definitions for the prediction.aiplatform.gdc.goog v1 API group.

### Autoscaling

Defines the autoscaling parameters for a deployment.

_Appears in:_

  * DedicatedResources

Field | Description  
---|---  
`minReplica` _integer_ | Number of minimum replicas. The default value is `1`. The next tag is `5`.  
`maxReplica` _integer_ | Number of maximum replicas.  
`cpuTarget` _integer_ | The threshold of CPU usage for scaling up a pod.  
`gpuDutyCycleTarget` _integer_ | The threshold of GPU duty-cycle utilization for scaling up a pod. Not supported on GDC Online Prediction.  
  
### DedicatedResources

Defines the resources that are dedicated to a resource pool. The next ID is `8`.

_Appears in:_

  * ResourcePoolSpec

Field | Description  
---|---  
`machineSpec` | Not required. Specifies the configuration of a single machine using the `machineType` value. If not provided, a default value is used. For Prediction, the default machine type for a deployment is `n1-standard-2` (GKE-based models) or `n2-standard-2-gdc` (CPU-based models).  
`autoscaling` _Autoscaling_ | Specifies the autoscaling parameters for the user workloads, for example, the predictor deployment for prediction.  
  
### DeployedModel

Defines the Schema for the `DeployedModels` API.

_Appears in:_

  * DeployedModelList

Field | Description  
---|---  
`apiVersion` _string_ | `prediction.aiplatform.gdc.goog/v1`  
`kind` _string_ | `DeployedModel`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _DeployedModelSpec_ |   
`status` _DeployedModelStatus_ |   
  
### DeployedModelList

Contains a list of `DeployedModel` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `prediction.aiplatform.gdc.goog/v1`  
`kind` _string_ | `DeployedModelList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _DeployedModel array_ |   
  
### DeployedModelSpec

Defines the expected state of `DeployedModel` resources.

_Appears in:_

  * DeployedModel

Field | Description  
---|---  
`endpointPath` _string_ | Specifies the resource name of the endpoint. The format is `projects/{project}/locations/{location}/endpoints/{endpoint-id}`. The next tag is `6`.  
`modelSpec` _invalid type_ | Defines the model specification needed when deploying the model.  
`resourcePoolRef` _[ObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectreference-v1-core)_ | Specifies the reference of the resource pool with the resource specifications required for this `DeployedModel`.  
`sharesResourcePool` _boolean_ | Specifies if the `DeployedModel` shares a resource pool with other models.  
  
### DeployedModelStatus

Defines the observed state of the `DeployedModel` resource.

_Appears in:_

  * DeployedModel

Field | Description  
---|---  
`ready` _boolean_ | Indicates whether the resource is in a ready state.  
`primaryCondition` | Represents the primary condition of a resource. If the resource is ready, then the condition indicates the resource is ready. Otherwise, the condition is the primary reason why the resource is not ready.  
`resourceConditions` _array_ | Represents a collection of conditions for a resource and its subresources. You can use it to determine the overall health of a resource and its subresources.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Represents raw resource conditions populated from Kubernetes resources for debugging purposes.  
`routes` _Routes_ | Represents the container or system routes for the deployed model prediction or health check.  
`ports` _Ports_ | Represents the container HTTP or gRPC ports.  
`rpcStatus` _RpcStatus_ | Indicates a canonical RPC representation of the deployed model's primary condition.  
`observedGeneration` _integer_ | Indicates the revision of the resource that was most recently reconciled.  
  
### Ports

_Appears in:_

  * DeployedModelStatus

Field | Description  
---|---  
`predictorPorts` _integer array_ | Lists the HTTP ports to expose from the predictor. Requests aren't forwarded to ports other than the first one listed. This field corresponds to the `ports` field of the Kubernetes Containers [v1 core API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#container-v1-core).  
`predictorGRPCPorts` _integer array_ | Lists the gRPC ports to expose from the predictor. If this field is omitted, then the gRPC requests to the container are disabled. Requests aren't forwarded to ports other than the first one listed. This field corresponds to the `ports` field of the Kubernetes Containers [v1 core API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#container-v1-core).  
  
### ReplicaStatus

Defines the replica information of the `ResourcePool` resource.

_Appears in:_

  * ResourcePoolStatus

Field | Description  
---|---  
`resourceType` _ResourceType_ | Specifies the type of the resource.  
`resourceName` _string_ | Indicates the unique resource name in the namespace of the resource type. For example, a `Deployment` `ResourceType` has the Kubernetes deployment name as its resource name.  
`resourceNamespace` _string_ | Indicates the namespace of the resource. This field is not applicable for cluster-scoped resources.  
`appType` _string_ | Indicates the application type of the resource, defined by a specific product. For example, Prediction supports `predictor` and `explainer` as `appType`.  
`availableReplicas` _integer_ | Indicates the total number of available replicas. For Kubernetes deployment resource type, this field represents the total number of available pods, ready for at least a minimum of ready seconds, targeted by this deployment.  
`unavailableReplicas` _integer_ | Indicates the total number of unavailable replicas. For Kubernetes deployment resource type, it represents the total number of unavailable pods targeted by the deployment.  
  
### ResourcePool

Defines the Schema for the `ResourcePools` API.

_Appears in:_

  * ResourcePoolList

Field | Description  
---|---  
`apiVersion` _string_ | `prediction.aiplatform.gdc.goog/v1`  
`kind` _string_ | `ResourcePool`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ResourcePoolSpec_ |   
`status` _ResourcePoolStatus_ |   
  
### ResourcePoolList

Contains a list of `ResourcePool` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `prediction.aiplatform.gdc.goog/v1`  
`kind` _string_ | `ResourcePoolList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ResourcePool array_ |   
  
### ResourcePoolSpec

Defines the expected state of `ResourcePool` resources.

_Appears in:_

  * ResourcePool

Field | Description  
---|---  
`resourcePoolID` _string_ | Represents the system-generated ID of the `ResourcePool` resource. This field is only applicable for Google Cloud and GDCE. The next tag is `8`.  
`userProvidedID` _string_ | Represents the user-provided ID of the `ResourcePool` resource. This field is only applicable for Google Cloud and GDCE.  
`dedicatedResources` _DedicatedResources_ | Contains a description of resources that are dedicated to the resource pool.  
`enableContainerLogging` _boolean_ | Indicates whether or not container logging is enabled for the `ResourcePool`.  
`userGsa` _string_ | Indicates the user-provided IAM service account in the user project. If not specified, the default serving service account is used.  
`customKsaName` _string_ | Specifies the custom name that the operator creates and the user workload uses for bring your own service account (BYOSA) cases only. If empty, the system uses the default naming pattern.  
`rolloutStrategy` _invalid type_ | Specifies whether models deployed to this pool must be rolled out to the model server replicas gradually or all at once.  
  
### ResourcePoolStatus

Defines the observed state of `ResourcePool` resources.

_Appears in:_

  * ResourcePool

Field | Description  
---|---  
`ready` _boolean_ | Indicates whether the resource is in a ready state.  
`primaryCondition` | Represents the primary condition of a resource. If the resource is ready, then the condition indicates the resource is ready. Otherwise, the condition is the primary reason why the resource is not ready.  
`resourceConditions` | Represents a collection of conditions for a resource and its subresources. You can use it to determine the overall health of a resource and its subresources.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Represents raw resource conditions populated from Kubernetes resources for debugging purposes.  
`replicaStatuses` _ReplicaStatus array_ |   
`rpcStatus` _RpcStatus_ | Indicates a canonical RPC representation of the ResourcePool's primary condition.  
`observedGeneration` _integer_ | Indicates what revision of the resource was most recently reconciled.  
  
### Routes

_Appears in:_

  * DeployedModelStatus

Field | Description  
---|---  
`predictRoute` _string_ | Represents the routing path on the container to send prediction requests. Vertex AI forwards requests using `projects.locations.endpoints.predict` to this path on the container's IP address and port. Vertex AI then returns the container's response in the API response.  
`predictSystemRoute` _string_ | Represents the system routing path to send prediction requests to the cluster ingress. This field is populated internally only when it is copied to the `deployedModel` during deployment.  
`healthRoute` _string_ | Represents the routing path on the container to send health checks. Vertex AI intermittently sends GET requests to this path on the container's IP address and port to check that the container is healthy.  
`healthSystemRoute` _string_ | Represents the system routing path to send health check requests to the cluster ingress. This field is populated internally only when it is copied to the `deployedModel` during deployment.  
  
### RpcStatus

Encapsulates an RPC code and a message.

_Appears in:_

  * DeployedModelStatus

Field | Description  
---|---  
`code` _Code_ | Represents the RPC code. The next tag is `4`.  
`message` _string_ | Contains a user-facing description of the condition.  
`terminalState` _boolean_ | Indicates a value of `true` if the resource has reached a terminal state and it cannot become ready.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
