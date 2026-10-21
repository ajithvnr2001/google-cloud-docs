---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/voltage/
title: Collect Voltage logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:31:28.656510+00:00
---

# Collect Voltage logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/voltage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Voltage logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Voltage SecureMail logs to Google Security Operations using the Bindplane agent.

Voltage SecureMail is an email encryption platform that generates syslog messages for email encryption/decryption events, policy enforcement, and administrative actions.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Voltage SecureMail server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Voltage SecureMail Management Console



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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/voltage:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VOLTAGE
            raw_log_field: body
        
        service:
          pipelines:
            logs/voltage_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/voltage
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/voltage:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VOLTAGE
            raw_log_field: body
        


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

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure syslog in Voltage SecureMail

  1. Sign in to the **Voltage SecureMail Management Console**.
  2. Go to **System > Syslog Settings**.
  3. Provide the following configuration details: 
     * **Server Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
     * **Facility** : Select the appropriate syslog facility.
     * **Log Level** : Select the desired log level.
  4. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`attemptedAuthMethods_label` | `additional.fields` | Merged  
`authTokens_label` | `additional.fields` | Merged  
`elapsedTimeMillis_label` | `additional.fields` | Merged  
`isUserPassSet_label` | `additional.fields` | Merged  
`keyId_label` | `additional.fields` | Merged  
`leadingDigits_label` | `additional.fields` | Merged  
`masked_label` | `additional.fields` | Merged  
`merchantId_label` | `additional.fields` | Merged  
`out_label` | `additional.fields` | Merged  
`phaseBit_label` | `additional.fields` | Merged  
`proxyType_label` | `additional.fields` | Merged  
`rollover_label` | `additional.fields` | Merged  
`trailingDigits_label` | `additional.fields` | Merged  
`AuthenticationMethod` | `extensions.auth.mechanism` | Mapped: `USER_PASSWORD` → `mechanism`  
`mechanism` | `extensions.auth.mechanism` | Merged  
`has_principal` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`proxyConnectionIp` | `intermediary.asset.ip` | Merged  
`inter_hostname` | `intermediary.hostname` | Directly mapped  
`proxyConnectionIp` | `intermediary.ip` | Merged  
`description` | `metadata.description` | Directly mapped  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`, `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`prod_event_name` | `metadata.product_event_type` | Directly mapped  
`event_id` | `metadata.product_log_id` | Directly mapped  
`cef_product` | `metadata.product_name` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`request` | `network.http.referral_url` | Directly mapped  
`length` | `network.received_bytes` | Directly mapped  
`requestTimeMillis` | `network.session_duration.nanos` | Directly mapped  
`timeMillis` | `network.session_duration.seconds` | Directly mapped  
`sessionid` | `network.session_id` | Directly mapped  
`cvProduct` | `observer.application` | Directly mapped  
`cvapi_label` | `observer.labels` | Merged  
`cvdevice_label` | `observer.labels` | Merged  
`cvframework_label` | `observer.labels` | Merged  
`cvos` | `observer.platform` | Mapped: `Li` → `LINUX`, `Win` → `WINDOWS`  
`requestClientApplication` | `principal.application` | Directly mapped  
`src_hostname` | `principal.asset.hostname` | Directly mapped  
`ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`src_hostname` | `principal.hostname` | Directly mapped  
`ip` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`src_port` | `principal.port` | Renamed/mapped  
`identity` | `principal.user.email_addresses` | Mapped: `(.*)@(.*)` → `identity`  
`user` | `principal.user.userid` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`sec_action` | `security_result.action` | Merged  
`msg` | `security_result.description` | Directly mapped  
`CachedAuthentication_label` | `security_result.detection_fields` | Merged  
`acceptBadData_label` | `security_result.detection_fields` | Merged  
`algorithm_label` | `security_result.detection_fields` | Merged  
`authMethodName_label` | `security_result.detection_fields` | Merged  
`authTimeMillis_label` | `security_result.detection_fields` | Merged  
`authType_label` | `security_result.detection_fields` | Merged  
`format_label` | `security_result.detection_fields` | Merged  
`fullIdentity_label` | `security_result.detection_fields` | Merged  
`hsmEnabled_label` | `security_result.detection_fields` | Merged  
`returnEncryptedKeyOption_label` | `security_result.detection_fields` | Merged  
`returnFullIdentity_label` | `security_result.detection_fields` | Merged  
`wrappedMode_label` | `security_result.detection_fields` | Merged  
`severity` | `security_result.severity` | Mapped: `"0", "1", "2"` → `INFORMATIONAL`, `"3", "4"` → `LOW`, `"5", "6"` → `MEDIUM`, `"7", ...  
`severity` | `security_result.severity_details` | Directly mapped  
`district` | `target.administrative_domain` | Directly mapped  
`shost` | `target.asset.hostname` | Directly mapped  
`dst_ip` | `target.asset.ip` | Merged  
`shost` | `target.hostname` | Directly mapped  
`dst_ip` | `target.ip` | Merged  
`cmd_line` | `target.process.command_line` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`path` | `target.resource.name` | Directly mapped  
`tar_user` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `VOLTAGE`  
N/A | `metadata.vendor_name` | Constant: `VOLTAGE`  
N/A | `observer.platform` | Constant: `LINUX`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
`district` | `event.idm.read_only_udm.target.administrative_domain` | Mapped from changelog  
`identity` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`shost` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`requestClientApplication` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`length` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`AuthenticationMethod` | `event.idm.read_only_udm.extensions.auth.mechanism` | Mapped from changelog  
`cvProduct` | `event.idm.read_only_udm.observer.application` | Mapped from changelog  
`cvapi` | `event.idm.read_only_udm.observer.labels` | Mapped from changelog  
`cvframework` | `event.idm.read_only_udm.observer.labels` | Mapped from changelog  
`cvdevice` | `event.idm.read_only_udm.observer.labels` | Mapped from changelog  
`cvos` | `event.idm.read_only_udm.observer.platform` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`proxyConnectionIp` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`:` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`,` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`and` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cached` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`fullIdentity` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`algorithm` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`returnEncryptedKeyOption` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authMethodName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`authTimeMillis` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`hsmEnabled` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`wrappedMode` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`format` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`returnFullIdentity` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`acceptBadData` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`CachedAuthentication` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/voltage-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
