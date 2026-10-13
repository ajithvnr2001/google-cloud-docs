---
url: https://docs.cloud.google.com/cpp/docs/reference/contentwarehouse/latest/classgoogle_1_1cloud_1_1contentwarehouse__v1_1_1DocumentSchemaServiceConnection/
title: Class DocumentSchemaServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:29.012813+00:00
---

# Class DocumentSchemaServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/contentwarehouse/latest/classgoogle_1_1cloud_1_1contentwarehouse__v1_1_1DocumentSchemaServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class DocumentSchemaServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0 

The [`DocumentSchemaServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/contentwarehouse/latest/classgoogle_1_1cloud_1_1contentwarehouse__v1_1_1DocumentSchemaServiceConnection) object for [`DocumentSchemaServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/contentwarehouse/latest/classgoogle_1_1cloud_1_1contentwarehouse__v1_1_1DocumentSchemaServiceClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`DocumentSchemaServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/contentwarehouse/latest/classgoogle_1_1cloud_1_1contentwarehouse__v1_1_1DocumentSchemaServiceClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`DocumentSchemaServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/contentwarehouse/latest/classgoogle_1_1cloud_1_1contentwarehouse__v1_1_1DocumentSchemaServiceClient).

To create a concrete instance, see [`MakeDocumentSchemaServiceConnection()`](https://docs.cloud.google.com/cpp/docs/reference/contentwarehouse/latest/namespacegoogle_1_1cloud_1_1contentwarehouse__v1).

For mocking, see [`contentwarehouse_v1_mocks::MockDocumentSchemaServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/contentwarehouse/latest/classgoogle_1_1cloud_1_1contentwarehouse__v1__mocks_1_1MockDocumentSchemaServiceConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateDocumentSchema(google::cloud::contentwarehouse::v1::CreateDocumentSchemaRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::contentwarehouse::v1::CreateDocumentSchemaRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::contentwarehouse::v1::DocumentSchema >` |   
  
### virtual UpdateDocumentSchema(google::cloud::contentwarehouse::v1::UpdateDocumentSchemaRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::contentwarehouse::v1::UpdateDocumentSchemaRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::contentwarehouse::v1::DocumentSchema >` |   
  
### virtual GetDocumentSchema(google::cloud::contentwarehouse::v1::GetDocumentSchemaRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::contentwarehouse::v1::GetDocumentSchemaRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::contentwarehouse::v1::DocumentSchema >` |   
  
### virtual DeleteDocumentSchema(google::cloud::contentwarehouse::v1::DeleteDocumentSchemaRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::contentwarehouse::v1::DeleteDocumentSchemaRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual ListDocumentSchemas(google::cloud::contentwarehouse::v1::ListDocumentSchemasRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::contentwarehouse::v1::ListDocumentSchemasRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::contentwarehouse::v1::DocumentSchema >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
