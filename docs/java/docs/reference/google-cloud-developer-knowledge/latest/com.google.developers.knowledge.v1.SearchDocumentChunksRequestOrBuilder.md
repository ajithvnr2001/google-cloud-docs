---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksRequestOrBuilder
title: Interface SearchDocumentChunksRequestOrBuilder (0.3.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:12.343196+00:00
---

# Interface SearchDocumentChunksRequestOrBuilder (0.3.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-developer-knowledge/latest/com.google.developers.knowledge.v1.SearchDocumentChunksRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchDocumentChunksRequestOrBuilder (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.2.0  0.1.0 
    
    
    public interface SearchDocumentChunksRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getFilter()
    
    
    public abstract String getFilter()

Optional. Applies a strict filter to the search results. The expression supports a subset of the syntax described at <https://google.aip.dev/160>.

While `SearchDocumentChunks` returns DocumentChunks, the filter is applied to `DocumentChunk.document` fields.

Supported fields for filtering:

  * `data_source` (STRING): The source of the document, e.g. `docs.cloud.google.com`. See <https://developers.google.com/knowledge/reference/corpus-reference> for the complete list of data sources in the corpus.
  * `update_time` (TIMESTAMP): The timestamp of when the document was last meaningfully updated. A meaningful update is one that changes document's markdown content or metadata.
  * `uri` (STRING): The document URI, e.g. `<https://docs.cloud.google.com/bigquery/docs/tables>`.

STRING fields support `=` (equals) and `!=` (not equals) operators for **exact match** on the whole string. Partial match, prefix match, and regexp match are not supported.

TIMESTAMP fields support `=`, `<`, `<=`, `>`, and `>=` operators. Timestamps must be in RFC-3339 format, e.g., `"2025-01-01T00:00:00Z"`.

Note: Field names must be in `snake_case` (e.g., `data_source`). Values on the right-hand side of filtering expressions must be string literals enclosed in double quotes (e.g., `"docs.cloud.google.com"`).

You can combine expressions using `AND`, `OR`, and `NOT` (or `-`) logical operators. `OR` has higher precedence than `AND`. Use parentheses for explicit precedence grouping.

Examples:

  * `data_source = "docs.cloud.google.com" OR data_source = "firebase.google.com"`

  * `data_source != "firebase.google.com"`
  * `update_time < "2024-01-01T00:00:00Z"`
  * `update_time >= "2025-01-22T00:00:00Z" AND (data_source = "developer.chrome.com" OR data_source = "web.dev")`
  * `uri = "<https://docs.cloud.google.com/release-notes>"`

The `filter` string must not exceed 500 characters; values longer than 500 characters will result in an `INVALID_ARGUMENT` error.




`string filter = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filter.  
  
### getFilterBytes()
    
    
    public abstract ByteString getFilterBytes()

Optional. Applies a strict filter to the search results. The expression supports a subset of the syntax described at <https://google.aip.dev/160>.

While `SearchDocumentChunks` returns DocumentChunks, the filter is applied to `DocumentChunk.document` fields.

Supported fields for filtering:

  * `data_source` (STRING): The source of the document, e.g. `docs.cloud.google.com`. See <https://developers.google.com/knowledge/reference/corpus-reference> for the complete list of data sources in the corpus.
  * `update_time` (TIMESTAMP): The timestamp of when the document was last meaningfully updated. A meaningful update is one that changes document's markdown content or metadata.
  * `uri` (STRING): The document URI, e.g. `<https://docs.cloud.google.com/bigquery/docs/tables>`.

STRING fields support `=` (equals) and `!=` (not equals) operators for **exact match** on the whole string. Partial match, prefix match, and regexp match are not supported.

TIMESTAMP fields support `=`, `<`, `<=`, `>`, and `>=` operators. Timestamps must be in RFC-3339 format, e.g., `"2025-01-01T00:00:00Z"`.

Note: Field names must be in `snake_case` (e.g., `data_source`). Values on the right-hand side of filtering expressions must be string literals enclosed in double quotes (e.g., `"docs.cloud.google.com"`).

You can combine expressions using `AND`, `OR`, and `NOT` (or `-`) logical operators. `OR` has higher precedence than `AND`. Use parentheses for explicit precedence grouping.

Examples:

  * `data_source = "docs.cloud.google.com" OR data_source = "firebase.google.com"`

  * `data_source != "firebase.google.com"`
  * `update_time < "2024-01-01T00:00:00Z"`
  * `update_time >= "2025-01-22T00:00:00Z" AND (data_source = "developer.chrome.com" OR data_source = "web.dev")`
  * `uri = "<https://docs.cloud.google.com/release-notes>"`

The `filter` string must not exceed 500 characters; values longer than 500 characters will result in an `INVALID_ARGUMENT` error.




`string filter = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filter.  
  
### getPageSize()
    
    
    public abstract int getPageSize()

Optional. Specifies the maximum number of results to return. The service may return fewer than this value.

If unspecified, at most 5 results will be returned.

The maximum value is 100; values above 100 will be coerced to 100.

`int32 page_size = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

Optional. Contains a page token, received from a previous `SearchDocumentChunks` call. Provide this to retrieve the subsequent page.

`string page_token = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

Optional. Contains a page token, received from a previous `SearchDocumentChunks` call. Provide this to retrieve the subsequent page.

`string page_token = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getQuery()
    
    
    public abstract String getQuery()

Required. Provides the raw query string provided by the user, such as "How to create a Cloud Storage bucket?".

`string query = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The query.  
  
### getQueryBytes()
    
    
    public abstract ByteString getQueryBytes()

Required. Provides the raw query string provided by the user, such as "How to create a Cloud Storage bucket?".

`string query = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
