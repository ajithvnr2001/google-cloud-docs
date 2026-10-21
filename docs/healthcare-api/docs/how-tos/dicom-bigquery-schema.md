---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-bigquery-schema/
title: Understanding the BigQuery DICOM schema \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:01:46.662313+00:00
---

# Understanding the BigQuery DICOM schema  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-bigquery-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Understanding the BigQuery DICOM schema Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the schema of the BigQuery table that is created when [exporting DICOM metadata to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery).

## Terminology

To understand the schema and its components, familiarize yourself with the [DICOM terminology](https://dicom.nema.org/medical/dicom/current/output/html/part05.html#chapter_3). In particular, this page uses several terms found in [3.10 DICOM Data Structures and Encoding Definitions](https://dicom.nema.org/medical/dicom/current/output/html/part05.html#sect_3.10).

## Overview

The Cloud Healthcare API automatically generates the BigQuery schema using the data you are exporting and the DICOM dictionary. The schema only contains columns for DICOM data elements that exist in the metadata. The only exception is the Person Name VR.

When exporting DICOM metadata, the Cloud Healthcare API attempts to export all data elements in the metadata. For information on what happens if an issue arises, see Conflicting and mismatching types.

## Standard and private data elements

DICOM provides standard data elements that conform to a predefined specification. For a list of these data elements, see [Registry of DICOM Data Elements](https://dicom.nema.org/medical/dicom/current/output/html/part06.html#chapter_6).

In cases where you must communicate data that doesn't conform to the standard elements, you can use [private data elements](https://dicom.nema.org/medical/dicom/current/output/html/part05.html#sect_7.8).

## Standard data elements

The following behaviors apply to standard data elements. For private data element behavior, see Private data elements.

### Column names

Columns in the generated BigQuery schema are named according to the keyword of the data element. For example, if the DICOM metadata contains a data element whose keyword is InstanceCreationDate, then the generated schema has a corresponding column named InstanceCreationDate.

### Standard DICOM data element behavior

The following table shows a list of Value Representations (VRs) and their abbreviations. For any data element exported to BigQuery that contains one of these VRs, the data element uses the BigQuery data type found under "Data type":

VR | Data type  
---|---  
  
  * Application Entity (AE)
  * Age String (AS)
  * Code String (CS)
  * Long String (LO)
  * Long Text (LT)
  * Short String (SH)
  * Short Text (ST)
  * Unlimited Characters (UC)
  * Unique Identifier (UI/UID)
  * Universal Resource Identifier (UR) or Universal Resource Locator (URI/URL)
  * Unlimited Text (UT)

| [String](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type)  
Date (DA) | [Date](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#date_type)  
Time (TM) | [Time](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#time_type)  
Date Time (DT) | [Timestamp](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type)  
  
  * Decimal String (DS)
  * Integer String (IS)

| String  
Person Name (PN) | [Struct (Record)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type)  
  
  * Floating Point Single (FL)
  * Floating Point Double (FD)

| [Floating point](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#floating_point_type)  
  
  * Attribute Tag (AT)
  * Signed Long (SL)
  * Signed Short (SS)
  * Unsigned Long (UL)
  * Unsigned Short (US)

| [Integer](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#integer_type)  
Sequence of Items (SQ) | Struct (Record)  
  
### Nullable and repeated modes

Depending on the Value Multiplicity (VM) value of a data element, its BigQuery column has one of two [modes](https://docs.cloud.google.com/bigquery/docs/schemas#modes): `NULLABLE` or `REPEATED`.

If a data element has a VM value of 1, which indicates that the data element is unique, the data element uses the `NULLABLE` mode. For any other VM value, the data element uses the `REPEATED` mode.

For example, as shown in the [Registry of DICOM Data Elements](https://dicom.nema.org/medical/dicom/current/output/html/part06.html#chapter_6), the SOPInstanceUID keyword has a VM value of 1. As a result, when it is exported to BigQuery, its mode is `NULLABLE`, and its representation in the table looks like the following (when represented as JSON):
    
    
    "SOPInstanceUID": "0.0.000.000000.0.000.0000.0000000.0000.0000000000.000",
    

Conversely, the ImageType keyword has a VM value of 2-n. As a result, when it is exported to BigQuery, its mode is `REPEATED`, and its representation in the table looks like the following (when represented as JSON):
    
    
    "ImageType": [
      "ORIGINAL",
      "PRIMARY",
      "OTHER",
      "..."
    ],
    

### Excluded VRs

Binary and long-form data is not exported to the generated BigQuery table, so data elements containing the following VRs are not exported. Instead, the following VRs are included in a separate column (called `DroppedTags.TagName`) in the destination BigQuery table.

  * Other Double (OD)
  * Other Float (OF)
  * Other Long (OL)
  * Other Byte (OB)
  * Other Word (OW)
  * Unknown (UN)
  * Sequence (SQ) tags containing more than approximately 1 MiB of data
  * Attribute (AT), Floating Point Double (FD), Floating Point Single (FL), Unsigned Long (UL), or Unsigned Short (US), if the Value Multiplicity (VM) is greater than 512. 
    * For legacy reasons, tags of instances already ingested into the Cloud Healthcare API might be included in the `DroppedTags.TagName` column if the Value Multiplicity is greater than 64.



### Person Name VR

Each column in the BigQuery schema with a Person Name (PN) VR always contains three subcolumns, regardless of whether the subcolumns contain any data. The three subcolumns are:

  * Alphabetic
  * Ideographic
  * Phonetic



Each of the three subcolumns has its own five subcolumns:

  * FamilyName
  * GivenName
  * MiddleName
  * NamePrefix
  * NameSuffix



For example, consider the public tag "OperatorsName (0008,1070)," which has a VR of Person Name (PN). Suppose that the value of OperatorsName is "Darcy Smith." The schema will contain an OperatorsName column containing the subcolumns listed previously, but only Alphabetic.FamilyName (Smith) and Alphabetic.GivenName (Darcy) will contain values.

## Private data elements

Some clinical implementations might require you to store custom data that does not fit within the structure of public data elements. As an alternative, you can use private data elements.

Private data elements with a VR of SQ (Sequence of Items) have the same behavior as standard data elements. Private data elements with a VR of SQ are called _private data sequences_.

Private data elements that do not have a VR of SQ are nested under a column called `OtherElements` and are converted to strings. These private data elements are called _non-sequence private data_. To query non-sequence private data elements, your query must search within the `OtherElements` column of the element.

The `OtherElements` column contains two subcolumns, "Data" and "Tag." The Data column is the string representation of the private data element's value. It is always type `REPEATED`. The Tag column uses the format "Tag_HEX" where HEX is a hex string of the tag number.

## `LastUpdated` and `Type` columns

The `LastUpdated` and `Type` columns are added to the BigQuery table created when you export DICOM metadata. These columns are not standard or private data elements, and they do not correspond to the Registry of DICOM Data Elements.

The behavior of these columns is as follows:

  * The `LastUpdated` column contains a [timestamp](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type) value that shows when the DICOM instance was inserted into or deleted from the DICOM store.
  * The `Type` column contains a [string](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type) that shows what type of operation occurred. The possible values are `CREATE` or `DELETE`.



## Conflicting and mismatching types

If a type conflict occurs, such as when a public tag is used with an incorrect type, the public tag is treated as though it were a private tag. The value of the data element is nested under a column called `OtherElements` and the value is converted to a string.

For example, say that the DICOM metadata contains a tag with:

  * A tag number "(4010,1017)"
  * A VR of SL (Signed Long)
  * A value of 32



(4010,1017) is same tag number as "Mass," which is a public tag name in the DICOM specification that has a VR of FL. The export operation expects a data element with the tag number of "(4010,1017)" to be the "Mass" public tag name with a VR of FL. Therefore, the export operation expects to convert the data element's value to a float (as shown in the table in Standard DICOM data element behavior

A type conflict occurs because any tags with a VR of SL use the integer data type. The tag is therefore converted to a private tag and added to the `OtherElements` column.

If a non-sequence public tag name is used for sequence data, a type mismatch occurs. As a result, the sequence is treated as though it were a private data element. Instead of using the public tag name as the column name in the BigQuery schema, the public tag name's hex number is used. The hex number is of type string.

## Examples: Querying public and private data elements

Consider the following snippet of a schema represented as JSON. The schema was created after exporting DICOM data to BigQuery.
    
    
    [
      ...
      {
        "name": "SOPInstanceUID",
        "type": "STRING"
      },
      {
        "fields": [
          {
            "fields": [
              {
                "mode": "REQUIRED",
                "name": "Tag",
                "type": "STRING"
              },
              {
                "mode": "REPEATED",
                "name": "Data",
                "type": "STRING"
              }
            ],
            "mode": "REPEATED",
            "name": "OtherElements",
            "type": "RECORD"
          }
        ],
        "mode": "REPEATED",
        "name": "Tag_12345678",
        "type": "RECORD"
      }
      ...
    ]
    

The following sample shows how to query for the `SOPInstanceUID` public data element. To access the value of the column, run the following query:
    
    
    #standardSQL
    SELECT
      SOPInstanceUID
    FROM
      `PROJECT_ID.DATASET_ID.TABLE_ID`

Running the query returns an output similar to the following:
    
    
    [
      ...
      {
        "SOPInstanceUID": "0.0.000.000000.0.000.0000.0000000.0000.0000000000.000"
      },
      ...
    ]

The following sample shows how to query for non-sequence private data. Run the following query against the `OtherElements` column which is inside the `Tag_12345678` column. Note the use of the [`UNNEST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#unnest) operator, which is required because you are querying a `RECORD`.
    
    
    #standardSQL
    SELECT
      Tag_12345678.OtherElements AS OtherElements
    FROM
      `PROJECT_ID.DATASET_ID.TABLE_ID`,
      UNNEST(Tag_12345678) AS Tag_12345678

Running the query returns an output similar to the following, depending on the amount and type of data in the `Tag_12345678.OtherElements` column:
    
    
    [
      {
        "OtherElements": [
          {
            "Tag": "Tag_12345678",
            "Data": [
              "DATA"
            ]
          }
        ]
      },
      {
        "OtherElements": [
          {
            "Tag": "Tag_12345678",
            "Data": [
              "DATA"
            ]
          }
        ]
      },
      {
        "OtherElements": [
          {
            "Tag": "Tag_12345678",
            "Data": [
              "DATA"
            ]
          }
        ]
      }
    ]

## JSON Schema

You can export DICOM instance metadata into a BigQuery table with a simpler schema where the full instance metadata is stored as a single JSON column. This can be useful when you prefer to work with the raw JSON structure of the DICOM metadata within BigQuery. It is also useful when the number of unique tags across all DICOM instances exceeds the maximum number of columns allowed in a BigQuery table.

To enable the JSON schema, set the `schema_json` field in the `BigQueryDestination`. For more details on configuring the schema, see [BigQueryDestination](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#BigQueryDestination).

When the JSON schema is enabled, the BigQuery table will have the following columns:

Field Name | Type | Description  
---|---|---  
`StudyInstanceUID` | STRING | DICOM Tag (0020,000D).  
`SeriesInstanceUID` | STRING | DICOM Tag (0020,000E).  
`SOPInstanceUID` | STRING | DICOM Tag (0008,0018).  
`SourceDicomStore` | STRING | The name of the source DICOM store. This field is only included if the `includeSourceStore` option is set to true in the export configuration.  
`Type` | STRING | Indicates the type of operation that triggered the export (e.g., `CREATE`, `DELETE`).  
`LastUpdated` | TIMESTAMP | Timestamp of the last update to the instance in the DICOM store.  
`Metadata` | JSON | All DICOM tags for the instance, stored in a single JSON object.  
`DroppedTags` | REPEATED STRING | List of tags that were dropped during the conversion, typically binary or very large tags.  
`StorageClass` | STRING | The storage class of the instance (e.g., STANDARD, NEARLINE).  
`BlobStorageSize` | INTEGER | Size of the blob storage in bytes.  
`StructuredStorageSize` | INTEGER | Size of the structured storage in bytes.  
  
### Example: Querying the Metadata JSON column

Here is an example of how to query a specific DICOM tag from the `Metadata` column following BigQuery's [JSON data support](https://docs.cloud.google.com/bigquery/docs/json-data). This query selects the `PatientID` and `PatientAge` tags:
    
    
    #standardSQL
    SELECT
      Metadata.PatientID AS patient_id,
      Metadata.PatientAge AS patient_age
    FROM
      `PROJECT_ID.DATASET_ID.TABLE_ID`;

Running the query returns an output similar to the following:
    
    
    /*-------------+---------------*
    | patient_id   | patient_age   |
    +--------------+---------------+
    | "John-Doe"   | "042Y"        |
    *--------------+---------------*/
    

You can adapt query to extract other DICOM tags from the `Metadata` JSON column as needed.

## What's next

Learn more about [BigQuery standard SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql) operations and view examples.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
