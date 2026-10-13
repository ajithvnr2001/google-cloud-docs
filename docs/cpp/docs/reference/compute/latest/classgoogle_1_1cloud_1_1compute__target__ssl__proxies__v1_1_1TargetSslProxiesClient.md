---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__ssl__proxies__v1_1_1TargetSslProxiesClient/
title: Class TargetSslProxiesClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:18.167903+00:00
---

# Class TargetSslProxiesClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__ssl__proxies__v1_1_1TargetSslProxiesClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class TargetSslProxiesClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the targetSslProxies resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies>

This client uses TargetSslProxies version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### TargetSslProxiesClient(TargetSslProxiesClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TargetSslProxiesClient const &`   
  
  
### TargetSslProxiesClient(TargetSslProxiesClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TargetSslProxiesClient &&`   
  
  
### TargetSslProxiesClient(std::shared_ptr< TargetSslProxiesConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< TargetSslProxiesConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(TargetSslProxiesClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TargetSslProxiesClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`TargetSslProxiesClient &` |   
  
### operator=(TargetSslProxiesClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `TargetSslProxiesClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`TargetSslProxiesClient &` |   
  
## Functions 

### DeleteTargetSslProxy(std::string const &, std::string const &, Options)

Deletes the specified TargetSslProxy resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/delete>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`target_ssl_proxy` |  `std::string const &`   
Name of the TargetSslProxy resource to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteTargetSslProxy(NoAwaitTag, std::string const &, std::string const &, Options)

Deletes the specified TargetSslProxy resource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`target_ssl_proxy` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteTargetSslProxy(google::cloud::cpp::compute::target_ssl_proxies::v1::DeleteTargetSslProxyRequest const &, Options)

Deletes the specified TargetSslProxy resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/delete>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::DeleteTargetSslProxyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.DeleteTargetSslProxyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L170). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteTargetSslProxy(NoAwaitTag, google::cloud::cpp::compute::target_ssl_proxies::v1::DeleteTargetSslProxyRequest const &, Options)

Deletes the specified TargetSslProxy resource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::DeleteTargetSslProxyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteTargetSslProxy(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes the specified TargetSslProxy resource. 

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
  
### GetTargetSslProxy(std::string const &, std::string const &, Options)

Returns the specified TargetSslProxy resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`target_ssl_proxy` |  `std::string const &`   
Name of the TargetSslProxy resource to return.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TargetSslProxy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TargetSslProxy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_173.proto#L58)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetTargetSslProxy(google::cloud::cpp::compute::target_ssl_proxies::v1::GetTargetSslProxyRequest const &, Options)

Returns the specified TargetSslProxy resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::GetTargetSslProxyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.GetTargetSslProxyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L199). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TargetSslProxy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TargetSslProxy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_173.proto#L58)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### InsertTargetSslProxy(std::string const &, google::cloud::cpp::compute::v1::TargetSslProxy const &, Options)

Creates a TargetSslProxy resource in the specified project using the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/insert>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`target_ssl_proxy_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxy const &`   
The TargetSslProxy for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertTargetSslProxy(NoAwaitTag, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxy const &, Options)

Creates a TargetSslProxy resource in the specified project using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`target_ssl_proxy_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxy const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertTargetSslProxy(google::cloud::cpp::compute::target_ssl_proxies::v1::InsertTargetSslProxyRequest const &, Options)

Creates a TargetSslProxy resource in the specified project using the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/insert>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::InsertTargetSslProxyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.InsertTargetSslProxyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L210). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertTargetSslProxy(NoAwaitTag, google::cloud::cpp::compute::target_ssl_proxies::v1::InsertTargetSslProxyRequest const &, Options)

Creates a TargetSslProxy resource in the specified project using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::InsertTargetSslProxyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertTargetSslProxy(google::cloud::cpp::compute::v1::Operation const &, Options)

Creates a TargetSslProxy resource in the specified project using the data included in the request. 

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
  
### ListTargetSslProxies(std::string const &, Options)

Retrieves the list of TargetSslProxy resources available to the specified project. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/list>

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
`StreamRange< google::cloud::cpp::compute::v1::TargetSslProxy >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.TargetSslProxy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_173.proto#L58), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListTargetSslProxies(google::cloud::cpp::compute::target_ssl_proxies::v1::ListTargetSslProxiesRequest, Options)

