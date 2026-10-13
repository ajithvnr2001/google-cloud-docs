---
url: https://docs.cloud.google.com/cpp/docs/reference/managedkafka/latest/classgoogle_1_1cloud_1_1managedkafka__schemaregistry__v1__mocks_1_1MockManagedSchemaRegistryConnection/
title: Class MockManagedSchemaRegistryConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:31.721015+00:00
---

# Class MockManagedSchemaRegistryConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/managedkafka/latest/classgoogle_1_1cloud_1_1managedkafka__schemaregistry__v1__mocks_1_1MockManagedSchemaRegistryConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class MockManagedSchemaRegistryConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0 

A class to mock `ManagedSchemaRegistryConnection`. 

Application developers may want to test their code with simulated responses, including errors, from an object of type `ManagedSchemaRegistryClient`. To do so, construct an object of type `ManagedSchemaRegistryClient` with an instance of this class. Then use the Google Test framework functions to program the behavior of this mock.

###### See Also

[This example](https://cloud.google.com/cpp/docs/reference/bigquery/latest/bigquery-read-mock) for how to test your application with GoogleTest. While the example showcases types from the BigQuery library, the underlying principles apply for any pair of `*Client` and `*Connection`. 

## Functions 

### virtual options()

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual GetSchemaRegistry(google::cloud::managedkafka::schemaregistry::v1::GetSchemaRegistryRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::GetSchemaRegistryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaRegistry >` |   
  
### virtual ListSchemaRegistries(google::cloud::managedkafka::schemaregistry::v1::ListSchemaRegistriesRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::ListSchemaRegistriesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::ListSchemaRegistriesResponse >` |   
  
### virtual CreateSchemaRegistry(google::cloud::managedkafka::schemaregistry::v1::CreateSchemaRegistryRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::CreateSchemaRegistryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaRegistry >` |   
  
### virtual DeleteSchemaRegistry(google::cloud::managedkafka::schemaregistry::v1::DeleteSchemaRegistryRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::DeleteSchemaRegistryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual GetContext(google::cloud::managedkafka::schemaregistry::v1::GetContextRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::GetContextRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::Context >` |   
  
### virtual ListContexts(google::cloud::managedkafka::schemaregistry::v1::ListContextsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::ListContextsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual GetSchema(google::cloud::managedkafka::schemaregistry::v1::GetSchemaRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::GetSchemaRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::Schema >` |   
  
### virtual GetRawSchema(google::cloud::managedkafka::schemaregistry::v1::GetSchemaRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::GetSchemaRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual ListSchemaVersions(google::cloud::managedkafka::schemaregistry::v1::ListSchemaVersionsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::ListSchemaVersionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual ListSchemaTypes(google::cloud::managedkafka::schemaregistry::v1::ListSchemaTypesRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::ListSchemaTypesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual ListSubjects(google::cloud::managedkafka::schemaregistry::v1::ListSubjectsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::ListSubjectsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual ListSubjectsBySchemaId(google::cloud::managedkafka::schemaregistry::v1::ListSubjectsBySchemaIdRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::ListSubjectsBySchemaIdRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual DeleteSubject(google::cloud::managedkafka::schemaregistry::v1::DeleteSubjectRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::DeleteSubjectRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual LookupVersion(google::cloud::managedkafka::schemaregistry::v1::LookupVersionRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::LookupVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaVersion >` |   
  
### virtual GetVersion(google::cloud::managedkafka::schemaregistry::v1::GetVersionRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::GetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaVersion >` |   
  
### virtual GetRawSchemaVersion(google::cloud::managedkafka::schemaregistry::v1::GetVersionRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::GetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual ListVersions(google::cloud::managedkafka::schemaregistry::v1::ListVersionsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::ListVersionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual CreateVersion(google::cloud::managedkafka::schemaregistry::v1::CreateVersionRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::CreateVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::CreateVersionResponse >` |   
  
### virtual DeleteVersion(google::cloud::managedkafka::schemaregistry::v1::DeleteVersionRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::DeleteVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual ListReferencedSchemas(google::cloud::managedkafka::schemaregistry::v1::ListReferencedSchemasRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::ListReferencedSchemasRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::api::HttpBody >` |   
  
### virtual CheckCompatibility(google::cloud::managedkafka::schemaregistry::v1::CheckCompatibilityRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::CheckCompatibilityRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::CheckCompatibilityResponse >` |   
  
### virtual GetSchemaConfig(google::cloud::managedkafka::schemaregistry::v1::GetSchemaConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::GetSchemaConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaConfig >` |   
  
### virtual UpdateSchemaConfig(google::cloud::managedkafka::schemaregistry::v1::UpdateSchemaConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::UpdateSchemaConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaConfig >` |   
  
### virtual DeleteSchemaConfig(google::cloud::managedkafka::schemaregistry::v1::DeleteSchemaConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::DeleteSchemaConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaConfig >` |   
  
### virtual GetSchemaMode(google::cloud::managedkafka::schemaregistry::v1::GetSchemaModeRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::GetSchemaModeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaMode >` |   
  
### virtual UpdateSchemaMode(google::cloud::managedkafka::schemaregistry::v1::UpdateSchemaModeRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::UpdateSchemaModeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaMode >` |   
  
### virtual DeleteSchemaMode(google::cloud::managedkafka::schemaregistry::v1::DeleteSchemaModeRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::managedkafka::schemaregistry::v1::DeleteSchemaModeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::managedkafka::schemaregistry::v1::SchemaMode >` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::location::Location >` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::location::Location >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
