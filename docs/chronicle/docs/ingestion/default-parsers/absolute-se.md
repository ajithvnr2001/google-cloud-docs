---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/absolute-se/
title: Collect Absolute Secure Endpoint logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:37.413831+00:00
---

# Collect Absolute Secure Endpoint logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/absolute-se/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Absolute Secure Endpoint logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Absolute Secure Endpoint (formerly Absolute Data & Device Security) logs to Google Security Operations using the Bindplane agent. The parser extracts fields from the SIEM connector logs in either SYSLOG + or KV (CEF) format. It uses grok patterns to identify and extract fields, then uses conditional logic based on the presence of `kv_pair` or `cef` data to map the extracted fields to the UDM schema. Specific mappings and transformations are applied depending on the identified fields and their values, handling both status heartbeat and security event data.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with systemd to run the Bindplane agent
  * A Windows Server (2012 or later) to host the Absolute SIEM Connector service
  * Microsoft .NET Framework 4.0 or higher installed on the Windows Server hosting the SIEM Connector
  * Privileged access to the Absolute Secure Endpoint console with SIEM integration enabled
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements



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

## Get your Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **customer ID** from the **Organization Details** section.



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

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file as follows:

     * Open the `config.yaml` file: `/opt/observiq-otel-collector/config.yaml` on Linux, or `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml` on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             endpoint: chronicle.googleapis.com
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             # Replace with your actual customer ID
             customer_id: '<CUSTOMER_ID>'
             # Adjust the path to the service account key file you saved in Option 1
             creds_file_path: '/path/to/secops-key.json'
             compression: gzip
             log_type: 'ABSOLUTE'
             raw_log_field: body
             # Add optional ingestion labels for better organization
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<LOCATION>` with the region of your Google SecOps instance. The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/secops-key.json` to the file path where the service account key file (Option 1) was saved.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the ingestion authentication file you downloaded in Option 2
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'ABSOLUTE'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Install the Absolute SIEM Connector on Windows Server

The Absolute SIEM Connector is a Windows service that retrieves alert event data from the Absolute Monitoring Center and forwards it through syslog in CEF format. The SIEM Connector is delivered as an MSI installer and is available as a free download to Absolute Data & Device Security (DDS) Professional and Premium customers from the Absolute Customer Center.

  1. Sign in to the **Absolute Secure Endpoint Console** at `https://cc.absolute.com/`.
  2. Go to the **Customer Center** or **Downloads** section.
  3. Download the **Absolute SIEM Connector** MSI installer.
  4. Transfer the installer to your Windows Server.
  5. Run the installer on your Windows Server as an administrator.
  6. Follow the installation wizard to complete the installation.
  7. Note the installation directory (typically `C:\Program Files\Absolute Software\Absolute SIEM Connector`).



## Enable SIEM integration in the Absolute Secure Endpoint Console

Before the SIEM Connector can retrieve events, you must enable SIEM integration in the Absolute Secure Endpoint Console.

  1. Sign in to the **Absolute Secure Endpoint Console** at `https://cc.absolute.com/`.
  2. Go to the **Settings** or **Administration** section.
  3. Go to the **SIEM Integration** settings.
  4. Click **Enable SIEM Integration** or toggle the SIEM integration setting to **On**.
  5. Select the event types you want to forward to your SIEM. 
     * You can also select **All event types** to forward all available logs.
  6. Click **Save** or **Apply** the configuration.



## Configure the Absolute SIEM Connector

After installing the SIEM Connector and enabling SIEM integration in the console, configure the connector to send events to the Bindplane agent as follows:

  1. On the Windows Server where the Absolute SIEM Connector is installed, open the **Absolute SIEM Connector Configuration Tool**. 
     * You can find this in the **Start Menu** under **Absolute Software** or in the installation directory.
  2. Provide the following configuration details: 
     * **Syslog Server Host** : Enter the IP address or hostname of the Bindplane agent host.
     * **Syslog Server Port** : Enter `514` (or the port configured in Bindplane).
     * **Protocol** : Select **UDP** or **TCP** depending on your Bindplane configuration.
     * **Format** : Confirm **CEF** (Common Event Format) is selected.
     * **Update Interval** : Set how often the connector retrieves events from Absolute. The minimum is 2 minutes, the maximum is 1,440 minutes or 24 hours. The default is 60 minutes.
     * **Timezone** : Events are transmitted in **UTC** timezone for universal consistency across systems.
  3. Click **Save**.
  4. Start or restart the **Absolute SIEM Connector** service: 
     * Open **Services** (services.msc).
     * Select the **Absolute SIEM Connector** service.
     * Click **Start** or **Restart**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`pid` | `about.process.pid` | Directly mapped  
`hostname` | `intermediary.hostname` | Directly mapped  
`dvc_ip` | `intermediary.ip` | Merged  
`Alert Time` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`date` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss UTC`  
`event_type` | `metadata.event_type` | Directly mapped  
`eventType` | `metadata.product_event_type` | Directly mapped  
`event_class` | `metadata.product_event_type` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`Serial Number` | `principal.asset.asset_id` | Directly mapped  
`Computer Name` | `principal.hostname` | Directly mapped  
`actorName` | `principal.hostname` | Directly mapped  
`objectName` | `principal.hostname` | Directly mapped  
`objectID` | `principal.resource.product_object_id` | Directly mapped  
`objectType` | `principal.resource.resource_type` | Directly mapped  
`roles` | `principal.user.attribute.roles` | Merged  
`actorID` | `principal.user.product_object_id` | Directly mapped  
`actorName` | `principal.user.userid` | Directly mapped  
`Condition` | `security_result.description` | Directly mapped  
`esn_label` | `security_result.detection_fields` | Merged  
`kv_pair` | `security_result.detection_fields` | Mapped: `ESN` → `esn_label`  
`verb` | `security_result.summary` | Directly mapped  
`Alert ID` | `security_result.threat_id` | Directly mapped  
`Alert Name` | `security_result.threat_name` | Directly mapped  
`field_` | `target.resource.attribute.labels` | Merged  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `ABSOLUTE_PLATFORM`  
N/A | `metadata.vendor_name` | Constant: `ABSOLUTE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/absolute-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