Retrieves the list of TargetSslProxy resources available to the specified project. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::ListTargetSslProxiesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.ListTargetSslProxiesRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L239). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::TargetSslProxy >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.TargetSslProxy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_173.proto#L58), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetBackendService(std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxiesSetBackendServiceRequest const &, Options)

Changes the BackendService for TargetSslProxy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setBackendService>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`target_ssl_proxy` |  `std::string const &`   
Name of the TargetSslProxy resource whose BackendService resource is to be set.   
`target_ssl_proxies_set_backend_service_request_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxiesSetBackendServiceRequest const &`   
The TargetSslProxiesSetBackendServiceRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetBackendService(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxiesSetBackendServiceRequest const &, Options)

Changes the BackendService for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`target_ssl_proxy` |  `std::string const &`   
  
`target_ssl_proxies_set_backend_service_request_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxiesSetBackendServiceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetBackendService(google::cloud::cpp::compute::target_ssl_proxies::v1::SetBackendServiceRequest const &, Options)

Changes the BackendService for TargetSslProxy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setBackendService>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetBackendServiceRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.SetBackendServiceRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L333). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetBackendService(NoAwaitTag, google::cloud::cpp::compute::target_ssl_proxies::v1::SetBackendServiceRequest const &, Options)

Changes the BackendService for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetBackendServiceRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetBackendService(google::cloud::cpp::compute::v1::Operation const &, Options)

Changes the BackendService for TargetSslProxy. 

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
  
### SetCertificateMap(std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxiesSetCertificateMapRequest const &, Options)

Changes the Certificate Map for TargetSslProxy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setCertificateMap>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`target_ssl_proxy` |  `std::string const &`   
Name of the TargetSslProxy resource whose CertificateMap is to be set. The name must be 1-63 characters long, and comply with RFC1035.   
`target_ssl_proxies_set_certificate_map_request_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxiesSetCertificateMapRequest const &`   
The TargetSslProxiesSetCertificateMapRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetCertificateMap(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxiesSetCertificateMapRequest const &, Options)

Changes the Certificate Map for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`target_ssl_proxy` |  `std::string const &`   
  
`target_ssl_proxies_set_certificate_map_request_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxiesSetCertificateMapRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetCertificateMap(google::cloud::cpp::compute::target_ssl_proxies::v1::SetCertificateMapRequest const &, Options)

Changes the Certificate Map for TargetSslProxy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setCertificateMap>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetCertificateMapRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.SetCertificateMapRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L368). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetCertificateMap(NoAwaitTag, google::cloud::cpp::compute::target_ssl_proxies::v1::SetCertificateMapRequest const &, Options)

Changes the Certificate Map for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetCertificateMapRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetCertificateMap(google::cloud::cpp::compute::v1::Operation const &, Options)

Changes the Certificate Map for TargetSslProxy. 

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
  
### SetProxyHeader(std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxiesSetProxyHeaderRequest const &, Options)

Changes the ProxyHeaderType for TargetSslProxy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setProxyHeader>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`target_ssl_proxy` |  `std::string const &`   
Name of the TargetSslProxy resource whose ProxyHeader is to be set.   
`target_ssl_proxies_set_proxy_header_request_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxiesSetProxyHeaderRequest const &`   
The TargetSslProxiesSetProxyHeaderRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetProxyHeader(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxiesSetProxyHeaderRequest const &, Options)

Changes the ProxyHeaderType for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`target_ssl_proxy` |  `std::string const &`   
  
