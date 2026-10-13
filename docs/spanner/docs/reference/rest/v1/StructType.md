---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType/
title: StructType \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:22.226507+00:00
---

# StructType  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  StructType Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Field
    * JSON representation



`StructType` defines the fields of a `[STRUCT](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type#TypeCode.ENUM_VALUES.STRUCT)` type.

JSON representation  
---  
      
    
    {
      "fields": [
        {
          object ([Field](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType#Field))
        }
      ]
    }  
  
Fields  
---  
`fields[]` |  `object (`[Field](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType#Field)`)` The list of fields that make up this struct. Order is significant, because values of this struct type are represented as lists, where the order of field values matches the order of fields in the `[StructType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/StructType)`. In turn, the order of fields matches the order of columns in a read request, or the order of fields in the `SELECT` clause of a query.  
  
## Field

Message representing a single field of a struct.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": {
        object ([Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the field. For reads, this is the column name. For SQL queries, it is the column alias (e.g., `"Word"` in the query `"SELECT 'hello' AS Word"`), or the column name (e.g., `"ColName"` in the query `"SELECT ColName FROM Table"`). Some columns might have an empty name (e.g., `"SELECT UPPER(ColName)"`). Note that a query result can contain multiple fields with the same name.  
`type` |  `object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)`)` The type of the field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
