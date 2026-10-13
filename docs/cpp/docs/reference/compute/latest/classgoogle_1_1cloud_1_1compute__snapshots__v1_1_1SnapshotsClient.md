---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__snapshots__v1_1_1SnapshotsClient/
title: Class SnapshotsClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:18.363251+00:00
---

# Class SnapshotsClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__snapshots__v1_1_1SnapshotsClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class SnapshotsClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the snapshots resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots>

This client uses Snapshots version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### SnapshotsClient(SnapshotsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `SnapshotsClient const &`   
  
  
### SnapshotsClient(SnapshotsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `SnapshotsClient &&`   
  
  
### SnapshotsClient(std::shared_ptr< SnapshotsConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< SnapshotsConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(SnapshotsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `SnapshotsClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`SnapshotsClient &` |   
  
### operator=(SnapshotsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `SnapshotsClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`SnapshotsClient &` |   
  
## Functions 

### DeleteSnapshot(std::string const &, std::string const &, Options)

Deletes the specified Snapshot resource. 

Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/delete>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`snapshot` |  `std::string const &`   
Name of the Snapshot resource to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteSnapshot(NoAwaitTag, std::string const &, std::string const &, Options)

Deletes the specified Snapshot resource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`snapshot` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteSnapshot(google::cloud::cpp::compute::snapshots::v1::DeleteSnapshotRequest const &, Options)

Deletes the specified Snapshot resource. 

Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/delete>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::DeleteSnapshotRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.DeleteSnapshotRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L168). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteSnapshot(NoAwaitTag, google::cloud::cpp::compute::snapshots::v1::DeleteSnapshotRequest const &, Options)

Deletes the specified Snapshot resource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::snapshots::v1::DeleteSnapshotRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteSnapshot(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes the specified Snapshot resource. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### GetSnapshot(std::string const &, std::string const &, Options)

Returns the specified Snapshot resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`snapshot` |  `std::string const &`   
Name of the Snapshot resource to return.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Snapshot >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Snapshot](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_152.proto#L31)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetSnapshot(google::cloud::cpp::compute::snapshots::v1::GetSnapshotRequest const &, Options)

Returns the specified Snapshot resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::GetSnapshotRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.GetSnapshotRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L212). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Snapshot >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Snapshot](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_152.proto#L31)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetIamPolicy(std::string const &, std::string const &, Options)

Gets the access control policy for a resource. 

May be empty if no such policy or resource exists. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/getIamPolicy>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`resource` |  `std::string const &`   
Name or id of the resource for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Policy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Policy](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_010.proto#L317)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetIamPolicy(google::cloud::cpp::compute::snapshots::v1::GetIamPolicyRequest const &, Options)

Gets the access control policy for a resource. 

May be empty if no such policy or resource exists. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/getIamPolicy>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::GetIamPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.GetIamPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L197). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Policy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Policy](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_010.proto#L317)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### InsertSnapshot(std::string const &, google::cloud::cpp::compute::v1::Snapshot const &, Options)

Creates a snapshot in the specified project using the data included in the request. 

For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`snapshot_resource` |  `google::cloud::cpp::compute::v1::Snapshot const &`   
The Snapshot for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertSnapshot(NoAwaitTag, std::string const &, google::cloud::cpp::compute::v1::Snapshot const &, Options)

Creates a snapshot in the specified project using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`snapshot_resource` |  `google::cloud::cpp::compute::v1::Snapshot const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertSnapshot(google::cloud::cpp::compute::snapshots::v1::InsertSnapshotRequest const &, Options)

Creates a snapshot in the specified project using the data included in the request. 

For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::InsertSnapshotRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.InsertSnapshotRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L223). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertSnapshot(NoAwaitTag, google::cloud::cpp::compute::snapshots::v1::InsertSnapshotRequest const &, Options)

Creates a snapshot in the specified project using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::snapshots::v1::InsertSnapshotRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertSnapshot(google::cloud::cpp::compute::v1::Operation const &, Options)

Creates a snapshot in the specified project using the data included in the request. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### ListSnapshots(std::string const &, Options)

Retrieves the list of Snapshot resources contained within the specified project. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/list>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::Snapshot >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.Snapshot](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_152.proto#L31), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListSnapshots(google::cloud::cpp::compute::snapshots::v1::ListSnapshotsRequest, Options)

Retrieves the list of Snapshot resources contained within the specified project. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::ListSnapshotsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.ListSnapshotsRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L252). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::Snapshot >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.Snapshot](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_152.proto#L31), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetIamPolicy(std::string const &, std::string const &, google::cloud::cpp::compute::v1::GlobalSetPolicyRequest const &, Options)

Sets the access control policy on the specified resource. 

Replaces any existing policy. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/setIamPolicy>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`resource` |  `std::string const &`   
Name or id of the resource for this request.   
`global_set_policy_request_resource` |  `google::cloud::cpp::compute::v1::GlobalSetPolicyRequest const &`   
The GlobalSetPolicyRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Policy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Policy](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_010.proto#L317)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### SetIamPolicy(google::cloud::cpp::compute::snapshots::v1::SetIamPolicyRequest const &, Options)

Sets the access control policy on the specified resource. 

Replaces any existing policy. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/setIamPolicy>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::SetIamPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.SetIamPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L346). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Policy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Policy](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_010.proto#L317)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### SetLabels(std::string const &, std::string const &, google::cloud::cpp::compute::v1::GlobalSetLabelsRequest const &, Options)

Sets the labels on a snapshot. 

To learn more about labels, read theLabeling Resources documentation. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/setLabels>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`resource` |  `std::string const &`   
Name or id of the resource for this request.   
`global_set_labels_request_resource` |  `google::cloud::cpp::compute::v1::GlobalSetLabelsRequest const &`   
The GlobalSetLabelsRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetLabels(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::GlobalSetLabelsRequest const &, Options)

Sets the labels on a snapshot. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`resource` |  `std::string const &`   
  
`global_set_labels_request_resource` |  `google::cloud::cpp::compute::v1::GlobalSetLabelsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetLabels(google::cloud::cpp::compute::snapshots::v1::SetLabelsRequest const &, Options)

Sets the labels on a snapshot. 

To learn more about labels, read theLabeling Resources documentation. <https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/setLabels>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::SetLabelsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.SetLabelsRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L362). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetLabels(NoAwaitTag, google::cloud::cpp::compute::snapshots::v1::SetLabelsRequest const &, Options)

