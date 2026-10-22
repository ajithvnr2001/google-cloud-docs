---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sharepoint/
title: Collect Microsoft SharePoint (Office 365) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:58.743071+00:00
---

# Collect Microsoft SharePoint (Office 365) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sharepoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft SharePoint (Office 365) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to collect Microsoft SharePoint (Office 365) logs into Google Security Operations using Bindplane.

Microsoft SharePoint is a web-based collaborative platform that integrates with Microsoft 361. SharePoint audit logs capture user activities including file operations, folder activities, sharing operations, list operations, and site administration actions. These logs are accessed through the Microsoft Defender for Cloud Apps SIEM agent, which retrieves audit data from SharePoint Online and OneDrive for Business and streams it as syslog to a local receiver.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Microsoft 365 tenant with SharePoint Online
  * Microsoft Defender for Cloud Apps license (included with Microsoft 365 E5 or as an add-on)
  * Global Administrator or Security Administrator role in the Microsoft Defender portal
  * A Windows or Linux server with Java 8 or later to run the SIEM agent (can be the same host as Bindplane)
  * Unified audit logging enabled in Microsoft 365



## Enable unified audit logging

Before Microsoft Defender for Cloud Apps can capture SharePoint audit data, unified audit logging must be enabled for your Microsoft 365 tenant.

  1. Sign in to the [Microsoft Purview compliance portal](https://compliance.microsoft.com).
  2. Go to **Audit**.
  3. If prompted, click **Start recording user and admin activity**. Note: After enabling unified audit logging, it can take up to 12 hours for content to become available.


  * Alternatively, you can enable unified audit logging using PowerShell:
        
        Connect-ExchangeOnline
        Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true
        




## Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/sharepoint:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: SHAREPOINT
            raw_log_field: body
        
        service:
          pipelines:
            logs/sharepoint_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/sharepoint
        




### Configuration parameters

Replace the following placeholders:

  * **Exporter configuration:**

    * `<CUSTOMER_ID>`: The Google SecOps customer ID copied in the previous step
    * **creds_file_path** : Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/sharepoint:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SHAREPOINT
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
    
    net stop observiq-otel-collector && net start observiq-otel-collector
    

     * Services console: 
       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure Microsoft Defender for Cloud Apps SIEM agent to forward SharePoint logs

Microsoft SharePoint Online is a cloud service and does not have a built-in syslog forwarding capability. To forward SharePoint audit logs via syslog, use the Microsoft Defender for Cloud Apps SIEM agent, which retrieves alerts and activities from Defender for Cloud Apps and streams them as syslog messages (in CEF format) to the Bindplane agent.

### Prerequisites for the SIEM agent

  * A Windows or Linux server (can be a virtual machine) with:

    * Java 8 or later installed
    * Transport Layer Security (TLS) 1.2 or later
    * CPU: 2 cores
    * Disk space: 20 GB
    * RAM: 2 GB
**Note:** The SIEM agent can run on the same host as the Bindplane agent, or on a separate server that can reach the Bindplane agent over UDP or TCP port 514.



### Step 1: Configure the SIEM agent in Microsoft Defender portal

  1. Sign in to the [Microsoft Defender portal](https://security.microsoft.com).
  2. Select **Settings**.
  3. Choose **Cloud Apps**.
  4. Under **System** , select **SIEM agents**.
  5. Click **Add SIEM agent** , then choose **Generic SIEM**.
  6. Click **Start Wizard**.
  7. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle-Bindplane-SharePoint`).
     * **Select your SIEM format** : Select **CEF**.
  8. Click **Next**.
  9. Provide the following syslog connection details: 
     * **Remote syslog host** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
     * **Syslog port number** : Enter `514` (or the port configured in your Bindplane agent `config.yaml`).
     * **Remote Syslog protocol** : Select **UDP** (must match the receiver type in Bindplane agent configuration).
  10. Click **Next**.
  11. Configure data types to export: 
     1. Enable the slider for **Activities**.
     2. In the **Apply to** dropdown for **Activities** , set filters to include SharePoint activities: 
        1. Select **App equals** and choose **Microsoft SharePoint Online** and **Microsoft OneDrive for Business**.
     3. Enable the slider for **Alerts** if you also want to receive policy alerts related to SharePoint.
  12. Click **Edit and preview results** to verify the filter matches expected activities.
  13. Click **Next**.
  14. Copy the **token** displayed on the summary page and save it securely.
  15. Click **Finish**.

**Note:** The token is bound to the administrator who created it. If the administrator is removed from Defender for Cloud Apps, the token becomes invalid.



### Step 2: Download and run the SIEM agent JAR file

  1. Download the SIEM agent from the [Microsoft Download Center](https://go.microsoft.com/fwlink/?linkid=838596).
  2. Extract the downloaded ZIP file on the server where the SIEM agent will run.
  3. Run the SIEM agent with the following command:
         
         java -jar mcas-siemagent-0.87.20-signed.jar --token <TOKEN>
         




Replace `<TOKEN>` with the token copied from the Microsoft Defender portal.

**Note:** The JAR filename may differ depending on the version. If the SIEM agent server uses a proxy, add `--proxy ADDRESS:PORT` to the command.

### Step 3: Configure the SIEM agent to run as a service

To ensure continuous log forwarding, configure the SIEM agent to start automatically:

**Linux:**

  * Add the run command to `/etc/rc.local` or create a systemd service:
        
        java -jar /opt/mcas-siemagent/mcas-siemagent-0.87.20-signed.jar --token <TOKEN> &
        




**Windows:**

  * Configure a scheduled task: 
    1. Open **Task Scheduler**.
    2. Create a new task with **Run whether the user is logged on or not**.
    3. Set the action to run the JAR file with the token parameter.
    4. Uncheck **Stop the task if it runs longer than**.



### Step 4: Verify the SIEM agent connection

  1. In the [Microsoft Defender portal](https://security.microsoft.com), go to **Settings > Cloud Apps > SIEM agents**.
  2. Verify the SIEM agent status shows **Connected** (green).
  3. On the Bindplane agent host, verify syslog messages are being received:
         
         sudo journalctl -u observiq-otel-collector -f
         

  4. In Google SecOps, search for logs with `metadata.log_type = "SHAREPOINT"` to confirm log ingestion.

**Note:** When first connected, activities and alerts from the last two days are forwarded, followed by all new activities and alerts going forward.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
Occurred | metadata.event_timestamp | Parsed using date filter with formats "MM/dd/yyyy HH:mm:ss A","MM/dd/yyyy HH:mm:ss a","M/d/yyyy HH:mm:ss A"  
has_principal | metadata.event_type | Set to "USER_RESOURCE_ACCESS" if has_principal and (has_target_resource or has_target), else "STATUS_UPDATE" if has_principal, else "GENERIC_EVENT"  
has_target_resource | metadata.event_type |   
has_target | metadata.event_type |   
metadata.product_name | metadata.product_name | Set to "SHAREPOINT"  
EventData | metadata.product_version | Value copied directly  
metadata.vendor_name | metadata.vendor_name | Set to "SHAREPOINT"  
Created | principal.asset.attribute.labels | Merged labels with key "Created" from Created and key "Last Modified" from LastModified  
LastModified | principal.asset.attribute.labels |   
SamAccountName | principal.asset.hostname | Value copied directly  
SamAccountName | principal.hostname | Value copied directly  
database | principal.process.file.names | Merged from database  
UserEmail | principal.user.email_addresses | Merged from UserEmail if matches email regex  
UserName | principal.user.user_display_name | Value copied directly  
EventType | security_result.description | Value copied directly  
Directory | target.file.full_path | Value copied directly  
Leaf | target.file.names | Merged from Leaf  
ItemType | target.resource.type | Value copied directly  
SecUserURL | target.url | Value copied directly  
SecUserRole | target.user.attribute.roles | Merged role with name from SecUserRole  
SecUserEmail | target.user.email_addresses | Merged from SecUserEmail if matches email regex  
SecGroupName | target.user.group_identifiers | Merged from SecGroupName  
SecUserName | target.user.user_display_name | Value copied directly  
SecSamAccountName | target.user.userid | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sharepoint-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
