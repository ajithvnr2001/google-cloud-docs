---
url: https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types
title: Package types (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:01.918374+00:00
---

# Package types (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.2  1.7.1  1.6.0  1.5.3  1.4.2  1.3.0  1.2.1  1.1.0  1.0.2  0.1.2 

API documentation for `data_fusion_v1.types` package.

## Classes 

### [Accelerator](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.Accelerator)

Identifies Data Fusion accelerators for an instance.

### [CreateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.CreateInstanceRequest)

Request message for creating a Data Fusion instance.

### [CryptoKeyConfig](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.CryptoKeyConfig)

The crypto key configuration. This field is used by the Customer-managed encryption keys (CMEK) feature.

### [DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.DeleteInstanceRequest)

Request message for deleting a Data Fusion instance.

### [GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.GetInstanceRequest)

Request message for getting details about a Data Fusion instance.

### [Instance](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.Instance)

Represents a Data Fusion instance.

### [ListAvailableVersionsRequest](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.ListAvailableVersionsRequest)

Request message for the list available versions request.

### [ListAvailableVersionsResponse](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.ListAvailableVersionsResponse)

Response message for the list available versions request.

### [ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.ListInstancesRequest)

Request message for listing Data Fusion instances.

### [ListInstancesResponse](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.ListInstancesResponse)

Response message for the list instance request.

### [NetworkConfig](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.NetworkConfig)

Network configuration for a Data Fusion instance. These configurations are used for peering with the customer network. Configurations are optional when a public Data Fusion instance is to be created. However, providing these configurations allows several benefits, such as reduced network latency while accessing the customer resources from managed Data Fusion instance nodes, as well as access to the customer on-prem resources.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.OperationMetadata)

Represents the metadata of a long-running operation.

### [RestartInstanceRequest](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.RestartInstanceRequest)

Request message for restarting a Data Fusion instance.

### [UpdateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.UpdateInstanceRequest)

Request message for updating a Data Fusion instance. Data Fusion allows updating the labels, options, and stack driver settings. This is also used for CDF version upgrade.

### [Version](https://docs.cloud.google.com/python/docs/reference/datafusion/latest/google.cloud.data_fusion_v1.types.Version)

The Data Fusion version. This proto message stores information about certain Data Fusion version, which is used for Data Fusion version upgrade.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
