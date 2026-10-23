---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/mutateDeployedModel/
title: Method: endpoints.mutateDeployedModel \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:21.490829+00:00
---

# Method: endpoints.mutateDeployedModel  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/mutateDeployedModel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: endpoints.mutateDeployedModel Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.endpoints.mutateDeployedModel

Updates an existing deployed model. Updatable fields include `minReplicaCount`, `maxReplicaCount`, `requiredReplicaCount`, `autoscalingMetricSpecs`, `disableContainerLogging` (v1 only), and `enableContainerLogging` (v1beta1 only).

### Endpoint

post  `https://{service-endpoint}/v1/{endpoint}:mutateDeployedModel`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`endpoint` `string` Required. The name of the Endpoint resource into which to mutate a DeployedModel. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

### Request body

The request body contains data with the following structure: | Fields  
  
`deployedModel` `object (`[DeployedModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints#DeployedModel)`)` Required. The DeployedModel to be mutated within the Endpoint. Only the following fields can be mutated:

  * `minReplicaCount` in either `[DedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DedicatedResources)` or `[AutomaticResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/AutomaticResources)`
  * `maxReplicaCount` in either `[DedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DedicatedResources)` or `[AutomaticResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/AutomaticResources)`
  * `requiredReplicaCount` in `[DedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DedicatedResources)`
  * `[autoscalingMetricSpecs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DedicatedResources#FIELDS.autoscaling_metric_specs)`
  * `disableContainerLogging` (v1 only)
  * `enableContainerLogging` (v1beta1 only)
  * `scaleToZeroSpec` in `[DedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DedicatedResources)` (v1beta1 only)
  * `initialReplicaCount` in `[DedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DedicatedResources)` (v1beta1 only)

| `updateMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The update mask applies to the resource. See `[google.protobuf.FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)`.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `endpoint` resource:

  * `aiplatform.endpoints.deploy`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs). Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
