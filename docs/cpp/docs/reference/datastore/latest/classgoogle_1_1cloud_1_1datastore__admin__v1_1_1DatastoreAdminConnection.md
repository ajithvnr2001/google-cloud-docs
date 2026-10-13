---
url: https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__admin__v1_1_1DatastoreAdminConnection/
title: Class DatastoreAdminConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:57.385101+00:00
---

# Class DatastoreAdminConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__admin__v1_1_1DatastoreAdminConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class DatastoreAdminConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

The [`DatastoreAdminConnection`](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__admin__v1_1_1DatastoreAdminConnection) object for [`DatastoreAdminClient`](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__admin__v1_1_1DatastoreAdminClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`DatastoreAdminClient`](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__admin__v1_1_1DatastoreAdminClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`DatastoreAdminClient`](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__admin__v1_1_1DatastoreAdminClient).

To create a concrete instance, see [`MakeDatastoreAdminConnection()`](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/namespacegoogle_1_1cloud_1_1datastore__admin__v1).

For mocking, see [`datastore_admin_v1_mocks::MockDatastoreAdminConnection`](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__admin__v1__mocks_1_1MockDatastoreAdminConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ExportEntities(google::datastore::admin::v1::ExportEntitiesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::datastore::admin::v1::ExportEntitiesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::datastore::admin::v1::ExportEntitiesResponse > >` |   
  
### virtual ExportEntities(NoAwaitTag, google::datastore::admin::v1::ExportEntitiesRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::datastore::admin::v1::ExportEntitiesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ExportEntities(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::datastore::admin::v1::ExportEntitiesResponse > >` |   
  
### virtual ImportEntities(google::datastore::admin::v1::ImportEntitiesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::datastore::admin::v1::ImportEntitiesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::datastore::admin::v1::ImportEntitiesMetadata > >` |   
  
### virtual ImportEntities(NoAwaitTag, google::datastore::admin::v1::ImportEntitiesRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::datastore::admin::v1::ImportEntitiesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ImportEntities(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::datastore::admin::v1::ImportEntitiesMetadata > >` |   
  
### virtual CreateIndex(google::datastore::admin::v1::CreateIndexRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::datastore::admin::v1::CreateIndexRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::datastore::admin::v1::Index > >` |   
  
### virtual CreateIndex(NoAwaitTag, google::datastore::admin::v1::CreateIndexRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::datastore::admin::v1::CreateIndexRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateIndex(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::datastore::admin::v1::Index > >` |   
  
### virtual DeleteIndex(google::datastore::admin::v1::DeleteIndexRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::datastore::admin::v1::DeleteIndexRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::datastore::admin::v1::Index > >` |   
  
### virtual DeleteIndex(NoAwaitTag, google::datastore::admin::v1::DeleteIndexRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::datastore::admin::v1::DeleteIndexRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteIndex(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::datastore::admin::v1::Index > >` |   
  
### virtual GetIndex(google::datastore::admin::v1::GetIndexRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::datastore::admin::v1::GetIndexRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::datastore::admin::v1::Index >` |   
  
### virtual ListIndexes(google::datastore::admin::v1::ListIndexesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::datastore::admin::v1::ListIndexesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::datastore::admin::v1::Index >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

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
