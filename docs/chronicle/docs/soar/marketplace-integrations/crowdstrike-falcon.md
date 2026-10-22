---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/crowdstrike-falcon/
title: Integrate CrowdStrike Falcon with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:09.615493+00:00
---

# Integrate CrowdStrike Falcon with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/crowdstrike-falcon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate CrowdStrike Falcon with Google SecOps

This document explains how to integrate CrowdStrike Falcon with Google Security Operations.

This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/CrowdStrikeFalcon.zip).

## Use cases

In the Google SecOps platform, the CrowdStrike Falcon integration solves the following use cases:

  * **Automated malware containment** : use the capabilities of the Google SecOps platform to automatically quarantine the affected endpoint, retrieve the file hash for further analysis, and prevent the spread of malware. The automated malware containment activates when a phishing email triggers a CrowdStrike Falcon alert for a suspicious file download.

  * **Accelerated incident response** : use Google SecOps to gather contextual data like process trees and network connections, isolate the compromised host, and create a ticket for investigation.

  * **Threat hunting and investigation** : use the capabilities of the Google SecOps platform to query CrowdStrike Falcon for specific user actions, file modifications, and network connections over a defined period. Threat hunting and investigation lets your security analysts investigate a potential insider threat and analyze a historical endpoint activity while streamlining the investigation process.

  * **Phishing response and remediation** : use CrowdStrike Falcon and the Google SecOps platform to scan the email attachments, open them in a sandbox environment, and automatically block the sender email address if malicious activity is detected.

  * **Vulnerability management** : use the capabilities of the Google SecOps platform to automatically create tickets for each vulnerable system, prioritize them based on severity and asset value, and trigger automated patching workflows. The vulnerability management helps you identify a critical vulnerability on multiple endpoints.




## Before you begin

Before you configure the integration in Google SecOps, complete the following steps:

  1. Configure the CrowdStrike Falcon API client.

  2. Configure action permissions.

  3. Configure connector permissions.




### Configure the CrowdStrike Falcon API client

