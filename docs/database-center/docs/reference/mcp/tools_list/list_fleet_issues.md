---
url: https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues/
title: MCP Tools Reference: databasecenter.googleapis.com \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:30.613058+00:00
---

# MCP Tools Reference: databasecenter.googleapis.com  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  MCP Tools Reference: databasecenter.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_fleet_issues`

This tool provides a list of issues and recommendations that a user has access to and that are within the requested scope. Use this tool to identify specific database resources affected by health issues based on different categories like availability, data protection, security, performance and cost. It supports filtering issues by criteria such as product type, location, issue severity, tags, and labels. You can also apply filters for specific signal types and their associated products. The results can be sorted by signal type, product, location, or issue severity. If you need aggregated issue statistics instead of a list of individual issues, use the list_fleet_health_issues tool.

The following sample demonstrate how to use `curl` to invoke the `list_fleet_issues` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://databasecenter.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_fleet_issues",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

QueryIssuesRequest is the request to get a list of issues.

### QueryIssuesRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "filter": string,
      "signalProductsFilters": [
        {
          object ([SignalProductsFilters](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Input.Schema.SignalProductsFilters))
        }
      ],
      "orderBy": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The list is limited to the one attached to resources within the `scope` that a user has access to.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. Supported fields are: 'product', `location`, `issue_severity`, 'tags', 'labels',  
`signalProductsFilters[]` |  `object (`[SignalProductsFilters](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Input.Schema.SignalProductsFilters)`)` Optional. Filters based on signal and product. The filter list will be ORed across pairs and ANDed within a signal and products pair.  
`orderBy` |  `string` Optional. Following fields are sortable: SignalType Product Location IssueSeverityThe default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It only supports a single field at a time.  
`pageSize` |  `integer` Optional. If unspecified, at most 50 issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `QueryIssues` call. Provide this to retrieve the subsequent page. All parameters except page size should match the parameters used in the call that provided the page token.  
  
### SignalProductsFilters

JSON representation  
---  
      
    
    {
      "signalType": enum (SignalType),
      "products": [
        {
          object ([Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product))
        }
      ]
    }  
  
Fields  
---  
`signalType` |  `enum (`SignalType`)` Optional. The type of signal.  
`products[]` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product)`)` Optional. Product type of the resource. The version of the product will be ignored in filtering.  
  
### Product

JSON representation  
---  
      
    
    {
      "type": enum (ProductType),
      "engine": enum (Engine),
      "version": string,
      "minorVersion": string
    }  
  
Fields  
---  
`type` |  `enum (`ProductType`)` Optional. Type of specific database product. It could be CloudSQL, AlloyDB etc..  
`engine` |  `enum (`Engine`)` Optional. The specific engine that the underlying database is running.  
`version` |  `string` Optional. Version of the underlying database engine. Example values: For MySQL, it could be "8.0", "5.7" etc. For Postgres, it could be "14", "15" etc.  
`minorVersion` |  `string` Optional. Minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
## Output Schema

QueryIssuesResponse is the response containing a list of issues.

### QueryIssuesResponse

