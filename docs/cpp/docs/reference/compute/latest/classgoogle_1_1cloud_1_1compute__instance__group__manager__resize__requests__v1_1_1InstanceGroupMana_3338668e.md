---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instance__group__manager__resize__requests__v1_1_1InstanceGroupManagerResizeRequestsClient/
title: Class InstanceGroupManagerResizeRequestsClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:19.815154+00:00
---

# Class InstanceGroupManagerResizeRequestsClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instance__group__manager__resize__requests__v1_1_1InstanceGroupManagerResizeRequestsClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class InstanceGroupManagerResizeRequestsClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the instanceGroupManagerResizeRequests resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests>

This client uses InstanceGroupManagerResizeRequests version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### InstanceGroupManagerResizeRequestsClient(InstanceGroupManagerResizeRequestsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `InstanceGroupManagerResizeRequestsClient const &`   
  
  
### InstanceGroupManagerResizeRequestsClient(InstanceGroupManagerResizeRequestsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `InstanceGroupManagerResizeRequestsClient &&`   
  
  
### InstanceGroupManagerResizeRequestsClient(std::shared_ptr< InstanceGroupManagerResizeRequestsConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< InstanceGroupManagerResizeRequestsConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(InstanceGroupManagerResizeRequestsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `InstanceGroupManagerResizeRequestsClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`InstanceGroupManagerResizeRequestsClient &` |   
  
### operator=(InstanceGroupManagerResizeRequestsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `InstanceGroupManagerResizeRequestsClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`InstanceGroupManagerResizeRequestsClient &` |   
  
## Functions 

### Cancel(std::string const &, std::string const &, std::string const &, std::string const &, Options)

Cancels the specified resize request and removes it from the queue. 

Cancelled resize request does no longer wait for the resources to be provisioned. Cancel is only possible for requests that are accepted in the queue. <https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/cancel>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`zone` |  `std::string const &`   
The name of thezone where the managed instance group is located. The name should conform to RFC1035.   
`instance_group_manager` |  `std::string const &`   
The name of the managed instance group. The name should conform to RFC1035 or be a resource ID.   
`resize_request` |  `std::string const &`   
The name of the resize request to cancel. The name should conform to RFC1035 or be a resource ID.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### Cancel(NoAwaitTag, std::string const &, std::string const &, std::string const &, std::string const &, Options)

Cancels the specified resize request and removes it from the queue. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`zone` |  `std::string const &`   
  
`instance_group_manager` |  `std::string const &`   
  
`resize_request` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### Cancel(google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::CancelRequest const &, Options)

Cancels the specified resize request and removes it from the queue. 

Cancelled resize request does no longer wait for the resources to be provisioned. Cancel is only possible for requests that are accepted in the queue. <https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/cancel>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::CancelRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.instance_group_manager_resize_requests.v1.CancelRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/instance_group_manager_resize_requests/v1/instance_group_manager_resize_requests.proto#L115). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### Cancel(NoAwaitTag, google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::CancelRequest const &, Options)

Cancels the specified resize request and removes it from the queue. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::CancelRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### Cancel(google::cloud::cpp::compute::v1::Operation const &, Options)

Cancels the specified resize request and removes it from the queue. 

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
  
### DeleteInstanceGroupManagerResizeRequest(std::string const &, std::string const &, std::string const &, std::string const &, Options)

Deletes the specified, inactive resize request. 

Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously. <https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/delete>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`zone` |  `std::string const &`   
The name of thezone where the managed instance group is located. The name should conform to RFC1035.   
`instance_group_manager` |  `std::string const &`   
The name of the managed instance group. The name should conform to RFC1035 or be a resource ID.   
`resize_request` |  `std::string const &`   
The name of the resize request to delete. The name should conform to RFC1035 or be a resource ID.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteInstanceGroupManagerResizeRequest(NoAwaitTag, std::string const &, std::string const &, std::string const &, std::string const &, Options)

Deletes the specified, inactive resize request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`zone` |  `std::string const &`   
  
`instance_group_manager` |  `std::string const &`   
  
`resize_request` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteInstanceGroupManagerResizeRequest(google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::DeleteInstanceGroupManagerResizeRequestRequest const &, Options)

Deletes the specified, inactive resize request. 

Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously. <https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/delete>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::DeleteInstanceGroupManagerResizeRequestRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.instance_group_manager_resize_requests.v1.DeleteInstanceGroupManagerResizeRequestRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/instance_group_manager_resize_requests/v1/instance_group_manager_resize_requests.proto#L160). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteInstanceGroupManagerResizeRequest(NoAwaitTag, google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::DeleteInstanceGroupManagerResizeRequestRequest const &, Options)

