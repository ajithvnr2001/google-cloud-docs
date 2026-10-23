---
url: https://docs.cloud.google.com/unified-maintenance/docs/log-schema/
title: Unified Maintenance log schema \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:32.587998+00:00
---

# Unified Maintenance log schema  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/log-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Guides ](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

#  Unified Maintenance log schema Stay organized with collections  Save and categorize content based on your preferences. 

To create alert policies and filter logs, you must use the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language). The following table details the fields in the Unified Maintenance resource `ResourceMaintenance`. Use these fields to write query operations for Unified Maintenance resources.

## `ResourceMaintenance` log schema

Fields |   
---|---  
[`resource`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.resource) | [`MonitoredResource`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource)  
`resource.type` | `string`  
  
Set to the [monitored resource type](https://docs.cloud.google.com/monitoring/api/resources) of the targeted resource. For example, Cloud SQL instance: `cloudsql_database`  
`resource.labels` | `map (key: string, value: string)`  
  
Labels that uniquely identify a target resource (see a list of labels in [monitored resource types](https://docs.cloud.google.com/monitoring/api/resources)).  
[`labels`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.labels) | `map (key: string, value: string)`  
  
Key-value pair used to filter logs entries. Possible keys:   
  
`maintenance.googleapis.com/new_resource_maintenance` \- set to True for the first log entry for a `ResourceMaintenance`   
  
`maintenance.googleapis.com/updated_fields` \- a list of updated `ResourceMaintenance` fields, for example:   
`"['state','maintenanceScheduledStartTime','maintenanceScheduledEndTime']"`  
`insertId` | `string`  
  
A unique identifier for the log entry.  
`timestamp` | `string (Timestamp format)`  
  
The time the event described by the log entry occurred. This time is used to compute the log entry's age and to enforce the logs retention period.  
`receiveTimestamp` | `string (Timestamp format)`  
  
The time the log entry was received by Logging.  
`jsonPayload` | `ResourceMaintenance`  
  
Payload with resource maintenance details.  
`jsonPayload.@type` | `string`  
  
Type definition of the payload.   
Equal to: `type.googleapis.com/google.cloud.maintenance.logging.v1beta.ResourceMaintenanceLog`  
`jsonPayload.name` | `string`  
  
Identifier. The name of the resourceMaintenance resource. Format: `"projects/{project}/locations/{location}/resourceMaintenance/{resource-maintenance-id}"`  
`jsonPayload.resource.resourceName` | `string`  
  
Output only. Name is the reference to the consumer resource affected by the maintenance. For available values, see [Asset names](https://docs.cloud.google.com/asset-inventory/docs/asset-names).  
`jsonPayload.resource.location` | `string`  
  
Output only. The location of the resource. Format: `us-central1`.  
`jsonPayload.resource.type` | `string`  
  
Output only. The type of the resource. For available values, see resource types of [supported services](https://docs.cloud.google.com/unified-maintenance/docs/supported-services).  
`jsonPayload.maintenance` | `object`  
  
Output only. The details of the maintenance.  
`jsonPayload.maintenance.maintenanceName` | `string`  
  
The name of the corresponding maintenance resource following the standard naming scheme: `"{maintenance-id}"`.  
`jsonPayload.maintenance.title` | `string`  
  
Output only. The title of the maintenance.  
`jsonPayload.maintenance. description` | `string`  
  
Output only. The description of the maintenance.  
`jsonPayload.state` | `enum`  
  
State of the maintenance:  
`SCHEDULED` \- Scheduled for a particular window. For disruptive maintenance it should respect maintenance policy. For example, the available windows, exclusions, and notification period.  
`STARTED` \- Maintenance is ongoing.  
`CANCELLED` \- No longer planned, typically when other maintenance (e.g. upgrade to newer version) already happened, or the user skipped the maintenance.  
`SUCCEEDED` \- Successfully completed.  
`jsonPayload.maintenanceScheduledStartTime` | `string`  
  
Output only. The time when the maintenance on the resource is `SCHEDULED`.  
Uses [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt), where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted.  
Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`jsonPayload.maintenanceScheduledEndTime` | `string`  
  
Output only. The time when the maintenance on the resource was scheduled to end.  
Uses [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt), where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted.  
Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`jsonPayload.maintenanceStartTime` | `string`  
  
Output only. The time when the resource maintenance has `STARTED`.  
Uses [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt), where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted.   
Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`jsonPayload.maintenanceEndTime` | `string`  
  
Output only. The time when the resource maintenance has `SUCCEEDED`.  
Uses [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt), where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted.  
Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`jsonPayload.maintenanceCancelTime` | `string`  
  
Output only. The time when the resource maintenance was `CANCELLED`.  
Uses [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt), where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted.  
Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`jsonPayload.userControllable` | `boolean`  
  
Output only. Indicates whether the user has some control over that maintenance, either proactively before maintenance was scheduled with maintenance policy or with reactive controls after it was scheduled (see [`controls`](https://docs.cloud.google.com/unified-maintenance/docs/reference/rest/v1beta/projects.locations.resourceMaintenances#control) field).  
`jsonPayload.controls` | `object`([`MaintenanceControl`](https://docs.cloud.google.com/unified-maintenance/docs/reference/rest/v1beta/projects.locations.resourceMaintenances#MaintenanceControl))  
  
Output only. The controls of the maintenance.  
  
## Example log fields

The following example shows a `ResourceMaintenance` resource.
    
    
    "insertId": "proj-1-us-west1-db-1-830d851d-2adf-4fb0-8f5b-1e18e16530d9",
    "timestamp": "2023-09-14T16:00:00Z",
    "receiveTimestamp": "2023-09-14T16:00:01Z",
    "logName":"projects/proj-1/logs/maintenance.googleapis.com%2Fmaintenance_events",
    "resource": {
      "type":"cloudsql_database",
      "labels": {
        "project_id": "proj-1",
        "database_id":"db-1",
        "region": "us-west1",
      },
    },
    "labels": {
      "maintenance.googleapis.com/new_resource_maintenance": "False",
      "maintenance.googleapis.com/updated_fields": "['state','maintenanceScheduledStartTime','maintenanceScheduledEndTime']"
    },
    "jsonPayload": {
      "@type": "type.googleapis.com/google.cloud.maintenance.logging.v1beta.ResourceMaintenanceLog",
      "name": "projects/proj-1/locations/us-west1/resourceMaintenances/db-1-a8307daa-5e1f-4974-b6a5-61fceb8331c0",
      "resource": {
        "resourceName": "//sqladmin.googleapis.com/projects/proj-1/instances/db-1",
        "location": "us-west1",
        "type": "sqladmin.googleapis.com/Instance"
      },
      "maintenance": {
        "maintenanceName": "830d851d-2adf-4fb0-8f5b-1e18e16530d9",
        "title": "Cloud SQL upgrade to v2",
        "description": "An upgrade to v2 release. New features... Release notes: https://..."
      },
      "state": "SCHEDULED",
      "maintenanceScheduledStartTime": "2023-09-21T16:00:00Z",
      "maintenanceScheduledEndTime": "2023-09-21T20:00:00Z"
    }

## What's next

  * Unified Maintenance [overview](https://docs.cloud.google.com/unified-maintenance/docs/overview)
  * [Set up Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/set-up-unified-maintenance)
  * Configure [alerts and notifications](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications)
  * Implement [common alert policies](https://docs.cloud.google.com/unified-maintenance/docs/implement-common-alert-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
