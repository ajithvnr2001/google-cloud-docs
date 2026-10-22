---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-dlp/
title: Collect Fortra Digital Guardian DLP (formerly Digital Guardian DLP) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:52.144328+00:00
---

# Collect Fortra Digital Guardian DLP (formerly Digital Guardian DLP) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-dlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortra Digital Guardian DLP (formerly Digital Guardian DLP) logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortra Digital Guardian DLP (formerly known as Digital Guardian DLP) logs to Google Security Operations using Bindplane.

Fortra Digital Guardian DLP is a data loss prevention platform that monitors, detects, and prevents unauthorized data transfers across endpoints, networks, and cloud applications. The platform provides visibility into sensitive data movement through policy-based controls, content inspection, and contextual classification, helping organizations protect intellectual property and comply with regulatory requirements.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A host running Windows Server 2016 or later, or a Linux host with `systemd`.
  * Network connectivity between the Bindplane agent and Fortra Digital Guardian DLP.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Fortra Digital Guardian Management Console.



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

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with **root** or **sudo** privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux** : `/opt/observiq-otel-collector/config.yaml`
  * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`



### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/dg_dlp:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: DIGITALGUARDIAN_DLP
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/digitalguardian_dlp:
              receivers:
                - tcplog
              exporters:
                - chronicle/dg_dlp
        




### Configuration parameters

Replace the following placeholders:

  * **`tcplog`** : TCP syslog receiver. TCP is recommended for **Fortra Digital Guardian DLP** to prevent truncation of events exceeding 1024 bytes.
  * **`creds_file_path`** : Full path to the service account JSON key file (Option 1).
  * **`<customer_id>`**: Your Customer ID from the previous step.
  * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
  * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/dg_dlp:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: DIGITALGUARDIAN_DLP
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
         




## Configure Fortra Digital Guardian syslog export

  1. Sign in to the **Digital Guardian Management Console**.
  2. Go to **Workspace** > **Data Export** > **Create Export**.
  3. Select **Alerts** or **Events** as the data source.
  4. Select **Syslog** as the Export Type.
  5. From the **Type** list, select **TCP**.
  6. In the **Server** field, enter the IP address of the **Bindplane agent** host.
  7. In the **Port** field, enter `514`.
  8. Select a severity level and ensure the **Is Active** checkbox is selected.
  9. Click **Next**.
  10. Add **All** Alert and Event fields for the data export.
  11. Complete the wizard by testing the query and clicking **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
Agent Version | `observer.platform_version` | Directly mapped.  
Application | `principal.process.command_line` | Mapped if not empty.  
Command Line | `target.process.command_line` | Directly mapped.  
Company Name | `principal.user.company_name` | Directly mapped.  
Computer Name | `principal.hostname` | Directly mapped.  
DNS Hostname | `target.asset.hostname` | Directly mapped.  
Destination File Path | `target.file.full_path` | Directly mapped.  
Email Sender | `network.email.from` | Mapped if not empty.  
Email Subject | `network.email.subject` | Mapped if Sender is not empty.  
Event Time | `metadata.event_timestamp` | Converted to timestamp format.  
MAC Address | `target.mac` | Mapped if not empty.  
MD5 Hash | `target.process.file.md5` | Lowercased and mapped.  
Network Direction | `network.direction` | Mapped to **INBOUND** or **OUTBOUND**.  
Process Path | `target.process.file.full_path` | Directly mapped.  
SHA256 Hash | `target.process.file.sha256` | Lowercased and mapped.  
URL Path | `target.url` | Directly mapped.  
User | `principal.user.userid` | Directly mapped.  
Was Detail Blocked | `security_result.action` | **BLOCK** if Yes, **ALLOW** if No.  
N/A | `metadata.log_type` | Set to `DIGITALGUARDIAN_DLP`.  
N/A | `metadata.vendor_name` | Set to `DigitalGuardian`.  
`recipient_address` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`recipient_name` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`recipient_address` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
`recipient_name` | `event.idm.read_only_udm.target.user.attribute.labels` | Mapped from changelog  
`recipient_address` | `event.idm.read_only_udm.network.email.cc` | Mapped from changelog  
`recipient_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attachment_display_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attachment_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Classification` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Classification_value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`xmlns_m` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Configuration` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Host_Product_Version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Host_Product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Item_Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Product_Version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`Product_Edition` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Product_Name` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`McAfee_product_code` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`os` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`WINDOWS` | `event.idm.read_only_udm.principal.platform` | Mapped from changelog  
`machine_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ipv6` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`ipv4` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`machine` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`eventtype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`date_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`event_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalguardian-dlp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