To define a CrowdStrike API client and view, create, or modify API clients or keys, you need to have a [FalconAdministrator](https://falcon.crowdstrike.com/support/documentation/1/crowdstrike-api-introduction) role.

Secrets are only shown when you create a new API client or reset the API client.

To configure the CrowdStrike Falcon API client, complete the following steps:

  1. In the Falcon UI, navigate to **Support and resources > Resources and tools > API clients and keys**. On this page, you can find existing clients, add new API clients, or view the audit log.
  2. Click **Create API Client**.
  3. Provide a name for your new API client.
  4. Select appropriate **API scopes**.
  5. Click **Create**. The **Client ID** and **Client Secret** values appear.

This is the only time when you see the client secret value. Make sure to store it securely. If you lose your client secret, reset your API client and update all applications that rely on the client secret with new credentials.




For more details regarding access to the CrowdStrike API, see the [Getting Access to the CrowdStrike API](https://www.crowdstrike.com/blog/tech-center/get-access-falcon-apis/) guide at the CrowdStrike blog.

### Configure action permissions

Refer to the minimal permissions for actions, as listed in the following table:

Action | Required permissions  
---|---  
Add Comment to Detection | `Detections.Read`  
`Detection.Write`  
Add Identity Protection Detection Comment | `Alerts.Read`  
`Alerts.Write`  
Add Incident Comment | `Incidents.Write`  
Close Detection | `Detections.Read`  
`Detection.Write`  
Contain Endpoint | `Hosts.Read`  
`Hosts.Write`  
Delete IOC | `IOC Management.Read`  
`IOC Management.Write`  
Download File | `Hosts.Read`  
`Real time response.Read`  
`Real time response.Write`  
Execute Command | `Hosts.Read`  
`Real time response.Read`  
`Real time response.Write`  
`Real time response (admin).Write*` for full privilege commands.   
Get Event Offset | `Event streams.Read`  
Get Hosts by IOC | Not available: Deprecated  
Get Host Information | `Hosts.Read`  
Get Process Name By IOC | Not available: Deprecated  
Lift Contained Endpoint | `Hosts.Read`  
`Hosts.Write`  
List Hosts | `Hosts.Read`  
List Host Vulnerabilities | `Hosts.Read`  
`Spotlight vulnerabilities.Read`  
List Uploaded IOCs | `IOC Management.Read`  
On-Demand Scan | `On-demand scans (ODS).Read`  
`On-demand scans (ODS).Write`  
Ping | `Hosts.Read`  
Submit File | `Reports (Falcon Intelligence).Read`  
`Sandbox (Falcon Intelligence).Read`  
`Sandbox (Falcon Intelligence).Write`  
Submit URL | `Reports (Falcon Intelligence).Read`  
`Sandbox (Falcon Intelligence).Read`  
`Sandbox (Falcon Intelligence).Write`  
Update Detection | `Detections.Read`  
`Detection.Write`  
`User management.Read`  
Update Identity Protection Detection | `Alerts.Read`  
`Alerts.Write`  
Update Incident | ` Incidents.Write`  
Update IOC Information | `IOC Management.Read`  
`IOC Management.Write`  
Upload IOCs | `IOC Management.Read`  
`IOC Management.Write`  
  
### Configure connector permissions

Refer to the minimal permissions for connectors, as listed in the following table:

Connector | Required permissions  
---|---  
CrowdStrike Detections Connector | `Detection.Read`  
CrowdStrike Falcon Streaming Events Connector | `Event streams.Read`  
CrowdStrike Identity Protection Detections Connector | `Alerts.Read`  
CrowdStrike Incidents Connector | `Incidents.Read`  
  
## Endpoints

The CrowdStrike Falcon integration interacts with the following CrowdStrike Falcon API endpoints:

**General API endpoints** :

  * `/oauth2/token`



**Hosts and devices** :

  * `/devices/entities/devices/v1`
  * `/devices/entities/devices-actions/v2`



**Detections and events** :

  * `/detections/entities/detections/v2`
  * `/detections/entities/summaries/GET/v1`
  * `/protection/entities/detections/v1`



**Indicators of compromise (IOCs)** :

  * `/intel/entities/indicators/v1`
  * `/intel/queries/devices/v1`



**Vulnerabilities** :

  * `/devices/combined/devices/vulnerabilities/v1`



**Response and containment** :

  * `/respond/entities/command-queues/v1`
  * `/respond/entities/extracted-files/v1`



**Incidents** :

  * `/incidents/entities/incidents/GET/v1`
  * `/incidents/entities/incidents/comments/GET/v1`
  * `/incidents/entities/incidents/GET/v1`



**File and URL analysis** :

  * `/malware-uploads/entities/submissions/v2`
  * `/url/entities/scans/v1`



## Integration parameters

For the integration to function properly, a premium version of CrowdStrike Falcon with full capabilities is required. Certain actions don't work with a basic version of CrowdStrike Falcon.

The CrowdStrike Falcon integration requires the following parameters:

Parameters  
---  
`API Root` | An API root of the CrowdStrike instance. The default value is `https://api.crowdstrike.com`  
`Client API ID` | _Required_ The client ID for CrowdStrike API.  
`Client API Secret` | _Required_ The client secret for CrowdStrike API.  
`Verify SSL` | If selected, the integration verifies if the SSL certificate for connecting to the CrowdStrike Falcon server is valid. Not selected by default.  
`Customer ID` | _Optional_ The customer ID of the tenant in which to execute the integration. For use in multi-tenant (MSSP) environments.   
  
For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage if needed. After you configure an integration instance, you can use it in playbooks. For more information about configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

Before proceeding with the integration configuration, configure the minimal permissions required for every integration item. For more detail, refer to the Action permissions section of this document.

### Add Alert Comment

Use the **Add Alert Comment** action to add a comment to an alert in CrowdStrike Falcon.

This action doesn't run on entities.

#### Action inputs

The **Add Alert Comment** action requires the following parameters:

Parameters  
---  
`Alert` | _Required_ The ID of the alert to update.  
`Comment` | _Required_ The comment to add to the alert.  
  
#### Action outputs

The **Add Alert Comment** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add Alert Comment** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added comment to the alert with ID ALERT_ID in CrowdStrike` | Action succeeded.  
`Error executing action "Add Alert Comment". Reason: ERROR_REASON` `Error executing action "Add Alert Comment". Reason: alert with ID ALERT_ID wasn't found in CrowdStrike. Please check the spelling.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Alert Comment** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add Comment to Detection - Deprecated

**Deprecated:** This action is deprecated. Use the Add Alert Comment action instead. 

Use the **Add Comment to Detection** action to add a comment to the detection in CrowdStrike Falcon.

This action runs on all entities.

#### Action inputs

The **Add Comment to Detection** action requires the following parameters:

Parameter | Description  
---|---  
`Detection ID` | Required. The ID of the detection to add a comment to.  
`Comment` | Required. The comment to add to the detection.  
  
#### Action outputs

The **Add Comment to Detection** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Add Comment to Detection** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Identity Protection Detection Comment

Use the **Add Identity Protection Detection Comment** action to add a comment to the identity protection detection in CrowdStrike.

This action requires an Identity Protection license.

This action doesn't run on entities.

#### Action inputs

The **Add Identity Protection Detection Comment** action requires the following parameters:

Parameters  
---  
`Detection ID` | _Required_ The ID of the detection to update.  
`Comment` | _Required_ The comment to add to the detection.  
  
#### Action outputs

The **Add Identity Protection Detection Comment** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add Identity Protection Detection Comment** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added comment to the identity protection detection with ID  DETECTION_ID in CrowdStrike` | Action succeeded.  
`Error executing action "Add Identity Protection Detection Comment". Reason:  ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "Add Identity Protection Detection Comment". Reason: identity protection detection with ID DETECTION_ID wasn't found in CrowdStrike. Please check the spelling.` | Action failed.Check the spelling.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Identity Protection Detection Comment** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add Incident Comment - Deprecated

**Deprecated:** This action is deprecated. Use the Update Alert action instead.

Use the **Add Incident Comment** action to add a comment to an incident in CrowdStrike.

This action doesn't run on entities.

#### Action inputs

The **Add Incident Comment** action requires the following parameters:

Parameter | Description  
---|---  
`Incident ID` | Required. ID of the incident to update.  
`Comment` | Required. The comment to add to the incident.  
  
#### Action outputs

The **Add Incident Comment** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add Incident Comment** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added comment to the incident INCIDENT_ID in CrowdStrike ` | Action succeeded.  
`Error executing action "Add Incident Comment". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "Add Incident Comment". Reason: incident with ID INCIDENT_ID wasn't found in CrowdStrike. Please check the spelling.` | Action failed.Check the spelling.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Incident Comment** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Close Detection - Deprecated

**Deprecated:** This action is deprecated. Use the Update Alert action instead. 

Use the **Close Detection** action to close a CrowdStrike Falcon detection.

**Note:** The Update Alert action is the best practice for this use case and should be used in place of this action by providing the appropriate status. 

This action runs on all entities.

#### Action inputs

The **Close Detection** action requires the following parameters:

Parameter | Description  
---|---  
`Detection ID` |  Required. The ID of the detection to close.  
`Hide Detection` |  Optional. If selected, the action hides the detection in the UI. Selected by default.  
  
#### Action outputs

The **Close Detection** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Close Detection** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Contain Endpoint

Use the **Contain Endpoint** action to contain endpoint in CrowdStrike Falcon.

This action runs on the following entities:

  * IP address
  * Hostname



#### Action inputs

The **Contain Endpoint** action requires the following parameters:

Parameters  
---  
`Customer ID` | _Optional_ Specify the ID of the customer for which you want to execute the action.  
`Device ID` | _Optional_ Comma-separated list of device IDs on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Fail If Timeout` | _Optional_ If selected and not all of the endpoints are contained, the action fails. Selected by default.  
  
#### Action outputs

The **Contain Endpoint** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment

The **Contain Endpoint** action supports the following entity enrichment logic:

Enrichment field | Logic  
---|---  
`status` | Returns if it exists in the JSON result  
`modified_timestamp` | Returns if it exists in the JSON result  
`major_version` | Returns if it exists in the JSON result  
`policies` | Returns if it exists in the JSON result  
`config_id_platform` | Returns if it exists in the JSON result  
`bios_manufacturer` | Returns if it exists in the JSON result  
`system_manufacturer` | Returns if it exists in the JSON result  
`device_policies` | Returns if it exists in the JSON result  
`meta` | Returns if it exists in the JSON result  
`pointer_size` | Returns if it exists in the JSON result  
`last_seen` | Returns if it exists in the JSON result  
`agent_local_time` | Returns if it exists in the JSON result  
`first_seen` | Returns if it exists in the JSON result  
`service_pack_major` | Returns if it exists in the JSON result  
`slow_changing_modified_timestamp` | Returns if it exists in the JSON result  
`service_pack_minor` | Returns if it exists in the JSON result  
`system_product_name` | Returns if it exists in the JSON result  
`product_type_desc` | Returns if it exists in the JSON result  
`build_number` | Returns if it exists in the JSON result  
`cid` | Returns if it exists in the JSON result  
`local_ip` | Returns if it exists in the JSON result  
`external_ip` | Returns if it exists in the JSON result  
`hostname` | Returns if it exists in the JSON result  
`config_id_build` | Returns if it exists in the JSON result  
`minor_version` | Returns if it exists in the JSON result  
`platform_id` | Returns if it exists in the JSON result  
`os_version` | Returns if it exists in the JSON result  
`config_id_base` | Returns if it exists in the JSON result  
`provision_status` | Returns if it exists in the JSON result  
`mac_address` | Returns if it exists in the JSON result  
`bios_version` | Returns if it exists in the JSON result  
`platform_name` | Returns if it exists in the JSON result  
`agent_load_flags` | Returns if it exists in the JSON result  
`device_id` | Returns if it exists in the JSON result  
`product_type` | Returns if it exists in the JSON result  
`agent_version` | Returns if it exists in the JSON result  
  
##### JSON result

The following example describes the JSON result output received when using the **Contain Endpoint** action:
    
    
    {
      "EntityResult":
        {
          "status": "contained",
          "modified_timestamp": "2019-06-24T07:47:37Z",
          "major_version": "6",
          "policies":
            [{
               "applied": "True",
               "applied_date": "2019-04-29T07:40:06.876850888Z",
               "settings_hash": "ce17279e",
               "policy_type": "prevention",
               "assigned_date": "2019-04-29T07:39:55.218651583Z",
               "policy_id": ""
             }],
          "config_id_platform": "3",
          "bios_manufacturer": "Example Inc.",
          "system_manufacturer": "Example Corporation",
          "device_policies":
             {
                "global_config":
                   {
                     "applied": "True",
                     "applied_date": "2019-06-03T23:24:04.893780991Z",
                     "settings_hash": "a75911b0",
                     "policy_type": "globalconfig",
                     "assigned_date": "2019-06-03T23:23:17.184432743Z",
                     "policy_id": ""
                    },
                "Sensor_update":
                   {
                     "applied": "True",
                     "applied_date": "2019-05-30T23:13:55.23597658Z",
                     "settings_hash": "65994753|3|2|automatic;101",
                     "uninstall_protection": "ENABLED",
                     "policy_type": "sensor-update",
                     "assigned_date": "2019-05-30T23:04:31.485311459Z",
                     "policy_id": ""
                    },
                "prevention":
                   {
                     "applied": "True",
                     "applied_date": "2019-04-29T07:40:06.876850888Z",
                     "settings_hash": "ce17279e",
                     "policy_type": "prevention",
                     "assigned_date": "2019-04-29T07:39:55.218651583Z",
                     "policy_id": ""
                    },
                "device_control":
                    {
                      "applied": "True",
                      "applied_date": "2019-06-03T23:14:29.800434222Z",
                      "policy_type": "device-control",
                      "assigned_date": "2019-06-03T23:05:17.425127539Z",
                      "policy_id": ""
                     },
                "remote_response":
                    {
                      "applied": "True",
                      "applied_date": "2019-04-29T07:40:04.469808388Z",
                      "settings_hash": "f472bd8e",
                      "policy_type": "remote-response",
                      "assigned_date": "2019-04-29T07:39:55.218642441Z",
                      "policy_id": ""
                     }
              },
           "meta":
              {
                "Version":"12765"
              },
           "pointer_size": "8",
           "last_seen": "2019-06-24T07:45:34Z",
           "agent_local_time": "2019-06-18T12:17:06.259Z",
           "first_seen": "2019-04-29T07:39:45Z",
           "service_pack_major": "0",
           "slow_changing_modified_timestamp": "2019-06-23T11:20:42Z",
           "service_pack_minor": "0",
           "system_product_name": "Virtual Machine",
           "product_type_desc": "Server",
           "build_number": "9600",
           "cid": "123456789abcdef123456789abcdef12",
           "local_ip": "192.0.2.1",
           "external_ip": "203.0.113.1",
           "hostname": "",
           "config_id_build": "example-id",
           "minor_version": "3",
           "platform_id": "x",
           "os_version": "Windows Server 2012 R2",
           "config_id_base": "example-config",
           "provision_status": "Provisioned",
           "mac_address": "01:23:45:ab:cd:ef",
           "bios_version": "090007 ",
           "platform_name": "Windows",
           "Agent_load_flags":"1",
           "device_id": "",
           "product_type": "3",
           "agent_version": "5.10.9106.0"
         },
       "Entity": "198.51.100.255"
    }
    

##### Output messages

The **Contain Endpoint** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully contained the following endpoints in CrowdStrike Falcon: ENTITY_ID` `The following endpoints were already contained in CrowdStrike Falcon:  ENTITY_ID` `The following endpoints were not found in CrowdStrike Falcon: ENTITY_ID ` | Action succeeded.  
`Error executing action "Contain Endpoint". Reason: ERROR_REASON ` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "Contain Endpoint". Reason: the following endpoints initiated containment, but were not able to finish it during action execution: ENTITY_ID` | Action failed.Check the endpoint status and the `Fail If Timeout` parameter value.  
  
##### Script result

The following table describes the values for the script result output when using the **Contain Endpoint** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete IOC

Use the **Delete IOC** action to delete custom IOCs in CrowdStrike Falcon.

This action treats hostname entities as domain IOCs and extracts the domain part out of URLs. This action only supports the MD5 and SHA-256 hashes.

The **Delete IOC** action runs on the following entities:

  * IP Address
  * Hostname
  * URL
  * Hash



#### Action inputs

None.

#### Action outputs

The **Delete IOC** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Delete IOC** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
##### Output messages

On a Case Wall, the **Delete IOC** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully deleted the following custom IOCs in CrowdStrike Falcon:  ENTITY_ID` `The following custom IOCs were not a part of CrowdStrike Falcon instance:  ENTITY_ID` `All of the provided IOCs were not a part of CrowdStrike Falcon instance.` | Action succeeded.  
`Error executing action "Delete IOC". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
### Download File

Use the **Download File** action to download files from the hosts in CrowdStrike Falcon.

This action requires both the Filename and IP address or a Hostname entity to be in the scope of the Google SecOps alert.

You can find the downloaded file in a password-protected zip package. To access the file, provide the following password: `infected`.

The **Download File** action runs on the following entities:

  * Filename
  * IP address
  * Host



#### Action inputs

The **Download File** action requires the following parameters:

Parameters  
---  
`Customer ID` | _Optional_ Specify the ID of the customer for which you want to execute the action.  
`Device ID` | _Optional_ Comma-separated list of device IDs on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Download Folder Path` | _Required_ The path to the folder that stores the downloaded file. The format depends on your deployment:

  * **SaaS deployment** : The path is internal to the hosted platform.
  * **Remote Deployment** : The path must be an absolute, valid directory path on the local machine where the Remote Agent is installed (such as, `C:\temp\download` for Windows or `/var/tmp/download/` for Linux).

  
`Overwrite` | _Required_ If selected, the action overwrites the file with the same name. Not selected by default.  
  
#### Action outputs

The **Download File** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity table

The **Download File** action provides the following entity table:

Entity  
---  
`filepath` | Absolute path to the file.  
  
##### JSON result

The following example describes the JSON result output received when using the **Download File** action:
    
    
    {
    
    "absolute_paths": ["/opt/file_1", "opt_file_2"]
    
    }
    

##### Output messages

The **Download File** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully downloaded file "FILENAME" from the following endpoints in CrowdStrike Falcon:  ENTITY_ID` `Action wasn't able to download file from the following endpoints in CrowdStrike Falcon: ENTITY_ID ` | Action succeeded.  
`Error executing action "Download File". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "Download File". Reason: file with path PATH already exists. Please delete the file or set "Overwrite" to true.` | Action failed.Check the `Overwrite` parameter value or delete the file.  
`Waiting for results for the following entities: ENTITY_ID` | Asynchronous message.  
  
##### Script result

The following table describes the values for the script result output when using the **Download File** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Execute Command

Use the **Execute Command** action to execute commands on the hosts in CrowdStrike Falcon.

This action runs on the following entities:

  * IP address
  * Hostname



#### Action inputs

The **Execute Command** action requires the following parameters:

Parameters  
---  
`Customer ID` | _Optional_ Specify the ID of the customer for which you want to execute the action.  
`Command` | _Required_ Specify what command to execute on the hosts.  
`Admin Command` | _Optional_ If selected, the action executes commands with administrative permissions. This is required for specific commands such as `put`. Not selected by default.  
`Hostname` | _Optional_ Comma-separated list of hostnames on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Device ID` | _Optional_ Comma-separated list of device IDs on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Queue Offline` | _Optional_ If selected, commands targeting offline hosts are queued and executed once the host reconnects to the network. Not selected by default.  
  
#### Action outputs

The **Execute Command** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

On a Case Wall, the **Execute Command** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully executed command "COMMAND" on the following endpoints in CrowdStrike Falcon: ENTITY_ID` | Action succeeded.  
`Error executing action "Execute Command". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Waiting for results for the following entities: ENTITY_ID` | Asynchronous message.  
  
##### Script result

The following table describes the values for the script result output when using the **Execute Command** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Alert Details

Use the **Get Alert Details** action to retrieve the details of an alert in CrowdStrike Falcon.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Alert Details** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | Required. The unique ID of the alert from which to retrieve details.  
  
#### Action outputs

The **Get Alert Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Get Alert Details** action:
    
    
    {
        "added_privileges": [
            "DomainAdminsRole"
        ],
        "aggregate_id": "aggind:CID_VALUE:AGGREGATE_ID_VALUE",
        "assigned_to_uid": "analyst@example.com",
        "cid": "CID_VALUE",
        "composite_id": "CID_VALUE:ind:CID_VALUE:COMPOSITE_ID_VALUE",
        "confidence": 20,
        "context_timestamp": "2022-11-15T12:58:15.629Z",
        "crawl_edge_ids": {
            "Sensor": [
                "EDGE_ID_1_OBFUSCATED_STRING",
                "EDGE_ID_2_OBFUSCATED_STRING",
                "EDGE_ID_3_OBFUSCATED_STRING"
            ]
        },
        "crawl_vertex_ids": {
            "Sensor": [
                "aggind:CID_VALUE:AGGREGATE_ID_VALUE",
                "idpind:CID_VALUE:IDP_DETECTION_ID",
                "ind:CID_VALUE:DETECTION_ID",
                "uid:CID_VALUE:SOURCE_SID_VALUE"
            ]
        },
        "crawled_timestamp": "2022-11-15T13:58:17.251061883Z",
        "created_timestamp": "2022-11-15T12:59:17.239585706Z",
        "description": "A user received new privileges",
        "display_name": "Privilege escalation (user)",
        "end_time": "2022-11-15T12:58:15.629Z",
        "falcon_host_link": "https://falcon.crowdstrike.com/identity-protection/detections/DETECTION_ID?cid=CID_VALUE",
        "id": "ind:CID_VALUE:DETECTION_ID",
        "name": "IdpEntityPrivilegeEscalationUser",
        "objective": "Gain Access",
        "pattern_id": 51113,
        "previous_privileges": "0",
        "privileges": "8321",
        "product": "idp",
        "scenario": "privilege_escalation",
        "severity": 2,
        "show_in_ui": true,
        "source_account_domain": "EXAMPLE.LOCAL",
        "source_account_name": "TEST_MAILBOX",
        "source_account_object_sid": "S-1-5-21-3479765008-4256118348-3151044947-3595",
        "start_time": "2022-11-15T12:58:15.629Z",
        "status": "new",
        "tactic": "Privilege Escalation",
        "tactic_id": "TA0004",
        "tags": [
            "red_team"
        ],
        "technique": "Valid Accounts",
        "technique_id": "T1078",
        "timestamp": "2022-11-15T12:58:17.239Z",
        "type": "idp-user-endpoint-app-info",
        "updated_timestamp": "2022-11-23T15:22:20.271100181Z"
    }
    

##### Output messages

The **Get Alert Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about the alert with ID ALERT_ID in Crowdstrike.` | The action succeeded.  
`Error executing action "Get Alert Details". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Alert Details** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Event Offset

Use the **Get Event Offset** action to retrieve the event offset used by the Streaming Events Connector.

This action starts processing events from 30 days ago.

This action doesn't run on entities.

#### Action inputs

The **Get Event Offset** action requires the following parameters:

Parameters  
---  
`Max Events To Process` | _Required_ The number of events that the action needs to process starting from 30 days ago.The default value is `10000`.  
  
#### Action outputs

The **Get Event Offset** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Get Event Offset** action:
    
    
    {
    "offset": 100000
    "timestamp": "<code><var>EVENT_TIMESTAMP</var></code>"
    }
    

##### Output messages

The **Get Event Offset** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved event offset in CrowdStrike Falcon. ` | Action succeeded.  
`Error executing action "Get Event Offset". Reason: ERROR_REASON ` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Event Offset** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Host Information

Use the **Get Host Information** action to retrieve information about the hostname from CrowdStrike Falcon.

This action runs on the following entities:

  * Hostname
  * IP address



#### Action inputs

The **Get Host Information** action requires the following parameters:

Parameters  
---  
`Hostname` | _Optional_ A comma-separated list of hostnames to hide in CrowdStrike Falcon. The action processes both the input values provided in this parameter and the Hostname and IP Address entities attached to the case.  
`Device ID` | _Optional_ Comma-separated list of device IDs on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Customer ID` | _Optional_ The unique CrowdStrike Customer ID (CID) used to target a specific tenant. This parameter is required in Falcon Flight Control or multi-tenant environments to perform the action on a specific child CID.  
  
#### Action outputs

The **Get Host Information** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment

The **Get Host Information** action supports the following entity enrichment logic:

Enrichment field | Logic  
---|---  
`modified_timestamp` | Returns if it exists in the JSON result  
`major_version` | Returns if it exists in the JSON result  
`site_name` | Returns if it exists in the JSON result  
`platform_id` | Returns if it exists in the JSON result  
`config_id_platform` | Returns if it exists in the JSON result  
`system_manufacturer` | Returns if it exists in the JSON result  
`meta` | Returns if it exists in the JSON result  
`first_seen` | Returns if it exists in the JSON result  
`service_pack_minor` | Returns if it exists in the JSON result  
`product_type_desc` | Returns if it exists in the JSON result  
`build_number` | Returns if it exists in the JSON result  
`hostname` | Returns if it exists in the JSON result  
`config_id_build` | Returns if it exists in the JSON result  
`minor_version` | Returns if it exists in the JSON result  
`os_version` | Returns if it exists in the JSON result  
`provision_status` | Returns if it exists in the JSON result  
`mac_address` | Returns if it exists in the JSON result  
`bios_version` | Returns if it exists in the JSON result  
`agent_load_flags` | Returns if it exists in the JSON result  
`status` | Returns if it exists in the JSON result  
`bios_manufacturer` | Returns if it exists in the JSON result  
`machine_domain` | Returns if it exists in the JSON result  
`agent_local_time` | Returns if it exists in the JSON result  
`slow_changing_modified_timestamp` | Returns if it exists in the JSON result  
`service_pack_major` | Returns if it exists in the JSON result  
`device_id` | Returns if it exists in the JSON result  
`system_product_name` | Returns if it exists in the JSON result  
`product_type` | Returns if it exists in the JSON result  
`local_ip` | Returns if it exists in the JSON result  
`external_ip` | Returns if it exists in the JSON result  
`cid` | Returns if it exists in the JSON result  
`platform_name` | Returns if it exists in the JSON result  
`config_id_base` | Returns if it exists in the JSON result  
`last_seen` | Returns if it exists in the JSON result  
`pointer_size` | Returns if it exists in the JSON result  
`agent_version` | Returns if it exists in the JSON result  
  
##### JSON result

The following example describes the JSON result output received when using the **Get Host Information** action:
    
    
    [
      {
        "EntityResult": [
          {
            "modified_timestamp": "2019-01-17T13: 44: 57Z",
            "major_version": "10",
            "site_name": "Default-First-Site-Name",
            "platform_id": "0",
            "config_id_platform": "3",
            "system_manufacturer": "ExampleInc.",
            "meta": {
              "version": "1111"
            },
            "first_seen": "2018-04-22T13: 06: 53Z",
            "service_pack_minor": "0",
            "product_type_desc": "Workstation",
            "build_number": "111",
            "hostname": "name",
            "config_id_build": "8104",
            "minor_version": "0",
            "os_version": "Windows10",
            "provision_status": "Provisioned",
            "mac_address": "64-00-6a-2a-43-3f",
            "bios_version": "1.2.1",
            "agent_load_flags": "1",
            "status": "normal",
            "bios_manufacturer": "ExampleInc.",
            "machine_domain": "Domain name",
            "agent_local_time": "2019-01-14T19: 41: 09.738Z",
            "slow_changing_modified_timestamp": "2019-01-14T17: 44: 40Z",
            "service_pack_major": "0",
            "device_id": "example-id",
            "system_product_name": "OptiPlex7040",
            "product_type": "1",
            "local_ip": "192.0.2.1",
            "external_ip": "203.0.113.1",
            "cid": "example-cid",
            "platform_name": "Windows",
            "config_id_base": "65994753",
            "last_seen": "2019-01-17T13: 44: 46Z",
            "pointer_size": "8",
            "agent_version": "4.18.8104.0",
            "recent_logins": [
              {
                "user_name": "test",
                "login_time": "2022-08-10T07:36:38Z"
              },
              {
                "user_name": "test",
                "login_time": "2022-08-10T07:36:35Z"
              }
            ],
            "online_status": "offline"
          }
        ],
        "Entity": "198.51.100.255"
      }
    ]
    

##### Output messages

The **Get Host Information** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following entities using CrowdStrike Falcon: ENTITY_ID` `Action wasn't able to enrich the following entities using CrowdStrike Falcon: ENTITY_ID` | Action succeeded.  
`Error executing action "Get Host Information". Reason: ERROR_REASON ` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Host Information** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Hosts by IOC - Deprecated

**Deprecated:** This action is deprecated.

List hosts related to the IOCs in CrowdStrike Falcon. Supported entities: Hostname, URL, IP Address and Hash.  
**Note:** Hostname entities are treated as domain IOCs. The action extracts the domain part out of URLs. Only the MD5 and SHA-256 hashes are supported.

#### Entities

This action runs on the following entities:

  * IP Address
  * Hostname
  * URL
  * Hash



#### Action inputs

N/A

#### Action outputs

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
     {
      "hash":
       [{
         "modified_timestamp": "2019-01-17T13: 44: 57Z",
         "major_version": "10",
         "site_name": "Example-Name",
         "platform_id": "ExampleID",
         "config_id_platform": "3",
         "system_manufacturer": "ExampleInc.",
         "meta": {"version": "49622"},
         "first_seen": "2018-04-22T13: 06: 53Z",
       "service_pack_minor": "0",
         "product_type_desc": "Workstation",
         "build_number": "14393",
         "hostname": "name",
         "config_id_build": "ExampleID",
         "minor_version": "0",
         "os_version": "Windows10",
         "provision_status": "Provisioned",
         "mac_address": "01:23:45:ab:cd:ef",
         "bios_version": "1.2.1",
         "agent_load_flags": "1",
         "status": "normal",
         "bios_manufacturer": "ExampleInc.",
         "machine_domain": "Example Domain",
         "Device_policies":
             {
               "sensor_update":
                  {
                    "applied": true,
                    "applied_date": "2018-12-11T23: 09: 18.071417837Z",
                    "settings_hash": "65994753|3|2|automatic",
                    "policy_type": "sensor-update",
                    "assigned_date": "2018-12-11T23: 08: 38.16990705Z",
                    "policy_id": "Example ID"
                   }
              },
          "agent_local_time": "2019-01-14T19: 41: 09.738Z",
          "slow_changing_modified_timestamp": "2019-01-14T17: 44: 40Z",
          "service_pack_major": "0", "device_id": "2653595a063e4566519ef4fc813fcc56",
          "system_product_name": "OptiPlex7040",
          "product_type": "1",
          "local_ip": "192.0.2.1",
          "external_ip": "203.0.113.1",
          "cid": "123456789abcdef123456789abcdef12",
          "platform_name": "Windows",
          "config_id_base": "ExampleID",
          "policies":
              [{
                 "applied": true,
                 "applied_date": "2019-01-02T22: 45: 21.315392338Z",
                 "settings_hash": "18db1203",
                 "policy_type": "prevention",
                 "assigned_date": "2019-01-02T22: 45: 11.214774996Z",
                 "policy_id": "Example ID"
              }],
          "last_seen": "2019-01-17T13: 44: 46Z",
          "pointer_size": "8",
          "agent_version": "4.18.8104.0"
       }]
     }
      

##### Entity enrichment

Enrichment field | Logic  
---|---  
modified_timestamp | Returns if it exists in JSON result  
major_version | Returns if it exists in JSON result  
site_name | Returns if it exists in JSON result  
platform_id | Returns if it exists in JSON result  
config_id_platform | Returns if it exists in JSON result  
system_manufacturer | Returns if it exists in JSON result  
meta | Returns if it exists in JSON result  
first_seen | Returns if it exists in JSON result  
service_pack_minor | Returns if it exists in JSON result  
product_type_desc | Returns if it exists in JSON result  
build_number | Returns if it exists in JSON result  
hostname | Returns if it exists in JSON result  
config_id_build | Returns if it exists in JSON result  
minor_version | Returns if it exists in JSON result  
os_version | Returns if it exists in JSON result  
provision_status | Returns if it exists in JSON result  
mac_address | Returns if it exists in JSON result  
bios_version | Returns if it exists in JSON result  
agent_load_flags | Returns if it exists in JSON result  
status | Returns if it exists in JSON result  
bios_manufacturer | Returns if it exists in JSON result  
machine_domain | Returns if it exists in JSON result  
Device_policies | Returns if it exists in JSON result  
agent_local_time | Returns if it exists in JSON result  
slow_changing_modified_timestamp | Returns if it exists in JSON result  
service_pack_major | Returns if it exists in JSON result  
system_product_name | Returns if it exists in JSON result  
product_type | Returns if it exists in JSON result  
local_ip | Returns if it exists in JSON result  
external_ip | Returns if it exists in JSON result  
cid | Returns if it exists in JSON result  
platform_name | Returns if it exists in JSON result  
config_id_base | Returns if it exists in JSON result  
policies | Returns if it exists in JSON result  
last_seen | Returns if it exists in JSON result  
pointer_size | Returns if it exists in JSON result  
agent_version | Returns if it exists in JSON result  
  
##### Entity insight

N/A

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | The action shouldn't fail nor stop a playbook execution:  
_If successful and at least one host related to the provided IOCs is found (is_success=true):_ "Successfully retrieved hosts related to the provided IOCs in CrowdStrike Falcon."  
_If no related hosts are found (is_success=false):_ "No hosts were related to the provided IOCs in CrowdStrike Falcon."  
The action should fail and stop a playbook execution:  
_If a critical error is reported: "_ Error executing action "{action name}". Reason: {traceback}." | General  
  
### Get Process Name by IOC - Deprecated

**Deprecated:** This action is deprecated.

Retrieve processes related to the IOCs and provided devices in CrowdStrike Falcon. Supported entities: Hostname, URL, IP Address and Hash.  
**Note:** Hostname entities are treated as domain IOCs. The action extracts the domain part out of URLs. Only the MD5, SHA-1 and SHA-256 hashes are supported. The IP Address entities are treated as IOCs.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Devices Names | 11 | N/A | Yes | Specify a comma-separated list of devices for which you want to retrieve processes related to entities.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * URL
  * Hash



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
      {
      "EntityResult":
       [{
          "Process Name": "example.exe",
          "Indicator": "986a4715113359b527b15efe1ee09306", "Host Name": "example-name"
         },{
          "Process Name": "example.exe",
          "Indicator": "986a4715113359b527b15efe1ee09306",
          "Host Name": "example-name"
        },{
          "Process Name": "example.exe",
          "Indicator": "986a4715113359b527b15efe1ee09306",
          "Host Name": "example-name"
       }],
       "Entity": "example_entity"
      }
      

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Process Name | Returns if it exists in JSON result  
Indicator | Returns if it exists in JSON result  
Host Name | Returns if it exists in JSON result  
  
##### Entity Insights

N/A

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | The action shouldn't fail nor stop a playbook execution:  
_If found processes related to entities for at least one endpoint (is_success=true):_ "Successfully retrieved processes related to the IOCs on the following endpoints in CrowdStrike Falcon: {device name}."  
_If no processes are found for at least one endpoint or the device is not found (is_success=true): "_ No related processes were found on the following endpoints in CrowdStrike Falcon: {device name}."  
_If_ _no processes are found for all endpoints or none of the devices are found (is_success=false):_ "No related processes were found on the provided endpoints in CrowdStrike Falcon.  
The action should fail and stop a playbook execution:  
_If a critical error is reported:_ "Error executing "{action name}". Reason: {trace back}." |   
  
### Hide Hosts

Use the **Hide Hosts** action to hide one or more hosts from the CrowdStrike Falcon console.

This action runs on the following Google SecOps entities:

  * Hostname
  * IP Address



#### Action inputs

The **Hide Hosts** action requires the following parameters:

Parameter | Description  
---|---  
`Hostname` | Optional. A comma-separated list of hostnames to hide in CrowdStrike Falcon. The action processes both the input values provided in this parameter and the `Hostname` and `IP Address` entities attached to the case.  
`Customer ID` | Optional. The unique CrowdStrike Customer ID (CID) used to target a specific tenant. This parameter is required in Falcon Flight Control or multi-tenant environments to perform the action on a specific child CID.  
  
#### Action outputs

The **Hide Hosts** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Hide Hosts** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully hid the following hosts in Crowdstrike: HOSTS.` `Action wasn't able to hide the following hosts in Crowdstrike: HOSTS.` `None of the provided hosts were hidden.` | The action succeeded.  
`Error executing action "Hide Host". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Hide Hosts** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Lift Contained Endpoint

Use the **Lift Contained Endpoint** action to lift an endpoint containment in CrowdStrike Falcon.

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action inputs

The **Lift Contained Endpoint** action requires the following parameters:

Parameters  
---  
`Customer ID` | _Optional_ Specify the ID of the customer for which you want to execute the action.  
`Device ID` | _Optional_ Comma-separated list of device IDs on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Fail If Timeout` | _Optional_ If selected and containment was not lifted on all endpoints, the action fails. Selected by default.  
  
#### Action outputs

The **Lift Contained Endpoint** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment

The **Lift Contained Endpoint** action supports the following entity enrichment:

Enrichment field | Logic  
---|---  
`status` | Returns if it exists in the JSON result  
`modified_timestamp` | Returns if it exists in the JSON result  
`major_version` | Returns if it exists in the JSON result  
`config_id_platform` | Returns if it exists in the JSON result  
`system_manufacturer` | Returns if it exists in the JSON result  
`device_policies` | Returns if it exists in the JSON result  
`meta` | Returns if it exists in the JSON result  
`pointer_size` | Returns if it exists in the JSON result  
`last_seen` | Returns if it exists in the JSON result  
`agent_local_time` | Returns if it exists in the JSON result  
`first_seen` | Returns if it exists in the JSON result  
`service_pack_major` | Returns if it exists in the JSON result  
`slow_changing_modified_timestamp` | Returns if it exists in the JSON result  
`service_pack_minor` | Returns if it exists in the JSON result  
`system_product_name` | Returns if it exists in the JSON result  
`product_type_desc` | Returns if it exists in the JSON result  
`build_number` | Returns if it exists in the JSON result  
`cid` | Returns if it exists in the JSON result  
`local_ip` | Returns if it exists in the JSON result  
`external_ip` | Returns if it exists in the JSON result  
`hostname` | Returns if it exists in the JSON result  
`config_id_build` | Returns if it exists in the JSON result  
`minor_version` | Returns if it exists in the JSON result  
`platform_id` | Returns if it exists in the JSON result  
`os_version` | Returns if it exists in the JSON result  
`config_id_base` | Returns if it exists in the JSON result  
`provision_status` | Returns if it exists in the JSON result  
`mac_address` | Returns if it exists in the JSON result  
`bios_version` | Returns if it exists in the JSON result  
`platform_name` | Returns if it exists in the JSON result  
`agent_load_flags` | Returns if it exists in the JSON result  
`device_id` | Returns if it exists in the JSON result  
`product_type` | Returns if it exists in the JSON result  
`agent_version` | Returns if it exists in the JSON result  
  
##### JSON result

The following example describes the JSON result output received when using the **Lift Contained Endpoint** action:
    
    
    {
      "EntityResult":
       {
         "status": "contained",
         "modified_timestamp": "2019-06-24T07:47:37Z",
         "major_version": "6", "policies":
          [{
            "applied": "True",
            "applied_date": "2019-04-29T07:40:06.876850888Z",
            "settings_hash": "ce17279e",
            "policy_type": "prevention",
            "assigned_date": "2019-04-29T07:39:55.218651583Z",
            "policy_id": ""
           }],
         "config_id_platform": "example-id",
         "bios_manufacturer": "Example Inc.",
         "system_manufacturer": "Example Corporation",
         "Device_policies":
            {
             "global_config":
               {
                 "applied": "True",
                 "applied_date": "2019-06-03T23:24:04.893780991Z",
                 "settings_hash": "a75911b0",
                 "policy_type": "globalconfig",
                 "assigned_date": "2019-06-03T23:23:17.184432743Z",
                 "policy_id": ""
               },
             "Sensor_update":
               {
                 "applied": "True",
                 "applied_date": "2019-05-30T23:13:55.23597658Z",
                 "settings_hash": "65994753|3|2|automatic;101",
                 "uninstall_protection": "ENABLED",
                 "policy_type": "sensor-update",
                 "assigned_date": "2019-05-30T23:04:31.485311459Z",
                 "policy_id": "9d1e405846de4ebdb63f674866d390dc"
               },
              "Prevention":
               {
                 "applied": "True",
                 "applied_date": "2019-04-29T07:40:06.876850888Z",
                 "settings_hash": "ce17279e",
                 "policy_type": "prevention",
                 "assigned_date": "2019-04-29T07:39:55.218651583Z",
                 "policy_id": ""
                },
              "device_control":
               {
                 "applied": "True",
                 "applied_date": "2019-06-03T23:14:29.800434222Z",
                 "policy_type": "device-control",
                 "assigned_date": "2019-06-03T23:05:17.425127539Z",
                 "policy_id": ""
                },
              "Remote_response":
               {
                 "applied": "True",
                 "applied_date": "2019-04-29T07:40:04.469808388Z",
                 "settings_hash": "f472bd8e",
                 "policy_type": "remote-response",
                 "assigned_date": "2019-04-29T07:39:55.218642441Z",
                 "policy_id": ""
                }
            },
         "meta":
            {"version": "12765"},
         "pointer_size": "8",
         "last_seen": "2019-06-24T07:45:34Z",
         "agent_local_time": "2019-06-18T12:17:06.259Z",
         "first_seen": "2019-04-29T07:39:45Z",
         "service_pack_major": "0",
         "slow_changing_modified_timestamp": "2019-06-23T11:20:42Z",
         "service_pack_minor": "0",
         "system_product_name":"Virtual Machine",
         "product_type_desc": "Server",
         "build_number": "9600",
         "cid": "",
         "local_ip": "192.0.2.1",
         "external_ip": "203.0.113.1",
         "hostname": "example-hostname",
         "config_id_build": "9106",
         "minor_version": "3",
         "platform_id": "0",
         "os_version": "Windows Server 2012 R2",
         "config_id_base": "example-id",
         "provision_status": "Provisioned",
         "mac_address": "01-23-45-ab-cd-ef",
         "bios_version": "090007 ",
         "platform_name": "Windows",
         "agent_load_flags": "1",
         "device_id": "",
         "product_type": "3",
         "agent_version": "5.10.9106.0"
       },
     "Entity": "198.51.100.255"
     }
    

##### Output messages

The **Lift Contained Endpoint** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully lifted containment on the following endpoints in CrowdStrike Falcon: ENTITY_ID` `The following endpoints were not contained in CrowdStrike Falcon: ENTITY_ID` `The following endpoints were not found in CrowdStrike Falcon: ENTITY_ID` | Action succeeded.  
`Waiting for containment lift to finish for the following endpoints: ENTITY_ID` | Asynchronous message.  
`Error executing action "Lift Contained Endpoint". Reason: the following endpoints initiated containment lift, but were not able to finish it during action execution: ENTITY_ID` | Action failed.Check the endpoint status and the `Fail If Timeout` parameter value.  
`Error executing action "Lift Contained Endpoint". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Lift Contained Endpoint** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Host Vulnerabilities

Use the **List Host Vulnerabilities** action to list vulnerabilities found on the host in CrowdStrike Falcon.

This action requires a Falcon Spotlight license and permissions.

This action runs on the following entities:

  * IP address
  * Hostname



#### Action inputs

The **List Host Vulnerabilities** action requires the following parameters:

Parameters  
---  
`Customer ID` | _Optional_ Specify the ID of the customer for which you want to execute the action.  
`Device ID` | _Optional_ Comma-separated list of device IDs on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Severity Filter` | _Optional_ Specify a comma-separated list of severities for vulnerabilities. If nothing is provided, the action ingests all related vulnerabilities. Possible values: `Critical`, `High`, `Medium`, `Low`, `Unknown`.  
`Create Insight` | _Optional_ If selected, the action creates an insight per entity containing statistical information about related vulnerabilities. Selected by default.  
`Max Vulnerabilities To Return` | _Optional_ Specify how many vulnerabilities to return per host. If nothing is provided, the action processes all related vulnerabilities. The default value is `100`.  
  
#### Action outputs

The **List Host Vulnerabilities** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

On a Case Wall, the **List Host Vulnerabilities** action provides the following table:

Type: Entity

Columns:

  * Name
  * Score
  * Severity
  * Status
  * App
  * Has Remediation



##### JSON result

The following example describes the JSON result output received when using the **List Host Vulnerabilities** action:
    
    
    {
        "statistics": {
            "total": 123,
            "severity": {
                "critical": 1,
                "high": 1,
                "medium": 1,
                "low": 1,
                "unknown": 1
            },
            "status": {
                "open": 1,
                "reopened": 1
            },
            "has_remediation": 1
        },
        "details": [
            {
                "id": "74089e36ac3a4271ab14abc076ed18eb_fff6de34c1b7352babdf7c7d240749e7",
                "cid": "123456789abcdef123456789abcdef12",
                "aid": "74089e36ac3a4271ab14abc076ed18eb",
                "created_timestamp": "2021-05-12T22:45:47Z",
                "updated_timestamp": "2021-05-12T22:45:47Z",
                "status": "open",
                "cve": {
                    "id": "CVE-2021-28476",
                    "base_score": 9.9,
                    "severity": "CRITICAL",
                    "exploit_status": 0
                },
                "app": {
                    "product_name_version": "Example 01"
                },
                "apps": [
                    {
                        "product_name_version": "Example 01",
                        "sub_status": "open",
                        "remediation": {
                            "ids": [
                                "acc34cd461023ff8a966420fa8839365"
                            ]
                        }
                    }
                ],
                "host_info": {
                    "hostname": "example-hostname",
                    "local_ip": "192.0.2.1",
                    "machine_domain": "",
                    "os_version": "Windows 10",
                    "ou": "",
                    "site_name": "",
                    "system_manufacturer": "Example Inc.",
                    "groups": [],
                    "tags": [],
                    "platform": "Windows"
                },
                "remediation": [
                    {
                        "id": "acc34cd461023ff8a966420fa8839365",
                        "reference": "KB5003169",
                        "title": "Update Microsoft Windows 10 1909",
                        "action": "Install patch for Microsoft Windows 10 1909 x64 (Workstation): Security Update ABCDEF",
                        "link": "https://example.com/ABCDEF"
                    }
                ]
            }
        ]
    }
    

##### Output messages

The **List Host Vulnerabilities** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved vulnerabilities for the following hosts: ENTITIES` `No vulnerabilities were found for the following hosts: ENTITIES` | Action succeeded.  
`Error executing action "List Host Vulnerabilities". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "List Host Vulnerabilities". Reason: Invalid value provided in the Severity Filter parameter. Possible values: Critical, High, Medium, Low, Unknown.` | Action failed.Check the `Severity Filter` parameter value.  
  
##### Script result

The following table describes the values for the script result output when using the **List Host Vulnerabilities** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Hosts

Use the **List Hosts** action to list available hosts in CrowdStrike Falcon.

This action runs on all entities.

#### Action inputs

The **List Hosts** action requires the following parameters:

Parameters  
---  
`Filter Logic` | _Optional_ A logic to use when searching for hosts. The default value is `Equals`. The possible values are as follows: 

  * `Equals`
  * `Contains`

  
`Filter Value` | _Optional_ A value to use for host filtering.  
`Max Hosts To Return` | _Optional_ The number of hosts to return.The default value is `50`. The maximum value is `1000`.  
  
#### Action outputs

The **List Hosts** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **List Hosts** action:
    
    
    [{
       "modified_timestamp": "2019-05-15T15:03:12Z",
       "platform_id": "0",
       "config_id_platform": "3",
       "system_manufacturer": "Example Corporation",
       "meta": {"version": "4067"},
       "first_seen": "2019-04-29T07:39:45Z",
       "service_pack_minor": "0",
       "product_type_desc": "Server",
       "build_number": "9600",
       "hostname": "example-hostname",
       "config_id_build": "8904",
       "minor_version": "3",
       "os_version": "Windows Server 2012 R2",
       "provision_status": "Provisioned",
       "mac_address": "01:23:45:ab:cd:ef",
       "bios_version": "090007 ",
       "agent_load_flags": "0",
       "status": "normal",
       "bios_manufacturer": "Example Inc.",
       "device_policies":
         {
          "Sensor_update":
             {
               "applied": true,
               "applied_date": "2019-05-02T22:05:09.577000651Z",
               "settings_hash": "65994753|3|2|automatic",
               "policy_type": "sensor-update",
               "assigned_date": "2019-05-02T22:03:36.804382667Z",
               "policy_id": "9d1e405846de4ebdb63f674866d390dc"
              },
          "remote_response":
              {
                "applied": true,
                "applied_date": "2019-04-29T07:40:04.469808388Z",
                "settings_hash": "f472bd8e",
                "policy_type": "remote-response",
                "assigned_date": "2019-04-29T07:39:55.218642441Z",
                "policy_id": "21e4fb4dedd74c6fb0bcd6a348aa046c"
               },
         "device_control":
              {
                "applied": true,
                "applied_date": "2019-04-29T07:40:06.896362608Z",
                "assigned_date": "2019-04-29T07:39:55.218637999Z",
                "policy_type": "device-control",
                "policy_id": "c360df7193364b23aa4fc47f0238c899"
               },
         "prevention":
               {
                "applied": true,
                "applied_date": "2019-04-29T07:40:06.876850888Z",
                "settings_hash": "ce17279e",
                "policy_type": "prevention",
                "assigned_date": "2019-04-29T07:39:55.218651583Z",
                "policy_id": "7efdf97d7805402186b61151e8abd745"
               },
         "global_config":
              {
                "applied": true,
                "applied_date": "2019-04-29T07:45:18.94807838Z",
                "settings_hash": "3d78f9ab",
                "policy_type": "globalconfig",
                "assigned_date": "2019-04-29T07:45:08.165941325Z",
                "policy_id": "985b1a25afcb489ea442d2d1430b1679"
               }
          },
       "cid": "123456789abcdef123456789abcdef12",
       "agent_local_time": "2019-05-02T22:05:00.015Z",
       "slow_changing_modified_timestamp": "2019-05-02T22:05:09Z",
       "service_pack_major": "0",
       "device_id": "0ab8bc6d968b473b72a5d11a41a24c21",
       "system_product_name": "Virtual Machine",
       "product_type": "3",
       "local_ip": "192.0.2.1",
       "external_ip": "203.0.113.1",
       "major_version": "6",
       "platform_name": "Windows",
       "config_id_base": "65994753",
       "policies":
         [{
            "applied": true,
            "applied_date": "2019-04-29T07:40:06.876850888Z",
            "settings_hash": "ce17279e",
            "policy_type": "prevention",
            "assigned_date": "2019-04-29T07:39:55.218651583Z",
            "policy_id": "7efdf97d7805402186b61151e8abd745"
          }],
       "agent_version": "4.26.8904.0",
       "pointer_size": "8",
       "last_seen": "2019-05-15T15:01:23Z"
     },
     {
      "modified_timestamp": "2019-05-13T07:24:36Z",
      "site_name": "Example-Site-Name",
      "config_id_platform": "3",
      "system_manufacturer": "Example Inc.",
      "meta": {"version": "14706"},
      "first_seen": "2018-04-17T11:02:20Z",
      "platform_name": "Windows",
      "service_pack_minor": "0",
      "product_type_desc": "Workstation",
      "build_number": "17134",
      "hostname": "example-hostname",
      "config_id_build": "8904",
      "minor_version": "0",
      "os_version": "Windows 10",
      "provision_status": "Provisioned",
      "mac_address": "01:23:45:ab:cd:ef",
      "bios_version": "1.6.5",
      "agent_load_flags": "0",
      "status": "normal",
      "bios_manufacturer": "Example Inc.",
      "machine_domain": "example.com",
      "device_policies":
         {
           "sensor_update":
             {
              "applied": true,
              "applied_date": "2019-05-05T12:52:23.121596885Z",
              "settings_hash": "65994753|3|2|automatic",
              "policy_type": "sensor-update",
              "assigned_date": "2019-05-05T12:51:37.544605747Z",
              "policy_id": "9d1e405846de4ebdb63f674866d390dc"
             },
           "Remote_response":
             {
              "applied": true,
              "applied_date": "2019-02-10T07:57:59.064362539Z",
              "settings_hash": "f472bd8e",
              "policy_type": "remote-response",
              "assigned_date": "2019-02-10T07:57:50.610924385Z",
              "policy_id": "21e4fb4dedd74c6fb0bcd6a348aa046c"
             },
          "device_control":
              {
                "applied": true,
                "applied_date": "2019-03-25T15:01:28.51681072Z",
                "assigned_date": "2019-03-25T15:00:22.442519168Z",
                "policy_type": "device-control",
                "policy_id": "c360df7193364b23aa4fc47f0238c899"
              },
          "Prevention":
              {
                "applied": true,
                "applied_date": "2019-04-04T06:54:06.909774295Z",
                "settings_hash": "ce17279e",
                "policy_type": "prevention",
                "assigned_date": "2019-04-04T06:53:57.135897343Z",
                "policy_id": "7efdf97d7805402186b61151e8abd745"
              },
          "global_config":
              {
                "applied": true,
                "applied_date": "2019-02-10T07:57:53.70275875Z",
                "settings_hash": "3d78f9ab",
                "policy_type": "globalconfig",
                "assigned_date": "2019-02-10T07:57:50.610917888Z",
                "policy_id": "985b1a25afcb489ea442d2d1430b1679"
               }
         },
     "cid": "123456789abcdef123456789abcdef12",
     "agent_local_time": "2019-05-05T15:52:08.172Z",
     "slow_changing_modified_timestamp": "2019-05-12T12:37:35Z",
     "service_pack_major": "0",
     "device_id": "cb4493e4af2742b068efd16cb48b7260",
     "system_product_name": "example-name",
     "product_type": "1",
     "local_ip": "192.0.2.1",
     "external_ip": "203.0.113.1",
     "major_version": "10",
     "platform_id": "0",
     "config_id_base": "65994753",
     "policies":
        [{
           "applied": true,
           "applied_date": "2019-04-04T06:54:06.909774295Z",
           "settings_hash": "ce17279e",
           "policy_type": "prevention",
           "assigned_date": "2019-04-04T06:53:57.135897343Z",
           "policy_id": "7efdf97d7805402186b61151e8abd745"
         }],
     "agent_version": "4.26.8904.0",
     "pointer_size": "8",
     "last_seen": "2019-05-13T07:21:30Z"
    },
    {
      "modified_timestamp": "2019-05-09T14:22:50Z",
      "site_name": "Example-Site-Name",
      "config_id_platform": "3",
      "system_manufacturer": "Dell Inc.",
      "meta": {"version": "77747"},
      "first_seen": "2018-07-01T12:19:23Z",
      "platform_name": "Windows",
     "service_pack_minor": "0",
     "product_type_desc": "Workstation",
     "build_number": "17134",
     "hostname":"example-hostname",
     "config_id_build": "8904",
     "minor_version": "0",
     "os_version": "Windows 10",
     "provision_status": "Provisioned",
     "mac_address": "01:23:45:ab:cd:ef",
     "bios_version": "1.2.1",
     "agent_load_flags": "0",
     "status": "normal",
     "bios_manufacturer": "Example Inc.",
     "machine_domain": "example.com",
     "device_policies":
        {
          "sensor_update":
           {
             "applied": true,
             "applied_date": "2019-05-02T22:10:50.336101107Z",
             "settings_hash": "65994753|3|2|automatic",
             "policy_type": "sensor-update",
             "assigned_date": "2019-05-02T22:10:50.336100731Z",
             "policy_id": "9d1e405846de4ebdb63f674866d390dc"
            },
          "remote_response":
           {
             "applied": true,
             "applied_date": "2019-02-08T02:46:31.919442939Z",
             "settings_hash": "f472bd8e",
             "policy_type": "remote-response",
             "assigned_date": "2019-02-08T02:46:22.219718098Z",
             "policy_id": "21e4fb4dedd74c6fb0bcd6a348aa046c"
            },
     "device_control":
         {
           "applied": true,
           "applied_date": "2019-03-24T16:43:31.777981725Z",
           "assigned_date": "2019-03-24T16:42:21.395540493Z",
           "policy_type": "device-control",
           "policy_id": "c360df7193364b23aa4fc47f0238c899"
         },
     "prevention":
         {
          "applied": true,
          "applied_date": "2019-04-03T23:58:50.870694195Z",
          "settings_hash": "ce17279e",
          "policy_type": "prevention",
          "assigned_date": "2019-04-03T23:57:22.534513932Z",
          "policy_id": "7efdf97d7805402186b61151e8abd745"
         },
     "global_config":
         {
          "applied": true,
          "applied_date": "2019-02-08T01:14:14.810607774Z",
          "settings_hash": "3d78f9ab",
          "policy_type": "globalconfig",
          "assigned_date": "2019-02-08T01:14:05.585922067Z",
          "policy_id": "985b1a25afcb489ea442d2d1430b1679"
          }
     },
      "cid": "123456789abcdef123456789abcdef12",
      "agent_local_time": "2019-05-03T01:10:29.340Z",
      "slow_changing_modified_timestamp": "2019-05-02T22:10:46Z",
      "service_pack_major": "0",
      "device_id": "1c2f1a7f88f8457f532f1c615f07617b",
      "system_product_name": "Example Name",
      "product_type": "1",
      "local_ip": "192.0.2.1",
      "external_ip": "203.0.113.1",
      "major_version": "10",
      "platform_id": "0",
      "config_id_base": "65994753",
      "policies":
         [{
           "applied": true,
           "applied_date": "2019-04-03T23:58:50.870694195Z",
           "settings_hash": "ce17279e",
           "policy_type": "prevention",
           "assigned_date": "2019-04-03T23:57:22.534513932Z",
           "policy_id": "7efdf97d7805402186b61151e8abd745"
         }],
     "agent_version": "4.26.8904.0",
     "pointer_size": "8",
     "last_seen": "2019-05-09T14:20:53Z"
    }]
    

##### Output messages

The **List Hosts** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved available hosts based on the provided criteria.` `No hosts were found for the provided criteria.` | Action succeeded.  
`Error executing action "List Hosts". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **List Hosts** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Uploaded IOCs

Use the **List Uploaded IOCs** action ton list available custom IOCs in CrowdStrike Falcon.

This action runs on all entities.

#### Action inputs

The **List Uploaded IOCs** action requires the following parameters:

Parameters  
---  
`IOC Type Filter` | _Optional_ A comma-separated list of IOC types to return. The default value is `ipv4,ipv6,md5,sha1,sha256,domain`. The possible values are as follows: 

  * `ipv4`
  * `ipv6`
  * `md5`
  * `sha1`
  * `sha256`
  * `domain`

  
`Value Filter Logic` | _Optional_ A value of the filter logic.The default value is `Equal`. The possible values are as follows: 

  * `Equal`
  * `Contains`

If `Equal` is set, the action attempts to find the exact match among IOCs.  
If `Contains` is set, the action attempts to find IOCs containing the selected substring.  
`Value Filter String` | _Optional_ A string to search among IOCs.  
`Max IOCs To Return` | _Optional_ The number of IOCs to return.The default value is `50`. The maximum value is 500.  
  
#### Action outputs

The **List Uploaded IOCs** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

On a Case Wall, the **List Uploaded IOCs** action provides the following table:

Columns: 

  * Action
  * Severity
  * Signed
  * AV Hits
  * Platforms 
  * Tags
  * Created At
  * Created By



##### JSON result

The following example describes the JSON result output received when using the **List Uploaded IOCs** action:
    
    
    {
                "id": "fbe8c2739f3c6df95e62e0ae54569974437b2d9306eaf6740134ccf1a05e23d3",
                "type": "sha256",
                "value": "8a86c4eecf12446ff273afc03e1b3a09a911d0b7981db1af58cb45c439161295",
                "action": "no_action",
                "severity": "",
                "metadata": {
                    "signed": false,
                    "av_hits": -1
                },
                "platforms": [
                    "windows"
                ],
                "tags": [
                    "Hashes 22.Nov.20 15:29 (Windows)"
                ],
                "expired": false,
                "deleted": false,
                "applied_globally": true,
                "from_parent": false,
                "created_on": "2021-04-22T03:54:09.235120463Z",
                "created_by": "internal@example.com",
                "modified_on": "2021-04-22T03:54:09.235120463Z",
                "modified_by": "internal@example.com"
            }
    

##### Output messages

The **List Uploaded IOCs** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found custom IOCs for the provided criteria in CrowdStrike Falcon.` | Action succeeded.  
`Error executing action "List Uploaded IOCs". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "List Uploaded IOCs". Reason: "IOC Type Filter" contains an invalid value. Please check the spelling. Possible values: ipv4, ipv6, md5, sha1, sha256, domain.` | Action failed.Check the spelling and the `IOC Type Filter` parameter value.  
  
##### Script result

The following table describes the values for the script result output when using the **List Uploaded IOCs** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### On-Demand Scan

Use the **On-Demand Scan** action to scan the endpoint on demand in CrowdStrike.

This action only runs on Windows hosts and the following entities:

  * IP address
  * Hostname



The **On-Demand Scan** action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE, if necessary.

#### Action inputs

The **On-Demand Scan** action requires the following parameters:

Parameters  
---  
`Customer ID` | _Optional_ Specify the ID of the customer for which you want to execute the action.  
`File Paths To Scan` | _Required_ Comma-separated list of paths to scan. The default value is `C:\Windows`.  
`File Paths To Exclude From Scan` | _Optional_ Comma-separated list of paths to exclude from scanning.  
`Host Group Name` | _Optional_ Comma-separated list of host group names to initiate scanning for. **Note:** A separate scanning process is created for each host group.  
`Scan Description` | _Optional_ Description for the scan. If no value is provided, the action sets the description to `Scan initialized by Chronicle SecOps.`  
`CPU Priority` | _Optional_ The amount of CPU to use for the underlying host during scanning. Possible values: `Up to 1% CPU utilization`, `Up to 25% CPU utilization`, `Up to 50% CPU utilization`, `Up to 75% CPU utilization`, `Up to 100% CPU utilization`. The default value is `Up to 25% CPU utilization`.  
`Sensor Anti-malware Detection Level` | _Optional_ Specify the sensor anti-malware detection level. **Note:** Detection level must be equal to or higher than the Prevention level. Possible values: `Cautious`, `Moderate`, `Aggressive`, `Extra Aggressive`. The default value is `Moderate`.  
`Sensor Anti-malware Prevention Level` | _Optional_ Specify the sensor anti-malware prevention level. **Note:** Detection level must be equal to or higher than the Prevention level. Possible values: `Cautious`, `Moderate`, `Aggressive`, `Extra Aggressive`, `Disabled`. The default value is `Moderate`.  
`Cloud Anti-malware Detection Level` | _Optional_ Specify the cloud anti-malware detection level. **Note:** Detection level must be equal to or higher than the Prevention level. Possible values: `Cautious`, `Moderate`, `Aggressive`, `Extra Aggressive`. The default value is `Moderate`.  
`Cloud Anti-malware Prevention Level` | _Optional_ Specify the cloud anti-malware prevention level. **Note:** Detection level must be equal to or higher than the Prevention level. Possible values: `Cautious`, `Moderate`, `Aggressive`, `Extra Aggressive`, `Disabled`. The default value is `Moderate`.  
`Quarantine Hosts` | _Optional_ If selected, underlying hosts are quarantined as part of scanning. Not selected by default.  
`Create Endpoint Notification` | _Optional_ If selected, the scanning process creates an endpoint notification. Selected by default.  
`Max Scan Duration` | _Optional_ Number of hours for a scan to run. If no value is provided, the scan runs continuously. The default value is `1`.  
`Hostname` | _Optional_ Comma-separated list of hostnames on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Device ID` | _Optional_ Comma-separated list of device IDs on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
  
#### Action outputs

The **On-Demand Scan** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **On-Demand Scan** action:
    
    
    {
     "id": "ID",
     "cid": "123456789abcdef123456789abcdef12",
     "profile_id": "c94149b9a52d4c76b027e63a88dcc710",
     "description": "test APIS ",
     "file_paths": [
         "C:\\Windows"
     ],
     "initiated_from": "falcon_adhoc",
     "quarantine": true,
     "cpu_priority": 1,
     "preemption_priority": 1,
     "metadata": [
         {
             "host_id": "HOST_ID",
             "host_scan_id": "909262bd2fff664282a46464d8625a62",
             "scan_host_metadata_id": "815dae51d8e543108ac01f6f139f42b1",
             "filecount": {
                 "scanned": 16992,
                 "malicious": 0,
                 "quarantined": 0,
                 "skipped": 124998,
                 "traversed": 198822
             },
             "status": "completed",
             "started_on": "2024-02-05T13:55:45.25066635Z",
             "completed_on": "2024-02-05T14:11:18.092427363Z",
             "last_updated": "2024-02-05T14:11:18.092431457Z"
         }
     ],
     "filecount": {
         "scanned": 16992,
         "malicious": 0,
         "quarantined": 0,
         "skipped": 124998,
         "traversed": 198822
     },
     "targeted_host_count": 1,
     "completed_host_count": 1,
     "status": "completed",
     "hosts": [
         "86db81f390394cb080417a1ffb7d46fd"
     ],
     "endpoint_notification": true,
     "pause_duration": 2,
     "max_duration": 1,
     "max_file_size": 60,
     "sensor_ml_level_detection": 2,
     "sensor_ml_level_prevention": 2,
     "cloud_ml_level_detection": 2,
     "cloud_ml_level_prevention": 2,
     "policy_setting": [
         26439818674573,
     ],
     "scan_started_on": "2024-02-05T13:55:45.25Z",
     "scan_completed_on": "2024-02-05T14:11:18.092Z",
     "created_on": "2024-02-05T13:55:43.436807525Z",
     "created_by": "88f5d9e8284f4b85b92dab2389cb349d",
     "last_updated": "2024-02-05T14:14:18.776620391Z"
    }
    

##### Output messages

The **On-Demand Scan** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully scanned and returned results for the following hosts in CrowdStrike: ENTITIES ` `Action couldn't start a scan on the following hosts in CrowdStrike: ENTITIES. They are either not found or non-Windows instances.` `None of the provided hosts were found or none of the hosts were Windows instances. No scans have been created.` `Successfully scanned and returned results for the following host groups in CrowdStrike: HOST_GROUPS ` `The following host groups were not found in CrowdStrike: HOST_GROUPS` `None of the provided host groups were found in CrowdStrike.` `Waiting for scan results for the following entities or host groups: ENTITIES_OR_HOST_GROUPS ` | Action succeeded.  
`Error executing action "On-Demand Scan". Reason: ERROR_REASON` `Error executing action "On-Demand Scan". Reason: Detection level should be equal to or higher than the Prevention level. Please check the corresponding parameters.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **On-Demand Scan** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test connectivity to the CrowdStrike Falcon.

This action runs on all entities.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Run Script

Use the **Run Script** action to execute a PowerShell script on the endpoints in CrowdStrike.

This action is asynchronous. Adjust the script timeout value in the Google SecOps IDE, if necessary.

This action runs on the IP address and Hostname entities.

#### Action inputs

The **Run Script** action requires the following parameters:

Parameters  
---  
`Customer ID` | _Optional_ Specify the ID of the customer for which you want to execute the action.  
`Script Name` | _Optional_ The name of the script file that needs to be executed. **Note:** Either `Script Name` or `Raw Script` must be provided. If both are provided, `Raw Script` takes priority.  
`Raw Script` | _Optional_ Raw PowerShell script payload that needs to be executed on the endpoints. **Note:** Either `Script Name` or `Raw Script` must be provided. If both are provided, `Raw Script` takes priority.  
`Hostname` | _Optional_ Comma-separated list of hostnames on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Device ID` | _Optional_ Comma-separated list of device IDs on which you want to execute the action. **Note:** The action executes on both the entities attached to the case and these parameter values.  
`Queue Offline` | _Optional_ If selected, commands targeting offline hosts are queued and executed once the host reconnects to the network. Not selected by default.  
  
#### Action outputs

The **Run Script** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

On a Case Wall, the **Run Script** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully executed script SCRIPT_OR_PAYLOAD on the following endpoints in CrowdStrike: ENTITIES ` `Action wasn't able to execute script SCRIPT_OR_PAYLOAD on the following endpoints in CrowdStrike: ENTITIES ` `Script wasn't executed on the provided endpoints in CrowdStrike. ` `Waiting for the scripts to finish execution on the following endpoints: ENTITIES` | Action succeeded.  
`Error executing action "Run Script". Reason: ERROR_REASON` `Error executing action "Run Script". Reason: either "Script Name" or "Raw Script" should be provided.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Run Script** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Events

Use this action to search events in CrowdStrike. Note: Action is running as async, please adjust script timeout value in Google SecOps IDE for action, as needed.

This action doesn't run on entities.

#### Action inputs

The **Search Events** action requires the following parameters:

Parameters  
---  
`Repository` | _Required_ Repository that should be searched. Possible values are as follows:

  * `All`
  * `Falcon`
  * `Third Party`
  * `IT Automation`
  * `Forensics`

  
`Query` | _Required_ Query that needs to be executed in CrowdStrike. Note: don't provide "head" as part of the query. Action will provide it automatically based on the value provided in the "Max Results To Return" parameter.  
`Time Frame` | _Optional_ Timeframe for the results. If "Custom" is selected, you also need to provide "Start Time". Last Hour Possible Values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

  
`Start Time` | _Optional_ Start time for the results. If "Custom" is selected for the "Time Frame" parameter, this parameter is mandatory. Format: ISO 8601.  
`End Time` | _Optional_ How many results to return for the query. Action will append "head" to the provided query. Default: 50. Maximum: 1000.  
  
#### Action outputs

The **Search Events** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Output messages

On a Case Wall, the **Search Events** action provides the following output messages:

Output message | Message description  
---|---  
` Successfully returned results for the query "{query}" in CrowdStrike.`   
`No results were found for the query "{query}" in CrowdStrike`   
`Waiting for the search job to finish...`   
| The action shouldn't fail or stop a playbook execution.  
`Error executing action "Search Events". Reason: {0}''.format(error.Stacktrace)`   
`Error executing action "Search Events". Reason: {0}''.format(message)`   
`Error executing action "Search Events". Reason: query Job {query id} has expired. Please decrease the async polling interval.`   
|  Action failed.  
  
##### Script result

The following table describes the values for the script result output when using the **Search Events** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Submit File

Use the **Submit File** action to submit files to a sandbox in CrowdStrike.

This action requires a Falcon Sandbox license.

This action doesn't run on entities.

#### Supported file and archive formats

According to the CrowdStrike portal, the sandbox supports the following file formats:

Supported file formats  
---  
`.exe`, `.scr`, `.pif`, `.dll`, `.com`, `.cpl` | Portable executables  
`.doc`, `.docx`, `.ppt`, `.pps`, `.pptx`, `.ppsx`, `.xls`, `.xlsx`, `.rtf`, `.pub` | Office documents  
`.pdf` | PDF  
`.apk` | APK  
`.jar` | Executable JAR  
`.sct` | Windows script component  
`.lnk` | Windows shortcut  
`.chm` | Windows help  
`.hta` | HTML application  
`.wsf` | Windows script file  
`.js` | JavaScript  
`.vbs`, `.vbe` | Visual Basic  
`.swf` | Shockwave Flash  
`.pl` | Perl  
`.ps1`, `.psd1`, `.psm1` | Powershell  
`.svg` | Scalable vector graphics  
`.py` | Python  
`.elf` | Linux ELF executables  
`.eml` | Email files: MIME RFC 822  
`.msg` | Email files: Outlook  
  
According to the CrowdStrike portal, the sandbox supports the following archive formats:

  * `.zip`
  * `.7z`



#### Action inputs

The **Submit File** action requires the following parameters:

Parameters  
---  
`File Paths` | _Required_ A list of absolute paths to the files submitted. The format depends on your deployment:

  * **SaaS deployment** \- The paths are internal to the hosted platform.
  * **Remote Deployment** \- The paths must be absolute, valid file paths on the local machine where the Remote Agent is installed (such as, `C:\temp\download` for Windows or `/var/tmp/download/` for Linux).

For a list of the supported file formats, refer to Supported file and archive formats.  
`Sandbox Environment` | _Optional_ A sandbox environment to analyze.The default value is `Windows 10, 64-bit`.Possible values are as follows:

  * `Linux Ubuntu 16.04, 64-bit`
  * `Android (static analysis)`
  * `Windows 10, 64-bit`
  * `Windows 7, 64-bit`
  * `Windows 7, 32-bit`

  
`Network Environment` | _Optional_ A network environment to analyze.The default value is `Default`.Possible values are as follows: 

  * `Default`
  * `TOR`
  * `Offline`
  * `Simulated`

  
`Archive Password` | _Optional_ A password to use when working with archive files.  
`Document Password` | _Optional_ A password to use when working with Adobe or Office files. The maximum password length is 32 characters.  
`Check Duplicate` | _Optional_ If selected, the action checks if the file was already submitted previously and returns the available report.During validation, the action doesn't consider the `Network Environment` and the `Sandbox Environment ` parameters. Selected by default.  
`Comment` | _Optional_ A comment to submit.  
`Confidential Submission` | _Optional_ If selected, the file is only shown to users within your customer account.  Not selected by default.  
  
#### Action outputs

The **Submit File** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

On a Case Wall, the **Submit File** action provides the following table:

Columns:

  * Results
  * Name
  * Threat Score
  * Verdict
  * Tags



##### Output messages

The **Submit File** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about the following files using CrowdStrike: PATHS` `Action wasn't able to return details about the following files using CrowdStrike: PATHS` | Action succeeded.  
`Action wasn't able to submit the following samples, because file type is not supported:  NOT_SUPPORTED_FILES. Please refer to the doc portal for a list of supported files.` `None of the samples were submitted, because file type is not supported. Please refer to the doc portal for a list of supported files.` `None of the samples in the archive were submitted, because file type is not supported. Please refer to the doc portal for a list of supported files.` | The action returned an error.Check the supported file formats for this action.   
`Waiting for results for the following files: PATHS` | Asynchronous message.  
`Error executing action "Submit File". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "Submit File". Reason: action ran into a timeout during execution. Pending files: FILES_IN_PROGRESS. Please increase the timeout in IDE.` | Action failed.Increase the timeout in IDE.  
  
##### Script result

The following table describes the values for the script result output when using the **Submit File** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Submit URL

Use the **Submit URL** action to submit URLs to a sandbox in CrowdStrike.

This action requires a Falcon Sandbox license. To check what file formats the sandbox supports, refer to the Supported file and archive formats section of this document.

This action doesn't run on entities.

#### Action inputs

The **Submit URL** action requires the following parameters:

Parameters  
---  
`URLs` | _Required_ URLs to submit.  
`Sandbox Environment` | _Optional_ A sandbox environment to analyze. The default value is `Windows 10, 64-bit`.Possible values are as follows:

  * `Linux Ubuntu 16.04, 64-bit`
  * `Android (static analysis)`
  * `Windows 10, 64-bit`
  * `Windows 7, 64-bit`
  * `Windows 7, 32-bit`

  
`Network Environment` | _Optional_ A network environment to analyze.The default value is `Default`.Possible values are as follows: 

  * `Default`
  * `TOR`
  * `Offline`
  * `Simulated`

  
`Check Duplicate` | _Optional_ If selected, the action checks if the URL was already submitted previously and returns the available report. During validation, the action doesn't consider the `Network Environment` and the `Sandbox Environment` parameters. Selected by default.  
  
#### Action outputs

The **Submit URL** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Submit URL** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about the following URLs using CrowdStrike: PATHS` `Action wasn't able to return details about the following URLs using CrowdStrike: PATHS` | Action succeeded.  
`Waiting for results for the following URLs: PATHS` | Asynchronous message.  
`Error executing action "Submit URL". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "Submit URL". Reason: action ran into a timeout during execution. Pending files: FILES_IN_PROGRESS. Please increase the timeout in IDE.` | Action failed.Increase the timeout in IDE.  
  
##### Script result

The following table describes the values for the script result output when using the **Submit URL** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Alert

Use the **Update Alert** action to update alerts in CrowdStrike Falcon.

This action doesn't run on entities.

#### Action inputs

The **Update Alert** action requires the following parameters:

Parameters  
---  
`Alert ID` | _Required_ The ID of the alert to update.  
`Status` | _Optional_ The status of the alert.Possible values are as follows:

  * `Closed`
  * `In Progress`
  * `New`
  * `Reopened`

  
`Verdict` | _Optional_ The verdict for the alert.Possible values are as follows:

  * `True Positive`
  * `False Positive`

  
`Assign To` | _Optional_ The name of the analyst to assign the alert to. If you provide `Unassign` as a parameter value, the action removes an assignment from the alert.The API accepts any value even if the provided user doesn't exist in the system.  
  
#### Action outputs

The **Update Alert** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Update Alert** action:
    
    
    {
        "added_privileges": [
            "DomainAdminsRole"
        ],
        "aggregate_id": "aggind:ID",
        "assigned_to_uid": "example@example.com",
        "cid": "123456789abcdef123456789abcdef12",
        "composite_id": "123456789abcdef123456789abcdef12:ind:ID",
        "confidence": 20,
        "context_timestamp": "2022-11-15T12:58:15.629Z",
        "crawl_edge_ids": {
            "Sensor": [
                "N6KIZ`%V`&d#&#sRaHNV[f3[CA4lr/C_N;.JnbglJpdg8TCCTqnr!9D\\['ALM&eNbPq?kt$#@]+01Ac[&th0-0]E'J8:]mFV?'g5HZ/$B.%BC29_`4U_?%a)_&#k>,G>:=E>%[7^<aLSVj=`UCMcRUH[a9/*^hO_7Ft(js#P<M<(eG3(B=I8rr",
                "XNXnKK.mi:ckQ^2c7AGRMK^'rd:p[_JkD_5ZM$W:d'J8oN:42nj.Ho1-^E5D16b0VALJ`2cDEEJTVdY\\n.-WQ^_B[7$1pH[Glgm@go]-LB%M1,c#2F)nli-Ge#V<=[!c_jh8e3D8E-S0FheDm*BHh-P/s6q!!*'!",
                "N6L*L\">LGfi/.a$IkpaFlWjT.YU#P@Gu8Qe6'0SK=M]ChI,FQXqo=*M(QR+@6c8@m1pIc)Dqs+WLXjbpom5@$T+oqC5RJk!9atPF/<mG'H`V9P0YII;!>C8YL)XS&ATORi>!U.7<Ds\"<dT/Mkp\\V%!U[RS_YC/Wrn[Z`S(^4NU,lV#X3/#pP7K*>g!<<'"
            ]
        },
        "crawl_vertex_ids": {
            "Sensor": [
                "aggind:ID",
                "idpind:ID",
                "ind:ID",
                "uid:ID"
            ]
        },
        "crawled_timestamp": "2022-11-15T13:58:17.251061883Z",
        "created_timestamp": "2022-11-15T12:59:17.239585706Z",
        "description": "A user received new privileges",
        "display_name": "Privilege escalation (user)",
        "end_time": "2022-11-15T12:58:15.629Z",
        "falcon_host_link": "https://falcon.crowdstrike.com/identity-protection/detections/ID",
        "id": "ind:ID",
        "name": "IdpEntityPrivilegeEscalationUser",
        "objective": "Gain Access",
        "pattern_id": 51113,
        "previous_privileges": "0",
        "privileges": "8321",
        "product": "idp",
        "scenario": "privilege_escalation",
        "severity": 2,
        "show_in_ui": true,
        "source_account_domain": "EXAMPLE.EXAMPLE",
        "source_account_name": "ExampleMailbox",
        "source_account_object_sid": "S-1-5-21-3479765008-4256118348-3151044947-3595",
        "start_time": "2022-11-15T12:58:15.629Z",
        "status": "new",
        "tactic": "Privilege Escalation",
        "tactic_id": "TA0004",
        "tags": [
            "red_team"
        ],
        "technique": "Valid Accounts",
        "technique_id": "T1078",
        "timestamp": "2022-11-15T12:58:17.239Z",
        "type": "idp-user-endpoint-app-info",
        "updated_timestamp": "2022-11-23T15:22:20.271100181Z"
    }
    

##### Output messages

The **Update Alert** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated alert with ID ALERT_ID in CrowdStrike` | Action succeeded.  
`Error executing action "Update Alert". Reason: ERROR_REASON` `Error executing action "Update Alert". Reason: alert with ID ALERT_ID wasn't found in CrowdStrike. Please check the spelling.` `Error executing action "Update Alert". Reason: at least one of the "Status" or "Assign To" or "Verdict" parameters should have a value.` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Update Alert** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Detection - Deprecated

**Deprecated:** This action is deprecated. Use the Update Alert action instead. 

Use the **Update Detection** action to update detections in CrowdStrike Falcon.

This action runs on all entities.

#### Action inputs

The **Update Detection** action requires the following parameters:

Parameter | Description  
---|---  
`Detection ID` |  Required. The ID of the detection to update.  
`Status` |  Required. A detection status. The default value is `Select One`. Possible values are as follows: 

  * `Select One`
  * `new`
  * `in_progress`
  * `true_positive`
  * `false_positive`
  * `ignored`
  * `closed`

  
`Assign Detection to` |  Optional. An email address of the CrowdStrike Falcon user who is the assignee of the detection.  
  
#### Action outputs

The **Update Detection** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Update Detection** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated detection DETECTION_ID in CrowdStrike Falcon.` | Action succeeded.  
`Error executing action "Update Detection". Reason: ERROR_REASON` |  Action failed. Check connection to the server, input parameters, or credentials.  
`Error executing action "Update Detection". Reason: Either "Status" or "Assign Detection To" should have a proper value.` |  Action failed. Check the values of the `Status` and `Assign Detection To` parameters.  
  
##### Script result

The following table describes the values for the script result output when using the **Update Detection** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Update Identity Protection Detection

Use the **Update Identity Protection Detection** to update an identity protection detection in CrowdStrike.

This action requires an Identity Protection license.

This action doesn't run on entities.

#### Action inputs

The **Update Identity Protection Detection** action requires the following parameters:

Parameters  
---  
`Detection ID` | _Required_ The ID of the detection to update.  
`Status` | _Optional_ A status of the detection.The default value is `Select One`. Th possible values are as follows:

  * `Closed`
  * `Ignored`
  * `In Progress`
  * `New`
  * `Reopened`
  * `Select One`

  
`Assign to` | _Optional_ The name of the assigned analyst. If `Unassign` is provided, the action removes an assignee from the detection.If an invalid value is provided, the action does not change the current assignee.  
  
#### Action outputs

The **Update Identity Protection Detection** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Update Identity Protection Detection** action:
    
    
    {
        "added_privileges": [
            "DomainAdminsRole"
        ],
        "aggregate_id": "aggind:ID",
        "assigned_to_uid": "example@example.com",
        "cid": "123456789abcdef123456789abcdef12",
        "composite_id": "123456789abcdef123456789abcdef12:ind:ID",
        "confidence": 20,
        "context_timestamp": "2022-11-15T12:58:15.629Z",
        "crawl_edge_ids": {
            "Sensor": [
                "N6KIZ`%V`&d#&#sRaHNV[f3[CA4lr/C_N;.JnbglJpdg8TCCTqnr!9D\\['ALM&eNbPq?kt$#@]+01Ac[&th0-0]E'J8:]mFV?'g5HZ/$B.%BC29_`4U_?%a)_&#k>,G>:=E>%[7^<aLSVj=`UCMcRUH[a9/*^hO_7Ft(js#P<M<(eG3(B=I8rr",
                "XNXnKK.mi:ckQ^2c7AGRMK^'rd:p[_JkD_5ZM$W:d'J8oN:42nj.Ho1-^E5D16b0VALJ`2cDEEJTVdY\\n.-WQ^_B[7$1pH[Glgm@go]-LB%M1,c#2F)nli-Ge#V<=[!c_jh8e3D8E-S0FheDm*BHh-P/s6q!!*'!",
                "N6L*L\">LGfi/.a$IkpaFlWjT.YU#P@Gu8Qe6'0SK=M]ChI,FQXqo=*M(QR+@6c8@m1pIc)Dqs+WLXjbpom5@$T+oqC5RJk!9atPF/<mG'H`V9P0YII;!>C8YL)XS&ATORi>!U.7<Ds\"<dT/Mkp\\V%!U[RS_YC/Wrn[Z`S(^4NU,lV#X3/#pP7K*>g!<<'"
            ]
        },
        "crawl_vertex_ids": {
            "Sensor": [
                "aggind:ID",
                "idpind:ID",
                "ind:ID",
                "uid:ID"
            ]
        },
        "crawled_timestamp": "2022-11-15T13:58:17.251061883Z",
        "created_timestamp": "2022-11-15T12:59:17.239585706Z",
        "description": "A user received new privileges",
        "display_name": "Privilege escalation (user)",
        "end_time": "2022-11-15T12:58:15.629Z",
        "falcon_host_link": "https://example.com/",
        "id": "ind:ID",
        "name": "IdpEntityPrivilegeEscalationUser",
        "objective": "Gain Access",
        "pattern_id": 51113,
        "previous_privileges": "0",
        "privileges": "8321",
        "product": "idp",
        "scenario": "privilege_escalation",
        "severity": 2,
        "show_in_ui": true,
        "source_account_domain": "EXAMPLE.COM",
        "source_account_name": "ExampleName",
        "source_account_object_sid": "S-1-5-21-3479765008-4256118348-3151044947-3595",
        "start_time": "2022-11-15T12:58:15.629Z",
        "status": "new",
        "tactic": "Privilege Escalation",
        "tactic_id": "TA0004",
        "tags": [
            "red_team"
        ],
        "technique": "Valid Accounts",
        "technique_id": "T1078",
        "timestamp": "2022-11-15T12:58:17.239Z",
        "type": "idp-user-endpoint-app-info",
        "updated_timestamp": "2022-11-23T15:22:20.271100181Z"
    }
    

