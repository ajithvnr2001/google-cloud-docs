---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/namespacegoogle_1_1cloud_1_1compute__storage__pools__v1/
title: Namespace google::cloud::compute_storage_pools_v1 (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:52.152121+00:00
---

# Namespace google::cloud::compute_storage_pools_v1 (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/namespacegoogle_1_1cloud_1_1compute__storage__pools__v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Namespace google::cloud::compute_storage_pools_v1 (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

## Classes 

### [StoragePoolsClient](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsClient)

Service for the storagePools resource. 

### [StoragePoolsConnection](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnection)

The [`StoragePoolsConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnection) object for [`StoragePoolsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsClient). 

### [StoragePoolsConnectionIdempotencyPolicy](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnectionIdempotencyPolicy)

### [StoragePoolsLimitedErrorCountRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsLimitedErrorCountRetryPolicy)

A retry policy for [`StoragePoolsConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnection) based on counting errors. 

### [StoragePoolsLimitedTimeRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsLimitedTimeRetryPolicy)

A retry policy for [`StoragePoolsConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnection) based on elapsed time. 

### [StoragePoolsRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsRetryPolicy)

The retry policy for [`StoragePoolsConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnection). 

## Structs 

### [StoragePoolsBackoffPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/structgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsBackoffPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the backoff policy. 

### [StoragePoolsConnectionIdempotencyPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/structgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnectionIdempotencyPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure which operations are retried. 

### [StoragePoolsPollingPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/structgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsPollingPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the long-running operations polling policy. 

### [StoragePoolsRetryPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/structgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsRetryPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the retry policy. 

## Functions 

### MakeDefaultStoragePoolsConnectionIdempotencyPolicy()

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< StoragePoolsConnectionIdempotencyPolicy >` |   
  
### MakeStoragePoolsConnectionRest(Options)

A factory function to construct an object of type [`StoragePoolsConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnection) that uses REST over HTTP as transport in lieu of gRPC. 

REST transport should only be used for services that do not support gRPC or if the existing network configuration precludes using gRPC.

The returned connection object should not be used directly; instead it should be passed as an argument to the constructor of [StoragePoolsClient](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsClient).

The optional `options` argument may be used to configure aspects of the returned [`StoragePoolsConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnection). Expected options are any of the types in the following option lists:

  * [`google::cloud::CommonOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::RestOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::UnifiedCredentialsOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::compute_storage_pools_v1::StoragePoolsPolicyOptionList`](about:invalid#zCSafez)

**Note:** Unexpected options will be ignored. To log unexpected options instead, set `GOOGLE_CLOUD_CPP_ENABLE_CLOG=yes` in the environment. 

**Parameter**  
---  
**Name** | **Description**  
`options` | `Options`  
(optional) Configure the [`StoragePoolsConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsConnection) created by this function.   
**Returns**  
---  
**Type** | **Description**  
`std::shared_ptr< StoragePoolsConnection >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
