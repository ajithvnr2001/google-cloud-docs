---
url: https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1_1_1StorageTransferServiceClient/
title: Class StorageTransferServiceClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:44.537158+00:00
---

# Class StorageTransferServiceClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storagetransfer/latest/classgoogle_1_1cloud_1_1storagetransfer__v1_1_1StorageTransferServiceClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class StorageTransferServiceClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Storage Transfer Service and its protos. 

Transfers data between between Google Cloud Storage buckets or from a data source external to Google to a Cloud Storage bucket.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### StorageTransferServiceClient(StorageTransferServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `StorageTransferServiceClient const &`   
  
  
### StorageTransferServiceClient(StorageTransferServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `StorageTransferServiceClient &&`   
  
  
### StorageTransferServiceClient(std::shared_ptr< StorageTransferServiceConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< StorageTransferServiceConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(StorageTransferServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `StorageTransferServiceClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StorageTransferServiceClient &` |   
  
### operator=(StorageTransferServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `StorageTransferServiceClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`StorageTransferServiceClient &` |   
  
## Functions 

### GetGoogleServiceAccount(google::storagetransfer::v1::GetGoogleServiceAccountRequest const &, Options)

Returns the Google service account that is used by Storage Transfer Service to access buckets in the project where transfers run or in other projects. 

Each Google service account is associated with one Google Cloud project. Users should add this service account to the Google Cloud Storage bucket ACLs to grant access to Storage Transfer Service. This service account is created and owned by Storage Transfer Service and can only be used by Storage Transfer Service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::GetGoogleServiceAccountRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.GetGoogleServiceAccountRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L183). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::GoogleServiceAccount >` | the result of the RPC. The response message type ([google.storagetransfer.v1.GoogleServiceAccount](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L35)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateTransferJob(google::storagetransfer::v1::CreateTransferJobRequest const &, Options)

Creates a transfer job that runs periodically. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::CreateTransferJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.CreateTransferJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L190). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::TransferJob >` | the result of the RPC. The response message type ([google.storagetransfer.v1.TransferJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1045)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateTransferJob(google::storagetransfer::v1::UpdateTransferJobRequest const &, Options)

Updates a transfer job. 

Updating a job's transfer spec does not affect transfer operations that are running already.

**Note:** The job's [status](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1146) field can be modified using this RPC (for example, to set a job's status to [DELETED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1061), [DISABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1055), or [ENABLED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1052)).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::UpdateTransferJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.UpdateTransferJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L196). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::TransferJob >` | the result of the RPC. The response message type ([google.storagetransfer.v1.TransferJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1045)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetTransferJob(google::storagetransfer::v1::GetTransferJobRequest const &, Options)

Gets a transfer job. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::GetTransferJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.GetTransferJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L233). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::TransferJob >` | the result of the RPC. The response message type ([google.storagetransfer.v1.TransferJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1045)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListTransferJobs(google::storagetransfer::v1::ListTransferJobsRequest, Options)

Lists transfer jobs. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::ListTransferJobsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.ListTransferJobsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L254). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storagetransfer::v1::TransferJob >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.storagetransfer.v1.TransferJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1045), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PauseTransferOperation(google::storagetransfer::v1::PauseTransferOperationRequest const &, Options)

Pauses a transfer operation. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::PauseTransferOperationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.PauseTransferOperationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L301). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### ResumeTransferOperation(google::storagetransfer::v1::ResumeTransferOperationRequest const &, Options)

Resumes a transfer operation that is paused. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::ResumeTransferOperationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.ResumeTransferOperationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L307). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### RunTransferJob(google::storagetransfer::v1::RunTransferJobRequest const &, Options)

Starts a new operation for the specified transfer job. 

A `TransferJob` has a maximum of one active `TransferOperation`. If this method is called while a `TransferOperation` is active, an error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::RunTransferJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.RunTransferJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L313). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storagetransfer::v1::TransferOperation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.storagetransfer.v1.TransferOperation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1409) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### RunTransferJob(NoAwaitTag, google::storagetransfer::v1::RunTransferJobRequest const &, Options)

Starts a new operation for the specified transfer job. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::storagetransfer::v1::RunTransferJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### RunTransferJob(google::longrunning::Operation const &, Options)

