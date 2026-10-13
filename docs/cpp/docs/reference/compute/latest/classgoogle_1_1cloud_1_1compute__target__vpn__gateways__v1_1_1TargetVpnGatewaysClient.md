---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__vpn__gateways__v1_1_1TargetVpnGatewaysClient/
title: Class TargetVpnGatewaysClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:37.393833+00:00
---

# Class TargetVpnGatewaysClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__vpn__gateways__v1_1_1TargetVpnGatewaysClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class TargetVpnGatewaysClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the targetVpnGateways resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways>

This client uses TargetVpnGateways version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### TargetVpnGatewaysClient(TargetVpnGatewaysClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TargetVpnGatewaysClient const &`   
  
  
### TargetVpnGatewaysClient(TargetVpnGatewaysClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TargetVpnGatewaysClient &&`   
  
  
### TargetVpnGatewaysClient(std::shared_ptr< TargetVpnGatewaysConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< TargetVpnGatewaysConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(TargetVpnGatewaysClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TargetVpnGatewaysClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`TargetVpnGatewaysClient &` |   
  
### operator=(TargetVpnGatewaysClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TargetVpnGatewaysClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`TargetVpnGatewaysClient &` |   
  
## Functions 

### AggregatedListTargetVpnGateways(std::string const &, Options)

Retrieves an aggregated list of target VPN gateways. 

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. <https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/aggregatedList>

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
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::TargetVpnGatewaysScopedList > >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.TargetVpnGatewaysScopedList](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_176.proto#L389), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AggregatedListTargetVpnGateways(google::cloud::cpp::compute::target_vpn_gateways::v1::AggregatedListTargetVpnGatewaysRequest, Options)

Retrieves an aggregated list of target VPN gateways. 

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. <https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/aggregatedList>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::AggregatedListTargetVpnGatewaysRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_vpn_gateways.v1.AggregatedListTargetVpnGatewaysRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_vpn_gateways/v1/target_vpn_gateways.proto#L118). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::TargetVpnGatewaysScopedList > >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.TargetVpnGatewaysScopedList](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_176.proto#L389), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteTargetVpnGateway(std::string const &, std::string const &, std::string const &, Options)

Deletes the specified target VPN gateway. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/delete>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region for this request.   
`target_vpn_gateway` |  `std::string const &`   
Name of the target VPN gateway to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteTargetVpnGateway(NoAwaitTag, std::string const &, std::string const &, std::string const &, Options)

Deletes the specified target VPN gateway. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`target_vpn_gateway` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteTargetVpnGateway(google::cloud::cpp::compute::target_vpn_gateways::v1::DeleteTargetVpnGatewayRequest const &, Options)

Deletes the specified target VPN gateway. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/delete>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::DeleteTargetVpnGatewayRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_vpn_gateways.v1.DeleteTargetVpnGatewayRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_vpn_gateways/v1/target_vpn_gateways.proto#L226). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteTargetVpnGateway(NoAwaitTag, google::cloud::cpp::compute::target_vpn_gateways::v1::DeleteTargetVpnGatewayRequest const &, Options)

Deletes the specified target VPN gateway. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::DeleteTargetVpnGatewayRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteTargetVpnGateway(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes the specified target VPN gateway. 

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
  
### GetTargetVpnGateway(std::string const &, std::string const &, std::string const &, Options)

Returns the specified target VPN gateway. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region for this request.   
`target_vpn_gateway` |  `std::string const &`   
Name of the target VPN gateway to return.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TargetVpnGateway >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TargetVpnGateway](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_176.proto#L29)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetTargetVpnGateway(google::cloud::cpp::compute::target_vpn_gateways::v1::GetTargetVpnGatewayRequest const &, Options)

Returns the specified target VPN gateway. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::GetTargetVpnGatewayRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_vpn_gateways.v1.GetTargetVpnGatewayRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_vpn_gateways/v1/target_vpn_gateways.proto#L262). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TargetVpnGateway >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TargetVpnGateway](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_176.proto#L29)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### InsertTargetVpnGateway(std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetVpnGateway const &, Options)

Creates a target VPN gateway in the specified project and region using the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/insert>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region for this request.   
`target_vpn_gateway_resource` |  `google::cloud::cpp::compute::v1::TargetVpnGateway const &`   
The TargetVpnGateway for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertTargetVpnGateway(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetVpnGateway const &, Options)

Creates a target VPN gateway in the specified project and region using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`target_vpn_gateway_resource` |  `google::cloud::cpp::compute::v1::TargetVpnGateway const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertTargetVpnGateway(google::cloud::cpp::compute::target_vpn_gateways::v1::InsertTargetVpnGatewayRequest const &, Options)

Creates a target VPN gateway in the specified project and region using the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/insert>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::InsertTargetVpnGatewayRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_vpn_gateways.v1.InsertTargetVpnGatewayRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_vpn_gateways/v1/target_vpn_gateways.proto#L277). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertTargetVpnGateway(NoAwaitTag, google::cloud::cpp::compute::target_vpn_gateways::v1::InsertTargetVpnGatewayRequest const &, Options)

Creates a target VPN gateway in the specified project and region using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::InsertTargetVpnGatewayRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertTargetVpnGateway(google::cloud::cpp::compute::v1::Operation const &, Options)

Creates a target VPN gateway in the specified project and region using the data included in the request. 

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
  
### ListTargetVpnGateways(std::string const &, std::string const &, Options)

Retrieves a list of target VPN gateways available to the specified project and region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/list>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::TargetVpnGateway >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.TargetVpnGateway](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_176.proto#L29), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListTargetVpnGateways(google::cloud::cpp::compute::target_vpn_gateways::v1::ListTargetVpnGatewaysRequest, Options)

Retrieves a list of target VPN gateways available to the specified project and region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::ListTargetVpnGatewaysRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_vpn_gateways.v1.ListTargetVpnGatewaysRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_vpn_gateways/v1/target_vpn_gateways.proto#L313). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::TargetVpnGateway >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.TargetVpnGateway](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_176.proto#L29), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetLabels(std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::RegionSetLabelsRequest const &, Options)

Sets the labels on a TargetVpnGateway. 

To learn more about labels, read theLabeling Resources documentation. <https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/setLabels>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
The region for this request.   
`resource` |  `std::string const &`   
Name or id of the resource for this request.   
`region_set_labels_request_resource` |  `google::cloud::cpp::compute::v1::RegionSetLabelsRequest const &`   
The RegionSetLabelsRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetLabels(NoAwaitTag, std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::RegionSetLabelsRequest const &, Options)

Sets the labels on a TargetVpnGateway. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`resource` |  `std::string const &`   
  
`region_set_labels_request_resource` |  `google::cloud::cpp::compute::v1::RegionSetLabelsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetLabels(google::cloud::cpp::compute::target_vpn_gateways::v1::SetLabelsRequest const &, Options)

Sets the labels on a TargetVpnGateway. 

To learn more about labels, read theLabeling Resources documentation. <https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/setLabels>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::SetLabelsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_vpn_gateways.v1.SetLabelsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_vpn_gateways/v1/target_vpn_gateways.proto#L411). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetLabels(NoAwaitTag, google::cloud::cpp::compute::target_vpn_gateways::v1::SetLabelsRequest const &, Options)

Sets the labels on a TargetVpnGateway. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_vpn_gateways::v1::SetLabelsRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetLabels(google::cloud::cpp::compute::v1::Operation const &, Options)

Sets the labels on a TargetVpnGateway. 

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
