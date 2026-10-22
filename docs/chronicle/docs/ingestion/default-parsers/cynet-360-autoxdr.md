---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cynet-360-autoxdr/
title: Collect Cynet 360 AutoXDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:06.893524+00:00
---

# Collect Cynet 360 AutoXDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cynet-360-autoxdr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cynet 360 AutoXDR logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cynet 360 AutoXDR logs to Google Security Operations using the Bindplane agent.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cynet 360 AutoXDR management console



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

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
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
             customer_id: <CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'CYNET_360_AUTOXDR'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'CYNET_360_AUTOXDR'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Cynet 360 AutoXDR

  1. Sign in to the **Cynet 360 AutoXDR Management Console**.
  2. Go to **Settings** > **Configuration** > **SIEM Settings**.
  3. Provide the following configuration details: 
     * **Transmission method** : Select **UDP**.
     * **IP address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (default is **514**).
  4. Click **Add**.
  5. Go to **Settings** > **Advanced**.
  6. Select the **Send Audit Records to SIEM** checkbox.
  7. Save the configuration.

**Note:** If you enter a port other than 514, you must restart the Cynet services on the server to apply the change.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Uniqueness_label` | `additional.fields` | Merged  
`clientId_label` | `additional.fields` | Merged  
`confVer_label` | `additional.fields` | Merged  
`epsVer_label` | `additional.fields` | Merged  
`etwAlertId_label` | `additional.fields` | Merged  
`externalId_label` | `additional.fields` | Merged  
`fname_label` | `additional.fields` | Merged  
`gpParams_label` | `additional.fields` | Merged  
`gpSign_label` | `additional.fields` | Merged  
`gpprUser_label` | `additional.fields` | Merged  
`gpssdeep_label` | `additional.fields` | Merged  
`hostLS_label` | `additional.fields` | Merged  
`pParams_label` | `additional.fields` | Merged  
`pSign_label` | `additional.fields` | Merged  
`pct_label` | `additional.fields` | Merged  
`pssdeep_label` | `additional.fields` | Merged  
`scanGroupId_label` | `additional.fields` | Merged  
`sev_label` | `additional.fields` | Merged  
`sign_label` | `additional.fields` | Merged  
`Action` | `extensions.auth.type` | Mapped: `111` → `AUTHTYPE_UNSPECIFIED`  
`Info` | `metadata.description` | Directly mapped  
`dtUtc` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss.SSS`  
`rt` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss`  
`rtUtc` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss.SSS`  
`Action` | `metadata.event_type` | Mapped: `111` → `USER_LOGIN`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `FILE_UNCATEGORIZED`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`DbId` | `metadata.product_log_id` | Directly mapped  
`pprUser` | `principal.administrative_domain` | Directly mapped  
`HostName` | `principal.asset.hostname` | Directly mapped  
`dhost` | `principal.asset.hostname` | Directly mapped  
`RequesterIp` | `principal.asset.ip` | Merged  
`StringIP` | `principal.asset.ip` | Merged  
`src` | `principal.asset.ip` | Merged  
`pFileHash` | `principal.file.sha256` | Directly mapped  
`HostName` | `principal.hostname` | Directly mapped  
`dhost` | `principal.hostname` | Directly mapped  
`RequesterIp` | `principal.ip` | Merged  
`StringIP` | `principal.ip` | Merged  
`src` | `principal.ip` | Merged  
`osVer` | `principal.platform_version` | Directly mapped  
`ppParams` | `principal.process.file.full_path` | Directly mapped  
`gpFileHash` | `principal.process.parent_process.file.sha256` | Directly mapped  
`prUser` | `principal.user.userid` | Directly mapped  
`sec_result` | `security_result` | Merged  
`sev` | `security_result.severity` | Mapped: `Medium` → `MEDIUM`, `Low` → `LOW`, `High` → `HIGH`, `Critical` → `CRITICAL`  
`domain` | `target.administrative_domain` | Directly mapped  
`dst` | `target.asset.ip` | Merged  
`Path` | `target.file.full_path` | Directly mapped  
`filePath` | `target.file.full_path` | Directly mapped  
`fileHash` | `target.file.sha256` | Directly mapped  
`scanGroupName` | `target.group.group_display_name` | Directly mapped  
`dst` | `target.ip` | Merged  
`UserName` | `target.user.userid` | Directly mapped  
`duser` | `target.user.userid` | Directly mapped  
`user` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `Cynet 360 AutoXDR`  
N/A | `metadata.vendor_name` | Constant: `Cynet 360 AutoXDR`  
N/A | `security_result.severity` | Constant: `MEDIUM`  
`externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`fname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sev` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`gpParams` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`gpprUser` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`gpSign` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`hostLS` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`epsVer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`confVer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`scanGroupId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sign` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pssdeep` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pSign` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pct` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`gpssdeep` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`clientId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`etwAlertId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pParams` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sev` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`remedStat` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`actRem` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`cat` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`prUser` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`dhost` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`dhost` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`osVer` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`pFileHash` | `event.idm.read_only_udm.principal.file.sha256` | Mapped from changelog  
`pprUser` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`ppParams` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`gpFileHash` | `event.idm.read_only_udm.principal.process.parent_process.file.sha256` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`filePath` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`duser` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`cef_header` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`duser` | `event.idm.read_only_udm.target.administrative_domain` | Mapped from changelog  
`scanGroupName` | `event.idm.read_only_udm.target.group.group_display_name` | Mapped from changelog  
`dtUtc` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`rt` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`rtUtc` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cynet-360-autoxdr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
