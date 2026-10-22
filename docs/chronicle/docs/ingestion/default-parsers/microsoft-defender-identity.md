---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-identity/
title: Collect Microsoft Defender for Identity logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:05.938207+00:00
---

# Collect Microsoft Defender for Identity logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Defender for Identity logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest the Microsoft Defender for Identity logs to Google Security Operations using Azure Storage. The parser processes JSON logs, or CEF formatted logs if the JSON parsing fails. It extracts fields, performs data transformations such as string conversions, renaming, and merging, and maps them to the Unified Data Model (UDM), handling various log formats and enriching the data with additional context like labels and authentication details.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * active Azure tenant
  * Privileged access to Azure and Administrative Security role



## Configure Azure Storage account

  1. In the Azure console, search for **Storage accounts**.
  2. Click **Create**.
  3. Specify values for the following input parameters: 
     * **Subscription** : select the subscription.
     * **Resource Group** : select the resource group.
     * **Region** : select the region.
     * **Performance** : select the type of performance (**Standard** recommended).
     * **Redundancy** : select the type of redundancy (**GRS** or **LRS** recommended).
     * **Storage account name** : enter a name for the new Storage account.
  4. Click **Review + create**.
  5. Review the overview of the account and click **Create**.
  6. From the storage account **Overview** page, select submenu **Access keys** in **Security + networking**.
  7. Click **Show** next to **key1** or **key2**.
  8. Click **Copy to clipboard** to copy the key.
  9. Save the key in a secure location for future reference.

**Caution:** To avoid **HTTP 429 (Too Many Requests)** errors and ingestion delays, don't reuse the same shared key or storage account across multiple feeds.
  10. From the storage account **Overview** page, select submenu **Endpoints** in **Settings**.

  11. Click **Copy to clipboard** to copy the **Blob service** endpoint URL. (for example, `https://<storageaccountname>.blob.core.windows.net`).

  12. Save the endpoint URL in a secure location for future reference.

  13. Go to **Overview > JSON View**.

  14. Copy and save the Storage **Resource ID**.




## Configure Log Export for Microsoft Defender for Identity

  1. Sign in to the **Defender Portal** using a privileged account.
  2. Go to **Settings**.
  3. Select the **Microsoft Defender XDR** tab.
  4. Select **Streaming API** from the general section and click **Add**.
  5. Select **Forward events to Azure Storage**.
  6. Provide the following configuration details: 
     * **Name** : Enter a unique and meaningful name.
     * Select **Forward events to Azure Storage**.
     * **Storage Account Resource ID** : Enter the Azure Storage resource ID copied earlier.
     * **Event Types** : Select both **Alerts & Behaviors** and **Devices**.
  7. Click **Submit**.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Microsoft Defender for Identity feed

  1. Click the **Microsoft Defender** pack.
  2. Specify the following values:

     * **Source Type** : Microsoft Azure Blob Storage V2.
     * **Azure uri** : the blob endpoint URL.

`ENDPOINT_URL/BLOB_NAME`

Replace the following:

       * `ENDPOINT_URL`: the blob endpoint URL. (`https://<storageaccountname>.blob.core.windows.net`)
       * `BLOB_NAME`: the name of the blob. (such as, `insights-logs-<logname>`)
     * **Source deletion options** : select deletion option according to your preference.

**Note:** If you select the **Delete transferred files** or **Delete transferred files and empty directories** option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Shared key** : the access key to the Azure Blob Storage.

**Caution:** To avoid **HTTP 429 (Too Many Requests)** errors and ingestion delays, don't reuse the same shared key or storage account across multiple feeds.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  3. Click **Create feed.**

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds). 




