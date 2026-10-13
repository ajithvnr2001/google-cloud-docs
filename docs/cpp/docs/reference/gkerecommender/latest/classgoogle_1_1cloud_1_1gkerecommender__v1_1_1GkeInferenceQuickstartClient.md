---
url: https://docs.cloud.google.com/cpp/docs/reference/gkerecommender/latest/classgoogle_1_1cloud_1_1gkerecommender__v1_1_1GkeInferenceQuickstartClient/
title: Class GkeInferenceQuickstartClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:24.144712+00:00
---

# Class GkeInferenceQuickstartClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/gkerecommender/latest/classgoogle_1_1cloud_1_1gkerecommender__v1_1_1GkeInferenceQuickstartClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class GkeInferenceQuickstartClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1 

GKE Inference Quickstart (GIQ) service provides profiles with performance metrics for popular models and model servers across multiple accelerators. 

These profiles help generate optimized best practices for running inference on GKE.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### GkeInferenceQuickstartClient(GkeInferenceQuickstartClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `GkeInferenceQuickstartClient const &`   
  
  
### GkeInferenceQuickstartClient(GkeInferenceQuickstartClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `GkeInferenceQuickstartClient &&`   
  
  
### GkeInferenceQuickstartClient(std::shared_ptr< GkeInferenceQuickstartConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< GkeInferenceQuickstartConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(GkeInferenceQuickstartClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `GkeInferenceQuickstartClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`GkeInferenceQuickstartClient &` |   
  
### operator=(GkeInferenceQuickstartClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `GkeInferenceQuickstartClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`GkeInferenceQuickstartClient &` |   
  
## Functions 

### FetchModels(google::cloud::gkerecommender::v1::FetchModelsRequest, Options)

Fetches available models. 

Open-source models follow the Huggingface Hub `owner/model_name` format.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkerecommender::v1::FetchModelsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.gkerecommender.v1.FetchModelsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L117). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::string >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains a [`std::string`](https://en.cppreference.com/w/cpp/string/basic_string).   
  
### FetchModelServers(google::cloud::gkerecommender::v1::FetchModelServersRequest, Options)

Fetches available model servers. 

Open-source model servers use simplified, lowercase names (e.g., `vllm`).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkerecommender::v1::FetchModelServersRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.gkerecommender.v1.FetchModelServersRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L152). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::string >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains a [`std::string`](https://en.cppreference.com/w/cpp/string/basic_string).   
  
### FetchModelServerVersions(google::cloud::gkerecommender::v1::FetchModelServerVersionsRequest, Options)

Fetches available model server versions. 

Open-source servers use their own versioning schemas (e.g., `vllm` uses semver like `v1.0.0`).

Some model servers have different versioning schemas depending on the accelerator. For example, `vllm` uses semver on GPUs, but returns nightly build tags on TPUs. All available versions will be returned when different schemas are present.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkerecommender::v1::FetchModelServerVersionsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.gkerecommender.v1.FetchModelServerVersionsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L194). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::string >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains a [`std::string`](https://en.cppreference.com/w/cpp/string/basic_string).   
  
### FetchProfiles(google::cloud::gkerecommender::v1::FetchProfilesRequest, Options)

Fetches available profiles. 

A profile contains performance metrics and cost information for a specific model server setup. Profiles can be filtered by parameters. If no filters are provided, all profiles are returned.

Profiles display a single value per performance metric based on the provided performance requirements. If no requirements are given, the metrics represent the inflection point. See [Run best practice inference with GKE Inference Quickstart recipes](about:invalid#zCSafez) for details.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkerecommender::v1::FetchProfilesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.gkerecommender.v1.FetchProfilesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L271). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkerecommender::v1::Profile >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.gkerecommender.v1.Profile](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L490), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GenerateOptimizedManifest(google::cloud::gkerecommender::v1::GenerateOptimizedManifestRequest const &, Options)

Generates an optimized deployment manifest for a given model and model server, based on the specified accelerator, performance targets, and configurations. 

See [Run best practice inference with GKE Inference Quickstart recipes](about:invalid#zCSafez) for deployment details.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkerecommender::v1::GenerateOptimizedManifestRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.gkerecommender.v1.GenerateOptimizedManifestRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L516). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkerecommender::v1::GenerateOptimizedManifestResponse >` | the result of the RPC. The response message type ([google.cloud.gkerecommender.v1.GenerateOptimizedManifestResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L559)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### FetchBenchmarkingData(google::cloud::gkerecommender::v1::FetchBenchmarkingDataRequest const &, Options)

Fetches all of the benchmarking data available for a profile. 

Benchmarking data returns all of the performance metrics available for a given model server setup on a given instance type.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkerecommender::v1::FetchBenchmarkingDataRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.gkerecommender.v1.FetchBenchmarkingDataRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L242). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkerecommender::v1::FetchBenchmarkingDataResponse >` | the result of the RPC. The response message type ([google.cloud.gkerecommender.v1.FetchBenchmarkingDataResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/gkerecommender/v1/gkerecommender.proto#L263)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