Deletes the specified, inactive resize request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::DeleteInstanceGroupManagerResizeRequestRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteInstanceGroupManagerResizeRequest(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes the specified, inactive resize request. 

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
  
### GetInstanceGroupManagerResizeRequest(std::string const &, std::string const &, std::string const &, std::string const &, Options)

Returns all of the details about the specified resize request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`zone` |  `std::string const &`   
Name of the href="/compute/docs/regions-zones/#available">zone scoping this request. Name should conform to RFC1035.   
`instance_group_manager` |  `std::string const &`   
The name of the managed instance group. Name should conform to RFC1035 or be a resource ID.   
`resize_request` |  `std::string const &`   
The name of the resize request. Name should conform to RFC1035 or be a resource ID.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::InstanceGroupManagerResizeRequest >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.InstanceGroupManagerResizeRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_079.proto#L33)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetInstanceGroupManagerResizeRequest(google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::GetInstanceGroupManagerResizeRequestRequest const &, Options)

Returns all of the details about the specified resize request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::GetInstanceGroupManagerResizeRequestRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.instance_group_manager_resize_requests.v1.GetInstanceGroupManagerResizeRequestRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/instance_group_manager_resize_requests/v1/instance_group_manager_resize_requests.proto#L205). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::InstanceGroupManagerResizeRequest >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.InstanceGroupManagerResizeRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_079.proto#L33)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### InsertInstanceGroupManagerResizeRequest(std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::InstanceGroupManagerResizeRequest const &, Options)

Creates a new resize request that starts provisioning VMs immediately or queues VM creation. 

<https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`zone` |  `std::string const &`   
The name of thezone where the managed instance group is located and where the resize request will be created. Name should conform to RFC1035.   
`instance_group_manager` |  `std::string const &`   
The name of the managed instance group to which the resize request will be added. Name should conform to RFC1035 or be a resource ID.   
`instance_group_manager_resize_request_resource` |  `google::cloud::cpp::compute::v1::InstanceGroupManagerResizeRequest const &`   
The InstanceGroupManagerResizeRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertInstanceGroupManagerResizeRequest(NoAwaitTag, std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::InstanceGroupManagerResizeRequest const &, Options)

Creates a new resize request that starts provisioning VMs immediately or queues VM creation. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`zone` |  `std::string const &`   
  
`instance_group_manager` |  `std::string const &`   
  
`instance_group_manager_resize_request_resource` |  `google::cloud::cpp::compute::v1::InstanceGroupManagerResizeRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertInstanceGroupManagerResizeRequest(google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::InsertInstanceGroupManagerResizeRequestRequest const &, Options)

Creates a new resize request that starts provisioning VMs immediately or queues VM creation. 

<https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::InsertInstanceGroupManagerResizeRequestRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.instance_group_manager_resize_requests.v1.InsertInstanceGroupManagerResizeRequestRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/instance_group_manager_resize_requests/v1/instance_group_manager_resize_requests.proto#L228). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertInstanceGroupManagerResizeRequest(NoAwaitTag, google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::InsertInstanceGroupManagerResizeRequestRequest const &, Options)

Creates a new resize request that starts provisioning VMs immediately or queues VM creation. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::InsertInstanceGroupManagerResizeRequestRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertInstanceGroupManagerResizeRequest(google::cloud::cpp::compute::v1::Operation const &, Options)

Creates a new resize request that starts provisioning VMs immediately or queues VM creation. 

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
  
### ListInstanceGroupManagerResizeRequests(std::string const &, std::string const &, std::string const &, Options)

Retrieves a list of resize requests that are contained in the managed instance group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/list>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`zone` |  `std::string const &`   
The name of thezone where the managed instance group is located. The name should conform to RFC1035.   
`instance_group_manager` |  `std::string const &`   
The name of the managed instance group. The name should conform to RFC1035.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::InstanceGroupManagerResizeRequest >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.InstanceGroupManagerResizeRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_079.proto#L33), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListInstanceGroupManagerResizeRequests(google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::ListInstanceGroupManagerResizeRequestsRequest, Options)

Retrieves a list of resize requests that are contained in the managed instance group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::instance_group_manager_resize_requests::v1::ListInstanceGroupManagerResizeRequestsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.instance_group_manager_resize_requests.v1.ListInstanceGroupManagerResizeRequestsRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/instance_group_manager_resize_requests/v1/instance_group_manager_resize_requests.proto#L275). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::InstanceGroupManagerResizeRequest >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.InstanceGroupManagerResizeRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_079.proto#L33), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
