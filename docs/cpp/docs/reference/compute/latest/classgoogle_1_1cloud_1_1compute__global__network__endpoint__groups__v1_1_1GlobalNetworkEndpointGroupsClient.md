---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__network__endpoint__groups__v1_1_1GlobalNetworkEndpointGroupsClient/
title: Class GlobalNetworkEndpointGroupsClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:29.887227+00:00
---

# Class GlobalNetworkEndpointGroupsClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__network__endpoint__groups__v1_1_1GlobalNetworkEndpointGroupsClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class GlobalNetworkEndpointGroupsClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the globalNetworkEndpointGroups resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups>

This client uses GlobalNetworkEndpointGroups version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### GlobalNetworkEndpointGroupsClient(GlobalNetworkEndpointGroupsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `GlobalNetworkEndpointGroupsClient const &`   
  
  
### GlobalNetworkEndpointGroupsClient(GlobalNetworkEndpointGroupsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `GlobalNetworkEndpointGroupsClient &&`   
  
  
### GlobalNetworkEndpointGroupsClient(std::shared_ptr< GlobalNetworkEndpointGroupsConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< GlobalNetworkEndpointGroupsConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(GlobalNetworkEndpointGroupsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `GlobalNetworkEndpointGroupsClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`GlobalNetworkEndpointGroupsClient &` |   
  
### operator=(GlobalNetworkEndpointGroupsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `GlobalNetworkEndpointGroupsClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`GlobalNetworkEndpointGroupsClient &` |   
  
## Functions 

### AttachNetworkEndpoints(std::string const &, std::string const &, google::cloud::cpp::compute::v1::GlobalNetworkEndpointGroupsAttachEndpointsRequest const &, Options)

Attach a network endpoint to the specified network endpoint group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/attachNetworkEndpoints>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`network_endpoint_group` |  `std::string const &`   
The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035.   
`global_network_endpoint_groups_attach_endpoints_request_resource` |  `google::cloud::cpp::compute::v1::GlobalNetworkEndpointGroupsAttachEndpointsRequest const &`   
The GlobalNetworkEndpointGroupsAttachEndpointsRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AttachNetworkEndpoints(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::GlobalNetworkEndpointGroupsAttachEndpointsRequest const &, Options)

Attach a network endpoint to the specified network endpoint group. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`network_endpoint_group` |  `std::string const &`   
  
`global_network_endpoint_groups_attach_endpoints_request_resource` |  `google::cloud::cpp::compute::v1::GlobalNetworkEndpointGroupsAttachEndpointsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### AttachNetworkEndpoints(google::cloud::cpp::compute::global_network_endpoint_groups::v1::AttachNetworkEndpointsRequest const &, Options)

Attach a network endpoint to the specified network endpoint group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/attachNetworkEndpoints>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::AttachNetworkEndpointsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.global_network_endpoint_groups.v1.AttachNetworkEndpointsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/global_network_endpoint_groups/v1/global_network_endpoint_groups.proto#L142). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AttachNetworkEndpoints(NoAwaitTag, google::cloud::cpp::compute::global_network_endpoint_groups::v1::AttachNetworkEndpointsRequest const &, Options)

Attach a network endpoint to the specified network endpoint group. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::AttachNetworkEndpointsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### AttachNetworkEndpoints(google::cloud::cpp::compute::v1::Operation const &, Options)

Attach a network endpoint to the specified network endpoint group. 

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
  
### DeleteNetworkEndpointGroup(std::string const &, std::string const &, Options)

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/delete>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`network_endpoint_group` |  `std::string const &`   
The name of the network endpoint group to delete. It should comply with RFC1035.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteNetworkEndpointGroup(NoAwaitTag, std::string const &, std::string const &, Options)

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`network_endpoint_group` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteNetworkEndpointGroup(google::cloud::cpp::compute::global_network_endpoint_groups::v1::DeleteNetworkEndpointGroupRequest const &, Options)

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/delete>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::DeleteNetworkEndpointGroupRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.global_network_endpoint_groups.v1.DeleteNetworkEndpointGroupRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/global_network_endpoint_groups/v1/global_network_endpoint_groups.proto#L180). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteNetworkEndpointGroup(NoAwaitTag, google::cloud::cpp::compute::global_network_endpoint_groups::v1::DeleteNetworkEndpointGroupRequest const &, Options)

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::DeleteNetworkEndpointGroupRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteNetworkEndpointGroup(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it. 

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
  
### DetachNetworkEndpoints(std::string const &, std::string const &, google::cloud::cpp::compute::v1::GlobalNetworkEndpointGroupsDetachEndpointsRequest const &, Options)

Detach the network endpoint from the specified network endpoint group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/detachNetworkEndpoints>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`network_endpoint_group` |  `std::string const &`   
The name of the network endpoint group where you are removing network endpoints. It should comply with RFC1035.   
`global_network_endpoint_groups_detach_endpoints_request_resource` |  `google::cloud::cpp::compute::v1::GlobalNetworkEndpointGroupsDetachEndpointsRequest const &`   
The GlobalNetworkEndpointGroupsDetachEndpointsRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DetachNetworkEndpoints(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::GlobalNetworkEndpointGroupsDetachEndpointsRequest const &, Options)

Detach the network endpoint from the specified network endpoint group. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`network_endpoint_group` |  `std::string const &`   
  
`global_network_endpoint_groups_detach_endpoints_request_resource` |  `google::cloud::cpp::compute::v1::GlobalNetworkEndpointGroupsDetachEndpointsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DetachNetworkEndpoints(google::cloud::cpp::compute::global_network_endpoint_groups::v1::DetachNetworkEndpointsRequest const &, Options)

