---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-dlp/
title: Collect Forcepoint DLP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:47.642694+00:00
---

# Collect Forcepoint DLP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-dlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Forcepoint DLP logs

**Parser Version:** 10.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Forcepoint DLP logs to Google Security Operations using Bindplane.

Forcepoint DLP (Data Loss Prevention) is a data protection solution that identifies, monitors, and protects sensitive data across enterprise environments. It detects and prevents unauthorized data transfers through email, web, endpoints, and cloud applications using content-aware policies and machine learning. The parser extracts fields from Forcepoint DLP CEF formatted logs. It then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Forcepoint Security Manager web console



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
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: 'FORCEPOINT_DLP'
            raw_log_field: body
            ingestion_labels:
        
        service:
          pipelines:
            logs/source0__chronicle_w_labels-0:
              receivers:
                - tcplog
              exporters:
                - chronicle/chronicle_w_labels
        




### Configuration parameters

  * Replace the following placeholders:

    * **Receiver configuration:**

      * `tcplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog
      * `0.0.0.0`: IP address to listen on (`0.0.0.0` to listen on all interfaces)
      * `514`: Port number to listen on (standard syslog port)
    * **Exporter configuration:**

      * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
        * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
        * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
      * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section
      * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
      * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
      * `endpoint`: Keep set to `chronicle.googleapis.com`.
      * `log_type`: Log type exactly as it appears in Chronicle (`FORCEPOINT_DLP`)



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'FORCEPOINT_DLP'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows, choose one of the following options: 

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Services console:

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Forcepoint DLP syslog forwarding

  1. Sign in to the **Forcepoint Security Manager** web console.
  2. Go to **Settings > General > SIEM Integration**.
  3. Select **Enable SIEM integration**.
  4. Provide the following configuration details: 
     * **Syslog Server IP Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
     * **Format** : Select **CEF** (Common Event Format).
     * **TLS Enabled** : Uncheck (unless using TLS).
  5. In the **Incident Data** section, select the data to include in syslog messages: 
     * **Action taken**
     * **Severity**
     * **Policy name**
     * **Source information**
     * **Destination information**
     * **Content details**
  6. Click **OK** to save.
  7. Go to **Main > Policy Management > DLP Policies**.
  8. For each policy that should forward events, verify syslog notification is enabled: 
     1. Select the policy.
     2. Go to the **Action Plan** tab.
     3. Verify the action plan includes **Send to SIEM**.
  9. Click **Deploy** to apply the policy changes.
  10. Verify syslog messages are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
act | security_result.description | If actionPerformed is empty, the value of act is assigned to security_result.description.  
actionID | metadata.product_log_id | The value of actionID is assigned to metadata.product_log_id.  
actionPerformed | security_result.description | The value of actionPerformed is assigned to security_result.description.  
administrator | principal.user.userid | The value of administrator is assigned to principal.user.userid.  
analyzedBy | additional.fields.key | The string "analyzedBy" is assigned to additional.fields.key.  
analyzedBy | additional.fields.value.string_value | The value of analyzedBy is assigned to additional.fields.value.string_value.  
cat | security_result.category_details | The values of cat are merged into the security_result.category_details field as a list.  
destinationHosts | target.hostname | The value of destinationHosts is assigned to target.hostname.  
destinationHosts | target.asset.hostname | The value of destinationHosts is assigned to target.asset.hostname.  
details | security_result.description | If both actionPerformed and act are empty, the value of details is assigned to security_result.description.  
duser | target.user.userid | The value of duser is used to populate target.user.userid. Multiple values separated by "; " are split and assigned as individual email addresses if they match the email regex, otherwise they are treated as user IDs.  
eventId | metadata.product_log_id | If actionID is empty, the value of eventId is assigned to metadata.product_log_id.  
fname | target.file.full_path | The value of fname is assigned to target.file.full_path.  
logTime | metadata.event_timestamp | The value of logTime is parsed and used to populate metadata.event_timestamp.  
loginName | principal.user.user_display_name | The value of loginName is assigned to principal.user.user_display_name.  
msg | metadata.description | The value of msg is assigned to metadata.description.  
productVersion | additional.fields.key | The string "productVersion" is assigned to additional.fields.key.  
productVersion | additional.fields.value.string_value | The value of productVersion is assigned to additional.fields.value.string_value.  
role | principal.user.attribute.roles.name | The value of role is assigned to principal.user.attribute.roles.name.  
severityType | security_result.severity | The value of severityType is mapped to security_result.severity. "high" maps to "HIGH", "med" maps to "MEDIUM", and "low" maps to "LOW" (case-insensitive).  
sourceHost | principal.hostname | The value of sourceHost is assigned to principal.hostname.  
sourceHost | principal.asset.hostname | The value of sourceHost is assigned to principal.asset.hostname.  
sourceIp | principal.ip | The value of sourceIp is added to the principal.ip field.  
sourceIp | principal.asset.ip | The value of sourceIp is added to the principal.asset.ip field.  
sourceServiceName | principal.application | The value of sourceServiceName is assigned to principal.application.  
suser | principal.user.userid | If administrator is empty, the value of suser is assigned to principal.user.userid.  
timestamp | metadata.event_timestamp | The value of timestamp is used to populate metadata.event_timestamp.  
topic | security_result.rule_name | The value of topic is assigned to security_result.rule_name after commas are removed. Hardcoded to "FORCEPOINT_DLP". Hardcoded to "Forcepoint". Extracted from the CEF message. Can be "Forcepoint DLP" or "Forcepoint DLP Audit". Extracted from the CEF message. Concatenation of device_event_class_id and event_name, formatted as "[device_event_class_id] - event_name". Initialized to "GENERIC_EVENT". Changed to "USER_UNCATEGORIZED" if is_principal_user_present is "true".  
`destinationDnsDomain` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`inter_host` | `intermediary.hostname` | Mapped from changelog  
`violationTriggers.VZ CPNI" and "violationTriggers.Controlled Unclassified Information: Portion Marking` | `additional.fields` | Mapped from changelog  
`act` | `security_result.action_details` | Mapped from changelog  
`caseDescription` | `metadata.description` | Mapped from changelog  
`eventIDs` | `metadata.product_event_type` | Mapped from changelog  
`sourceServiceName` | `network.application_protocol` | Mapped from changelog  
`productVersion` | `metadata.product_version` | Mapped from changelog  
`riskScore` | `additional.fields` | Mapped from changelog  
`productVersion" and "analyzedBy` | `additional.fields` | Mapped from changelog  
`timeStamp` | `metadata.event_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-dlp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
