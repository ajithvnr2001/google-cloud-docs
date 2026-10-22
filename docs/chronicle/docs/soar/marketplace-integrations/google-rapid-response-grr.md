---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-rapid-response-grr/
title: Integrate GRR Rapid Response with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:03.654169+00:00
---

# Integrate GRR Rapid Response with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-rapid-response-grr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate GRR Rapid Response with Google SecOps

This document explains how to configure and integrate GRR Rapid Response with Google Security Operations.

**Important:** In the Google SecOps platform, the integration for GRR Rapid Response is called _Google Rapid Response (GRR)_.

## Use cases

The **GRR Rapid Response** integration uses Google SecOps capabilities to support the following use cases:

  * **Endpoint forensic collection** : Automatically trigger forensic flows to collect files, registry keys, and memory artifacts from remote endpoints during an investigation.

  * **Rapid threat hunting** : Search for specific files or hashes across all managed clients to identify the scope of a compromise.

  * **Client metadata enrichment** : Retrieve detailed client information, including OS version, hardware specifications, and network configuration, to provide context for security alerts.

  * **Automated incident response** : Use playbooks to list active clients or search for suspicious artifacts immediately upon detection of malicious activity.




## Before you begin

Before you configure the integration in Google SecOps, verify that your GRR Rapid Response environment meets the following requirements:

  * **API credentials** : You must have a valid username and password for a user account with API access to the GRR server.

  * **Account permissions** : Ensure the account used for the integration has sufficient permissions to initiate flows and search for artifacts on target clients.

  * **Server configuration** : Identify the API root of your GRR server (for example, `https://<grr-server-address>:8000`).

  * **Network access** : Ensure your network configuration allows outbound HTTPS connections from your Google SecOps environment to the GRR API endpoint.




## Integration parameters

The **GRR Rapid Response** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` |  Required. The base URL of the GRR server API, including the port (for example, `https://grr.example.com:8000`).  
`Username` |  Required. The username of the GRR account used to authenticate the connection.  
`Password` |  Required. The password associated with the GRR account used for authentication.  
`Verify SSL` |  Optional. If selected, the integration validates the SSL certificate when connecting to the GRR server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Client Details

Use the **Get Client Details** action to retrieve full client details.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Client Details** action requires the following parameters:

Parameter | Description  
---|---  
`Client ID` | Required.The ID of the client. This parameter accepts multiple values as a comma-separated string.  
  
#### Action outputs

The **Get Client Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Client Details** action can generate the following table:

Table name: **GRR Clients Details**

Table columns:

  * **Client ID**
  * **Host**
  * **OS Version**
  * **Labels**
  * **Memory Size**
  * **Client Version**
  * **First Seen**
  * **Last Seen**
  * **OS Install Date**



##### JSON result

The following example shows the JSON result output received when using the **Get Client Details** action:
    
    
    [
            {
                "HardwareInfo": {
                    "system_product_name": "HVM domU",
                    "bios_rom_size": "64 kB",
                    "bios_vendor": "Xen",
                    "system_sku_number": "Not Specified",
                    "system_family": "Not Specified",
                    "system_uuid": "UUID",
                    "system_manufacturer": "Xen",
                    "bios_release_date": "08/24/2006",
                    "bios_version": "4.2.amazon",
                    "serial_number": "UUID",
                    "bios_revision": "4.2"
                },
                "LastClock": 1535907460060247,
                "Interfaces": [
                    {
                        "ifname": "lo",
                        "addresses": [
                            {
                                "packed_bytes": "fwAAAQ==",
                                "address_type": "INET"
                            },
                            {
                                "packed_bytes": "AAAAAAAAAAAAAAAAAAAAAQ==",
                                "address_type": "INET6"
                            }
                        ],
                        "mac_address": "MAC_ADDRESS"
                    },
                    {
                        "ifname": "eth0",
                        "addresses": [
                            {
                                "packed_bytes": "rB8sWw==",
                                "address_type": "INET"
                            },
                            {
                                "packed_bytes": "/oAAAAAAAAAE1kv//h5yfg==",
                                "address_type": "INET6"
                            }
                        ],
                        "mac_address": "MAC_ADDRESS"
                    }
                ],
                "OS": {
                    "kernel": "4.4.0-1065-aws",
                    "install_date": 1534280169000000,
                    "system": "Linux",
                    "fqdn": "ip-192-0-2-91.example",
                    "machine": "x86_64",
                    "version": "16.4",
                    "release": "Ubuntu"
                },
                "AgentInfo": {
                    "client_name": "grr",
                    "client_description": "grr linux amd64",
                    "client_version": 3232,
                    "build_time": "2018-06-28 09:37:57"
                },
                "Labels": [],
                "LastBootedAt": 1535292604000000,
                "FirstSeenAt": 1535293827970976,
                "User": [],
                "Volumes": [
                    {
                        "total_allocation_units": 50808745,
                        "bytes_per_sector": 4096,
                        "sectors_per_allocation_unit": 1,
                        "unixvolume": {
                            "mount_point": "/"
                        },
                        "actual_available_allocation_units": 50027766
                    }
                ],
                "LastCrashAt": null,
                "LastSeenAt": 1535907460075229,
                "ID": "CLIENT_ID"
            }
    ]
    

