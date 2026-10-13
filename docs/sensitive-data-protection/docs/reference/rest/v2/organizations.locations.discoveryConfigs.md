---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs
title: REST Resource: organizations.locations.discoveryConfigs \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:23.529794+00:00
---

# REST Resource: organizations.locations.discoveryConfigs  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.discoveryConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DiscoveryConfig
    * JSON representation
    * OrgConfig
      * JSON representation
    * DiscoveryStartingLocation
      * JSON representation
    * DiscoveryTarget
      * JSON representation
    * BigQueryDiscoveryTarget
      * JSON representation
    * DiscoveryBigQueryFilter
      * JSON representation
    * BigQueryTableCollection
      * JSON representation
    * BigQueryRegexes
      * JSON representation
    * BigQueryRegex
      * JSON representation
    * AllOtherBigQueryTables
    * TableReference
      * JSON representation
    * DiscoveryBigQueryConditions
      * JSON representation
    * BigQueryTableTypes
      * JSON representation
    * BigQueryTableType
    * BigQueryTableTypeCollection
    * OrConditions
      * JSON representation
    * DiscoveryGenerationCadence
      * JSON representation
    * DiscoverySchemaModifiedCadence
      * JSON representation
    * BigQuerySchemaModification
    * DataProfileUpdateFrequency
    * DiscoveryTableModifiedCadence
      * JSON representation
    * BigQueryTableModification
    * DiscoveryInspectTemplateModifiedCadence
      * JSON representation
    * Disabled
    * CloudSqlDiscoveryTarget
      * JSON representation
    * DiscoveryCloudSqlFilter
      * JSON representation
    * DatabaseResourceCollection
      * JSON representation
    * DatabaseResourceRegexes
      * JSON representation
    * DatabaseResourceRegex
      * JSON representation
    * AllOtherDatabaseResources
    * DatabaseResourceReference
      * JSON representation
    * DiscoveryCloudSqlConditions
      * JSON representation
    * DatabaseEngine
    * DatabaseResourceType
    * DiscoveryCloudSqlGenerationCadence
      * JSON representation
    * SchemaModifiedCadence
      * JSON representation
    * CloudSqlSchemaModification
    * SecretsDiscoveryTarget
    * CloudStorageDiscoveryTarget
      * JSON representation
    * DiscoveryCloudStorageFilter
      * JSON representation
    * FileStoreCollection
      * JSON representation
    * FileStoreRegexes
      * JSON representation
    * FileStoreRegex
      * JSON representation
    * CloudStorageRegex
      * JSON representation
    * TagFilters
      * JSON representation
    * TagFilter
      * JSON representation
    * CloudStorageResourceReference
      * JSON representation
    * AllOtherResources
    * DiscoveryFileStoreConditions
      * JSON representation
    * DiscoveryCloudStorageConditions
      * JSON representation
    * CloudStorageObjectAttribute
    * CloudStorageBucketAttribute
    * DiscoveryCloudStorageGenerationCadence
      * JSON representation
    * OtherCloudDiscoveryTarget
      * JSON representation
    * DiscoveryOtherCloudFilter
      * JSON representation
    * OtherCloudResourceCollection
      * JSON representation
    * OtherCloudResourceRegexes
      * JSON representation
    * OtherCloudResourceRegex
      * JSON representation
    * AmazonS3BucketRegex
      * JSON representation
    * AwsAccountRegex
      * JSON representation
    * OtherCloudSingleResourceReference
      * JSON representation
    * AmazonS3Bucket
      * JSON representation
    * AwsAccount
      * JSON representation
    * DiscoveryOtherCloudConditions
      * JSON representation
    * AmazonS3BucketConditions
      * JSON representation
    * BucketType
    * ObjectStorageClass
    * DiscoveryOtherCloudGenerationCadence
      * JSON representation
    * VertexDatasetDiscoveryTarget
      * JSON representation
    * DiscoveryVertexDatasetFilter
      * JSON representation
    * VertexDatasetCollection
      * JSON representation
    * VertexDatasetRegexes
      * JSON representation
    * VertexDatasetRegex
      * JSON representation
    * VertexDatasetResourceReference
      * JSON representation
    * DiscoveryVertexDatasetConditions
      * JSON representation
    * DiscoveryVertexDatasetGenerationCadence
      * JSON representation
    * Status
    * ProcessingLocation
      * JSON representation
    * ImageFallbackLocation
      * JSON representation
    * MultiRegionProcessing
    * GlobalProcessing
    * DocumentFallbackLocation
      * JSON representation
  * Methods



## Resource: DiscoveryConfig

Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "orgConfig": {
        object ([OrgConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OrgConfig))
      },
      "otherCloudStartingLocation": {
        object ([OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/OtherCloudDiscoveryStartingLocation))
      },
      "inspectTemplates": [
        string
      ],
      "actions": [
        {
          object ([DataProfileAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction))
        }
      ],
      "targets": [
        {
          object ([DiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryTarget))
        }
      ],
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "lastRunTime": string,
      "status": enum ([Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Status)),
      "processingLocation": {
        object ([ProcessingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.ProcessingLocation))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.  
`displayName` |  `string` Display name (max 100 chars)  
`orgConfig` |  `object (`[OrgConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OrgConfig)`)` Only set when the parent is an org.  
`otherCloudStartingLocation` |  `object (`[OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/OtherCloudDiscoveryStartingLocation)`)` Must be set only when scanning other clouds.  
`inspectTemplates[]` |  `string` Detection logic for profile generation.Not all template features are used by Discovery. FindingLimits, includeQuote and excludeInfoTypes have no impact on Discovery.Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.  
`actions[]` |  `object (`[DataProfileAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction)`)` Actions to execute at the completion of scanning.  
`targets[]` |  `object (`[DiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryTarget)`)` Target to match against for determining what to scan and how frequently.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of a DiscoveryConfig.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of a DiscoveryConfig.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastRunTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of the last time this config was executed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Status)`)` Required. A status for this configuration.  
`processingLocation` |  `object (`[ProcessingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.ProcessingLocation)`)` Optional. Processing location configuration. Vertex AI dataset scanning will set processingLocation.image_fallback_type to MultiRegionProcessing by default.  
  
### OrgConfig

Project and scan location information. Only set when the parent is an org.

JSON representation  
---  
      
    
    {
      "location": {
        object ([DiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryStartingLocation))
      },
      "projectId": string
    }  
  
Fields  
---  
`location` |  `object (`[DiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryStartingLocation)`)` The data to scan: folder, org, or project  
`projectId` |  `string` The project that will run the scan. The DLP service account that exists within this project must have access to all resources that are profiled, and the DLP API must be enabled.  
  
### DiscoveryStartingLocation

The location to begin a discovery scan. Denotes an organization ID or folder ID within an organization.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "organizationId": string,
      "folderId": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The location to be scanned. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`organizationId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The ID of an organization to scan.  
`folderId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The ID of the folder within an organization to be scanned.  
End of mutually exclusive fields.  
  
