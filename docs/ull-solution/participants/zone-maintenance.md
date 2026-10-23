---
url: https://docs.cloud.google.com/ull-solution/participants/zone-maintenance/
title: Maintenance in ULL Solution private zones \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:33.244178+00:00
---

# Maintenance in ULL Solution private zones  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/zone-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Maintenance in ULL Solution private zones

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page provides an overview of the zone maintenance process for private zones used by Google Cloud Ultra Low Latency (ULL) Solution.

## Overview of the dual-zone design for ULL Solution

ULL Solution uses a dual-zone design to help ensure that regular maintenance and testing can be performed without interrupting market trading. To support this design, the private zones used for ULL Solution have unique availability and maintenance properties compared to public zones in Google Cloud. For details, see the following:

  * **Two private zones in a given region** : A given region used by ULL Solution has two private zones. For example, the `us-south1` region has the private zones `us-south1-d` and `us-south1-e`.
  * **Only one zone supports production workloads at a given time** : See the following: 
    * The _production zone_ is the active environment for live trading. To help maintain a stable environment in this zone, Google doesn't perform maintenance or updates.
    * The _maintenance zone_ is the inactive environment in which Google performs updates and repairs, and exchange operators and participants can also perform updates and testing. The maintenance process includes unique windows that determine when Google performs updates and repairs, as well as when customers should perform recommended actions.
  * **Weekly zone transition** : The role of each zone switches on a weekly schedule that you can view by using gcloud or the API. Once per week, the existing production zone switches to the maintenance zone, and the maintenance zone switches to the production zone.



### Requirements for exchange operators and exchange participants

Exchange operators and exchange participants must ensure that they run production workloads in the production zone, and perform updates and testing in the maintenance zone according to the recommended actions for each maintenance window.

For more information, see the following sections:

  * To understand how maintenance progresses in a given week in the maintenance zone, see Zone maintenance windows.
  * To view current and upcoming maintenance for a given zone, including specific start and end times, see View zone maintenance status.



## Zone maintenance windows

For the zone that is designated as the maintenance zone for a given week, the following sequential maintenance windows occur. For the specific start and end times of each window, see View zone maintenance status. For more details about each window, see the following Maintenance window details section.

Day | Applicable maintenance windows | Recommended actions for exchange operators and participants  
---|---|---  
Days 1 and 2 | 

  * Disruptive upgrade window

|  Avoid using the infrastructure as operations might fail.   
Days 3, 4, 5 | 

  * Customer maintenance window

|  Provision instances, update software applications, and update infrastructure configurations. Perform functional testing.   
Days 6 and 7 | 

  * Stable window

|  Conduct performance validation and stress testing.   
End of day 7 | 

  * Zone transition window

|  Migrate production workloads.   
  
### Maintenance window details

The following table describes each maintenance window.

Maintenance window | Description  
---|---  
Disruptive upgrade window |  This window lasts for the first 48 hours. Google performs updates that are likely to cause disruptions to instances and services. Using the infrastructure in the zone isn't recommended. While APIs might be available, operations are unstable.  
Customer maintenance window |  This window begins after the completion of the disruptive upgrade window and lasts for 72 hours. Exchange operators and exchange participants can provision instances, maintain and update the software running on instances, update infrastructure configurations, and perform functional testing.  
Stable window |  This window begins after the completion of the customer maintenance window and lasts for about 46 hours. During this window, the zone is stable and exchange operators and exchange participants can conduct performance validation and stress testing to prepare for active trading in the zone.  
Transition window |  This window begins after the completion of the stable window and lasts for about 2 hours. The state of each zone is changing. The existing production zone is switching to the maintenance zone. The existing maintenance zone is switching to the production zone. During this window, Google performs preliminary, non-disruptive tasks.  
  
## Maintenance experience for U4 instances

