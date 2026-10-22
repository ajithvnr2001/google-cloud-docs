---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pta/
title: Collect CyberArk Privileged Threat Analytics logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:09.857702+00:00
---

# Collect CyberArk Privileged Threat Analytics logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CyberArk Privileged Threat Analytics logs

**Parser Version:** 18.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CyberArk Privileged Threat Analytics logs to Google Security Operations using Bindplane. CyberArk Privileged Threat Analytics (PTA) is a security solution that detects and responds to malicious activities involving privileged accounts. It uses advanced analytics and machine learning to monitor, analyze, and flag abnormal behaviors that may indicate potential insider threats or compromised credentials.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the CyberArk Privileged Threat Analytics server.



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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/cyberark_pta:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: 'CYBERARK_PTA'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/cyberark_pta_to_chronicle:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/cyberark_pta
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<CUSTOMER_ID>` with the actual customer ID.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cyberark_pta:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'CYBERARK_PTA'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure CyberArk Privileged Threat Analytics syslog forwarding

  1. Sign in to the **Privileged Threat Analytics** server.
  2. Run the **DEFAULTPARM** command to open the default `systemparm.properties` file.
  3. Copy the line containing the `syslog_outbound` property and exit the `systemparm.properties` file.
  4. Run the **LOCALPARM** command to open the local `systemparm.properties` file.
  5. Press `i` on the keyboard to edit the file.
  6. In the `systemparm.properties` file, uncomment the `syslog_outbound` property.
  7. Paste the line that you copied and edit the parameters according to the following example:
         
         syslog_outbound=[{"siem": "Chronicle", "format": "CEF", "host": "BINDPLANE_IP", "port": BINDPLANE_PORT, "protocol": "TCP"}]
         

     * Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.
     * Replace `BINDPLANE_PORT` with the port number configured in the Bindplane agent (for example, `514`).
  8. Save the configuration file and close it.

  9. Restart the **Privileged Threat Analytics** server to apply the changes.




For more information, see the [CyberArk Privileged Threat Analytics documentation](https://docs.cyberark.com/PAS/latest/en/Content/PTA/Outbound-Sending-%20PTA-syslog-Messages-to-SIEM.htm).

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`src` | `principal.ip` | Direct mapping from `src` field.  
`dst` | `target.ip` | Direct mapping from `dst` field.  
`suser` | `principal.user.userid` | Direct mapping from `suser` field.  
`duser` | `target.user.userid` | Direct mapping from `duser` field.  
`cs1` | `security_result.description` | Direct mapping from `cs1` field (reason).  
`cs2` | `additional.fields` | Direct mapping from `cs2` field (station).  
`act` | `security_result.action_details` | Direct mapping from `act` field (action taken).  
`cat` | `metadata.product_event_type` | Direct mapping from `cat` field (event category).  
`severity` | `security_result.severity` | Mapped from CEF severity value.  
`deviceCustomDate1` | `metadata.event_timestamp` | Parsed from `deviceCustomDate1` field.  
| `metadata.vendor_name` | Set to `CyberArk`.  
| `metadata.product_name` | Set to `Privileged Threat Analytics`.  
| `metadata.log_type` | Set to `CYBERARK_PTA`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-pta-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