### Supported Microsoft Defender For Identity sample logs

  * **JSON - Advanced Hunting**
        
        {
         "time": "2025-02-05T02:01:49.9837340Z",
         "tenantId": "00000000-0000-0000-0000-000000000000",
         "operationName": "Publish",
         "category": "AdvancedHunting-IdentityDirectoryEvents",
         "_TimeReceivedBySvc": "2025-02-05T02:00:23.0990817Z",
         "properties": {
          "ActionType": "SMB file copy",
          "Protocol": "Smb",
          "AccountName": null,
          "AccountDomain": null,
          "AccountUpn": null,
          "AccountSid": null,
          "AccountObjectId": null,
          "AccountDisplayName": null,
          "DeviceName": "HOST-SOURCE",
          "IPAddress": "10.10.10.5",
          "DestinationDeviceName": "HOST-DEST",
          "TargetDeviceName": null,
          "Location": null,
          "ISP": "INTERNAL_NETWORK",
          "Port": 445,
          "DestinationPort": 64589,
          "DestinationIPAddress": "10.10.10.5",
          "TargetAccountUpn": null,
          "TargetAccountDisplayName": null,
          "AdditionalFields": {
           "ActionTypeInner": "smbfilecopy",
           "Count": "4",
           "Category": "Lateral Movement",
           "AttackTechniques": "Remote Services (T1021), Lateral Tool Transfer (T1570), SMB/Windows Admin Shares (T1021.002)",
           "FilePath": "dns\\dns.log",
           "FileName": "dns\\dns.log",
           "FileSize": "138373233",
           "Method": "Read",
           "SourceComputerObjectGuid": "11111111-1111-1111-1111-111111111111",
           "SourceComputerOperatingSystem": "windows server 2016 standard",
           "SourceComputerOperatingSystemVersion": "10.0 (14393)",
           "SourceComputerOperatingSystemType": "windows",
           "DestinationComputerObjectGuid": "22222222-2222-2222-2222-222222222222",
           "DestinationComputerOperatingSystem": "windows server 2016 standard",
           "DestinationComputerOperatingSystemVersion": "10.0 (14393)",
           "DestinationComputerOperatingSystemType": "windows",
           "SourceComputerId": "33333333-3333-3333-3333-333333333333",
           "SourceComputerSid": "S-1-5-21-REDACTED-SID",
           "FROM.DEVICE": "HOST-SOURCE",
           "TO.DEVICE": "HOST-DEST",
           "ACTOR.DEVICE": "HOST-SOURCE"
          },
          "ReportId": "44444444-4444-4444-4444-444444444444",
          "Timestamp": "2025-02-05T02:00:01.335347Z",
          "Application": "Active Directory"
         },
         "Tenant": "DefaultTenant"
        }
        

  * **SYSLOG + CEF**
        
        <36>1 2022-06-29T01:55:03.819108+00:00 SYSLOG_HOST CEF 5556 RemoteExecutionSecurityAlert 0|
        Microsoft|
        Azure ATP|
        2.183.15420.19379|
        RemoteExecutionSecurityAlert|
        Remote code execution attempt|
        5|
        start=2022-06-29T01:50:43.1995560Z|
        app=Wmi, WinRm|
        shost=SRC_HOST|
        shostfqdn=src_host.domain.lan|
        msg=Service Account, SVC_ACCOUNT made 5 attempts to run commands remotely on 38 domain controllers from SRC_HOST using 1 WMI method,4 PowerShell commands.|
        externalId=2019|
        cs1Label=url|
        cs1=https://security.microsoft.com/alerts/sanitized_alert_id|
        cs2Label=trigger|
        cs2=update|
        cs3Label=mSecUrl|
        cs3=https://security.microsoft.com/alerts/sanitized_alert_id
        

  * **JSON - Records Batch**
        
        {
          "records": [
            {
              "time": "2024-08-21T11:46:25.1024982Z",
              "tenantId": "00000000-0000-0000-0000-000000000000",
              "operationName": "Publish",
              "category": "AdvancedHunting-IdentityDirectoryEvents",
              "_TimeReceivedBySvc": "2024-08-21T11:44:07.0952670Z",
              "properties": {
                "ActionType": "Directory Services replication",
                "Protocol": "Drsr",
                "AccountName": null,
                "AccountDomain": null,
                "AccountUpn": null,
                "AccountSid": "S-1-5-21-REDACTED-SID",
                "AccountObjectId": null,
                "AccountDisplayName": null,
                "DeviceName": "HOST-DEVICE",
                "IPAddress": "10.10.10.20",
                "DestinationDeviceName": "HOST-DEST",
                "TargetDeviceName": null,
                "Location": null,
                "ISP": "INTERNAL_NETWORK",
                "Port": 64464,
                "DestinationPort": 1066,
                "DestinationIPAddress": "10.10.10.30",
                "TargetAccountUpn": null,
                "TargetAccountDisplayName": null,
                "AdditionalFields": {
                  "Count": "2",
                  "Category": "Credential Access",
                  "AttackTechniques": [
                    "OS Credential Dumping (T1003)",
                    "DC Sync (T1003.006)",
                    "NTDS (T1003.003)"
                  ],
                  "IsSuccess": "True",
                  "ARG.TASK": "Directory Services replication",
                  "SourceAccountId": "11111111-1111-1111-1111-111111111111",
                  "SourceAccountSid": "S-1-5-21-REDACTED-SID",
                  "SourceComputerObjectGuid": "22222222-2222-2222-2222-222222222222",
                  "SourceComputerOperatingSystem": "windows server 2022 standard",
                  "SourceComputerOperatingSystemVersion": "10.0 (20348)",
                  "SourceComputerOperatingSystemType": "windows",
                  "DestinationComputerObjectGuid": "33333333-3333-3333-3333-333333333333",
                  "DestinationComputerOperatingSystem": "windows server 2016 standard",
                  "DestinationComputerOperatingSystemVersion": "10.0 (14393)",
                  "DestinationComputerOperatingSystemType": "windows",
                  "SourceComputerId": "44444444-4444-4444-4444-444444444444",
                  "SourceComputerSid": "S-1-5-21-REDACTED-SID",
                  "ACTOR.ACCOUNT": "MSOL_REDACTED",
                  "ACTOR.ENTITY_USER": "",
                  "FROM.DEVICE": "HOST-SRC",
                  "TO.DEVICE": "HOST-DEST",
                  "ACTOR.DEVICE": "HOST-SRC"
                },
                "ReportId": "55555555-5555-5555-5555-555555555555",
                "Timestamp": "2024-08-21T11:41:12.700159Z",
                "Application": "Active Directory"
              },
              "Tenant": "DefaultTenant"
            }
          ]
        }
        

  * **JSON - Azure Monitor / Activity**
        
        {
          "RoleLocation": "West Europe",
          "Stamp": "FDWeb",
          "ReleaseVersion": "6.2025.3.31+fc19adc.release_2025w03",
          "time": "2025-02-20T23:47:55.8304991Z",
          "resourceId": "/SUBSCRIPTIONS/00000000-0000-0000-0000-000000000000/RESOURCEGROUPS/SANITIZED_RG/PROVIDERS/MICROSOFT.NETWORK/LOADBALANCERS/SANITIZED-LB",
          "operationName": "MICROSOFT.AUTHORIZATION/POLICIES/MODIFY/ACTION",
          "category": "Administrative",
          "resultType": "Success",
          "resultSignature": "Succeeded.",
          "durationMs": "0",
          "callerIpAddress": "10.10.10.40",
          "correlationId": "11111111-1111-1111-1111-111111111111",
          "identity": {
            "authorization": {
              "scope": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/sanitized_rg/providers/Microsoft.Network/loadBalancers/sanitized-lb",
              "action": "Microsoft.Network/loadBalancers/write",
              "evidence": {
                "role": "Contributor",
                "roleAssignmentScope": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/SANITIZED_RG",
                "roleAssignmentId": "22222222222222222222222222222222",
                "roleDefinitionId": "33333333333333333333333333333333",
                "principalId": "REDACTED_PRINCIPAL_ID",
                "principalType": "ServicePrincipal"
              }
            },
            "claims": {
              "aud": "https://management.core.windows.net/",
              "iss": "https://sts.windows.net/00000000-0000-0000-0000-000000000000/",
              "iat": "1740087743",
              "nbf": "1740087743",
              "exp": "1740174443",
              "aio": "REDACTED_AIO",
              "appid": "REDACTED_APPID",
              "appidacr": "2",
              "http://schemas.microsoft.com/identity/claims/identityprovider": "https://sts.windows.net/00000000-0000-0000-0000-000000000000/",
              "idtyp": "app",
              "http://schemas.microsoft.com/identity/claims/objectidentifier": "44444444-4444-4444-4444-444444444444",
              "rh": "REDACTED_RH",
              "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier": "55555555-5555-5555-5555-555555555555",
              "http://schemas.microsoft.com/identity/claims/tenantid": "00000000-0000-0000-0000-000000000000",
              "uti": "REDACTED_UTI",
              "ver": "1.0",
              "xms_idrel": "7 12",
              "xms_mirid": "/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/sanitized_rg/providers/Microsoft.ContainerService/managedClusters/sanitized_cluster",
              "xms_tcdt": "1461941593"
            }
          },
          "level": "Information",
          "properties": {
            "isComplianceCheck": "False",
            "resourceLocation": "westeurope",
            "ancestors": "DataPlatform,LandingZone,REDACTED_ANCESTOR,00000000-0000-0000-0000-000000000000",
            "policies": [
              {
                "policyDefinitionId": "/providers/Microsoft.Management/managementGroups/REDACTED/providers/Microsoft.Authorization/policyDefinitions/REDACTED_ID",
                "policySetDefinitionId": "/providers/Microsoft.Management/managementGroups/REDACTED/providers/Microsoft.Authorization/policySetDefinitions/REDACTED_ID",
                "policyDefinitionReferenceId": "Inherit A Tag From Resource Group And Overwrite Existing_1",
                "policySetDefinitionName": "REDACTED_ID",
                "policySetDefinitionDisplayName": "Inherit All Tags From Resource Group And Overwrite Existing",
                "policySetDefinitionVersion": "1.0.0",
                "policyDefinitionName": "REDACTED_ID",
                "policyDefinitionDisplayName": "Inherit A Tag From Resource Group And Overwrite Existing",
                "policyDefinitionVersion": "1.0.0",
                "policyDefinitionEffect": "modify",
                "policyAssignmentId": "/providers/Microsoft.Management/managementGroups/REDACTED/providers/Microsoft.Authorization/policyAssignments/REDACTED_ID",
                "policyAssignmentName": "REDACTED_ID",
                "policyAssignmentDisplayName": "Inherit All Tags From Resource Group And Overwrite Existing",
                "policyAssignmentScope": "/providers/Microsoft.Management/managementGroups/REDACTED",
                "policyExemptionIds": [],
                "policyEnrollmentIds": []
              }
            ],
            "tenantId": "00000000-0000-0000-0000-000000000000"
          }
        }
        




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`category` | `metadata.log_type` | The raw log `category` field is mapped to `metadata.log_type`.  
`properties.AccountDisplayName` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AccountName` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AccountUpn` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.ActionType` | `metadata.product_event_type` | The raw log `properties.ActionType` field is mapped to `metadata.product_event_type`.  
`properties.AdditionalFields.ACTOR.ACCOUNT` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.ACTOR.DEVICE` | `principal.asset.asset_id` | The parser extracts the value of `properties.AdditionalFields.ACTOR.DEVICE` and prepends `ASSET ID:`.  
`properties.AdditionalFields.ACTOR.ENTITY_USER` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.Count` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.DestinationComputerDnsName` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.DestinationComputerObjectGuid` | `target.asset.product_object_id` | The first element of the array `properties.AdditionalFields.DestinationComputerObjectGuid` is mapped to `target.asset.product_object_id`. Subsequent elements are mapped to `additional.fields` with keys like `DestinationComputerObjectGuid_1`, `DestinationComputerObjectGuid_2`, etc.  
`properties.AdditionalFields.DestinationComputerOperatingSystem` | `target.asset.platform_software.platform_version` | The first element of the array `properties.AdditionalFields.DestinationComputerOperatingSystem` is mapped to `target.asset.platform_software.platform_version`. Subsequent elements are mapped to `additional.fields` with keys like `DestinationComputerOperatingSystem_1`, `DestinationComputerOperatingSystem_2`, etc.  
`properties.AdditionalFields.DestinationComputerOperatingSystemType` | `target.asset.platform_software.platform` | If the value is `windows`, the UDM field is set to `WINDOWS`.  
`properties.AdditionalFields.DestinationComputerOperatingSystemVersion` | `target.platform_version` | The first element of the array `properties.AdditionalFields.DestinationComputerOperatingSystemVersion` is mapped to `target.platform_version`. Subsequent elements are mapped to `additional.fields` with keys like `DestinationComputerOperatingSystemVersion1`, `DestinationComputerOperatingSystemVersion2`, etc.  
`properties.AdditionalFields.FROM.DEVICE` | `principal.asset.asset_id` | The parser extracts the value of `properties.AdditionalFields.FROM.DEVICE` and prepends `ASSET ID:`.  
`properties.AdditionalFields.KerberosDelegationType` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.SourceAccountId` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.SourceAccountSid` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.SourceComputerObjectGuid` | `principal.asset.product_object_id` | The raw log `properties.AdditionalFields.SourceComputerObjectGuid` field is mapped to `principal.asset.product_object_id`.  
`properties.AdditionalFields.SourceComputerOperatingSystem` | `principal.asset.platform_software.platform_version` | The raw log `properties.AdditionalFields.SourceComputerOperatingSystem` field is mapped to `principal.asset.platform_software.platform_version`.  
`properties.AdditionalFields.SourceComputerOperatingSystemType` | `principal.asset.platform_software.platform_version` | If the value is `windows`, the UDM field is set to `WINDOWS`.  
`properties.AdditionalFields.SourceComputerOperatingSystemVersion` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.Spns` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.TARGET_OBJECT.ENTITY_USER` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.AdditionalFields.TARGET_OBJECT.USER` | `target.user.userid` | The first element of the array `properties.AdditionalFields.TARGET_OBJECT.USER` is mapped to `target.user.userid`. Subsequent elements are mapped to `additional.fields` with keys like `TARGET_OBJECT.USER_1`, `TARGET_OBJECT.USER_2`, etc.  
`properties.AdditionalFields.TO.DEVICE` | `target.asset.asset_id` | The first element of the array `properties.AdditionalFields.TO.DEVICE` is mapped to `target.asset.asset_id` with `ASSET ID:` prepended. Subsequent elements are mapped to `additional.fields` with keys like `TODEVICE1`, `TODEVICE2`, etc.  
`properties.AuthenticationDetails` | `extensions.auth.auth_details` | The parser removes curly braces, square brackets, and double quotes from the value and prepends `AuthenticationDetails:`.  
`properties.DeliveryAction` | `additional.fields` | Mapped with key `DeliveryAction`.  
`properties.DeliveryLocation` | `additional.fields` | Mapped with key `DeliveryLocation`.  
`properties.DestinationDeviceName` | `target.hostname`, `target.asset.hostname` | The raw log `properties.DestinationDeviceName` field is mapped to both `target.hostname` and `target.asset.hostname`.  
`properties.DestinationIPAddress` | `target.ip`, `target.asset.ip` | The raw log `properties.DestinationIPAddress` field is mapped to both `target.ip` and `target.asset.ip`.  
`properties.DestinationPort` | `target.port` | The raw log `properties.DestinationPort` field is mapped to `target.port`.  
`properties.DeviceName` | `principal.hostname`, `principal.asset.hostname` | The raw log `properties.DeviceName` field is mapped to both `principal.hostname` and `principal.asset.hostname`.  
`properties.EmailClusterId` | `additional.fields` | Mapped with key `EmailClusterId`.  
`properties.EmailDirection` | `network.direction` | If the value is `Inbound`, the UDM field is set to `INBOUND`. If the value is `Outbound`, the UDM field is set to `OUTBOUND`. Otherwise, it's set to `UNKNOWN_DIRECTION`.  
`properties.EmailLanguage` | `additional.fields` | Mapped with key `EmailLanguage`.  
`properties.InitiatingProcessAccountDomain` | `principal.administrative_domain` | The raw log `properties.InitiatingProcessAccountDomain` field is mapped to `principal.administrative_domain`.  
`properties.InitiatingProcessAccountSid` | `principal.user.windows_sid` | The raw log `properties.InitiatingProcessAccountSid` field is mapped to `principal.user.windows_sid`.  
`properties.InitiatingProcessCommandLine` | `principal.process.command_line` | The raw log `properties.InitiatingProcessCommandLine` field is mapped to `principal.process.command_line`.  
`properties.InitiatingProcessFileName` | `principal.process.file.full_path` | Used in combination with `properties.InitiatingProcessFolderPath` to construct the full path. If `properties.InitiatingProcessFolderPath` already contains the filename, it's used directly.  
`properties.InitiatingProcessFolderPath` | `principal.process.file.full_path` | Used in combination with `properties.InitiatingProcessFileName` to construct the full path.  
`properties.InitiatingProcessId` | `principal.process.pid` | The raw log `properties.InitiatingProcessId` field is mapped to `principal.process.pid`.  
`properties.InitiatingProcessIntegrityLevel` | `about.labels` | Mapped with key `InitiatingProcessIntegrityLevel`.  
`properties.InitiatingProcessMD5` | `principal.process.file.md5` | The raw log `properties.InitiatingProcessMD5` field is mapped to `principal.process.file.md5`.  
`properties.InitiatingProcessParentId` | `principal.process.parent_process.pid` | The raw log `properties.InitiatingProcessParentId` field is mapped to `principal.process.parent_process.pid`.  
`properties.InitiatingProcessParentFileName` | `principal.process.parent_process.file.full_path` | The raw log `properties.InitiatingProcessParentFileName` field is mapped to `principal.process.parent_process.file.full_path`.  
`properties.InitiatingProcessSHA1` | `principal.process.file.sha1` | The raw log `properties.InitiatingProcessSHA1` field is mapped to `principal.process.file.sha1`.  
`properties.InitiatingProcessSHA256` | `principal.process.file.sha256` | The raw log `properties.InitiatingProcessSHA256` field is mapped to `principal.process.file.sha256`.  
`properties.InitiatingProcessTokenElevation` | `about.labels` | Mapped with key `InitiatingProcessTokenElevation`.  
`properties.InternetMessageId` | `additional.fields` | The parser removes angle brackets and maps the value with key `InternetMessageId`.  
`properties.IPAddress` | `principal.ip`, `principal.asset.ip` | The raw log `properties.IPAddress` field is mapped to both `principal.ip` and `principal.asset.ip`.  
`properties.LogonType` | `extensions.auth.mechanism` | Used to derive the value for `extensions.auth.mechanism`.  
`properties.Port` | `principal.port` | The raw log `properties.Port` field is mapped to `principal.port`.  
`properties.PreviousRegistryKey` | `src.registry.registry_key` | The raw log `properties.PreviousRegistryKey` field is mapped to `src.registry.registry_key`.  
`properties.PreviousRegistryValueData` | `src.registry.registry_value_data` | The raw log `properties.PreviousRegistryValueData` field is mapped to `src.registry.registry_value_data`.  
`properties.PreviousRegistryValueName` | `src.registry.registry_value_name` | The raw log `properties.PreviousRegistryValueName` field is mapped to `src.registry.registry_value_name`.  
`properties.Query` | `principal.user.attribute.labels` | Mapped with key `LDAP Search Scope`.  
`properties.RecipientEmailAddress` | Not Mapped | This field is not mapped to the IDM object in the UDM.  
`properties.RegistryKey` | `target.registry.registry_key` | The raw log `properties.RegistryKey` field is mapped to `target.registry.registry_key`.  
`properties.RegistryValueData` | `target.registry.registry_value_data` | The raw log `properties.RegistryValueData` field is mapped to `target.registry.registry_value_data`.  
`properties.RegistryValueName` | `target.registry.registry_value_name` | The raw log `properties.RegistryValueName` field is mapped to `target.registry.registry_value_name`.  
`properties.ReportId` | `about.labels` | Mapped with key `ReportId`.  
`properties.SenderIPv4` | `principal.ip`, `principal.asset.ip` | The raw log `properties.SenderIPv4` field is mapped to both `principal.ip` and `principal.asset.ip`.  
`properties.SenderMailFromAddress` | `principal.user.attribute.labels` | Mapped with key `SenderMailFromAddress`.  
`properties.SenderMailFromDomain` | `principal.user.attribute.labels` | Mapped with key `SenderMailFromDomain`.  
`properties.SenderObjectId` | `principal.user.product_object_id` | The raw log `properties.SenderObjectId` field is mapped to `principal.user.product_object_id`.  
`properties.Timestamp` | `metadata.event_timestamp` | The raw log `properties.Timestamp` field is mapped to `metadata.event_timestamp`.  
`tenantId` | `observer.cloud.project.id` | The raw log `tenantId` field is mapped to `observer.cloud.project.id`.  
N/A | `extensions.auth.type` | The value `MACHINE` is assigned by the parser.  
N/A | `metadata.event_type` | Derived based on the `category` and `properties.ActionType` fields. Can be `USER_LOGIN`, `USER_RESOURCE_ACCESS`, `USER_CHANGE_PASSWORD`, `REGISTRY_MODIFICATION`, `REGISTRY_DELETION`, `REGISTRY_CREATION`, `GENERIC_EVENT`, or `STATUS_UPDATE`.  
N/A | `metadata.vendor_name` | The value `Microsoft` is assigned by the parser.  
N/A | `metadata.product_name` | The value `Microsoft Defender Identity` is assigned by the parser.  
`cs1` | `metadata.url_back_to_product` | The raw log `cs1` field is mapped to `metadata.url_back_to_product`.  
`externalId` | `metadata.product_log_id` | The raw log `externalId` field is mapped to `metadata.product_log_id`.  
`msg` | `metadata.description` | The raw log `msg` field is mapped to `metadata.description`.  
`rule_name` | `security_result.rule_name` | The raw log `rule_name` field is mapped to `security_result.rule_name`.  
`severity` | `security_result.severity` | The raw log `severity` field is mapped to `security_result.severity`.  
`shost` | `principal.hostname`, `principal.asset.hostname` | The raw log `shost` field is mapped to both `principal.hostname` and `principal.asset.hostname`.  
`src` | `principal.ip` | The raw log `src` field is mapped to `principal.ip`.  
`suser` | `principal.user.user_display_name` | The raw log `suser` field is mapped to `principal.user.user_display_name`.  
`time` | `metadata.event_timestamp` | The raw log `time` field is mapped to `metadata.event_timestamp`.  
`userid` | `principal.user.userid` | The raw log `userid` field is mapped to `principal.user.userid`.  
N/A | `security_result.action` | Derived based on the `properties.ActionType` field. Can be `ALLOW` or `BLOCK`.  
N/A | `security_result.summary` | Derived from either the `category` field or the `properties.ActionType` field.  
`record.properties.AdditionalFields.IsMfaPerformed` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record.properties.OSPlatform` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`record.properties.DeviceType` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`record.properties.TargetDeviceName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`record.properties.AdditionalFields.SourceComputerOperatingSystemType` | `event.idm.read_only_udm.src.platform_patch_level` | Mapped from changelog  
`record.properties.AdditionalFields.TargetComputerObjectGuid` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`record.properties.AdditionalFields.TargetComputerOperatingSystem` | `event.idm.read_only_udm.principal.platform_patch_level` | Mapped from changelog  
`record.properties.AdditionalFields.TargetComputerOperatingSystemVersion` | `event.idm.read_only_udm.target.platform_patch_level` | Mapped from changelog  
`record.properties.AdditionalFields.TargetComputerOperatingSystemType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`record.properties.UncommonForUser` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`record.properties.LastSeenForUser` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`properties.AccountUpn` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`record.category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`record.properties.FailureReason` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`device_event_class_id` | `security_result.rule_name` | Mapped from changelog  
`event_name` | `security_result.description` | Mapped from changelog  
`app" and "alert_id` | `additional.fields` | Mapped from changelog  
`properties.Location` | `principal.location.country_or_region` | Mapped from changelog  
`properties.AccountObjectId` | `principal.user.attribute.labels` | Mapped from changelog  
`properties.DeviceId` | `principal.asset_id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-identity-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
