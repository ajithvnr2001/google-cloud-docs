---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__accelerator__types__v1_1_1AcceleratorTypesClient/
title: Class AcceleratorTypesClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:19.443385+00:00
---

# Class AcceleratorTypesClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__accelerator__types__v1_1_1AcceleratorTypesClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class AcceleratorTypesClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the acceleratorTypes resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/acceleratorTypes>

This client uses AcceleratorTypes version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### AcceleratorTypesClient(AcceleratorTypesClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `AcceleratorTypesClient const &`   
  
  
### AcceleratorTypesClient(AcceleratorTypesClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `AcceleratorTypesClient &&`   
  
  
### AcceleratorTypesClient(std::shared_ptr< AcceleratorTypesConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< AcceleratorTypesConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(AcceleratorTypesClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `AcceleratorTypesClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`AcceleratorTypesClient &` |   
  
### operator=(AcceleratorTypesClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `AcceleratorTypesClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`AcceleratorTypesClient &` |   
  
## Functions 

### AggregatedListAcceleratorTypes(std::string const &, Options)

Retrieves an aggregated list of accelerator types. 

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. <https://cloud.google.com/compute/docs/reference/rest/v1/acceleratorTypes/aggregatedList>

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
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::AcceleratorTypesScopedList > >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.AcceleratorTypesScopedList](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_003.proto#L339), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AggregatedListAcceleratorTypes(google::cloud::cpp::compute::accelerator_types::v1::AggregatedListAcceleratorTypesRequest, Options)

Retrieves an aggregated list of accelerator types. 

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. <https://cloud.google.com/compute/docs/reference/rest/v1/acceleratorTypes/aggregatedList>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::accelerator_types::v1::AggregatedListAcceleratorTypesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.accelerator_types.v1.AggregatedListAcceleratorTypesRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/accelerator_types/v1/accelerator_types.proto#L75). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::AcceleratorTypesScopedList > >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.AcceleratorTypesScopedList](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_003.proto#L339), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetAcceleratorType(std::string const &, std::string const &, std::string const &, Options)

Returns the specified accelerator type. 

<https://cloud.google.com/compute/docs/reference/rest/v1/acceleratorTypes/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`zone` |  `std::string const &`   
The name of the zone for this request.   
`accelerator_type` |  `std::string const &`   
Name of the accelerator type to return.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::AcceleratorType >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.AcceleratorType](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_003.proto#L32)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetAcceleratorType(google::cloud::cpp::compute::accelerator_types::v1::GetAcceleratorTypeRequest const &, Options)

Returns the specified accelerator type. 

<https://cloud.google.com/compute/docs/reference/rest/v1/acceleratorTypes/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::accelerator_types::v1::GetAcceleratorTypeRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.accelerator_types.v1.GetAcceleratorTypeRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/accelerator_types/v1/accelerator_types.proto#L183). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::AcceleratorType >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.AcceleratorType](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_003.proto#L32)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ListAcceleratorTypes(std::string const &, std::string const &, Options)

Retrieves a list of accelerator types that are available to the specified project. 

<https://cloud.google.com/compute/docs/reference/rest/v1/acceleratorTypes/list>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`zone` |  `std::string const &`   
The name of the zone for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::AcceleratorType >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.AcceleratorType](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_003.proto#L32), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListAcceleratorTypes(google::cloud::cpp::compute::accelerator_types::v1::ListAcceleratorTypesRequest, Options)

Retrieves a list of accelerator types that are available to the specified project. 

<https://cloud.google.com/compute/docs/reference/rest/v1/acceleratorTypes/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::accelerator_types::v1::ListAcceleratorTypesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.accelerator_types.v1.ListAcceleratorTypesRequest](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/accelerator_types/v1/accelerator_types.proto#L197). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::AcceleratorType >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.AcceleratorType](https://github.com/googleapis/google-cloud-cpp/blob/61709d3a08ee4a7232b427d527e510c2da42b04a/google/cloud/compute/v1/internal/common_003.proto#L32), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
