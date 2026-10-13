---
url: https://docs.cloud.google.com/cpp/docs/reference/cloudcontrolspartner/latest/classgoogle_1_1cloud_1_1cloudcontrolspartner__v1_1_1CloudControlsPartnerMonitoringClient/
title: Class CloudControlsPartnerMonitoringClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:45.679521+00:00
---

# Class CloudControlsPartnerMonitoringClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/cloudcontrolspartner/latest/classgoogle_1_1cloud_1_1cloudcontrolspartner__v1_1_1CloudControlsPartnerMonitoringClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class CloudControlsPartnerMonitoringClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0 

Service describing handlers for resources. 

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### CloudControlsPartnerMonitoringClient(CloudControlsPartnerMonitoringClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `CloudControlsPartnerMonitoringClient const &`   
  
  
### CloudControlsPartnerMonitoringClient(CloudControlsPartnerMonitoringClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `CloudControlsPartnerMonitoringClient &&`   
  
  
### CloudControlsPartnerMonitoringClient(std::shared_ptr< CloudControlsPartnerMonitoringConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< CloudControlsPartnerMonitoringConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(CloudControlsPartnerMonitoringClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `CloudControlsPartnerMonitoringClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`CloudControlsPartnerMonitoringClient &` |   
  
### operator=(CloudControlsPartnerMonitoringClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `CloudControlsPartnerMonitoringClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`CloudControlsPartnerMonitoringClient &` |   
  
## Functions 

### ListViolations(std::string const &, Options)

Lists Violations for a workload Callers may also choose to read across multiple Customers or for a single customer as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of {customer} & {workload}. 

Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `std::string const &`   
Required. Parent resource Format `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`  
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cloudcontrolspartner::v1::Violation >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cloudcontrolspartner.v1.Violation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/cloudcontrolspartner/v1/violations.proto#L33), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListViolations(google::cloud::cloudcontrolspartner::v1::ListViolationsRequest, Options)

Lists Violations for a workload Callers may also choose to read across multiple Customers or for a single customer as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of {customer} & {workload}. 

Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cloudcontrolspartner::v1::ListViolationsRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cloudcontrolspartner.v1.ListViolationsRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/cloudcontrolspartner/v1/violations.proto#L178). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cloudcontrolspartner::v1::Violation >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cloudcontrolspartner.v1.Violation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/cloudcontrolspartner/v1/violations.proto#L33), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### GetViolation(std::string const &, Options)

Gets details of a single Violation. 

**Parameters**  
---  
**Name** | **Description**  
`name` |  `std::string const &`   
Required. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/violations/{violation}`  
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cloudcontrolspartner::v1::Violation >` | the result of the RPC. The response message type ([google.cloud.cloudcontrolspartner.v1.Violation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/cloudcontrolspartner/v1/violations.proto#L33)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetViolation(google::cloud::cloudcontrolspartner::v1::GetViolationRequest const &, Options)

Gets details of a single Violation. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cloudcontrolspartner::v1::GetViolationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cloudcontrolspartner.v1.GetViolationRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/cloudcontrolspartner/v1/violations.proto#L224). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cloudcontrolspartner::v1::Violation >` | the result of the RPC. The response message type ([google.cloud.cloudcontrolspartner.v1.Violation](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/cloudcontrolspartner/v1/violations.proto#L33)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
