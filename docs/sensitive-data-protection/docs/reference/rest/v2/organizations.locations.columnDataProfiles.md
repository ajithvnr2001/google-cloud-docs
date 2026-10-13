---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles
title: REST Resource: organizations.locations.columnDataProfiles \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:22.374264+00:00
---

# REST Resource: organizations.locations.columnDataProfiles  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.columnDataProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ColumnDataProfile
    * JSON representation
    * State
    * NullPercentageLevel
    * UniquenessScoreLevel
    * ColumnDataType
    * ColumnPolicyState
  * Methods



## Resource: ColumnDataProfile

The profile for a scanned column within a table.

JSON representation  
---  
      
    
    {
      "name": string,
      "profileStatus": {
        object ([ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ProfileStatus))
      },
      "state": enum ([State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.State)),
      "profileLastGenerated": string,
      "tableDataProfile": string,
      "tableFullResource": string,
      "datasetProjectId": string,
      "datasetLocation": string,
      "datasetId": string,
      "tableId": string,
      "column": string,
      "sensitivityScore": {
        object ([SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore))
      },
      "dataRiskLevel": {
        object ([DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel))
      },
      "columnInfoType": {
        object ([InfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoTypeSummary))
      },
      "otherMatches": [
        {
          object ([OtherInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/OtherInfoTypeSummary))
        }
      ],
      "estimatedNullPercentage": enum ([NullPercentageLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.NullPercentageLevel)),
      "estimatedUniquenessScore": enum ([UniquenessScoreLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.UniquenessScoreLevel)),
      "freeTextScore": number,
      "columnType": enum ([ColumnDataType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.ColumnDataType)),
      "policyState": enum ([ColumnPolicyState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.ColumnPolicyState))
    }  
  
Fields  
---  
`name` |  `string` The name of the profile.  
`profileStatus` |  `object (`[ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ProfileStatus)`)` Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.State)`)` State of a profile.  
`profileLastGenerated` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last time the profile was generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tableDataProfile` |  `string` The resource name of the table data profile.  
`tableFullResource` |  `string` The resource name of the resource this column is within.  
`datasetProjectId` |  `string` The Google Cloud project ID that owns the profiled resource.  
`datasetLocation` |  `string` If supported, the location where the dataset's data is stored. See <https://docs.cloud.google.com/bigquery/docs/locations> for supported BigQuery locations.  
`datasetId` |  `string` The BigQuery dataset ID, if the resource profiled is a BigQuery table.  
`tableId` |  `string` The table ID.  
`column` |  `string` The name of the column.  
`sensitivityScore` |  `object (`[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore)`)` The sensitivity of this column.  
`dataRiskLevel` |  `object (`[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel)`)` The data risk level for this column.  
`columnInfoType` |  `object (`[InfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoTypeSummary)`)` If it's been determined this column can be identified as a single type, this will be set. Otherwise the column either has unidentifiable content or mixed types.  
`otherMatches[]` |  `object (`[OtherInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/OtherInfoTypeSummary)`)` Other types found within this column. List will be unordered.  
`estimatedNullPercentage` |  `enum (`[NullPercentageLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.NullPercentageLevel)`)` Approximate percentage of entries being null in the column.  
`estimatedUniquenessScore` |  `enum (`[UniquenessScoreLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.UniquenessScoreLevel)`)` Approximate uniqueness of the column.  
`freeTextScore` |  `number` The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1.  
`columnType` |  `enum (`[ColumnDataType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.ColumnDataType)`)` The data type of a given column.  
`policyState` |  `enum (`[ColumnPolicyState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles#ColumnDataProfile.ColumnPolicyState)`)` Indicates if a policy tag has been applied to the column.  
  
### State

Possible states of a profile. New items may be added.

Enums  
---  
`STATE_UNSPECIFIED` | Unused.  
`RUNNING` | The profile is currently running. Once a profile has finished it will transition to DONE.  
`DONE` | The profile is no longer generating. If profileStatus.status.code is 0, the profile succeeded, otherwise, it failed.  
  
### NullPercentageLevel

Bucketized nullness percentage levels. A higher level means a higher percentage of the column is null.

Enums  
---  
`NULL_PERCENTAGE_LEVEL_UNSPECIFIED` | Unused.  
`NULL_PERCENTAGE_VERY_LOW` | Very few null entries.  
`NULL_PERCENTAGE_LOW` | Some null entries.  
`NULL_PERCENTAGE_MEDIUM` | A few null entries.  
`NULL_PERCENTAGE_HIGH` | A lot of null entries.  
  
### UniquenessScoreLevel

Bucketized uniqueness score levels. A higher uniqueness score is a strong signal that the column may contain a unique identifier like user id. A low value indicates that the column contains few unique values like booleans or other classifiers.

Enums  
---  
`UNIQUENESS_SCORE_LEVEL_UNSPECIFIED` | Some columns do not have estimated uniqueness. Possible reasons include having too few values.  
`UNIQUENESS_SCORE_LOW` | Low uniqueness, possibly a boolean, enum or similiarly typed column.  
`UNIQUENESS_SCORE_MEDIUM` | Medium uniqueness.  
`UNIQUENESS_SCORE_HIGH` | High uniqueness, possibly a column of free text or unique identifiers.  
  
### ColumnDataType

Data types of the data in a column. Types may be added over time.

Enums  
---  
`COLUMN_DATA_TYPE_UNSPECIFIED` | Invalid type.  
`TYPE_INT64` | Encoded as a string in decimal format.  
`TYPE_BOOL` | Encoded as a boolean "false" or "true".  
`TYPE_FLOAT64` | Encoded as a number, or string "NaN", "Infinity" or "-Infinity".  
`TYPE_STRING` | Encoded as a string value.  
`TYPE_BYTES` | Encoded as a base64 string per RFC 4648, section 4.  
`TYPE_TIMESTAMP` | Encoded as an RFC 3339 timestamp with mandatory "Z" time zone string: 1985-04-12T23:20:50.52Z  
`TYPE_DATE` | Encoded as RFC 3339 full-date format string: 1985-04-12  
`TYPE_TIME` | Encoded as RFC 3339 partial-time format string: 23:20:50.52  
`TYPE_DATETIME` | Encoded as RFC 3339 full-date "T" partial-time: 1985-04-12T23:20:50.52  
`TYPE_GEOGRAPHY` | Encoded as WKT  
`TYPE_NUMERIC` | Encoded as a decimal string.  
`TYPE_RECORD` | Container of ordered fields, each with a type and field name.  
`TYPE_BIGNUMERIC` | Decimal type.  
`TYPE_JSON` | Json type.  
`TYPE_INTERVAL` | Interval type.  
`TYPE_RANGE_DATE` | `Range<Date>` type.  
`TYPE_RANGE_DATETIME` | `Range<Datetime>` type.  
`TYPE_RANGE_TIMESTAMP` | `Range<Timestamp>` type.  
  
### ColumnPolicyState

The possible policy states for a column.

Enums  
---  
`COLUMN_POLICY_STATE_UNSPECIFIED` | No policy tags.  
`COLUMN_POLICY_TAGGED` | Column has policy tag applied.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles/get)`

|  Gets a column data profile.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles/list)`

|  Lists column data profiles for an organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
