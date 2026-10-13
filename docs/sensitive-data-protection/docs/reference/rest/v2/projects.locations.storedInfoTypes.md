---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes
title: REST Resource: projects.locations.storedInfoTypes \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:39.759801+00:00
---

# REST Resource: projects.locations.storedInfoTypes  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.locations.storedInfoTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: StoredInfoType
    * JSON representation
    * StoredInfoTypeVersion
      * JSON representation
    * StoredInfoTypeConfig
      * JSON representation
    * LargeCustomDictionaryConfig
      * JSON representation
    * CloudStorageFileSet
      * JSON representation
    * BigQueryField
      * JSON representation
    * StoredInfoTypeState
    * StoredInfoTypeStats
      * JSON representation
    * LargeCustomDictionaryStats
      * JSON representation
  * Methods



## Resource: StoredInfoType

StoredInfoType resource message that contains information about the current version and any pending updates.

JSON representation  
---  
      
    
    {
      "name": string,
      "currentVersion": {
        object ([StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeVersion))
      },
      "pendingVersions": [
        {
          object ([StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeVersion))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name.  
`currentVersion` |  `object (`[StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeVersion)`)` Current version of the stored info type.  
`pendingVersions[]` |  `object (`[StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeVersion)`)` Pending versions of the stored info type. Empty if no versions are pending.  
  
### StoredInfoTypeVersion

Version of a StoredInfoType, including the configuration used to build it, create timestamp, and current state.

JSON representation  
---  
      
    
    {
      "config": {
        object ([StoredInfoTypeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeConfig))
      },
      "createTime": string,
      "state": enum ([StoredInfoTypeState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeState)),
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ],
      "stats": {
        object ([StoredInfoTypeStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeStats))
      }
    }  
  
Fields  
---  
`config` |  `object (`[StoredInfoTypeConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeConfig)`)` StoredInfoType configuration.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create timestamp of the version. Read-only, determined by the system when the version is created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[StoredInfoTypeState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeState)`)` Output only. Stored info type version state. Read-only, updated by the system during dictionary creation.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` Output only. Errors that occurred when creating this storedInfoType version, or anomalies detected in the storedInfoType data that render it unusable. Only the five most recent errors will be displayed, with the most recent error appearing first.For example, some of the data for stored custom dictionaries is put in the user's Cloud Storage bucket, and if this data is modified or deleted by the user or another system, the dictionary becomes invalid.If any errors occur, fix the problem indicated by the error message and use the storedInfoTypes.patch API method to create another version of the storedInfoType to continue using it, reusing the same `config` if it was not the source of the error.  
`stats` |  `object (`[StoredInfoTypeStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeStats)`)` Output only. Statistics about this storedInfoType version.  
  
### StoredInfoTypeConfig

Configuration for stored infoTypes. All fields and subfield are provided by the user. For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes>.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "description": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "largeCustomDictionary": {
        object ([LargeCustomDictionaryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.LargeCustomDictionaryConfig))
      },
      "dictionary": {
        object ([Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary))
      },
      "regex": {
        object ([Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`displayName` |  `string` Display name of the StoredInfoType (max 256 characters).  
`description` |  `string` Description of the StoredInfoType (max 256 characters).  
Stored infotype types. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`largeCustomDictionary` |  `object (`[LargeCustomDictionaryConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.LargeCustomDictionaryConfig)`)` StoredInfoType where findings are defined by a dictionary of phrases.  
`dictionary` |  `object (`[Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary)`)` Store dictionary-based CustomInfoType.  
`regex` |  `object (`[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex)`)` Store regular expression-based StoredInfoType.  
End of mutually exclusive fields.  
  
### LargeCustomDictionaryConfig

Configuration for a custom dictionary created from a data source of any size up to the maximum size defined in the [limits](https://docs.cloud.google.com/sensitive-data-protection/limits) page. The artifacts of dictionary creation are stored in the specified Cloud Storage location. Consider using `CustomInfoType.Dictionary` for smaller dictionaries that satisfy the size requirements.

JSON representation  
---  
      
    
    {
      "outputPath": {
        object ([CloudStoragePath](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/CloudStoragePath))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cloudStorageFileSet": {
        object ([CloudStorageFileSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.CloudStorageFileSet))
      },
      "bigQueryField": {
        object ([BigQueryField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.BigQueryField))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`outputPath` |  `object (`[CloudStoragePath](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/CloudStoragePath)`)` Location to store dictionary artifacts in Cloud Storage. These files will only be accessible by project owners and the DLP API. If any of these artifacts are modified, the dictionary is considered invalid and can no longer be used.  
Source of the dictionary. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cloudStorageFileSet` |  `object (`[CloudStorageFileSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.CloudStorageFileSet)`)` Set of files containing newline-delimited lists of dictionary phrases.  
`bigQueryField` |  `object (`[BigQueryField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.BigQueryField)`)` Field in a BigQuery table where each cell represents a dictionary phrase.  
End of mutually exclusive fields.  
  
### CloudStorageFileSet

Message representing a set of files in Cloud Storage.

JSON representation  
---  
      
    
    {
      "url": string
    }  
  
Fields  
---  
`url` |  `string` The url, in the format `gs://<bucket>/<path>`. Trailing wildcard in the path is allowed.  
  
### BigQueryField

Message defining a field of a BigQuery table.

JSON representation  
---  
      
    
    {
      "table": {
        object ([BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable))
      },
      "field": {
        object ([FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId))
      }
    }  
  
Fields  
---  
`table` |  `object (`[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable)`)` Source table of the field.  
`field` |  `object (`[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId)`)` Designated field in the BigQuery table.  
  
### StoredInfoTypeState

State of a StoredInfoType version.

Enums  
---  
`STORED_INFO_TYPE_STATE_UNSPECIFIED` | Unused  
`PENDING` | StoredInfoType version is being created.  
`READY` | StoredInfoType version is ready for use.  
`FAILED` | StoredInfoType creation failed. All relevant error messages are returned in the `StoredInfoTypeVersion` message.  
`INVALID` | StoredInfoType is no longer valid because artifacts stored in user-controlled storage were modified. To fix an invalid StoredInfoType, use the `storedInfoTypes.patch` method to create a new version.  
  
### StoredInfoTypeStats

Statistics for a StoredInfoType.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "largeCustomDictionary": {
        object ([LargeCustomDictionaryStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.LargeCustomDictionaryStats))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Stat types The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`largeCustomDictionary` |  `object (`[LargeCustomDictionaryStats](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.LargeCustomDictionaryStats)`)` StoredInfoType where findings are defined by a dictionary of phrases.  
End of mutually exclusive fields.  
  
### LargeCustomDictionaryStats

Summary statistics of a custom dictionary.

JSON representation  
---  
      
    
    {
      "approxNumPhrases": string
    }  
  
Fields  
---  
`approxNumPhrases` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Approximate number of distinct phrases in the dictionary.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/create)`

|  Creates a pre-built stored infoType to be used for inspection.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/delete)`

|  Deletes a stored infoType.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/get)`

|  Gets a stored infoType.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/list)`

|  Lists stored infoTypes.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/patch)`

|  Updates the stored infoType by creating a new version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