##### Output messages

On a Case Wall, the **Update Identity Protection Detection** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated identity protection detection with ID DETECTION_ID in CrowdStrike.` | Action succeeded.  
`Error executing action "Update Identity Protection Detection". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "Update Identity Protection Detection". Reason: identity protection detection with ID DETECTION_ID wasn't found in CrowdStrike. Please check the spelling.` | Action failed.Check the spelling.  
`Error executing action "Update Identity Protection Detection". Reason: at least one of the "Status" or "Assign To" parameters should have a value.` | Action failed.Check the values of the `Status` and `Assign to` parameters.  
  
##### Script result

The following table describes the values for the script result output when using the **Update Identity Protection Detection** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Incident - Deprecated

**Deprecated:** This action is deprecated. Use the Update Alert action instead.

Use the **Update Incident** action to update incidents in CrowdStrike.

This action doesn't run on entities.

#### Action inputs

The **Update Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Incident ID` | Required. The ID of the incident to update.  
`Status` | Optional. The status of the incident. The possible values are as follows:

  * `Closed`
  * `In Progress`
  * `New`
  * `Reopened`

  
`Assign to` | Optional. The name or email address of the assigned analyst. If `Unassign` is provided, the action removes an assignee from the incident. To specify a name, provide the first and last name of the analyst in the following format: `"FIRST_NAME` `LAST_NAME"`  
  
#### Action outputs

The **Update Incident** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Update Incident** action:
    
    
     {
    "data_type": "Incident",
                "incident_id": "inc:fee8a6ef0cb3412e9a781dcae0287c85:9dfa480ae6214309bff0c8dc2ad8af7c",
                "incident_type": 1,
                "cid": "123456789abcdef123456789abcdef12",
                "host_ids": [
                    "fee8a6ef0cb3412e9a781dcae0287c85"
                ],
                "hosts": [
                    {
                        "device_id": "fee8a6ef0cb3412e9a781dcae0287c85",
                        "hostname": "DESKTOP-EXAMPLE",
                        "external_ip": "198.51.100.1",
                        "os_version": "Windows 10",
                        "status": "contained"
                    }
                ],
                "created": "2023-01-09T12:12:51Z",
                "state": "closed",
                "status": 20,
                "tactics": [
                    "Defense Evasion",
                    "Privilege Escalation",
                    "Credential Access"
                ],
                "fine_score": 21
            }
    

##### Output messages

The **Update Incident** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated incident with ID INCIDENT_ID in CrowdStrike` | Action succeeded.  
`Error executing action "Update Incident". Reason: ERROR_REASON` | Action failed.Check connection, input parameters, or credentials.  
`Error executing action "Update Incident". Reason: incident with ID INCIDENT_ID wasn't found in CrowdStrike. Please check the spelling.` | Action failed.Check the spelling.  
  
