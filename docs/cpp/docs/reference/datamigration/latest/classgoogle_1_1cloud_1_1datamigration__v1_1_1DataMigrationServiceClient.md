---
url: https://docs.cloud.google.com/cpp/docs/reference/datamigration/latest/classgoogle_1_1cloud_1_1datamigration__v1_1_1DataMigrationServiceClient/
title: Class DataMigrationServiceClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:51.127581+00:00
---

# Class DataMigrationServiceClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/datamigration/latest/classgoogle_1_1cloud_1_1datamigration__v1_1_1DataMigrationServiceClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class DataMigrationServiceClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Database Migration service. 

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### DataMigrationServiceClient(DataMigrationServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DataMigrationServiceClient const &`   
  
  
### DataMigrationServiceClient(DataMigrationServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DataMigrationServiceClient &&`   
  
  
### DataMigrationServiceClient(std::shared_ptr< DataMigrationServiceConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< DataMigrationServiceConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(DataMigrationServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DataMigrationServiceClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`DataMigrationServiceClient &` |   
  
### operator=(DataMigrationServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `DataMigrationServiceClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`DataMigrationServiceClient &` |   
  
## Functions 

### ListMigrationJobs(std::string const &, Options)

Lists migration jobs in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent which owns this collection of migrationJobs.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::MigrationJob >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListMigrationJobs(google::cloud::clouddms::v1::ListMigrationJobsRequest, Options)

Lists migration jobs in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ListMigrationJobsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ListMigrationJobsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L537). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::MigrationJob >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetMigrationJob(std::string const &, Options)

Gets details of a single migration job. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Name of the migration job resource to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::MigrationJob >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetMigrationJob(google::cloud::clouddms::v1::GetMigrationJobRequest const &, Options)

Gets details of a single migration job. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::GetMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.GetMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L589). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::MigrationJob >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateMigrationJob(std::string const &, google::cloud::clouddms::v1::MigrationJob const &, std::string const &, Options)

Creates a new migration job in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent which owns this collection of migration jobs.   
`migration_job` |  `google::cloud::clouddms::v1::MigrationJob const &`   
Required. Represents a [migration job](https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs) object.   
`migration_job_id` |  `std::string const &`   
Required. The ID of the instance to create.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateMigrationJob(NoAwaitTag, std::string const &, google::cloud::clouddms::v1::MigrationJob const &, std::string const &, Options)

Creates a new migration job in a given project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`migration_job` |  `google::cloud::clouddms::v1::MigrationJob const &`   
  
`migration_job_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateMigrationJob(google::cloud::clouddms::v1::CreateMigrationJobRequest const &, Options)

Creates a new migration job in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::CreateMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.CreateMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L601). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::CreateMigrationJobRequest const &, Options)

Creates a new migration job in a given project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::CreateMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateMigrationJob(google::longrunning::Operation const &, Options)

Creates a new migration job in a given project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` |   
  
### UpdateMigrationJob(google::cloud::clouddms::v1::MigrationJob const &, google::protobuf::FieldMask const &, Options)

Updates the parameters of a single migration job. 

**Parameters**  
---  
**Name** | **Description**  
`migration_job` |  `google::cloud::clouddms::v1::MigrationJob const &`   
Required. The migration job parameters to update.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::MigrationJob const &, google::protobuf::FieldMask const &, Options)

Updates the parameters of a single migration job. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`migration_job` |  `google::cloud::clouddms::v1::MigrationJob const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateMigrationJob(google::cloud::clouddms::v1::UpdateMigrationJobRequest const &, Options)

Updates the parameters of a single migration job. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::UpdateMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.UpdateMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L629). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::UpdateMigrationJobRequest const &, Options)

Updates the parameters of a single migration job. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::UpdateMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateMigrationJob(google::longrunning::Operation const &, Options)

Updates the parameters of a single migration job. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` |   
  
### DeleteMigrationJob(std::string const &, Options)

Deletes a single migration job. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Name of the migration job resource to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.OperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteMigrationJob(NoAwaitTag, std::string const &, Options)

