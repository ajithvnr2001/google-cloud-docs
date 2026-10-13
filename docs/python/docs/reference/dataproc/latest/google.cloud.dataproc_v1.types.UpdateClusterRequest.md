---
url: https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.UpdateClusterRequest
title: Class UpdateClusterRequest (5.31.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:02.265180+00:00
---

# Class UpdateClusterRequest (5.31.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.UpdateClusterRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdateClusterRequest (5.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.31.0 (latest)  5.30.0  5.29.0  5.28.0  5.27.0  5.26.0  5.25.0  5.24.0  5.23.0  5.22.0  5.21.0  5.20.0  5.18.1  5.17.1  5.16.0  5.15.1  5.14.0  5.13.0  5.12.0  5.10.2  5.9.3  5.8.0  5.7.0  5.6.0  5.5.1  5.4.3  5.3.0  5.2.0  5.1.0  5.0.3  4.0.3  3.3.2  3.2.0  3.1.1  3.0.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.0.2  1.1.3  1.0.1  0.8.2  0.7.0  0.6.1  0.5.0 
    
    
    UpdateClusterRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A request to update a cluster.

## Attributes  
  
---  
**Name** | **Description**  
`project_id` |  `str`   
Required. The ID of the Google Cloud Platform project the cluster belongs to.   
`region` |  `str`   
Required. The Dataproc region in which to handle the request.   
`cluster_name` |  `str`   
Required. The cluster name.   
`cluster` |  `[google.cloud.dataproc_v1.types.Cluster](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.Cluster)`   
Required. The changes to the cluster.   
`graceful_decommission_timeout` |  `google.protobuf.duration_pb2.Duration`   
Optional. Timeout for graceful YARN decommissioning. Graceful decommissioning allows removing nodes from the cluster without interrupting jobs in progress. Timeout specifies how long to wait for jobs in progress to finish before forcefully removing nodes (and potentially interrupting jobs). Default timeout is 0 (for forceful decommission), and the maximum allowed timeout is 1 day. (see JSON representation of `Duration `__). Only supported on Dataproc image versions 1.2 and higher.   
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Specifies the path, relative to `Cluster`, of the field to update. For example, to change the number of workers in a cluster to 5, the `update_mask` parameter would be specified as `config.worker_config.num_instances`, and the `PATCH` request body would specify the new value, as follows: :: { "config":{ "workerConfig":{ "numInstances":"5" } } } Similarly, to change the number of preemptible workers in a cluster to 5, the `update_mask` parameter would be `config.secondary_worker_config.num_instances`, and the `PATCH` request body would be set as follows: :: { "config":{ "secondaryWorkerConfig":{ "numInstances":"5" } } } Note: Currently, only the following fields can be updated: .. raw:: html | **Mask** | **Purpose**  
---|---  
**_labels_** | Update labels  
**_config.worker_config.num_instances_** | Resize primary worker group  
**_config.secondary_worker_config.num_instances_** | Resize secondary worker group  
config.autoscaling_config.policy_uri| Use, stop using, or change autoscaling policies  
`request_id` |  `str`   
Optional. A unique ID used to identify the request. If the server receives two `UpdateClusterRequest `__\ s with the same id, then the second request will be ignored and the first `google.longrunning.Operation][google.longrunning.Operation]` created and stored in the backend is returned. It is recommended to always set this value to a `UUID `__. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (\\_), and hyphens (-). The maximum length is 40 characters.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
