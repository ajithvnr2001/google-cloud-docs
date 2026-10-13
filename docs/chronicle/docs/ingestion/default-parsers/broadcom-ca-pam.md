---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ca-pam/
title: Collect Broadcom CA PAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:40.856077+00:00
---

# Collect Broadcom CA PAM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-ca-pam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Broadcom CA PAM logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Broadcom CA Privileged Access Manager logs to Google Security Operations using Bindplane. Broadcom CA Privileged Access Manager (PAM) is an enterprise privileged access management solution that controls, monitors, and audits privileged user access to critical systems. It provides credential vaulting, session recording, and access policy enforcement across hybrid environments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Broadcom Privileged Access Management web UI.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agent**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.



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

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             tcplog:
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/broadcom_ca_pam:
                 compression: gzip
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 customer_id: '<customer_id>'
                 endpoint: malachiteingestion-pa.googleapis.com
                 log_type: BROADCOM_CA_PAM
                 raw_log_field: body
                 ingestion_labels:
         
         service:
             pipelines:
                 logs/broadcom_ca_pam:
                     receivers:
                         - tcplog
                     exporters:
                         - chronicle/broadcom_ca_pam
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<customer_id>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the authentication file was saved in the Get Google SecOps ingestion authentication file section.



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
         




## Configure remote syslog on Broadcom CA PAM

  1. Sign in to the **Privileged Access Management** web UI.
  2. Go to **Configuration > Logs > Syslog**.
  3. Select the **Syslog Enabled** toggle.
  4. Select **Space Delimited** from the **Message Format** list.
  5. Click **Add Server**.
  6. Provide the following configuration details in the new row:

     * **Server** : Enter the Bindplane agent IP address (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or your configured Bindplane agent port). If you leave the port blank, it defaults to `514`.
     * **Protocol** : Select **TCP**.
**Note:** If you select **TCP** , the **TLS** option becomes available. Enable TLS if your environment requires encrypted syslog transport.
  7. Click **Update** to save the settings.

  8. Verify that logs are being sent by checking the Bindplane agent logs.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`UserGroup_label` | `additional.fields` | Merged  
`access_protocol` | `metadata.access_protocol` | Directly mapped  
`Details` | `metadata.description` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `SCAN_UNCATEGORIZED`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`host` | `principal.asset.hostname` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`NatIP` | `principal.nat_ip` | Merged  
`Port` | `principal.port` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`DeviceName` | `principal.resource.name` | Directly mapped  
`User` | `principal.user.userid` | Directly mapped  
`sec_res` | `security_result` | Merged  
`detection_fields` | `security_result.detection_fields` | Merged  
`Service_App` | `target.application` | Directly mapped  
`Address` | `target.asset.hostname` | Directly mapped  
`Address` | `target.hostname` | Directly mapped  
N/A | `metadata.event_type` | Constant: `SCAN_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Broadcom CA Pam`  
N/A | `metadata.vendor_name` | Constant: `Broadcom`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/broadcom-ca-pam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