Sets the labels on a snapshot. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::snapshots::v1::SetLabelsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetLabels(google::cloud::cpp::compute::v1::Operation const &, Options)

Sets the labels on a snapshot. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### TestIamPermissions(std::string const &, std::string const &, google::cloud::cpp::compute::v1::TestPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/testIamPermissions>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`resource` |  `std::string const &`   
Name or id of the resource for this request.   
`test_permissions_request_resource` |  `google::cloud::cpp::compute::v1::TestPermissionsRequest const &`   
The TestPermissionsRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TestPermissionsResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TestPermissionsResponse](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_177.proto#L30)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### TestIamPermissions(google::cloud::cpp::compute::snapshots::v1::TestIamPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/testIamPermissions>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::TestIamPermissionsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.TestIamPermissionsRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L381). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TestPermissionsResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TestPermissionsResponse](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_177.proto#L30)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### UpdateKmsKey(std::string const &, std::string const &, google::cloud::cpp::compute::v1::SnapshotUpdateKmsKeyRequest const &, Options)

Rotates the customer-managed encryption key to the latest version for the specified snapshot. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/updateKmsKey>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`snapshot` |  `std::string const &`   
Name of the snapshot resource to update. Should conform to RFC1035.   
`snapshot_update_kms_key_request_resource` |  `google::cloud::cpp::compute::v1::SnapshotUpdateKmsKeyRequest const &`   
The SnapshotUpdateKmsKeyRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateKmsKey(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::SnapshotUpdateKmsKeyRequest const &, Options)

Rotates the customer-managed encryption key to the latest version for the specified snapshot. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`snapshot` |  `std::string const &`   
  
`snapshot_update_kms_key_request_resource` |  `google::cloud::cpp::compute::v1::SnapshotUpdateKmsKeyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### UpdateKmsKey(google::cloud::cpp::compute::snapshots::v1::UpdateKmsKeyRequest const &, Options)

Rotates the customer-managed encryption key to the latest version for the specified snapshot. 

<https://cloud.google.com/compute/docs/reference/rest/v1/snapshots/updateKmsKey>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::snapshots::v1::UpdateKmsKeyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.snapshots.v1.UpdateKmsKeyRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/snapshots/v1/snapshots.proto#L396). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateKmsKey(NoAwaitTag, google::cloud::cpp::compute::snapshots::v1::UpdateKmsKeyRequest const &, Options)

Rotates the customer-managed encryption key to the latest version for the specified snapshot. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::snapshots::v1::UpdateKmsKeyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### UpdateKmsKey(google::cloud::cpp::compute::v1::Operation const &, Options)

Rotates the customer-managed encryption key to the latest version for the specified snapshot. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
