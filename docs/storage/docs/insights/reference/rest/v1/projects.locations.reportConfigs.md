---
url: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs
title: REST Resource: projects.locations.reportConfigs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:37.729130+00:00
---

# REST Resource: projects.locations.reportConfigs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  REST Resource: projects.locations.reportConfigs Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: ReportConfig

Message describing the `ReportConfig` object. `ReportConfig` is the configuration used to generate inventory reports. For information about how to set various fields, see [Create an inventory report configuration](https://cloud.google.com/storage/docs/insights/using-inventory-reports#create-report-config).

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "frequencyOptions": {
        object ([FrequencyOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#FrequencyOptions))
      },
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
    
      // Union field report_format can be only one of the following:
      "csvOptions": {
        object ([CSVOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#CSVOptions))
      },
      "parquetOptions": {
        object ([ParquetOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#ParquetOptions))
      }
      // End of list of possible types for union field report_format.
    
      // Union field report_kind can be only one of the following:
      "objectMetadataReportOptions": {
        object ([ObjectMetadataReportOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#ObjectMetadataReportOptions))
      }
      // End of list of possible types for union field report_kind.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of resource.Format: `projects/{projectId}/locations/{location}/reportConfigs/{report-config-id}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The UTC time at which the inventory report configuration was created. This is auto-populated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The UTC time at which the inventory report configuration was updated. This is auto-populated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`frequencyOptions` |  `object (`[FrequencyOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#FrequencyOptions)`)` The frequency of the inventory report generation.  
`labels` |  `map (key: string, value: string)` Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` User provided display name that can be empty and limited to 256 characters that is editable..  
Union field `report_format`. Format in which the inventory report is generated. `report_format` can be only one of the following:  
`csvOptions` |  `object (`[CSVOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#CSVOptions)`)` Options for CSV formatted reports.  
`parquetOptions` |  `object (`[ParquetOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#ParquetOptions)`)` Options for Parquet formatted reports.  
Union field `report_kind`. Configuration options for inventory report contents. `report_kind` can be only one of the following:  
`objectMetadataReportOptions` |  `object (`[ObjectMetadataReportOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#ObjectMetadataReportOptions)`)` Options for including object metadata in an inventory report.  
  
## FrequencyOptions

`FrequencyOptions` resource

Frequency configuration for inventory report generation.

JSON representation  
---  
      
    
    {
      "frequency": enum ([Frequency](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#Frequency)),
      "startDate": {
        object ([Date](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#Date))
      },
      "endDate": {
        object ([Date](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#Date))
      }
    }  
  
Fields  
---  
`frequency` |  `enum (`[Frequency](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#Frequency)`)` Frequency of inventory report generation.  
`startDate` |  `object (`[Date](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#Date)`)` The UTC date to start generating inventory reports. For example,`{"day": 15, "month": 8, "year": 2022}`.  
`endDate` |  `object (`[Date](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#Date)`)` The UTC date to stop generating inventory reports. For example,`{"day": 15, "month": 8, "year": 2022}`.  
  
## Frequency

The frequency at which the inventory reports are generated. Values are `FREQUENCY_UNSPECIFIED`, `DAILY` or `WEEKLY`.

Enums  
---  
`FREQUENCY_UNSPECIFIED` | Unspecified.  
`DAILY` | Inventory report is generated daily.  
`WEEKLY` | Inventory report is generated weekly.  
  
## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * `google.type.TimeOfDay`
  * `[google.type.DateTime](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails#DateTime)`
  * `[google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
## CSVOptions

Options to configure inventory reports in CSV format.

JSON representation  
---  
      
    
    {
      "recordSeparator": string,
      "delimiter": string,
      "headerRequired": boolean
    }  
  
Fields  
---  
`recordSeparator` |  `string` Record separator characters in CSV.  
`delimiter` |  `string` Delimiter characters in CSV.  
`headerRequired` |  `boolean` If set, includes a header row in the CSV report.  
  
## ParquetOptions

This type has no fields.

Options to configure inventory reports in Parquet format.

## ObjectMetadataReportOptions

Options for including metadata in an inventory report.

JSON representation  
---  
      
    
    {
      "metadataFields": [
        string
      ],
    
      // Union field filter can be only one of the following:
      "storageFilters": {
        object ([CloudStorageFilters](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#CloudStorageFilters))
      }
      // End of list of possible types for union field filter.
    
      // Union field destination_options can be only one of the following:
      "storageDestinationOptions": {
        object ([CloudStorageDestinationOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#CloudStorageDestinationOptions))
      }
      // End of list of possible types for union field destination_options.
    }  
  
Fields  
---  
`metadataFields[]` |  `string` The metadata fields included in an inventory report.  
Union field `filter`. Filters buckets to generate inventory reports for Cloud Storage. `filter` can be only one of the following:  
`storageFilters` |  `object (`[CloudStorageFilters](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#CloudStorageFilters)`)` Filters buckets to generate inventory reports for Cloud Storage.  
Union field `destination_options`. Options to store reports in Cloud Storage. `destination_options` can be only one of the following:  
`storageDestinationOptions` |  `object (`[CloudStorageDestinationOptions](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#CloudStorageDestinationOptions)`)` Options to store reports in Cloud Storage.  
  
## CloudStorageFilters

Filters buckets to generate inventory reports for Cloud Storage.

JSON representation  
---  
      
    
    {
      "bucket": string
    }  
  
Fields  
---  
`bucket` |  `string` Optional. Bucket for which the inventory report is generated.  
  
## CloudStorageDestinationOptions

Options to store inventory reports in Cloud Storage.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "destinationPath": string
    }  
  
Fields  
---  
`bucket` |  `string` Optional. The destination bucket for the inventory reports.  
`destinationPath` |  `string` The destination path within the bucket where the inventory reports are stored.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/create)`

|  Creates a new inventory report configuration in a given project for a given location.  
  
### `[delete](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/delete)`

|  Deletes an existing inventory report configuration in a given project for a given location.  
  
### `[get](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/get)`

|  Gets the inventory report configuration in a given project for a given location.  
  
### `[list](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/list)`

|  Lists the inventory report configurations in a given project for a given location.  
  
### `[patch](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/patch)`

|  Updates an existing inventory report configuration in a given project for a given location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
