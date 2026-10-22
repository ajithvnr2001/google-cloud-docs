---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nasuni-file-services/
title: Collect Nasuni File Data Services logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:04.744850+00:00
---

# Collect Nasuni File Data Services logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nasuni-file-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Nasuni File Data Services logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Nasuni File Data Services logs to Google Security Operations using Bindplane. Nasuni File Data Services is a cloud-native file data platform that replaces traditional file storage infrastructure with a scalable, cloud-based solution. It provides file access, file sharing, protection, and global file locking capabilities across edge locations. Nasuni generates audit logs for file operations, access events, and administrative actions that can be forwarded via syslog for security monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Nasuni Management Console (NMC) with administrative privileges.
  * Nasuni Edge Appliance firmware version 9.0 or later.



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
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <PLACEHOLDER_CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'NASUNI_FILE_SERVICES'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<PLACEHOLDER_CUSTOMER_ID>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the **Get Google SecOps credentials for the Bindplane agent** section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <PLACEHOLDER_CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'NASUNI_FILE_SERVICES'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Configure Nasuni syslog forwarding

### Configure syslog on the Nasuni Edge Appliance

  1. Sign in to the **Nasuni Management Console** (NMC).
  2. Go to **Filers > Filer Settings**.
  3. Select the Nasuni Edge Appliance that you want to configure.
  4. Go to the **Syslog** section.
  5. Click **Add Syslog Server**.
  6. Provide the following configuration details: 
     * **Server Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or the port configured in Bindplane).
     * **Protocol** : Select **TCP**.
     * **Format** : Select **Syslog (RFC 5424)** if available, or **Syslog (RFC 3164)**.
  7. In the **Log Categories** section, enable the following log types:

     * **Audit Logs** : File access, create, delete, and rename operations.
     * **Authentication Logs** : User authentication events.
     * **System Logs** : Appliance health, sync, and administrative events.
     * **Snapshot Logs** : Snapshot creation and deletion events.
**Note:** Enable all available categories for comprehensive security monitoring.
  8. Click **Save** to apply the syslog configuration.




### Repeat for additional Edge Appliances

  1. If you have multiple Nasuni Edge Appliances, repeat the syslog configuration for each appliance.
  2. In the **NMC** , go to **Filers > All Filers** to see a list of all managed appliances.
  3. Configure each appliance to forward logs to the same Bindplane agent host and port.



### Verify syslog forwarding

  1. On the Bindplane agent host, verify that logs are being received by checking the agent logs:
         
         sudo journalctl -u observiq-otel-collector -f
         

  2. In the **NMC** , go to **Filers > Filer Settings > Syslog** for the configured appliance.

  3. Verify the syslog server status shows **Connected** or **Active**.




For additional details, refer to the [Nasuni documentation on syslog configuration](https://docs.nasuni.com/).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_label` | `additional.fields` | Merged  
`is_dir_label` | `additional.fields` | Merged  
`offset_label` | `additional.fields` | Merged  
`sequence_label` | `additional.fields` | Merged  
`uid_label` | `additional.fields` | Merged  
`volume_label` | `additional.fields` | Merged  
`msg` | `metadata.description` | Directly mapped  
`proto` | `metadata.description` | Directly mapped  
`event_timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`when` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`event_type` | `metadata.event_type` | Mapped: `"AUDIT_READDIR", "AUDIT_READ","Read"` → `FILE_READ`, `"AUDIT_WRITE","Write"` → `FIL...  
`has_principal` | `metadata.event_type` | Mapped: `true` → `FILE_READ`, `true` → `FILE_MODIFICATION`, `true` → `FILE_UNCATEGORIZED`, `...  
`event_type` | `metadata.product_event_type` | Directly mapped  
`product_log_id` | `metadata.product_log_id` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`ipaddr` | `principal.asset.ip` | Merged  
`host` | `principal.hostname` | Directly mapped  
`ipaddr` | `principal.ip` | Merged  
`prin_port` | `principal.port` | Directly mapped  
`proc_id` | `principal.process.pid` | Directly mapped  
`username` | `principal.user.user_display_name` | Directly mapped  
`sid` | `principal.user.windows_sid` | Directly mapped  
`action` | `security_result.action_details` | Directly mapped  
`application` | `target.application` | Directly mapped  
`path` | `target.file.full_path` | Directly mapped  
`groupname` | `target.group.group_display_name` | Directly mapped  
`gid` | `target.group.product_object_id` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`tid` | `target.resource.product_object_id` | Directly mapped  
`resource` | `target.resource.resource_subtype` | Directly mapped  
`grp` | `target.user.group_identifiers` | Merged  
N/A | `metadata.event_type` | Constant: `FILE_READ`  
N/A | `metadata.product_name` | Constant: `Nasuni File Services Platform`  
N/A | `metadata.vendor_name` | Constant: `Nasuni`  
`action` | `event.idm.read_only_udm.section_result.action_details` | Mapped from changelog  
`group_identifiers` | `event.idm.read_only_udm.target.user.group_identifiers` | Mapped from changelog  
`event_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`ipaddr` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`host` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`newpath` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nasuni-file-services-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
