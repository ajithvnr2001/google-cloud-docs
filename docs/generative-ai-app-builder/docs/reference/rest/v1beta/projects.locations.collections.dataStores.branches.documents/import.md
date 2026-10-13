---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents/import/
title: Method: projects.locations.collections.dataStores.branches.documents.import \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:39.174073+00:00
---

# Method: projects.locations.collections.dataStores.branches.documents.import  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents/import/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.branches.documents.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Bulk import of multiple `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)`s. Request processing may be synchronous. Non-existing items are created.

Note: It is possible for a subset of the `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document)`s to be successfully updated.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:import`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/branches/{branch}`. Requires create/update permission.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "errorConfig": {
        object ([ImportErrorConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ImportErrorConfig))
      },
      "reconciliationMode": enum ([ReconciliationMode](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ReconciliationMode)),
      "updateMask": string,
      "autoGenerateIds": boolean,
      "idField": string,
      "forceRefreshContent": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inlineSource": {
        object (InlineSource)
      },
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/GcsSource))
      },
      "bigquerySource": {
        object ([BigQuerySource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigQuerySource))
      },
      "fhirStoreSource": {
        object ([FhirStoreSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/FhirStoreSource))
      },
      "spannerSource": {
        object ([SpannerSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SpannerSource))
      },
      "cloudSqlSource": {
        object ([CloudSqlSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/CloudSqlSource))
      },
      "firestoreSource": {
        object ([FirestoreSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/FirestoreSource))
      },
      "alloyDbSource": {
        object ([AlloyDbSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/AlloyDbSource))
      },
      "bigtableSource": {
        object ([BigtableSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigtableSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`errorConfig` |  `object (`[ImportErrorConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ImportErrorConfig)`)` The desired location of errors incurred during the Import.  
`reconciliationMode` |  `enum (`[ReconciliationMode](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ReconciliationMode)`)` The mode of reconciliation between existing documents and the documents to be imported. Defaults to `[ReconciliationMode.INCREMENTAL](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ReconciliationMode#ENUM_VALUES.INCREMENTAL)`.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Indicates which fields in the provided imported documents to update. If not set, the default is to update all fields.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`autoGenerateIds` |  `boolean` Whether to automatically generate IDs for the documents if absent.If set to `true`, `[Document.id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.id)`s are automatically generated based on the hash of the payload, where IDs may not be consistent during multiple imports. In which case `[ReconciliationMode.FULL](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ReconciliationMode#ENUM_VALUES.FULL)` is highly recommended to avoid duplicate contents. If unset or set to `false`, `[Document.id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.id)`s have to be specified using `[idField](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.branches.documents/import#body.request_body.FIELDS.id_field)`, otherwise, documents without IDs fail to be imported.Supported data sources:

  * `[GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/GcsSource)`. `[GcsSource.data_schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/GcsSource#FIELDS.data_schema)` must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * `[BigQuerySource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigQuerySource)`. `[BigQuerySource.data_schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigQuerySource#FIELDS.data_schema)` must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * `[SpannerSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SpannerSource)`.
  * `[CloudSqlSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/CloudSqlSource)`.
  * `[FirestoreSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/FirestoreSource)`.
  * `[BigtableSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigtableSource)`.

  
`idField` |  `string` The field indicates the ID field or column to be used as unique IDs of the documents.For `[GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/GcsSource)` it is the key of the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`. For others, it may be the column name of the table where the unique ids are stored.The values of the JSON field or the table column are used as the `[Document.id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.id)`s. The JSON field or the table column must be of string type, and the values must be set as valid strings conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) with 1-63 characters. Otherwise, documents without valid IDs fail to be imported.Only set this field when `[autoGenerateIds](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.branches.documents/import#body.request_body.FIELDS.auto_generate_ids)` is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.If it is unset, a default value `Id` is used when importing from the allowed data sources.Supported data sources:

  * `[GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/GcsSource)`. `[GcsSource.data_schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/GcsSource#FIELDS.data_schema)` must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * `[BigQuerySource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigQuerySource)`. `[BigQuerySource.data_schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigQuerySource#FIELDS.data_schema)` must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * `[SpannerSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SpannerSource)`.
  * `[CloudSqlSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/CloudSqlSource)`.
  * `[BigtableSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigtableSource)`.

  
`forceRefreshContent` |  `boolean` Optional. Whether to force refresh the unstructured content of the documents.If set to `true`, the content part of the documents will be refreshed regardless of the update status of the referencing content.  
Required. The source of the input. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inlineSource` |  `object (`InlineSource`)` The Inline source for the input content for documents.  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/GcsSource)`)` Cloud Storage location for the input content.  
`bigquerySource` |  `object (`[BigQuerySource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigQuerySource)`)` BigQuery input source.  
`fhirStoreSource` |  `object (`[FhirStoreSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/FhirStoreSource)`)` FhirStore input source.  
`spannerSource` |  `object (`[SpannerSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/SpannerSource)`)` Spanner input source.  
`cloudSqlSource` |  `object (`[CloudSqlSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/CloudSqlSource)`)` Cloud SQL input source.  
`firestoreSource` |  `object (`[FirestoreSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/FirestoreSource)`)` Firestore input source.  
`alloyDbSource` |  `object (`[AlloyDbSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/AlloyDbSource)`)` AlloyDB input source.  
`bigtableSource` |  `object (`[BigtableSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/BigtableSource)`)` Cloud Bigtable input source.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.documents.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