JSON representation  
---  
      
    
    {
      "resourceIssues": [
        {
          object ([DatabaseResourceIssue](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.DatabaseResourceIssue))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`resourceIssues[]` |  `object (`[DatabaseResourceIssue](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.DatabaseResourceIssue)`)` List of issues and resource details.  
`nextPageToken` |  `string` A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### DatabaseResourceIssue

JSON representation  
---  
      
    
    {
      "signal": {
        object ([Signal](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Signal))
      },
      "resource": {
        object ([DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.DatabaseResource))
      }
    }  
  
Fields  
---  
`signal` |  `object (`[Signal](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Signal)`)` Signal associated with the issue.  
`resource` |  `object (`[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.DatabaseResource)`)` Resource associated with the issue.  
  
### Signal

JSON representation  
---  
      
    
    {
      "signalType": enum (SignalType),
      "signalStatus": enum (SignalStatus),
      "additionalDetails": [
        {
          object ([AdditionalDetail](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.AdditionalDetail))
        }
      ],
      "issueSeverity": enum (IssueSeverity),
      "issueCreateTime": string
    }  
  
Fields  
---  
`signalType` |  `enum (`SignalType`)` Type of the signal.  
`signalStatus` |  `enum (`SignalStatus`)` Status of the signal.  
`additionalDetails[]` |  `object (`[AdditionalDetail](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.AdditionalDetail)`)` Additional information related to the signal. In the case of composite signals, this field encapsulates details associated with granular signals, having a signal status of "ISSUE"; signals with a status of "OK" are not included. For granular signals, it encompasses information relevant to the signal, regardless of the signal status.  
`issueSeverity` |  `enum (`IssueSeverity`)` Severity of the issue.  
`issueCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the issue was created (when signal status is ISSUE).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### AdditionalDetail

JSON representation  
---  
      
    
    {
      "signalSource": enum (SignalSource),
      "signalType": enum (SignalType),
      "signalEventTime": string,
    
      // Union field detail can be only one of the following:
      "shortBackupRetentionInfo": {
        object ([RetentionSettingsInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.RetentionSettingsInfo))
      },
      "backupRunInfo": {
        object ([BackupRunInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.BackupRunInfo))
      },
      "sccInfo": {
        object ([SCCInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SCCInfo))
      },
      "recommendationInfo": {
        object ([RecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.RecommendationInfo))
      },
      "automatedBackupPolicyInfo": {
        object ([AutomatedBackupPolicyInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.AutomatedBackupPolicyInfo))
      },
      "deletionProtectionInfo": {
        object ([DeletionProtectionInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.DeletionProtectionInfo))
      },
      "resourceSuspensionInfo": {
        object ([ResourceSuspensionInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.ResourceSuspensionInfo))
      },
      "inefficientQueryInfo": {
        object ([InefficientQueryInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.InefficientQueryInfo))
      },
      "outdatedMinorVersionInfo": {
        object ([OutdatedMinorVersionInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.OutdatedMinorVersionInfo))
      },
      "maintenanceRecommendationInfo": {
        object ([MaintenanceRecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MaintenanceRecommendationInfo))
      }
      // End of list of possible types for union field detail.
    }  
  
Fields  
---  
`signalSource` |  `enum (`SignalSource`)` Where the signal is coming from.  
`signalType` |  `enum (`SignalType`)` Type of the signal.  
`signalEventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Event time when signal was recorded by source service.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `detail`. Details related to signal. `detail` can be only one of the following:  
`shortBackupRetentionInfo` |  `object (`[RetentionSettingsInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.RetentionSettingsInfo)`)` Short backup retention information applies to signals with type SIGNAL_TYPE_SHORT_BACKUP_RETENTION.  
`backupRunInfo` |  `object (`[BackupRunInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.BackupRunInfo)`)` Backup run information applies to signals with types SIGNAL_TYPE_LAST_BACKUP_FAILED and SIGNAL_TYPE_LAST_BACKUP_OLD.  
`sccInfo` |  `object (`[SCCInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SCCInfo)`)` SCC information applies to SCC signals.  
`recommendationInfo` |  `object (`[RecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.RecommendationInfo)`)` Recommendation information applies to recommendations.  
`automatedBackupPolicyInfo` |  `object (`[AutomatedBackupPolicyInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.AutomatedBackupPolicyInfo)`)` Automated backup policy information applies to signals with type SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY.  
`deletionProtectionInfo` |  `object (`[DeletionProtectionInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.DeletionProtectionInfo)`)` Deletion protection information applies to signals with type `SIGNAL_TYPE_NO_DELETION_PROTECTION`  
`resourceSuspensionInfo` |  `object (`[ResourceSuspensionInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.ResourceSuspensionInfo)`)` Resource suspension information applies to signals with type `SIGNAL_TYPE_RESOURCE_SUSPENDED`.  
`inefficientQueryInfo` |  `object (`[InefficientQueryInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.InefficientQueryInfo)`)` Inefficient query information applies to signals with type `SIGNAL_TYPE_INEFFICIENT_QUERY`.  
`outdatedMinorVersionInfo` |  `object (`[OutdatedMinorVersionInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.OutdatedMinorVersionInfo)`)` Outdated minor version information applies to signals with type SIGNAL_TYPE_OUTDATED_MINOR_VERSION.  
`maintenanceRecommendationInfo` |  `object (`[MaintenanceRecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MaintenanceRecommendationInfo)`)` Maintenance recommendation information applies to signals with type SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES.  
  
### RetentionSettingsInfo

JSON representation  
---  
      
    
    {
      "subResource": {
        object ([SubResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SubResource))
      },
    
      // Union field retention can be only one of the following:
      "quantityBasedRetention": integer,
      "durationBasedRetention": string,
      "timestampBasedRetentionTime": string
      // End of list of possible types for union field retention.
    }  
  
Fields  
---  
`subResource` |  `object (`[SubResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SubResource)`)` Optional. Sub resource details associated with the backup configuration.  
Union field `retention`.`retention` can be only one of the following:  
`quantityBasedRetention` |  `integer` Number of backups that will be retained.  
`durationBasedRetention` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration based retention period i.e. 172800 seconds (2 days)A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timestampBasedRetentionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp based retention period i.e. till 2024-05-01T00:00:00ZUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Int32Value

JSON representation  
---  
      
    
    {
      "value": integer
    }  
  
Fields  
---  
`value` |  `integer` The int32 value.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### SubResource

JSON representation  
---  
      
    
    {
      "resourceType": string,
      "fullResourceName": string,
      "product": {
        object ([Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product))
      },
      "container": string
    }  
  
Fields  
---  
`resourceType` |  `string` Optional. Resource type associated with the sub resource where backup settings are configured. E.g. "spanner.googleapis.com/Database" for Spanner where backup retention is configured on database within an instance OPTIONAL  
`fullResourceName` |  `string` Optional. Resource name associated with the sub resource where backup settings are configured. E.g."//spanner.googleapis.com/projects/project1/instances/inst1/databases/db1" for Spanner where backup retention is configured on database within an instance OPTIONAL  
`product` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product)`)` Optional. Product information associated with the sub resource where backup retention settings are configured. e.g.
    
    
    product: {
     type   : PRODUCT_TYPE_SPANNER
     engine : ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT
    }
    

for Spanner where backup is configured on database within an instance OPTIONAL  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
  
### Product

JSON representation  
---  
      
    
    {
      "type": enum (ProductType),
      "engine": enum (Engine),
      "version": string,
      "minorVersion": string
    }  
  
Fields  
---  
`type` |  `enum (`ProductType`)` Optional. Type of specific database product. It could be CloudSQL, AlloyDB etc..  
`engine` |  `enum (`Engine`)` Optional. The specific engine that the underlying database is running.  
`version` |  `string` Optional. Version of the underlying database engine. Example values: For MySQL, it could be "8.0", "5.7" etc. For Postgres, it could be "14", "15" etc.  
`minorVersion` |  `string` Optional. Minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
### BackupRunInfo

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "state": enum (State),
      "errorMessage": string,
      "operationErrorType": enum (OperationErrorType),
      "subResource": {
        object ([SubResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SubResource))
      }
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the backup operation started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the backup operation completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`State`)` Output only. The state of this run.  
`errorMessage` |  `string` Additional information about the error encountered.  
`operationErrorType` |  `enum (`OperationErrorType`)` Optional. OperationErrorType to expose specific error when backup operation of database resource failed, that is state is FAILED.  
`subResource` |  `object (`[SubResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SubResource)`)` Optional. Sub resource details associated with the backup run.  
  
### SCCInfo

JSON representation  
---  
      
    
    {
      "signal": string,
      "category": string,
      "regulatoryStandards": [
        {
          object ([RegulatoryStandard](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.RegulatoryStandard))
        }
      ],
      "externalUri": string
    }  
  
Fields  
---  
`signal` |  `string` Name of the signal.  
`category` |  `string` Name by which SCC calls this signal.  
`regulatoryStandards[]` |  `object (`[RegulatoryStandard](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.RegulatoryStandard)`)` Compliances that are associated with the signal.  
`externalUri` |  `string` External URI which points to a SCC page associated with the signal.  
  
### RegulatoryStandard

JSON representation  
---  
      
    
    {
      "standard": string,
      "version": string
    }  
  
Fields  
---  
`standard` |  `string` Name of industry compliance standards, such as such as CIS, PCI, and OWASP.  
`version` |  `string` Version of the standard or benchmark, for example, 1.1.  
  
### RecommendationInfo

JSON representation  
---  
      
    
    {
      "recommender": string,
      "recommenderId": string,
      "recommenderSubtype": string
    }  
  
Fields  
---  
`recommender` |  `string` Name of recommendation. Examples: organizations/1234/locations/us-central1/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations/9876  
`recommenderId` |  `string` ID of recommender. Examples: "google.cloudsql.instance.PerformanceRecommender"  
`recommenderSubtype` |  `string` Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to `content` or `primary_impact.category` are introduced. See the Recommenders section to see a list of subtypes for a given Recommender.Examples: For recommender = "google.cloudsql.instance.PerformanceRecommender", recommender_subtype can be "MYSQL_HIGH_NUMBER_OF_OPEN_TABLES_BEST_PRACTICE"/"POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION_BEST_PRACTICE"  
  
### AutomatedBackupPolicyInfo

JSON representation  
---  
      
    
    {
      "subResource": {
        object ([SubResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SubResource))
      },
      "isEnabled": boolean
    }  
  
Fields  
---  
`subResource` |  `object (`[SubResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SubResource)`)` Optional. Sub resource details associated with the signal.  
`isEnabled` |  `boolean` Is automated policy enabled.  
  
### DeletionProtectionInfo

JSON representation  
---  
      
    
    {
      "subResource": {
        object ([SubResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SubResource))
      },
      "deletionProtectionEnabled": boolean
    }  
  
Fields  
---  
`subResource` |  `object (`[SubResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SubResource)`)` Optional. Sub resource details associated with the signal.  
`deletionProtectionEnabled` |  `boolean` Is deletion protection enabled.  
  
### ResourceSuspensionInfo

JSON representation  
---  
      
    
    {
      "resourceSuspended": boolean,
      "suspensionReason": enum (SuspensionReason)
    }  
  
Fields  
---  
`resourceSuspended` |  `boolean` Is resource suspended.  
`suspensionReason` |  `enum (`SuspensionReason`)` Suspension reason for the resource.  
  
### InefficientQueryInfo

JSON representation  
---  
      
    
    {
      "database": string,
      "table": string,
      "sqlIndexStatement": string,
      "storageCostBytes": string,
      "impactedQueriesCount": string
    }  
  
Fields  
---  
`database` |  `string` Name of the database where index is required. For example, "db1", which is the name of the database present in the instance.  
`table` |  `string` Name of the table where index is required  
`sqlIndexStatement` |  `string` SQL statement of the index. Based on the ddl type, this will be either CREATE INDEX or DROP INDEX.  
`storageCostBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Cost of additional disk usage in bytes  
`impactedQueriesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Count of queries to be impacted if index is applied  
  
### OutdatedMinorVersionInfo

JSON representation  
---  
      
    
    {
      "recommendedMinorVersion": string
    }  
  
Fields  
---  
`recommendedMinorVersion` |  `string` Recommended minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
### MaintenanceRecommendationInfo

JSON representation  
---  
      
    
    {
      "resourceMaintenanceSchedules": [
        {
          object ([ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.ResourceMaintenanceSchedule))
        }
      ]
    }  
  
Fields  
---  
`resourceMaintenanceSchedules[]` |  `object (`[ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.ResourceMaintenanceSchedule)`)` Optional. List of recommended maintenance schedules for the database resource.  
  
### ResourceMaintenanceSchedule

JSON representation  
---  
      
    
    {
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.TimeOfDay))
      },
      "day": enum (google.type.DayOfWeek),
      "phase": enum (Phase)
    }  
  
Fields  
---  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.TimeOfDay)`)` Optional. Preferred time to start the maintenance operation on the specified day.  
`day` |  `enum (`google.type.DayOfWeek`)` Optional. Preferred day of the week for maintenance, e.g. MONDAY, TUESDAY, etc.  
`phase` |  `enum (`Phase`)` Optional. Phase of the maintenance window. This is to capture order of maintenance. For example, for Cloud SQL resources, this can be used to capture if the maintenance window is in Week1, Week2, Week5, etc. Non production resources are usually part of early phase. For more details, refer to Cloud SQL resources - <https://cloud.google.com/sql/docs/mysql/maintenance>  
  
### TimeOfDay

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
### DatabaseResource

JSON representation  
---  
      
    
    {
      "childResources": [
        {
          object ([DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.DatabaseResource))
        }
      ],
      "fullResourceName": string,
      "container": string,
      "product": {
        object ([Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product))
      },
      "location": string,
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Label))
        }
      ],
      "tags": [
        {
          object ([Tag](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Tag))
        }
      ],
      "resourceType": string,
      "subResourceType": enum (SubResourceType),
      "machineConfig": {
        object ([MachineConfig](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MachineConfig))
      },
      "signalGroups": [
        {
          object ([SignalGroup](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SignalGroup))
        }
      ],
      "metrics": {
        object ([Metrics](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Metrics))
      },
      "resourceCategory": enum (ResourceCategory),
      "resourceName": string,
      "backupdrConfig": {
        object ([BackupDRConfig](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.BackupDRConfig))
      },
      "edition": enum (Edition),
      "maintenanceInfo": {
        object ([MaintenanceInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MaintenanceInfo))
      }
    }  
  
Fields  
---  
`childResources[]` |  `object (`[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.DatabaseResource)`)` List of children associated with a database group.  
`fullResourceName` |  `string` The full resource name, based on CAIS resource name format <https://cloud.google.com/asset-inventory/docs/resource-name-format>Example:`//cloudsql.googleapis.com/projects/project-number/instances/mysql-1` `//cloudsql.googleapis.com/projects/project-number/instances/postgres-1` `//spanner.googleapis.com/projects/project-number/instances/spanner-instance-1` `//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1` `//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1/instances/i1`  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
`product` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products#Output.Schema.Product)`)` The product this resource represents.  
`location` |  `string` The location of the resources. It supports returning only regional locations in Google Cloud. These are of the form: "us-central1", "us-east1", etc. See <https://cloud.google.com/about/locations> for a list of such regions.  
`labels[]` |  `object (`[Label](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Label)`)` Labels applied on the resource. The requirements for labels assigned to Google Cloud resources may be found at <https://cloud.google.com/resource-manager/docs/labels-overview#requirements>  
`tags[]` |  `object (`[Tag](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Tag)`)` Tags applied on the resource. The requirements for tags assigned to Google Cloud resources may be found at <https://cloud.google.com/resource-manager/docs/tags/tags-overview>  
`resourceType` |  `string` The type of resource defined according to the pattern: {Service Name}/{Type}. Ex: sqladmin.googleapis.com/Instance alloydb.googleapis.com/Cluster alloydb.googleapis.com/Instance spanner.googleapis.com/Instance  
`subResourceType` |  `enum (`SubResourceType`)` Subtype of the resource specified at creation time.  
`machineConfig` |  `object (`[MachineConfig](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MachineConfig)`)` Machine configuration like CPU, memory, etc for the resource.  
`signalGroups[]` |  `object (`[SignalGroup](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.SignalGroup)`)` The list of signal groups and count of issues related to the resource. Only those signals which have been requested would be included.  
`metrics` |  `object (`[Metrics](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Metrics)`)` Observable metrics for the resource e.g. CPU utilization, memory utilization, etc.  
`resourceCategory` |  `enum (`ResourceCategory`)` The category of the resource.  
`resourceName` |  `string` The name of the resource(The last part of the full resource name). Example: For full resource name - `//cloudsql.googleapis.com/projects/project-number/instances/mysql-1`, resource name - `mysql-1` For full resource name - `//cloudsql.googleapis.com/projects/project-number/instances/postgres-1` , resource name - `postgres-1` Note: In some cases, there might be more than one resource with the same resource name.  
`backupdrConfig` |  `object (`[BackupDRConfig](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.BackupDRConfig)`)` Optional. Backup and disaster recovery details for the resource.  
`edition` |  `enum (`Edition`)` The edition of the resource.  
`maintenanceInfo` |  `object (`[MaintenanceInfo](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MaintenanceInfo)`)` Optional. The maintenance information of the resource.  
  
