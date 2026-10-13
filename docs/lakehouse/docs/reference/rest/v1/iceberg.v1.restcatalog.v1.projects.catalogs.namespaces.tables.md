---
url: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables
title: REST Resource: iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:39.952585+00:00
---

# REST Resource: iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



#  REST Resource: iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HttpBody
    * JSON representation
  * Methods



## Resource: HttpBody

Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page.

This message can be used both in streaming and non-streaming API methods in the request as well as the response.

It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body.

Example:
    
    
    message GetResourceRequest {
      // A unique request id.
      string request_id = 1;
    
      // The raw HTTP body is bound to this field.
      google.api.HttpBody httpBody = 2;
    
    }
    
    service ResourceService {
      rpc GetResource(GetResourceRequest)
        returns (google.api.HttpBody);
      rpc UpdateResource(google.api.HttpBody)
        returns (google.protobuf.Empty);
    
    }
    

Example with streaming methods:
    
    
    service CaldavService {
      rpc GetCalendar(stream google.api.HttpBody)
        returns (stream google.api.HttpBody);
      rpc UpdateCalendar(stream google.api.HttpBody)
        returns (stream google.api.HttpBody);
    
    }
    

Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.

JSON representation  
---  
      
    
    {
      "contentType": string,
      "data": string,
      "extensions": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`contentType` |  `string` The HTTP Content-Type header value specifying the content type of the body.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The HTTP request/response body as raw binary.A base64-encoded string.  
`extensions[]` |  `object` Application specific response metadata. Must be set in the first response for streaming APIs.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/create)`

|  Creates a table in the namespace.  
  
### `[credentials](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/credentials)`

|  Loads credentials for a table in the namespace.  
  
### `[delete](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/delete)`

|  Deletes a table in the namespace.  
  
### `[get](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/get)`

|  Gets a table in the namespace.  
  
### `[head](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/head)`

|  Returns 204 if the table exists, 404 otherwise.  
  
### `[list](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/list)`

|  Lists table identifiers (not _tables_) in the namespace.  
  
### `[metrics](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/metrics)`

|  Reports a metrics report for a table.  
  
### `[updateIcebergTable](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/updateIcebergTable)`

|  This is CommitTable Iceberg API, which maps to `UpdateIcebergTable` in the Google API nomenclature.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