Deletes a single migration job. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteMigrationJob(google::cloud::clouddms::v1::DeleteMigrationJobRequest const &, Options)

Deletes a single migration job. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::DeleteMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.DeleteMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L649). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.OperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::DeleteMigrationJobRequest const &, Options)

Deletes a single migration job. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::DeleteMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteMigrationJob(google::longrunning::Operation const &, Options)

Deletes a single migration job. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` |   
  
### StartMigrationJob(google::cloud::clouddms::v1::StartMigrationJobRequest const &, Options)

Start an already created migration job. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::StartMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.StartMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L674). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### StartMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::StartMigrationJobRequest const &, Options)

Start an already created migration job. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::StartMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### StartMigrationJob(google::longrunning::Operation const &, Options)

Start an already created migration job. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` |   
  
### StopMigrationJob(google::cloud::clouddms::v1::StopMigrationJobRequest const &, Options)

Stops a running migration job. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::StopMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.StopMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L686). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### StopMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::StopMigrationJobRequest const &, Options)

Stops a running migration job. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::StopMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### StopMigrationJob(google::longrunning::Operation const &, Options)

Stops a running migration job. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` |   
  
### ResumeMigrationJob(google::cloud::clouddms::v1::ResumeMigrationJobRequest const &, Options)

Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase). 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ResumeMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ResumeMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L694). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ResumeMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::ResumeMigrationJobRequest const &, Options)

Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase). 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::ResumeMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ResumeMigrationJob(google::longrunning::Operation const &, Options)

Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase). 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` |   
  
### PromoteMigrationJob(google::cloud::clouddms::v1::PromoteMigrationJobRequest const &, Options)

Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::PromoteMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.PromoteMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L702). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PromoteMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::PromoteMigrationJobRequest const &, Options)

Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::PromoteMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### PromoteMigrationJob(google::longrunning::Operation const &, Options)

Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` |   
  
### VerifyMigrationJob(google::cloud::clouddms::v1::VerifyMigrationJobRequest const &, Options)

Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::VerifyMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.VerifyMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L710). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### VerifyMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::VerifyMigrationJobRequest const &, Options)

Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::VerifyMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### VerifyMigrationJob(google::longrunning::Operation const &, Options)

Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` |   
  
### RestartMigrationJob(google::cloud::clouddms::v1::RestartMigrationJobRequest const &, Options)

Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::RestartMigrationJobRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.RestartMigrationJobRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L727). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.MigrationJob](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L648) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### RestartMigrationJob(NoAwaitTag, google::cloud::clouddms::v1::RestartMigrationJobRequest const &, Options)

Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::RestartMigrationJobRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### RestartMigrationJob(google::longrunning::Operation const &, Options)

Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::MigrationJob > >` |   
  
### GenerateSshScript(google::cloud::clouddms::v1::GenerateSshScriptRequest const &, Options)

Generate a SSH configuration script to configure the reverse SSH connectivity. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::GenerateSshScriptRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.GenerateSshScriptRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L739). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::SshScript >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.SshScript](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L780)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GenerateTcpProxyScript(google::cloud::clouddms::v1::GenerateTcpProxyScriptRequest const &, Options)

Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::GenerateTcpProxyScriptRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.GenerateTcpProxyScriptRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L786). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::TcpProxyScript >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.TcpProxyScript](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L812)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListConnectionProfiles(std::string const &, Options)

Retrieves a list of all connection profiles in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent which owns this collection of connection profiles.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::ConnectionProfile >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.ConnectionProfile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L896), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListConnectionProfiles(google::cloud::clouddms::v1::ListConnectionProfilesRequest, Options)

Retrieves a list of all connection profiles in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ListConnectionProfilesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ListConnectionProfilesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L818). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::ConnectionProfile >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.ConnectionProfile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L896), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetConnectionProfile(std::string const &, Options)

Gets details of a single connection profile. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Name of the connection profile resource to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::ConnectionProfile >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.ConnectionProfile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L896)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetConnectionProfile(google::cloud::clouddms::v1::GetConnectionProfileRequest const &, Options)

Gets details of a single connection profile. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::GetConnectionProfileRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.GetConnectionProfileRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L869). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::ConnectionProfile >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.ConnectionProfile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L896)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateConnectionProfile(std::string const &, google::cloud::clouddms::v1::ConnectionProfile const &, std::string const &, Options)

Creates a new connection profile in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent which owns this collection of connection profiles.   
`connection_profile` |  `google::cloud::clouddms::v1::ConnectionProfile const &`   
Required. The create request body including the connection profile data   
`connection_profile_id` |  `std::string const &`   
Required. The connection profile identifier.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConnectionProfile > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConnectionProfile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L896) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateConnectionProfile(NoAwaitTag, std::string const &, google::cloud::clouddms::v1::ConnectionProfile const &, std::string const &, Options)

Creates a new connection profile in a given project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`connection_profile` |  `google::cloud::clouddms::v1::ConnectionProfile const &`   
  
`connection_profile_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateConnectionProfile(google::cloud::clouddms::v1::CreateConnectionProfileRequest const &, Options)