### Label

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string,
      "source": string
    }  
  
Fields  
---  
`key` |  `string` The key part of the label.  
`value` |  `string` The value part of the label.  
`source` |  `string` The source of the Label. Source is empty if the label is directly attached to the resource and not inherited.  
  
### Tag

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string,
      "source": string,
      "inherited": boolean
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string` The value part of the tag.  
`source` |  `string` The source of the tag. According to <https://cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels>, tags can be created only at the project or organization level. Tags can be inherited from different project as well not just the current project where the database resource is present. Format: "projects/{PROJECT_ID}", "projects/{PROJECT_NUMBER}", "organizations/{ORGANIZATION_ID}"  
`inherited` |  `boolean` Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource's ancestors, inherited will be true. If false, then the tag value is directly attached to the resource.  
  
### MachineConfig

JSON representation  
---  
      
    
    {
      "memorySizeBytes": string,
    
      // Union field _shard_count can be only one of the following:
      "shardCount": integer
      // End of list of possible types for union field _shard_count.
    
      // Union field _vcpu_count can be only one of the following:
      "vcpuCount": number
      // End of list of possible types for union field _vcpu_count.
    }  
  
Fields  
---  
`memorySizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Memory size in bytes.  
Union field `_shard_count`.`_shard_count` can be only one of the following:  
`shardCount` |  `integer` Optional. The number of Shards (if applicable).  
Union field `_vcpu_count`.`_vcpu_count` can be only one of the following:  
`vcpuCount` |  `number` Optional. The number of vCPUs (if applicable).  
  