##### Output messages

The **Get Client Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully fetched details for the following clients: CLIENT_ID_LIST.` `Could not fetch details for the specified clients. CLIENT_ID does not exist.` | The action succeeded.  
`Error executing action "Get Client Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Client Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Hunt Details

Use the **Get Hunt Details** action to retrieve hunt details.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Hunt Details** action requires the following parameters:

Parameter | Description  
---|---  
`Hunt ID` | Required.The ID of a hunt to retrieve. This parameter accepts multiple values as a comma-separated string.  
  
#### Action outputs

The **Get Hunt Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall link

The **Get Hunt Details** action can generate the following link:

`API_ROOT/#/hunts/HUNT_ID`

##### JSON result

The following example shows the JSON result output received when using the **Get Hunt Details** action:
    
    
    [
            {
                "Name": "ExampleHunt",
                "Expires": 1537063517000000,
                "Description": "test",
                "Creator": "admin",
                "IsRobot": false,
                "Status": "PAUSED",
                "Hunt_ID": "HUNT_ID",
                "Created": 1535853917657925,
                "Start_Time": 1535853917657925,
                "Duration": "2w",
                "Expiration time": " ",
                "Crash_limit": 100,
                "Client_limit": 100,
                "Client_rate (clients/min)": "20.5",
                "Client_Queued": "20.5",
                "Client_Scheduled": "20.5",
                "Client_Outstanding": "20.5",
                "Client_Completed": "20.5",
                "Client_with Results": "20.5",
                "Results": "20.5",
                "Total_CPU_Time_Used": "20.5",
                "Total_Network_Traffic": "20.5",
                "Flow_Name": "KeepAlive",
                "Flow_Arguments": "20.5",
                "Client_Rule_Set": " "
            }
    ]
    

##### Output messages

The **Get Hunt Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully fetched details for the HUNT_ID hunt.` `Could not fetch details for the specified hunts. HUNT_ID does not exist.` `` | The action succeeded.  
`Error executing action "Get Hunt Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Hunt Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Clients

Use the **List Clients** action to search for clients and interact with them.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Clients** action requires the following parameters:

Parameter | Description  
---|---  
`Offset` | Optional.The starting point (offset) to search for clients.  
`Max Results To Return` | Optional.The maximum number of clients to return in in every response.The default value is `5`.  
  
#### Action outputs

The **List Clients** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Clients** action can generate the following table:

Table name: **GRR Clients**

Table columns:

  * **Client ID**
  * **Host**
  * **OS Version**
  * **First Seen**
  * **Client Version**
  * **Labels**
  * **Last Check In**
  * **OS Install Date**



##### JSON result

The following example shows the JSON result output received when using the **List Clients** action:
    
    
    [{
        "Client_ID": "CLIENT_ID",
        "Agent_Info":{
           "Client_Name": "example",
           "Client_Version": 3420}
        "OS_Info":{
           "System": "Linux",
           "Release": "Ubuntu",
           "Architecture": "x86_64",
           "Installation_Time": "2020-04-09 13:44:17 UTC",
           "Kernel": "4.15.0-96-generic",
           "Version": "18.04"}
        "Client_Last_Booted_At": "",
        "Client_First_Seen_At": "2020-09-25 14:26:38 UTC",
        "Client_Last_Seen": "2020-11-19 10:12:52 UTC",
        "Client_Last_Clock": "2020-11-19 10:12:52 UTC",
        "Memory_Size": "985.6MiB",
        "Client_Labels": []
       }]
    

##### Output messages

The **List Clients** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully listed available clients in GRR.` `No clients are available in GRR.` | The action succeeded.  
`Error executing action "List Clients". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Clients** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Hunts

Use the **List Hunts** action to retrieve information about all available hunts.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Hunts** action requires the following parameters:

Parameter | Description  
---|---  
`Creator` | Optional.A user who created a hunt.  
`Offset` | Optional.The starting point (offset) to search for hunts.  
`Max Results To Return` | Optional.The maximum number of hunts to return in every response.The default value is `5`.  
  
#### Action outputs

The **List Hunts** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Hunts** action can generate the following table:

Table name: **Hunts**