Creates a new connection profile in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::CreateConnectionProfileRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.CreateConnectionProfileRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L880). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConnectionProfile > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConnectionProfile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L896) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateConnectionProfile(NoAwaitTag, google::cloud::clouddms::v1::CreateConnectionProfileRequest const &, Options)

Creates a new connection profile in a given project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::CreateConnectionProfileRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateConnectionProfile(google::longrunning::Operation const &, Options)

Creates a new connection profile in a given project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConnectionProfile > >` |   
  
### UpdateConnectionProfile(google::cloud::clouddms::v1::ConnectionProfile const &, google::protobuf::FieldMask const &, Options)

Update the configuration of a single connection profile. 

**Parameters**  
---  
**Name** | **Description**  
`connection_profile` |  `google::cloud::clouddms::v1::ConnectionProfile const &`   
Required. The connection profile parameters to update.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConnectionProfile > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConnectionProfile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L896) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateConnectionProfile(NoAwaitTag, google::cloud::clouddms::v1::ConnectionProfile const &, google::protobuf::FieldMask const &, Options)

Update the configuration of a single connection profile. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`connection_profile` |  `google::cloud::clouddms::v1::ConnectionProfile const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateConnectionProfile(google::cloud::clouddms::v1::UpdateConnectionProfileRequest const &, Options)

Update the configuration of a single connection profile. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::UpdateConnectionProfileRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.UpdateConnectionProfileRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L917). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConnectionProfile > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConnectionProfile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L896) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateConnectionProfile(NoAwaitTag, google::cloud::clouddms::v1::UpdateConnectionProfileRequest const &, Options)

Update the configuration of a single connection profile. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::UpdateConnectionProfileRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateConnectionProfile(google::longrunning::Operation const &, Options)

Update the configuration of a single connection profile. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConnectionProfile > >` |   
  
### DeleteConnectionProfile(std::string const &, Options)

Deletes a single Database Migration Service connection profile. 

A connection profile can only be deleted if it is not in use by any active migration jobs.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Name of the connection profile resource to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.OperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteConnectionProfile(NoAwaitTag, std::string const &, Options)

Deletes a single Database Migration Service connection profile. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteConnectionProfile(google::cloud::clouddms::v1::DeleteConnectionProfileRequest const &, Options)

Deletes a single Database Migration Service connection profile. 

A connection profile can only be deleted if it is not in use by any active migration jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::DeleteConnectionProfileRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.DeleteConnectionProfileRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L948). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.OperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteConnectionProfile(NoAwaitTag, google::cloud::clouddms::v1::DeleteConnectionProfileRequest const &, Options)

Deletes a single Database Migration Service connection profile. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::DeleteConnectionProfileRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteConnectionProfile(google::longrunning::Operation const &, Options)

Deletes a single Database Migration Service connection profile. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` |   
  
### CreatePrivateConnection(std::string const &, google::cloud::clouddms::v1::PrivateConnection const &, std::string const &, Options)

