---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint-ios/
title: Collect Microsoft Defender for Endpoint on iOS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:43:45.711190+00:00
---

# Collect Microsoft Defender for Endpoint on iOS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-endpoint-ios/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Defender for Endpoint on iOS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect Microsoft Defender for Endpoint on iOS logs by setting up a Google SecOps feed using Microsoft Azure Blob Storage V2.

Microsoft Defender for Endpoint on iOS is a mobile threat defense solution that protects iOS devices against phishing, unsafe network connections, and malicious apps. It provides web protection using a local VPN and integrates with Microsoft Intune for device management. Events from iOS devices are captured in the same Advanced Hunting tables as other Defender for Endpoint platforms, including DeviceEvents, DeviceInfo, DeviceLogonEvents, and DeviceNetworkEvents.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Microsoft Azure** portal with permissions to: 
    * Create Storage Accounts
    * Configure Diagnostic Settings (for Azure services)
    * Manage access keys
  * Access to **Microsoft Defender portal** with permissions to: 
    * Configure Data export settings
    * Manage Microsoft Defender XDR settings
  * iOS devices running iOS 16.0 or later
  * Devices enrolled via Intune Company Portal or registered via Microsoft Authenticator

**Note:** If you restrict access to your Azure resources using an Azure Storage firewall, you must add the IP ranges used by Storage Transfer Service (STS) workers to your list of allowed IPs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting).



## Configure Azure Storage Account

### Create Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `defenderioslogssa`)  
**Region** | Select the region (for example, `East US`)  
**Performance** | Standard (recommended)  
**Redundancy** | GRS (Geo-redundant storage) or LRS (Locally redundant storage)  
  4. Click **Review + create**.

  5. Review the overview of the account and click **Create**.

  6. Wait for the deployment to complete.




### Get Storage Account credentials

  1. Go to the **Storage Account** you just created.
  2. In the left navigation, select **Access keys** under **Security + networking**.
  3. Click **Show keys**.
  4. Copy and save the following for later use: 
     * **Storage account name** : The name you created (for example, `defenderioslogssa`)
     * **Key 1** or **Key 2** : The shared access key (a 512-bit random string in base-64 encoding)



### Get Blob Service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://defenderioslogssa.blob.core.windows.net/`



### Get Storage Account Resource ID

  1. In the same Storage Account, select **Properties** from the left navigation.
  2. Scroll down to find **Storage account resource ID**.
  3. Click the copy icon next to the Resource ID and save it for later use. 
     * Example: `/subscriptions/12345678-1234-1234-1234-123456789012/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/defenderioslogssa`



## Configure Microsoft Defender for Endpoint data export

  1. Sign in to the **Microsoft Defender portal** at `https://security.microsoft.com`.
  2. Go to **Settings > Microsoft Defender XDR > Data export settings**.
  3. Click **\+ Add data export settings**.
  4. In the **Name** field, enter a descriptive name (for example, `Export to Chronicle`).
  5. In the **Forward events to** section, select **Azure Storage**.
  6. In the **Storage account resource ID** field, paste the Storage Account Resource ID you copied earlier.
  7. In the **Choose events** section, select the event types to export. For comprehensive iOS device monitoring, select the following:

     * **DeviceEvents** : General device events including app launches and system events
     * **DeviceInfo** : Device inventory information including OS version and device properties
     * **DeviceLogonEvents** : Sign-in and authentication events
     * **DeviceNetworkEvents** : Network connections and web protection events
     * **DeviceProcessEvents** : Process creation and termination events
     * **DeviceFileEvents** : File creation, modification, and deletion events
     * **AlertInfo** : Alert metadata from Defender for Endpoint
     * **AlertEvidence** : Evidence associated with alerts