### SignalGroup

JSON representation  
---  
      
    
    {
      "displayName": string,
      "issueCount": integer,
      "signals": [
        {
          object ([Signal](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Signal))
        }
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Title of a signal group corresponding to the request.  
`issueCount` |  `integer` When applied to a DatabaseResource represents count of issues associated with the resource. A signal is an issue when its SignalStatus field is set to SIGNAL_STATUS_ISSUE.  
`signals[]` |  `object (`[Signal](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.Signal)`)` List of signals present in the group and associated with the resource.Only applies to a DatabaseResource.  
  
### Metrics

JSON representation  
---  
      
    
    {
    
      // Union field _p99_cpu_utilization can be only one of the following:
      "p99CpuUtilization": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _p99_cpu_utilization.
    
      // Union field _p95_cpu_utilization can be only one of the following:
      "p95CpuUtilization": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _p95_cpu_utilization.
    
      // Union field _current_storage_used_bytes can be only one of the following:
      "currentStorageUsedBytes": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _current_storage_used_bytes.
    
      // Union field _peak_storage_utilization can be only one of the following:
      "peakStorageUtilization": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _peak_storage_utilization.
    
      // Union field _peak_memory_utilization can be only one of the following:
      "peakMemoryUtilization": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _peak_memory_utilization.
    
      // Union field _peak_number_connections can be only one of the following:
      "peakNumberConnections": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _peak_number_connections.
    
      // Union field _node_count can be only one of the following:
      "nodeCount": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _node_count.
    
      // Union field _processing_unit_count can be only one of the following:
      "processingUnitCount": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _processing_unit_count.
    
      // Union field _current_memory_used_bytes can be only one of the following:
      "currentMemoryUsedBytes": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData))
      }
      // End of list of possible types for union field _current_memory_used_bytes.
    }  
  
