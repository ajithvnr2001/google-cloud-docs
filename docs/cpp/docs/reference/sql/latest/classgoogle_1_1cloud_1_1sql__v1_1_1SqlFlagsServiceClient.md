---
url: https://docs.cloud.google.com/cpp/docs/reference/sql/latest/classgoogle_1_1cloud_1_1sql__v1_1_1SqlFlagsServiceClient/
title: Class SqlFlagsServiceClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:50.127994+00:00
---

# Class SqlFlagsServiceClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/sql/latest/classgoogle_1_1cloud_1_1sql__v1_1_1SqlFlagsServiceClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class SqlFlagsServiceClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Service to manage database flags for Cloud SQL instances. 

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### SqlFlagsServiceClient(SqlFlagsServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `SqlFlagsServiceClient const &`   
  
  
### SqlFlagsServiceClient(SqlFlagsServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `SqlFlagsServiceClient &&`   
  
  
### SqlFlagsServiceClient(std::shared_ptr< SqlFlagsServiceConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< SqlFlagsServiceConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(SqlFlagsServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `SqlFlagsServiceClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`SqlFlagsServiceClient &` |   
  
### operator=(SqlFlagsServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `SqlFlagsServiceClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`SqlFlagsServiceClient &` |   
  
## Functions 

### List(google::cloud::sql::v1::SqlFlagsListRequest const &, Options)

Lists all available database flags for Cloud SQL instances. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::sql::v1::SqlFlagsListRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.sql.v1.SqlFlagsListRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/sql/v1/cloud_sql_flags.proto#L46). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::sql::v1::FlagsListResponse >` | the result of the RPC. The response message type ([google.cloud.sql.v1.FlagsListResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/sql/v1/cloud_sql_flags.proto#L57)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
