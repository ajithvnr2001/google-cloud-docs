---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aide/
title: Collect AIDE (Advanced Intrusion Detection Environment) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:23.054031+00:00
---

# Collect AIDE (Advanced Intrusion Detection Environment) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AIDE (Advanced Intrusion Detection Environment) logs 

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AIDE (Advanced Intrusion Detection Environment) logs to Google Security Operations using Bindplane. AIDE is a file integrity monitoring tool that detects changes to files on Linux/Unix systems.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Linux host with systemd running AIDE version 0.18 or later (for JSON format support)
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the AIDE configuration files



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

Install the Bindplane agent on your Linux operating system according to the following instructions.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux.
     * Open the file using a text editor (for example, `nano` or `vi`).
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
             log_type: 'AIDE'
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
            log_type: 'AIDE'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart observiq-otel-collector
        




## Configure Syslog forwarding on AIDE

  1. Open the AIDE configuration file:
         
         sudo vi /etc/aide/aide.conf
         

  2. Go to the reporting section.

  3. Add the following configuration:

     * **report_level** : Enter `list_entries`.
     * **report_format** : Enter `json` (for AIDE 0.18+) or `plain`.
     * **report_url** : Enter `syslog:authpriv`.

Example configuration:
    
    ```ini
    report_level=list_entries
    report_format=json
    report_url=syslog:authpriv
    ```
    

  4. Save the configuration.

  5. Configure rsyslog to forward AIDE logs to the Bindplane agent. Open the rsyslog configuration:
         
         sudo vi /etc/rsyslog.d/aide-forward.conf
         

  6. Add the following configuration to forward `authpriv` facility logs to the Bindplane agent:
         
         authpriv.* @<BINDPLANE_AGENT_IP>:514
         

     * Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.
     * Use `@` for UDP or `@@` for TCP forwarding.
  7. Restart rsyslog:
         
         sudo systemctl restart rsyslog
         

  8. Initialize the AIDE database if this is a fresh installation:
         
         sudo aide --init
         sudo mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db
         

  9. Test the configuration:
         
         sudo aide --check
         

  10. Set up automated checks using cron:
         
         sudo crontab -e
         

  11. Add the following line to run AIDE daily at 04:05 AM:
         
         05 4 * * * root /usr/sbin/aide --check
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`added_label` | `principal.asset.attribute.labels` | Merged  
`changed_label` | `principal.asset.attribute.labels` | Merged  
`old_acl_label` | `principal.asset.attribute.labels` | Merged  
`old_md5_label` | `principal.asset.attribute.labels` | Merged  
`old_perms_label` | `principal.asset.attribute.labels` | Merged  
`old_sha256_label` | `principal.asset.attribute.labels` | Merged  
`old_ts_label` | `principal.asset.attribute.labels` | Merged  
`removed_label` | `principal.asset.attribute.labels` | Merged  
`total_label` | `principal.asset.attribute.labels` | Merged  
`file_path` | `principal.file.full_path` | Directly mapped  
`path` | `principal.file.full_path` | Directly mapped  
`old_size` | `principal.file.size` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`sr` | `security_result` | Merged  
`new_acl_label` | `target.asset.attribute.labels` | Merged  
`new_md5_label` | `target.asset.attribute.labels` | Merged  
`new_perms_label` | `target.asset.attribute.labels` | Merged  
`new_sha256_label` | `target.asset.attribute.labels` | Merged  
`new_ts_label` | `target.asset.attribute.labels` | Merged  
`path` | `target.file.full_path` | Directly mapped  
`new_size` | `target.file.size` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `AIDE`  
N/A | `metadata.vendor_name` | Constant: `AIDE`  
N/A | `principal.application` | Constant: `aide`  
N/A | `principal.file.size` | Constant: `sizedata`  
N/A | `target.file.size` | Constant: `sizedata_target`  
`total_files", "added_files", "removed_files", "changed_files", "old_timestamp", "old_perms", "old_sha256", "old_md5", and "old_acl` | `principal.asset.attribute.labels` | Mapped from changelog  
`new_timestamp", "new_perms", "new_sha256", "new_md5", and "new_acl` | `target.asset.attribute.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aide-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
