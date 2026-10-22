---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sentinelone/
title: Integrate SentinelOne with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:33.354588+00:00
---

# Integrate SentinelOne with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sentinelone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate SentinelOne with Google SecOps 

This document explains how to configure and integrate SentinelOne with Google Security Operations (Google SecOps).

## Use cases

  1. **Automated threat response** : use Google SecOps capabilities to automatically respond to threats detected by SentinelOne, reducing the time and effort required for security operations.

  2. **Enriched incident context** : use Google SecOps capabilities to provide security analysts with more context around security incidents and make more informed decisions. For example, you can automatically enrich incident data with information about the affected endpoints and threats.

  3. **Orchestrated remediation actions** : use Google SecOps capabilities to automatically execute playbooks that combine SentinelOne actions with other security tools, such as network firewalls or identity management systems, ensuring a coordinated response to threats and minimizing their impact.




## Integration parameters

The SentinelOne integration requires the following parameters:

Parameter | Description  
---|---  
`Api root` | Required. The SentinelOne API root.The default value is `https://{server}.sentinelone.net/`.  
`Username` | Required. The username to authenticate with.  
`Password` | Required. The password to authenticate with.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Disconnect Agent From Network

Use the **Disconnect Agent From Network** action to disconnect an agent from the network connection.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

None.

#### Action outputs

The **Disconnect Agent From Network** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Disconnect Agent From Network** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enrich Endpoint

Use the **Enrich Endpoint** action to enrich an endpoint entity with information from the system.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

None.

#### Action outputs

The **Enrich Endpoint** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Endpoint** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Agent Status

Use the **Get Agent Status** action to retrieve the status of an agent.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

None.

#### Action outputs

The **Get Agent Status** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get Agent Status** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Application List for Endpoint

Use the **Get Application List for Endpoint** action to obtain a list of applications used on an endpoint.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

None.

#### Action outputs

The **Get Application List for Endpoint** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get Application List for Endpoint** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Events for Endpoint by Time

Use the **Get Events for Endpoint by Time** action to retrieve all events that are related to an endpoint.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

The **Get Events for Endpoint by Time** action requires the following parameters:

Parameter | Description  
---|---  
`Hours Back` | Optional.The number of hours prior to the current time to retrieve events.  
`Events Amount Limit` | Optional.The number of events to retrieve for every action run.  
  
#### Action outputs

The **Get Events for Endpoint by Time** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get Events for Endpoint by Time** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Hash Reputation

Use the **Get Hash Reputation** action to obtain the reputation of a SHA-1 hash.

This action runs on the Google SecOps `Filehash` entity.

#### Action inputs

None.

#### Action outputs

The **Get Hash Reputation** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get Hash Reputation** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Process List for Endpoint

Use the **Get Process List for Endpoint** action to retrieve the process list for an endpoint.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

None.

#### Action outputs

The **Get Process List for Endpoint** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get Process List for Endpoint** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get System Status

Use the **Get System Status** action to get the SentinelOne system health status.

This action runs on all Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Get System Status** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get System Status** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get System Version

Use the **Get System Version** action to get the SentinelOne system version.

This action runs on all Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Get System Version** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get System Version** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Initiate Full Scan

Use the **Initiate Full Scan** action to initiate a full disk scan on an endpoint.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

None.

#### Action outputs

The **Initiate Full Scan** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Initiate Full Scan** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to SentinelOne.

This action runs on all Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Reconnect Agent to the Network

Use the **Reconnect Agent to the Network** action to reconnect a disconnected agent to the network.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

None.

#### Action outputs

The **Reconnect Agent to the Network** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Reconnect Agent to the Network** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Exclusion List Add Path

Use the **Update Exclusion List Add Path** action to add a path to an existing exclusion list.

This action supports the following operating systems: Windows, OSX, Linux, and Android.

This action runs on all Google SecOps entities.

#### Action inputs

The **Update Exclusion List Add Path** action requires the following parameters:

Parameter | Description  
---|---  
`List Name` | Required.The exclusion list name.  
`Path` | Required.The path to add to the list.  
`Operation System` | Required.The operating system.The possible values are as follows:

  * `windows`
  * `osx`
  * `linux`
  * `android`

  
  
#### Action outputs

The **Update Exclusion List Add Path** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Update Exclusion List Add Path** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
