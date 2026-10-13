---
url: https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/namespacegoogle_1_1cloud_1_1biglake__hive__v1/
title: Namespace google::cloud::biglake_hive_v1 (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:58.601745+00:00
---

# Namespace google::cloud::biglake_hive_v1 (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/namespacegoogle_1_1cloud_1_1biglake__hive__v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Namespace google::cloud::biglake_hive_v1 (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0 

## Classes 

### [HiveMetastoreServiceClient](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceClient)

Hive Metastore Service is a biglake service that allows users to manage their external Hive catalogs. 

### [HiveMetastoreServiceConnection](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnection)

The [`HiveMetastoreServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnection) object for [`HiveMetastoreServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceClient). 

### [HiveMetastoreServiceConnectionIdempotencyPolicy](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnectionIdempotencyPolicy)

### [HiveMetastoreServiceLimitedErrorCountRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceLimitedErrorCountRetryPolicy)

A retry policy for [`HiveMetastoreServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnection) based on counting errors. 

### [HiveMetastoreServiceLimitedTimeRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceLimitedTimeRetryPolicy)

A retry policy for [`HiveMetastoreServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnection) based on elapsed time. 

### [HiveMetastoreServiceRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceRetryPolicy)

The retry policy for [`HiveMetastoreServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnection). 

## Structs 

### [HiveMetastoreServiceBackoffPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/structgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceBackoffPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the backoff policy. 

### [HiveMetastoreServiceConnectionIdempotencyPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/structgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnectionIdempotencyPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure which operations are retried. 

### [HiveMetastoreServiceRetryPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/structgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceRetryPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the retry policy. 

## Functions 

### MakeHiveMetastoreServiceConnection(Options)

A factory function to construct an object of type [`HiveMetastoreServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnection). 

The returned connection object should not be used directly; instead it should be passed as an argument to the constructor of [HiveMetastoreServiceClient](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceClient).

The optional `options` argument may be used to configure aspects of the returned [`HiveMetastoreServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnection). Expected options are any of the types in the following option lists:

  * [`google::cloud::CommonOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::GrpcOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::UnifiedCredentialsOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::biglake_hive_v1::HiveMetastoreServicePolicyOptionList`](about:invalid#zCSafez)

**Note:** Unexpected options will be ignored. To log unexpected options instead, set `GOOGLE_CLOUD_CPP_ENABLE_CLOG=yes` in the environment. 

**Parameter**  
---  
**Name** | **Description**  
`options` | `Options`  
(optional) Configure the [`HiveMetastoreServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1_1_1HiveMetastoreServiceConnection) created by this function.   
**Returns**  
---  
**Type** | **Description**  
`std::shared_ptr< HiveMetastoreServiceConnection >` |   
  
### MakeDefaultHiveMetastoreServiceConnectionIdempotencyPolicy()

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< HiveMetastoreServiceConnectionIdempotencyPolicy >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