Creates a new private connection in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent that owns the collection of PrivateConnections.   
`private_connection` |  `google::cloud::clouddms::v1::PrivateConnection const &`   
Required. The private connection resource to create.   
`private_connection_id` |  `std::string const &`   
Required. The private connection identifier.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::PrivateConnection > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.PrivateConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L1124) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreatePrivateConnection(NoAwaitTag, std::string const &, google::cloud::clouddms::v1::PrivateConnection const &, std::string const &, Options)

Creates a new private connection in a given project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`private_connection` |  `google::cloud::clouddms::v1::PrivateConnection const &`   
  
`private_connection_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreatePrivateConnection(google::cloud::clouddms::v1::CreatePrivateConnectionRequest const &, Options)

Creates a new private connection in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::CreatePrivateConnectionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.CreatePrivateConnectionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L973). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::PrivateConnection > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.PrivateConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L1124) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreatePrivateConnection(NoAwaitTag, google::cloud::clouddms::v1::CreatePrivateConnectionRequest const &, Options)

Creates a new private connection in a given project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::CreatePrivateConnectionRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreatePrivateConnection(google::longrunning::Operation const &, Options)

Creates a new private connection in a given project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::PrivateConnection > >` |   
  
### GetPrivateConnection(std::string const &, Options)

Gets details of a single private connection. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the private connection to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::PrivateConnection >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.PrivateConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L1124)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetPrivateConnection(google::cloud::clouddms::v1::GetPrivateConnectionRequest const &, Options)

Gets details of a single private connection. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::GetPrivateConnectionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.GetPrivateConnectionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1072). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::PrivateConnection >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.PrivateConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L1124)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListPrivateConnections(std::string const &, Options)

Retrieves a list of private connections in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent that owns the collection of private connections.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::PrivateConnection >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.PrivateConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L1124), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListPrivateConnections(google::cloud::clouddms::v1::ListPrivateConnectionsRequest, Options)

Retrieves a list of private connections in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ListPrivateConnectionsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ListPrivateConnectionsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1004). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::PrivateConnection >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.PrivateConnection](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms_resources.proto#L1124), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeletePrivateConnection(std::string const &, Options)

Deletes a single Database Migration Service private connection. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The name of the private connection to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.OperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeletePrivateConnection(NoAwaitTag, std::string const &, Options)

Deletes a single Database Migration Service private connection. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeletePrivateConnection(google::cloud::clouddms::v1::DeletePrivateConnectionRequest const &, Options)

Deletes a single Database Migration Service private connection. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::DeletePrivateConnectionRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.DeletePrivateConnectionRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1052). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.OperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeletePrivateConnection(NoAwaitTag, google::cloud::clouddms::v1::DeletePrivateConnectionRequest const &, Options)

Deletes a single Database Migration Service private connection. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::DeletePrivateConnectionRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeletePrivateConnection(google::longrunning::Operation const &, Options)

Deletes a single Database Migration Service private connection. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` |   
  
### GetConversionWorkspace(std::string const &, Options)

Gets details of a single conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Name of the conversion workspace resource to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::ConversionWorkspace >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetConversionWorkspace(google::cloud::clouddms::v1::GetConversionWorkspaceRequest const &, Options)

Gets details of a single conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::GetConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.GetConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1160). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::ConversionWorkspace >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListConversionWorkspaces(std::string const &, Options)

Lists conversion workspaces in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent which owns this collection of conversion workspaces.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::ConversionWorkspace >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListConversionWorkspaces(google::cloud::clouddms::v1::ListConversionWorkspacesRequest, Options)

Lists conversion workspaces in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ListConversionWorkspacesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ListConversionWorkspacesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1114). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::ConversionWorkspace >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateConversionWorkspace(std::string const &, google::cloud::clouddms::v1::ConversionWorkspace const &, std::string const &, Options)

Creates a new conversion workspace in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent which owns this collection of conversion workspaces.   
`conversion_workspace` |  `google::cloud::clouddms::v1::ConversionWorkspace const &`   
Required. Represents a conversion workspace object.   
`conversion_workspace_id` |  `std::string const &`   
Required. The ID of the conversion workspace to create.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateConversionWorkspace(NoAwaitTag, std::string const &, google::cloud::clouddms::v1::ConversionWorkspace const &, std::string const &, Options)

Creates a new conversion workspace in a given project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`parent` |  `std::string const &`   
  
`conversion_workspace` |  `google::cloud::clouddms::v1::ConversionWorkspace const &`   
  
`conversion_workspace_id` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateConversionWorkspace(google::cloud::clouddms::v1::CreateConversionWorkspaceRequest const &, Options)

Creates a new conversion workspace in a given project and location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::CreateConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.CreateConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1172). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CreateConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::CreateConversionWorkspaceRequest const &, Options)

Creates a new conversion workspace in a given project and location. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::CreateConversionWorkspaceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CreateConversionWorkspace(google::longrunning::Operation const &, Options)

Creates a new conversion workspace in a given project and location. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` |   
  
