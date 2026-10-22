---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sentinelonev2/
title: Integrate SentinelOne v2 with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:17.510945+00:00
---

# Integrate SentinelOne v2 with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sentinelonev2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate SentinelOne v2 with Google SecOps

This document explains how to configure and integrate SentinelOne v2 with Google Security Operations.

This integration supports SentinelOne API version 2.0 and higher.

**Important:** In the Google SecOps platform, the integration for SentinelOne v2 is called _SentinelOneV2_.

This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/SentinelOneV2.zip).

## Use cases

The SentinelOne integration can help you solve the following use cases:

  1. **Contain infected endpoints** : use Google SecOps capabilities to isolate an infected host and prevent lateral movement and data exfiltration.

  2. **Retrieve detailed endpoint information** : use Google SecOps capabilities to enrich incident data with in-depth host analysis for better context and decision-making. You can automatically query SentinelOne for detailed information about an endpoint involved in an alert, including agent version, operating system, and network interfaces.

  3. **Initiate Deep Visibility scans** : use Google SecOps capabilities to hunt for threats and hidden malware on suspect machines and initiate a full disk scan using SentinelOne when suspicious activity is detected, such as unusual file modifications or registry changes.

  4. **Investigate threats with threat intelligence** : use Google SecOps capabilities to improve accuracy by correlating SentinelOne alerts with threat intelligence data, forward suspicious hashes, file paths, or IP addresses found within SentinelOne alerts to threat intelligence platforms.

  5. **Triage malware** : use Google SecOps capabilities to automatically classify malware with static analysis tools for streamlined incident response. You can extract samples from infected endpoints, trigger the analysis within your environment, and receive classification for the malware based on the static analysis.




## Before you begin

To authenticate the connection between Google SecOps and your SentinelOne instance, you must provide a valid SentinelOne API token.

You can generate a personal API token within your SentinelOne management console.

