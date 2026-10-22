---
url: https://docs.cloud.google.com/compute/docs/logging/activity-logs/
title: Viewing activity logs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:44.973541+00:00
---

# Viewing activity logs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/logging/activity-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Viewing activity logs Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine activity logs are deprecated. Instead, use [audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging). For more information, see [Migrating from activity logs to audit logs](https://docs.cloud.google.com/compute/docs/logging/migrating-from-activity-logs-to-audit-logs).

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Compute Engine activity logs aren't the same thing as [audit logs](https://docs.cloud.google.com/logging/docs/audit). Audit logs contain the same information as legacy activity logs and more. We recommend you use audit logs instead of activity logs. If you are already using activity logs, read [Migrating from activity logs to audit logs](https://docs.cloud.google.com/compute/docs/logging/migrating-from-activity-logs-to-audit-logs).

Compute Engine provides activity logs that let you track certain events that affect your project, such as API calls and system events. Specifically, activity logs provide information about:

  * Compute Engine API calls: `GCE_API_CALL` events are [API calls](https://docs.cloud.google.com/compute/docs/reference/latest) that change the state of a resource. For example, API calls to create a disk, update instance metadata, create an instance group, change a machine type, are recorded in activity logs. API calls that do not update a resource, such as `get` and `list` requests aren't recorded.
  * Operation logs: `GCE_OPERATION_DONE` events are logged when an API call changes the state of a resource finishes, Compute Engine returns a completed operation event that is recorded in your activity logs.
  * System logs: `GCE_SYSTEM_EVENT` events are logged when Compute Engine performs a system event, it is recorded in activity logs. For example, a transparent maintenance event would be logged as a system event.



For example, with an API event, an activity log provides details such as the start and end time of an API request, the specifics of the request body, the authorized user who made the API request, and the request endpoint. You can download activity logs to search for specific API requests, or to review system events initiated by Compute Engine.

Activity logs do not provide billing or usage information about a project, such as how long a virtual machine instance has been running or how much it costs. For billing logs, see the [billing export](https://support.google.com/cloud/answer/4524336) feature. For usage logs, see [Viewing usage reports](https://docs.cloud.google.com/compute/docs/usage-export).

Activity logs are provided as part of the Cloud Logging service. For more information about Logging in general, read the [Cloud Logging](https://docs.cloud.google.com/logging/docs) documentation.

## Before you begin

  * Familiar with [Cloud Logging](https://docs.cloud.google.com/logging).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `logging.logServiceIndexes.list` on the project
  * `logging.logServices.list` on the project



## Viewing logs

Activity logging is enabled by default for all Compute Engine projects.

You can see your project's activity logs through the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) in the [Google Cloud console](https://console.cloud.google.com/):

  1. In the Google Cloud console, go to the **Logging** page. 

[Go to the Logging page](https://console.cloud.google.com/logs)

  2. When in the Logs Explorer, select and filter your resource type from the first drop-down list.
  3. From the **All logs** drop-down list, select **compute.googleapis.com/activity_log** to see Compute Engine activity logs.



## Routing logs

To learn how to export activity logs, read [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export) in the Cloud Logging documentation.

## Identifying log files

When you export logs into Cloud Storage, the log files are stored in the structure described by the [Log entry objects](https://docs.cloud.google.com/logging/docs/export/using_exported_logs#the_logentry_type) documentation.

Compute Engine log files are stored with the following directory structure:
    
    
    <bucket>/compute.googleapis.com/activity_log/<year>/<month>/<day>
    

The following is an example log filename stored in a Cloud Storage bucket named `my-bucket`:
    
    
    my-bucket/compute.googleapis.com/activity_log/2014/10/31/20:00:00_20:59:59_S0.json

In BigQuery, activity logs are stored in a set of tables, one table for each log type and day, and the tables are named using the following format:
    
    
    <dataset>.compute_googleapis_com_activity_log_YYYYMMDD

For information about how to query activity logs in BigQuery, see [Log entries in BigQuery](https://docs.cloud.google.com/logging/docs/exported_logs#log_entries_in_google_bigquery).

## Reading activity logs

**Note:** Compute Engine recently updated the format of activity logs to use [protobuf format](https://github.com/google/protobuf). This changes the format of your logs slightly, but the content remains the same.

Activity logs are structured as described in the [LogEntry type](https://docs.cloud.google.com/logging/docs/exported_logs#the_logentry_type) documentation.

Compute Engine activity logs have:

  * `compute.googleapis.com/activity_log` as value of the `log` field
  * [`metadata`](https://docs.cloud.google.com/logging/docs/api/ref/rest/v1beta3/projects.logs.entries/write#LogEntryMetadata), which describes common information such as timestamp
  * `structPayload`, which contains the specific contents of the log entry



You can get more details about the common fields provided with every log entry from the [LogEntry](https://docs.cloud.google.com/logging/docs/export/using_exported_logs#the_logentry_type) description, but the payload contents of activity log entries are specific to Compute Engine and are described below.

### Payload contents

The contents of a log entry are provided in JSON object format, and are stored in the `structPayload` field. The `structPayload` field contains the following information:

Field | Type | Description | `actor` | string | Email of user or service account performing the operation. This is the same as the `user_id`.  
---|---|---  
`error` | string | Provides any error details if an error occurred during this event. This is omitted if there were no errors. Errors usually prevent a request from completing successfully. You can use this field to debug a failed request.  
`event_subtype` | string | Describes the specific subtype as an API method. For example, a request to [insert a new instance](https://docs.cloud.google.com/compute/docs/reference/latest/instances/insert) appears as `compute.instances.insert`, and a request to [delete an Address resource](https://docs.cloud.google.com/compute/docs/reference/latest/addresses/delete) appears as `compute.addresses.delete`. See the [API reference](https://docs.cloud.google.com/compute/docs/reference/latest) for a comprehensive list of API methods.  
`event_timestamp_us` | timestamp | The timestamp, in microseconds, of the logged event since standard epoch. This is the same as `metadata.timestamp`.  
`event_type` | string | Describes the general event type. This can be one of the following values:

  * `GCE_API_CALL`. Indicates a REST API call that updated a resource.
  * `GCE_OPERATION_DONE`. After an API request completes, whether successful or not, this event type is logged. 
  * `GCE_SYSTEM_EVENT`. A system event initiated by Compute Engine.

  
`info` | string | An optional field with additional information, if applicable. This field is omitted if there is no additional information to show.  
`operation` | string | When an API request is made to update or change any resources, a corresponding operation object is created to track the request to completion. This property describes the operation object for this event, providing information such as the operation name, the zone or region of the operation, and the operation ID. Operations can be a [zone operation](https://docs.cloud.google.com/compute/docs/reference/latest/zoneOperations), a [region operation](https://docs.cloud.google.com/compute/docs/reference/latest/regionOperations), or a [global operation](https://docs.cloud.google.com/compute/docs/reference/latest/globalOperations), depending on the resource the operation is modifying.  
`request` | JSON | Contains the original API request body. Show Example Request
    
    
    "request": {
      "url": "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances\",
      "body": "{
        \"canIpForward\":"false",
        \"description\":\"\",
        \"disks\":[{
          \"autoDelete\":true,
          \"boot\":true,
          \"deviceName\":\"example-instance\",
          \"initializeParams\":{
            \"diskSizeGb\":\"10\",
            \"diskType\":\"https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/diskTypes/pd-standard\",
            \"sourceImage\":\"https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-8-jessie-v20150818\"
          },
          \"mode\":\"READ_WRITE\",
          \"type\":\"PERSISTENT\"
        }],
        \"machineType\":\"https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/machineTypes/n1-standard-1\",
        \"metadata\":{
          \"items\":[]
        },
        \"name\":\"example-instance\",
        \"networkInterfaces\":[{
            \"accessConfigs\":[{
              \"name\":\"External NAT\",
              \"type\":\"ONE_TO_ONE_NAT\"
            }],
            \"network\":\"https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default\"
          }],
        \"scheduling\":{
          \"automaticRestart\":true,
          \"onHostMaintenance\":\"MIGRATE\",
          \"preemptible\":false
        },
        \"serviceAccounts\":[{
          \"email\":\"default\",
          \"scopes\":[
            \"https://www.googleapis.com/auth/devstorage.read_only\",
            \"https://www.googleapis.com/auth/logging.write\"
          ]
        }],
        \"tags\":{
          \"items\":[]
        },
        \"zone\":\"https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f\"
      }"
    }  
  
