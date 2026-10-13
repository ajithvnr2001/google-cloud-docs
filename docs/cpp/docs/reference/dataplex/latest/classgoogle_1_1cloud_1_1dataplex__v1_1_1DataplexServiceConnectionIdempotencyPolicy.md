---
url: https://docs.cloud.google.com/cpp/docs/reference/dataplex/latest/classgoogle_1_1cloud_1_1dataplex__v1_1_1DataplexServiceConnectionIdempotencyPolicy/
title: Class DataplexServiceConnectionIdempotencyPolicy (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:50.229277+00:00
---

# Class DataplexServiceConnectionIdempotencyPolicy (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/dataplex/latest/classgoogle_1_1cloud_1_1dataplex__v1_1_1DataplexServiceConnectionIdempotencyPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class DataplexServiceConnectionIdempotencyPolicy (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

## Functions 

### virtual clone() const

Create a new copy of this object. 

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< DataplexServiceConnectionIdempotencyPolicy >` |   
  
### virtual CreateLake(google::cloud::dataplex::v1::CreateLakeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::CreateLakeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateLake(google::cloud::dataplex::v1::UpdateLakeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::UpdateLakeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteLake(google::cloud::dataplex::v1::DeleteLakeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::DeleteLakeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListLakes(google::cloud::dataplex::v1::ListLakesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::ListLakesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetLake(google::cloud::dataplex::v1::GetLakeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::GetLakeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListLakeActions(google::cloud::dataplex::v1::ListLakeActionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::ListLakeActionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateZone(google::cloud::dataplex::v1::CreateZoneRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::CreateZoneRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateZone(google::cloud::dataplex::v1::UpdateZoneRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::UpdateZoneRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteZone(google::cloud::dataplex::v1::DeleteZoneRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::DeleteZoneRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListZones(google::cloud::dataplex::v1::ListZonesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::ListZonesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetZone(google::cloud::dataplex::v1::GetZoneRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::GetZoneRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListZoneActions(google::cloud::dataplex::v1::ListZoneActionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::ListZoneActionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateAsset(google::cloud::dataplex::v1::CreateAssetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::CreateAssetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateAsset(google::cloud::dataplex::v1::UpdateAssetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::UpdateAssetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteAsset(google::cloud::dataplex::v1::DeleteAssetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::DeleteAssetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListAssets(google::cloud::dataplex::v1::ListAssetsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::ListAssetsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetAsset(google::cloud::dataplex::v1::GetAssetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::GetAssetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListAssetActions(google::cloud::dataplex::v1::ListAssetActionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::ListAssetActionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateTask(google::cloud::dataplex::v1::CreateTaskRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::CreateTaskRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateTask(google::cloud::dataplex::v1::UpdateTaskRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::UpdateTaskRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteTask(google::cloud::dataplex::v1::DeleteTaskRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::DeleteTaskRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListTasks(google::cloud::dataplex::v1::ListTasksRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::ListTasksRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetTask(google::cloud::dataplex::v1::GetTaskRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::GetTaskRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListJobs(google::cloud::dataplex::v1::ListJobsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::ListJobsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual RunTask(google::cloud::dataplex::v1::RunTaskRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::RunTaskRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetJob(google::cloud::dataplex::v1::GetJobRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::GetJobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CancelJob(google::cloud::dataplex::v1::CancelJobRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::dataplex::v1::CancelJobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