The maintenance experience for U4 instances depends on the machine type:

  * **ULL Compute Engine instances (U4P and U4C)** : ULL instances have a unique maintenance experience compared to other instance types in Google Cloud. These instances are maintained according to the maintenance schedule for ULL Solution private zones. The duration of host maintenance aligns with the disruptive upgrade window of the zone.
  * **Non-ULL Compute Engine instances (U4S)** : Non-ULL instances have a maintenance experience that is generally consistent with other instance types in Google Cloud as described in [Transparent maintenance](https://docs.cloud.google.com/compute/docs/regions-zones#maintenance). However, [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) of non-ULL instances due to upgrades isn't supported in the production zone.



For general information about maintenance of Compute Engine instances, see [About host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).

The following table describes the host maintenance properties for U4 machine types.

Machine type | Typical scheduled maintenance event frequency | [Maintenance behavior](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenance_behaviors) | [Advanced notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) | [On-demand maintenance](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)  
---|---|---|---|---  
U4P and U4C | 14 days | Terminate | 14 days | No  
U4S | 28 days | Live migrate | 7 days | Yes  
  
## View zone maintenance status

You can view the current and upcoming maintenance details for a zone, including specific start and end times of each maintenance window, by using either of the following options.

### Enable APIs

If you haven't already, enable the following APIs.

###  Console 

Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

###  gcloud 

Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable compute.googleapis.com

### View maintenance details

  * **gcloud** : the [`gcloud compute zones describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/describe)
        
        gcloud compute zones describe ZONE --project PROJECT
        

  * **API** : the [`zones.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zones/get)
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE
        




The information about maintenance is presented in the response in a section similar to the following example:
    
    
    "upcomingMaintenances": [
          {
            "type": "PRIVATE_ZONE_MAINTENANCE",
            "subType": "MAINTENANCE_TYPE_DISRUPTIVE_UPGRADE",
            "targetResource": "projects/my-project/zones/us-south1-d",
            "windowStartTime": "2025-08-26T15:00:00Z",
            "windowEndTime": "2025-08-27T15:00:00Z"
          }
          // Additional maintenance windows ...
        ]
    

While Google Cloud also provides an instance-level maintenance status as described in [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event), only the zone-level output provides the full maintenance schedule and window details for ULL Solution private zones as described in the following Field descriptions section.

### Limitations

Maintenance status isn't available for `list` operations with gcloud or the API, such as by using the [`zones.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zones/list) or the [`regionZones.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionZones/list). You must use the preceding `describe` command or `get` method to view maintenance status.

### Field descriptions

The following sections describe the unique fields available for ULL Solution private zones when describing a zone. The following fields aren't available for public zones in Google Cloud.

#### `resourceStatus.upcomingMaintenances[]`

An array of objects, where each object represents a scheduled maintenance window. Includes all ongoing and future maintenance windows scheduled within the next 7 days.

Field | Type | Description  
---|---|---  
`type` | enum | The type of maintenance. See type enum.  
`subType` | enum | The subtype of maintenance. See subType enum.  
`targetResource` | string | The full resource name of the zone undergoing maintenance (such as `projects/my-project/zones/us-south1-d`).  
`windowStartTime` | string | Start time of the maintenance window in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC "Zulu" format (such as `2025-08-26T15:00:00Z`).  
`windowEndTime` | string | End time of the maintenance window in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) UTC "Zulu" format (such as `2025-08-27T15:00:00Z`).  
  
#### `type`

Value | Description  
---|---  
`MAINTENANCE_TYPE_UNSPECIFIED` | Default value.  
`PRIVATE_ZONE_MAINTENANCE` | Maintenance that applies to a ULL Solution private zone.  
  
#### `subType`

Value | Description  
---|---  
`MAINTENANCE_SUBTYPE_UNSPECIFIED` | Default value.  
`MAINTENANCE_TYPE_DISRUPTIVE_UPGRADE` | Corresponds to the _disruptive upgrade window_ described in Zone maintenance window details.  
`MAINTENANCE_TYPE_CUSTOMER_MAINTENANCE` | Corresponds to the _customer maintenance window_ described in Zone maintenance window details.  
`MAINTENANCE_TYPE_STABLE` | Corresponds to the _stable window_ described in Zone maintenance window details.  
`MAINTENANCE_TYPE_TRANSITION` | Corresponds to the _transition window_ described in Zone maintenance window details.  
  
#### `warnings[]`

An array of warning objects providing additional information.

Field | Type | Description  
---|---|---  
`code` | enum | A warning code. See warning.code enum.  
`message` | string | A description of the warning.  
`data` | array | Metadata about the warning in key/value pairs (such as `[{"key": "scope", "value": "zones/us-east1-d"}]`).  
  
#### `warning.code`

Value | Description  
---|---  
`WARNING_CODE_UNSPECIFIED` | Default value.  
`UPCOMING_MAINTENANCES_UNAVAILABLE` | Upcoming maintenance window information can't be retrieved. Try again later.  
  
## What's next

  * [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
