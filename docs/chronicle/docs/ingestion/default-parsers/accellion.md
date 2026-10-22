---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/accellion/
title: Collect Kiteworks (formerly Accellion) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:45.063952+00:00
---

# Collect Kiteworks (formerly Accellion) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/accellion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Kiteworks (formerly Accellion) logs

**Parser Version:** 16.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Kiteworks (formerly known as Accellion) logs to Google Security Operations using Bindplane.

Kiteworks is a secure file sharing and governance platform that provides enterprise content communications across email, file sharing, managed file transfer, and web forms. It delivers visibility, compliance, and control over sensitive content moving in and out of the organization.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Kiteworks appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Kiteworks administration console (System Administrator role)



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
          chronicle/accellion:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: ACCELLION
            raw_log_field: body
        
        service:
          pipelines:
            logs/accellion_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/accellion
        




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
          chronicle/accellion:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ACCELLION
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



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
         




## Configure syslog forwarding on Kiteworks (formerly Accellion)

  1. Sign in to the **Kiteworks** administration console as a System Administrator.
  2. Go to the **Locations** page: 
     * **Legacy admin UI** : Go to **System > Locations**.
     * **New admin UI** : Go to **System Setup > Locations**.
  3. Select the target location from the list.
  4. Go to the **External Services** section.
  5. Expand the **Syslog Settings** panel.
  6. Click **Add** to create a new syslog server configuration.
  7. Provide the following configuration details: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Protocol** : Select **UDP** or **TCP** , depending on your Bindplane agent receiver configuration.
     * **Port** : Enter the Bindplane agent port number (for example, `514`).
     * **Use TLS** : Select this checkbox if you want to transport syslog messages over TLS (available only when **TCP** is selected as the protocol).
     * **Format** : Select **JSON Format** (recommended for structured parsing).
  8. Click **Save** to apply the configuration.

**Note:** Kiteworks syslog exports all data and administrative events including file movements, file access, errors, access control changes, privilege changes, user on/offboarding, failed and successful logins, and scan failures (AV, ATP, DLP).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`acct` | `principal.user.user_display_name` | The value of `acct` from the raw log's `msg` field.  
`acct` | `target.user.user_display_name` | The value of `acct` from the raw log's `msg` field.  
`addr` | `principal.ip` | The value of `addr` from the raw log's `msg` field.  
`a0` | `security_result.about.labels.value` | The value of `a0` from the raw log's `msg` field, where the corresponding `key` is "a0".  
`a1` | `security_result.about.labels.value` | The value of `a1` from the raw log's `msg` field, where the corresponding `key` is "a1".  
`a2` | `security_result.about.labels.value` | The value of `a2` from the raw log's `msg` field, where the corresponding `key` is "a2".  
`a3` | `security_result.about.labels.value` | The value of `a3` from the raw log's `msg` field, where the corresponding `key` is "a3".  
`arch` | `security_result.about.platform_version` | The value of `arch` from the raw log's `msg` field. Only applicable for `type_name` SYSCALL.  
`auid` | `about.user.userid` | The value of `auid` from the raw log's `msg` field.  
`auid` | `security_result.detection_fields.value` | The value of `auid` from the raw log's `msg` field, where the corresponding `key` is "auid".  
`comm` | `principal.application` | The value of `comm` from the raw log's `msg` field.  
`cmd` | `principal.process.command_line` | The value of `cmd` from the raw log's `msg` field.  
`cwd` | `security_result.detection_fields.value` | The value of `cwd` from the raw log's `msg` field, where the corresponding `key` is "cwd".  
`cwd` | `target.process.file.full_path` | The value of `cwd` from the raw log's `msg` field.  
`exe` | `principal.process.file.full_path` | The value of `exe` from the raw log's `msg` field.  
`exe` | `target.process.file.full_path` | The value of `exe` from the raw log's `msg` field.  
`exit` | `security_result.about.labels.value` | The value of `exit` from the raw log's `msg` field, where the corresponding `key` is "Exit Code".  
`hostname` | `principal.hostname` | The value of `hostname` from the raw log's `msg` field.  
`key` | `security_result.about.registry.registry_key` | The value of `key` from the raw log's `msg` field. Only applicable for `type_name` SYSCALL.  
`log_type` | `metadata.log_type` | The value of `log_type` from the raw log.  
`msg` | `security_result.action_details` | The value after `res=` in the `msg` field of the raw log.  
`msg` | `security_result.summary` | Combination of fields from the `msg` field of the raw log. Parsed from the `audit` section of the `msg` field in the raw log. Mapped based on the `type` field in the raw log. For example, "USER_START" maps to "USER_LOGIN", "CRED_DISP" maps to "USER_LOGOUT", "CRED_ACQ" maps to "USER_LOGIN", "USER_END" maps to "USER_LOGOUT", "CRED_REFR" maps to "USER_LOGIN", "USER_CMD" maps to "USER_LOGIN", "CWD" maps to "STATUS_UPDATE", "PROCTITLE" maps to "STATUS_UPDATE", "USER_ACCT" maps to "USER_UNCATEGORIZED", and "SYSCALL" maps to "USER_UNCATEGORIZED".  
`node` | `principal.hostname` | The value of `node` from the raw log's `msg` field.  
`pid` | `principal.process.pid` | The value of `pid` from the raw log's `msg` field.  
`ppid` | `principal.process.parent_process.pid` | The value of `ppid` from the raw log's `msg` field.  
`proctitle` | `target.process.file.full_path` | Decoded hexadecimal value of `proctitle` from the raw log's `msg` field. Hardcoded to "LINUX". Set to "ALLOW" if `res=success` is present in the raw log's `msg` field.  
`ses` | `network.session_id` | The value of `ses` from the raw log's `msg` field.  
`syscall` | `security_result.about.labels.value` | The value of `syscall` from the raw log's `msg` field, where the corresponding `key` is "Syscall".  
`success` | `security_result.summary` | Combined with other fields to form the summary. For SYSCALL events, the logic is: if success=yes, then "yes, The System call succeeded", otherwise "no, The System call failed".  
`terminal` | `principal.terminal` | The value of `terminal` from the raw log's `msg` field.  
`timestamp` | `timestamp` | The value of `timestamp` from the raw log entry.  
`tty` | `principal.terminal` | The value of `tty` from the raw log's `msg` field.  
`type` | `metadata.product_event_type` | The value of `type` from the raw log's `msg` field.  
`uid` | `about.user.userid` | The value of `uid` from the raw log's `msg` field. Only applicable for `type_name` SYSCALL.  
`uid` | `target.user.userid` | The value of `uid` from the raw log's `msg` field. Set to "SETTING" if `type` is "USER_ACCT".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/accellion-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