### DiscoveryTarget

Target used to match against for Discovery.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "bigQueryTarget": {
        object ([BigQueryDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryDiscoveryTarget))
      },
      "cloudSqlTarget": {
        object ([CloudSqlDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudSqlDiscoveryTarget))
      },
      "secretsTarget": {
        object ([SecretsDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.SecretsDiscoveryTarget))
      },
      "cloudStorageTarget": {
        object ([CloudStorageDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageDiscoveryTarget))
      },
      "otherCloudTarget": {
        object ([OtherCloudDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudDiscoveryTarget))
      },
      "vertexDatasetTarget": {
        object ([VertexDatasetDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetDiscoveryTarget))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
A target to match against for Discovery. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`bigQueryTarget` |  `object (`[BigQueryDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryDiscoveryTarget)`)` BigQuery target for Discovery. The first target to match a table will be the one applied.  
`cloudSqlTarget` |  `object (`[CloudSqlDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudSqlDiscoveryTarget)`)` Cloud SQL target for Discovery. The first target to match a table will be the one applied.  
`secretsTarget` |  `object (`[SecretsDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.SecretsDiscoveryTarget)`)` Discovery target that looks for credentials and secrets stored in cloud resource metadata and reports them as vulnerabilities to Security Command Center. Only one target of this type is allowed.  
`cloudStorageTarget` |  `object (`[CloudStorageDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageDiscoveryTarget)`)` Cloud Storage target for Discovery. The first target to match a table will be the one applied.  
`otherCloudTarget` |  `object (`[OtherCloudDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudDiscoveryTarget)`)` Other clouds target for discovery. The first target to match a resource will be the one applied.  
`vertexDatasetTarget` |  `object (`[VertexDatasetDiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetDiscoveryTarget)`)` Vertex AI dataset target for Discovery. The first target to match a dataset will be the one applied. Note that discovery for Vertex AI can incur Cloud Storage Class B operation charges for storage.objects.get operations and retrieval fees. For more information, see [Cloud Storage pricing](https://cloud.google.com/storage/pricing#price-tables). Note that discovery for Vertex AI dataset will not be able to scan images unless DiscoveryConfig.processing_location.image_fallback_location has multiRegionProcessing or globalProcessing configured.  
End of mutually exclusive fields.  
  
### BigQueryDiscoveryTarget

Target used to match against for discovery with BigQuery tables

JSON representation  
---  
      
    
    {
      "filter": {
        object ([DiscoveryBigQueryFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryBigQueryFilter))
      },
      "conditions": {
        object ([DiscoveryBigQueryConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryBigQueryConditions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cadence": {
        object ([DiscoveryGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryGenerationCadence))
      },
      "disabled": {
        object ([Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`filter` |  `object (`[DiscoveryBigQueryFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryBigQueryFilter)`)` Required. The tables the discovery cadence applies to. The first target with a matching filter will be the one to apply to a table.  
`conditions` |  `object (`[DiscoveryBigQueryConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryBigQueryConditions)`)` In addition to matching the filter, these conditions must be true before a profile is generated.  
The generation rule includes the logic on how frequently to update the data profiles. If not specified, discovery will re-run and update no more than once a month if new columns appear in the table. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cadence` |  `object (`[DiscoveryGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryGenerationCadence)`)` How often and when to update profiles. New tables that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `object (`[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled)`)` Tables that match this filter will not have profiles created.  
End of mutually exclusive fields.  
  
### DiscoveryBigQueryFilter

Determines what tables will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID, dataset ID, and table ID.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tables": {
        object ([BigQueryTableCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableCollection))
      },
      "otherTables": {
        object ([AllOtherBigQueryTables](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherBigQueryTables))
      },
      "tableReference": {
        object ([TableReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.TableReference))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether the filter applies to a specific set of tables or all other tables within the location being profiled. The first filter to match will be applied, regardless of the condition. If none is set, will default to `other_tables`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tables` |  `object (`[BigQueryTableCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableCollection)`)` A specific set of tables for this filter to apply to. A table collection must be specified in only one filter per config. If a table id or dataset is empty, Cloud DLP assumes all tables in that collection must be profiled. Must specify a project ID.  
`otherTables` |  `object (`[AllOtherBigQueryTables](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherBigQueryTables)`)` Catch-all. This should always be the last filter in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
`tableReference` |  `object (`[TableReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.TableReference)`)` The table to scan. Discovery configurations including this can only include one DiscoveryTarget (the DiscoveryTarget with this TableReference).  
End of mutually exclusive fields.  
  
### BigQueryTableCollection

Specifies a collection of BigQuery tables. Used for Discovery.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "includeRegexes": {
        object ([BigQueryRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryRegexes))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Maximum of 100 entries. The first filter containing a pattern that matches a table will be used. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`includeRegexes` |  `object (`[BigQueryRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryRegexes)`)` A collection of regular expressions to match a BigQuery table against.  
End of mutually exclusive fields.  
  
### BigQueryRegexes

A collection of regular expressions to determine what tables to match against.

JSON representation  
---  
      
    
    {
      "patterns": [
        {
          object ([BigQueryRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryRegex))
        }
      ]
    }  
  
Fields  
---  
`patterns[]` |  `object (`[BigQueryRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryRegex)`)` A single BigQuery regular expression pattern to match against one or more tables, datasets, or projects that contain BigQuery tables.  
  
### BigQueryRegex

A pattern to match against one or more tables, datasets, or projects that contain BigQuery tables. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

JSON representation  
---  
      
    
    {
      "projectIdRegex": string,
      "datasetIdRegex": string,
      "tableIdRegex": string
    }  
  
Fields  
---  
`projectIdRegex` |  `string` For organizations, if unset, will match all projects. Has no effect for data profile configurations created within a project.  
`datasetIdRegex` |  `string` If unset, this property matches all datasets.  
`tableIdRegex` |  `string` If unset, this property matches all tables.  
  
### AllOtherBigQueryTables

This type has no fields.

Catch-all for all other tables not specified by other filters. Should always be last, except for single-table configurations, which will only have a TableReference target.

### TableReference

Message defining the location of a BigQuery table with the projectId inferred from the parent project.

JSON representation  
---  
      
    
    {
      "datasetId": string,
      "tableId": string,
      "projectId": string
    }  
  
Fields  
---  
`datasetId` |  `string` Dataset ID of the table.  
`tableId` |  `string` Name of the table.  
`projectId` |  `string` The Google Cloud project ID of the project containing the table. If omitted, the project ID is inferred from the parent project. This field is required if the parent resource is an organization.  
  
### DiscoveryBigQueryConditions

Requirements that must be true before a table is scanned in discovery for the first time. There is an AND relationship between the top-level attributes. Additionally, minimum conditions with an OR relationship that must be met before Cloud DLP scans a table can be set (like a minimum row count or a minimum table age).

JSON representation  
---  
      
    
    {
      "createdAfter": string,
      "orConditions": {
        object ([OrConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OrConditions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "types": {
        object ([BigQueryTableTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableTypes))
      },
      "typeCollection": enum ([BigQueryTableTypeCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableTypeCollection))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`createdAfter` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` BigQuery table must have been created after this date. Used to avoid backfilling.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`orConditions` |  `object (`[OrConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OrConditions)`)` At least one of the conditions must be true for a table to be scanned.  
The type of BigQuery tables to scan. If nothing is set the default behavior is to scan only tables of type TABLE and to give errors for all unsupported tables. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`types` |  `object (`[BigQueryTableTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableTypes)`)` Restrict discovery to specific table types.  
`typeCollection` |  `enum (`[BigQueryTableTypeCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableTypeCollection)`)` Restrict discovery to categories of table types.  
End of mutually exclusive fields.  
  
### BigQueryTableTypes

The types of BigQuery tables supported by Cloud DLP.

JSON representation  
---  
      
    
    {
      "types": [
        enum ([BigQueryTableType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableType))
      ]
    }  
  
Fields  
---  
`types[]` |  `enum (`[BigQueryTableType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableType)`)` A set of BigQuery table types.  
  
### BigQueryTableType

Over time new types may be added. Currently VIEW, MATERIALIZED_VIEW, and non-BigLake external tables are not supported.

Enums  
---  
`BIG_QUERY_TABLE_TYPE_UNSPECIFIED` | Unused.  
`BIG_QUERY_TABLE_TYPE_TABLE` | A normal BigQuery table.  
`BIG_QUERY_TABLE_TYPE_EXTERNAL_BIG_LAKE` | A table that references data stored in Cloud Storage.  
`BIG_QUERY_TABLE_TYPE_SNAPSHOT` | A snapshot of a BigQuery table.  
  
### BigQueryTableTypeCollection

Over time new types may be added. Currently VIEW, MATERIALIZED_VIEW, and non-BigLake external tables are not supported.

Enums  
---  
`BIG_QUERY_COLLECTION_UNSPECIFIED` | Unused.  
`BIG_QUERY_COLLECTION_ALL_TYPES` | Automatically generate profiles for all tables, even if the table type is not yet fully supported for analysis. Profiles for unsupported tables will be generated with errors to indicate their partial support. When full support is added, the tables will automatically be profiled during the next scheduled run.  
`BIG_QUERY_COLLECTION_ONLY_SUPPORTED_TYPES` | Only those types fully supported will be profiled. Will expand automatically as Cloud DLP adds support for new table types. Unsupported table types will not have partial profiles generated.  
  
### OrConditions

There is an OR relationship between these attributes. They are used to determine if a table should be scanned or not in Discovery.

JSON representation  
---  
      
    
    {
      "minRowCount": integer,
      "minAge": string
    }  
  
Fields  
---  
`minRowCount` |  `integer` Minimum number of rows that should be present before Cloud DLP profiles a table  
`minAge` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Minimum age a table must have before Cloud DLP can profile it. Value must be 1 hour or greater.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### DiscoveryGenerationCadence

What must take place for a profile to be updated and how frequently it should occur. New tables are scanned as quickly as possible depending on system capacity.

JSON representation  
---  
      
    
    {
      "schemaModifiedCadence": {
        object ([DiscoverySchemaModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoverySchemaModifiedCadence))
      },
      "tableModifiedCadence": {
        object ([DiscoveryTableModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryTableModifiedCadence))
      },
      "inspectTemplateModifiedCadence": {
        object ([DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence))
      },
      "refreshFrequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency))
    }  
  
Fields  
---  
`schemaModifiedCadence` |  `object (`[DiscoverySchemaModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoverySchemaModifiedCadence)`)` Governs when to update data profiles when a schema is modified.  
`tableModifiedCadence` |  `object (`[DiscoveryTableModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryTableModifiedCadence)`)` Governs when to update data profiles when a table is modified.  
`inspectTemplateModifiedCadence` |  `object (`[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence)`)` Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to update.  
`refreshFrequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` Frequency at which profiles should be updated, regardless of whether the underlying resource has changed. Defaults to never.  
  
### DiscoverySchemaModifiedCadence

The cadence at which to update data profiles when a schema is modified.

JSON representation  
---  
      
    
    {
      "types": [
        enum ([BigQuerySchemaModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQuerySchemaModification))
      ],
      "frequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency))
    }  
  
Fields  
---  
`types[]` |  `enum (`[BigQuerySchemaModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQuerySchemaModification)`)` The type of events to consider when deciding if the table's schema has been modified and should have the profile updated. Defaults to NEW_COLUMNS.  
`frequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` How frequently profiles may be updated when schemas are modified. Defaults to monthly.  
  
### BigQuerySchemaModification

Attributes evaluated to determine if a schema has been modified. New values may be added at a later time.

Enums  
---  
`SCHEMA_MODIFICATION_UNSPECIFIED` | Unused  
`SCHEMA_NEW_COLUMNS` | Profiles should be regenerated when new columns are added to the table. Default.  
`SCHEMA_REMOVED_COLUMNS` | Profiles should be regenerated when columns are removed from the table.  
  
### DataProfileUpdateFrequency

How frequently data profiles can be updated. New options can be added at a later time.

Enums  
---  
`UPDATE_FREQUENCY_UNSPECIFIED` | Unspecified.  
`UPDATE_FREQUENCY_NEVER` | After the data profile is created, it will never be updated.  
`UPDATE_FREQUENCY_DAILY` | The data profile can be updated up to once every 24 hours.  
`UPDATE_FREQUENCY_MONTHLY` | The data profile can be updated up to once every 30 days. Default.  
  
### DiscoveryTableModifiedCadence

The cadence at which to update data profiles when a table is modified.

JSON representation  
---  
      
    
    {
      "types": [
        enum ([BigQueryTableModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableModification))
      ],
      "frequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency))
    }  
  
Fields  
---  
`types[]` |  `enum (`[BigQueryTableModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BigQueryTableModification)`)` The type of events to consider when deciding if the table has been modified and should have the profile updated. Defaults to MODIFIED_TIMESTAMP.  
`frequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` How frequently data profiles can be updated when tables are modified. Defaults to never.  
  
### BigQueryTableModification

Attributes evaluated to determine if a table has been modified. New values may be added at a later time.

Enums  
---  
`TABLE_MODIFICATION_UNSPECIFIED` | Unused.  
`TABLE_MODIFIED_TIMESTAMP` | A table will be considered modified when the lastModifiedTime from BigQuery has been updated.  
  
### DiscoveryInspectTemplateModifiedCadence

The cadence at which to update data profiles when the inspection rules defined by the `InspectTemplate` change.

JSON representation  
---  
      
    
    {
      "frequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency))
    }  
  
Fields  
---  
`frequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` How frequently data profiles can be updated when the template is modified. Defaults to never.  
  
### Disabled

This type has no fields.

Do not profile the tables.

### CloudSqlDiscoveryTarget

Target used to match against for discovery with Cloud SQL tables.

JSON representation  
---  
      
    
    {
      "filter": {
        object ([DiscoveryCloudSqlFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudSqlFilter))
      },
      "conditions": {
        object ([DiscoveryCloudSqlConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudSqlConditions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "generationCadence": {
        object ([DiscoveryCloudSqlGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudSqlGenerationCadence))
      },
      "disabled": {
        object ([Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`filter` |  `object (`[DiscoveryCloudSqlFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudSqlFilter)`)` Required. The tables the discovery cadence applies to. The first target with a matching filter will be the one to apply to a table.  
`conditions` |  `object (`[DiscoveryCloudSqlConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudSqlConditions)`)` In addition to matching the filter, these conditions must be true before a profile is generated.  
Type of schedule. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`generationCadence` |  `object (`[DiscoveryCloudSqlGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudSqlGenerationCadence)`)` How often and when to update profiles. New tables that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `object (`[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled)`)` Disable profiling for database resources that match this filter.  
End of mutually exclusive fields.  
  
### DiscoveryCloudSqlFilter

Determines what tables will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID, location, instance, database, and database resource name.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "collection": {
        object ([DatabaseResourceCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceCollection))
      },
      "others": {
        object ([AllOtherDatabaseResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherDatabaseResources))
      },
      "databaseResourceReference": {
        object ([DatabaseResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceReference))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether the filter applies to a specific set of database resources or all other database resources within the location being profiled. The first filter to match will be applied, regardless of the condition. If none is set, will default to `others`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`collection` |  `object (`[DatabaseResourceCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceCollection)`)` A specific set of database resources for this filter to apply to.  
`others` |  `object (`[AllOtherDatabaseResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherDatabaseResources)`)` Catch-all. This should always be the last target in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
`databaseResourceReference` |  `object (`[DatabaseResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceReference)`)` The database resource to scan. Targets including this can only include one target (the target with this database resource reference).  
End of mutually exclusive fields.  
  
### DatabaseResourceCollection

Match database resources using regex filters. Examples of database resources are tables, views, and stored procedures.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "includeRegexes": {
        object ([DatabaseResourceRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceRegexes))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The first filter containing a pattern that matches a database resource will be used. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`includeRegexes` |  `object (`[DatabaseResourceRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceRegexes)`)` A collection of regular expressions to match a database resource against.  
End of mutually exclusive fields.  
  
### DatabaseResourceRegexes

A collection of regular expressions to determine what database resources to match against.

JSON representation  
---  
      
    
    {
      "patterns": [
        {
          object ([DatabaseResourceRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceRegex))
        }
      ]
    }  
  
Fields  
---  
`patterns[]` |  `object (`[DatabaseResourceRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceRegex)`)` A group of regular expression patterns to match against one or more database resources. Maximum of 100 entries. The sum of all regular expression's length can't exceed 10 KiB.  
  
### DatabaseResourceRegex

A pattern to match against one or more database resources. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

JSON representation  
---  
      
    
    {
      "projectIdRegex": string,
      "instanceRegex": string,
      "databaseRegex": string,
      "databaseResourceNameRegex": string
    }  
  
Fields  
---  
`projectIdRegex` |  `string` For organizations, if unset, will match all projects. Has no effect for configurations created within a project.  
`instanceRegex` |  `string` Regex to test the instance name against. If empty, all instances match.  
`databaseRegex` |  `string` Regex to test the database name against. If empty, all databases match.  
`databaseResourceNameRegex` |  `string` Regex to test the database resource's name against. An example of a database resource name is a table's name. Other database resource names like view names could be included in the future. If empty, all database resources match.  
  
### AllOtherDatabaseResources

This type has no fields.

Match database resources not covered by any other filter.

### DatabaseResourceReference

Identifies a single database resource, like a table within a database.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "instance": string,
      "database": string,
      "databaseResource": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. If within a project-level config, then this must match the config's project ID.  
`instance` |  `string` Required. The instance where this resource is located. For example: Cloud SQL instance ID.  
`database` |  `string` Required. Name of a database within the instance.  
`databaseResource` |  `string` Required. Name of a database resource, for example, a table within the database.  
  
### DiscoveryCloudSqlConditions

Requirements that must be true before a table is profiled for the first time.

JSON representation  
---  
      
    
    {
      "databaseEngines": [
        enum ([DatabaseEngine](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseEngine))
      ],
      "types": [
        enum ([DatabaseResourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceType))
      ]
    }  
  
Fields  
---  
`databaseEngines[]` |  `enum (`[DatabaseEngine](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseEngine)`)` Optional. Database engines that should be profiled. Optional. Defaults to ALL_SUPPORTED_DATABASE_ENGINES if unspecified.  
`types[]` |  `enum (`[DatabaseResourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DatabaseResourceType)`)` Data profiles will only be generated for the database resource types specified in this field. If not specified, defaults to [DATABASE_RESOURCE_TYPE_ALL_SUPPORTED_TYPES].  
  
### DatabaseEngine

The database engines that should be profiled.

Enums  
---  
`DATABASE_ENGINE_UNSPECIFIED` | Unused.  
`ALL_SUPPORTED_DATABASE_ENGINES` | Include all supported database engines.  
`MYSQL` | MySQL database.  
`POSTGRES` | PostgreSQL database.  
  
### DatabaseResourceType

Cloud SQL database resource types. New values can be added at a later time.

Enums  
---  
`DATABASE_RESOURCE_TYPE_UNSPECIFIED` | Unused.  
`DATABASE_RESOURCE_TYPE_ALL_SUPPORTED_TYPES` | Includes database resource types that become supported at a later time.  
`DATABASE_RESOURCE_TYPE_TABLE` | Tables.  
  
### DiscoveryCloudSqlGenerationCadence

How often existing tables should have their profiles refreshed. New tables are scanned as quickly as possible depending on system capacity.

JSON representation  
---  
      
    
    {
      "schemaModifiedCadence": {
        object ([SchemaModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.SchemaModifiedCadence))
      },
      "refreshFrequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)),
      "inspectTemplateModifiedCadence": {
        object ([DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence))
      }
    }  
  
Fields  
---  
`schemaModifiedCadence` |  `object (`[SchemaModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.SchemaModifiedCadence)`)` When to reprofile if the schema has changed.  
`refreshFrequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` Data changes (non-schema changes) in Cloud SQL tables can't trigger reprofiling. If you set this field, profiles are refreshed at this frequency regardless of whether the underlying tables have changed. Defaults to never.  
`inspectTemplateModifiedCadence` |  `object (`[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence)`)` Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to update.  
  
### SchemaModifiedCadence

How frequently to modify the profile when the table's schema is modified.

JSON representation  
---  
      
    
    {
      "types": [
        enum ([CloudSqlSchemaModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudSqlSchemaModification))
      ],
      "frequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency))
    }  
  
Fields  
---  
`types[]` |  `enum (`[CloudSqlSchemaModification](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudSqlSchemaModification)`)` The types of schema modifications to consider. Defaults to NEW_COLUMNS.  
`frequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` Frequency to regenerate data profiles when the schema is modified. Defaults to monthly.  
  
### CloudSqlSchemaModification

The type of modification that causes a profile update.

Enums  
---  
`SQL_SCHEMA_MODIFICATION_UNSPECIFIED` | Unused.  
`NEW_COLUMNS` | New columns have appeared.  
`REMOVED_COLUMNS` | Columns have been removed from the table.  
  
### SecretsDiscoveryTarget

This type has no fields.

Discovery target for credentials and secrets in cloud resource metadata.

This target does not include any filtering or frequency controls. Cloud DLP will scan cloud resource metadata for secrets daily.

No inspect template should be included in the discovery config for a security benchmarks scan. Instead, the built-in list of secrets and credentials infoTypes will be used (see <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets)>.

Credentials and secrets discovered will be reported as vulnerabilities to Security Command Center.

### CloudStorageDiscoveryTarget

Target used to match against for discovery with Cloud Storage buckets.

JSON representation  
---  
      
    
    {
      "filter": {
        object ([DiscoveryCloudStorageFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudStorageFilter))
      },
      "conditions": {
        object ([DiscoveryFileStoreConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryFileStoreConditions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "generationCadence": {
        object ([DiscoveryCloudStorageGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudStorageGenerationCadence))
      },
      "disabled": {
        object ([Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`filter` |  `object (`[DiscoveryCloudStorageFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudStorageFilter)`)` Required. The buckets the generationCadence applies to. The first target with a matching filter will be the one to apply to a bucket.  
`conditions` |  `object (`[DiscoveryFileStoreConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryFileStoreConditions)`)` Optional. In addition to matching the filter, these conditions must be true before a profile is generated.  
How often and when to update profiles. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`generationCadence` |  `object (`[DiscoveryCloudStorageGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudStorageGenerationCadence)`)` Optional. How often and when to update profiles. New buckets that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `object (`[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled)`)` Optional. Disable profiling for buckets that match this filter.  
End of mutually exclusive fields.  
  
### DiscoveryCloudStorageFilter

Determines which buckets will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID and bucket name.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "collection": {
        object ([FileStoreCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.FileStoreCollection))
      },
      "cloudStorageResourceReference": {
        object ([CloudStorageResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageResourceReference))
      },
      "others": {
        object ([AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherResources))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether the filter applies to a specific set of buckets or all other buckets within the location being profiled. The first filter to match will be applied, regardless of the condition. If none is set, will default to `others`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`collection` |  `object (`[FileStoreCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.FileStoreCollection)`)` Optional. A specific set of buckets for this filter to apply to.  
`cloudStorageResourceReference` |  `object (`[CloudStorageResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageResourceReference)`)` Optional. The bucket to scan. Targets including this can only include one target (the target with this bucket). This enables profiling the contents of a single bucket, while the other options allow for easy profiling of many bucets within a project or an organization.  
`others` |  `object (`[AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherResources)`)` Optional. Catch-all. This should always be the last target in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
End of mutually exclusive fields.  
  
### FileStoreCollection

Match file stores (e.g. buckets) using filters.

JSON representation  
---  
      
    
    {
      "includeTags": {
        object ([TagFilters](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.TagFilters))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "includeRegexes": {
        object ([FileStoreRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.FileStoreRegexes))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`includeTags` |  `object (`[TagFilters](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.TagFilters)`)` Optional. To be included in the collection, a resource must meet all of the following requirements:

  * If tag filters are provided, match all provided tag filters.
  * If one or more patterns are specified, match at least one pattern.

For a resource to match the tag filters, the resource must have all of the provided tags attached. Tags refer to Resource Manager tags bound to the resource or its ancestors. For more information, see [Manage schedules](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-storage#manage-schedules).  
The first filter containing a pattern that matches a file store will be used. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`includeRegexes` |  `object (`[FileStoreRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.FileStoreRegexes)`)` Optional. A collection of regular expressions to match a file store against.  
End of mutually exclusive fields.  
  
### FileStoreRegexes

A collection of regular expressions to determine what file store to match against.

JSON representation  
---  
      
    
    {
      "patterns": [
        {
          object ([FileStoreRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.FileStoreRegex))
        }
      ]
    }  
  
Fields  
---  
`patterns[]` |  `object (`[FileStoreRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.FileStoreRegex)`)` Required. The group of regular expression patterns to match against one or more file stores. Maximum of 100 entries. The sum of all regular expression's length can't exceed 10 KiB.  
  
### FileStoreRegex

A pattern to match against one or more file stores.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cloudStorageRegex": {
        object ([CloudStorageRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageRegex))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of resource regex to use. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cloudStorageRegex` |  `object (`[CloudStorageRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageRegex)`)` Optional. Regex for Cloud Storage.  
End of mutually exclusive fields.  
  
### CloudStorageRegex

A pattern to match against one or more file stores. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

JSON representation  
---  
      
    
    {
      "projectIdRegex": string,
      "bucketNameRegex": string
    }  
  
Fields  
---  
`projectIdRegex` |  `string` Optional. For organizations, if unset, will match all projects.  
`bucketNameRegex` |  `string` Optional. Regex to test the bucket name against. If empty, all buckets match. Example: "marketing2021" or "(marketing)\d{4}" will both match the bucket gs://marketing2021  
  
### TagFilters

Tags to match against for filtering.

JSON representation  
---  
      
    
    {
      "tagFilters": [
        {
          object ([TagFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.TagFilter))
        }
      ]
    }  
  
Fields  
---  
`tagFilters[]` |  `object (`[TagFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.TagFilter)`)` Required. A resource must match ALL of the specified tag filters to be included in the collection.  
  
### TagFilter

A single tag to filter against.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "namespacedTagValue": string,
      "namespacedTagKey": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Tag filter formats. Tags refer to Resource Manager tags bound to the resource or its ancestors. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`namespacedTagValue` |  `string` The namespaced name for the tag value. Must be in the format `{parent_id}/{tag_key_short_name}/{short_name}`, for example, "123456/environment/prod" for an organization parent, or "my-project/environment/prod" for a project parent.  
`namespacedTagKey` |  `string` The namespaced name for the tag key. Must be in the format `{parent_id}/{tag_key_short_name}`, for example, "123456/sensitive" for an organization parent, or "my-project/sensitive" for a project parent.  
End of mutually exclusive fields.  
  
### CloudStorageResourceReference

Identifies a single Cloud Storage bucket.

JSON representation  
---  
      
    
    {
      "bucketName": string,
      "projectId": string
    }  
  
Fields  
---  
`bucketName` |  `string` Required. The bucket to scan.  
`projectId` |  `string` Required. If within a project-level config, then this must match the config's project id.  
  
### AllOtherResources

This type has no fields.

Match discovery resources not covered by any other filter.

### DiscoveryFileStoreConditions

Requirements that must be true before a file store is scanned in discovery for the first time. There is an AND relationship between the top-level attributes.

JSON representation  
---  
      
    
    {
      "createdAfter": string,
      "minAge": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cloudStorageConditions": {
        object ([DiscoveryCloudStorageConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudStorageConditions))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`createdAfter` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. File store must have been created after this date. Used to avoid backfilling.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`minAge` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Minimum age a file store must have. If set, the value must be 1 hour or greater.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
File store specific conditions. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cloudStorageConditions` |  `object (`[DiscoveryCloudStorageConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryCloudStorageConditions)`)` Optional. Cloud Storage conditions.  
End of mutually exclusive fields.  
  
### DiscoveryCloudStorageConditions

Requirements that must be true before a Cloud Storage bucket or object is scanned in discovery for the first time. There is an AND relationship between the top-level attributes.

JSON representation  
---  
      
    
    {
      "includedObjectAttributes": [
        enum ([CloudStorageObjectAttribute](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageObjectAttribute))
      ],
      "includedBucketAttributes": [
        enum ([CloudStorageBucketAttribute](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageBucketAttribute))
      ]
    }  
  
Fields  
---  
`includedObjectAttributes[]` |  `enum (`[CloudStorageObjectAttribute](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageObjectAttribute)`)` Required. Only objects with the specified attributes will be scanned. If an object has one of the specified attributes but is inside an excluded bucket, it will not be scanned. Defaults to [ALL_SUPPORTED_OBJECTS]. A profile will be created even if no objects match the includedObjectAttributes.  
`includedBucketAttributes[]` |  `enum (`[CloudStorageBucketAttribute](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.CloudStorageBucketAttribute)`)` Required. Only objects with the specified attributes will be scanned. Defaults to [ALL_SUPPORTED_BUCKETS] if unset.  
  
### CloudStorageObjectAttribute

The attribute of an object. See <https://docs.cloud.google.com/storage/docs/storage-classes> for more information on storage classes.

Enums  
---  
`CLOUD_STORAGE_OBJECT_ATTRIBUTE_UNSPECIFIED` | Unused.  
`ALL_SUPPORTED_OBJECTS` | Scan objects regardless of the attribute.  
`STANDARD` | Scan objects with the standard storage class.  
`NEARLINE` | Scan objects with the nearline storage class. This will incur retrieval fees.  
`COLDLINE` | Scan objects with the coldline storage class. This will incur retrieval fees.  
`ARCHIVE` | Scan objects with the archive storage class. This will incur retrieval fees.  
`REGIONAL` | Scan objects with the regional storage class.  
`MULTI_REGIONAL` | Scan objects with the multi-regional storage class.  
`DURABLE_REDUCED_AVAILABILITY` | Scan objects with the dual-regional storage class. This will incur retrieval fees.  
  
### CloudStorageBucketAttribute

The attribute of a bucket.

Enums  
---  
`CLOUD_STORAGE_BUCKET_ATTRIBUTE_UNSPECIFIED` | Unused.  
`ALL_SUPPORTED_BUCKETS` | Scan buckets regardless of the attribute.  
`AUTOCLASS_DISABLED` | Buckets with [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) disabled. Only one of AUTOCLASS_DISABLED or AUTOCLASS_ENABLED should be set.  
`AUTOCLASS_ENABLED` | Buckets with [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) enabled. Only one of AUTOCLASS_DISABLED or AUTOCLASS_ENABLED should be set. Scanning Autoclass-enabled buckets can affect object storage classes.  
  
### DiscoveryCloudStorageGenerationCadence

How often existing buckets should have their profiles refreshed. New buckets are scanned as quickly as possible depending on system capacity.

JSON representation  
---  
      
    
    {
      "refreshFrequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)),
      "inspectTemplateModifiedCadence": {
        object ([DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence))
      }
    }  
  
Fields  
---  
`refreshFrequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` Optional. Data changes in Cloud Storage can't trigger reprofiling. If you set this field, profiles are refreshed at this frequency regardless of whether the underlying buckets have changed. Defaults to never.  
`inspectTemplateModifiedCadence` |  `object (`[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence)`)` Optional. Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to update.  
  
### OtherCloudDiscoveryTarget

Target used to match against for discovery of resources from other clouds. An [AWS connector in Security Command Center (Enterprise](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) is required to use this feature.

JSON representation  
---  
      
    
    {
      "dataSourceType": {
        object ([DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType))
      },
      "filter": {
        object ([DiscoveryOtherCloudFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryOtherCloudFilter))
      },
      "conditions": {
        object ([DiscoveryOtherCloudConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryOtherCloudConditions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "generationCadence": {
        object ([DiscoveryOtherCloudGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryOtherCloudGenerationCadence))
      },
      "disabled": {
        object ([Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`dataSourceType` |  `object (`[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType)`)` Required. The type of data profiles generated by this discovery target. Supported values are: * aws/s3/bucket  
`filter` |  `object (`[DiscoveryOtherCloudFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryOtherCloudFilter)`)` Required. The resources that the discovery cadence applies to. The first target with a matching filter will be the one to apply to a resource.  
`conditions` |  `object (`[DiscoveryOtherCloudConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryOtherCloudConditions)`)` Optional. In addition to matching the filter, these conditions must be true before a profile is generated.  
Type of cadence. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`generationCadence` |  `object (`[DiscoveryOtherCloudGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryOtherCloudGenerationCadence)`)` How often and when to update data profiles. New resources that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `object (`[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled)`)` Disable profiling for resources that match this filter.  
End of mutually exclusive fields.  
  
### DiscoveryOtherCloudFilter

Determines which resources from the other cloud will have profiles generated. Includes the ability to filter by resource names.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "collection": {
        object ([OtherCloudResourceCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudResourceCollection))
      },
      "singleResource": {
        object ([OtherCloudSingleResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudSingleResourceReference))
      },
      "others": {
        object ([AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherResources))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether the filter applies to a specific set of resources or all other resources. The first filter to match will be applied, regardless of the condition. Defaults to `others` if none is set. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`collection` |  `object (`[OtherCloudResourceCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudResourceCollection)`)` A collection of resources for this filter to apply to.  
`singleResource` |  `object (`[OtherCloudSingleResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudSingleResourceReference)`)` The resource to scan. Configs using this filter can only have one target (the target with this single resource reference).  
`others` |  `object (`[AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherResources)`)` Optional. Catch-all. This should always be the last target in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
End of mutually exclusive fields.  
  
### OtherCloudResourceCollection

Match resources using regex filters.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "includeRegexes": {
        object ([OtherCloudResourceRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudResourceRegexes))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The first filter containing a pattern that matches a resource will be used. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`includeRegexes` |  `object (`[OtherCloudResourceRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudResourceRegexes)`)` A collection of regular expressions to match a resource against.  
End of mutually exclusive fields.  
  
### OtherCloudResourceRegexes

A collection of regular expressions to determine what resources to match against.

JSON representation  
---  
      
    
    {
      "patterns": [
        {
          object ([OtherCloudResourceRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudResourceRegex))
        }
      ]
    }  
  
Fields  
---  
`patterns[]` |  `object (`[OtherCloudResourceRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OtherCloudResourceRegex)`)` A group of regular expression patterns to match against one or more resources. Maximum of 100 entries. The sum of all regular expression's length can't exceed 10 KiB.  
  
### OtherCloudResourceRegex

A pattern to match against one or more resources. At least one pattern must be specified. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "amazonS3BucketRegex": {
        object ([AmazonS3BucketRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AmazonS3BucketRegex))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of resource regex to use. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`amazonS3BucketRegex` |  `object (`[AmazonS3BucketRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AmazonS3BucketRegex)`)` Regex for Amazon S3 buckets.  
End of mutually exclusive fields.  
  
### AmazonS3BucketRegex

Amazon S3 bucket regex.

JSON representation  
---  
      
    
    {
      "awsAccountRegex": {
        object ([AwsAccountRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AwsAccountRegex))
      },
      "bucketNameRegex": string
    }  
  
Fields  
---  
`awsAccountRegex` |  `object (`[AwsAccountRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AwsAccountRegex)`)` The AWS account regex.  
`bucketNameRegex` |  `string` Optional. Regex to test the bucket name against. If empty, all buckets match.  
  
### AwsAccountRegex

AWS account regex.

JSON representation  
---  
      
    
    {
      "accountIdRegex": string
    }  
  
Fields  
---  
`accountIdRegex` |  `string` Optional. Regex to test the AWS account ID against. If empty, all accounts match.  
  
### OtherCloudSingleResourceReference

Identifies a single resource, like a single Amazon S3 bucket.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "amazonS3Bucket": {
        object ([AmazonS3Bucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AmazonS3Bucket))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The resource to scan. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`amazonS3Bucket` |  `object (`[AmazonS3Bucket](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AmazonS3Bucket)`)` Amazon S3 bucket.  
End of mutually exclusive fields.  
  
### AmazonS3Bucket

Amazon S3 bucket.

JSON representation  
---  
      
    
    {
      "awsAccount": {
        object ([AwsAccount](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AwsAccount))
      },
      "bucketName": string
    }  
  
Fields  
---  
`awsAccount` |  `object (`[AwsAccount](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AwsAccount)`)` The AWS account.  
`bucketName` |  `string` Required. The bucket name.  
  
### AwsAccount

AWS account.

JSON representation  
---  
      
    
    {
      "accountId": string
    }  
  
Fields  
---  
`accountId` |  `string` Required. AWS account ID.  
  
### DiscoveryOtherCloudConditions

Requirements that must be true before a resource is profiled for the first time.

JSON representation  
---  
      
    
    {
      "minAge": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "amazonS3BucketConditions": {
        object ([AmazonS3BucketConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AmazonS3BucketConditions))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`minAge` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Minimum age a resource must be before Cloud DLP can profile it. Value must be 1 hour or greater.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
The conditions to apply. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`amazonS3BucketConditions` |  `object (`[AmazonS3BucketConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AmazonS3BucketConditions)`)` Amazon S3 bucket conditions.  
End of mutually exclusive fields.  
  
### AmazonS3BucketConditions

Amazon S3 bucket conditions.

JSON representation  
---  
      
    
    {
      "bucketTypes": [
        enum ([BucketType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BucketType))
      ],
      "objectStorageClasses": [
        enum ([ObjectStorageClass](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.ObjectStorageClass))
      ]
    }  
  
Fields  
---  
`bucketTypes[]` |  `enum (`[BucketType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.BucketType)`)` Optional. Bucket types that should be profiled. Optional. Defaults to TYPE_ALL_SUPPORTED if unspecified.  
`objectStorageClasses[]` |  `enum (`[ObjectStorageClass](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.ObjectStorageClass)`)` Optional. Object classes that should be profiled. Optional. Defaults to ALL_SUPPORTED_CLASSES if unspecified.  
  
### BucketType

Supported Amazon S3 bucket types. Defaults to TYPE_ALL_SUPPORTED.

Enums  
---  
`TYPE_UNSPECIFIED` | Unused.  
`TYPE_ALL_SUPPORTED` | All supported classes.  
`TYPE_GENERAL_PURPOSE` | A general purpose Amazon S3 bucket.  
  
### ObjectStorageClass

Supported Amazon S3 object storage classes. Defaults to ALL_SUPPORTED_CLASSES.

Enums  
---  
`UNSPECIFIED` | Unused.  
`ALL_SUPPORTED_CLASSES` | All supported classes.  
`STANDARD` | Standard object class.  
`STANDARD_INFREQUENT_ACCESS` | Standard - infrequent access object class.  
`GLACIER_INSTANT_RETRIEVAL` | Glacier - instant retrieval object class.  
`INTELLIGENT_TIERING` | Objects in the S3 Intelligent-Tiering access tiers.  
  
### DiscoveryOtherCloudGenerationCadence

How often existing resources should have their profiles refreshed. New resources are scanned as quickly as possible depending on system capacity.

JSON representation  
---  
      
    
    {
      "refreshFrequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)),
      "inspectTemplateModifiedCadence": {
        object ([DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence))
      }
    }  
  
Fields  
---  
`refreshFrequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` Optional. Frequency to update profiles regardless of whether the underlying resource has changes. Defaults to never.  
`inspectTemplateModifiedCadence` |  `object (`[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence)`)` Optional. Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to update.  
  
### VertexDatasetDiscoveryTarget

Target used to match against for discovery with Vertex AI datasets.

JSON representation  
---  
      
    
    {
      "filter": {
        object ([DiscoveryVertexDatasetFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryVertexDatasetFilter))
      },
      "conditions": {
        object ([DiscoveryVertexDatasetConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryVertexDatasetConditions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "generationCadence": {
        object ([DiscoveryVertexDatasetGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryVertexDatasetGenerationCadence))
      },
      "disabled": {
        object ([Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`filter` |  `object (`[DiscoveryVertexDatasetFilter](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryVertexDatasetFilter)`)` Required. The datasets the discovery cadence applies to. The first target with a matching filter will be the one to apply to a dataset.  
`conditions` |  `object (`[DiscoveryVertexDatasetConditions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryVertexDatasetConditions)`)` In addition to matching the filter, these conditions must be true before a profile is generated.  
Type of schedule. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`generationCadence` |  `object (`[DiscoveryVertexDatasetGenerationCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryVertexDatasetGenerationCadence)`)` How often and when to update profiles. New datasets that match both the filter and conditions are scanned as quickly as possible depending on system capacity.  
`disabled` |  `object (`[Disabled](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Disabled)`)` Disable profiling for datasets that match this filter.  
End of mutually exclusive fields.  
  
### DiscoveryVertexDatasetFilter

Determines what datasets will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID or dataset regex.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "collection": {
        object ([VertexDatasetCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetCollection))
      },
      "vertexDatasetResourceReference": {
        object ([VertexDatasetResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetResourceReference))
      },
      "others": {
        object ([AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherResources))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Whether the filter applies to a specific set of datasets or all other datasets within the location being profiled. The first filter to match will be applied, regardless of the condition. If none is set, this field defaults to `others`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`collection` |  `object (`[VertexDatasetCollection](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetCollection)`)` A specific set of Vertex AI datasets for this filter to apply to.  
`vertexDatasetResourceReference` |  `object (`[VertexDatasetResourceReference](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetResourceReference)`)` The dataset resource to scan. Targets including this can only include one target (the target with this dataset resource reference).  
`others` |  `object (`[AllOtherResources](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.AllOtherResources)`)` Catch-all. This should always be the last target in the list because anything above it will apply first. Should only appear once in a configuration. If none is specified, a default one will be added automatically.  
End of mutually exclusive fields.  
  
### VertexDatasetCollection

Match dataset resources using regex filters.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "vertexDatasetRegexes": {
        object ([VertexDatasetRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetRegexes))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The pattern used to filter dataset resources. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`vertexDatasetRegexes` |  `object (`[VertexDatasetRegexes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetRegexes)`)` The regex used to filter dataset resources.  
End of mutually exclusive fields.  
  
### VertexDatasetRegexes

A collection of regular expressions to determine what datasets to match against.

JSON representation  
---  
      
    
    {
      "patterns": [
        {
          object ([VertexDatasetRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetRegex))
        }
      ]
    }  
  
Fields  
---  
`patterns[]` |  `object (`[VertexDatasetRegex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.VertexDatasetRegex)`)` Required. The group of regular expression patterns to match against one or more datasets. Maximum of 100 entries. The sum of the lengths of all regular expressions can't exceed 10 KiB.  
  
### VertexDatasetRegex

A pattern to match against one or more dataset resources.

JSON representation  
---  
      
    
    {
      "projectIdRegex": string
    }  
  
Fields  
---  
`projectIdRegex` |  `string` For organizations, if unset, will match all projects. Has no effect for configurations created within a project.  
  
### VertexDatasetResourceReference

Identifies a single Vertex AI resource. Only datasets are supported.

JSON representation  
---  
      
    
    {
      "datasetResourceName": string
    }  
  
Fields  
---  
`datasetResourceName` |  `string` Required. The name of the Vertex AI resource. If set within a project-level configuration, the specified resource must be within the project. Examples:

  * `projects/{project}/locations/{location}/datasets/{dataset}`

  
  
### DiscoveryVertexDatasetConditions

Requirements that must be true before a dataset is profiled for the first time.

JSON representation  
---  
      
    
    {
      "createdAfter": string,
      "minAge": string
    }  
  
Fields  
---  
`createdAfter` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Vertex AI dataset must have been created after this date. Used to avoid backfilling.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`minAge` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Minimum age a Vertex AI dataset must have. If set, the value must be 1 hour or greater.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### DiscoveryVertexDatasetGenerationCadence

How often existing datasets should have their profiles refreshed. New datasets are scanned as quickly as possible depending on system capacity.

JSON representation  
---  
      
    
    {
      "refreshFrequency": enum ([DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)),
      "inspectTemplateModifiedCadence": {
        object ([DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence))
      }
    }  
  
Fields  
---  
`refreshFrequency` |  `enum (`[DataProfileUpdateFrequency](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DataProfileUpdateFrequency)`)` If you set this field, profiles are refreshed at this frequency regardless of whether the underlying datasets have changed. Defaults to never.  
`inspectTemplateModifiedCadence` |  `object (`[DiscoveryInspectTemplateModifiedCadence](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryInspectTemplateModifiedCadence)`)` Governs when to update data profiles when the inspection rules defined by the `InspectTemplate` change. If not set, changing the template will not cause a data profile to be updated.  
  
### Status

Whether the discovery config is currently active. New options may be added at a later time.

Enums  
---  
`STATUS_UNSPECIFIED` | Unused  
`RUNNING` | The discovery config is currently active.  
`PAUSED` | The discovery config is paused temporarily.  
  
### ProcessingLocation

Configure processing location for discovery and inspection. For example, image OCR is only provided in limited regions but configuring ProcessingLocation will redirect OCR to a location where OCR is provided.

JSON representation  
---  
      
    
    {
      "imageFallbackLocation": {
        object ([ImageFallbackLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.ImageFallbackLocation))
      },
      "documentFallbackLocation": {
        object ([DocumentFallbackLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DocumentFallbackLocation))
      }
    }  
  
Fields  
---  
`imageFallbackLocation` |  `object (`[ImageFallbackLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.ImageFallbackLocation)`)` Image processing falls back using this configuration.  
`documentFallbackLocation` |  `object (`[DocumentFallbackLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DocumentFallbackLocation)`)` Document processing falls back using this configuration.  
  
### ImageFallbackLocation

Configure image processing to fall back to any of the following processing options if image processing is unavailable in the original request location.

JSON representation  
---  
      
    
    {
      "multiRegionProcessing": {
        object ([MultiRegionProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.MultiRegionProcessing))
      },
      "globalProcessing": {
        object ([GlobalProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.GlobalProcessing))
      }
    }  
  
Fields  
---  
`multiRegionProcessing` |  `object (`[MultiRegionProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.MultiRegionProcessing)`)` Processing occurs in a multi-region that contains the current region if available.  
`globalProcessing` |  `object (`[GlobalProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.GlobalProcessing)`)` Processing occurs in the global region.  
  
### MultiRegionProcessing

This type has no fields.

Processing occurs in a multi-region that contains the current region if available.

### GlobalProcessing

This type has no fields.

Processing occurs in the global region.

### DocumentFallbackLocation

Configure document processing to fall back to any of the following processing options if document processing is unavailable in the original request location.

JSON representation  
---  
      
    
    {
      "multiRegionProcessing": {
        object ([MultiRegionProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.MultiRegionProcessing))
      },
      "globalProcessing": {
        object ([GlobalProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.GlobalProcessing))
      }
    }  
  
Fields  
---  
`multiRegionProcessing` |  `object (`[MultiRegionProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.MultiRegionProcessing)`)` Processing occurs in a multi-region that contains the current region if available.  
`globalProcessing` |  `object (`[GlobalProcessing](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.GlobalProcessing)`)` Processing occurs in the global region.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/create)`

|  Creates a config for discovery to scan and profile storage.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/delete)`

|  Deletes a discovery configuration.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/get)`

|  Gets a discovery configuration.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/list)`

|  Lists discovery configurations.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/patch)`

|  Updates a discovery configuration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