##### Script result

The following table describes the values for the script result output when using the **Update Incident** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update IOC Information

Use the **Update IOC Information** action to update information about custom IOCs in CrowdStrike Falcon.

This action treats Hostname entities as domain IOCs and extracts the domain part out of URLs. This action only supports the MD5 and SHA-256 hashes.

The **Update IOC Information** action runs on the following entities:

  * Hostname
  * URL
  * IP address
  * Hash



#### Action inputs

The **Update IOC Information** action requires the following parameters:

Parameters  
---  
`Description` | _Optional_ A new description for custom IOCs.  
`Source` | _Optional_ A source for custom IOCs.  
`Expiration days` | _Optional_ The number of days left until expiration. This parameter only affects the URL, IP address, and Hostname entities.   
`Detect policy` | _Optional_ If selected, the action sends a notification for the identified IOCs. If not selected, the action sends no notification. Selected by default.  
  
#### Action outputs

The **Update IOC Information** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Update IOC Information** action:
    
    
    {
        "id": "563df6a812f2e7020a17f77ccd809176ca3209cf7c9447ee36c86b4215860856",
        "type": "md5",
        "value": "7e4b0f81078f27fde4aeb87b78b6214c",
        "source": "testSource",
        "action": "detect",
        "severity": "high",
        "description": "test description update",
        "platforms": [
            "example"
        ],
        "tags": [
            "Hashes 17.Apr.18 12:20 (Example)"
        ],
        "expiration": "2022-05-01T12:00:00Z",
        "expired": false,
        "deleted": false,
        "applied_globally": true,
        "from_parent": false,
        "created_on": "2021-04-22T03:54:09.235120463Z",
        "created_by": "internal@example.com",
        "modified_on": "2021-09-16T10:09:07.755804336Z",
        "modified_by": "c16fd3a055eb46eda81e064fa6dd43de"
    }
    

