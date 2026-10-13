---
url: https://docs.cloud.google.com/cpp/docs/reference/memcache/latest/classgoogle_1_1cloud_1_1memcache__v1_1_1CloudMemcacheConnection/
title: Class CloudMemcacheConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:25.515224+00:00
---

# Class CloudMemcacheConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/memcache/latest/classgoogle_1_1cloud_1_1memcache__v1_1_1CloudMemcacheConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class CloudMemcacheConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`CloudMemcacheConnection`](https://docs.cloud.google.com/cpp/docs/reference/memcache/latest/classgoogle_1_1cloud_1_1memcache__v1_1_1CloudMemcacheConnection) object for [`CloudMemcacheClient`](https://docs.cloud.google.com/cpp/docs/reference/memcache/latest/classgoogle_1_1cloud_1_1memcache__v1_1_1CloudMemcacheClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`CloudMemcacheClient`](https://docs.cloud.google.com/cpp/docs/reference/memcache/latest/classgoogle_1_1cloud_1_1memcache__v1_1_1CloudMemcacheClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`CloudMemcacheClient`](https://docs.cloud.google.com/cpp/docs/reference/memcache/latest/classgoogle_1_1cloud_1_1memcache__v1_1_1CloudMemcacheClient).

To create a concrete instance, see [`MakeCloudMemcacheConnection()`](https://docs.cloud.google.com/cpp/docs/reference/memcache/latest/namespacegoogle_1_1cloud_1_1memcache__v1).

For mocking, see [`memcache_v1_mocks::MockCloudMemcacheConnection`](https://docs.cloud.google.com/cpp/docs/reference/memcache/latest/classgoogle_1_1cloud_1_1memcache__v1__mocks_1_1MockCloudMemcacheConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ListInstances(google::cloud::memcache::v1::ListInstancesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::memcache::v1::ListInstancesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::memcache::v1::Instance >` |   
  
### virtual GetInstance(google::cloud::memcache::v1::GetInstanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::memcache::v1::GetInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::memcache::v1::Instance >` |   
  
### virtual CreateInstance(google::cloud::memcache::v1::CreateInstanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::memcache::v1::CreateInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual CreateInstance(NoAwaitTag, google::cloud::memcache::v1::CreateInstanceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::memcache::v1::CreateInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateInstance(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual UpdateInstance(google::cloud::memcache::v1::UpdateInstanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::memcache::v1::UpdateInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual UpdateInstance(NoAwaitTag, google::cloud::memcache::v1::UpdateInstanceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::memcache::v1::UpdateInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateInstance(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual UpdateParameters(google::cloud::memcache::v1::UpdateParametersRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::memcache::v1::UpdateParametersRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual UpdateParameters(NoAwaitTag, google::cloud::memcache::v1::UpdateParametersRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::memcache::v1::UpdateParametersRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateParameters(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual DeleteInstance(google::cloud::memcache::v1::DeleteInstanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::memcache::v1::DeleteInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::OperationMetadata > >` |   
  
### virtual DeleteInstance(NoAwaitTag, google::cloud::memcache::v1::DeleteInstanceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::memcache::v1::DeleteInstanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteInstance(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::OperationMetadata > >` |   
  
### virtual ApplyParameters(google::cloud::memcache::v1::ApplyParametersRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::memcache::v1::ApplyParametersRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual ApplyParameters(NoAwaitTag, google::cloud::memcache::v1::ApplyParametersRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::memcache::v1::ApplyParametersRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ApplyParameters(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual RescheduleMaintenance(google::cloud::memcache::v1::RescheduleMaintenanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::memcache::v1::RescheduleMaintenanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual RescheduleMaintenance(NoAwaitTag, google::cloud::memcache::v1::RescheduleMaintenanceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::memcache::v1::RescheduleMaintenanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RescheduleMaintenance(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::memcache::v1::Instance > >` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::location::Location >` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::location::Location >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
