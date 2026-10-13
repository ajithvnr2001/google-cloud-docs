---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateConnectClusterRequest
title: Class CreateConnectClusterRequest (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:27.461775+00:00
---

# Class CreateConnectClusterRequest (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.CreateConnectClusterRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateConnectClusterRequest (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.12 
    
    
    CreateConnectClusterRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for CreateConnectCluster.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent project/location in which to create the Kafka Connect cluster. Structured like `projects/{project}/locations/{location}/`.   
`connect_cluster_id` |  `str`   
Required. The ID to use for the Connect cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035\. This value is structured like: `my-cluster-id`.   
`connect_cluster` |  `[google.cloud.managedkafka_v1.types.ConnectCluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-managedkafka/latest/google.cloud.managedkafka_v1.types.ConnectCluster)`   
Required. Configuration of the Kafka Connect cluster to create. Its `name` field is ignored.   
`request_id` |  `str`   
Optional. An optional request ID to identify requests. Specify a unique request ID to avoid duplication of requests. If a request times out or fails, retrying with the same ID allows the server to recognize the previous attempt. For at least 60 minutes, the server ignores duplicate requests bearing the same ID. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID within 60 minutes of the last request, the server checks if an original operation with the same request ID was received. If so, the server ignores the second request. The request ID must be a valid UUID. A zero UUID is not supported (00000000-0000-0000-0000-000000000000).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
