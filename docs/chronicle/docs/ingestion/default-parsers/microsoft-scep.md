---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-scep/
title: Collect Microsoft System Center Endpoint Protection (SCEP) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:32:09.848279+00:00
---

# Collect Microsoft System Center Endpoint Protection (SCEP) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-scep/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft System Center Endpoint Protection (SCEP) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document describes how to collect Microsoft System Center Endpoint Protection (SCEP) logs by setting up a Google Security Operations feed using Microsoft Azure Blob Storage V2.

Microsoft System Center Endpoint Protection (SCEP) is an enterprise antimalware and antivirus solution integrated with System Center Configuration Manager (SCCM). SCEP provides real-time protection against malware, viruses, spyware, and other malicious software for Windows-based endpoints. SCEP writes security events to the `Microsoft-Windows-Windows Defender/Operational` Windows Event Log channel, which can be collected using Azure Monitor Agent and exported to Azure Blob Storage.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to **Microsoft Azure** portal with permissions to: 
    * Create Storage Accounts
    * Create and manage Log Analytics workspaces
    * Create and manage Data Collection Rules
    * Configure data export rules
    * Manage access keys
  * Windows Server 2012 R2 or later with SCEP installed, or Windows Server 2016 or later with Windows Defender Antivirus
  * Azure Monitor Agent installed on the Windows server (requires Azure Arc for on-premises servers, or native support for Azure VMs)
  * Administrator access on the Windows server where SCEP is deployed

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
**Storage account name** | Enter a unique name (for example, `sceplogssa`)  
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
     * **Storage account name** : The name you created (for example, `sceplogssa`)
     * **Key 1** or **Key 2** : The shared access key (a 512-bit random string in base-64 encoding)



### Get Blob Service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://sceplogssa.blob.core.windows.net/`



## Create a Log Analytics workspace

  1. In the **Azure portal** , search for **Log Analytics workspaces**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select the same resource group as the Storage Account  
**Name** | Enter a unique name (for example, `scep-logs-workspace`)  
**Region** | Select the same region as the Storage Account  
  4. Click **Review + Create**.

  5. Click **Create**.

  6. Wait for the deployment to complete.




## Install Azure Monitor Agent on the Windows server

For on-premises servers running SCEP, you must first onboard the server to Azure Arc, and then install Azure Monitor Agent.

### Onboard to Azure Arc (on-premises servers only)

  1. In the **Azure portal** , search for **Azure Arc**.
  2. Select **Servers** under **Infrastructure**.
  3. Click **\+ Add**.
  4. Select **Add a single server** and click **Generate script**.
  5. Provide the following configuration details: 
     * **Subscription** : Select your Azure subscription
     * **Resource group** : Select your resource group
     * **Region** : Select the same region as the Storage Account
     * **Operating system** : Select **Windows**
  6. Click **Download and run script**.
  7. On the Windows server running SCEP, open **PowerShell** as an administrator.
  8. Run the downloaded script to complete the Azure Arc onboarding.

**Note:** For Azure virtual machines, skip the Azure Arc onboarding. Azure Monitor Agent can be installed directly on the VM.



### Install Azure Monitor Agent

  1. In the **Azure portal** , go to **Azure Arc > Servers** (or **Virtual Machines** for Azure VMs).
  2. Select the server running SCEP.
  3. In the left navigation, select **Extensions** under **Settings**.
  4. Click **\+ Add**.
  5. Search for and select **Azure Monitor Agent**.
  6. Click **Next** and then **Review + create**.
  7. Click **Create**.
  8. Wait for the extension installation to complete.



## Create a Data Collection Rule for SCEP events

  1. In the **Azure portal** , search for **Monitor**.
  2. Select **Data Collection Rules** under **Settings**.
  3. Click **\+ Create**.
  4. In the **Basics** tab, provide the following configuration details: 
     * **Rule name** : Enter a descriptive name (for example, `dcr-scep-events`)
     * **Subscription** : Select your Azure subscription
     * **Resource group** : Select your resource group
     * **Region** : Select the same region as the Log Analytics workspace
     * **Platform Type** : Select **Windows**
  5. Click **Next: Resources**.
  6. In the **Resources** tab: 
     1. Click **\+ Add resources**.
     2. Expand the resource group and select the server running SCEP (Azure Arc server or Azure VM).
     3. Click **Apply**.
  7. Click **Next: Collect and deliver**.
  8. In the **Collect and deliver** tab:

     1. Click **\+ Add data source**.
     2. In the **Data source type** dropdown, select **Windows Event Logs**.
     3. Select **Custom** to enter XPath queries.
     4. Click **\+ Add XPath query** and enter the following XPath query to collect all SCEP and Windows Defender events:
            
            Microsoft-Windows-Windows Defender/Operational!*[System[(Level=1 or Level=2 or Level=3 or Level=4 or Level=5)]]
            

