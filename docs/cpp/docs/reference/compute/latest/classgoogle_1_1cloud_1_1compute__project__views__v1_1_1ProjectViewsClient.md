---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__project__views__v1_1_1ProjectViewsClient/
title: Class ProjectViewsClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:21.116678+00:00
---

# Class ProjectViewsClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__project__views__v1_1_1ProjectViewsClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ProjectViewsClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the projectViews resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/projectViews>

This client uses ProjectViews version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### ProjectViewsClient(ProjectViewsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `ProjectViewsClient const &`   
  
  
### ProjectViewsClient(ProjectViewsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `ProjectViewsClient &&`   
  
  
### ProjectViewsClient(std::shared_ptr< ProjectViewsConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< ProjectViewsConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(ProjectViewsClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `ProjectViewsClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`ProjectViewsClient &` |   
  
### operator=(ProjectViewsClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `ProjectViewsClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`ProjectViewsClient &` |   
  
## Functions 

### GetProjectView(std::string const &, std::string const &, Options)

Returns the specified global ProjectViews resource, with a regional context. 

This regional API endpoint reads resource metadata from regional read-only replicas. Because changes are copied to these regional replicas asynchronously, for real-time resource reads or any write operations (creating, updating, or deleting resources), use the global [projects.get](https://cloud.google.com/compute/docs/reference/rest/v1/projects/get) endpoint. <https://cloud.google.com/compute/docs/reference/rest/v1/projectViews/get>

**Parameters**  
---  
**Name** | **Description**  
`project` |  `std::string const &`   
Required. [Project](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Project.html) ID for this request. This is part of the URL path.   
`region` |  `std::string const &`   
Required. Name of the region for this request. This is part of the URL path.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::ProjectView >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.ProjectView](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_117.proto#L30)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetProjectView(google::cloud::cpp::compute::project_views::v1::GetProjectViewRequest const &, Options)

Returns the specified global ProjectViews resource, with a regional context. 

This regional API endpoint reads resource metadata from regional read-only replicas. Because changes are copied to these regional replicas asynchronously, for real-time resource reads or any write operations (creating, updating, or deleting resources), use the global [projects.get](https://cloud.google.com/compute/docs/reference/rest/v1/projects/get) endpoint. <https://cloud.google.com/compute/docs/reference/rest/v1/projectViews/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::project_views::v1::GetProjectViewRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.project_views.v1.GetProjectViewRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/project_views/v1/project_views.proto#L58). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::ProjectView >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.ProjectView](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_117.proto#L30)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
