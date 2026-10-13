---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource/
title: BigtableSource \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:17.583747+00:00
---

# BigtableSource  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  BigtableSource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * BigtableOptions
    * JSON representation
  * BigtableColumnFamily
    * JSON representation
  * Encoding
  * Type
  * BigtableColumn
    * JSON representation



The Cloud Bigtable source for importing data.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "instanceId": string,
      "tableId": string,
      "bigtableOptions": {
        object ([BigtableOptions](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#BigtableOptions))
      }
    }  
  
Fields  
---  
`projectId` |  `string` The project ID that contains the Bigtable source. Has a length limit of 128 characters. If not specified, inherits the project ID from the parent request.  
`instanceId` |  `string` Required. The instance ID of the Cloud Bigtable that needs to be imported.  
`tableId` |  `string` Required. The table ID of the Cloud Bigtable that needs to be imported.  
`bigtableOptions` |  `object (`[BigtableOptions](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#BigtableOptions)`)` Required. Bigtable options that contains information needed when parsing data into typed structures. For example, column type annotations.  
  
## BigtableOptions

The Bigtable Options object that contains information to support the import.

JSON representation  
---  
      
    
    {
      "keyFieldName": string,
      "families": {
        string: {
          object ([BigtableColumnFamily](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#BigtableColumnFamily))
        },
        ...
      }
    }  
  
Fields  
---  
`keyFieldName` |  `string` The field name used for saving row key value in the document. The name has to match the pattern `[a-zA-Z0-9][a-zA-Z0-9-_]*`.  
`families` |  `map (key: string, value: object (`[BigtableColumnFamily](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#BigtableColumnFamily)`))` The mapping from family names to an object that contains column families level information for the given column family. If a family is not present in this map it will be ignored.  
  
## BigtableColumnFamily

The column family of the Bigtable.

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "encoding": enum ([Encoding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#Encoding)),
      "type": enum ([Type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#Type)),
      "columns": [
        {
          object ([BigtableColumn](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#BigtableColumn))
        }
      ]
    }  
  
Fields  
---  
`fieldName` |  `string` The field name to use for this column family in the document. The name has to match the pattern `[a-zA-Z0-9][a-zA-Z0-9-_]*`. If not set, it is parsed from the family name with best effort. However, due to different naming patterns, field name collisions could happen, where parsing behavior is undefined.  
`encoding` |  `enum (`[Encoding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#Encoding)`)` The encoding mode of the values when the type is not STRING. Acceptable encoding values are:

  * `TEXT`: indicates values are alphanumeric text strings.
  * `BINARY`: indicates values are encoded using `HBase Bytes.toBytes` family of functions. This can be overridden for a specific column by listing that column in `columns` and specifying an encoding for it.

  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#Type)`)` The type of values in this column family. The values are expected to be encoded using `HBase Bytes.toBytes` function when the encoding value is set to `BINARY`.  
`columns[]` |  `object (`[BigtableColumn](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#BigtableColumn)`)` The list of objects that contains column level information for each column. If a column is not present in this list it will be ignored.  
  
## Encoding

The encoding mode of a Bigtable column or column family.

Enums  
---  
`ENCODING_UNSPECIFIED` | The encoding is unspecified.  
`TEXT` | Text encoding.  
`BINARY` | Binary encoding.  
  
## Type

The type of values in a Bigtable column or column family. The values are expected to be encoded using [HBase Bytes.toBytes](https://hbase.apache.org/1.4/apidocs/org/apache/hadoop/hbase/util/Bytes.html) function when the encoding value is set to `BINARY`.

Enums  
---  
`TYPE_UNSPECIFIED` | The type is unspecified.  
`STRING` | String type.  
`NUMBER` | Numerical type.  
`INTEGER` | Integer type.  
`VAR_INTEGER` | Variable length integer type.  
`BIG_NUMERIC` | BigDecimal type.  
`BOOLEAN` | Boolean type.  
`JSON` | JSON type.  
  
## BigtableColumn

The column of the Bigtable.

JSON representation  
---  
      
    
    {
      "qualifier": string,
      "fieldName": string,
      "encoding": enum ([Encoding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#Encoding)),
      "type": enum ([Type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#Type))
    }  
  
Fields  
---  
`qualifier` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Qualifier of the column. If it cannot be decoded with utf-8, use a base-64 encoded string instead.A base64-encoded string.  
`fieldName` |  `string` The field name to use for this column in the document. The name has to match the pattern `[a-zA-Z0-9][a-zA-Z0-9-_]*`. If not set, it is parsed from the qualifier bytes with best effort. However, due to different naming patterns, field name collisions could happen, where parsing behavior is undefined.  
`encoding` |  `enum (`[Encoding](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#Encoding)`)` The encoding mode of the values when the type is not `STRING`. Acceptable encoding values are:

  * `TEXT`: indicates values are alphanumeric text strings.
  * `BINARY`: indicates values are encoded using `HBase Bytes.toBytes` family of functions. This can be overridden for a specific column by listing that column in `columns` and specifying an encoding for it.

  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/BigtableSource#Type)`)` The type of values in this column family. The values are expected to be encoded using `HBase Bytes.toBytes` function when the encoding value is set to `BINARY`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
