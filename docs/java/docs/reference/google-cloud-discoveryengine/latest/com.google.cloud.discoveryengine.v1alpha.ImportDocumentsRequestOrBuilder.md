---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequestOrBuilder
title: Interface ImportDocumentsRequestOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:14.185303+00:00
---

# Interface ImportDocumentsRequestOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportDocumentsRequestOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ImportDocumentsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAlloyDbSource()
    
    
    public abstract AlloyDbSource getAlloyDbSource()

AlloyDB input source.

`.google.cloud.discoveryengine.v1alpha.AlloyDbSource alloy_db_source = 14;`

**Returns**  
---  
**Type** | **Description**  
`[AlloyDbSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.AlloyDbSource)` | The alloyDbSource.  
  
### getAlloyDbSourceOrBuilder()
    
    
    public abstract AlloyDbSourceOrBuilder getAlloyDbSourceOrBuilder()

AlloyDB input source.

`.google.cloud.discoveryengine.v1alpha.AlloyDbSource alloy_db_source = 14;`

**Returns**  
---  
**Type** | **Description**  
`[AlloyDbSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.AlloyDbSourceOrBuilder)` |   
  
### getAutoGenerateIds()
    
    
    public abstract boolean getAutoGenerateIds()

Whether to automatically generate IDs for the documents if absent.

If set to `true`, Document.ids are automatically generated based on the hash of the payload, where IDs may not be consistent during multiple imports. In which case ReconciliationMode.FULL is highly recommended to avoid duplicate contents. If unset or set to `false`, Document.ids have to be specified using id_field, otherwise, documents without IDs fail to be imported.

Supported data sources:

  * GcsSource. GcsSource.data_schema must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * BigQuerySource. BigQuerySource.data_schema must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * SpannerSource.
  * CloudSqlSource.
  * FirestoreSource.
  * BigtableSource.



`bool auto_generate_ids = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The autoGenerateIds.  
  
### getBigquerySource()
    
    
    public abstract BigQuerySource getBigquerySource()

BigQuery input source.

`.google.cloud.discoveryengine.v1alpha.BigQuerySource bigquery_source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BigQuerySource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.BigQuerySource)` | The bigquerySource.  
  
### getBigquerySourceOrBuilder()
    
    
    public abstract BigQuerySourceOrBuilder getBigquerySourceOrBuilder()

BigQuery input source.

`.google.cloud.discoveryengine.v1alpha.BigQuerySource bigquery_source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BigQuerySourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.BigQuerySourceOrBuilder)` |   
  
### getBigtableSource()
    
    
    public abstract BigtableSource getBigtableSource()

Cloud Bigtable input source.

`.google.cloud.discoveryengine.v1alpha.BigtableSource bigtable_source = 15;`

**Returns**  
---  
**Type** | **Description**  
`[BigtableSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.BigtableSource)` | The bigtableSource.  
  
### getBigtableSourceOrBuilder()
    
    
    public abstract BigtableSourceOrBuilder getBigtableSourceOrBuilder()

Cloud Bigtable input source.

`.google.cloud.discoveryengine.v1alpha.BigtableSource bigtable_source = 15;`

**Returns**  
---  
**Type** | **Description**  
`[BigtableSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.BigtableSourceOrBuilder)` |   
  
### getCloudSqlSource()
    
    
    public abstract CloudSqlSource getCloudSqlSource()

Cloud SQL input source.

`.google.cloud.discoveryengine.v1alpha.CloudSqlSource cloud_sql_source = 12;`

**Returns**  
---  
**Type** | **Description**  
`[CloudSqlSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.CloudSqlSource)` | The cloudSqlSource.  
  
### getCloudSqlSourceOrBuilder()
    
    
    public abstract CloudSqlSourceOrBuilder getCloudSqlSourceOrBuilder()

Cloud SQL input source.

`.google.cloud.discoveryengine.v1alpha.CloudSqlSource cloud_sql_source = 12;`

**Returns**  
---  
**Type** | **Description**  
`[CloudSqlSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.CloudSqlSourceOrBuilder)` |   
  
### getErrorConfig()
    
    
    public abstract ImportErrorConfig getErrorConfig()

The desired location of errors incurred during the Import.

`.google.cloud.discoveryengine.v1alpha.ImportErrorConfig error_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ImportErrorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.ImportErrorConfig)` | The errorConfig.  
  
### getErrorConfigOrBuilder()
    
    
    public abstract ImportErrorConfigOrBuilder getErrorConfigOrBuilder()

The desired location of errors incurred during the Import.

`.google.cloud.discoveryengine.v1alpha.ImportErrorConfig error_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ImportErrorConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.ImportErrorConfigOrBuilder)` |   
  
### getFhirStoreSource()
    
    
    public abstract FhirStoreSource getFhirStoreSource()

FhirStore input source.

`.google.cloud.discoveryengine.v1alpha.FhirStoreSource fhir_store_source = 10;`

**Returns**  
---  
**Type** | **Description**  
`[FhirStoreSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.FhirStoreSource)` | The fhirStoreSource.  
  
### getFhirStoreSourceOrBuilder()
    
    
    public abstract FhirStoreSourceOrBuilder getFhirStoreSourceOrBuilder()

FhirStore input source.

`.google.cloud.discoveryengine.v1alpha.FhirStoreSource fhir_store_source = 10;`

**Returns**  
---  
**Type** | **Description**  
`[FhirStoreSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.FhirStoreSourceOrBuilder)` |   
  
### getFirestoreSource()
    
    
    public abstract FirestoreSource getFirestoreSource()

Firestore input source.

`.google.cloud.discoveryengine.v1alpha.FirestoreSource firestore_source = 13;`

**Returns**  
---  
**Type** | **Description**  
`[FirestoreSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.FirestoreSource)` | The firestoreSource.  
  
### getFirestoreSourceOrBuilder()
    
    
    public abstract FirestoreSourceOrBuilder getFirestoreSourceOrBuilder()

Firestore input source.

`.google.cloud.discoveryengine.v1alpha.FirestoreSource firestore_source = 13;`

**Returns**  
---  
**Type** | **Description**  
`[FirestoreSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.FirestoreSourceOrBuilder)` |   
  
### getGcsSource()
    
    
    public abstract GcsSource getGcsSource()

Cloud Storage location for the input content.

`.google.cloud.discoveryengine.v1alpha.GcsSource gcs_source = 3;`

**Returns**  
---  
**Type** | **Description**  
`[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.GcsSource)` | The gcsSource.  
  
### getGcsSourceOrBuilder()
    
    
    public abstract GcsSourceOrBuilder getGcsSourceOrBuilder()

Cloud Storage location for the input content.

`.google.cloud.discoveryengine.v1alpha.GcsSource gcs_source = 3;`

**Returns**  
---  
**Type** | **Description**  
`[GcsSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.GcsSourceOrBuilder)` |   
  
### getIdField()
    
    
    public abstract String getIdField()

The field indicates the ID field or column to be used as unique IDs of the documents.

For GcsSource it is the key of the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`. For others, it may be the column name of the table where the unique ids are stored.

