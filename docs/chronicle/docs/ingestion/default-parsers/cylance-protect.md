---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cylance-protect/
title: Collect Arctic Wolf Aurora Endpoint Security (formerly CylancePROTECT) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:21.683800+00:00
---

# Collect Arctic Wolf Aurora Endpoint Security (formerly CylancePROTECT) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cylance-protect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Arctic Wolf Aurora Endpoint Security (formerly CylancePROTECT) logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Arctic Wolf Aurora Endpoint Security (formerly known as CylancePROTECT) logs to Google Security Operations using Bindplane.

Arctic Wolf Aurora Endpoint Security is an AI-driven endpoint protection platform that uses machine learning to prevent malware, scripts, and fileless attacks before they can execute. It provides threat prevention, device control, and script management capabilities to protect endpoints across the organization without relying on traditional signature-based detection methods.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later, or a Linux host with `systemd`.
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open.
  * Privileged access to the CylancePROTECT management console.



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

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/cylance_protect:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: 'CYLANCE_PROTECT'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/cylance_protect_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/cylance_protect
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<customer_id>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cylance_protect:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'CYLANCE_PROTECT'
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
         




## Configure syslog forwarding on CylancePROTECT

  1. Sign in to the **CylancePROTECT** management console.
  2. Go to **Settings** > **Application**.
  3. Select the **Syslog/SIEM** checkbox to enable syslog forwarding.
  4. Select all **events** to forward.
  5. Provide the following configuration details: 
     * **SIEM** : Select **Syslog**.
     * **Protocol** : Select **UDP**.
     * Select the **Allow messages over 2KB** checkbox.
     * **IP/Domain** : Enter the Bindplane agent IP address (for example, `192.168.1.100`).
     * **Port** : Enter `514`.
     * **Facility** : Select the type of application logging.
  6. Click **Test Connection** to verify communication with the Bindplane agent.
  7. Click **Save**.

**Note:** For more information, see the [Arctic Wolf Aurora Endpoint Security documentation](https://docs.blackberry.com/en/unified-endpoint-security/blackberry-ues/setup/setup/Setting-up-Syslog-SIEM).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`logged_on_users` | `about` | Mapped: `()` → `about`  
`domain` | `about.administrative_domain` | Directly mapped  
`username` | `about.user.userid` | Directly mapped  
`event_name` | `extensions.auth.type` | Mapped: `Login` → `MACHINE`  
`event_type` | `extensions.auth.type` | Mapped: `AuditLog` → `MACHINE`  
`cylancehost` | `intermediary.hostname` | Directly mapped  
`int_ip` | `intermediary.ip` | Merged  
`syslogtime` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`event_name` | `metadata.event_type` | Mapped: `Login` → `USER_LOGIN`  
`event_type` | `metadata.event_type` | Mapped values (11 total, e.g. `ScriptControl` → `SCAN_HOST`, `AuditLog` → `USER_LOGIN`, `Dev...  
`event_type` | `network.application_protocol` | Mapped: `OpticsCaeDnsEvent` → `DNS`  
`a` | `network.dns.answers` | Merged  
`event_type` | `network.dns.answers` | Mapped: `OpticsCaeDnsEvent` → `a`  
`event_type` | `network.dns.questions` | Mapped: `OpticsCaeDnsEvent` → `q`  
`q` | `network.dns.questions` | Merged  
`event_type` | `network.ip_protocol` | Mapped: `OpticsCaeNetworkEvent` → `TCP`  
`Source IP` | `principal.ip` | Merged  
`ip_address1` | `principal.ip` | Merged  
`ip_address2` | `principal.ip` | Merged  
`ip_address3` | `principal.ip` | Merged  
`ip_address4` | `principal.ip` | Merged  
`ip_address5` | `principal.ip` | Merged  
`macAddr` | `principal.mac` | Merged  
`OS` | `principal.platform` | Mapped: `Windows` → `WINDOWS`  
`File Name` | `principal.process.file.full_path` | Mapped when `event_type` == `Threat`  
`Path` | `principal.process.file.full_path` | Mapped when `event_type` == `Threat`  
`Process Name` | `principal.process.file.full_path` | Mapped when `event_type` == `ExploitAttempt`  
`instigating_process_name` | `principal.process.file.full_path` | Mapped when `instigating_process_name` != ``  
`instigating_process_sha256` | `principal.process.file.sha256` | Mapped when `instigating_process_sha256` != `unknown`  
`Process ID` | `principal.process.pid` | Mapped when `event_type` == `ExploitAttempt`  
`user_email` | `principal.user.email_addresses` | Merged  
`User Name` | `principal.user.userid` | Mapped when `event_type` == `ExploitAttempt`  
`user_name` | `principal.user.userid` | Mapped when `principal_user` != ``  
`sr_action` | `security_result.action` | Merged  
`sr_category` | `security_result.category` | Merged  
`zone_names` | `security_result.description` | Directly mapped  
`label_detected_by` | `security_result.detection_fields` | Merged  
`rule_label_interpreter` | `security_result.rule_labels` | Merged  
`rule_label_interpreter_version` | `security_result.rule_labels` | Merged  
`Policy Name` | `security_result.rule_name` | Directly mapped  
`Severity` | `security_result.severity` | Directly mapped  
`Cylance Score` | `security_result.severity_details` | Directly mapped  
`Description` | `security_result.summary` | Directly mapped  
`External Device Name` | `security_result.summary` | Directly mapped  
`Violation Type` | `security_result.summary` | Directly mapped  
`event_name` | `security_result.summary` | Directly mapped  
`event_type` | `security_result.summary` | Directly mapped  
`Threat Classification` | `security_result.threat_name` | Directly mapped  
`Violation Type` | `security_result.threat_name` | Directly mapped  
`product_name` | `target.application` | Mapped when `event_type` == `AuditLog`  
`File Path` | `target.file.full_path` | Mapped when `event_type` == `ScriptControl`  
`Device Name` | `target.hostname` | Mapped when `event_type` == `ScriptControl`  
`Destination IP` | `target.ip` | Merged  
`event_type` | `target.ip` | Mapped: `OpticsCaeNetworkEvent` → `Destination IP`  
`Destination Port` | `target.port` | Renamed/mapped  
`Target Process Name` | `target.process.file.full_path` | Mapped when `event_type` == `OpticsCaeProcessEvent`  
`Target Registry KeyPath` | `target.registry.registry_key` | Mapped when `event_type` == `OpticsCaeRegistryEvent`  
N/A | `security_result.severity` | Constant: `HIGH`  
`Target Process Command Line` | `event1.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`Severity` | `event1.idm.read_only_udm.security_result.severity` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cylance-protect-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