This XPath query collects all events (Critical, Error, Warning, Information, and Verbose) from the Windows Defender Operational channel. To collect only specific event IDs (for example, malware detections), use a more targeted query such as:
            
            Microsoft-Windows-Windows Defender/Operational!*[System[(EventID=1006 or EventID=1007 or EventID=1116 or EventID=1117 or EventID=2000 or EventID=2001 or EventID=5007)]]
            

     5. In the **Destination** tab, click **\+ Add destination**.

     6. Select **Azure Monitor Logs** as the **Destination type**.

     7. Select the Log Analytics workspace you created earlier (for example, `scep-logs-workspace`).

  9. Click **Add data source**.

  10. Click **Review + create**.

  11. Click **Create**.




### Key event IDs collected

The Data Collection Rule collects events from the `Microsoft-Windows-Windows Defender/Operational` channel, which includes the following key SCEP event IDs:

Event ID | Description  
---|---  
1006 | Malware detected by antimalware engine  
1007 | Antimalware action taken on detected malware  
1116 | Real-time protection detected malware or potentially unwanted software  
1117 | Real-time protection took action against malware  
2000 | Antimalware signature update started  
2001 | Antimalware signature update completed  
5007 | Antimalware platform configuration changed  
  
## Configure data export from Log Analytics workspace to Azure Blob Storage

### Register the Microsoft.Insights resource provider

  1. In the **Azure portal** , go to **Subscriptions**.
  2. Select your subscription.
  3. In the left navigation, select **Resource providers** under **Settings**.
  4. Search for **Microsoft.Insights**.
  5. If the status is not **Registered** , select it and click **Register**.



### Create a data export rule

  1. In the **Azure portal** , go to your **Log Analytics workspace** (for example, `scep-logs-workspace`).
  2. In the left navigation, select **Data Export** under **Settings**.
  3. Click **\+ New export rule**.
  4. In the **Basics** tab: 
     * **Data export rule name** : Enter a descriptive name (for example, `export-scep-to-blob`)
  5. Click **Next: Source**.
  6. In the **Source** tab, select the **Event** table.

**Note:** Windows Defender Operational events collected via Azure Monitor Agent are stored in the **Event** table in the Log Analytics workspace.
  7. Click **Next: Destination**.

  8. In the **Destination** tab:

     * **Destination type** : Select **Storage Account**
     * **Subscription** : Select the subscription containing the Storage Account
     * **Storage account** : Select the Storage Account you created earlier (for example, `sceplogssa`)
  9. Click **Next: Review + Create**.

  10. Click **Create**.



  * After configuration, events are automatically exported to the Storage Account. A container named `am-Event` is created in the Storage Account. Blobs are stored in 5-minute folders using the following path structure:
        
        am-Event/
          └── WorkspaceResourceId=/subscriptions/{subscription-id}/resourcegroups/{resource-group}/providers/microsoft.operationalinsights/workspaces/{workspace}/
              └── y={year}/m={month}/d={day}/h={hour}/m={minute}/
                  └── PT05M.json
        




### Verify data export

  1. In the **Azure portal** , go to the **Storage Account** (for example, `sceplogssa`).
  2. In the left navigation, select **Containers** under **Data storage**.
  3. Verify that the container `am-Event` exists.
  4. Navigate into the container and verify that JSON files with event data are being created in the folder structure.



## Configure a feed in Google SecOps to ingest Microsoft System Center Endpoint Protection (SCEP) logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft SCEP Logs`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft System Center Endpoint Protection (SCEP)** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
    
    https://sceplogssa.blob.core.windows.net/am-Event/
    

Replace the following:

     * `sceplogssa`: Your Azure storage account name.
     * `am-Event`: The blob container name where exported events are stored.
**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers.
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Shared key** : Enter the shared key value (access key) you captured from the Storage Account
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




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
  6. Additionally, select the **Allow Azure services on the trusted services list to access this storage account** checkbox to permit the Log Analytics workspace data export to write to the Storage Account.

  7. Click **Save**.