`resource` | JSON | Describes the particular resource that is being modified by this event. For example, a virtual machine (VM) instance is considered a resource and an example resource property for a VM looks like the following: 
    
    
    "resource": {
      "type": "instance",
      "name": "example-instance",
      "id": "0",
      "zone": "us-central1-f"
    }

A list of resource types is described in detail in the [API reference](https://docs.cloud.google.com/compute/docs/reference/latest). **Note:** If an action affects multiple resources, there may be multiple log entries with the same `trace_id`.   
`trace_id` | string | A system-provided trace ID used to group related logs that are triggered by a single action. For example: 
    
    
    trace_id: "operation-1442436581415-51fe3700bd85a-7fd317e3-f1a3555e"  
  
`user_agent` | string | Describes the client that performed this request. For example, if you used the Cloud Client Libraries for Java to make a request, the user agent would be `Google-API-Java-Client`.  
`version` | string | The current log format version indicates the Compute Engine log schema. The current version is 1.2. **Note:** The Compute Engine API versioning is separate from the log format versioning.  
`warning` | string | Provides any warning details if any warnings occurred during this event. A warning is informational and does not affect the request, unlike errors.  
  
## Sample log entry

For example, a sample log entry describing an API request to create a VM looks like the following:
    
    
    {
      "log": "compute.googleapis.com/activity_log",
      "insertId": "2015-09-16|13:49:42.532185-07|10.106.9.208|335899593",
      "metadata": {
        "severity": "INFO",
        "projectId": "835469197146",
        "serviceName": "compute.googleapis.com",
        "zone": "us-central1-f",
        "labels":{
          "compute.googleapis.com/resource_id":"0",
          "compute.googleapis.com/resource_name":"example-instance",
          "compute.googleapis.com/resource_type":"instance",
          "compute.googleapis.com/resource_zone":"us-central1-f"
        },
        "timestamp": "2015-09-16T20:49:42.423637Z"
      },
      "structPayload": {
        "version": "1.2",
        "trace_id": "operation-1442436581415-51fe3700bd85a-7fd317e3-f1a3555e",
        "event_timestamp_us": "1442436582423637",
        "event_type": "GCE_API_CALL",
        "event_subtype": "compute.instances.insert",
        "resource": {
          "type": "instance",
          "name": "example-instance",
          "id": "0",
          "zone": "us-central1-f"
        },
        "actor": {
          "user": "user@example.com"
        },
        "ip_address": "",
        "user_agent": "apitools-client/1.0",
        "request": {
          "url": "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances",
          "body": "{
            \"canIpForward\":false,
            \"description\":\"\",
            \"disks\":[{
              \"autoDelete\":true,
              \"boot\":true,
              \"deviceName\":\"example-instance\",
              \"initializeParams\":{
                \"diskSizeGb\":\"10\",
                \"diskType\":\"https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/diskTypes/pd-standard\",
                \"sourceImage\":\"https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-8-jessie-v20150818\"
              },
              \"mode\":\"READ_WRITE\",
              \"type\":\"PERSISTENT\"
            }],
            \"machineType\":\"https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/machineTypes/n1-standard-1\",
            \"metadata\":{
              \"items\":[]
            },
            \"name\":\"example-instance\",
            \"networkInterfaces\":[{
                \"accessConfigs\":[{
                  \"name\":\"External NAT\",
                  \"type\":\"ONE_TO_ONE_NAT\"
    
                }],
                \"network\":\"https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default\"
              }],
            \"scheduling\":{
              \"automaticRestart\":true,
              \"onHostMaintenance\":\"MIGRATE\",
              \"preemptible\":false
            },
            \"serviceAccounts\":[{
              \"email\":\"default\",
              \"scopes\":[
                \"https://www.googleapis.com/auth/devstorage.read_only\",
                \"https://www.googleapis.com/auth/logging.write\"
              ]
            }],
            \"tags\":{
              \"items\":[]
            },
            \"zone\":\"https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f\"
          }"
        },
        "operation": {
          "type": "operation",
          "name": "operation-1442436581415-51fe3700bd85a-7fd317e3-f1a3555e",
          "id": "291347737657178184",
          "zone": "us-central1-f"
        }
      }
    }