The values of the JSON field or the table column are used as the Document.ids. The JSON field or the table column must be of string type, and the values must be set as valid strings conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) with 1-63 characters. Otherwise, documents without valid IDs fail to be imported.

Only set this field when auto_generate_ids is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.

If it is unset, a default value `_id` is used when importing from the allowed data sources.

Supported data sources:

  * GcsSource. GcsSource.data_schema must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * BigQuerySource. BigQuerySource.data_schema must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * SpannerSource.
  * CloudSqlSource.
  * FirestoreSource.
  * BigtableSource.



`string id_field = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The idField.  
  
### getIdFieldBytes()
    
    
    public abstract ByteString getIdFieldBytes()

The field indicates the ID field or column to be used as unique IDs of the documents.

For GcsSource it is the key of the JSON field. For instance, `my_id` for JSON `{"my_id": "some_uuid"}`. For others, it may be the column name of the table where the unique ids are stored.

The values of the JSON field or the table column are used as the Document.ids. The JSON field or the table column must be of string type, and the values must be set as valid strings conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) with 1-63 characters. Otherwise, documents without valid IDs fail to be imported.

Only set this field when auto_generate_ids is unset or set as `false`. Otherwise, an INVALID_ARGUMENT error is thrown.

If it is unset, a default value `_id` is used when importing from the allowed data sources.

Supported data sources:

  * GcsSource. GcsSource.data_schema must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * BigQuerySource. BigQuerySource.data_schema must be `custom` or `csv`. Otherwise, an INVALID_ARGUMENT error is thrown.
  * SpannerSource.
  * CloudSqlSource.
  * FirestoreSource.
  * BigtableSource.



`string id_field = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for idField.  
  
### getInlineSource()
    
    
    public abstract ImportDocumentsRequest.InlineSource getInlineSource()

The Inline source for the input content for documents.

` .google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.InlineSource inline_source = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ImportDocumentsRequest.InlineSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.InlineSource)` | The inlineSource.  
  
### getInlineSourceOrBuilder()
    
    
    public abstract ImportDocumentsRequest.InlineSourceOrBuilder getInlineSourceOrBuilder()