For detailed instructions on generating and managing tokens, go to the [SentinelOne Customer Portal](https://community.sentinelone.com/s/article/000006575).

## Integration parameters

The SentinelOne v2 integration requires the following parameters:

Parameter | Description  
---|---  
`API root` | Required. The SentinelOne API root.The default value is `https://{server}.SentinelOne.net/`.  
`API Token` | Required. The SentinelOne API token.To learn more about how to generate the API token for th eintegration, see Before you begin. The SentinelOne security policy requires you to create a new API token every six months.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Sentinel server.Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Threat Note

Use the **Add Threat Note** action to add a note to the threat in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Threat Note** action requires the following parameters:

Parameter | Description  
---|---  
`Threat ID` | Required.The ID of the threat to add a note.  
`Note` | Required.A note to add to the threat.  
  
#### Action outputs

The **Add Threat Note** action provides the following outputs:

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

The **Add Threat Note** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added note to the threat THREAT_ID in SentinelOne.` `Action wasn't able to add a note to the threat THREAT_ID in SentinelOne.` | The action succeeded.  
`Error executing action "Add Threat Note". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Threat Note** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Create Device Control Rule

Use the **Create Device Control Rule** action to create a device control rule in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Create Device Control Rule** action requires the following parameters:

Parameter | Description  
---|---  
`Rule JSON` | Required. The JSON object representing the device control rule configuration. The default value is as follows:
    
    
       {
            "ruleName": "String",
            "interface": "String",
            "ruleType": "String",
            "action": "String",
            "accessPermission": "String",
            "deviceClass": "String",
            "status": "String"
        }  
  
`Scope JSON` | Required. The JSON object representing the scope rule configuration. The default value is as follows:
    
    
       {
            "accountIds": "String",
            "groupIds": "String",
            "siteIds": "String"
        }  
  
#### Action outputs

The **Create Device Control Rule** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Create Device Control Rule** action:
    
    
    {
        "data": {
            "accessPermission": "Read-Write",
            "action": "Allow",
            "bluetoothAddress": null,
            "createdAt": "2024-01-01T00:00:00.000000Z",
            "creator": "[USERNAME] ([EMAIL_ADDRESS])",
            "creatorId": "[CREATOR_ID]",
            "deviceClass": "FFh",
            "deviceClassName": "FF Vendor Specific",
            "deviceId": null,
            "deviceInformationServiceInfoKey": null,
            "deviceInformationServiceInfoValue": null,
            "deviceName": null,
            "editable": true,
            "gattService": null,
            "id": "[RULE_ID]",
            "interface": "USB",
            "manufacturerName": null,
            "minorClasses": null,
            "order": 1,
            "productId": null,
            "ruleName": "Test",
            "ruleType": "class",
            "scope": "account",
            "scopeId": "[SCOPE_ID]",
            "scopeName": "[SCOPE_NAME]",
            "status": "Disabled",
            "uid": null,
            "updatedAt": "2024-01-01T00:00:00.000000Z",
            "vendorId": null,
            "version": null
        }
    }
    

##### Output messages

The **Create Device Control Rule** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created a Device Control Rule in SentinelOne.` | The action succeeded.  
`Error executing action "Create Device Control Rule". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Device Control Rule** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Create Hash Black List Record

Use the **Create Hash Black List Record** action to add hashes to a blocklist in SentinelOne.

This action only supports SHA-1 hashes.

This action runs on the Google SecOps `Hash` entity.

#### Action inputs

The **Create Hash Black List Record** action requires the following parameters:

Parameter | Description  
---|---  
`Operating System` | Required.An operating system for the hash.The possible values are as follows:

  * `windows`
  * `windows_legacy`
  * `macos`
  * `linux`

The default value is `windows`.  
`Site IDs` | Optional.A comma-separated list of site IDs to send to the blocklist.  
`Group IDs` | Optional.A comma-separated list of group IDs to send to the blocklist.  
`Account IDs` | Optional.A comma-separated list of account IDs to send to the blocklist.  
`Description` | Optional.Additional information related to a hash.The default value is `""`.  
`Add to global blocklist` | Required.If selected, the action adds a hash to a global blocklist.If you select this parameter, the action ignores the `Site IDs`, `Group IDs`, and `Account IDs` parameters.  
  
#### Action outputs

The **Create Hash Black List Record** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Hash Black List Record** action:
    
    
    [
        {
            "Entity": "ENTITY_ID",
            "EntityResult": [{
                "userName": "user",
                "description": "Created by user.",
                "userId": "USER_ID",
                "scopeName": "Test Group",
                "value": "36F9CA40B3CE96FCEE1CF1D4A7222935536FD25A",
                "source": "user",
                "updatedAt": "2020-07-02T14:41:20.678280Z",
                "osType": "windows",
                "scope": {
                    "groupIds": ["GROUP_ID"]
                },
                "type": "white_hash",
                "id": "ENTITY_ID",
                "createdAt": "2020-07-02T14:41:20.678690Z"
            }, {
                "userName": "user",
                "description": "Created by user.",
                "userId": "USER_ID",
                "scopeName": "Test Group 2",
                "value": "36F9CA40B3CE96FCEE1CF1D4A7222935536FD25A",
                "source": "user",
                "updatedAt": "2020-07-02T14:41:20.683858Z",
                "osType": "windows",
                "scope": {
                    "groupIds": ["GROUP_ID"]
                },
                "type": "white_hash",
                "id": "ENTITY_ID",
                "createdAt": "2020-07-02T14:41:20.684677Z"
            }]
        }
    ]
    

##### Output messages

The **Create Hash Black List Record** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added the following hashes to the blocklist in SentinelOne: ENTITY_ID.` `The following hashes were already a part of blocklist in SentinelOne: ENTITY_ID.` `Action wasn't able to add the following hashes to the blocklist in SentinelOne: ENTITY_ID.` `No hashes were added to the blocklist in SentinelOne.` | The action succeeded.  
`Error executing action "Create Hash Black List Record". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Hash Black List Record** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Create Hash Exclusion Record

Use the **Create Hash Exclusion Record** action to add a hash to the exclusion list in SentinelOne.

This action only supports SHA-1 hashes.

This action runs on the Google SecOps `Hash` entity.

#### Action inputs

The **Create Hash Exclusion Record** action requires the following parameters:

Parameter | Description  
---|---  
`Operation System` | Required.An operation system (OS) for the hash. The possible values are as follows:

  * `windows`
  * `windows_legacy`
  * `macos`
  * `linux`

The default value is `windows`.  
`Site IDs` | Optional. A comma-separated list of site IDs to send the hash to the exclusion list.The action requires at least one valid value.  
`Group IDs` | Optional.A comma-separated list of group ID to send the hash to the exclusion list.The action requires at least one valid value.  
`Account IDs` | Optional.A comma-separated list of account IDs to send the hash to the exclusion list.  
`Description` | Optional. Additional information related to the hash.  
`Add to global exclusion list` | Optional. If selected, the action adds a hash to the global exclusion list. If you select this parameter, the action ignores the `Site IDs`, `Group IDs`, and `Account IDs` parameters.  
  
#### Action outputs

The **Create Hash Exclusion Record** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Hash Exclusion Record** action:
    
    
    [
        {
        "ENTITY_ID":
            {
            "ID": "ALLOWLISTED_ENTITY_ID",
            "Created Time": "ITEM_CREATION_TIME",
            "Scope ID": "SITE_OR_GROUP_ID",
            "Scope Name": "example_scope"
            }
        }
    ]
    

##### Output messages

The **Create Hash Exclusion Record** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added the following hashes to the exclusion list in SentinelOne: HASH_ID` `The following hashes were already a part of exclusion list in SentinelOne: HASH_ID` `Action wasn't able to add the following hashes to the exclusion list in SentinelOne: HASH_ID` `No hashes were added to the exclusion list in SentinelOne.` | The action succeeded.  
`Error executing action "Create Hash Exclusion Record". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Hash Exclusion Record** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Create Path Exclusion Record

Use the **Create Path Exclusion Record** action to add a path to the exclusion list in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Create Path Exclusion Record** action requires the following parameters:

Parameter | Description  
---|---  
`Path` | Required. A path to add to the exclusion list.  
`Operation System` | Required.An operation system (OS) for the hash. The possible values are as follows:

  * `windows`
  * `windows_legacy`
  * `macos`
  * `linux`

The default value is `windows`.  
`Site IDs` | Optional. A comma-separated list of site IDs to send the hash to the exclusion list.The action requires at least one valid value.  
`Group IDs` | Optional.A comma-separated list of group ID to send the hash to the exclusion list.The action requires at least one valid value.  
`Account IDs` | Optional.A comma-separated list of account IDs to send the hash to the exclusion list.  
`Description` | Optional. Additional information related to the hash.  
`Add to global exclusion list` | Optional. If selected, the action adds a hash to the global exclusion list. If you select this parameter, the action ignores the `Site IDs`, `Group IDs`, and `Account IDs` parameters.  
`Include Subfolders` | Optional. If selected, the action includes subfolders for the provided path. This parameter only applies if you configure a folder path in the `Path` parameter.  
`Mode` | Optional. A mode to use for the excluded path.The possible values are as follows:

  * `Suppress Alerts`
  * `Interoperability`
  * `Interoperability - Extended`
  * `Performance Focus`
  * `Performance Focus - Extended`

The default value is `Suppress Alerts`.  
  
#### Action outputs

The **Create Path Exclusion Record** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Path Exclusion Record** action:
    
    
    [
        {
        "ENTITY_ID":
            {
            "ID": "ALLOWLISTED_ENTITY_ID",
            "Created Time": "ITEM_CREATION_TIME",
            "Scope ID": "SITE_OR_GROUP_ID",
            "Scope Name": "example_scope"
            }
        }
    ]
    

##### Output messages

The **Create Path Exclusion Record** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added the following path to the exclusion list in SentinelOne: PATH` `The following paths were already a part of exclusion list in SentinelOne: PATH_LIST` `Action wasn't able to add the following paths to the exclusion list in SentinelOne: PATH` `No paths were added to the exclusion list in SentinelOne.` | The action succeeded.  
`Error executing action "Create Path Exclusion Record". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Path Exclusion Record** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete Device Control Rule

Use the **Delete Device Control Rule** action to delete a device control rule in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Delete Device Control Rule** action requires the following parameters:

Parameter | Description  
---|---  
`Rule ID` | Required. The ID of the rule to delete.  
`Scope Type` | Optional. The organizational level where the alert is visible or applicable. The possible values are as follows:

  * `Account`
  * `Site`
  * `Group`

The default value is `Account`.  
`Scope ID` | Required. The ID of the scope.  
  
#### Action outputs

The **Delete Device Control Rule** action provides the following outputs:

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

The **Delete Device Control Rule** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully deleted a Device Control Rule with ID RULE_DEVICE_ID in SentinelOne.` `Rule RULE_DEVICE_ID wasn't found in SentinelOne.` | The action succeeded.  
`Error executing action "Delete Device Control Rule". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Device Control Rule** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Delete Hash Blacklist Record

Use the **Delete Hash Blacklist Record** action to delete hashes from a blocklist in SentinelOne.

This action only supports the SHA-1 hashes.

This action runs on the Google SecOps `Hash` entity.

#### Action inputs

The **Delete Hash Blacklist Record** action requires the following parameters:

Parameter | Description  
---|---  
`Site IDs` | Optional.A comma-separated list of site IDs to remove the hash.  
`Group IDs` | Optional.A comma-separated list of group IDs to remove the hash.  
`Account IDs` | Optional.A comma-separated list of account IDs to remove the hash.  
`Remove from global black list` | Optional.If selected, the action removes the hash from the global blocklist.If you select this parameter, the action ignores the `Site IDs`, `Group IDs`, and `Account IDs` parameters.  
  
#### Action outputs

The **Delete Hash Blacklist Record** action provides the following outputs:

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

The **Delete Hash Blacklist Record** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully removed the following hashes from the blocklist in SentinelOne: ENTITY_ID.` `The following hashes were not found in a blocklist in SentinelOne: ENTITY_ID.` `Action wasn't able to remove the following hashes to the blocklist in SentinelOne: ENTITY_ID.` `No hashes were removed from the blocklist in SentinelOne.` | The action succeeded.  
`Error executing action "Delete Hash Blacklist Record". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Hash Blacklist Record** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Disconnect Agent From Network

Use the **Disconnect Agent From Network** action to disconnect an agent from a network using the agent's hostname or IP address.

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
Output messages | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Disconnect Agent From Network** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Download Threat File

Use the **Download Threat File** action to download a file related to a threat in SentinelOne.

To retrieve threat files in SentinelOne, you need any of the following roles:

  * `Admin`
  * `IR Team`
  * `SOC`



This action doesn't run on Google SecOps entities. 

#### Action limitations

The **Download Threat File** action can reach timeout when SentinelOne retrieves a file, but doesn't provide a download URL.

To investigate the cause for timeout, go to the threat timeline.

#### Action inputs

The **Download Threat File** action requires the following parameters:

Parameter | Description  
---|---  
`Threat ID` | Required.The ID of the threat to download a file.  
`Password` | Required.A password for the zipped folder that contains the threat file.The password requirements are as follows:

  * Is at least 10 characters long.
  * Includes uppercase letters, lowercase letters, digits, and special symbols.

The maximum length for the password is 256 characters.  
`Download Folder Path` | Required.A path to a folder to store the threat file.  
`Overwrite` | Required.If selected, the action overwrites a file with the identical name.Not selected by default.  
  
#### Action outputs

The **Download Threat File** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Download Threat File** action:
    
    
    {
        "absolute_path": "ABSOLUTE_PATH"
    }
    

##### Output messages

The **Download Threat File** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully downloaded the file related to threat THREAT_ID in SentinelOne.` `Action wasn't able to download the file related to threat THREAT_ID. Reason: The action was able to initiate the downloading of the file, but SentinelOne didn't return a download URL.` `Waiting for the download link to appear in SentinelOne.` | The action succeeded.  
`Error executing action "Download Threat File". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Download Threat File** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enrich Endpoints

Use the **Enrich Endpoints** action to enrich information about the endpoint using the IP address or hostname.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

The **Enrich Endpoints** action requires the following parameters:

Parameter | Description  
---|---  
`Create Insight` | Optional.If selected, the action creates an insight with information about endpoints.  
`Only Infected Endpoints Insights` | Optional.If selected, the action only creates insights for infected endpoints.  
  
#### Action outputs

The **Enrich Endpoints** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Enrich Endpoints** action:
    
    
    {
        "accountId": "ACCOUNT_ID",
        "accountName": "SentinelOne",
        "activeDirectory": {
            "computerDistinguishedName": "CN=LP-EXAMPLE,CN=Computers,DC=EXAMPLE,DC=LOCAL",
            "computerMemberOf": [],
            "lastUserDistinguishedName": "CN=Example,OU=Users,OU=PS,OU=IL,OU=Operations,OU=EXAMPLE,DC=EXAMPLE,DC=LOCAL",
            "lastUserMemberOf": [
                "CN=esx.cs,OU=ESX,OU=GROUPS,OU=IL,OU=IT,OU=EXAMPLE,DC=EXAMPLE,DC=LOCAL",
                "CN=Backup Operators,CN=Builtin,DC=EXAMPLE,DC=LOCAL",
                "CN=esx.product,OU=ESX,OU=GROUPS,OU=IL,OU=IT,OU=EXAMPLE,DC=EXAMPLE,DC=LOCAL",
                "CN=EXAMPLE_Admins,OU=QA,OU=IL,OU=IT,OU=EXAMPLE,DC=EXAMPLE,DC=LOCAL",
                "CN=Local Admin,OU=GROUPS,OU=IL,OU=IT,OU=EXAMPLE,DC=EXAMPLE,DC=LOCAL",
                "CN=CSM,OU=Operations,OU=EXAMPLE,DC=EXAMPLE,DC=LOCAL",
                "CN=Event Log Readers,CN=Builtin,DC=EXAMPLE,DC=LOCAL"
            ]
        },
        "activeThreats": 0,
        "agentVersion": "4.1.4.82",
        "allowRemoteShell": false,
        "appsVulnerabilityStatus": "patch_required",
        "computerName": "LP-EXAMPLE",
        "consoleMigrationStatus": "N/A",
        "coreCount": 8,
        "cpuCount": 8,
        "cpuId": "Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz",
        "createdAt": "2020-05-31T07:22:14.695136Z",
        "domain": "EXAMPLE",
        "encryptedApplications": false,
        "externalId": "",
        "externalIp": "192.0.2.91",
        "groupId": "863712577864500060",
        "groupIp": "192.0.2.0",
        "groupName": "Test Group",
        "id": "ID",
        "inRemoteShellSession": false,
        "infected": false,
        "installerType": ".msi",
        "isActive": false,
        "isDecommissioned": false,
        "isPendingUninstall": false,
        "isUninstalled": false,
        "isUpToDate": true,
        "lastActiveDate": "2021-01-12T12:59:43.143066Z",
        "lastIpToMgmt": "192.0.2.20",
        "lastLoggedInUserName": "EXAMPLE",
        "licenseKey": "",
        "locationType": "fallback",
        "locations": [
            {
                "id": "ID",
                "name": "Fallback",
                "scope": "global"
            }
        ],
        "machineType": "laptop",
        "mitigationMode": "protect",
        "mitigationModeSuspicious": "protect",
        "modelName": "Dell Inc. - Latitude 7490",
        "networkInterfaces": [
            {
                "id": "ID",
                "inet": [
                    "192.0.2.20"
                ],
                "inet6": [
                    "2001:db8:1:1:1:1:1:1",
                    "2001:db8:2:2:2:2:2:2",
                    "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
                ],
                "name": "Wi-Fi",
                "physical": "MAC_ADDRESS"
            },
            {
                "id": "ID",
                "inet": [
                    "192.168.193.193"
                ],
                "inet6": [
                    "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
                ],
                "name": "vEthernet (Default Switch)",
                "physical": "MAC_ADDRESS"
            },
            {
                "id": "ID",
                "inet": [
                    "201.0.113.1"
                ],
                "inet6": [
                    "2001:db8:1:1:1:1:1:1",
                    "2001:db8:2:2:2:2:2:2"
                ],
                "name": "vEthernet (DockerNAT)",
                "physical": "MAC_ADDRESS"
            }
        ],
        "networkStatus": "connecting",
        "osArch": "64 bit",
        "osName": "Windows 10 Pro",
        "osRevision": "18363",
        "osStartTime": "2021-01-03T15:38:32Z",
        "osType": "windows",
        "osUsername": null,
        "rangerStatus": "NotApplicable",
        "rangerVersion": null,
        "registeredAt": "2020-05-31T07:22:14.691561Z",
        "scanAbortedAt": null,
        "scanFinishedAt": "2020-05-31T09:28:53.867014Z",
        "scanStartedAt": "2020-05-31T07:25:37.814972Z",
        "scanStatus": "finished",
        "siteId": "SITE_ID",
        "siteName": "example.com",
        "threatRebootRequired": false,
        "totalMemory": 16263,
        "updatedAt": "2021-01-18T13:33:43.834618Z",
        "userActionsNeeded": [],
        "uuid": "UUID"
    }
    

##### Output messages

The **Enrich Endpoints** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved information about the following endpoints from SentinelOne: ENTITY_ID ` `Action wasn't able to retrieve information about the following endpoints from SentinelOne: ENTITY_ID ` `No information was retrieved for provided entities.` | The action succeeded.  
`Error executing action "Enrich Endpoints". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Endpoints** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Agent Status

Use the **Get Agent Status** action to retrieve information about the status of agents on the endpoints based on the provided entity.

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
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Agent Status** action:
    
    
    {
    "status": "Not active"
    }
    

##### Output messages

The **Get Agent Status** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved information about agent status for the following endpoints: ENTITY_ID` `Action wasn't able to retrieve information about agent status for the following endpoints: ENTITY_ID ` `No information about agent status was found for the provided endpoints.` | The action succeeded.  
`Error executing action "Get Agent Status". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Agent Status** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Application List for Endpoint

Use the **Get Application List for Endpoint** action to retrieve information about available applications on an endpoint using the provided entities.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

The **Get Application List for Endpoint** action requires the following parameters:

Parameter | Description  
---|---  
`Max Applications To Return` | Optional.The maximum number of applications to return. If you don't set a number, the action returns all available applications.  
  
#### Action outputs

The **Get Application List for Endpoint** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Application List for Endpoint** action:
    
    
    {
        "data": [
            {
                "installedDate": "2021-01-06T08:55:56.762000Z",
                "name": "Mozilla Firefox 84.0.1 (x64 en-US)",
                "publisher": "Mozilla",
                "size": 211562,
                "version": "84.0.1"
            }
        ]
    }
    

##### Output messages

The **Get Application List for Endpoint** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved available applications for the following endpoints: ENTITY_ID.` `Action wasn't able to retrieve available applications for the following endpoints: ENTITY_ID. ` `No applications were retrieved for provided endpoints.` | The action succeeded.  
`Error executing action "Get Application List for Endpoint". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Application List for Endpoint** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Blacklist

Use the **Get Blacklist** action to get a list of all the items available in the blocklist in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Blacklist** action requires the following parameters:

Parameter | Description  
---|---  
`Hash` | Optional.A comma-separated list of hashes to check in the blocklist.The action only returns hashes that were found.If you set the `Hash`, the action ignores the `Limit` parameter.  
`Site IDs` | Optional.A comma-separated list of site IDs to return blocklist items.  
`Group IDs` | Optional.A comma-separated list of group IDs to return blocklist items.  
`Account Ids` | Optional.A comma-separated list of account IDs to return blocklist items.  
`Limit` | Optional.A number of blocklist items to return.If you set the `Hash` parameter, the action ignores this parameter. The maximum value is `1000`.The default value is `50`.  
`Query` | Optional.A query to filter results.  
`Use Global Blacklist` | Optional.If selected, the action returns hashes from a global blocklist.Not selected by default.  
  
#### Action outputs

The **Get Blacklist** action provides the following outputs:

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

The **Get Blacklist** action can return the following table:

Table name: **Blocklist Hashes**

Table columns:

  * **Hash**
  * **Scope**
  * **Description**
  * **OS**
  * **User**



##### JSON result

The following example shows the JSON result output received when using the **Get Blacklist** action:
    
    
    [
        {
            "userName": "Example",
            "description": "test",
            "userId": "USER_ID",
            "scopeName": "Example.com",
            "value": "cf23df2207d99a74fbe169e3eba035e633bxxxxx",
            "source": "user",
            "updatedAt": "2020-02-27T15:02:54.686991Z",
            "osType": "windows",
            "scope": {
                "siteIds": ["SITE_ID"]
            },
            "type": "black_hash",
            "id": "8353960925573xxxxx",
            "createdAt": "2020-02-27T15:02:54.687675Z"
        }, {
            "description": "Detected by SentinelOne Cloud",
            "userId": null,
            "scopeName": "Example.com",
            "value": "3395856ce81f2b7382dee72602f798b642fxxxxx",
            "source": "cloud",
            "updatedAt": "2020-03-18T14:42:02.730095Z",
            "osType": "linux",
            "scope": {
                "siteIds": ["SITE_ID"]
            },
            "type": "black_hash",
            "id": "ENTITY_ID",
            "createdAt": "2020-03-18T14:42:02.730449Z"
        }, {
            "description": "Detected by SentinelOne Cloud",
            "userId": null,
            "scopeName": "Example.com",
            "value": "df531d66173235167ac502b867f3cae2170xxxxx",
            "source": "cloud",
            "updatedAt": "2020-04-08T07:27:35.686775Z",
            "osType": "linux",
            "scope": {
                "siteIds": ["SITE_ID"]
            },
            "type": "black_hash",
            "id": "ENTITY_ID",
            "createdAt": "2020-04-08T07:27:35.687168Z"
        }
    ]
    

##### Output messages

The **Get Blacklist** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved blocklisted hashes based on the provided filter criteria in SentinelOne.` `No blocklisted hashes were found for the provided criteria in SentinelOne.` | The action succeeded.  
`Error executing action "Get Blacklist". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Blacklist** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Deep Visibility Query Result

Use the **Get Deep Visibility Query Result** action to retrieve information about the Deep Visibility query results.

Run this action in combination with the **Initiate Deep Visibility Query** action.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Deep Visibility Query Result** action requires the following parameters:

Parameter | Description  
---|---  
`Query ID` | Required.The ID of the query to return results.The ID value is available in the JSON result of the **Initiate Deep Visibility Query** action as the `query_id` parameter.  
`Limit` | Optional.The number of events to return.The maximum value is `100`.The default value is `50`.  
  
#### Action outputs

The **Get Deep Visibility Query Result** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Deep Visibility Query Result** action can return the following table:

Table name: **SentinelOne Events**

Table columns:

  * **Event Type**
  * **Site Name**
  * **Time**
  * **Agent OS**
  * **Process ID**
  * **Process UID**
  * **Process Name**
  * **MD5**
  * **SHA256**



##### Output messages

The **Get Deep Visibility Query Result** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found events for query: QUERY_ID.` | The action succeeded.  
`Error executing action "Get Deep Visibility Query Result". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Deep Visibility Query Result** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Events for Endpoint Hours Back

Use the **Get Events for Endpoint Hours Back** action to retrieve information about the latest events on an endpoint.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

The **Get Events for Endpoint Hours Back** action requires the following parameters:

Parameter | Description  
---|---  
`Hours Back` | Required.The number of hours prior to now to fetch events.  
`Events Amount Limit` | Optional.The maximum number of events to return for every event type.The default value is `50`.  
`Include File Events Information` | Optional.If selected, the action queries information about `file` events.  
`Include Indicator Events Information` | Optional.If selected, the action queries information about `indicator` events.  
`Include DNS Events Information` | Optional.If selected, the action queries information about `DNS` events.  
`Include Network Actions Events Information` | Optional.If selected, the action queries information about the `network actions` events.  
`Include URL Events Information` | Optional.If selected, the action queries information about `URL` events.  
`Include Registry Events Information` | Optional.If selected, the action queries information about `registry` events.  
`Include Scheduled Task Events Information` | Optional.If selected, the action queries information about `scheduled task` events.  
  
#### Action outputs

The **Get Events for Endpoint Hours Back** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Events for Endpoint Hours Back** action:
    
    
    {
        "data": [
            {
                "activeContentFileId": null,
                "activeContentHash": null,
                "activeContentPath": null,
                "activeContentSignedStatus": null,
                "activeContentType": null,
                "agentDomain": "",
                "agentGroupId": "GROUP_ID",
                "agentId": "ID",
                "agentInfected": false,
                "agentIp": "192.0.2.160",
                "agentIsActive": true,
                "agentIsDecommissioned": false,
                "agentMachineType": "server",
                "agentName": "ip-203-0-113-205",
                "agentNetworkStatus": "connected",
                "agentOs": "linux",
                "agentTimestamp": "2020-03-19T08:17:01.575Z",
                "agentUuid": "UUID",
                "agentVersion": "3.3.1.14",
                "attributes": [
                    {
                        "display": "Created At",
                        "display_attribute": false,
                        "field_id": "agentTimestamp",
                        "priority": 3,
                        "queryable": false,
                        "section": "Main Attributes",
                        "value": "2020-03-19T08:17:01.575Z"
                    },{
                        "display": "Site ID",
                        "display_attribute": false,
                        "field_id": "siteId",
                        "priority": 7,
                        "queryable": true,
                        "section": "Endpoint Info",
                        "value": null
                    }
                ],
                "containerId": null,
                "containerImage": null,
                "containerLabels": null,
                "containerName": null,
                "createdAt": "2020-03-19T08:17:01.575000Z",
                "eventType": "Process Creation",
                "hasParent": true,
                "id": "ID",
                "k8sCluame": null,
                "k8sControllerLabels": null,
                "k8sControllerName": null,
                "k8sControllerType": null,
                "k8sNamespace": null,
                "k8sNamespaceLabels": null,
                "k8sNode": null,
                "k8sPodLabels": null,
                "k8sPodName": null,
                "md5": null,
                "objectType": "process",
                "parentPid": "32461",
                "parentProcessName": "dash",
                "parentProcessStartTime": "2020-03-19T08:17:01.785Z",
                "parentProcessUniqueKey": "KEY",
                "pid": "32462",
                "processCmd": " run-parts --report /etc/cron.hourly",
                "processDisplayName": null,
                "processGroupId": "GROUP_ID",
                "processImagePath": "/bin/run-parts",
                "processImageSha1Hash": "66df74a1f7cc3509c87d6a190ff90ac86caf440d",
                "processIntegrityLevel": "INTEGRITY_LEVEL_UNKNOWN",
                "processIsRedirectedCommandProcessor": "False",
                "processIsWow64": "False",
                "processName": "run-parts",
                "processRoot": "False",
                "processSessionId": "0",
                "processStartTime": "2020-03-19T08:17:01.787Z",
                "processSubSystem": "SUBSYSTEM_UNKNOWN",
                "processUniqueKey": "KEY",
                "publisher": null,
                "relatedToThreat": "False",
                "sha256": null,
                "signatureSignedInvalidReason": null,
                "signedStatus": "unsigned",
                "siteName": "example.com",
                "trueContext": "c98a4557-94b5-da31-5074-fe6360f17228",
                "user": "unknown",
                "verifiedStatus": null
            }
        ],
        "pagination": {
            "nextCursor": "VALUE",
            "totalItems": 632
        }
    }
    

##### Output messages

The **Get Events for Endpoint Hours Back** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved information about the events for the following endpoints: ENDPOINT_ID. ` `Action wasn't able to find any events for the following endpoints: ENDPOINT_ID.` `No information events for the provided endpoints.` | The action succeeded.  
`Error executing action "Get Events for Endpoint Hours Back". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Events for Endpoint Hours Back** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Group Details

Use the **Get Group Details** action to retrieve detailed information about provided groups.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Group Details** action requires the following parameters:

Parameter | Description  
---|---  
`Group Names` | Required.Group names to retrieve details. This parameter accepts multiple values as a comma-separated list.  
  
#### Action outputs

The **Get Group Details** action provides the following outputs:

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

The **Get Group Details** action can return the following table:

Table name: **SentinelOne Groups**

Table columns:

  * **ID**
  * **Name**
  * **Type**
  * **Rank**
  * **Creator**
  * **Creation Time**



##### JSON result

The following example shows the JSON result output received when using the **Get Group Details** action:
    
    
    [
        {
            "GROUP_NAME":"UNEDITABLE_VARIABLERESPONSE_DATA"
        }
    ]
    

##### Output messages

The **Get Group Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved information about the following groups in SentinelOne: GROUP_NAME.` `Action wasn't able to retrieve information about the following groups in SentinelOne: GROUP_NAME. ` `No information about provided groups was found.` | The action succeeded.  
`Error executing action "Get Group Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Group Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Hash Reputation

(Deprecated) Use the **Get Hash Reputation** action to retrieve information about hashes from SentinelOne.

This action runs on the Google SecOps `Hash` entity.

#### Action inputs

The **Get Hash Reputation** action requires the following parameters:

Parameter | Description  
---|---  
`Reputation Threshold` | Optional.A reputation threshold to mark entity as suspicious.If you don't set a value, the action doesn't mark any entity as suspicious.The maximum value is `10`.The default value is `5`.  
`Create Insight` | Optional.If selected, the action creates an insight that contains information about the reputation.  
`Only Suspicious Hashes Insight` | Optional.If selected, the action only creates an insight for hashes with the reputation exceeding or equal to the `Reputation Threshold` value.  
  
#### Action outputs

The **Get Hash Reputation** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Available  
JSON result | Not available  
Output messages | Not available  
Script result | Available  
  
##### Enrichment table

The **Get Hash Reputation** action can enrich the following fields:

Enrichment field name | Applicability  
---|---  
`SENO_reputation` | Returns if it exists in the JSON result.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Hash Reputation** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Process List for Endpoint - Deprecated

**Deprecated:** This action is deprecated. Use the **Get Application List For Endpoint** action instead.

### Get Site Agents

Use the **Get Site Agents** action to retrieve information associated with a specific Site in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Site Agents** action requires the following parameters:

Parameter | Description  
---|---  
`Site Name` | Required. The ID of the alert to return.  
`Max Agents To Return` | Required. The maximum number of agents to return. The maximum value is `1000`. The default value is `100`.  
  
#### Action outputs

The **Get Site Agents** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Site Agents** action:
    
    
    [
        {
            "accountId": "0000000000000000000",
            "accountName": "Customer_Company_Name",
            "activeDirectory": {
                "computerDistinguishedName": null,
                "computerMemberOf": [],
                "lastUserDistinguishedName": null,
                "lastUserMemberOf": [],
                "userPrincipalName": null
            },
            "activeProtection": [
                "edr"
            ],
            "activeThreats": 27,
            "agentVersion": "XX.X.X.X",
            "allowRemoteShell": true,
            "appsVulnerabilityStatus": "not_applicable",
            "cloudProviders": {
                "Google Cloud": {
                    "cloudAccount": "customer-edr-agents-yyyy",
                    "cloudImage": "debian-image-name-vYYYYMMDD",
                    "cloudInstanceId": "0000000000000000000",
                    "cloudInstanceSize": "e2-medium",
                    "cloudLocation": "us-region-x",
                    "cloudNetwork": "private-network-name",
                    "cloudTags": [
                        "corelight-ingress",
                        "Endpoint does not have sufficient permissions to fetch labels"
                    ],
                    "gcpServiceAccount": "000000000000-compute@developer.gserviceaccount.com"
                }
            },
            "computerName": "virtual-machine-name-1",
            "consoleMigrationStatus": "N/A",
            "containerizedWorkloadCounts": null,
            "coreCount": 2,
            "cpuCount": 1,
            "cpuId": "Intel(R) Xeon(R) CPU @ X.XGHz",
            "createdAt": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
            "detectionState": null,
            "domain": "us-region-x.c.customer-edr-agents-yyyy.internal",
            "encryptedApplications": false,
            "externalId": "",
            "externalIp": "000.000.000.000",
            "firewallEnabled": false,
            "firstFullModeTime": null,
            "fullDiskScanLastUpdatedAt": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
            "groupId": "0000000000000000000",
            "groupIp": "000.000.000.0",
            "groupName": "Default Group",
            "hasContainerizedWorkload": false,
            "id": "0000000000000000000",
            "inRemoteShellSession": false,
            "infected": true,
            "installerType": ".deb",
            "isActive": true,
            "isAdConnector": false,
            "isDecommissioned": false,
            "isHyperAutomate": null,
            "isPendingUninstall": false,
            "isUninstalled": false,
            "isUpToDate": true,
            "lastActiveDate": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
            "lastIpToMgmt": "000.000.000.000",
            "lastLoggedInUserName": "",
            "lastSuccessfulScanDate": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
            "licenseKey": "",
            "locationEnabled": false,
            "locationType": "not_supported",
            "locations": null,
            "machineSid": null,
            "machineType": "server",
            "missingPermissions": [],
            "mitigationMode": "detect",
            "mitigationModeSuspicious": "detect",
            "modelName": "Google Google Compute Engine",
            "networkInterfaces": [
                {
                    "gatewayIp": "000.000.000.000",
                    "gatewayMacAddress": "XX:XX:XX:XX:XX:XX",
                    "id": "0000000000000000000",
                    "inet": [
                        "000.000.000.000"
                    ],
                    "inet6": [
                        "fe80::0000:0000:0000:0"
                    ],
                    "name": "ens4",
                    "physical": "XX:XX:XX:XX:XX:XX"
                },
                {
                    "gatewayIp": null,
                    "gatewayMacAddress": null,
                    "id": "0000000000000000000",
                    "inet": [
                        "172.17.0.1"
                    ],
                    "inet6": [],
                    "name": "docker0",
                    "physical": "XX:XX:XX:XX:XX:XX"
                }
            ],
            "networkQuarantineEnabled": false,
            "networkStatus": "connected",
            "operationalState": "na",
            "operationalStateExpiration": null,
            "osArch": "64 bit",
            "osName": "Linux",
            "osRevision": "Debian GNU/11 (bullseye) X.X.X.X-cloud-amd64",
            "osStartTime": "YYYY-MM-DDTHH:MM:SSZ",
            "osType": "linux",
            "osUsername": "user",
            "proxyStates": null,
            "rangerStatus": "Disabled",
            "rangerVersion": null,
            "registeredAt": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
            "remoteProfilingState": "disabled",
            "remoteProfilingStateExpiration": null,
            "scanAbortedAt": null,
            "scanFinishedAt": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
            "scanStartedAt": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
            "scanStatus": "finished",
            "serialNumber": null,
            "showAlertIcon": false,
            "siteId": "0000000000000000000",
            "siteName": "SITE_NAME",
            "storageName": null,
            "storageType": null,
            "tags": {
                "sentinelone": [
                    {
                        "assignedAt": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
                        "assignedBy": "anon.user@google.com",
                        "assignedById": "0000000000000000000",
                        "id": "0000000000000000000",
                        "key": "MD_Containment_Allowlist",
                        "value": "No Value"
                    }
                ]
            },
            "threatRebootRequired": false,
            "totalMemory": 3930,
            "updatedAt": "YYYY-MM-DDTHH:MM:SS.SSSSSSZ",
            "userActionsNeeded": [],
            "uuid": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
        }
    ]
    

##### Output messages

The **Get Site Agents** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about the hosts from Site SITE_NAME in SentinelOne.` `No hosts are associated with Site SITE_NAME in SentinelOne.` | The action succeeded.  
`Error executing action "Get Site Agents". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Site Agents** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get System Status

Use the **Get System Status** action to retrieve the status of a system.

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
JSON result | Available  
Output messages | Not available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get System Status** action:
    
    
    {
        "system_status": {
            "data": {
                "health": "ok"
            }},
        "db_status": {
            "data": {
                "health": "ok"
            }},
        "cache_status": {
            "data": {
                "health": "ok"
            }
        }
    }
    

##### Script result

The following table lists the value for the script result output when using the **Get System Status** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get System Version

Use the **Get System Version** action to retrieve the version of a system.

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
Output messages | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get System Version** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Threats

Use the **Get Threats** action to retrieve information about threats in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Threats** action requires the following parameters:

Parameter | Description  
---|---  
`Mitigation Status` | Optional.A comma-separated list of threat statuses. The action only returns threats that match the configured statuses. The possible values are as follows:

  * `mitigated`
  * `active`
  * `blocked`
  * `suspicious`
  * `suspicious_resolved`

  
`Created until` | Optional. The end time for the threats, such as `2020-03-02T21:30:13.014874Z`.  
`Created from` | Optional. The start time for the threats, such as `2020-03-02T21:30:13.014874Z`.  
`Resolved Threats` | Optional.If selected, the action only returns resolved threats.  
`Threat Display Name` | Optional.A display name of the threat to return.  
`Limit` | Optional.A number of threats to return.The default value is `10`.  
`API Version` | Optional. The version of the API to use for the action. The API version impacts JSON result structure. We recommend using the latest supported API version for your environment. **Important:** Version `2.1` or higher is required to retrieve private and internal IP address data (`agentDetectionInfo_agentIpV4`). The default value is `2.0`.  
  
#### Action outputs

The **Get Threats** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Threats** action:
    
    
    {
                "accountId": "ACCOUNT_ID",
                "accountName": "ACCOUNT_NAME",
                "agentComputerName": "desktop-example",
                "agentDomain": "WORKGROUP",
                "agentId": "AGENT_ID",
                "agentInfected": false,
                "agentIp": "192.0.2.176",
                "agentIsActive": false,
                "agentIsDecommissioned": false,
                "agentMachineType": "desktop",
                "agentNetworkStatus": "connected",
                "agentOsType": "windows",
                "agentVersion": "3.6.6.104",
                "annotation": null,
                "automaticallyResolved": false,
                "browserType": null,
                "certId": "",
                "classification": "generic.heuristic",
                "classificationSource": "Cloud",
                "classifierName": "MANUAL",
                "cloudVerdict": "provider_unknown",
                "collectionId": "838490132723152335",
                "commandId": "835975626369402963",
                "createdAt": "2020-03-02T21:30:13.014874Z",
                "createdDate": "2020-03-02T21:30:12.748000Z",
                "description": "malware detected - not mitigated yet",
                "engines": [
                    "manual"
                ],
                "external_ticket_id": null,
                "fileContentHash": "fc5a9b5e806f35a7b285e012ef8df3f06f399492",
                "fileCreatedDate": null,
                "fileDisplayName": "example.exe",
                "fileExtensionType": "Executable",
                "fileIsDotNet": null,
                "fileIsExecutable": true,
                "fileIsSystem": false,
                "fileMaliciousContent": null,
                "fileObjectId": "99FF941D82E382D1",
                "filePath": "\\Device\\HarddiskVolume3\\Program Files\\example.exe",
                "fileSha256": null,
                "fileVerificationType": "NotSigned",
                "fromCloud": false,
                "fromScan": false,
                "id": "THREAT_ID",
                "indicators": [],
                "initiatedBy": "dvCommand",
                "initiatedByDescription": "Deep Visibility Command",
                "initiatingUserId": "INITIATING_USER_ID",
                "isCertValid": false,
                "isInteractiveSession": false,
                "isPartialStory": false,
                "maliciousGroupId": "0BB46E119EF0AE51",
                "maliciousProcessArguments": "-ServerName:App.Example.mca",
                "markedAsBenign": true,
                "mitigationMode": "protect",
                "mitigationReport": {
                    "kill": {
                        "status": "success"
                    },
                    "network_quarantine": {
                        "status": null
                    },
                    "quarantine": {
                        "status": "success"
                    },
                    "remediate": {
                        "status": null
                    },
                    "rollback": {
                        "status": null
                    },
                    "unquarantine": {
                        "status": "sent"
                    }
                },
                "mitigationStatus": "mitigated",
                "publisher": "",
                "rank": 2,
                "resolved": true,
                "siteId": "SITE_ID",
                "siteName": "Example.com",
                "threatAgentVersion": "3.6.6.104",
                "threatName": "example.exe",
                "updatedAt": "2020-07-07T17:19:48.260119Z",
                "username": "DESKTOP-example\\ddiserens",
                "whiteningOptions": []
    }
    

##### Output messages

The **Get Threats** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved information about the available threats in SentinelOne.` `No information about threats was found based on the provided criteria.` | The action succeeded.  
`Error executing action "Get Threats". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Threats** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Initiate Deep Visibility Query

Use the **Initiate Deep Visibility Query** action to initiate a Deep Visibility query search.

This action returns the query ID value which the **Get Deep Visibility Query Result** action requires.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Initiate Deep Visibility Query** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | Required.A query for the search.For more information about the query syntax, see [SentinelOne Deep Visibility Cheat Sheet](https://assets.sentinelone.com/dv/sentinel-one-dv-chea-1?xs=105462#page=1).  
`Start Date` | Optional.A start date for the search.If you don't set a value, the action retrieves events 30 days prior to now by default.  
`End Date` | Optional.An end date for the search.If you don't set a value, the action uses current time.  
  
#### Action outputs

The **Initiate Deep Visibility Query** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Initiate Deep Visibility Query** action:
    
    
    [
        {
            "query_id": "QUERY_ID"
        }
    ]
    

##### Output messages

The **Initiate Deep Visibility Query** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created a Deep Visibility query. Query ID: QUERY_ID.` `Failed to create a Deep Visibility query.` | The action succeeded.  
`Error executing action "Initiate Deep Visibility Query". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Initiate Deep Visibility Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Initiate Full Scan

Use the **Initiate Full Scan** action to initiate a full disk scan on an endpoint in SentinelOne.

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
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Initiate Full Scan** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully started the full disk scan on the following endpoints in SentinelOne: ENTITY_ID. ` `Action wasn't able to start a full disk scan on the following endpoints in SentinelOne: ENTITY_ID. ` `No full disk scans were initiated.` | The action succeeded.  
`Error executing action "Initiate Full Scan". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Initiate Full Scan** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Sites

Use the **List Sites** action to list available sites in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Sites** action requires the following parameters:

Parameter | Description  
---|---  
`Filter Key` |  Optional.The key to filter sites.The possible values are as follows:

  * `Select One`
  * `Name`
  * `ID`

The default value is `Select One`.  
`Filter Logic` | Optional.The filter logic to apply.The filter logic uses the value set in the `Filter Key` parameter.The possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

The default value is `Not Specified`.  
`Filter Value` | Optional.The value to use in the filter.The filter logic uses the value set in the `Filter Key` parameter.If you select `Equal` in the `Filter Logic` parameter, the action searches for the exact match among results.If you select `Contains` in the `Filter Logic` parameter, the action searches for results that contain the specified substring.If you don't set a value, the action ignores the filter.  
`Max Records To Return` | Optional.The number of records to return.The default value is `50`.  
  
#### Action outputs

The **List Sites** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Sites** action can return the following table:

Table name: **Available Sites**

Table columns:

  * **Name**
  * **ID**
  * **Creator**
  * **Expiration**
  * **Type**
  * **State**



##### Output messages

The **List Sites** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found sites for the provided criteria in SentinelOne.` `No sites were found for the provided criteria in SentinelOne.` `The filter was not applied, because parameter "Filter Value" has an empty value.` | The action succeeded.  
`Error executing action "List Sites". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Sites** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Mark as Threat

Use the **Mark as Threat** action to mark suspicious threats as true positive threats in SentinelOne.

To mark threats in SentinelOne, you need any of the following roles:

  * `Admin`
  * `IR Team`
  * `SOC`



You can mark as threats only suspicious detections.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Mark as Threat** action requires the following parameters:

Parameter | Description  
---|---  
`Threat IDs` | Required. A comma-separated list of detection IDs to mark as threats.  
  
#### Action outputs

The **Mark as Threat** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Mark as Threat** action:
    
    
    [
        {
            "ID": "DETECTION_ID",
            "marked_as_threat": "true"
        }
    ]
    

##### Output messages

The **Mark as Threat** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully marked the following threats in SentinelOne: THREAT_ID.` `Action wasn't able to mark the following threats in SentinelOne: THREAT_ID.` `No threats were marked.` | The action succeeded.  
`Error executing action "Mark as Threat". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Mark as Threat** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Mitigate Threat

Use the **Mitigate Threat** action to execute mitigation actions on the threats in SentinelOne.

To mitigate threats in SentinelOne, you need any of the following roles:

  * `Admin`
  * `IR Team`
  * `SOC`



The rollback applies only to Windows. The threat remediation applies only to macOS and Windows.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Mitigate Threat** action requires the following parameters:

Parameter | Description  
---|---  
`Mitigation action` | Required.A mitigation action for the detected threats. The possible values are as follows:

  * `quarantine`
  * `kill`
  * `un-quarantine`
  * `remediate`
  * `rollback-remediate`

The default value is `quarantine`.  
`Threat IDs` | Required.A comma-separated list of threat IDs to mitigate.  
  
#### Action outputs

The **Mitigate Threat** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Mitigate Threat** action:
    
    
    [
            {
                "mitigated": true,
                "mitigation_action": "quarantine",
                "Threat_ID": "THREAT_ID"
            }
    ]
    

##### Output messages

The **Mitigate Threat** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully mitigated the following threats in SentinelOne: THREAT_ID.` `Action wasn't able to mitigate the following threats in SentinelOne: THREAT_ID.` `No threats were mitigated.` | The action succeeded.  
`Error executing action "Mitigate Threat". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Mitigate Threat** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Move Agents

Use the **Move Agents** action to move agents to the provided group from the same site.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`



#### Action inputs

The **Move Agents** action requires the following parameters:

Parameter | Description  
---|---  
`Group ID` | Optional.The ID of the group to move agents.  
`Group Name` | Optional.The name of the group to move agents.If you configure both the `Group ID` parameter and the `Group Name` parameters, the action prioritizes the `Group ID` parameter.  
  
#### Action outputs

The **Move Agents** action provides the following outputs:

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

The **Move Agents** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully moved the following endpoints to the group with ID_OR_NAME GROUP_ID_OR_NAMEin SentinelOne: ENTITY_ID.` `Action wasn't able to move the following endpoints to the group with ID_OR_NAME GROUP_ID_OR_NAMEin SentinelOne: ENTITY_ID.` `No endpoints were moved to the group ID_OR_NAME GROUP_ID_OR_NAMEin SentinelOne.` | The action succeeded.  
`Error executing action "Move Agents". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Move Agents** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity.

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
Output messages | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Reconnect Agent to the Network

Use the **Reconnect Agent to the Network** action to reconnect a disconnected endpoint to a network.

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
Output messages | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Reconnect Agent to the Network** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Resolve Threat

Use the **Resolve Threat** action to resolve threats in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Resolve Threat** action requires the following parameters:

Parameter | Description  
---|---  
`Threat IDs` | Required.A comma-separated list of threat IDs to resolve.  
`Annotation` | Optional.A justification for resolving the threat.  
  
#### Action outputs

The **Resolve Threat** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Resolve Threat** action:
    
    
    [
        {
            "resolved": false,
            "Threat_ID": "THREAT_ID"
            }
    ]
    

##### Output messages

The **Resolve Threat** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully resolved the following threats in SentinelOne: THREAT_ID.` `Action wasn't able to resolve the following threats in SentinelOne: THREAT_ID.` `No threats were resolved.` | The action succeeded.  
`Error executing action "Resolve Threat". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Resolve Threat** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Alert

Use the **Update Alert** action to update the alert of the threat in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update Alert** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | Required.The ID of the alert to update.  
`Status` | Optional. The status for the alert. The possible values are as follows:

  * `Unresolved`
  * `In Progress`
  * `Resolved`

  
`Verdict` | Optional. The verdict for the alert. The possible values are as follows:

  * `True Positive`
  * `False Positive`
  * `Suspicious`

  
  
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

The following example shows the JSON result outputs received when using the **Update Alert** action:
    
    
    {
               "agentDetectionInfo": {
                   "accountId": "1727154225040260868",
                   "machineType": "server",
                   "name": "windows-server-20230913",
                   "osFamily": "windows",
                   "osName": "Windows Server 2019 Datacenter",
                   "osRevision": "17763",
                   "siteId": "1727154229628829519",
                   "uuid": "da943d26318e46a8b3f6fc480c02636d",
                   "version": "23.1.2.400"
               },
               "agentRealtimeInfo": {
                   "id": "1896661984701699721",
                   "infected": true,
                   "isActive": true,
                   "isDecommissioned": false,
                   "machineType": "server",
                   "name": "windows-server-20230913",
                   "os": "windows",
                   "uuid": "da943d26318e46a8b3f6fc480c02636d"
               },
               "alertInfo": {
                   "alertId": "1947486263439640318",
                   "analystVerdict": "Undefined",
                   "createdAt": "2024-05-11T00:27:23.135000Z",
                   "dnsRequest": null,
                   "dnsResponse": null,
                   "dstIp": null,
                   "dstPort": null,
                   "dvEventId": "01HXJGR13VFVQAHW6TPDZ78WSX_35",
                   "eventType": "REGVALUEMODIFIED",
                   "hitType": "Events",
                   "incidentStatus": "Unresolved",
                   "indicatorCategory": null,
                   "indicatorDescription": null,
                   "indicatorName": null,
                   "isEdr": true,
                   "loginAccountDomain": null,
                   "loginAccountSid": null,
                   "loginIsAdministratorEquivalent": null,
                   "loginIsSuccessful": null,
                   "loginType": null,
                   "loginsUserName": null,
                   "modulePath": null,
                   "moduleSha1": null,
                   "netEventDirection": null,
                   "registryKeyPath": "MACHINE\\SYSTEM\\ControlSet001\\Services\\CSAgent\\Sim\\NT",
                   "registryOldValue": "0060030100000000",
                   "registryOldValueType": "BINARY",
                   "registryPath": "MACHINE\\SYSTEM\\ControlSet001\\Services\\CSAgent\\Sim\\NT",
                   "registryValue": "0070030100000000",
                   "reportedAt": "2024-05-11T00:27:33.873767Z",
                   "source": "STAR",
                   "srcIp": null,
                   "srcMachineIp": null,
                   "srcPort": null,
                   "tiIndicatorComparisonMethod": null,
                   "tiIndicatorSource": null,
                   "tiIndicatorType": null,
                   "tiIndicatorValue": null,
                   "updatedAt": "2025-05-12T18:41:08.366615Z"
               },
               "containerInfo": {
                   "id": null,
                   "image": null,
                   "labels": null,
                   "name": null
               },
               "kubernetesInfo": {
                   "cluster": null,
                   "controllerKind": null,
                   "controllerLabels": null,
                   "controllerName": null,
                   "namespace": null,
                   "namespaceLabels": null,
                   "node": null,
                   "pod": null,
                   "podLabels": null
               },
               "ruleInfo": {
                   "description": null,
                   "id": "1763599692710649014",
                   "name": "Registry Value Modified",
                   "queryLang": "1.0",
                   "queryType": "events",
                   "s1ql": "EventType = \"Registry Value Modified\"",
                   "scopeLevel": "account",
                   "severity": "Critical",
                   "treatAsThreat": "UNDEFINED"
               },
               "sourceParentProcessInfo": {
                   "commandline": "C:\\Windows\\system32\\services.exe",
                   "effectiveUser": null,
                   "fileHashMd5": "0d464c4bf9d85412d6ef15eea3a91e72",
                   "fileHashSha1": "582a7cbf0bf13889080900cd7bea368bf77f8faf",
                   "fileHashSha256": "243e370c279b3b8062e5dd81d8df539705397cc68472168251ed54134b13d70b",
                   "filePath": "C:\\Windows\\System32\\services.exe",
                   "fileSignerIdentity": "MICROSOFT WINDOWS PUBLISHER",
                   "integrityLevel": "system",
                   "loginUser": null,
                   "name": "services.exe",
                   "pid": "896",
                   "pidStarttime": "2024-04-26T17:33:41.962000Z",
                   "realUser": null,
                   "storyline": "DD880F57CA4DC0BB",
                   "subsystem": "sys_win32",
                   "uniqueId": "DC880F57CA4DC0BB",
                   "user": "NT AUTHORITY\\SYSTEM"
               },
               "sourceProcessInfo": {
                   "commandline": "\"C:\\Program Files\\Palo Alto Networks\\Traps\\cyserver.exe\"",
                   "effectiveUser": null,
                   "fileHashMd5": "1d6ec27dc8bbf1509a4ebf81b9ea6c26",
                   "fileHashSha1": "dca4478ce7db9f98b930b12096205be8a587620e",
                   "fileHashSha256": "c043dfeafb79b60018f3098f5908eb57b2fe84dbdfde0c83e613b4b42d7255c6",
                   "filePath": "C:\\Program Files\\Palo Alto Networks\\Traps\\cyserver.exe",
                   "fileSignerIdentity": "PALO ALTO NETWORKS (NETHERLANDS) B.V.",
                   "integrityLevel": "system",
                   "loginUser": null,
                   "name": "cyserver.exe",
                   "pid": "3204",
                   "pidStarttime": "2024-04-26T17:34:17.273000Z",
                   "realUser": null,
                   "storyline": "74890F57CA4DC0BB",
                   "subsystem": "sys_win32",
                   "uniqueId": "73890F57CA4DC0BB",
                   "user": "NT AUTHORITY\\SYSTEM"
               },
               "targetProcessInfo": {
                   "tgtFileCreatedAt": "1970-01-01T00:00:00Z",
                   "tgtFileHashSha1": null,
                   "tgtFileHashSha256": null,
                   "tgtFileId": null,
                   "tgtFileIsSigned": "signed",
                   "tgtFileModifiedAt": "1970-01-01T00:00:00Z",
                   "tgtFileOldPath": null,
                   "tgtFilePath": null,
                   "tgtProcCmdLine": null,
                   "tgtProcImagePath": null,
                   "tgtProcIntegrityLevel": "unknown",
                   "tgtProcName": null,
                   "tgtProcPid": null,
                   "tgtProcSignedStatus": null,
                   "tgtProcStorylineId": null,
                   "tgtProcUid": null,
                   "tgtProcessStartTime": "1970-01-01T00:00:00Z"
               }
           }
    

##### Output messages

The **Update Alert** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated alert with ID ALERT_ID in SentinelOne.` | The action succeeded.  
`Error executing action "Update Alert". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Alert** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Analyst Verdict

Use the **Update Analyst Verdict** action to update the analyst verdict of the threat in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update Analyst Verdict** action requires the following parameters:

Parameter | Description  
---|---  
`Threat ID` | Required.A comma-separated list of threat IDs to update the analyst verdict.  
`Analyst Verdict` | Required.An analyst verdict.The possible values are as follows:

  * `True Positive`
  * `False Positive`
  * `Suspicious`
  * `Undefined`

The default value is `Undefined`.  
  
#### Action outputs

The **Update Analyst Verdict** action provides the following outputs:

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

The **Update Analyst Verdict** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated analyst verdict for the following threats in SentinelOne: THREAT_ID.` `Action wasn't able to update analyst verdict for the following threats in SentinelOne: THREAT_ID. ` `Action wasn't able to update analyst verdict for the provided threats in SentinelOne.` | The action succeeded.  
`Error executing action "Update Analyst Verdict". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Analyst Verdict** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Device Control Rule

Use the **Update Device Control Rule** action to update a device control rule in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update Device Control Rule** action requires the following parameters:

Parameter | Description  
---|---  
`Rule ID` | Required. The ID of the rule to update.  
`Rule JSON` | Required. The JSON object representing the device control rule configuration. The default value is as follows:
    
    
       {
            "ruleName": "String",
            "interface": "String",
            "ruleType": "String",
            "action": "String",
            "accessPermission": "String",
            "deviceClass": "String",
            "status": "String"
        }  
  
#### Action outputs

The **Update Device Control Rule** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Update Device Control Rule** action:
    
    
    {
        "data": {
            "accessPermission": "Read-Write",
            "action": "Allow",
            "bluetoothAddress": null,
            "createdAt": "2024-01-01T00:00:00.000000Z",
            "creator": "[USERNAME] ([EMAIL_ADDRESS])",
            "creatorId": "[CREATOR_ID]",
            "deviceClass": "FFh",
            "deviceClassName": "FF Vendor Specific",
            "deviceId": null,
            "deviceInformationServiceInfoKey": null,
            "deviceInformationServiceInfoValue": null,
            "deviceName": null,
            "editable": true,
            "gattService": null,
            "id": "[RULE_ID]",
            "interface": "USB",
            "manufacturerName": null,
            "minorClasses": null,
            "order": 1,
            "productId": null,
            "ruleName": "Test",
            "ruleType": "class",
            "scope": "account",
            "scopeId": "[SCOPE_ID]",
            "scopeName": "[SCOPE_NAME]",
            "status": "Disabled",
            "uid": null,
            "updatedAt": "2024-01-01T00:00:00.000000Z",
            "vendorId": null,
            "version": null
        }
    }
    

##### Output messages

The **Update Device Control Rule** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated a Device Control Rule with ID DEVICE_CONTROL_ID in SentinelOne.` | The action succeeded.  
`Error executing action "Update Device Control Rule". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Device Control Rule** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Update Incident Status

Use the **Update Incident Status** action to update threat incident status in SentinelOne.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Update Incident Status** action requires the following parameters:

Parameter | Description  
---|---  
`Threat ID` | Required.A comma-separated list of threat IDs to update the incident status.  
`Status` | Required.An incident status.The possible values are as follows:

  * `Unresolved`
  * `In Progress`
  * `Resolved`

The default value is `Resolved`.  
  
#### Action outputs

The **Update Incident Status** action provides the following outputs:

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

The **Update Incident Status** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated incident status for the following threats in SentinelOne: THREAT_ID.` `Action wasn't able to update incident status for the following threats in SentinelOne: THREAT_ID. ` `Action wasn't able to update incident status for the provided threats in SentinelOne.` | The action succeeded.  
`Error executing action "Update Incident Status". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Incident Status** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### SentinelOne - Alerts Connector

Use the **SentinelOne - Alerts Connector** to ingest alerts from SentinelOne.

The connector lets you filter alerts using a dynamic list based on the `ruleInfo.name` parameter. The behavior of this list depends on the `Use dynamic list as a blocklist` parameter.

  * If you don't select `Use dynamic list as a blocklist`:

The dynamic list functions as a whitelist. The connector only ingests alerts whose `ruleInfo.name` matches a value in the list. If the list is empty, no alerts are ingested.

  * If you select `Use dynamic list as a blocklist`:

The dynamic list functions as a blocklist. The connector ingests all alerts excluding those whose `ruleInfo.name` matches a value in the list. If the list is empty, all alerts are ingested.




##### Connector parameters

The **SentinelOne - Alerts Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype). The default value is `ruleInfo_name`.  
`Environment Field Name` | Optional.The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value. The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment. The default value is `.*`.  
`PythonProcessTimeout` | Required.The timeout limit, in seconds, for the Python process that runs the current script. The default value is `180`.  
`API Root` | Required. The API root of the SentinelOne instance.  
`API Token` | Required.The SentinelOne API token.  
`Status Filter` | Optional. A comma-separated list of alert statuses to ingest. The possible values are as follows:

  * `Unresolved`
  * `In Progress`
  * `Resolved`

If no value is provided, the connector fetches alerts with the `Unresolved` and `In Progress` statuses.  
`Case Name Template` | Optional. A template to define a custom case name. The connector adds a `custom_case_name` key to the event. You can use placeholders in the format FIELD_NAME, which are populated from the first event's string values. Example: `Phishing - EVENT_MAILBOX`.  
`Alert Name Template` | Optional. A template to define the alert name. You can use placeholders in the format FIELD_NAME, which are populated from the first event's string values. Example: `Phishing - EVENT_MAILBOX`. If a value is not provided or the template is invalid, the connector uses a default alert name.  
`Lowest Severity To Fetch` | Optional. The lowest severity of the alerts to retrieve.If you don't configure this parameter, the connector ingests alerts with all severity levels. The possible values are as follows:

  * `Info`
  * `Low`
  * `Medium`
  * `High`
  * `Critical`

If no value is provided, all severities are ingested.  
`Max Hours Backwards` | Required. The number of hours before the current time to fetch alerts. The default value is `24`.  
`Max Alerts To Fetch` | Required. The maximum number of alerts to process in every connector iteration. The maximum value is `100`. The default value is `10`.  
`Use dynamic list as a blocklist` | Required. If selected, the connector uses the dynamic list as a blocklist. Not enabled by default.  
`Disable Overflow` | Optional. If selected, the connector ignores the Google SecOps overflow mechanism. Not enabled by default.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the SentinelOne server. Enabled by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

#### Alert structure

The following table describes the mapping of SentinelOne alert fields to Google SecOps alert fields:

Siemplify Alert Field | SentinelOne Alert Field (JSON key from API)  
---|---  
`SourceSystemName` | Filled by the framework.  
`TicketId` | `alertInfo.alertId`  
`DisplayId` | `SentinelOne_Alert_{alertInfo.alertId}`  
`Name` | `SentinelOne Alert: {ruleInfo.name}`  
`Reason` | `ruleInfo.s1q1`  
`Description` | `ruleInfo.description`  
`DeviceVendor` | Hardcoded: `SentinelOne`  
`DeviceProduct` | Fallback value: `Alerts`  
`Priority` | Mapped from `ruleInfo.severity`  
`RuleGenerator` | `SentinelOne Alert: {ruleInfo.name}`  
`SourceGroupingIdentifier` | `ruleInfo.name`  
`Severity` | Mapped from `ruleInfo.severity`  
`Risk Score` | Integer representation of severity  
`StartTime` | Converted from `alertInfo.createdAt`  
`EndTime` | Converted from `alertInfo.createdAt`  
`Siemplify Alert - Extensions` | N/A  
`Siemplify Alert - Attachments` | N/A  
  
#### Connector Events

The example of a connector event is as follows:
    
    
    {
        "agentDetectionInfo": {
            "accountId": "1727154225040260868",
            "machineType": "server",
            "name": "windows-server-20230913",
            "osFamily": "windows",
            "osName": "Windows Server 2019 Datacenter",
            "osRevision": "17763",
            "siteId": "1727154229628829519",
            "uuid": "da943d26318e46a8b3f6fc480c02636d",
            "version": "23.1.2.400"
        },
        "agentRealtimeInfo": {
            "id": "1896661984701699721",
            "infected": true,
            "isActive": true,
            "isDecommissioned": false,
            "machineType": "server",
            "name": "windows-server-20230913",
            "os": "windows",
            "uuid": "da943d26318e46a8b3f6fc480c02636d"
        },
        "alertInfo": {
            "alertId": "1947486263439640318",
            "analystVerdict": "Undefined",
            "createdAt": "2024-05-11T00:27:23.135000Z",
            "dnsRequest": null,
            "dnsResponse": null,
            "dstIp": null,
            "dstPort": null,
            "dvEventId": "01HXJGR13VFVQAHW6TPDZ78WSX_35",
            "eventType": "REGVALUEMODIFIED",
            "hitType": "Events",
            "incidentStatus": "Unresolved",
            "indicatorCategory": null,
            "indicatorDescription": null,
            "indicatorName": null,
            "isEdr": true,
            "loginAccountDomain": null,
            "loginAccountSid": null,
            "loginIsAdministratorEquivalent": null,
            "loginIsSuccessful": null,
            "loginType": null,
            "loginsUserName": null,
            "modulePath": null,
            "moduleSha1": null,
            "netEventDirection": null,
            "registryKeyPath": "MACHINE\\SYSTEM\\ControlSet001\\Services\\CSAgent\\Sim\\NT",
            "registryOldValue": "0060030100000000",
            "registryOldValueType": "BINARY",
            "registryPath": "MACHINE\\SYSTEM\\ControlSet001\\Services\\CSAgent\\Sim\\NT",
            "registryValue": "0070030100000000",
            "reportedAt": "2024-05-11T00:27:33.873767Z",
            "source": "STAR",
            "srcIp": null,
            "srcMachineIp": null,
            "srcPort": null,
            "tiIndicatorComparisonMethod": null,
            "tiIndicatorSource": null,
            "tiIndicatorType": null,
            "tiIndicatorValue": null,
            "updatedAt": "2025-05-12T18:41:08.366615Z"
        },
        "containerInfo": {
            "id": null,
            "image": null,
            "labels": null,
            "name": null
        },
        "kubernetesInfo": {
            "cluster": null,
            "controllerKind": null,
            "controllerLabels": null,
            "controllerName": null,
            "namespace": null,
            "namespaceLabels": null,
            "node": null,
            "pod": null,
            "podLabels": null
        },
        "ruleInfo": {
            "description": null,
            "id": "1763599692710649014",
            "name": "Registry Value Modified",
            "queryLang": "1.0",
            "queryType": "events",
            "s1ql": "EventType = \"Registry Value Modified\"",
            "scopeLevel": "account",
            "severity": "Critical",
            "treatAsThreat": "UNDEFINED"
        },
        "sourceParentProcessInfo": {
            "commandline": "C:\\Windows\\system32\\services.exe",
            "effectiveUser": null,
            "fileHashMd5": "0d464c4bf9d85412d6ef15eea3a91e72",
            "fileHashSha1": "582a7cbf0bf13889080900cd7bea368bf77f8faf",
            "fileHashSha256": "243e370c279b3b8062e5dd81d8df539705397cc68472168251ed54134b13d70b",
            "filePath": "C:\\Windows\\System32\\services.exe",
            "fileSignerIdentity": "MICROSOFT WINDOWS PUBLISHER",
            "integrityLevel": "system",
            "loginUser": null,
            "name": "services.exe",
            "pid": "896",
            "pidStarttime": "2024-04-26T17:33:41.962000Z",
            "realUser": null,
            "storyline": "DD880F57CA4DC0BB",
            "subsystem": "sys_win32",
            "uniqueId": "DC880F57CA4DC0BB",
            "user": "NT AUTHORITY\\SYSTEM"
        },
        "sourceProcessInfo": {
            "commandline": "\"C:\\Program Files\\Palo Alto Networks\\Traps\\cyserver.exe\"",
            "effectiveUser": null,
            "fileHashMd5": "1d6ec27dc8bbf1509a4ebf81b9ea6c26",
            "fileHashSha1": "dca4478ce7db9f98b930b12096205be8a587620e",
            "fileHashSha256": "c043dfeafb79b60018f3098f5908eb57b2fe84dbdfde0c83e613b4b42d7255c6",
            "filePath": "C:\\Program Files\\Palo Alto Networks\\Traps\\cyserver.exe",
            "fileSignerIdentity": "PALO ALTO NETWORKS (NETHERLANDS) B.V.",
            "integrityLevel": "system",
            "loginUser": null,
            "name": "cyserver.exe",
            "pid": "3204",
            "pidStarttime": "2024-04-26T17:34:17.273000Z",
            "realUser": null,
            "storyline": "74890F57CA4DC0BB",
            "subsystem": "sys_win32",
            "uniqueId": "73890F57CA4DC0BB",
            "user": "NT AUTHORITY\\SYSTEM"
        },
        "targetProcessInfo": {
            "tgtFileCreatedAt": "1970-01-01T00:00:00Z",
            "tgtFileHashSha1": null,
            "tgtFileHashSha256": null,
            "tgtFileId": null,
            "tgtFileIsSigned": "signed",
            "tgtFileModifiedAt": "1970-01-01T00:00:00Z",
            "tgtFileOldPath": null,
            "tgtFilePath": null,
            "tgtProcCmdLine": null,
            "tgtProcImagePath": null,
            "tgtProcIntegrityLevel": "unknown",
            "tgtProcName": null,
            "tgtProcPid": null,
            "tgtProcSignedStatus": null,
            "tgtProcStorylineId": null,
            "tgtProcUid": null,
            "tgtProcessStartTime": "1970-01-01T00:00:00Z"
        }
    }
    

### SentinelOne - Threats Connector

Use the **SentinelOne - Threats Connector** to ingest threats from SentinelOne.

The connector lets you filter alerts based on dynamic lists.

The **SentinelOne - Threats Connector** filters alerts using the `alert_name` parameter.

If you select the `Use whitelist as a blacklist` parameter, the connector only ingests alerts whose `alert_name` doesn't match any value in the dynamic list.

If you don't configure `alert_name` values in the dynamic list, the connector ingests all alerts.

If you don't select the `Use whitelist as a blacklist` parameter, the connector only ingests alerts whose `alert_name` matches a value in the dynamic list.

##### Connector inputs

The **SentinelOne - Threats Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required.The name of the field where the product name is stored.The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value `siemplify_event` resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default.The default value is `siemplify_event`.  
`Event Field Name` | Required.The name of the field that determines the event name (subtype). The default value is `threatinfo_classification`.  
`Environment Field Name` | Optional.The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.The default value is `""`.  
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout` | Required.The timeout limit, in seconds, for the Python process that runs the current script.The default value is `180`.  
`API Root` | Required.The SentinelOne API root.The default value is `https://usea1-partners.sentinelone.net/`.  
`API Token` | Required.The SentinelOne API token.  
`API Version` | Optional. The version of the SentinelOne API for the connector to use. **Important:** Version `2.1` or higher is required to ingest private and internal IP addresses (`agentDetectionInfo_agentIpV4`). Version `2.0` only retrieves public IP addresses. The default value is `2.0`.  
`Fetch Max Days Backwards` | Optional.The number of days prior to now to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The default value is `1`.  
`Max Alerts Per Cycle` | Optional.The maximum number of alerts to process in every connector iteration.The default value is `25`.  
`Disable Overflow` | Optional.If selected, the connector ignores the Google SecOps overflow mechanism.Not selected by default.  
`Use whitelist as a blacklist` | Required.If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | Required.If selected, the integration validates the SSL certificate when connecting to the SentinelOne server.Selected by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
`Event Object Type Filter` | Optional.A comma-separated list of event objects to return with the threat information.The connector uses this parameter as a filter to only return certain objects, such as `process, ip, indicators`.If you don't set a value, the connector ingests all event object types.  
`Event Type Filter` | Optional.A comma-separated list of event types to return with the threat information.The connector uses this parameter as a filter to only return certain event types, such as `Process Creation, Behavioral Indicators`.  
`Max Events To Return` | Optional.The number of events to return for every threat. The maximum value is `199`.The default value is `199`.  
  
#### Connector rules

The connector supports proxies.

The connector supports allowlist and blocklist.

#### Connector events

The example of the connector event is as follows:
    
    
    {
        "data": [
            {
                "accountId": "ACCOUNT_ID",
                "accountName": "SentinelOne",
                "agentComputerName": "desktop-example",
                "agentDomain": "WORKGROUP",
                "agentId": "AGENT_ID",
                "agentInfected": false,
                "agentIp": "203.0.113.180",
                "agentIsActive": false,
                "agentIsDecommissioned": true,
                "agentMachineType": "desktop",
                "agentNetworkStatus": "connecting",
                "agentOsType": "windows",
                "agentVersion": "3.6.6.104",
                "annotation": null,
                "annotationUrl": null,
                "automaticallyResolved": false,
                "browserType": null,
                "certId": "",
                "classification": "generic.heuristic",
                "classificationSource": "Cloud",
                "classifierName": "MANUAL",
                "cloudVerdict": "provider_unknown",
                "collectionId": "COLLECTION_ID",
                "commandId": "835975626369402963",
                "createdAt": "2020-03-02T21:30:13.014874Z",
                "createdDate": "2020-03-02T21:30:12.748000Z",
                "description": "malware detected - not mitigated yet",
                "engines": [
                    "manual"
                ],
                "fileContentHash": "fc5a9b5e806f35a7b285e012ef8df3f06f399492",
                "fileCreatedDate": null,
                "fileDisplayName": "example.exe",
                "fileExtensionType": "Executable",
                "fileIsDotNet": null,
                "fileIsExecutable": true,
                "fileIsSystem": false,
                "fileMaliciousContent": null,
                "fileObjectId": "99FF941D82E382D1",
                "filePath": "\\Device\\HarddiskVolume3\\Program Files\\example.exe",
                "fileSha256": null,
                "fileVerificationType": "NotSigned",
                "fromCloud": false,
                "fromScan": false,
                "id": "ID",
                "indicators": [],
                "initiatedBy": "dvCommand",
                "initiatedByDescription": "Deep Visibility Command",
                "initiatingUserId": "INITIATING_USER_ID",
                "isCertValid": false,
                "isInteractiveSession": false,
                "isPartialStory": false,
                "maliciousGroupId": "MALICED_GROUP_ID",
                "maliciousProcessArguments": "-ServerName:App.Example.mca",
                "markedAsBenign": false,
                "mitigationMode": "protect",
                "mitigationReport": {
                    "kill": {
                        "status": "success"
                    },
                    "network_quarantine": {
                        "status": null
                    },
                    "quarantine": {
                        "status": "success"
                    },
                    "remediate": {
                        "status": null
                    },
                    "rollback": {
                        "status": null
                    },
                    "unquarantine": {
                        "status": null
                    }
                },
                "mitigationStatus": "mitigated",
                "publisher": "",
                "rank": 2,
                "resolved": true,
                "siteId": "SITE_ID",
                "siteName": "Example.com",
                "threatAgentVersion": "3.6.6.104",
                "threatName": "example.exe",
                "updatedAt": "2020-04-02T14:51:21.901754Z",
                "username": "DESKTOP-example\\username",
                "whiteningOptions": [
                    "hash"
                ]
            }
        ],
        "pagination": {
            "nextCursor": "VALUE",
            "totalItems": 161
        }
    }
    

## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### SentinelOneV2 - Sync Alerts

Use the **SentinelOneV2 - Sync Alerts** job to synchronize alert statuses and analyst verdicts bi-directionally between Google SecOps and SentinelOne.

#### Job requirements

To ensure the job identifies and synchronizes the correct data, the following conditions must be met:

  * The Google SecOps case must contain the `SentinelOne Alert` tag.

  * If the alert didn't originate from the **SentinelOne - Alerts Connector** , you must add an `Alert_ID` context value to the alert for the job to identify the correct SentinelOne record.




#### Operational logic

The job performs synchronization in two stages. First from Google SecOps to SentinelOne, and then from SentinelOne to Google SecOps.

The following logic applies when closing cases in SentinelOne:

  * If the Google SecOps closure **Reason** is `Malicious`, the SentinelOne **Verdict** is set to `True Positive`.

  * If the Google SecOps closure **Reason** is `Not Malicious`, the SentinelOne **Verdict** is set to `False Positive`.

  * For all other closure reasons, the alert is marked as `Resolved` in SentinelOne without a verdict being set.

  * If a SentinelOne alert is marked as `undefined`, the corresponding Google SecOps case is closed with the reason `Inconclusive`.




#### Job parameters

The **SentinelOne V2 - Sync Alerts** job requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Optional. The name of the environment from which to synchronize alerts. The default value is `Default Environment`.  
`API Root` | Required. The API root of the SentinelOne instance.  
`API Token` | Required. The API token used for authentication with SentinelOne.  
`Max Hours Backwards` | Required. The number of hours prior to the current time to synchronize alerts during the first job iteration. The default value is `24`.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the SentinelOne server. Enabled by default.  
  
### SentinelOneV2 - Sync Threats

Use the **SentinelOneV2 - Sync Threats** job to synchronize comments and statuses bi-directionally between Google SecOps alerts and SentinelOne threats.

#### Job requirements

To ensure the job identifies and synchronizes the correct data, the following conditions must be met:

  * The Google SecOps case must contain the `SentinelOne Threat` tag.

  * If the alert didn't originate from the **SentinelOne - Threats Connector** , you must add a `Threat_ID` context value to the alert for the job to identify the correct SentinelOne record.




#### Operational logic

The job synchronizes data in two stages. The first stage synchronizes SentinelOne threat data to Google SecOps alerts. The second stage synchronizes Google SecOps alert data to SentinelOne threats.

The job uses `Max Hours Backwards` for the initial iteration. For all subsequent requests, the job uses the `start_time` of the last processed alert.

##### Comment synchronization logic

The job uses the `last_update_time` to filter comments and prevent duplicate entries. Synchronized comments use the following structures:

  * **Sent from SentinelOne** : `SentinelOne {threat_id}: {comment}`
  * **Sent from Google SecOps** : `Google SecOps {case_id}: {comment}`



##### Status and verdict mapping

When an alert is closed in Google SecOps, the job updates the SentinelOne threat based on the following mapping:

  * If the closure **Reason** is `Malicious`, the SentinelOne status is set to `Resolved` and the **Verdict** is set to `True Positive`.

  * If the closure **Reason** is `Not Malicious`, the SentinelOne status is set to `Resolved` and the **Verdict** is set to `False Positive`.

  * For all other closure reasons, the SentinelOne status is set to `Resolved` without a verdict.




#### Job parameters

The **SentinelOneV2 - Sync Threats** job requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. The name of the environment where the job searches for threats. The default value is `Default Environment`.  
`API Root` | Required. The API root of the SentinelOne instance.  
`API Token` | Required. The API token used for authentication with SentinelOne.  
`Max Hours Backwards` | Required. The number of hours prior to the current time to synchronize threats during the first job iteration. The default value is `24`.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the SentinelOne server. Enabled by default.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
