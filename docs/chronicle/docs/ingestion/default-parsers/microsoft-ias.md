---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-ias/
title: Collect Microsoft IAS / Network Policy Server (NPS) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:16.531554+00:00
---

# Collect Microsoft IAS / Network Policy Server (NPS) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-ias/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft IAS / Network Policy Server (NPS) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect Microsoft Internet Authentication Service (IAS) / Network Policy Server (NPS) logs by setting up a Google SecOps feed using Microsoft Azure Blob Storage V2.

Microsoft Network Policy Server (NPS) is the Microsoft implementation of a RADIUS (Remote Authentication Dial-In User Service) server and proxy. NPS enables centralized management of network access authentication, authorization, and accounting for VPN connections, wireless access points, 802.1X authenticating switches, and dial-up remote access. NPS was formerly known as Internet Authentication Service (IAS) in Windows Server 2003 and earlier versions. Because NPS runs as a Windows Server role without native cloud export capabilities, this guide uses Azure Monitor Agent to collect NPS accounting log files from the local file system and route them through a Log Analytics workspace to Azure Blob Storage.

## Before you begin

  * Ensure that you have the following prerequisites:

  * A Google SecOps instance

  * Privileged access to **Microsoft Azure** portal with permissions to:

    * Create Storage Accounts
    * Create and manage Log Analytics workspaces
    * Create Data Collection Rules
    * Create data export rules
    * Manage access keys
  * Windows Server 2016 or later with the NPS role installed

  * Administrative access to the NPS server

  * Network connectivity from the NPS server to Azure (HTTPS outbound on port 443)

