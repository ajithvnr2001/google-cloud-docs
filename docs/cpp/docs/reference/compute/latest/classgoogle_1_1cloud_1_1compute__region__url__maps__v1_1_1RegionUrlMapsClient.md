---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__url__maps__v1_1_1RegionUrlMapsClient/
title: Class RegionUrlMapsClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:14.603641+00:00
---

# Class RegionUrlMapsClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__url__maps__v1_1_1RegionUrlMapsClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class RegionUrlMapsClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the regionUrlMaps resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps>

This client uses RegionUrlMaps version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### RegionUrlMapsClient(RegionUrlMapsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `RegionUrlMapsClient const &`   
  
  
### RegionUrlMapsClient(RegionUrlMapsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `RegionUrlMapsClient &&`   
  
  
### RegionUrlMapsClient(std::shared_ptr< RegionUrlMapsConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< RegionUrlMapsConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(RegionUrlMapsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `RegionUrlMapsClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`RegionUrlMapsClient &` |   
  
### operator=(RegionUrlMapsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `RegionUrlMapsClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`RegionUrlMapsClient &` |   
  
## Functions 

### DeleteUrlMap(std::string const &, std::string const &, std::string const &, Options)

Deletes the specified UrlMap resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/delete>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`url_map` |  `std::string const &`   
Name of the UrlMap resource to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteUrlMap(NoAwaitTag, std::string const &, std::string const &, std::string const &, Options)

Deletes the specified UrlMap resource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`url_map` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteUrlMap(google::cloud::cpp::compute::region_url_maps::v1::DeleteUrlMapRequest const &, Options)

Deletes the specified UrlMap resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/delete>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::DeleteUrlMapRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_url_maps.v1.DeleteUrlMapRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/region_url_maps/v1/region_url_maps.proto#L132). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteUrlMap(NoAwaitTag, google::cloud::cpp::compute::region_url_maps::v1::DeleteUrlMapRequest const &, Options)