**Note:** This feed source uses the Storage Transfer Service (STS) to transfer data from Azure storage to Google SecOps. Before using this feed source, you may need to add the IP ranges used by STS workers to your list of allowed IPs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
about.hostname | about.hostname | Set to "%{_DB_HOST}"  
_DB_PORT | about.port | Value copied directly, converted to integer  
_DB_DRIVER | about.resource.name | Set to "%{_DB_DRIVER}"  
_DB_URL | about.url | Set to "%{_DB_URL}"  
signature_labels | event.idm.read_only_udm.additional.fields | Merged from signature_labels if signature not empty, pending_action if PendingAction not empty, execution_status if ExecutionStatus not empty, record_id if RecordID not empty, error_code if ErrorCode not empty, action_success if ActionSuccess not empty  
pending_action | event.idm.read_only_udm.additional.fields |   
execution_status | event.idm.read_only_udm.additional.fields |   
record_id | event.idm.read_only_udm.additional.fields |   
error_code | event.idm.read_only_udm.additional.fields |   
action_success | event.idm.read_only_udm.additional.fields |   
source_url | event.idm.read_only_udm.src.url | Value from source_url if not empty, else from my_string1 if not empty  
my_string1 | event.idm.read_only_udm.src.url |   
has_principal | metadata.event_type | Set to "NETWORK_CONNECTION" if has_principal and has_target true, else "STATUS_UPDATE" if has_principal true, else "SCAN_FILE" if not no_target_host and path_available true, else "STATUS_UNCATEGORIZED" if not no_target_host, else "USER_UNCATEGORIZED" if has_user true, else "GENERIC_EVENT"  
has_user | metadata.event_type |   
has_target | metadata.event_type |   
no_target_host | metadata.event_type |   
path_available | metadata.event_type |   
Name | metadata.product_event_type | Value copied directly  
DetectionID | metadata.product_log_id | Value copied directly  
metadata.product_name | metadata.product_name | Set to "MICROSOFT SYSTEM CENTER ENDPOINT PROTECTION"  
metadata.vendor_name | metadata.vendor_name | Set to "MICROSOFT"  
NTdomain | principal.administrative_domain | Value copied directly  
hostname | principal.asset.hostname | Value from hostname if not empty, else from TargetHost  
TargetHost | principal.asset.hostname |   
action_type | principal.group.attribute.labels | Merged from action_type_label if action_type not empty  
hostname | principal.hostname | Value from hostname if not empty, else from TargetHost  
TargetHost | principal.hostname |   
Process | principal.process.file.full_path | Value copied directly if Process not empty  
USERNAME | principal.user.user_display_name | Value copied directly  
UserName | principal.user.userid | Value from UserName if not empty, else from user if not empty  
user | principal.user.userid |   
action | security_result.action | Set based on action values (ALLOW for success/created/started/delivered/allowed, BLOCK for failure/blocked/teardown/deferred/deleted/rejected/dropped/error/locked, ALLOW_WITH_MODIFICATION for acl_modified/modified, QUARANTINE for quarantined) or CleanAction (FAIL if Failed, QUARANTINE if Quarantined, ALLOW if Allowed, BLOCK if Blocked)  
CleanAction | security_result.action |   
CleanAction | security_result.action_details | Value copied directly if CleanAction not empty  
category | security_result.category_details | Merged from category if not empty, else from Category  
Category | security_result.category_details |   
DetectionID | security_result.detection_fields | Merged from DetectionID_field if DetectionID not empty, detectionid_field if detectionid not empty, detection_source_labels if detection_source not empty, pending_action_labels if pending_action not empty, detection_Path if source_url and file_path and Path not empty  
detectionid | security_result.detection_fields |   
detection_source | security_result.detection_fields |   
pending_action | security_result.detection_fields |   
Path | security_result.detection_fields |   
severity | security_result.severity | Set based on severity (LOW for 0/1/2/3/LOW, MEDIUM for 4/5/6/MEDIUM/SUBSTANTIAL/INFO, HIGH for 7/8/HIGH/SEVERE, CRITICAL for 9/10/VERY-HIGH/CRITICAL) or SeverityID (LOW for 1, MEDIUM for 2, HIGH for 4, CRITICAL for 5, UNKNOWN_SEVERITY else)  
SeverityID | security_result.severity |   
SeverityID | security_result.severity_details | Value copied directly  
ThreatID | security_result.threat_id | Value copied directly  
ThreatName | security_result.threat_name | Value copied directly  
MaliciousFileCt | security_result.verdict_info | Value copied directly, converted to integer, merged as malicious_file_ct  
dest_nt_domain | target.administrative_domain | Value copied directly  
dest_name | target.asset.hostname | Value copied directly if dest_name not empty  
file_path | target.file.full_path | Value from file_path if not empty, else from Path if file_path empty, else from my_string if not empty  
Path | target.file.full_path |   
my_string | target.file.full_path |   
dest_name | target.hostname | Value copied directly if dest_name not empty  
ResourceID | target.resource.name | Value from ResourceID if not empty, else from resourceid if not empty  
resourceid | target.resource.name |   
user | target.user.userid | Value copied directly if user not empty  
time | metadata.event_timestamp | Converted from time using format "MMM dd HH:mm:ss" if time not empty, else from DetectionTime or detectiontime using UNIX_MS  
DetectionTime | metadata.event_timestamp |   
detectiontime | metadata.event_timestamp |   
`time` | `syslogtimestamp` | Mapped from changelog  
`DetectionID", "detection_source", and "pending_action` | `security_result.detection_fields` | Mapped from changelog  
`action` | `temp_action` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-scep-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