##### Output messages

On a Case Wall, the **Update IOC Information** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated the following entities in CrowdStrike Falcon: ENTITY_ID ` `Action wasn't able to update the following entities in CrowdStrike Falcon: ENTITY_ID` | Action succeeded.  
`Error executing action "Update IOC Information". Reason: ERROR_REASON ` | Action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Update IOC Information** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Upload IOCs

Use the **Upload IOCs** action to add custom IOCs in CrowdStrike Falcon.

This action treats Hostname entities as domain IOCs and extracts the domain part out of URLs. This action only supports the MD5 and SHA-256 hashes.

The **Upload IOCs** action runs on the following entities:

  * IP address
  * Hostname
  * URL
  * Hash



#### Action inputs

The **Upload IOCs** action requires the following parameters:

Parameters  
---  
`Platform` | _Required_ A comma-separated list of platforms related to the IOC. The default value is `Windows,Linux,Mac`. Possible values are as follows: 

  * `Windows`
  * `Linux`
  * `Mac`

  
`Severity` | _Required_ A severity of the IOC. The default value is `Medium`. Possible values are as follows: 

  * `Informational`
  * `Low`
  * `Medium`
  * `High`
  * `Critical`

  
`Comment` | _Optional_ A comment containing more context related to the IOC.  
`Host Group Name` | _Required_ The name of the host group.  
`Action` | _Optional_ An action for uploaded IOCs. The default value is `Detect`.The possible values are as follows:

  * `Block`
  * `Detect`