The Inline source for the input content for documents.

` .google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.InlineSource inline_source = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ImportDocumentsRequest.InlineSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.InlineSourceOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Requires create/update permission.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Requires create/update permission.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getReconciliationMode()
    
    
    public abstract ImportDocumentsRequest.ReconciliationMode getReconciliationMode()

The mode of reconciliation between existing documents and the documents to be imported. Defaults to ReconciliationMode.INCREMENTAL.

` .google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.ReconciliationMode reconciliation_mode = 6; `

**Returns**  
---  
**Type** | **Description**  
`[ImportDocumentsRequest.ReconciliationMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.ReconciliationMode)` | The reconciliationMode.  
  
### getReconciliationModeValue()
    
    
    public abstract int getReconciliationModeValue()

The mode of reconciliation between existing documents and the documents to be imported. Defaults to ReconciliationMode.INCREMENTAL.

` .google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.ReconciliationMode reconciliation_mode = 6; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for reconciliationMode.  
  
### getSourceCase()
    
    
    public abstract ImportDocumentsRequest.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[ImportDocumentsRequest.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.SourceCase)` |   
  
### getSpannerSource()
    
    
    public abstract SpannerSource getSpannerSource()

Spanner input source.

`.google.cloud.discoveryengine.v1alpha.SpannerSource spanner_source = 11;`

**Returns**  
---  
**Type** | **Description**  
`[SpannerSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.SpannerSource)` | The spannerSource.  
  
### getSpannerSourceOrBuilder()
    
    
    public abstract SpannerSourceOrBuilder getSpannerSourceOrBuilder()

Spanner input source.

`.google.cloud.discoveryengine.v1alpha.SpannerSource spanner_source = 11;`

**Returns**  
---  
**Type** | **Description**  
`[SpannerSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1alpha.SpannerSourceOrBuilder)` |   
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

Indicates which fields in the provided imported documents to update. If not set, the default is to update all fields.

`.google.protobuf.FieldMask update_mask = 7;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

Indicates which fields in the provided imported documents to update. If not set, the default is to update all fields.

`.google.protobuf.FieldMask update_mask = 7;`

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### hasAlloyDbSource()
    
    
    public abstract boolean hasAlloyDbSource()

AlloyDB input source.

`.google.cloud.discoveryengine.v1alpha.AlloyDbSource alloy_db_source = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the alloyDbSource field is set.  
  
### hasBigquerySource()
    
    
    public abstract boolean hasBigquerySource()

BigQuery input source.

`.google.cloud.discoveryengine.v1alpha.BigQuerySource bigquery_source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigquerySource field is set.  
  
### hasBigtableSource()
    
    
    public abstract boolean hasBigtableSource()

Cloud Bigtable input source.

`.google.cloud.discoveryengine.v1alpha.BigtableSource bigtable_source = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigtableSource field is set.  
  
### hasCloudSqlSource()
    
    
    public abstract boolean hasCloudSqlSource()

Cloud SQL input source.

`.google.cloud.discoveryengine.v1alpha.CloudSqlSource cloud_sql_source = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudSqlSource field is set.  
  
### hasErrorConfig()
    
    
    public abstract boolean hasErrorConfig()

The desired location of errors incurred during the Import.

`.google.cloud.discoveryengine.v1alpha.ImportErrorConfig error_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the errorConfig field is set.  
  
### hasFhirStoreSource()
    
    
    public abstract boolean hasFhirStoreSource()

FhirStore input source.

`.google.cloud.discoveryengine.v1alpha.FhirStoreSource fhir_store_source = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fhirStoreSource field is set.  
  
### hasFirestoreSource()
    
    
    public abstract boolean hasFirestoreSource()

Firestore input source.

`.google.cloud.discoveryengine.v1alpha.FirestoreSource firestore_source = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the firestoreSource field is set.  
  
### hasGcsSource()
    
    
    public abstract boolean hasGcsSource()

Cloud Storage location for the input content.

`.google.cloud.discoveryengine.v1alpha.GcsSource gcs_source = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsSource field is set.  
  
### hasInlineSource()
    
    
    public abstract boolean hasInlineSource()

The Inline source for the input content for documents.

` .google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest.InlineSource inline_source = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the inlineSource field is set.  
  
### hasSpannerSource()
    
    
    public abstract boolean hasSpannerSource()

Spanner input source.

`.google.cloud.discoveryengine.v1alpha.SpannerSource spanner_source = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the spannerSource field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

Indicates which fields in the provided imported documents to update. If not set, the default is to update all fields.

`.google.protobuf.FieldMask update_mask = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
