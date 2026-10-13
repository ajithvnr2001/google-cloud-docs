---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__health__aggregation__policies__v1_1_1RegionHealthAggregationPoliciesClient/
title: Class RegionHealthAggregationPoliciesClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:30.515165+00:00
---

# Class RegionHealthAggregationPoliciesClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__health__aggregation__policies__v1_1_1RegionHealthAggregationPoliciesClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class RegionHealthAggregationPoliciesClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the regionHealthAggregationPolicies resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies>

This client uses RegionHealthAggregationPolicies version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### RegionHealthAggregationPoliciesClient(RegionHealthAggregationPoliciesClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `RegionHealthAggregationPoliciesClient const &`   
  
  
### RegionHealthAggregationPoliciesClient(RegionHealthAggregationPoliciesClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `RegionHealthAggregationPoliciesClient &&`   
  
  
### RegionHealthAggregationPoliciesClient(std::shared_ptr< RegionHealthAggregationPoliciesConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< RegionHealthAggregationPoliciesConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(RegionHealthAggregationPoliciesClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `RegionHealthAggregationPoliciesClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`RegionHealthAggregationPoliciesClient &` |   
  
### operator=(RegionHealthAggregationPoliciesClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `RegionHealthAggregationPoliciesClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`RegionHealthAggregationPoliciesClient &` |   
  
## Functions 

### AggregatedListRegionHealthAggregationPolicies(std::string const &, Options)