**Note:** If you restrict access to your Azure resources using an Azure Storage firewall, you must add the IP ranges used by Storage Transfer Service (STS) workers to your list of allowed IPs. See [IP Allowlisting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#ip_allowlisting).



## Configure NPS accounting and logging

Enable NPS to log authentication and accounting requests to a local text file in IAS format.

### Enable NPS accounting logs

  1. On the Windows Server running NPS, open **Server Manager**.
  2. Go to **Tools > Network Policy Server**.
  3. In the NPS console tree, click **Accounting**.
  4. In the details pane, under **Accounting** , click **Configure Accounting**.
  5. In the **Accounting Configuration** wizard, select **Log to a text file on the local computer** and click **Next**.
  6. In the **Configure Log File Properties** page, configure the following: 
     * In the **Log the following information** section, select the checkboxes for the information you want to log: 
       * **Accounting requests**
       * **Authentication requests**
       * **Periodic accounting status**
       * **Periodic authentication status**
     * In the **Logging failure action** section, select **If logging fails, discard connection requests** if you want NPS to stop processing when log files are unavailable. Leave unchecked if you want NPS to continue processing even if logging fails.
  7. Click **Next**.
  8. Review the summary and click **Finish**.



### Configure log file properties

  1. In the NPS console tree, click **Accounting**.
  2. In the details pane, under **Log File Properties** , click **Change Log File Properties**.
  3. Click the **Log File** tab.
  4. In the **Directory** field, verify or change the log file location: 
     * Default location: `%systemroot%\System32\LogFiles`
     * For better organization, specify a dedicated directory (for example, `C:\NPSLogs`)
  5. In the **Format** dropdown, select **IAS (Legacy)**.

**Note:** The MICROSOFT_IAS log type parser expects the IAS legacy CSV format. Do not select DTS Compliant or ODBC (Legacy) for this integration.
  6. In **Create a new log file** , select the log rotation interval:

     * **Daily** (recommended for most environments)
     * **Weekly**
     * **Monthly**
     * **Never (unlimited file size)**
     * **When the log file reaches this size** (specify size in MB)
  7. If you want NPS to delete old log files when disk space is low, select **When the disk is full delete older log files**.

  8. Click **OK** to save the configuration.

  9. Verify that log files are being created in the configured directory.

**Note:** Log files are named in the format `INyymmdd.log` where `yy` is the two-digit year, `mm` is the month, and `dd` is the day (for example, `IN250315.log` for March 15, 2025). For more information, see [Configure Network Policy Server Accounting](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-accounting-configure).



## Configure Azure Storage Account

### Create Storage Account

  1. In the **Azure portal** , search for **Storage accounts**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select existing or create new  
**Storage account name** | Enter a unique name (for example, `npsiaslogs`)  
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
     * **Storage account name** : Your storage account name (for example, `npsiaslogs`)
     * **Key 1** or **Key 2** : The shared access key (a 512-bit random string in base-64 encoding)



### Get Blob Service endpoint

  1. In the same Storage Account, select **Endpoints** from the left navigation.
  2. Copy and save the **Blob service** endpoint URL. 
     * Example: `https://npsiaslogs.blob.core.windows.net/`



## Create a Log Analytics workspace

A Log Analytics workspace is required to receive custom text logs from Azure Monitor Agent before exporting them to Azure Blob Storage.

  1. In the **Azure portal** , search for **Log Analytics workspaces**.
  2. Click **\+ Create**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription** | Select your Azure subscription  
**Resource group** | Select the same resource group as your Storage Account  
**Name** | Enter a unique name (for example, `nps-ias-workspace`)  
**Region** | Select the same region as your Storage Account  
  4. Click **Review + Create**.

  5. Review the settings and click **Create**.

  6. Wait for the deployment to complete.




### Create a custom log table

Create a custom table in the Log Analytics workspace to store the NPS/IAS log data.

  1. In the **Azure portal** , go to the **Log Analytics workspace** you just created.
  2. In the left navigation, select **Tables** under **Settings**.
  3. Click **\+ Create > New custom log (DCR-based)**.
  4. In the **Table name** field, enter `NpsIasLogs`. The full table name will be `NpsIasLogs_CL`.
  5. Click **Create**.

**Note:** The table must exist before you create the Data Collection Rule. The `_CL` suffix is automatically appended to custom log table names. For more information, see [Create a custom table](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/create-custom-table).



## Onboard the NPS server to Azure Arc

Because NPS runs on an on-premises Windows Server, you must onboard the server to Azure Arc before installing Azure Monitor Agent.

### Register the NPS server with Azure Arc

  1. In the **Azure portal** , search for **Azure Arc**.
  2. In the left navigation, select **Machines** under **Infrastructure**.
  3. Click **\+ Add/Create > Add a machine**.
  4. In the **Add servers with Azure Arc** section, select **Generate script** under **Add a single server**.
  5. Provide the following configuration details: 
     * **Subscription** : Select your Azure subscription.
     * **Resource group** : Select the same resource group used previously.
     * **Region** : Select the same region as your Log Analytics workspace.
     * **Operating system** : Select **Windows**.
     * **Connectivity method** : Select **Public endpoint** (or **Proxy server** if required by your network).
  6. Click **Download and run script**.
  7. Copy the generated PowerShell script to the NPS server.
  8. On the NPS server, open **PowerShell** as Administrator and run the script:
         
         & '.\OnboardingScript.ps1'
         

  9. Follow the on-screen instructions to authenticate with Azure and complete the onboarding.

  10. After the script completes, go back to the **Azure portal > Azure Arc > Machines** and verify that the NPS server appears with a **Connected** status.

**Note:** The Azure Connected Machine agent requires HTTPS outbound connectivity on port 443 to Azure endpoints. For more information, see [Deploy Azure Arc-enabled servers](https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview).



## Install Azure Monitor Agent

### Install Azure Monitor Agent on the Arc-enabled server

  1. In the **Azure portal** , go to **Azure Arc > Machines**.
  2. Select the NPS server from the list of machines.
  3. In the left navigation, select **Extensions** under **Settings**.
  4. Click **\+ Add**.
  5. Select **Azure Monitor Agent** from the list of extensions.
  6. Click **Next**.
  7. Click **Review + create**.
  8. Click **Create**.
  9. Wait for the extension installation to complete. The status will change to **Provisioning succeeded**.

**Note:** You can also install the Azure Monitor Agent using PowerShell or the Azure CLI. For more information, see [Install and manage the Azure Monitor Agent](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-manage).



## Create a Data Collection Rule for NPS log files

A Data Collection Rule (DCR) instructs Azure Monitor Agent to collect the NPS IAS log files and send them to the Log Analytics workspace.

  1. In the **Azure portal** , search for **Monitor**.
  2. In the left navigation, select **Data Collection Rules** under **Settings**.
  3. Click **\+ Create**.
  4. In the **Basics** tab, provide the following configuration details: 
     * **Rule Name** : Enter `dcr-nps-ias-logs`.
     * **Subscription** : Select your Azure subscription.
     * **Resource Group** : Select the same resource group used previously.
     * **Region** : Select the same region as your Log Analytics workspace.
     * **Platform Type** : Select **Windows**.
  5. Click **Next: Resources**.
  6. In the **Resources** tab: 
     1. Click **\+ Add resources**.
     2. Expand the resource group and select the Azure Arc-enabled NPS server.
     3. Click **Apply**.
  7. Click **Next: Collect and deliver**.
  8. In the **Collect and deliver** tab:

     1. Click **\+ Add data source**.
     2. In the **Data source type** dropdown, select **Custom Text Logs**.
     3. In the **File pattern** field, enter the path to the NPS log files:
            
            C:\Windows\System32\LogFiles\IN*.log
            

**Note:** Update this path if you configured NPS to write logs to a different directory (for example, `C:\NPSLogs\IN*.log`).
     4. In the **Table name** dropdown, select `NpsIasLogs_CL`.

     5. In the **Record delimiter** field, select **End of line**.

     6. In the **Transform** field, enter `source` to send the raw log data unchanged.

     7. Click **Add data source**.

  9. In the **Destination** section, verify that the Log Analytics workspace you created is listed.

  10. Click **Next: Review + create**.

  11. Review the configuration and click **Create**.

**Note:** After the DCR is created and associated with the Azure Monitor Agent, it may take up to 5 minutes for log collection to begin. Verify that data is appearing in the `NpsIasLogs_CL` table by running a query in Log Analytics. For more information, see [Collect logs from a text or JSON file with Azure Monitor Agent](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/data-collection-text-log).



## Configure data export to Azure Blob Storage

Create a data export rule to continuously export NPS/IAS log data from the Log Analytics workspace to Azure Blob Storage.

### Create data export rule

  1. In the **Azure portal** , go to the **Log Analytics workspace** you created.
  2. In the left navigation, select **Data Export** under **Settings**.
  3. Click **\+ New export rule**.
  4. In the **Basics** tab, provide the following configuration details: 
     * **Rule name** : Enter `export-nps-ias-logs`.
     * **Destination** : Select **Storage Account**.
  5. Click **Next: Source**.
  6. In the **Source** tab, select the **NpsIasLogs_CL** table.
  7. Click **Next: Destination**.
  8. In the **Destination** tab: 
     * **Subscription** : Select the subscription containing your Storage Account.
     * **Storage Account** : Select the Storage Account you created earlier (for example, `npsiaslogs`).
  9. Click **Review + create**.
  10. Review the configuration and click **Create**.

**Note:** The data export rule provisioning takes approximately 30 minutes before the export operation starts. Once active, data is continuously exported as it arrives. A container named `am-NpsIasLogs_CL` is automatically created in the Storage Account. Blobs are stored in 5-minute folders using the path structure: `WorkspaceResourceId=/subscriptions/{subscription-id}/resourcegroups/{resource-group}/providers/microsoft.operationalinsights/workspaces/{workspace}/y={year}/m={month}/d={day}/h={hour}/m={minute}/PT05M.json`. For more information, see [Log Analytics workspace data export](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-data-export).



## Configure a feed in Google SecOps to ingest Microsoft IAS logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft IAS NPS Logs`).
  5. Select **Microsoft Azure Blob Storage V2** as the **Source type**.
  6. Select **Microsoft IAS** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Azure URI** : Enter the Blob Service endpoint URL with the container path:
    
    https://npsiaslogs.blob.core.windows.net/am-NpsIasLogs_CL/
    

     * Replace the following: 
       * `npsiaslogs`: Your Azure storage account name.
       * `am-NpsIasLogs_CL`: The blob container name automatically created by the data export rule.
**Note:** Include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:
     * **Never** : Never deletes any files after transfers.
     * **Delete transferred files** : Deletes files after successful transfer.
     * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Shared key** : Enter the shared key value (access key) you captured from the Storage Account earlier
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
  6. Verify that the **Allow Azure services on the trusted services list to access this storage account** checkbox is selected (required for the Log Analytics data export to work).

  7. Click **Save**.

**Note:** This feed source uses the Storage Transfer Service (STS) to transfer data from Azure storage to Google SecOps. Before using this feed source, you may need to add the IP ranges used by STS workers to your list of allowed IPs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
packet_type | additional.fields | Merged with labels for each field if not empty  
auth_type | additional.fields |   
filter_id | additional.fields |   
framed_netmask | additional.fields |   
framed_address | additional.fields |   
framed_protocol | additional.fields |   
framed_routing | additional.fields |   
framed_mtu | additional.fields |   
framed_compression | additional.fields |   
reason_code | additional.fields |   
extensible_auth_protocol | additional.fields |   
service_type | additional.fields |   
nas_port | additional.fields |   
reply_message | additional.fields |   
nas_identifier | additional.fields |   
device-type | additional.fields |   
coa-push | additional.fields |   
audit-session-id | additional.fields |   
date | metadata.event_timestamp | Concatenated from date and time, then parsed with format MM/dd/yyyy HH:mm:ss  
time | metadata.event_timestamp |   
principal_present | metadata.event_type | Set to "GENERIC_EVENT", then "NETWORK_CONNECTION" if principal_present and target_present, else "STATUS_UPDATE" if principal_present  
target_present | metadata.event_type |   
ac-user-agent | network.http.parsed_user_agent | Converted from ac-user-agent if parsing succeeds  
ac-user-agent | network.http.user_agent | Value copied directly  
session_duration | network.session_duration.seconds | Value copied directly, then converted to integer  
session_id | network.session_id | Value copied directly  
principal_hostname | principal.asset.hostname | Value copied directly  
principal_ip | principal.asset.ip | Value from principal_ip if valid IP, else calling_station_id if valid IP  
calling_station_id | principal.asset.ip |   
principal_hostname | principal.hostname | Value copied directly  
principal_ip | principal.ip | Value from principal_ip if valid IP, else calling_station_id if valid IP  
calling_station_id | principal.ip |   
device-mac | principal.mac | Value from device-mac if not empty (after replacing - with :), else device-public-mac  
device-public-mac | principal.mac |   
nat_ip | principal.nat_ip | Value copied directly  
device-platform | principal.platform | Set to "WINDOWS" if in ["Win","win"], "MAC" if =~ "mac|iOS", "LINUX" if =~ "lin"  
device-platform-version | principal.platform_version | Value copied directly  
device-uid | principal.resource.product_object_id | Value copied directly  
user_name | principal.user.user_display_name | Value copied directly  
userid | principal.user.userid | Value copied directly  
service_name | target.application | Value copied directly  
computer_name | target.asset.hostname | Value copied directly  
target_ip | target.asset.ip | Value from target_ip if valid IP, else called_station_id if valid IP  
called_station_id | target.asset.ip |   
computer_name | target.hostname | Value copied directly  
target_ip | target.ip | Value from target_ip if valid IP, else called_station_id if valid IP  
called_station_id | target.ip |   
target_port | target.port | Value copied directly, then converted to integer  
metadata.product_name | metadata.product_name | Set to "MICROSOFT_IAS"  
metadata.vendor_name | metadata.vendor_name | Set to "MICROSOFT_IAS"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