Table columns:

  * **Hunt ID**
  * **Status**
  * **Creation Time**
  * **Start Time**
  * **Duration**
  * **Client Limit**
  * **Expiration Time**
  * **Creator**
  * **Description**



##### JSON result

The following example shows the JSON result output received when using the **List Hunts** action:
    
    
    [
        {
            "Hunt_Description": "Interrogate run by cron to keep host info fresh.",
            "Creator": "GRRCron",
            "Is_Robot": false,
            "State": "STARTED",
            "Creation Time": "1605690387510082",
            "Start Time (initial)": "1605690387678448",
            "Start Time (last)": "1605690387678448",
            "Duration": " ",
            "Client Limit": 0,
            "Expiration Time": " ",
            "Hunt_ID": "HUNT_ID",
        }
    ]
    

##### Output messages

The **List Hunts** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully listed hunts.` `Could not list hunts for the specified creator. CREATOR_ID< does not exist.` `Could not list hunts for the specified creator. Please check the Offset value.` | The action succeeded.  
`Error executing action "List Hunts". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Hunts** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Launched Flows

Use the **List Launched Flows** action to list the flows launched on a specified client.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

The **List Launched Flows** action requires the following parameters:

Parameter | Description  
---|---  
`Offset` | Optional.The starting point (offset) to search for flows.  
`Max Results To Return` | Optional.A maximum number of flows to return in every response.The default value is `5`.  
  
#### Action outputs

The **List Launched Flows** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Launched Flows** action can generate the following table:

Table name: **GRR Launch Flows**

Table columns:

  * **Flow Name**
  * **Flow ID**
  * **State**
  * **Creation Time**
  * **Last Active**
  * **Creator**



##### JSON result

The following example shows the JSON result output received when using the **List Launched Flows** action:
    
    
    {
        "Creator": "admin",
        "NestedFlow": [],
        "LastActiveAt": 1535900632278975,
        "Args": {
            "ARGUMENTS"
        },
        "State": "TERMINATED",
        "StartedAt": 1535900542745106,
        "Flow_ID": "FLOW_ID",
        "Flow_Name": "FLOW_NAME"
    }
    

##### Output messages

The **List Launched Flows** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully listed flows launched on CLIENT_ID client.` `Could not list flows. No entities were found.` `Could not list flows. IPs or Hosts entities were not found in current scope.` `Could not list flows on the following entities: ENTITY_ID.` | The action succeeded.  
`Error executing action "List Launched Flows". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Launched Flows** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to GRR Rapid Response.

This action doesn't run on Google SecOps entities. 

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
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the GRR server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the GRR server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Start A Hunt

Use the **Start A Hunt** action to start a newly created hunt. By default, the GRR Rapid Response assigns the `PAUSED` state to all new hunts.

The GRR Rapid Response sets all hunts that reached their client limit to the `PAUSED` state. After you remove the client limit, you can use the **Start A Hunt** action to restart paused hunts.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Start A Hunt** action requires the following parameters:

Parameter | Description  
---|---  
`Hunt ID` | Required.The ID of a the hunt to start. This parameter accepts multiple values as a comma-separated string.  
  
#### Action outputs

The **Start A Hunt** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Start A Hunt** action:
    
    
    [{ "Hunt_ID": "HUNT_ID", "State": STARTED}]
    

##### Output messages

The **Start A Hunt** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully started the following hunts: HUNT_ID_LIST.` `Could not start the following hunts. HUNT_ID_LIST could not be found in GRR.` `Could not stop the following hunts: HUNT_ID_LIST. Hunt can only be started from PAUSED state.` | The action succeeded.  
`Error executing action "Start A Hunt". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
### Stop A Hunt

Use the **Stop A Hunt** action to prevent new clients from scheduling and interrupt current flows at the moment when their state changes.

After you stop a hunt, you cannot resume it. This action deletes all current results that are in progress and doesn't affect the results that are already reported.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Stop A Hunt** action requires the following parameters:

Parameter | Description  
---|---  
`Hunt ID` | Required.The ID of a hunt to stop. This parameter accepts multiple values as a comma-separated string.  
  
#### Action outputs

The **Stop A Hunt** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Stop A Hunt** action:
    
    
    [{ "Hunt_ID": "HUNT_ID", "State": STOPPED}]
    

##### Output messages

The **Stop A Hunt** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully stopped the following hunts: HUNT_ID_LIST.` `Could not stop the following hunts. HUNT_ID_LIST could not be found in GRR.` `Could not stop the following hunts: HUNT_ID_LIST. Hunt can only be stopped from STARTED or PAUSED states.` | The action succeeded.  
`Error executing action "Stop A Hunt". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Stop A Hunt** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
