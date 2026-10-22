---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-linux/
title: Collect HP Linux logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:21.371846+00:00
---

# Collect HP Linux logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hp-linux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HP Linux logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HP-UX operating system logs to Google Security Operations using the Bindplane agent.

HP-UX is an enterprise UNIX operating system for HP Integrity and PA-RISC servers. HP-UX system logs capture authentication events, process execution, security audit data, and general system activity. Syslog files are stored locally under `/var/adm/syslog/`.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the HP-UX server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged (root) access to the HP-UX server



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
          chronicle/hp_linux:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: HP_LINUX
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/hpux_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/hp_linux
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `hp_linux`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `HP_LINUX`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `hpux_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/hp_linux:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: HP_LINUX
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
             




## Configure HP-UX syslog forwarding

  1. Sign in to the HP-UX server with root privileges.
  2. Edit the syslog configuration file:
         
         vi /etc/syslog.conf
         

  3. Add the following line to forward all syslog messages to the Bindplane agent:
         
         *.* @<BINDPLANE_AGENT_IP>
         

     * Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.
     * The `@` prefix sends logs via UDP. HP-UX syslog uses UDP by default.
  4. To forward specific facilities only, use individual lines:
         
         auth.*  @<BINDPLANE_AGENT_IP>
         kern.*  @<BINDPLANE_AGENT_IP>
         *.err   @<BINDPLANE_AGENT_IP>
         

  5. Save and close the file.

  6. Restart the syslog daemon to apply the changes:
         
         /sbin/init.d/syslogd stop
         /sbin/init.d/syslogd start
         

  7. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** HP-UX stores syslog data in files such as `/var/adm/syslog/syslog.log`, `/var/adm/syslog/mail.log`, and rotated log files under `/var/adm/syslog/`. The `/var/adm/btmp` and `/var/adm/wtmp` files capture failed login attempts and login/logout records respectively.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`audit_type_label` | `additional.fields` | Merged  
`auth_failures_label` | `additional.fields` | Merged  
`ctladdr_label` | `additional.fields` | Merged  
`da_instance_label` | `additional.fields` | Merged  
`delay_label` | `additional.fields` | Merged  
`dsn_label` | `additional.fields` | Merged  
`event_code_label` | `additional.fields` | Merged  
`mailer_label` | `additional.fields` | Merged  
`msg_id_label` | `additional.fields` | Merged  
`pri_label` | `additional.fields` | Merged  
`raw_severity_label` | `additional.fields` | Merged  
`ssh_version_label` | `additional.fields` | Merged  
`stat_label` | `additional.fields` | Merged  
`suite_label` | `additional.fields` | Merged  
`syslog_priority_label` | `additional.fields` | Merged  
`to_label` | `additional.fields` | Merged  
`tty_label` | `additional.fields` | Merged  
`xdelay_label` | `additional.fields` | Merged  
`process` | `extensions.auth.type` | Mapped: `"sshd", "login"` → `AUTHTYPE_UNSPECIFIED`  
`msg` | `metadata.description` | Directly mapped  
`ts` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`utc` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`event_type` | `metadata.event_type` | Directly mapped  
`action_type` | `metadata.product_event_type` | Directly mapped  
`centrifyEventID` | `metadata.product_log_id` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`message` | `network.application_protocol` | Mapped: `(?i)ssh` → `SSH`  
`proto` | `network.ip_protocol` | Mapped: `tcp` → `TCP`  
`DASessID` | `network.session_id` | Directly mapped  
`process` | `principal.application` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`src_ip` | `principal.asset.ip` | Merged  
`host` | `principal.hostname` | Directly mapped  
`src_ip` | `principal.ip` | Merged  
`src_port` | `principal.port` | Directly mapped  
`p_id` | `principal.process.pid` | Directly mapped  
`principal_user` | `principal.user.userid` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`ruleset` | `security_result.rule_name` | Directly mapped  
`log_level` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`  
`sev` | `security_result.severity` | Mapped: `(?i)ERROR` → `ERROR`  
`log_level` | `security_result.severity_details` | Directly mapped  
`t_domain` | `target.administrative_domain` | Directly mapped  
`t_app` | `target.application` | Directly mapped  
`t_hostname` | `target.asset.hostname` | Directly mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`t_hostname` | `target.hostname` | Directly mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`target_user` | `target.user.userid` | Directly mapped  
`user` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.product_name` | Constant: `HP Linux`  
N/A | `metadata.vendor_name` | Constant: `HP Linux`  
N/A | `network.application_protocol` | Constant: `SSH`  
N/A | `network.ip_protocol` | Constant: `TCP`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hp-linux-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
