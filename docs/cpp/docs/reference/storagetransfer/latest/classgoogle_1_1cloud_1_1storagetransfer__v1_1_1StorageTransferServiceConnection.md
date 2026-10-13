---
url: https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1_1_1StorageTransferServiceConnection/
title: Class StorageTransferServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:33.529981+00:00
---

# Class StorageTransferServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1_1_1StorageTransferServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class StorageTransferServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`StorageTransferServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1_1_1StorageTransferServiceConnection) object for [`StorageTransferServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1_1_1StorageTransferServiceClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`StorageTransferServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1_1_1StorageTransferServiceClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`StorageTransferServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1_1_1StorageTransferServiceClient).

To create a concrete instance, see [`MakeStorageTransferServiceConnection()`](https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/namespacegoogle_1_1cloud_1_1storagetransfer__v1).

For mocking, see [`storagetransfer_v1_mocks::MockStorageTransferServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1__mocks_1_1MockStorageTransferServiceConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual GetGoogleServiceAccount(google::storagetransfer::v1::GetGoogleServiceAccountRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::GetGoogleServiceAccountRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::GoogleServiceAccount >` |   
  
### virtual CreateTransferJob(google::storagetransfer::v1::CreateTransferJobRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::CreateTransferJobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::TransferJob >` |   
  
### virtual UpdateTransferJob(google::storagetransfer::v1::UpdateTransferJobRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::UpdateTransferJobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::TransferJob >` |   
  
### virtual GetTransferJob(google::storagetransfer::v1::GetTransferJobRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::GetTransferJobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::TransferJob >` |   
  
### virtual ListTransferJobs(google::storagetransfer::v1::ListTransferJobsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::ListTransferJobsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storagetransfer::v1::TransferJob >` |   
  
### virtual PauseTransferOperation(google::storagetransfer::v1::PauseTransferOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::PauseTransferOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual ResumeTransferOperation(google::storagetransfer::v1::ResumeTransferOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::ResumeTransferOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual RunTransferJob(google::storagetransfer::v1::RunTransferJobRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::RunTransferJobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storagetransfer::v1::TransferOperation > >` |   
  
### virtual RunTransferJob(NoAwaitTag, google::storagetransfer::v1::RunTransferJobRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::storagetransfer::v1::RunTransferJobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RunTransferJob(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storagetransfer::v1::TransferOperation > >` |   
  
### virtual DeleteTransferJob(google::storagetransfer::v1::DeleteTransferJobRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::DeleteTransferJobRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CreateAgentPool(google::storagetransfer::v1::CreateAgentPoolRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::CreateAgentPoolRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` |   
  
### virtual UpdateAgentPool(google::storagetransfer::v1::UpdateAgentPoolRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::UpdateAgentPoolRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` |   
  
### virtual GetAgentPool(google::storagetransfer::v1::GetAgentPoolRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::GetAgentPoolRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` |   
  
### virtual ListAgentPools(google::storagetransfer::v1::ListAgentPoolsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::ListAgentPoolsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storagetransfer::v1::AgentPool >` |   
  
### virtual DeleteAgentPool(google::storagetransfer::v1::DeleteAgentPoolRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::DeleteAgentPoolRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
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