The `Block` value applies only to MD5 hashes. The action always applies the `Detect` policy to all other IOC types.  
`Days To Expire` | _Optional_ The number of days before the IOC expires.  
  
#### Action outputs

The **Upload IOCs** action provides the following outputs:

Action output type  
---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Upload IOCs** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added the following custom IOCs in CrowdStrike Falcon: ENTITY_ID` `The following custom IOCs were already a part of CrowdStrike Falcon instance: ENTITY_ID` `Action wasn't able to add the following custom IOCs in CrowdStrike Falcon: ENTITY_ID ` | Action succeeded.  
`Error executing action "Upload IOCs". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
`Error executing action "Upload IOCs". Reason: Host group "HOST_GROUP_NAME" was not found. Please check the spelling.` | Action failed.Check the `Host Group Name` parameter value.  
`Error executing action "Upload IOCs". Invalid value provided for the parameter "Platform". Possible values: Windows, Linux, Mac.` | Action failed.Check the `Platform` parameter value.  
  
##### Script result

The following table describes the values for the script result output when using the **Upload IOCs** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

Make sure you've configured the minimal permissions for every CrowdStrike connector. For more details, refer to the Connector permissions section of this document.

For instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### CrowdStrike events

Events are pieces of information gathered by the Falcon sensors on your hosts. There are four types of events in CrowdStrike:

CrowdStrike event types  
---  
Auth activity audit events | Events generated every time the authorization is requested, allowed, or completed on endpoints.  
Detection summary events | Events generated when threats are detected on endpoints.  
Remote response session end events | Events generated from remote sessions on endpoints.  
User activity audit events | Events generated to monitor activities carried out by active users on endpoints.  
  
Connectors ingest events into Google SecOps to create alerts and enrich cases with event data. You can select what events to ingest into Google SecOps: all event types or selected ones.

### Deprecated: CrowdStrike Detections Connector

This connector no longer gets updates or code changes. 

Use the **CrowdStrike - Alerts Connector** instead.

Use the **CrowdStrike Detections Connector** to pull detections from CrowdStrike.

The dynamic list works with filters supported by the CrowdStrike API.

#### How to work with the dynamic list

When working with the dynamic list, adhere to the following recommendations:

  * Use the CrowdStrike FQL language to modify the filter sent by the connector.
  * Provide a separate entry in the dynamic list for each filter.
  * To ingest all detections assigned to a specific analyst, make sure that the analyst provides the following dynamic list entry: 
        
        assigned_to_name:'ANALYST_USER_NAME'




The dynamic list supports the following parameters:

Supported parameters | Description  
---|---  
`q` | A full text search across all metadata fields.  
`date_updated` | A date of the most recent detection update.  
`assigned_to_name` | The human-readable username of the detection assignee.  
`max_confidence` |  When a detection has more than one associated behavior with varying confidence levels, this field captures the highest confidence value of all behaviors. The parameter value can be any integer from 1 to 100.  
`detection_id` | The detection ID that can be used in conjunction with other APIs, such as the Detection Details API or Resolve Detection API.  
`max_severity` |  When a detection has more than one associated behavior with varying severity levels, this field captures the highest severity value of all behaviors. The parameter value can be any integer from 1 to 100.  
`max_severity_displayname` |  The name used in UI to determine the detection severity. The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`

  
`seconds_to_triaged` | The time required for a detection to change its status from `new` to `in_progress`.  
`seconds_to_resolved` | The time required for a detection to change its status from `new` to any of the resolved states (`true_positive`, `false_positive`, `ignored`, and `closed`).  
`status` |  A current status of the detection. The possible values are as follows:

  * `new`
  * `in_progress`
  * `true_positive`
  * `false_positive`
  * `ignored`

  