### UpdateConversionWorkspace(google::cloud::clouddms::v1::ConversionWorkspace const &, google::protobuf::FieldMask const &, Options)

Updates the parameters of a single conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`conversion_workspace` |  `google::cloud::clouddms::v1::ConversionWorkspace const &`   
Required. The conversion workspace parameters to update.   
`update_mask` |  `google::protobuf::FieldMask const &`   
Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::ConversionWorkspace const &, google::protobuf::FieldMask const &, Options)

Updates the parameters of a single conversion workspace. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`conversion_workspace` |  `google::cloud::clouddms::v1::ConversionWorkspace const &`   
  
`update_mask` |  `google::protobuf::FieldMask const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateConversionWorkspace(google::cloud::clouddms::v1::UpdateConversionWorkspaceRequest const &, Options)

Updates the parameters of a single conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::UpdateConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.UpdateConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1199). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::UpdateConversionWorkspaceRequest const &, Options)

Updates the parameters of a single conversion workspace. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::UpdateConversionWorkspaceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### UpdateConversionWorkspace(google::longrunning::Operation const &, Options)

Updates the parameters of a single conversion workspace. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` |   
  
### DeleteConversionWorkspace(std::string const &, Options)

Deletes a single conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Name of the conversion workspace resource to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.OperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteConversionWorkspace(NoAwaitTag, std::string const &, Options)

Deletes a single conversion workspace. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`name` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteConversionWorkspace(google::cloud::clouddms::v1::DeleteConversionWorkspaceRequest const &, Options)

Deletes a single conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::DeleteConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.DeleteConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1220). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.OperationMetadata](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1083) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::DeleteConversionWorkspaceRequest const &, Options)

Deletes a single conversion workspace. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::DeleteConversionWorkspaceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### DeleteConversionWorkspace(google::longrunning::Operation const &, Options)