## Deprecated activity log entries

The following activity log entries will be discontinued, with no replacement, on June 1, 2020:

Monitored Resource Type | Event SubType  
---|---  
`gce_backend_service` | `BackendServiceConfigProgramming`  
`gce_instance` | `RE_ENCRYPT_SSL_CERTIFICATE_FLOW`  
`gce_instance` | `addFirewallRuleToSecurityPolicy`  
`gce_instance` | `attachCloudLink`  
`gce_instance` | `attachFirewallSecurityPolicy`  
`gce_instance` | `compute.instanceGroupManagers.updateHealth`  
`gce_instance` | `compute.instanceGroups.detachHealthCheck`  
`gce_instance` | `compute.instanceNetworkConfig.updateName`  
`gce_instance` | `compute.regionInstanceGroups.attachHealthCheck`  
`gce_instance` | `compute.regionInstanceGroups.detachHealthCheck`  
`gce_instance` | `createFirewallSecurityPolicy`  
`gce_instance` | `deleteFirewallSecurityPolicy`  
`gce_instance` | `detachFirewallSecurityPolicy`  
`gce_instance` | `patchFirewallRuleInSecurityPolicy`  
`gce_instance` | `removeCloudLink`  
`gce_instance` | `removeFirewallRuleFromSecurityPolicy`  
`gce_instance` | `updateFirewallSecurityPolicy`  
`gce_instance` | `updateVpnTunnel`  
`gce_instance_group` | `compute.instanceGroups.attachHealthCheck`  
`gce_instance_group` | `compute.instanceGroups.attachNetworkInterfaces`  
`gce_instance_group` | `compute.instanceGroups.detachHealthCheck`  
`gce_instance_group` | `compute.regionInstanceGroups.attachHealthCheck`  
`gce_instance_group` | `compute.regionInstanceGroups.detachHealthCheck`  
`gce_instance_template` | `compute.zoneInstanceTemplates.insert`  
`gce_network` | `compute.networks.switchLegacyToCustomMode`  
`gce_project` | `compute.projects.moveProjectNetworking`  
`gce_reserved_address` | `compute.addresses.insertDnsForwarding`  
`gce_reserved_address` | `compute.addresses.insertNatAddress`  
`gce_ssl_certificate` | `RE_ENCRYPT_SSL_CERTIFICATE_FLOW`  
`gce_ssl_certificate` | `SslCertificateAddManagedCertificateChallenge`  
`gce_ssl_certificate` | `SslCertificateProvisionManagedCertificate`  
`gce_ssl_certificate` | `SslCertificateRemoveManagedCertificateChallenge`  
`gce_subnetwork` | `compute.subnetworks.createOrUpdateVirtualSubnetwork`  
`vpn_tunnel` | `updateVpnTunnel`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