Detach the network endpoint from the specified network endpoint group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/detachNetworkEndpoints>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::DetachNetworkEndpointsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.global_network_endpoint_groups.v1.DetachNetworkEndpointsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/global_network_endpoint_groups/v1/global_network_endpoint_groups.proto#L212). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DetachNetworkEndpoints(NoAwaitTag, google::cloud::cpp::compute::global_network_endpoint_groups::v1::DetachNetworkEndpointsRequest const &, Options)

Detach the network endpoint from the specified network endpoint group. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::DetachNetworkEndpointsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DetachNetworkEndpoints(google::cloud::cpp::compute::v1::Operation const &, Options)

Detach the network endpoint from the specified network endpoint group. 

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
  
### GetNetworkEndpointGroup(std::string const &, std::string const &, Options)

Returns the specified network endpoint group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`network_endpoint_group` |  `std::string const &`   
The name of the network endpoint group. It should comply with RFC1035.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::NetworkEndpointGroup >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.NetworkEndpointGroup](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_016.proto#L157)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetNetworkEndpointGroup(google::cloud::cpp::compute::global_network_endpoint_groups::v1::GetNetworkEndpointGroupRequest const &, Options)

Returns the specified network endpoint group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::GetNetworkEndpointGroupRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.global_network_endpoint_groups.v1.GetNetworkEndpointGroupRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/global_network_endpoint_groups/v1/global_network_endpoint_groups.proto#L250). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::NetworkEndpointGroup >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.NetworkEndpointGroup](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_016.proto#L157)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### InsertNetworkEndpointGroup(std::string const &, google::cloud::cpp::compute::v1::NetworkEndpointGroup const &, Options)

Creates a network endpoint group in the specified project using the parameters that are included in the request. 

Note: Use the following APIs to manage network endpoint groups:

  * To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API
  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API
  * To manage NEGs with global scope (such as global internet NEGs):global API <https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/insert>



**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`network_endpoint_group_resource` |  `google::cloud::cpp::compute::v1::NetworkEndpointGroup const &`   
The NetworkEndpointGroup for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertNetworkEndpointGroup(NoAwaitTag, std::string const &, google::cloud::cpp::compute::v1::NetworkEndpointGroup const &, Options)

Creates a network endpoint group in the specified project using the parameters that are included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`network_endpoint_group_resource` |  `google::cloud::cpp::compute::v1::NetworkEndpointGroup const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertNetworkEndpointGroup(google::cloud::cpp::compute::global_network_endpoint_groups::v1::InsertNetworkEndpointGroupRequest const &, Options)

Creates a network endpoint group in the specified project using the parameters that are included in the request. 

Note: Use the following APIs to manage network endpoint groups:

  * To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API
  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API
  * To manage NEGs with global scope (such as global internet NEGs):global API <https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/insert>



**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::InsertNetworkEndpointGroupRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.global_network_endpoint_groups.v1.InsertNetworkEndpointGroupRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/global_network_endpoint_groups/v1/global_network_endpoint_groups.proto#L263). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertNetworkEndpointGroup(NoAwaitTag, google::cloud::cpp::compute::global_network_endpoint_groups::v1::InsertNetworkEndpointGroupRequest const &, Options)

Creates a network endpoint group in the specified project using the parameters that are included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::InsertNetworkEndpointGroupRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertNetworkEndpointGroup(google::cloud::cpp::compute::v1::Operation const &, Options)

Creates a network endpoint group in the specified project using the parameters that are included in the request. 

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
  
### ListGlobalNetworkEndpointGroups(std::string const &, Options)

Retrieves the list of network endpoint groups that are located in the specified project. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/list>

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
`StreamRange< google::cloud::cpp::compute::v1::NetworkEndpointGroup >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.NetworkEndpointGroup](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_016.proto#L157), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListGlobalNetworkEndpointGroups(google::cloud::cpp::compute::global_network_endpoint_groups::v1::ListGlobalNetworkEndpointGroupsRequest, Options)

Retrieves the list of network endpoint groups that are located in the specified project. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::ListGlobalNetworkEndpointGroupsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.global_network_endpoint_groups.v1.ListGlobalNetworkEndpointGroupsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/global_network_endpoint_groups/v1/global_network_endpoint_groups.proto#L292). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::NetworkEndpointGroup >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.NetworkEndpointGroup](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_016.proto#L157), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListNetworkEndpoints(std::string const &, std::string const &, Options)

Lists the network endpoints in the specified network endpoint group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/listNetworkEndpoints>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`network_endpoint_group` |  `std::string const &`   
The name of the network endpoint group from which you want to generate a list of included network endpoints. It should comply with RFC1035.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::NetworkEndpointWithHealthStatus >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.NetworkEndpointWithHealthStatus](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_016.proto#L682), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListNetworkEndpoints(google::cloud::cpp::compute::global_network_endpoint_groups::v1::ListNetworkEndpointsRequest, Options)

Lists the network endpoints in the specified network endpoint group. 

<https://cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/listNetworkEndpoints>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::global_network_endpoint_groups::v1::ListNetworkEndpointsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.global_network_endpoint_groups.v1.ListNetworkEndpointsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/global_network_endpoint_groups/v1/global_network_endpoint_groups.proto#L386). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::NetworkEndpointWithHealthStatus >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.NetworkEndpointWithHealthStatus](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_016.proto#L682), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