`adversary_ids` | The adversary tracked by CrowdStrike Falcon Intelligence possesses an ID associated with the attributed behaviors or indicators in a detection. These IDs are located in a detection metadata accessible through the Detection Details API.  
`cid` | The customer ID (CID) of your organization.  
  
#### Connector inputs

The **CrowdStrike Detections Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` |  Required. The source field name that contains the `Product Field` name. The default value is `Product Name`.  
`Event Field Name` |  Required. The source field name that contains the `Event Field` name. The default value is `behaviors_technique`.  
`Environment Field Name` |  Optional. The name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` |  Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. Use the default value `.*` to retrieve the required raw `Environment Field Name` value.  
`Script Timeout (Seconds)` |  Required. The timeout limit in seconds for the Python process running the current script. The default value is `180`.  
`API Root` |  Required. The API root of the CrowdStrike instance. The default value is `https://api.crowdstrike.com`.  
`Client ID` |  Required. The client ID of the CrowdStrike account.  
`Client Secret` |  Required. The client Secret of the CrowdStrike account.  
`Lowest Severity Score To Fetch` |  Optional. The lowest severity score of the detections to fetch (max 100). The default value is `50`.  
`Lowest Confidence Score To Fetch` |  Optional. The lowest confidence score of the detections to fetch (max 100). The default value is `0`.  
`Max Hours Backwards` |  Optional. The amount of hours to fetch detections from. The default value is `1`.  
`Max Detections To Fetch` |  Optional. The number of detections to process in a single connector iteration. The default value is `10`.  
`Disable Overflow` |  Optional. If selected, the connector ignores the overflow mechanism.  
`Verify SSL` |  Required. If selected, the integration verifies the SSL certificate.  
`Proxy Server Address` | Optional.An address of the proxy server to use.  
`Proxy Username` | Optional.A proxy username to authenticate with.  
`Proxy Password` | Optional.A proxy password to authenticate with.  
`Case Name Template` | Optional.Placeholder format: [`FIELD_NAME` ].  
`Alert Name Template` | Optional.Placeholder format: [`FIELD_NAME` ].  
`Padding Period` | Optional.Number of hours used for padding (max 6).  
`Include Hidden Alerts` | Optional.If enabled, fetches alerts labeled as "hidden".  
`Fallback Severity` | Optional.Applied if severity is missing. Default: Informational.  
`Customer ID` | Optional.The customer ID for multi-tenant (MSSP) environments.  
  
#### Connector rules

The connector supports proxies.

#### Connector events

An example of the connector event is as follows:
    
    
    {
        "cid": "123456789abcdef123456789abcdef12",
        "created_timestamp": "2021-01-12T16:19:08.651448357Z",
        "detection_id": "ldt:74089e36ac3a4271ab14abc076ed18eb:4317290676",
        "device": {
            "device_id": "74089e36ac3a4271ab14abc076ed18eb",
            "cid": "123456789abcdef123456789abcdef12",
            "agent_load_flags": "0",
            "agent_local_time": "2021-01-12T16:07:16.205Z",
            "agent_version": "6.13.12708.0",
            "bios_manufacturer": "Example LTD",
            "bios_version": "6.00",
            "config_id_base": "65994753",
            "config_id_build": "12708",
            "config_id_platform": "3",
            "external_ip": "203.0.113.1",
            "hostname": "EXAMPLE-01",
            "first_seen": "2021-01-12T16:01:43Z",
            "last_seen": "2021-01-12T16:17:21Z",
            "local_ip": "192.0.2.1",
            "mac_address": "00-50-56-a2-5d-a3",
            "major_version": "10",
            "minor_version": "0",
            "os_version": "Windows 10",
            "platform_id": "0",
            "platform_name": "Windows",
            "product_type": "1",
            "product_type_desc": "Workstation",
            "status": "normal",
            "system_manufacturer": "Example, Inc.",
            "system_product_name": "Example ",
            "modified_timestamp": "2021-01-12T16:17:29Z",
        "behaviors": 
            {
                "device_id": "74089e36ac3a4271ab14abc076ed18eb",
                "timestamp": "2021-01-12T16:17:19Z",
                "template_instance_id": "10",
                "behavior_id": "10146",
                "filename": "reg.exe",
                "filepath": "\\Device\\HarddiskVolume2\\Windows\\System32\\reg.exe",
                "alleged_filetype": "exe",
                "cmdline": "REG  ADD HKCU\\Environment /f /v UserInitMprLogonScript /t REG_MULTI_SZ /d \"C:\\TMP\\mim.exe sekurlsa::LogonPasswords > C:\\TMP\\o.txt\"",
                "scenario": "credential_theft",
                "objective": "Gain Access",
                "tactic": "Credential Access",
                "tactic_id": "TA0006",
                "technique": "Credential Dumping",
                "technique_id": "T1003",
                "display_name": "Example-Name",
                "severity": 70,
                "confidence": 80,
                "ioc_type": "hash_sha256",
                "ioc_value": "b211c25bf0b10a82b47e9d8da12155aad95cff14cebda7c4acb35a94b433ddfb",
                "ioc_source": "library_load",
                "ioc_description": "\\Device\\HarddiskVolume2\\Windows\\System32\\reg.exe",
                "user_name": "Admin",
                "user_id": "example-id",
                "control_graph_id": "ctg:74089e36ac3a4271ab14abc076ed18eb:4317290676",
                "triggering_process_graph_id": "pid:74089e36ac3a4271ab14abc076ed18eb:4746437404",
                "sha256": "b211c25bf0b10a82b47e9d8da12155aad95cff14cebda7c4acb35a94b433ddfb",
                "md5": "05cf3ce225b05b669e3118092f4c8eab",
                "parent_details": {
                    "parent_sha256": "d0ceb18272966ab62b8edff100e9b4a6a3cb5dc0f2a32b2b18721fea2d9c09a5",
                    "parent_md5": "9d59442313565c2e0860b88bf32b2277",
                    "parent_cmdline": "C:\\Windows\\system32\\cmd.exe /c \"\"C:\\Users\\Admin\\Desktop\\APTSimulator-master\\APTSimulator-master\\APTSimulator.bat\" \"",
                    "parent_process_graph_id": "pid:74089e36ac3a4271ab14abc076ed18eb:4520199381"
                },
                "pattern_disposition": 2048,
                "pattern_disposition_details": {
                    "indicator": false,
                    "detect": false,
                    "inddet_mask": false,
                    "sensor_only": false,
                    "rooting": false,
                    "kill_process": false,
                    "kill_subprocess": false,
                    "quarantine_machine": false,
                    "quarantine_file": false,
                    "policy_disabled": false,
                    "kill_parent": false,
                    "operation_blocked": false,
                    "process_blocked": true,
                    "registry_operation_blocked": false,
                    "critical_process_disabled": false,
                    "bootup_safeguard_enabled": false,
                    "fs_operation_blocked": false,
                    "handle_operation_downgraded": false
                }
            }
        },
        "email_sent": false,
        "first_behavior": "2021-01-12T16:17:19Z",
        "last_behavior": "2021-01-12T16:17:19Z",
        "max_confidence": 80,
        "max_severity": 70,
        "max_severity_displayname": "High",
        "show_in_ui": true,
        "status": "new",
        "hostinfo": {
            "domain": ""
        },
        "seconds_to_triaged": 0,
        "seconds_to_resolved": 0,
    }
        

### CrowdStrike Falcon Streaming Events Connector

The **CrowdStrike Falcon Streaming Events Connector** addresses the following use cases:

  1. **Detection events data ingestion**.

CrowdStrike Falcon detects an attempt to execute the malicious `SophosCleanM.exe` file on an endpoint. CrowdStrike stops the operation and creates an alert containing file hashes in the event data.

An analyst interested in file reputation runs discovered hashes in VirusTotal and finds out that a hash is malicious. As a following step, the Mcafee EDR action quarantines the malicious file.

  2. **User activity audit events data ingestion**.

A CrowdStrike user, Dani, updates the detection status from `new` to `false-positive`. This user action creates an event named _detection_update_.

The analyst performs a follow up to understand why Dani has marked the action false positive and checks the ingested event containing the information about Dani's identity.

As a following step, the analyst runs the Active Directory _Enrich Entities_ action to obtain more details about the incident and simplify tracking Dani down.

  3. **Auth activity audit events data ingestion**.

An event indicates that Dani has created a new user account and granted user roles to it.

To investigates the event and understand why the user was created, the analyst uses Dani's user ID to run the Active Directory _Enrich Entities_ action and find out Dani's user role to confirm if they are authorized to add new users.

  4. **Remote response end events data ingestion**.

A remote event indicates that Dani had a remote connection to a specific host and executed commands as a root user to access a web server directory.

To get more information about both Dani and the host involved, the analyst runs the Active Directory action to enrich both the user and the host. Based on the information returned, the analyst might decide to suspend Dani until the purpose of the remote connection is clarified.




#### Connector inputs

The **CrowdStrike Falcon Streaming Event Connector** requires the following parameters:

Parameters  
---  
`Product Field Name` | _Required_ The source field name that contains the `Product Field` name. The default value is `device_product`.  
`Event Field Name` | _Required_ The source field name that contains the `Event Field` name. The default value is `Name`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Alert Name Template` | _Optional_ If provided, the connector uses this value for the Google SecOps Alert Name.You can provide placeholders in the following format: [`FIELD_NAME`], such as _Phishing - [event_mailbox]_. Note: If you provide no value or an invalid template, the connector uses the default alert name. The connector uses the first Google SecOps event for placeholders. This parameter only allows keys with a string value.  
`API Root` | _Required_ The API root of the CrowdStrike instance. The default value is `https://api.crowdstrike.com`.  
`Client ID` | _Required_ The client ID of the CrowdStrike account.  
`Client Secret` | _Required_ The client secret of the CrowdStrike account.  
`Event types` | _Optional_ A comma-separated list of event types.Examples of the event types are as follows:

  * `DetectionSummaryEvent`
  * `IncidentSummaryEvent`
  * `AuthActivityAuditEvent`
  * `UserActivityAuditEvent`
  * `RemoteResponseSessionStartEvent`
  * `RemoteResponseSessionEndEvent`

  
`Max Days Backwards` | _Optional_ The number of days before today to retrieve detections from. The default value is `3`.  
`Max Events Per Cycle` | _Optional_ The number of events to process in a single connector iteration. The default value is `10`.  
`Min Severity` | _Optional_ Events to ingest based on the event severity (detection events). The value ranges from 0 to 5. If other event types besides detections are ingested, their severity is set to `-1` and this filter doesn't apply to them.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the overflow mechanism.Not selected by default.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for the connection to the CrowdStrike server is valid. Not selected by default.  
`Script Timeout (Seconds)` | _Required_ The timeout limit for the Python process running the current script. Default value is 60 seconds.  
`Proxy Server Address` | _Optional_ An address of the proxy server to use.  
`Proxy Username` | _Optional_ A proxy username to authenticate with.  
`Proxy Password` | _Optional_ A proxy password to authenticate with.  
`Rule Generator Template` | _Optional_ If provided, the connector uses this value for the Google SecOps rule generator.You can provide placeholders in the following format: [`FIELD_NAME`], such as _Phishing - [event_mailbox]_. If you provide no value or an invalid template, the connector uses the default rule generator. The connector uses the first Google SecOps event for placeholders. This parameter allows only keys with a string value.  
`Customer ID` | _Optional_ The customer ID of the tenant in which to execute the connector. For use in multi-tenant (MSSP) environments.   
  
#### Connector rules

This connector supports proxies.

This connector doesn't support the dynamic list.

### CrowdStrike Identity Protection Detections Connector

Use the **CrowdStrike Identity Protection Detections Connector** to pull the identity protection detections from CrowdStrike. The dynamic list works with the `display_name` parameter.

This connector requires an Identity Protection license.

#### Connector inputs

The **CrowdStrike Identity Protection Detections Connector** requires the following parameters:

Parameters  
---  
`Product Field Name` | _Required_ The source field name that contains the `Product Field` name. The default value is `Product Name`.  
`Event Field Name` | _Required_ The source field name that contains the `Event Field` name. The default value is `behaviors_technique`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | _Required_ The timeout limit in seconds for the Python process running the current script. The default value is `180`.  
`API Root` | _Required_ The API root of the CrowdStrike instance. The default value is `https://api.crowdstrike.com`.  
`Client ID` | _Required_ The client ID of the CrowdStrike account.  
`Client Secret` | _Required_ The client secret of the CrowdStrike account.  
`Lowest Severity Score To Fetch` | _Optional_ The lowest severity score of the detections to fetch. If no value is provided, the connector doesn't apply this filter. The maximum value is `100`.The default value is `50`. The connector also supports the following values for this parameter:

  * `Low`
  * `Medium`
  * `High`
  * `Critical`

  
`Lowest Confidence Score To Fetch` | _Optional_ the lowest confidence score of the detections to fetch. If no value is provided, the connector doesn't apply this filter. The maximum value is `100`.The default value is `0`.  
`Max Hours Backwards` | _Optional_ The number of hours prior to now to retrieve detections from. The default value is `1`.  
`Max Detections To Fetch` | _Optional_ The number of detections to process in a single connector iteration. The default value is `10`.  
`Case Name Template` | _Optional_ If provided, the connector adds a new key called `custom_case_name` to the Google SecOps Event. You can provide placeholders in the following format: [`FIELD_NAME`], such as _Phishing - [event_mailbox]_. Note: The connector uses the first Google SecOps event for placeholders. This parameter only allows keys with a string value.  
`Alert Name Template` | _Optional_ If provided, the connector uses this value for the Google SecOps Alert Name.You can provide placeholders in the following format: [`FIELD_NAME`], such as _Phishing - [event_mailbox]_. Note: If you provide no value or an invalid template, the connector uses the default alert name. The connector uses the first Google SecOps event for placeholders. This parameter only allows keys with a string value.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the overflow mechanism.Not selected by default.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for the connection to the CrowdStrike server is valid. Not selected by default.  
`Proxy Server Address` | _Optional_ An address of the proxy server to use.  
`Proxy Username` | _Optional_ A proxy username to authenticate with.  
`Proxy Password` | _Optional_ A proxy password to authenticate with.  
`Customer ID` | _Optional_ The customer ID of the tenant in which to execute the connector. For use in multi-tenant (MSSP) environments.   
  
