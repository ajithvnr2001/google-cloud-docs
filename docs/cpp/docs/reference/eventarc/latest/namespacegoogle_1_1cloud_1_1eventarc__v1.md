---
url: https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/namespacegoogle_1_1cloud_1_1eventarc__v1/
title: Namespace google::cloud::eventarc_v1 (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:27:59.956921+00:00
---

# Namespace google::cloud::eventarc_v1 (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/namespacegoogle_1_1cloud_1_1eventarc__v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Namespace google::cloud::eventarc_v1 (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

## Classes 

### [EventarcClient](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcClient)

Eventarc allows users to subscribe to various events that are provided by Google Cloud services and forward them to supported destinations. 

### [EventarcConnection](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection)

The [`EventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection) object for [`EventarcClient`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcClient). 

### [EventarcConnectionIdempotencyPolicy](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnectionIdempotencyPolicy)

### [EventarcLimitedErrorCountRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcLimitedErrorCountRetryPolicy)

A retry policy for [`EventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection) based on counting errors. 

### [EventarcLimitedTimeRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcLimitedTimeRetryPolicy)

A retry policy for [`EventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection) based on elapsed time. 

### [EventarcRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcRetryPolicy)

The retry policy for [`EventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection). 

## Structs 

### [EventarcBackoffPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/structgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcBackoffPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the backoff policy. 

### [EventarcConnectionIdempotencyPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/structgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnectionIdempotencyPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure which operations are retried. 

### [EventarcPollingPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/structgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcPollingPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the long-running operations polling policy. 

### [EventarcRetryPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/structgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcRetryPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the retry policy. 

## Functions 

### MakeEventarcConnection(Options)

A factory function to construct an object of type [`EventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection). 

The returned connection object should not be used directly; instead it should be passed as an argument to the constructor of [EventarcClient](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcClient).

The optional `options` argument may be used to configure aspects of the returned [`EventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection). Expected options are any of the types in the following option lists:

  * [`google::cloud::CommonOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::GrpcOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::UnifiedCredentialsOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::eventarc_v1::EventarcPolicyOptionList`](about:invalid#zCSafez)

**Note:** Unexpected options will be ignored. To log unexpected options instead, set `GOOGLE_CLOUD_CPP_ENABLE_CLOG=yes` in the environment. 

**Parameter**  
---  
**Name** | **Description**  
`options` | `Options`  
(optional) Configure the [`EventarcConnection`](https://docs.cloud.google.com/cpp/docs/reference/eventarc/latest/classgoogle_1_1cloud_1_1eventarc__v1_1_1EventarcConnection) created by this function.   
**Returns**  
---  
**Type** | **Description**  
`std::shared_ptr< EventarcConnection >` |   
  
### MakeDefaultEventarcConnectionIdempotencyPolicy()

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< EventarcConnectionIdempotencyPolicy >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