Retrieves the list of all HealthAggregationPolicy resources, regional and global, available to the specified project. 

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. <https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/aggregatedList>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
Name of the project scoping this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::HealthAggregationPoliciesScopedList > >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.HealthAggregationPoliciesScopedList](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_062.proto#L24), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AggregatedListRegionHealthAggregationPolicies(google::cloud::cpp::compute::region_health_aggregation_policies::v1::AggregatedListRegionHealthAggregationPoliciesRequest, Options)

Retrieves the list of all HealthAggregationPolicy resources, regional and global, available to the specified project. 

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. <https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/aggregatedList>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::AggregatedListRegionHealthAggregationPoliciesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_health_aggregation_policies.v1.AggregatedListRegionHealthAggregationPoliciesRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/region_health_aggregation_policies/v1/region_health_aggregation_policies.proto#L136). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::HealthAggregationPoliciesScopedList > >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.HealthAggregationPoliciesScopedList](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_062.proto#L24), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteHealthAggregationPolicy(std::string const &, std::string const &, std::string const &, Options)

Deletes the specified HealthAggregationPolicy in the given region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/delete>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`health_aggregation_policy` |  `std::string const &`   
Name of the HealthAggregationPolicy resource to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteHealthAggregationPolicy(NoAwaitTag, std::string const &, std::string const &, std::string const &, Options)

Deletes the specified HealthAggregationPolicy in the given region. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`health_aggregation_policy` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteHealthAggregationPolicy(google::cloud::cpp::compute::region_health_aggregation_policies::v1::DeleteHealthAggregationPolicyRequest const &, Options)

Deletes the specified HealthAggregationPolicy in the given region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/delete>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::DeleteHealthAggregationPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_health_aggregation_policies.v1.DeleteHealthAggregationPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/region_health_aggregation_policies/v1/region_health_aggregation_policies.proto#L244). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteHealthAggregationPolicy(NoAwaitTag, google::cloud::cpp::compute::region_health_aggregation_policies::v1::DeleteHealthAggregationPolicyRequest const &, Options)

Deletes the specified HealthAggregationPolicy in the given region. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::DeleteHealthAggregationPolicyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteHealthAggregationPolicy(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes the specified HealthAggregationPolicy in the given region. 

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
  
### GetHealthAggregationPolicy(std::string const &, std::string const &, std::string const &, Options)

Returns the specified HealthAggregationPolicy resource in the given region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`health_aggregation_policy` |  `std::string const &`   
Name of the HealthAggregationPolicy resource to return.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::HealthAggregationPolicy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.HealthAggregationPolicy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_062.proto#L143)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetHealthAggregationPolicy(google::cloud::cpp::compute::region_health_aggregation_policies::v1::GetHealthAggregationPolicyRequest const &, Options)

Returns the specified HealthAggregationPolicy resource in the given region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::GetHealthAggregationPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_health_aggregation_policies.v1.GetHealthAggregationPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/region_health_aggregation_policies/v1/region_health_aggregation_policies.proto#L282). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::HealthAggregationPolicy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.HealthAggregationPolicy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_062.proto#L143)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### InsertHealthAggregationPolicy(std::string const &, std::string const &, google::cloud::cpp::compute::v1::HealthAggregationPolicy const &, Options)

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/insert>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`health_aggregation_policy_resource` |  `google::cloud::cpp::compute::v1::HealthAggregationPolicy const &`   
The HealthAggregationPolicy for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertHealthAggregationPolicy(NoAwaitTag, std::string const &, std::string const &, google::cloud::cpp::compute::v1::HealthAggregationPolicy const &, Options)

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`health_aggregation_policy_resource` |  `google::cloud::cpp::compute::v1::HealthAggregationPolicy const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertHealthAggregationPolicy(google::cloud::cpp::compute::region_health_aggregation_policies::v1::InsertHealthAggregationPolicyRequest const &, Options)

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/insert>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::InsertHealthAggregationPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_health_aggregation_policies.v1.InsertHealthAggregationPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/region_health_aggregation_policies/v1/region_health_aggregation_policies.proto#L299). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertHealthAggregationPolicy(NoAwaitTag, google::cloud::cpp::compute::region_health_aggregation_policies::v1::InsertHealthAggregationPolicyRequest const &, Options)

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::InsertHealthAggregationPolicyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertHealthAggregationPolicy(google::cloud::cpp::compute::v1::Operation const &, Options)

Create a HealthAggregationPolicy in the specified project in the given region using the parameters that are included in the request. 

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
  
### ListRegionHealthAggregationPolicies(std::string const &, std::string const &, Options)

Lists the HealthAggregationPolicies for a project in the given region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/list>

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
`StreamRange< google::cloud::cpp::compute::v1::HealthAggregationPolicy >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.HealthAggregationPolicy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_062.proto#L143), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListRegionHealthAggregationPolicies(google::cloud::cpp::compute::region_health_aggregation_policies::v1::ListRegionHealthAggregationPoliciesRequest, Options)

Lists the HealthAggregationPolicies for a project in the given region. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::ListRegionHealthAggregationPoliciesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_health_aggregation_policies.v1.ListRegionHealthAggregationPoliciesRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/region_health_aggregation_policies/v1/region_health_aggregation_policies.proto#L336). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::HealthAggregationPolicy >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.HealthAggregationPolicy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_062.proto#L143), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchHealthAggregationPolicy(std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::HealthAggregationPolicy const &, Options)

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. 

This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. <https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/patch>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
Name of the region scoping this request.   
`health_aggregation_policy` |  `std::string const &`   
Name of the HealthAggregationPolicy to update. The name must be 1-63 characters long, and comply with RFC1035.   
`health_aggregation_policy_resource` |  `google::cloud::cpp::compute::v1::HealthAggregationPolicy const &`   
The HealthAggregationPolicy for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchHealthAggregationPolicy(NoAwaitTag, std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::HealthAggregationPolicy const &, Options)

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`project` |  `std::string const &`   
  
`region` |  `std::string const &`   
  
`health_aggregation_policy` |  `std::string const &`   
  
`health_aggregation_policy_resource` |  `google::cloud::cpp::compute::v1::HealthAggregationPolicy const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### PatchHealthAggregationPolicy(google::cloud::cpp::compute::region_health_aggregation_policies::v1::PatchHealthAggregationPolicyRequest const &, Options)

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. 

This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. <https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/patch>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::PatchHealthAggregationPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_health_aggregation_policies.v1.PatchHealthAggregationPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/region_health_aggregation_policies/v1/region_health_aggregation_policies.proto#L434). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchHealthAggregationPolicy(NoAwaitTag, google::cloud::cpp::compute::region_health_aggregation_policies::v1::PatchHealthAggregationPolicyRequest const &, Options)

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::PatchHealthAggregationPolicyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### PatchHealthAggregationPolicy(google::cloud::cpp::compute::v1::Operation const &, Options)

Updates the specified regional HealthAggregationPolicy resource with the data included in the request. 

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
  
### TestIamPermissions(std::string const &, std::string const &, std::string const &, google::cloud::cpp::compute::v1::TestPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/testIamPermissions>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
[Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request.   
`region` |  `std::string const &`   
The name of the region for this request.   
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
  
### TestIamPermissions(google::cloud::cpp::compute::region_health_aggregation_policies::v1::TestIamPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/testIamPermissions>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::region_health_aggregation_policies::v1::TestIamPermissionsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.region_health_aggregation_policies.v1.TestIamPermissionsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/region_health_aggregation_policies/v1/region_health_aggregation_policies.proto#L478). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
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