#### Connector rules

This connector supports proxies.

#### Connector event

An example of the connector event is as follows:
    
    
    {
      "added_privileges": [
          "DomainAdminsRole"
      ],
      "aggregate_id": "aggind:123456789abcdef123456789abcdef12:C34185DF-C3BA-4F69-93EB-1B61A213AF86",
      "cid": "123456789abcdef123456789abcdef12",
      "composite_id": "123456789abcdef123456789abcdef12:ind:123456789abcdef123456789abcdef12:C34185DF-C3BA-4F69-93EB-1B61A213AF86",
      "confidence": 20,
      "context_timestamp": "2022-11-15T12:58:13.155Z",
      "crawl_edge_ids": {
          "Sensor": [
              "N6Fq4_]TKjckDDWI$fKO`l>_^KFO4!,Z/&o<H7_)4[Ip*h@KUG8%Xn3Fm3@]<gF_c,c1eeW\\O-J9l;HhVHA\"DH#\\pO1M#>X^dZWWg%V:`[+@g9@3h\"Q\"7r8&lj-o[K@24f;Xl.rlhgWC8%j5\\O7p/G7iQ*ST&12];a_!REjkIUL.R,/U^?]I!!*'!",
              "XNXPaK.m]6i\"HhDPGX=XlMl2?8Mr#H;,A,=7aF9N)>5*/Hc!D_>MmDTO\\t1>Oi6ENO`QkWK=@M9q?[I+pm^)mj5=T_EJ\"4cK99U+!/ERSdo(X^?.Z>^]kq!ECXH$T.sfrJpT:TE+(k]<'Hh]..+*N%h_5<Z,63,n!!*'!",
              "N6L$J`'>\":d#'I2pLF4-ZP?S-Qu#75O,>ZD+B,m[\"eGe@(]>?Nqsh8T3*q=L%=`KI_C[Wmj3?D!=:`(K)7/2g&8cCuB`r9e\"jTp/QqK7.GocpPSq4\\-#t1Q*%5C0%S1$f>KT&a81dJ!Up@EZY*;ssFlh8$cID*qr1!)S<!m@A@s%JrG9Go-f^B\"<7s8N"
          ]
      },
      "crawl_vertex_ids": {
          "Sensor": [
              "uid:123456789abcdef123456789abcdef12:S-1-5-21-3479765008-4256118348-3151044947-3195",
              "ind:123456789abcdef123456789abcdef12:C34185DF-C3BA-4F69-93EB-1B61A213AF86",
              "aggind:123456789abcdef123456789abcdef12:C34185DF-C3BA-4F69-93EB-1B61A213AF86",
              "idpind:123456789abcdef123456789abcdef12:715224EE-7AD6-33A1-ADA9-62C4608DA546"
          ]
      },
      "crawled_timestamp": "2022-11-15T14:33:50.641703679Z",
      "created_timestamp": "2022-11-15T12:59:15.444106807Z",
      "description": "A user received new privileges",
      "display_name": "Privilege escalation (user)",
      "end_time": "2022-11-15T12:58:13.155Z",
      "falcon_host_link": "https://example.com/identity-protection/detections/",
      "id": "ind:123456789abcdef123456789abcdef12:C34185DF-C3BA-4F69-93EB-1B61A213AF86",
      "name": "IdpEntityPrivilegeEscalationUser",
      "objective": "Gain Access",
      "pattern_id": 51113,
      "previous_privileges": "0",
      "privileges": "8321",
      "product": "idp",
      "scenario": "privilege_escalation",
      "severity": 2,
      "show_in_ui": true,
      "source_account_domain": "EXAMPLE.COM",
      "source_account_name": "ExampleName",
      "source_account_object_sid": "S-1-5-21-3479765008-4256118348-3151044947-3195",
      "start_time": "2022-11-15T12:58:13.155Z",
      "status": "new",
      "tactic": "Privilege Escalation",
      "tactic_id": "TA0004",
      "technique": "Valid Accounts",
      "technique_id": "T1078",
      "timestamp": "2022-11-15T12:58:15.397Z",
      "type": "idp-user-endpoint-app-info",
      "updated_timestamp": "2022-11-15T14:33:50.635238527Z"
    }
    

### Deprecated: CrowdStrike Incidents Connector

**Deprecated:** This connector is deprecated. Use the **CrowdStrike Alerts Connector** instead for pulling incident and behavior data.

Use the **CrowdStrike Incidents Connector** to pull incident and related behaviors from CrowdStrike.

The dynamic list works with the `incident_type` parameter.

#### Connector parameters

The **CrowdStrike Incidents Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The source field name that contains the `Product Field` name. The default value is `Product Name`.  
`Event Field Name` | Required. The source field name that contains the `Event Field` name. The default value is `data_type`.  
`Environment Field Name` | Optional. The name of the field where the environment name is stored. If not found, the default environment is used.Default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to manipulate the environment field value. Use the default `.*` to retrieve the raw value.  
`Script Timeout (Seconds)` | Required. The timeout limit for the Python process. The default value is `180`.  
`API Root` | Required. The API root of the CrowdStrike instance. The default value is `https://api.crowdstrike.com`.  
`Client ID` | Required. The client ID of the CrowdStrike account.  
`Client Secret` | Required. The client secret of the CrowdStrike account.  
`Lowest Severity Score To Fetch` | Optional. The lowest severity score of incidents to fetch. Supports `Low`, `Medium`, `High`, `Critical`, or numeric values up to `100`.  
`Max Hours Backwards` | Optional. Retrieval lookback window in hours.The default value is `1`.  
`Max Incidents To Fetch` | Optional. Number of incidents per iteration. Maximum is `100`. The default value is `10`.  
`Use dynamic list as a blocklist` | Required. If selected, the dynamic list acts as a blocklist.  
`Disable Overflow` | Optional. If selected, ignores the overflow mechanism.  
`Verify SSL` | Required. Verifies SSL certificate for the connection.  
`Proxy Parameters` | Optional. Includes `Proxy Server Address`, `Proxy Username`, and `Proxy Password`.  
`Customer ID` | Optional. Tenant ID for multi-tenant (MSSP) environments.  
  
#### Connector rules

This connector supports proxies.

#### Connector events

The connector supports two event types: incident-based and behavior-based.

**Example: Incident-based event**
    
    
     {
        "data_type": "Incident",
        "incident_id": "inc:fee8a6ef0cb3412e9a781dcae0287c85:9dfa480ae6214309bff0c8dc2ad8af7c",
        "incident_type": 1,
        "cid": "123456789abcdef123456789abcdef12",
        "state": "closed",
        "tactics": ["Defense Evasion", "Privilege Escalation"],
        "fine_score": 21
     }
    

**Example: Behavior-based event**
    
    
     {
        "behavior_id": "ind:fee8a6ef0cb3412e9a781dcae0287c85:1298143147841-372-840208",
        "incident_id": "inc:fee8a6ef0cb3412e9a781dcae0287c85:9dfa480ae6214309bff0c8dc2ad8af7c",
        "timestamp": "2023-01-09T11:24:25Z",
        "tactic": "Privilege Escalation",
        "technique": "Bypass User Account Control"
     }
    

### CrowdStrike – Alerts Connector

Use the **CrowdStrike – Alerts Connector** to pull alerts from CrowdStrike. The dynamic list works with the `display_name` parameter.

To fetch identity protection detections, use the Identity Protection Detections Connector.

#### Connector inputs

The **CrowdStrike – Alerts Connector** requires the following parameters:

Parameters  
---  
`Product Field Name` | _Required_ The source field name that contains the `Product Field` name. The default value is `Product Name`.  
`Event Field Name` | _Required_ The source field name that contains the `Event Field` name. The default value is `product`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | _Required_ Timeout limit in seconds for the Python process running the current script. The default value is `180`.  
`API Root` | _Required_ The API root of the CrowdStrike instance. The default value is `https://api.crowdstrike.com`.  
`Client ID` | _Required_ The client ID of the CrowdStrike account.  
`Client Secret` | _Required_ The client secret of the CrowdStrike account.  
`Case Name Template` | _Optional_ If provided, the connector adds a new key called `custom_case_name` to the Google SecOps Event. You can provide placeholders in the following format: [`FIELD_NAME`], such as _Phishing - [event_mailbox]_. Note: The connector uses the first Google SecOps event for placeholders. This parameter only allows keys with a string value.  
`Alert Name Template` | _Optional_ If provided, the connector uses this value for the Google SecOps Alert Name.You can provide placeholders in the following format: [`FIELD_NAME`], such as _Phishing - [event_mailbox]_. Note: If you provide no value or an invalid template, the connector uses the default alert name. The connector uses the first Google SecOps event for placeholders. This parameter only allows keys with a string value.  
`Lowest Severity Score To Fetch` | _Optional_ The lowest severity score of the incidents to fetch. If no value is provided, the connector ingests incidents with all severities. The maximum value is `100`. The connector also supports the following values for this parameter:

  * Low
  * Medium
  * High
  * Critical

In the CrowdStrike UI, the same value is presented as divided by 10.  
`Max Hours Backwards` | _Optional_ The number of hours before now to retrieve incidents from. The default value is `1`.  
`Max Alerts To Fetch` | _Optional_ The number of alerts to process in a single connector iteration. The maximum value is `100`.The default value is `10`.  
`Use dynamic list as a blocklist` | _Required_ If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the overflow mechanism.Not selected by default.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for the connection to the CrowdStrike server is valid. Not selected by default.  
`Proxy Server Address` | _Optional_ An address of the proxy server to use.  
`Proxy Username` | _Optional_ A proxy username to authenticate with.  
`Proxy Password` | _Optional_ A proxy password to authenticate with.  
`Customer ID` | _Optional_ The customer ID of the tenant in which to execute the connector. For use in multi-tenant (MSSP) environments.   
  
#### Connector rules

This connector supports proxies.

#### Connector events

The example of an event based on alerts is as follows:
    
    
    {
      "added_privileges": [
          "DomainAdminsRole"
      ],
      "aggregate_id": "aggind:123456789abcdef123456789abcdef12",
      "cid": "123456789abcdef123456789abcdef12",
      "composite_id": "123456789abcdef123456789abcdef12:ind:123456789abcdef123456789abcdef12",
      "confidence": 20,
      "context_timestamp": "2022-11-15T12:58:13.155Z",
      "crawl_edge_ids": {
          "Sensor": [
              "N6Fq4_]TKjckDDWI$fKO`l>_^KFO4!,Z/&o<H7_)4[Ip*h@KUG8%Xn3Fm3@]<gF_c,c1eeW\\O-J9l;HhVHA\"DH#\\pO1M#>X^dZWWg%V:`[+@g9@3h\"Q\"7r8&lj-o[K@24f;Xl.rlhgWC8%j5\\O7p/G7iQ*ST&12];a_!REjkIUL.R,/U^?]I!!*'!",
              "XNXPaK.m]6i\"HhDPGX=XlMl2?8Mr#H;,A,=7aF9N)>5*/Hc!D_>MmDTO\\t1>Oi6ENO`QkWK=@M9q?[I+pm^)mj5=T_EJ\"4cK99U+!/ERSdo(X^?.Z>^]kq!ECXH$T.sfrJpT:TE+(k]<'Hh]..+*N%h_5<Z,63,n!!*'!",
              "N6L$J`'>\":d#'I2pLF4-ZP?S-Qu#75O,>ZD+B,m[\"eGe@(]>?Nqsh8T3*q=L%=`KI_C[Wmj3?D!=:`(K)7/2g&8cCuB`r9e\"jTp/QqK7.GocpPSq4\\-#t1Q*%5C0%S1$f>KT&a81dJ!Up@EZY*;ssFlh8$cID*qr1!)S<!m@A@s%JrG9Go-f^B\"<7s8N"
          ]
      },
      "crawl_vertex_ids": {
          "Sensor": [
              "uid:123456789abcdef123456789abcdef12:S-1-5-21-3479765008-4256118348-3151044947-3195",
              "ind:123456789abcdef123456789abcdef12",
              "aggind:123456789abcdef123456789abcdef12",
              "idpind:123456789abcdef123456789abcdef12:715224EE-7AD6-33A1-ADA9-62C4608DA546"
          ]
      },
      "crawled_timestamp": "2022-11-15T14:33:50.641703679Z",
      "created_timestamp": "2022-11-15T12:59:15.444106807Z",
      "description": "A user received new privileges",
      "display_name": "Privilege escalation (user)",
      "end_time": "2022-11-15T12:58:13.155Z",
      "falcon_host_link": "https://falcon.crowdstrike.com/identity-protection/detections/123456789abcdef123456789abcdef12:ind:123456789abcdef123456789abcdef12?cid=123456789abcdef123456789abcdef12",
      "id": "ind:123456789abcdef123456789abcdef12",
      "name": "IdpEntityPrivilegeEscalationUser",
      "objective": "Gain Access",
      "pattern_id": 51113,
      "previous_privileges": "0",
      "privileges": "8321",
      "product": "idp",
      "scenario": "privilege_escalation",
      "severity": 2,
      "show_in_ui": true,
      "source_account_domain": "EXAMPLE.EXAMPLE",
      "source_account_name": "ExampleMailbox",
      "source_account_object_sid": "S-1-5-21-3479765008-4256118348-3151044947-3195",
      "start_time": "2022-11-15T12:58:13.155Z",
      "status": "new",
      "tactic": "Privilege Escalation",
      "tactic_id": "TA0004",
      "technique": "Valid Accounts",
      "technique_id": "T1078",
      "timestamp": "2022-11-15T12:58:15.397Z",
      "type": "idp-user-endpoint-app-info",
      "updated_timestamp": "2022-11-15T14:33:50.635238527Z"
    }
    

## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Crowdstrike Falcon - Sync Alerts

Use the **Crowdstrike Falcon - Sync Alerts** job to synchronize comments and statuses bi-directionally between Google SecOps and Crowdstrike.

#### Job requirements

To make sure the job identifies and synchronizes the correct data, the following conditions must be met:

  * The Google SecOps case must contain the `Crowdstrike Alert` tag.

  * If the alert didn't originate from the **Alerts Connector** or **Identity Protections Detection Connector** , you must add an `Alert_ID` alert context value for the job to identify the correct Crowdstrike record.




#### Operational logic

The job synchronizes data in two stages. The first stage synchronizes Crowdstrike data to Google SecOps alerts. The second stage synchronizes Google SecOps alert data to Crowdstrike alerts.

The job uses `Max Hours Backwards` for the initial iteration. For all subsequent requests, the job uses the `start_time` of the last processed alert.

##### Comment synchronization logic

The job uses the `last_update_time` to filter comments and prevent duplicate entries. Synchronized comments use the following structures:

  * **Sent from Crowdstrike** : `Crowdstrike {ticket_id}: {comment}`

  * **Sent from Google SecOps** : `Google SecOps {case_id}: {comment}`




Google SecOps case closure comments are also synchronized to Crowdstrike as comments.

##### Status and verdict mapping

When an alert is closed in Google SecOps, the job updates the corresponding Crowdstrike alert with the status `Closed`. The job also applies the following mapping for analyst verdicts:

  * If the closure **Reason** is `Malicious`, the Crowdstrike **Verdict** is set to `True Positive`.

  * If the closure **Reason** is `Not Malicious`, the Crowdstrike **Verdict** is set to `False Positive`.

  * For all other closure reasons, the status is set to `Closed` without a verdict.




#### Job parameters

The **Crowdstrike Falcon - Sync Alerts** job requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. The name of the environment where the job searches for alerts. The default value is `Default Environment`.  
`API Root` | Required. The API root of the Crowdstrike instance. The default value is `https://api.crowdstrike.com`.  
`Client ID` | Required. The client ID of the Crowdstrike account.  
`Client Secret` | Required. The client secret of the Crowdstrike account.  
`Max Hours Backwards` | Required. The number of hours prior to the current time to synchronize alerts during the first job iteration. The default value is `24`.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Crowdstrike server. Enabled by default.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
