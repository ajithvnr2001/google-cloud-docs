---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-dlp/
title: Collect Trellix DLP (formerly McAfee DLP) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:03.174631+00:00
---

# Collect Trellix DLP (formerly McAfee DLP) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-dlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix DLP (formerly McAfee DLP) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix DLP (formerly known as McAfee DLP) logs to Google Security Operations using Bindplane.

Trellix DLP is a data loss prevention solution that monitors, detects, and prevents unauthorized transmission of sensitive data across endpoints, networks, and cloud environments. It is managed through Trellix ePO (ePolicy Orchestrator), which provides centralized policy management, event monitoring, and reporting for DLP incidents.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Trellix ePO (ePolicy Orchestrator) console.
  * Trellix DLP policies configured and generating events in ePO.



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

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: MCAFEE_DLP
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
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the **Get Google SecOps credentials for the Bindplane agent** section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: MCAFEE_DLP
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
         




## Configure Trellix DLP syslog forwarding

Syslog forwarding for Trellix DLP is configured through the Trellix ePO (ePolicy Orchestrator) console by registering a syslog server.

  1. Sign in to the **Trellix ePO** console.
  2. Go to **Menu > Configuration > Registered Servers**.
  3. Click **New Server**.
  4. In the **Server type** dropdown, select **Syslog**.
  5. In the **Name** field, enter a descriptive name (for example, `Chronicle-Bindplane`).
  6. Click **Next**.
  7. Provide the following configuration details: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
     * **Event format** : Select **Common Event Format (CEF)**.
  8. Click **Test Connection** to verify connectivity to the Bindplane agent.
  9. Click **Save** to save the registered syslog server.



### Enable DLP event forwarding

  1. Go to **Menu > Automation > Automatic Responses**.
  2. Click **New Response** to create a new automatic response rule.
  3. In the **Name** field, enter a descriptive name (for example, `DLP Syslog Forwarding`).
  4. In the **Event Group** dropdown, select **DLP Events**.
  5. In the **Event Type** dropdown, select **DLP Incident Events**.
  6. Click **Next**.
  7. In the **Filters** tab, configure filters as needed or leave defaults to forward all DLP events.
  8. Click **Next**.
  9. In the **Actions** tab, click **Add Action**.
  10. In the **Action type** dropdown, select **Send Syslog**.
  11. In the **Syslog Server** dropdown, select the registered syslog server (`Chronicle-Bindplane`).
  12. Click **Next**.
  13. Review the summary and click **Save**.

**Note:** Repeat these steps for additional DLP event types (such as **DLP Operation Events** or **DLP Policy Events**) to forward all relevant DLP logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_field_0` | `additional.fields` | Merged  
`additional_field_1` | `additional.fields` | Merged  
`additional_field_2` | `additional.fields` | Merged  
`additional_field_3` | `additional.fields` | Merged  
`additional_field_4` | `additional.fields` | Merged  
`additional_field_5` | `additional.fields` | Merged  
`additional_field_6` | `additional.fields` | Merged  
`expected_act` | `additional.fields` | Merged  
`res_id` | `additional.fields` | Merged  
`status_label` | `additional.fields` | Merged  
`local_date` | `metadata.event_timestamp` | Parsed as `yyyy-MM-d HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`inc_type` | `metadata.event_type` | Mapped: `"10000","10001","10002","40101","40400","40500","40700"` → `SCAN_NETWORK`, `40102` ...  
`inc_type` | `metadata.product_event_type` | Directly mapped  
`inc_id` | `metadata.product_log_id` | Directly mapped  
`agent_ver` | `metadata.product_version` | Directly mapped  
`device_name` | `principal.asset.hostname` | Directly mapped  
`ip_address` | `principal.asset.ip` | Merged  
`device_name` | `principal.hostname` | Directly mapped  
`status_id` | `principal.investigation.status` | Mapped: `"1","2"` → `NEW`, `"3","4"` → `CLOSED`, `"5","6"` → `REVIEWED`  
`ip_address` | `principal.ip` | Merged  
`group_label` | `principal.user.attribute.labels` | Merged  
`user_ou` | `principal.user.group_identifiers` | Mapped: `^.{0,255}$` → `user_ou`  
`name` | `principal.user.user_display_name` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`sec_action` | `security_result.action` | Merged  
`action` | `security_result.action_details` | Directly mapped  
`fail_reason` | `security_result.description` | Mapped: `0` → `No Failure`  
`encryption_label` | `security_result.detection_fields` | Merged  
`usb_label` | `security_result.detection_fields` | Merged  
`volume_label` | `security_result.detection_fields` | Merged  
`rule_set_label` | `security_result.rule_labels` | Merged  
`rule_name` | `security_result.rule_name` | Directly mapped  
`sev` | `security_result.severity` | Mapped values (5 total, for example `1` → `INFORMATIONAL`, `2` → `ERROR`, `3` → `LOW`)  
`sev` | `security_result.severity_details` | Directly mapped  
`dst_app` | `target.application` | Directly mapped  
`dst` | `target.asset.hostname` | Directly mapped  
`file` | `target.file.full_path` | Directly mapped  
`file_size` | `target.file.size` | Renamed/mapped  
`dst` | `target.hostname` | Directly mapped  
`process_name` | `target.process.file.full_path` | Directly mapped  
`dst_url` | `target.url` | Directly mapped  
`dst` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `SCAN_NETWORK`  
N/A | `metadata.product_name` | Constant: `Mcafee DLP`  
N/A | `metadata.vendor_name` | Constant: `Mcafee`  
N/A | `principal.investigation.status` | Constant: `NEW`  
N/A | `security_result.description` | Constant: `No Failure`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
`dst` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`device_name` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-dlp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