`target_ssl_proxies_set_proxy_header_request_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxiesSetProxyHeaderRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetProxyHeader(google::cloud::cpp::compute::target_ssl_proxies::v1::SetProxyHeaderRequest const &, Options)

Changes the ProxyHeaderType for TargetSslProxy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setProxyHeader>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetProxyHeaderRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.SetProxyHeaderRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L403). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetProxyHeader(NoAwaitTag, google::cloud::cpp::compute::target_ssl_proxies::v1::SetProxyHeaderRequest const &, Options)

Changes the ProxyHeaderType for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetProxyHeaderRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetProxyHeader(google::cloud::cpp::compute::v1::Operation const &, Options)

Changes the ProxyHeaderType for TargetSslProxy. 

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
  
### SetSslCertificates(std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxiesSetSslCertificatesRequest const &, Options)

Changes SslCertificates for TargetSslProxy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setSslCertificates>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`target_ssl_proxy` |  `std::string const &`   
Name of the TargetSslProxy resource whose SslCertificate resource is to be set.   
`target_ssl_proxies_set_ssl_certificates_request_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxiesSetSslCertificatesRequest const &`   
The TargetSslProxiesSetSslCertificatesRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetSslCertificates(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::TargetSslProxiesSetSslCertificatesRequest const &, Options)

Changes SslCertificates for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`target_ssl_proxy` |  `std::string const &`   
  
`target_ssl_proxies_set_ssl_certificates_request_resource` |  `google::cloud::cpp::compute::v1::TargetSslProxiesSetSslCertificatesRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetSslCertificates(google::cloud::cpp::compute::target_ssl_proxies::v1::SetSslCertificatesRequest const &, Options)

Changes SslCertificates for TargetSslProxy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setSslCertificates>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetSslCertificatesRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.SetSslCertificatesRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L437). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetSslCertificates(NoAwaitTag, google::cloud::cpp::compute::target_ssl_proxies::v1::SetSslCertificatesRequest const &, Options)

Changes SslCertificates for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetSslCertificatesRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetSslCertificates(google::cloud::cpp::compute::v1::Operation const &, Options)

Changes SslCertificates for TargetSslProxy. 

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
  
### SetSslPolicy(std::string const &, std::string const &, google::cloud::cpp::compute::v1::SslPolicyReference const &, Options)

Sets the SSL policy for TargetSslProxy. 

The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the load balancer. They do not affect the connection between the load balancer and the backends. <https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setSslPolicy>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`target_ssl_proxy` |  `std::string const &`   
Name of the TargetSslProxy resource whose SSL policy is to be set. The name must be 1-63 characters long, and comply with RFC1035.   
`ssl_policy_reference_resource` |  `google::cloud::cpp::compute::v1::SslPolicyReference const &`   
The SslPolicyReference for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetSslPolicy(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::SslPolicyReference const &, Options)

Sets the SSL policy for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`target_ssl_proxy` |  `std::string const &`   
  
`ssl_policy_reference_resource` |  `google::cloud::cpp::compute::v1::SslPolicyReference const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetSslPolicy(google::cloud::cpp::compute::target_ssl_proxies::v1::SetSslPolicyRequest const &, Options)

Sets the SSL policy for TargetSslProxy. 

The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the load balancer. They do not affect the connection between the load balancer and the backends. <https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/setSslPolicy>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetSslPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.SetSslPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L472). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### SetSslPolicy(NoAwaitTag, google::cloud::cpp::compute::target_ssl_proxies::v1::SetSslPolicyRequest const &, Options)

Sets the SSL policy for TargetSslProxy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::SetSslPolicyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### SetSslPolicy(google::cloud::cpp::compute::v1::Operation const &, Options)

Sets the SSL policy for TargetSslProxy. 

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

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/testIamPermissions>

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
`StatusOr< google::cloud::cpp::compute::v1::TestPermissionsResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TestPermissionsResponse](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_177.proto#L30)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### TestIamPermissions(google::cloud::cpp::compute::target_ssl_proxies::v1::TestIamPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/testIamPermissions>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::target_ssl_proxies::v1::TestIamPermissionsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.target_ssl_proxies.v1.TestIamPermissionsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/target_ssl_proxies/v1/target_ssl_proxies.proto#L506). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TestPermissionsResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TestPermissionsResponse](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_177.proto#L30)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