Fields  
---  
Union field `_p99_cpu_utilization`.`_p99_cpu_utilization` can be only one of the following:  
`p99CpuUtilization` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` P99 CPU utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
Union field `_p95_cpu_utilization`.`_p95_cpu_utilization` can be only one of the following:  
`p95CpuUtilization` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` P95 CPU utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
Union field `_current_storage_used_bytes`.`_current_storage_used_bytes` can be only one of the following:  
`currentStorageUsedBytes` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` Current storage used by the resource in bytes.  
Union field `_peak_storage_utilization`.`_peak_storage_utilization` can be only one of the following:  
`peakStorageUtilization` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` Peak storage utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
Union field `_peak_memory_utilization`.`_peak_memory_utilization` can be only one of the following:  
`peakMemoryUtilization` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` Peak memory utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
Union field `_peak_number_connections`.`_peak_number_connections` can be only one of the following:  
`peakNumberConnections` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` Peak number of connections observed for the resource. The value is a positive integer.  
Union field `_node_count`.`_node_count` can be only one of the following:  
`nodeCount` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` Number of nodes in instance for spanner or bigtable.  
Union field `_processing_unit_count`.`_processing_unit_count` can be only one of the following:  
`processingUnitCount` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` Number of processing units in spanner.  
Union field `_current_memory_used_bytes`.`_current_memory_used_bytes` can be only one of the following:  
`currentMemoryUsedBytes` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.MetricData)`)` Current memory used by the resource in bytes.  
  