Deletes a single conversion workspace. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::OperationMetadata > >` |   
  
### CreateMappingRule(std::string const &, google::cloud::clouddms::v1::MappingRule const &, std::string const &, Options)

Creates a new mapping rule for a given conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. The parent which owns this collection of mapping rules.   
`mapping_rule` |  `google::cloud::clouddms::v1::MappingRule const &`   
Required. Represents a [mapping rule](about:invalid#zCSafez) object.   
`mapping_rule_id` |  `std::string const &`   
Required. The ID of the rule to create.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::MappingRule >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.MappingRule](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L215)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### CreateMappingRule(google::cloud::clouddms::v1::CreateMappingRuleRequest const &, Options)

Creates a new mapping rule for a given conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::CreateMappingRuleRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.CreateMappingRuleRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1562). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::MappingRule >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.MappingRule](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L215)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DeleteMappingRule(std::string const &, Options)

Deletes a single mapping rule. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Name of the mapping rule resource to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteMappingRule(google::cloud::clouddms::v1::DeleteMappingRuleRequest const &, Options)

Deletes a single mapping rule. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::DeleteMappingRuleRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.DeleteMappingRuleRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1590). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### ListMappingRules(std::string const &, Options)

Lists the mapping rules for a specific conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. Name of the conversion workspace resource whose mapping rules are listed in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::MappingRule >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.MappingRule](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L215), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListMappingRules(google::cloud::clouddms::v1::ListMappingRulesRequest, Options)

Lists the mapping rules for a specific conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ListMappingRulesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ListMappingRulesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1302). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::MappingRule >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.MappingRule](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L215), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetMappingRule(std::string const &, Options)

Gets the details of a mapping rule. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Name of the mapping rule resource to get. Example: conversionWorkspaces/123/mappingRules/rule123   
In order to retrieve a previous revision of the mapping rule, also provide the revision ID. Example: `conversionWorkspace/123/mappingRules/rule123@c7cfa2a8c7cfa2a8c7cfa2a8c7cfa2a8`  
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::MappingRule >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.MappingRule](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L215)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetMappingRule(google::cloud::clouddms::v1::GetMappingRuleRequest const &, Options)

Gets the details of a mapping rule. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::GetMappingRuleRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.GetMappingRuleRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1336). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::MappingRule >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.MappingRule](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L215)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### SeedConversionWorkspace(google::cloud::clouddms::v1::SeedConversionWorkspaceRequest const &, Options)

Imports a snapshot of the source database into the conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::SeedConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.SeedConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1353). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SeedConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::SeedConversionWorkspaceRequest const &, Options)

Imports a snapshot of the source database into the conversion workspace. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::SeedConversionWorkspaceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### SeedConversionWorkspace(google::longrunning::Operation const &, Options)

Imports a snapshot of the source database into the conversion workspace. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` |   
  
### ImportMappingRules(google::cloud::clouddms::v1::ImportMappingRulesRequest const &, Options)

Imports the mapping rules for a given conversion workspace. 

Supports various formats of external rules files.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ImportMappingRulesRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ImportMappingRulesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1403). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ImportMappingRules(NoAwaitTag, google::cloud::clouddms::v1::ImportMappingRulesRequest const &, Options)

Imports the mapping rules for a given conversion workspace. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::ImportMappingRulesRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ImportMappingRules(google::longrunning::Operation const &, Options)

Imports the mapping rules for a given conversion workspace. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` |   
  
### ConvertConversionWorkspace(google::cloud::clouddms::v1::ConvertConversionWorkspaceRequest const &, Options)

Creates a draft tree schema for the destination database. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ConvertConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ConvertConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1381). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ConvertConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::ConvertConversionWorkspaceRequest const &, Options)

Creates a draft tree schema for the destination database. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::ConvertConversionWorkspaceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ConvertConversionWorkspace(google::longrunning::Operation const &, Options)

Creates a draft tree schema for the destination database. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` |   
  
### CommitConversionWorkspace(google::cloud::clouddms::v1::CommitConversionWorkspaceRequest const &, Options)

Marks all the data in the conversion workspace as committed. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::CommitConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.CommitConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1244). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CommitConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::CommitConversionWorkspaceRequest const &, Options)

Marks all the data in the conversion workspace as committed. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::CommitConversionWorkspaceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### CommitConversionWorkspace(google::longrunning::Operation const &, Options)

Marks all the data in the conversion workspace as committed. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` |   
  
### RollbackConversionWorkspace(google::cloud::clouddms::v1::RollbackConversionWorkspaceRequest const &, Options)

Rolls back a conversion workspace to the last committed snapshot. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::RollbackConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.RollbackConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1258). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### RollbackConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::RollbackConversionWorkspaceRequest const &, Options)

Rolls back a conversion workspace to the last committed snapshot. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::RollbackConversionWorkspaceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### RollbackConversionWorkspace(google::longrunning::Operation const &, Options)

Rolls back a conversion workspace to the last committed snapshot. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` |   
  
### ApplyConversionWorkspace(google::cloud::clouddms::v1::ApplyConversionWorkspaceRequest const &, Options)

