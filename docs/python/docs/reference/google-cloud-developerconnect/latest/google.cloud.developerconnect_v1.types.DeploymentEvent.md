---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeploymentEvent
title: Class DeploymentEvent (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:31.406714+00:00
---

# Class DeploymentEvent (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeploymentEvent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeploymentEvent (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    DeploymentEvent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The DeploymentEvent resource represents the deployment of the artifact within the InsightsConfig resource.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The name of the DeploymentEvent. This name is provided by Developer Connect insights. Format: projects/{project}/locations/{location}/insightsConfigs/{insights_config}/deploymentEvents/{uuid}   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The create time of the DeploymentEvent.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The update time of the DeploymentEvent.   
`runtime_config` |  `[google.cloud.developerconnect_v1.types.RuntimeConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.RuntimeConfig)`   
Output only. The runtime configurations where the DeploymentEvent happened.   
`runtime_deployment_uri` |  `str`   
Output only. The runtime assigned URI of the DeploymentEvent. For GKE, this is the fully qualified replica set uri. e.g. container.googleapis.com/projects/{project}/locations/{location}/clusters/{cluster}/k8s/namespaces/{namespace}/apps/replicasets/{replica-set-id} For Cloud Run, this is the revision name.   
`state` |  `[google.cloud.developerconnect_v1.types.DeploymentEvent.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeploymentEvent.State)`   
Output only. The state of the DeploymentEvent.   
`artifact_deployments` |  `MutableSequence[[google.cloud.developerconnect_v1.types.ArtifactDeployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ArtifactDeployment)]`   
Output only. The artifact deployments of the DeploymentEvent. Each artifact deployment contains the artifact uri and the runtime configuration uri. For GKE, this would be all the containers images that are deployed in the pod.   
`deploy_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the DeploymentEvent was deployed. This would be the min of all ArtifactDeployment deploy_times.   
`undeploy_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the DeploymentEvent was undeployed, all artifacts are considered undeployed once this time is set. This would be the max of all ArtifactDeployment undeploy_times. If any ArtifactDeployment is still active (i.e. does not have an undeploy_time), this field will be empty.   
  
## Classes 

### State
    
    
    State(value)

The state of the DeploymentEvent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