### MetricData

JSON representation  
---  
      
    
    {
      "value": {
        object ([TypedValue](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.TypedValue))
      },
      "observationTime": string
    }  
  
Fields  
---  
`value` |  `object (`[TypedValue](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.TypedValue)`)` The value associated with the metric.  
`observationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the metric was observed in the metric source service.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### TypedValue

JSON representation  
---  
      
    
    {
    
      // Union field value can be only one of the following:
      "doubleValue": number,
      "int64Value": string
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
Union field `value`. The data type of metric value would be chosen based on the metric type. `value` can be only one of the following:  
`doubleValue` |  `number` The value of the metric as double.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The value of the metric as int.  
  
### BackupDRConfig

JSON representation  
---  
      
    
    {
    
      // Union field _backupdr_managed can be only one of the following:
      "backupdrManaged": boolean
      // End of list of possible types for union field _backupdr_managed.
    }  
  
Fields  
---  
Union field `_backupdr_managed`.`_backupdr_managed` can be only one of the following:  
`backupdrManaged` |  `boolean` Indicates if the resource is managed by BackupDR.  
  
### MaintenanceInfo

JSON representation  
---  
      
    
    {
      "maintenanceSchedule": {
        object ([ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.ResourceMaintenanceSchedule))
      },
      "denyMaintenanceSchedules": [
        {
          object ([ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.ResourceMaintenanceDenySchedule))
        }
      ],
      "maintenanceVersion": string
    }  
  
Fields  
---  
`maintenanceSchedule` |  `object (`[ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.ResourceMaintenanceSchedule)`)` Optional. Maintenance window for the database resource.  
`denyMaintenanceSchedules[]` |  `object (`[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.ResourceMaintenanceDenySchedule)`)` Optional. List of Deny maintenance period for the database resource.  
`maintenanceVersion` |  `string` Output only. Current Maintenance version of the database resource. Example: "MYSQL_8_0_41.R20250531.01_15"  
  
### ResourceMaintenanceDenySchedule

JSON representation  
---  
      
    
    {
      "startDate": {
        object ([Date](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Input.Schema.Date))
      },
      "endDate": {
        object ([Date](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Input.Schema.Date))
      },
      "time": {
        object ([TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.TimeOfDay))
      }
    }  
  
Fields  
---  
`startDate` |  `object (`[Date](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Input.Schema.Date)`)` Optional. The start date of the deny maintenance period.  
`endDate` |  `object (`[Date](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory#Input.Schema.Date)`)` Optional. Deny period end date.  
`time` |  `object (`[TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues#Output.Schema.TimeOfDay)`)` Optional. Time in UTC when the deny period starts on start_date and ends on end_date.  
  
### Date

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
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