Applies draft tree onto a specific destination database. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::ApplyConversionWorkspaceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.ApplyConversionWorkspaceRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1269). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](https://google.aip.dev/151)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.clouddms.v1.ConversionWorkspace](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L44) proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ApplyConversionWorkspace(NoAwaitTag, google::cloud::clouddms::v1::ApplyConversionWorkspaceRequest const &, Options)

Applies draft tree onto a specific destination database. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::longrunning::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::clouddms::v1::ApplyConversionWorkspaceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### ApplyConversionWorkspace(google::longrunning::Operation const &, Options)

Applies draft tree onto a specific destination database. 

This method accepts a `google::longrunning::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::clouddms::v1::ConversionWorkspace > >` |   
  
### DescribeDatabaseEntities(google::cloud::clouddms::v1::DescribeDatabaseEntitiesRequest, Options)

Describes the database entities tree for a specific conversion workspace and a specific tree type. 

Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::DescribeDatabaseEntitiesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.DescribeDatabaseEntitiesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1438). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::clouddms::v1::DatabaseEntity >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.clouddms.v1.DatabaseEntity](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/conversionworkspace_resources.proto#L734), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SearchBackgroundJobs(google::cloud::clouddms::v1::SearchBackgroundJobsRequest const &, Options)

Searches/lists the background jobs for a specific conversion workspace. 

The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::SearchBackgroundJobsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.SearchBackgroundJobsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1506). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::SearchBackgroundJobsResponse >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.SearchBackgroundJobsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1534)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### DescribeConversionWorkspaceRevisions(google::cloud::clouddms::v1::DescribeConversionWorkspaceRevisionsRequest const &, Options)

Retrieves a list of committed revisions of a specific conversion workspace. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::DescribeConversionWorkspaceRevisionsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.DescribeConversionWorkspaceRevisionsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1540). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::clouddms::v1::DescribeConversionWorkspaceRevisionsResponse >` | the result of the RPC. The response message type ([google.cloud.clouddms.v1.DescribeConversionWorkspaceRevisionsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1556)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### FetchStaticIps(std::string const &, Options)

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::string >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains a [`std::string`](https://en.cppreference.com/w/cpp/string/basic_string).   
  
### FetchStaticIps(google::cloud::clouddms::v1::FetchStaticIpsRequest, Options)

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::clouddms::v1::FetchStaticIpsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.clouddms.v1.FetchStaticIpsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/clouddms/v1/clouddms.proto#L1610). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::string >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains a [`std::string`](https://en.cppreference.com/w/cpp/string/basic_string).   
  
### ListLocations(google::cloud::location::ListLocationsRequest, Options)

Lists information about the supported locations for this service. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.location.ListLocationsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/location/locations.proto#L58). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::location::Location >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.location.Location](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/location/locations.proto#L88), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetLocation(google::cloud::location::GetLocationRequest const &, Options)

Gets information about a location. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.location.GetLocationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/location/locations.proto#L82). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::location::Location >` | the result of the RPC. The response message type ([google.cloud.location.Location](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/location/locations.proto#L88)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &, Options)

Sets the access control policy on the specified resource. 

Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.iam.v1.SetIamPolicyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/iam_policy.proto#L100). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | the result of the RPC. The response message type ([google.iam.v1.Policy](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/policy.proto#L102)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &, Options)

Gets the access control policy for a resource. 

Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.iam.v1.GetIamPolicyRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/iam_policy.proto#L123). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` | the result of the RPC. The response message type ([google.iam.v1.Policy](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/policy.proto#L102)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.iam.v1.TestIamPermissionsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/iam_policy.proto#L137). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::TestIamPermissionsResponse >` | the result of the RPC. The response message type ([google.iam.v1.TestIamPermissionsResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/iam/v1/iam_policy.proto#L153)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
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
  
### DeleteOperation(std::string const &, Options)

Deletes a long-running operation. 

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
The name of the operation resource to be deleted.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
### DeleteOperation(google::longrunning::DeleteOperationRequest const &, Options)

Deletes a long-running operation. 

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.longrunning.DeleteOperationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/longrunning/operations.proto#L219). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`Status` | a [`Status`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) object. If the request failed, the status contains the details of the failure.   
  
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