**Note:** You can select additional event types based on your monitoring requirements. For a complete list of available event types, see [Supported event types in Streaming API](https://learn.microsoft.com/en-us/defender-xdr/supported-event-types).
  8. Click **Save**.

After configuration, Microsoft Defender for Endpoint begins exporting events to your Azure Storage Account. Events are organized in blob containers with the following naming pattern:

     * `deviceevents`
     * `deviceinfo`
     * `devicelogonevents`
     * `devicenetworkevents`
     * `deviceprocessevents`
     * `devicefileevents`
     * `alertinfo`
     * `alertevidence`


  * Each container stores events in a hierarchical folder structure organized by date and time:
        
        container-name/
          └── year=YYYY/month=MM/day=DD/hour=HH/
              └── [event-files].json
        




## Configure a feed in Google SecOps to ingest Microsoft Defender for Endpoint on iOS logs

You need to create a separate feed for each event type container. Repeat the following steps for each container you want to ingest.

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Defender iOS - DeviceEvents`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft Defender for Endpoint on iOS** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
    
    https://defenderioslogssa.blob.core.windows.net/deviceevents/
    

Replace the following:

     * `defenderioslogssa`: Your Azure storage account name.
     * `deviceevents`: The blob container name for the event type.
**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:
     * **Never** : Never deletes any files after transfers.
     * **Delete transferred files** : Deletes files after successful transfer.
     * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Shared key** : Enter the shared key value (access key) you captured from the Storage Account
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed (for example, `defender_ios`)
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




Repeat the above steps for each event type container you want to ingest (for example, `deviceinfo`, `devicelogonevents`, `devicenetworkevents`, etc.). Use descriptive feed names to distinguish between event types.

## Configure Azure Storage firewall (if enabled)

If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.

  1. In the **Azure portal** , go to your **Storage Account**.
  2. Select **Networking** under **Security + networking**.
  3. Under **Firewalls and virtual networks** , select **Enabled from selected virtual networks and IP addresses**.
  4. In the **Firewall** section, under **Address range** , click **\+ Add IP range**.
  5. Add each Google SecOps IP range in CIDR notation.

To get the current IP ranges:

     * See [IP Allowlisting documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting)
     * Or retrieve them programmatically using the [Feed Management API](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api)
  6. Click **Save**.

**Note:** This feed source uses the Storage Transfer Service (STS) to transfer data from Azure storage to Google SecOps. Before using this feed source, you may need to add the IP ranges used by STS workers to your list of allowed IPs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
_TimeReceivedBySvc | additional.fields | Merged with labels created from each source field  
properties.InitiatingProcessUniqueId | additional.fields |   
properties.MachineGroup | additional.fields |   
properties.IsProcessRemoteSession | additional.fields |   
properties.IsInitiatingProcessRemoteSession | additional.fields |   
properties.InitiatingProcessSessionId | additional.fields |   
properties.InitiatingProcessParentCreationTime | additional.fields |   
properties.InitiatingProcessVersionInfoOriginalFileName | additional.fields |   
properties.InitiatingProcessVersionInfoFileDescription | additional.fields |   
properties.InitiatingProcessVersionInfoInternalFileName | additional.fields |   
properties.InitiatingProcessVersionInfoProductName | additional.fields |   
properties.AdditionalFields | additional.fields |   
properties.DeliveryAction | additional.fields |   
properties.DeliveryLocation | additional.fields |   
properties.EmailAction | additional.fields |   
properties.EmailActionPolicy | additional.fields |   
properties.EmailActionPolicyGuid | additional.fields |   
properties.AttachmentCount | additional.fields |   
properties.UrlCount | additional.fields |   
properties.EmailLanguage | additional.fields |   
properties.EmailClusterId | additional.fields |   
properties.Connectors | additional.fields |   
properties.OrgLevelAction | additional.fields |   
properties.OrgLevelPolicy | additional.fields |   
properties.UserLevelAction | additional.fields |   
properties.UserLevelPolicy | additional.fields |   
properties.ConfidenceLevel | additional.fields |   
SPF | additional.fields |   
DKIM | additional.fields |   
DMARC | additional.fields |   
CompAuth | additional.fields |   
properties.BulkComplaintLevel | additional.fields |   
has_email | metadata.event_type | Set to "EMAIL_TRANSACTION" if has_email true, else "NETWORK_CONNECTION" if has_principal and has_target true, else "STATUS_UPDATE" if has_principal true and has_target false, else "GENERIC_EVENT"  
has_principal | metadata.event_type |   
has_target | metadata.event_type |   
tenantId | metadata.product_deployment_id | Value copied directly  
operationName | metadata.product_event_type | Value copied directly  
properties.InitiatingProcessVersionInfoProductVersion | metadata.product_version | Value copied directly  
properties.EmailDirection | network.direction | Set to "INBOUND" if equals "Inbound"  
properties.SenderFromAddress | network.email.from | Value copied directly  
properties.InternetMessageId | network.email.mail_id | Value copied directly  
properties.Subject | network.email.subject | Merged from properties.Subject  
properties.RecipientEmailAddress | network.email.to | Merged from properties.RecipientEmailAddress  
properties.SenderFromDomain | principal.administrative_domain | Value from properties.SenderFromDomain if not empty, else properties.InitiatingProcessAccountDomain  
properties.InitiatingProcessAccountDomain | principal.administrative_domain |   
properties.DeviceId | principal.asset.asset_id | Concatenated as "DeviceId:%{properties.DeviceId}"  
properties.DeviceName | principal.asset.hostname | Value copied directly  
properties.SenderIPv4 | principal.asset.ip | Merged from properties.SenderIPv4 and properties.SenderIPv6  
properties.SenderIPv6 | principal.asset.ip |   
properties.DeviceName | principal.hostname | Value copied directly  
properties.SenderIPv4 | principal.ip | Merged from properties.SenderIPv4 and properties.SenderIPv6  
properties.SenderIPv6 | principal.ip |   
properties.InitiatingProcessCommandLine | principal.process.command_line | Value copied directly  
properties.InitiatingProcessFolderPath | principal.process.file.full_path | Value copied directly  
properties.InitiatingProcessMD5 | principal.process.file.md5 | Value copied directly  
properties.InitiatingProcessFileName | principal.process.file.names | Merged from properties.InitiatingProcessFileName  
properties.InitiatingProcessSHA1 | principal.process.file.sha1 | Value copied directly  
properties.InitiatingProcessSHA256 | principal.process.file.sha256 | Value copied directly if matches hex regex  
properties.InitiatingProcessParentFileName | principal.process.parent_process.file.full_path | Value copied directly  
properties.InitiatingProcessParentId | principal.process.parent_process.pid | Converted to string  
properties.InitiatingProcessId | principal.process.pid | Converted to string  
properties.InitiatingProcessCreationTime | principal.resource.attribute.labels | Merged with labels created from each source field  
properties.InitiatingProcessParentCreationTime | principal.resource.attribute.labels |   
properties.InitiatingProcessVersionInfoOriginalFileName | principal.resource.attribute.labels |   
properties.InitiatingProcessVersionInfoFileDescription | principal.resource.attribute.labels |   
properties.InitiatingProcessVersionInfoInternalFileName | principal.resource.attribute.labels |   
properties.InitiatingProcessVersionInfoProductName | principal.resource.attribute.labels |   
properties.InitiatingProcessLogonId | principal.resource.attribute.labels |   
properties.SenderMailFromDomain | principal.user.attribute.labels | Merged with label created from properties.SenderMailFromDomain  
properties.InitiatingProcessVersionInfoCompanyName | principal.user.company_name | Value copied directly  
properties.InitiatingProcessAccountUpn | principal.user.email_addresses | Merged from properties.InitiatingProcessAccountUpn if matches email regex, properties.SenderMailFromAddress, properties.SenderFromAddress  
properties.SenderMailFromAddress | principal.user.email_addresses |   
properties.SenderFromAddress | principal.user.email_addresses |   
properties.SenderObjectId | principal.user.product_object_id | Value copied directly  
properties.SenderDisplayName | principal.user.user_display_name | Value copied directly  
properties.InitiatingProcessAccountName | principal.user.userid | Value copied directly  
properties.InitiatingProcessAccountSid | principal.user.windows_sid | Extracted using grok pattern  
category | security_result.category_details | Value copied directly  
properties.ReportId | security_result.detection_fields | Merged with labels created from each source field  
properties.NetworkMessageId | security_result.detection_fields |   
properties.AppGuardContainerId | security_result.detection_fields |   
Tenant | security_result.detection_fields |   
properties.ActionType | security_result.summary | Value copied directly  
properties.ThreatTypes | security_result.threat_name | Value from properties.ThreatTypes if not empty/null, else properties.ThreatNames  
properties.ThreatNames | security_result.threat_name |   
properties.InitiatingProcessFileSize | target.process.file.size | Converted to string then to uinteger  
properties.ProcessTokenElevation | target.resource.attribute.labels | Merged with label created from properties.ProcessTokenElevation  
properties.RemoteUrl | target.url | Value copied directly  
properties.RecipientEmailAddress | target.user.email_addresses | Merged from properties.RecipientEmailAddress  
properties.RecipientObjectId | target.user.product_object_id | Value copied directly  
metadata.product_name | metadata.product_name | Set to " Microsoft Defender Endpoint"  
metadata.vendor_name | metadata.vendor_name | Set to "MICROSOFT_DEFENDER_ENDPOINT_IOS"  
`properties.DeviceName` | `principal.hostname and principal.asset.hostname` | Mapped from changelog  
`properties.Timestamp` | `metadata.event_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-defender-endpoint-ios-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
