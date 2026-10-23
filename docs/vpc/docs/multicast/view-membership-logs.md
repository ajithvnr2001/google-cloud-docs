---
url: https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs/
title: View multicast group membership event logs \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:17.081817+00:00
---

# View multicast group membership event logs  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View multicast group membership event logs

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page provides information about the logs that are available for monitoring multicast group membership events, such as IGMP joins, and describes how to enable and view them.

You can use these logs to help you understand activity in a multicast group, such as when a multicast consumer joined and when they left, or how many multicast consumers are in a group.

## About group membership event logs

Google Cloud writes group membership event logs for multicast to [Cloud Logging](https://docs.cloud.google.com/logging/docs).

This table provides a summary of the logs that are available for each resource type, including the project that receives logs. For more information about the events that are logged and the log format, see the following sections.

Resource | Description of logs  
---|---  
Multicast group range | Group membership event logs for all multicast consumers of a group range. These logs are available only in multicast administrator projects. You can configure logging on both a global multicast group range and a zonal multicast group range activation. See Enable logging for a multicast group range.  
Multicast group consumer activation | Group membership event logs for multicast consumers in a specific multicast consumer VPC network that is activated for a group range and zone. These logs are available in projects that contain multicast consumer configurations and their corresponding multicast consumer network. If you are using Shared VPC, this is the host project. See Enable logging for a multicast group consumer activation.  
  
### Logged events

This section describes the group membership events that are logged for multicast in Cloud Logging.

When a multicast consumer sends an IGMP membership report to join a group, the resulting log messages are as follows:

  * A successful IGMP join results in two log messages: an `IGMP join request received` message followed by `IGMP consumer joined`.
  * A failed IGMP join results in two log messages: an `IGMP join request received` message followed by `IGMP join request rejected due to *`.
  * For a multicast consumer that has already joined a group successfully, a keepalive IGMP join request in a single `IGMP join request received` message.



For a full list of logged events and their descriptions, see the following table.

Event | Description  
---|---  
`IGMP join request received` | The Google Cloud control plane received the join request. This message doesn't confirm that the join has completed successfully. Each join request is logged, including keepalive requests that multicast consumers send periodically as part of the IGMP protocol.  
`IGMP consumer joined` | The Google Cloud control plane successfully added the multicast consumer to the group. After this event has propagated to the multicast infrastructure for the domain, the multicast consumer begins receiving multicast traffic. This event is always preceded by an `IGMP join request received` event.  
`IGMP consumer left` | The Google Cloud control plane received an explicit IGMP leave request from the multicast consumer and applied the request.  
`IGMP consumer timed out` | The Google Cloud control plane removed the multicast consumer from the group because the multicast consumer stopped responding with keepalive requests.  
`Consumer removed due to configuration change` | The Google Cloud control plane removed the multicast consumer from the group because the consumer endpoint was deleted. For example, the consumer instance or project might have been deleted.  
`IGMP join request rejected due to full tree` | The Google Cloud control plane received the join request, but rejected the request because the multicast group is already at full capacity.  
`IGMP join request rejected due to missing quota` | The Google Cloud control plane received the join request, but rejected the request because the multicast consumer VPC network is already using all of its quota for [multicast consumer VMs per VPC network](https://docs.cloud.google.com/vpc/docs/multicast/quotas#quotas-per-network).  
`IGMP join request rejected due to unknown reason` | The Google Cloud control plane received the join request, but rejected the request because of a failure that doesn't have a dedicated reason.  
`IGMP entitlement rejected` | The Google Cloud control plane received the join request, but rejected the request because the required multicast consumer configuration is not complete, such as in the following cases:

  * The multicast consumer VPC network configuration isn't complete.
  * The multicast consumer VPC network configuration hasn't propagated to the multicast infrastructure for the domain.
  * The multicast consumer isn't configured for IGMP.

This event is only available in the logs for the multicast group consumer activation resource.  
`Consumer network activated` | A multicast consumer VPC network was activated for a multicast group range. This corresponds to the creation of a [multicast group consumer activation](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#consumer-resources) resource. This event is available only to multicast administrators in the logs for multicast group range resources.  
`Consumer network deactivated` | A multicast consumer VPC network was deactivated for a multicast group range. This means that a [multicast group consumer activation](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#consumer-resources) resource was deleted or its status changed to `INACTIVE`. This event is available only to multicast administrators in the logs for multicast group range resources.  
  
### Log format for multicast group ranges

This section describes the format of group membership event logs that are available in the multicast administrator project that contains multicast domain and group range resources.

These logs are written for membership events for all multicast consumers of a given multicast group range. You can configure logging on both the global multicast group range and zonal multicast group range activation resources as described in Enable logging for a multicast group range.

The Cloud Logging monitored resource type and log name are as follows:

  * **Resource type** : `networkservices.googleapis.com/MulticastGroupRange`
  * **Log name** : `networkservices.googleapis.com%2Fmulticast_memberships`



The log format is different depending on the type of logged event. See the tables in each of the following tabs for details.

###  IGMP event 

If the logged event is an IGMP event, the log includes the following fields:

Field | Type | Description  
---|---|---  
`consumerIp` | string | The primary internal IPv4 address of the multicast consumer. Example: `10.0.0.1`.  
`consumerLocation` | string | The zone of the multicast consumer VPC. Example: `us-east5-a`.  
`consumerNetwork` | Resource | The multicast consumer VPC network. Only the integer ID is populated. Example: 
    
    
          consumerNetwork {
           id: "1234"
          }
            
  
`consumerProject` | Project | The project that contains the multicast consumer VPC network. Only the project number is populated. Example: 
    
    
          consumerProject {
           number: "5678"
          }
            
  
`consumerResource` | Resource | The multicast consumer VM instance. Only the integer ID is populated. Example: 
    
    
          consumerResource {
           id: "1111"
          }
            
  
`consumerResourceProject` | Project |  The project that contains the multicast consumer VM instance. This can be different from the project that contains the multicast consumer VPC network, such as when using Shared VPC. Only the project number is populated. Example: 
    
    
          consumerResourceProject {
           number: "4321"
          }
            
  
`eventDescription` | string | One of the events described in Logged events. Example: `IGMP consumer joined`.  
`eventTime` | string | The timestamp of the event in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) text format. Example: `2024-10-21T06:46:42.990162973Z`.  
`multicastDomain` | string | The name of the multicast domain. Example: `my-domain-name`.  
`multicastGroupRange` | string | The name of the multicast group range. Example: `my-group-range-name`.  
`multicastIp` | string | The IP address of the multicast group. Example: `224.0.0.1`.  
  
###  Activation/deactivation 

If the logged event is a multicast consumer VPC network activation or deactivation, the log includes the following fields:

Field | Type | Description  
---|---|---  
`consumerLocation` | string | The zone in which the multicast consumer VPC network was activated. Example: `us-east5-a`.  
`consumerNetwork` | Resource | The multicast consumer VPC network. Only the integer ID is populated. Example: 
    
    
          consumerNetwork {
           id: "1234"
          }
            
  
`consumerProject` | Project | The project that contains the multicast consumer VPC network. Only the project number is populated. Example: 
    
    
          consumerProject {
           number: "5678"
          }
            
  
`eventDescription` | string | One of the events described in Logged events. Example: `Consumer network activated`.  
`eventTime` | string | The timestamp of the event in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) text format. Example: `2024-10-21T06:46:42.990162973Z`.  
`multicastDomain` | string | The name of the multicast domain. Example: `my-domain-name`.  
`multicastGroupRange` | string | The name of the multicast group range. Example: `my-group-range-name`.   
  
Integer IDs are used for resources of multicast consumers, such as projects, networks, and instances, to maintain privacy.

### Log format for multicast group consumer activations

This section describes the format of group membership event logs that are available in projects that contain multicast consumer configurations.

These logs are written for membership events for multicast consumers in a given VPC network that is activated for a multicast group range and zone. You can configure logging on the zonal multicast group consumer activation resource as described in Enable logging for a multicast group consumer activation.

The Cloud Logging monitored resource type and log name are as follows:

  * **Resource type** : `networkservices.googleapis.com/MulticastGroupConsumerActivation`
  * **Log name** : `networkservices.googleapis.com%2Fmulticast_memberships`



The log includes the following fields:

Field | Type | Description  
---|---|---  
`consumerIp` | string | The primary internal IPv4 address of the multicast consumer. Example: `10.0.0.1`.  
`consumerLocation` | string | The zone of the multicast consumer. Example: `us-east5-a`.  
`consumerNetwork` | Resource | The multicast consumer VPC network. Example: 
    
    
            consumerNetwork {
              name: "my-network"
              id: "1234"
            }
              
  
`consumerProject` | Project | The project that contains the multicast consumer VPC network. Example: 
    
    
            consumerProject {
              id: "my-project"
              number: "5678"
            }
              
  
`consumerResource` | Resource | The multicast consumer VM instance. Example: 
    
    
            consumerResource {
              name: "my-instance"
              id: "1111"
            }
              
  
`consumerResourceProject` | Project |  The project that contains the multicast consumer VM instance. This can be different from the project that contains the multicast consumer VPC network, such as when using Shared VPC. Example: 
    
    
            consumerResourceProject {
              id: "my-instance-project"
              number: "4321"
            }
              
  
`eventDescription` | string | One of the events described in Logged events. Example: `IGMP consumer joined`.  
`eventTime` | string | The timestamp of the event in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) text format. Example: `2024-10-21T06:46:42.990162973Z`.  
`multicastConsumerAssociation` | string | The name of the multicast consumer association between the multicast consumer VPC network and the domain. Example: `my-consumer-association-name`.  
`multicastGroupConsumerActivation` | string | The name of the multicast group consumer activation. Example: `my-group-consumer-activation-name`.  
`multicastIp` | string | The IP address of the multicast group. Example: `224.0.0.1`.  
  
Unlike the multicast group range logs, the multicast group consumer activation logs use string IDs for the project and network because the logs are only available to the project that contains the multicast consumer configurations.

### Field format reference

#### Project

Field | Type | Description  
---|---|---  
`number` | string ([uint64](https://developers.google.com/discovery/v1/type-format)) | The automatically generated integer ID of the project. Example: `5678`.  
`id` | string | The user-assigned ID of the project. Example: `my-project`.  
  
#### Resource

Field | Type | Description  
---|---|---  
`id` | string ([uint64](https://developers.google.com/discovery/v1/type-format)) | The automatically generated integer ID of the resource. Example: `1111`.  
`name` | string | The user-assigned name of the resource. Example: `my-instance`.  
  
## Enable group membership event logging

The following sections describe how to enable group membership event logging.

### Enable logging for a multicast group range

This section describes how a multicast administrator can configure group membership event logging for an existing multicast group range.

For more information about configuring logging when creating a new multicast group range, see [Create multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/create-group-ranges). Membership event logging is not enabled by default.

You can configure membership event logging on both of the following resources:

  * **Multicast group range:** The logging configuration of a global group range applies to all activations of the group range.
  * **Multicast group range activation:** The logging configuration of a zonal group range activation overrides the global group range configuration.



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networkservices.multicastGroupRanges.update`
  * `networkservices.multicastGroupRangeActivations.update`



**Roles**

  * [ Multicast Admin](https://docs.cloud.google.com/vpc/docs/multicast/reference/permissions-reference) (`roles/compute.multicastAdmin`)



###  gcloud 

  * To enable or disable logging for a multicast group range, use the [`network-services multicast-group-ranges update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/update).
        
        gcloud network-services multicast-group-ranges update GROUP_RANGE_NAME \
            --location=global \
            [--enable-logging | --no-enable-logging]
        

Replace the following:

    * `GROUP_RANGE_NAME`: the name of the multicast group range
    * `--[no-]enable-logging`: determines whether membership event logging is enabled. 
      * To enable logging, use `--enable-logging`.
      * To disable logging, use `--no-enable-logging`.
  * To enable or disable logging for a multicast group range activation, use the [`network-services multicast-group-range-activations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-range-activations/update).
        
        gcloud network-services multicast-group-range-activations update GROUP_RANGE_ACTIVATION_NAME \
            --location=ZONE \
            [--enable-logging | --no-enable-logging]
        

Replace the following:

    * `GROUP_RANGE_ACTIVATION_NAME`: the name of the multicast group range activation
    * `ZONE`: the zone of the multicast group range activation
    * `--[no-]enable-logging`: determines whether membership event logging is enabled. 
      * To enable logging, use `--enable-logging`.
      * To disable logging, use `--no-enable-logging`.



###  API 

  * To enable or disable logging for a multicast group range, use the [`multicastGroupRanges.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/patch).
        
        PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME?updateMask=logConfig
        {
          "logConfig": {"enabled": "LOGGING_ENABLED"}
        }
        

Replace the following:

    * `PROJECT_ID`: The ID of the project
    * `GROUP_RANGE_NAME`: the name of the multicast group range
    * `LOGGING_ENABLED`: specifies whether membership event logging is enabled. 
      * To enable logging, set to `true`.
      * To disable logging, set to `false`.
  * To enable or disable logging for a multicast group range activation, use the [`multicastGroupRangeActivations.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/patch).
        
        PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupRangeActivations/GROUP_RANGE_ACTIVATION_NAME?updateMask=logConfig
        {
          "logConfig": {"enabled": "LOGGING_ENABLED"}
        }
        

Replace the following:

    * `PROJECT_ID`: The ID of the project
    * `GROUP_RANGE_ACTIVATION_NAME`: the name of the multicast group range activation
    * `ZONE`: the zone of the multicast group range activation
    * `LOGGING_ENABLED`: specifies whether membership event logging is enabled. 
      * To enable logging, set to `true`.
      * To disable logging, set to `false`.



### Enable logging for a multicast group consumer activation

This section describes how a multicast consumer network administrator can configure group membership event logging for their VPC network.

For a given VPC network that you enabled to consume multicast traffic, you can configure membership event logging on the corresponding multicast group consumer activation.

For more information about configuring logging when creating a new multicast group consumer activation, see [Enable a VPC network to consume multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network). Membership event logging is not enabled by default.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `networkservices.multicastGroupConsumerActivations.update`



**Roles**

  * [ Multicast Admin](https://docs.cloud.google.com/vpc/docs/multicast/reference/permissions-reference) (`roles/compute.multicastAdmin`)



###  gcloud 

To enable or disable logging for a multicast group consumer activation, use the [`network-services multicast-group-consumer-activations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-consumer-activations/update).
    
    
      gcloud network-services multicast-group-consumer-activations update GROUP_CONSUMER_ACTIVATION_NAME \
          --location=ZONE \
          [--enable-logging | --no-enable-logging]
    

Replace the following:

  * `GROUP_CONSUMER_ACTIVATION_NAME`: the name of the multicast group consumer activation
  * `ZONE`: the zone of the multicast group consumer activation
  * `--[no-]enable-logging`: determines whether membership event logging is enabled. 
    * To enable logging, use `--enable-logging`.
    * To disable logging, use `--no-enable-logging`.



###  API 

To enable or disable logging for a multicast group consumer activation, use the [`multicastGroupConsumerActivations.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/patch).
    
    
      PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupConsumerActivations/GROUP_CONSUMER_ACTIVATION_NAME?updateMask=logConfig
      {
        "logConfig": {"enabled": "LOGGING_ENABLED"}
      }
    

Replace the following:

  * `PROJECT_ID`: The ID of the project
  * `GROUP_CONSUMER_ACTIVATION_NAME`: the name of the multicast group consumer activation
  * `ZONE`: the zone of the multicast group consumer activation
  * `LOGGING_ENABLED`: specifies whether membership event logging is enabled. 
    * To enable logging, set to `true`.
    * To disable logging, set to `false`.



## View group membership event logs

This section describes how to view group membership event logs for multicast.

For more information, see the [Logs Explorer overview](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page: 

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer?resource=dns_query)

  2. To see multicast group membership event logs, select one of the following monitored resource types from the **All resources** list: 
     * If you are a multicast administrator and you want to see the group membership event logs for all multicast consumers in a group, then select **Multicast Group Range**.
     * If you are a multicast consumer VPC network administrator and you want to see group membership event logs for your network, then select **Multicast Group Consumer Activation**.



## What's next

  * [Get an overview of Cloud Multicast observability](https://docs.cloud.google.com/vpc/docs/multicast/observability)
  * [View flow logs for multicast](https://docs.cloud.google.com/vpc/docs/multicast/view-flow-logs)
  * [Monitor membership metrics for multicast](https://docs.cloud.google.com/vpc/docs/multicast/monitor-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