Starts a new operation for the specified transfer job. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::storagetransfer::v1::TransferOperation > >` |   
  
### DeleteTransferJob(google::storagetransfer::v1::DeleteTransferJobRequest const &, Options)

Deletes a transfer job. 

Deleting a transfer job sets its status to [DELETED](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L1061).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::DeleteTransferJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.DeleteTransferJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L243). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### CreateAgentPool(std::string const &, google::storagetransfer::v1::AgentPool const &, std::string const &, Options)

Creates an agent pool resource. 

**Parameters**  
---  
**Name** | **Description**  
`project_id` |  `std::string const &`   
Required. The ID of the Google Cloud project that owns the agent pool.   
`agent_pool` |  `google::storagetransfer::v1::AgentPool const &`   
Required. The agent pool to create.   
`agent_pool_id` |  `std::string const &`   
Required. The ID of the agent pool to create.   
The `agent_pool_id` must meet the following requirements:   


  * Length of 128 characters or less.
  * Not start with the string `goog`.
  * Start with a lowercase ASCII character, followed by:
    * Zero or more: lowercase Latin alphabet characters, numerals, hyphens (`-`), periods (`.`), underscores (`_`), or tildes (`~`).
    * One or more numerals or lowercase ASCII characters.   
As expressed by the regular expression: `^(?!goog)[a-z]([a-z0-9-._~]*[a-z0-9])?$`. 

  
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` | the result of the RPC. The response message type ([google.storagetransfer.v1.AgentPool](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L556)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateAgentPool(google::storagetransfer::v1::CreateAgentPoolRequest const &, Options)

Creates an agent pool resource. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::CreateAgentPoolRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.CreateAgentPoolRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L323). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` | the result of the RPC. The response message type ([google.storagetransfer.v1.AgentPool](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L556)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateAgentPool(google::storagetransfer::v1::AgentPool const &, google::protobuf::FieldMask const &, Options)

Updates an existing agent pool resource. 

**Parameters**  
---  
**Name** | **Description**  
`agent_pool` |  `google::storagetransfer::v1::AgentPool const &`   
Required. The agent pool to update. `agent_pool` is expected to specify following fields:   


  * [name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L590)  

  * [display_name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L593)  

  * [bandwidth_limit](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L600) An `UpdateAgentPoolRequest` with any other fields is rejected with the error [INVALID_ARGUMENT](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/rpc/code.proto#L58). 

  
`update_mask` |  `google::protobuf::FieldMask const &`   
The [field mask](about:invalid#zCSafez) of the fields in `agentPool` to update in this request. The following `agentPool` fields can be updated:   


  * [display_name](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L593)  

  * [bandwidth_limit](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L600)

  
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` | the result of the RPC. The response message type ([google.storagetransfer.v1.AgentPool](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L556)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateAgentPool(google::storagetransfer::v1::UpdateAgentPoolRequest const &, Options)

Updates an existing agent pool resource. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::UpdateAgentPoolRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.UpdateAgentPoolRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L348). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` | the result of the RPC. The response message type ([google.storagetransfer.v1.AgentPool](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L556)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetAgentPool(std::string const &, Options)

Gets an agent pool. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the agent pool to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` | the result of the RPC. The response message type ([google.storagetransfer.v1.AgentPool](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L556)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetAgentPool(google::storagetransfer::v1::GetAgentPoolRequest const &, Options)

Gets an agent pool. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::GetAgentPoolRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.GetAgentPoolRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L373). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::storagetransfer::v1::AgentPool >` | the result of the RPC. The response message type ([google.storagetransfer.v1.AgentPool](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L556)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListAgentPools(std::string const &, Options)

Lists agent pools. 

**Parameters**  
---  
**Name** | **Description**  
`project_id` |  `std::string const &`   
Required. The ID of the Google Cloud project that owns the job.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storagetransfer::v1::AgentPool >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.storagetransfer.v1.AgentPool](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L556), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListAgentPools(google::storagetransfer::v1::ListAgentPoolsRequest, Options)

Lists agent pools. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::ListAgentPoolsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.ListAgentPoolsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L385). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::storagetransfer::v1::AgentPool >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.storagetransfer.v1.AgentPool](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer_types.proto#L556), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteAgentPool(std::string const &, Options)

Deletes an agent pool. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the agent pool to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteAgentPool(google::storagetransfer::v1::DeleteAgentPoolRequest const &, Options)

Deletes an agent pool. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::storagetransfer::v1::DeleteAgentPoolRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.storagetransfer.v1.DeleteAgentPoolRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/storagetransfer/v1/transfer.proto#L379). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### ListOperations(std::string const &, std::string const &, Options)

Lists operations that match the specified filter in the request. 

If the server doesn't support this method, it returns `UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
The name of the operation's parent resource.   
`filter` |  `std::string const &`   
The standard list filter.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.longrunning.Operation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L121), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListOperations(google::longrunning::ListOperationsRequest, Options)

Lists operations that match the specified filter in the request. 

If the server doesn't support this method, it returns `UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.longrunning.ListOperationsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L167). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.longrunning.Operation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L121), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetOperation(std::string const &, Options)

Gets the latest state of a long-running operation. 

Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
The name of the operation resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` | the result of the RPC. The response message type ([google.longrunning.Operation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L121)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetOperation(google::longrunning::GetOperationRequest const &, Options)

Gets the latest state of a long-running operation. 

Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.longrunning.GetOperationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L160). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` | the result of the RPC. The response message type ([google.longrunning.Operation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L121)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CancelOperation(std::string const &, Options)

Starts asynchronous cancellation on a long-running operation. 

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use [Operations.GetOperation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L70) or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L144) value with a [google.rpc.Status.code](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/rpc/status.proto#L37) of `1`, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
The name of the operation resource to be cancelled.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### CancelOperation(google::longrunning::CancelOperationRequest const &, Options)

Starts asynchronous cancellation on a long-running operation. 

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use [Operations.GetOperation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L70) or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L144) value with a [google.rpc.Status.code](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/rpc/status.proto#L37) of `1`, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.longrunning.CancelOperationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L212). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
