---
url: https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1__mocks_1_1MockHiveMetastoreServiceConnection/
title: Class MockHiveMetastoreServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:37.284688+00:00
---

# Class MockHiveMetastoreServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/biglake/latest/classgoogle_1_1cloud_1_1biglake__hive__v1__mocks_1_1MockHiveMetastoreServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class MockHiveMetastoreServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0 

A class to mock `HiveMetastoreServiceConnection`. 

Application developers may want to test their code with simulated responses, including errors, from an object of type `HiveMetastoreServiceClient`. To do so, construct an object of type `HiveMetastoreServiceClient` with an instance of this class. Then use the Google Test framework functions to program the behavior of this mock.

###### See Also

[This example](https://cloud.google.com/cpp/docs/reference/bigquery/latest/bigquery-read-mock) for how to test your application with GoogleTest. While the example showcases types from the BigQuery library, the underlying principles apply for any pair of `*Client` and `*Connection`. 

## Functions 

### virtual options()

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateHiveCatalog(google::cloud::biglake::hive::v1::CreateHiveCatalogRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::CreateHiveCatalogRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveCatalog >` |   
  
### virtual GetHiveCatalog(google::cloud::biglake::hive::v1::GetHiveCatalogRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::GetHiveCatalogRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveCatalog >` |   
  
### virtual ListHiveCatalogs(google::cloud::biglake::hive::v1::ListHiveCatalogsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::ListHiveCatalogsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::biglake::hive::v1::HiveCatalog >` |   
  
### virtual UpdateHiveCatalog(google::cloud::biglake::hive::v1::UpdateHiveCatalogRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::UpdateHiveCatalogRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveCatalog >` |   
  
### virtual DeleteHiveCatalog(google::cloud::biglake::hive::v1::DeleteHiveCatalogRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::DeleteHiveCatalogRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CreateHiveDatabase(google::cloud::biglake::hive::v1::CreateHiveDatabaseRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::CreateHiveDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveDatabase >` |   
  
### virtual GetHiveDatabase(google::cloud::biglake::hive::v1::GetHiveDatabaseRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::GetHiveDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveDatabase >` |   
  
### virtual ListHiveDatabases(google::cloud::biglake::hive::v1::ListHiveDatabasesRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::ListHiveDatabasesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::biglake::hive::v1::HiveDatabase >` |   
  
### virtual UpdateHiveDatabase(google::cloud::biglake::hive::v1::UpdateHiveDatabaseRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::UpdateHiveDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveDatabase >` |   
  
### virtual DeleteHiveDatabase(google::cloud::biglake::hive::v1::DeleteHiveDatabaseRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::DeleteHiveDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CreateHiveTable(google::cloud::biglake::hive::v1::CreateHiveTableRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::CreateHiveTableRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveTable >` |   
  
### virtual GetHiveTable(google::cloud::biglake::hive::v1::GetHiveTableRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::GetHiveTableRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveTable >` |   
  
### virtual ListHiveTables(google::cloud::biglake::hive::v1::ListHiveTablesRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::ListHiveTablesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::biglake::hive::v1::HiveTable >` |   
  
### virtual UpdateHiveTable(google::cloud::biglake::hive::v1::UpdateHiveTableRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::UpdateHiveTableRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::HiveTable >` |   
  
### virtual DeleteHiveTable(google::cloud::biglake::hive::v1::DeleteHiveTableRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::DeleteHiveTableRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual BatchCreatePartitions(google::cloud::biglake::hive::v1::BatchCreatePartitionsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::BatchCreatePartitionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::BatchCreatePartitionsResponse >` |   
  
### virtual BatchDeletePartitions(google::cloud::biglake::hive::v1::BatchDeletePartitionsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::BatchDeletePartitionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual BatchUpdatePartitions(google::cloud::biglake::hive::v1::BatchUpdatePartitionsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::BatchUpdatePartitionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::BatchUpdatePartitionsResponse >` |   
  
### virtual ListPartitions(google::cloud::biglake::hive::v1::ListPartitionsRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::ListPartitionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::biglake::hive::v1::ListPartitionsResponse >` |   
  
### virtual FailoverHiveCatalog(google::cloud::biglake::hive::v1::FailoverHiveCatalogRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::biglake::hive::v1::FailoverHiveCatalogRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::biglake::hive::v1::FailoverHiveCatalogResponse >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
