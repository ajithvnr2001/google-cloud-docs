---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-app-control/
title: Collect Carbon Black App Control (formerly CB Protection) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:09.065941+00:00
---

# Collect Carbon Black App Control (formerly CB Protection) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cb-app-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Carbon Black App Control (formerly CB Protection) logs

**Parser Version:** 28.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Carbon Black App Control (formerly known as CB Protection, now part of Broadcom) logs to Google Security Operations using Bindplane. The parser supports both CEF and JSON formats. It first attempts to parse the input as JSON; if that fails, it treats the input as CEF, performs text substitutions, extracts CEF fields, maps them to UDM, and sets the event type to `GENERIC_EVENT`.

Carbon Black App Control is an application control and whitelisting solution that allows organizations to lock down servers and critical systems. It prevents unauthorized and malicious software from executing by enforcing trust-based policies, monitoring file integrity changes, and providing real-time visibility into endpoint activity.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows Server 2016 or later or Linux host with `systemd`.
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open.
  * Carbon Black App Control Server version 8.x or later.
  * Privileged access (Administrator account) to the Carbon Black App Control console.



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

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
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
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: CB_APP_CONTROL
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
  * Replace `<customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: CB_APP_CONTROL
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
         




## Configure Carbon Black App Control syslog forwarding

  1. Sign in to the **Carbon Black App Control console** with an Administrator account.
  2. Click the **Settings** (gear) icon and click **System Configuration**.
  3. On the **System Configuration** page, click the **Events** tab.
  4. Click the **Edit** button at the bottom of the page.
  5. In the **External Event Logging** panel, select the **Syslog Enabled** checkbox.
  6. Provide the following configuration details: 
     * **Syslog Address** : Enter the IP address or FQDN of the Bindplane agent host (for example, `192.168.1.100`).
     * **Syslog Port** : Enter `514` (or the port configured in Bindplane).
     * **Syslog Format** : Select the output format from the **Syslog Format** menu: 
       * **CEF (ArcSight)** \- recommended for Google SecOps ingestion.
       * **Enhanced (RFC 5424)** \- default for new installations of v6.0.1 and later.
       * **Basic (RFC 3164)** \- default for upgrades from pre-6.0.1 versions.
       * **LEEF (Q1 Labs)** \- for QRadar integration.
  7. Click **Update** and then click **Yes** in the confirmation dialog box.

**Note:** For more information on supported syslog formats and event mapping, see the [Carbon Black App Control documentation](https://techdocs.broadcom.com/us/en/carbon-black/app-control/carbon-black-app-control/8-11-0/app-control-user-guide_tile/GUID-67590BCA-1415-4586-92D7-D9672C69F670-en/GUID-670A2774-0CEF-407B-8AE2-313A75FA7352-en/GUID-0DB65E05-937D-4D24-BDD1-E18AD684BB6C-en/GUID-610CCD1E-640A-43B3-BD7F-CC49213117D8-en.html).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`ABId` | `principal.asset.asset_id` | The `ABId` from the JSON log is used as part of the asset ID in the format `PRODUCT_SPECIFIC_ID:{ABId}-{Bit9Server}`.  
`Bit9Server` | `principal.asset.asset_id` | Used as part of the principal's asset ID, combined with `ABId`. Also used to construct the `metadata.url_back_to_product` field.  
`CommandLine` | `about.process.command_line` | Directly mapped.  
`EventType` | `metadata.product_event_type` | Mapped with the corresponding `EventTypeId` in square brackets (for example, `[5] - Discovery`).  
`EventTypeId` | `metadata.product_event_type` | Used with `EventType` to populate `metadata.product_event_type`.  
`EventSubType` | `metadata.description` | Appended to the `metadata.description` field.  
`EventSubTypeId` | `metadata.description` | Not explicitly mapped, but potentially contributes to the description based on the parser's internal logic.  
`externalId` | `metadata.product_log_id` | Directly mapped.  
`FileHash` | `about.file.sha256` | Directly mapped.  
`FileName` | `additional.fields` (with key `FileName`) | Added as an additional field. Also used as part of file information in `metadata.description` for some events.  
`FilePath` | `about.file.full_path` | Directly mapped.  
`FileThreat` | `additional.fields` (with key `fileThreat`) | Added as an additional field.  
`FileTrust` | `additional.fields` (with key `fileTrust`) | Added as an additional field.  
`HostId` | `principal.asset.asset_id` | Used to construct the URL back to the product in `metadata.url_back_to_product`.  
`HostName` | `target.hostname` | Directly mapped.  
`HostIP` | `target.ip` | Directly mapped.  
`Message` | `metadata.description` | Directly mapped.  
`PathName` | `about.file.full_path` | Directly mapped.  
`Platform` | `target.platform` | Mapped to the enum value `WINDOWS`.  
`Policy` | `additional.fields` (with key `Policy`) | Added as an additional field.  
`PolicyId` | `additional.fields` (with key `PolicyId`) | Added as an additional field.  
`ProcessKey` | `additional.fields` (with key `ProcessKey`) | Added as an additional field.  
`ProcessPath` | `about.process.command_line` | Directly mapped.  
`ProcessPathName` | `about.process.command_line` | Directly mapped.  
`ProcessThreat` | `additional.fields` (with key `ProcessThreat`) | Added as an additional field.  
`ProcessTrust` | `additional.fields` (with key `ProcessTrust`) | Added as an additional field.  
`RuleName` | `additional.fields` (with key `ruleName`) | Added as an additional field.  
`Timestamp` | `metadata.event_timestamp` | Directly mapped.  
`UserName` | `target.user.user_display_name` | Directly mapped.  
`UserSid` | `principal.user.userid` | Directly mapped.  
`agent.ephemeral_id` | `observer.labels` (with key `ephemeral_id`) | Added as an observer label.  
`agent.name` | `principal.hostname`, `observer.hostname`, `observer.user.userid` | Mapped to multiple fields.  
`agent.type` | `observer.application` | Directly mapped.  
`agent.version` | `metadata.product_version` | Directly mapped for JSON logs. For CEF logs, extracted from the CEF message.  
`cat` | `security_result.category_details` | Directly mapped.  
`process` | `event.idm.read_only_udm.principal.file.full_path` | Mapped from changelog  
`text` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`type` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`subtype` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`username` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`date` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`ip_address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`file_path` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`file_name` | `event.idm.read_only_udm.target.process.file.names` | Mapped from changelog  
`file_hash` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`policy` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`server_version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`file_trust` | `event.idm.read_only_udm.security_result.about.labels` | Mapped from changelog  
`file_threat` | `event.idm.read_only_udm.security_result.about.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cb-app-control-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
