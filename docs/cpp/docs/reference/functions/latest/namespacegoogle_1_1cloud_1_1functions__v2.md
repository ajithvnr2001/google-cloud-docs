---
url: https://docs.cloud.google.com/cpp/docs/reference/functions/latest/namespacegoogle_1_1cloud_1_1functions__v2/
title: Namespace google::cloud::functions_v2 (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:04.224083+00:00
---

# Namespace google::cloud::functions_v2 (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/functions/latest/namespacegoogle_1_1cloud_1_1functions__v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Namespace google::cloud::functions_v2 (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

## Classes 

### [FunctionServiceClient](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceClient)

Google Cloud Functions is used to deploy functions that are executed by Google in response to various events. 

### [FunctionServiceConnection](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnection)

The [`FunctionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnection) object for [`FunctionServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceClient). 

### [FunctionServiceConnectionIdempotencyPolicy](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnectionIdempotencyPolicy)

### [FunctionServiceLimitedErrorCountRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceLimitedErrorCountRetryPolicy)

A retry policy for [`FunctionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnection) based on counting errors. 

### [FunctionServiceLimitedTimeRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceLimitedTimeRetryPolicy)

A retry policy for [`FunctionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnection) based on elapsed time. 

### [FunctionServiceRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceRetryPolicy)

The retry policy for [`FunctionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnection). 

## Structs 

### [FunctionServiceBackoffPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/structgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceBackoffPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the backoff policy. 

### [FunctionServiceConnectionIdempotencyPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/structgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnectionIdempotencyPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure which operations are retried. 

### [FunctionServicePollingPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/structgoogle_1_1cloud_1_1functions__v2_1_1FunctionServicePollingPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the long-running operations polling policy. 

### [FunctionServiceRetryPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/structgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceRetryPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the retry policy. 

## Functions 

### MakeFunctionServiceConnection(Options)

A factory function to construct an object of type [`FunctionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnection). 

The returned connection object should not be used directly; instead it should be passed as an argument to the constructor of [FunctionServiceClient](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceClient).

The optional `options` argument may be used to configure aspects of the returned [`FunctionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnection). Expected options are any of the types in the following option lists:

  * [`google::cloud::CommonOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::GrpcOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::UnifiedCredentialsOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::functions_v2::FunctionServicePolicyOptionList`](about:invalid#zCSafez)

**Note:** Unexpected options will be ignored. To log unexpected options instead, set `GOOGLE_CLOUD_CPP_ENABLE_CLOG=yes` in the environment. 

**Parameter**  
---  
**Name** | **Description**  
`options` | `Options`  
(optional) Configure the [`FunctionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/functions/latest/classgoogle_1_1cloud_1_1functions__v2_1_1FunctionServiceConnection) created by this function.   
**Returns**  
---  
**Type** | **Description**  
`std::shared_ptr< FunctionServiceConnection >` |   
  
### MakeDefaultFunctionServiceConnectionIdempotencyPolicy()

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< FunctionServiceConnectionIdempotencyPolicy >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