Deletes the specified UrlMap resource. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::DeleteUrlMapRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteUrlMap(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes the specified UrlMap resource. 

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
  
### GetUrlMap(std::string const &, std::string const &, std::string const &, Options)

Returns the specified UrlMap resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`url_map` |  `std::string const &`   
Name of the UrlMap resource to return.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::UrlMap >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.UrlMap](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_024.proto#L1457)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetUrlMap(google::cloud::cpp::compute::region_url_maps::v1::GetUrlMapRequest const &, Options)

Returns the specified UrlMap resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::GetUrlMapRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_url_maps.v1.GetUrlMapRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/region_url_maps/v1/region_url_maps.proto#L157). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::UrlMap >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.UrlMap](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_024.proto#L1457)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### InsertUrlMap(std::string const &, std::string const &, google::cloud::cpp::compute::v1::UrlMap const &, Options)

Creates a UrlMap resource in the specified project using the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/insert>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`url_map_resource` |  `google::cloud::cpp::compute::v1::UrlMap const &`   
The UrlMap for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertUrlMap(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::UrlMap const &, Options)

Creates a UrlMap resource in the specified project using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`url_map_resource` |  `google::cloud::cpp::compute::v1::UrlMap const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertUrlMap(google::cloud::cpp::compute::region_url_maps::v1::InsertUrlMapRequest const &, Options)

Creates a UrlMap resource in the specified project using the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/insert>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::InsertUrlMapRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_url_maps.v1.InsertUrlMapRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/region_url_maps/v1/region_url_maps.proto#L172). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertUrlMap(NoAwaitTag, google::cloud::cpp::compute::region_url_maps::v1::InsertUrlMapRequest const &, Options)

Creates a UrlMap resource in the specified project using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::InsertUrlMapRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertUrlMap(google::cloud::cpp::compute::v1::Operation const &, Options)

Creates a UrlMap resource in the specified project using the data included in the request. 

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
  
### ListRegionUrlMaps(std::string const &, std::string const &, Options)

Retrieves the list of UrlMap resources available to the specified project in the specified region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/list>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::UrlMap >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.UrlMap](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_024.proto#L1457), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListRegionUrlMaps(google::cloud::cpp::compute::region_url_maps::v1::ListRegionUrlMapsRequest, Options)

Retrieves the list of UrlMap resources available to the specified project in the specified region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::ListRegionUrlMapsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_url_maps.v1.ListRegionUrlMapsRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/region_url_maps/v1/region_url_maps.proto#L197). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::UrlMap >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.UrlMap](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_024.proto#L1457), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchUrlMap(std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::UrlMap const &, Options)

Patches the specified UrlMap resource with the data included in the request. 

This method supportsPATCH semantics and usesJSON merge patch format and processing rules. <https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/patch>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`url_map` |  `std::string const &`   
Name of the UrlMap resource to patch.   
`url_map_resource` |  `google::cloud::cpp::compute::v1::UrlMap const &`   
The UrlMap for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchUrlMap(NoAwaitTag, std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::UrlMap const &, Options)

Patches the specified UrlMap resource with the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`url_map` |  `std::string const &`   
  
`url_map_resource` |  `google::cloud::cpp::compute::v1::UrlMap const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### PatchUrlMap(google::cloud::cpp::compute::region_url_maps::v1::PatchUrlMapRequest const &, Options)

Patches the specified UrlMap resource with the data included in the request. 

This method supportsPATCH semantics and usesJSON merge patch format and processing rules. <https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/patch>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::PatchUrlMapRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_url_maps.v1.PatchUrlMapRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/region_url_maps/v1/region_url_maps.proto#L295). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchUrlMap(NoAwaitTag, google::cloud::cpp::compute::region_url_maps::v1::PatchUrlMapRequest const &, Options)

Patches the specified UrlMap resource with the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::PatchUrlMapRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### PatchUrlMap(google::cloud::cpp::compute::v1::Operation const &, Options)

Patches the specified UrlMap resource with the data included in the request. 

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
  
### UpdateUrlMap(std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::UrlMap const &, Options)

Updates the specified UrlMap resource with the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/update>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`url_map` |  `std::string const &`   
Name of the UrlMap resource to update.   
`url_map_resource` |  `google::cloud::cpp::compute::v1::UrlMap const &`   
The UrlMap for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateUrlMap(NoAwaitTag, std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::UrlMap const &, Options)

Updates the specified UrlMap resource with the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`url_map` |  `std::string const &`   
  
`url_map_resource` |  `google::cloud::cpp::compute::v1::UrlMap const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### UpdateUrlMap(google::cloud::cpp::compute::region_url_maps::v1::UpdateUrlMapRequest const &, Options)

Updates the specified UrlMap resource with the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/update>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::UpdateUrlMapRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_url_maps.v1.UpdateUrlMapRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/region_url_maps/v1/region_url_maps.proto#L324). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### UpdateUrlMap(NoAwaitTag, google::cloud::cpp::compute::region_url_maps::v1::UpdateUrlMapRequest const &, Options)

Updates the specified UrlMap resource with the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::UpdateUrlMapRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### UpdateUrlMap(google::cloud::cpp::compute::v1::Operation const &, Options)

Updates the specified UrlMap resource with the data included in the request. 

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
  
### Validate(std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::RegionUrlMapsValidateRequest const &, Options)

Runs static validation for the UrlMap. 

In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap. <https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/validate>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`url_map` |  `std::string const &`   
Name of the UrlMap resource to be validated as.   
`region_url_maps_validate_request_resource` |  `google::cloud::cpp::compute::v1::RegionUrlMapsValidateRequest const &`   
The RegionUrlMapsValidateRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::UrlMapsValidateResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.UrlMapsValidateResponse](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_024.proto#L1826)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### Validate(google::cloud::cpp::compute::region_url_maps::v1::ValidateRequest const &, Options)

Runs static validation for the UrlMap. 

In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap. <https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/validate>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_url_maps::v1::ValidateRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_url_maps.v1.ValidateRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/region_url_maps/v1/region_url_maps.proto#L353). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::UrlMapsValidateResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.UrlMapsValidateResponse](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_024.proto#L1826)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
