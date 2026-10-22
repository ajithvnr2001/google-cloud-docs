---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ribbon-analytics-platform/
title: Collect Ribbon Analytics Platform logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:08.791338+00:00
---

# Collect Ribbon Analytics Platform logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ribbon-analytics-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Ribbon Analytics Platform logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Ribbon Analytics Platform logs to Google Security Operations using the Bindplane agent.

Ribbon Analytics Platform is a network analytics and session border controller platform for voice and data communications monitoring. It generates syslog messages for call detail records, session events, and system health information.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Ribbon Analytics Platform
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Ribbon Analytics Platform management interface



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
          chronicle/ribbon_analytics:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: RIBBON_ANALYTICS_PLATFORM
            raw_log_field: body
        
        service:
          pipelines:
            logs/ribbon_analytics_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/ribbon_analytics
        




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
          chronicle/ribbon_analytics:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: RIBBON_ANALYTICS_PLATFORM
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
             




## Configure Ribbon Analytics Platform syslog forwarding

  1. Sign in to the **Ribbon** management interface.
  2. Go to **Settings > Remote Log Servers**.
  3. Add a new remote log server with the following configuration: 
     * **Host** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
  4. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`type_name` | `about` | Mapped: `SYSCALL` → `about`  
`type_syscall_props.AUID` | `about.user.user_display_name` | Directly mapped  
`type_syscall_props.auid` | `about.user.userid` | Directly mapped  
`additional_delay_data` | `additional.fields` | Merged  
`additional_delays_data` | `additional.fields` | Merged  
`additional_dns_data` | `additional.fields` | Merged  
`additional_field` | `additional.fields` | Merged  
`additional_relay_data` | `additional.fields` | Merged  
`auth_realm_field` | `additional.fields` | Merged  
`log_details_label` | `additional.fields` | Merged  
`_mechanism` | `extensions.auth.mechanism` | Merged  
`audit_message` | `extensions.auth.type` | Mapped: `type=(SYSCALL/LOGIN/USER_LOGIN/USER_CMD/USER_ACCT/USER_ROLE_CHANGE/USER _START/USER_...  
`msg2` | `extensions.auth.type` | Mapped: `login failure` → `MACHINE`  
`type_name` | `extensions.auth.type` | Mapped: `USER_LOGIN` → `MACHINE`, `"LOGIN", "USER_START", "USER_AUTH", "CRED_ACQ", "CRED_REF...  
`dvc` | `intermediary.hostname` | Directly mapped  
`dvc` | `intermediary.ip` | Merged  
`description` | `metadata.description` | Directly mapped  
`error_message` | `metadata.description` | Directly mapped  
`msg2` | `metadata.description` | Directly mapped  
`event_timestamp` | `metadata.event_timestamp` | Parsed as `UNIX`  
`timestamp` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`event_type` | `metadata.event_type` | Mapped: `GENERIC_EVENT` → `STATUS_UPDATE`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`msg2` | `metadata.event_type` | Mapped: `HTTP` → `NETWORK_HTTP`, `login failure` → `USER_LOGIN`  
`target_user_present` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`type_name` | `metadata.event_type` | Mapped: `SYSCALL` → `USER_UNCATEGORIZED`  
`applica` | `metadata.product_event_type` | Directly mapped  
`audit_message` | `metadata.product_event_type` | Mapped values (6 total, e.g. `pam_krb5.*authentication fails for` → `PAM_KRB5_AUTH_ERROR`, `...  
`eventType` | `metadata.product_event_type` | Directly mapped  
`p_event_type` | `metadata.product_event_type` | Directly mapped  
`type` | `metadata.product_event_type` | Directly mapped  
`type_name` | `metadata.product_event_type` | Directly mapped  
`jsonPayload._AUDIT_ID` | `metadata.product_log_id` | Directly mapped  
`product_log_id` | `metadata.product_log_id` | Directly mapped  
`audit_message` | `network.application_protocol` | Mapped: `type=(CRYPTO_SESSION/CRYPTO_KEY_USER)` → `SSH`  
`auth` | `network.application_protocol` | Mapped: `ssh` → `SSH`  
`message` | `network.application_protocol` | Mapped: `ssh/ssh2` → `SSH`  
`tty` | `network.application_protocol` | Mapped: `ssh` → `SSH`  
`audit_message` | `network.direction` | Mapped: `type=(CRYPTO_SESSION/CRYPTO_KEY_USER)` → `OUTBOUND`, `type=(CRYPTO_SESSION/CRYPTO_K...  
`mailid` | `network.email.mail_id` | Directly mapped  
`to_email` | `network.email.to` | Mapped: `^.+@.+$` → `to_email`  
`response_code` | `network.http.response_code` | Directly mapped  
`audit_message` | `network.ip_protocol` | Mapped: `type=(CRYPTO_SESSION/CRYPTO_KEY_USER)` → `TCP`  
`bytes_sent` | `network.sent_bytes` | Directly mapped  
`type_crypto_props.ksize` | `network.sent_bytes` | Renamed/mapped  
`jsonPayload._AUDIT_SESSION` | `network.session_id` | Directly mapped  
`sessionid` | `network.session_id` | Directly mapped  
`type_anom_props.ses` | `network.session_id` | Renamed/mapped  
`type_syscall_props.ses` | `network.session_id` | Directly mapped  
`type_crypto_props.cipher` | `network.tls.cipher` | Directly mapped  
`type_crypto_props.pfs` | `network.tls.curve` | Directly mapped  
`applica` | `principal.application` | Directly mapped  
`jsonPayload._COMM` | `principal.application` | Directly mapped  
`type_anom_props.comm` | `principal.application` | Directly mapped  
`type_syscall_props.comm` | `principal.application` | Directly mapped  
`type_syscall_props.terminal` | `principal.application` | Directly mapped  
`%{rhost}` | `principal.asset.hostname` | Merged  
`rhost` | `principal.asset.hostname` | Mapped when `kvdata` != ``  
`princi_ip` | `principal.asset.ip` | Merged  
`rhost` | `principal.asset.ip` | Merged  
`srcIp` | `principal.asset.ip` | Mapped: `^(?:(25[0-5]/2[0-4][0-9]/1[0-9]{2}/[1-9]?[0-9]).){3}(25[0-5]/2[0-4][0-9]/1[0-9]{2}...  
`%{rhost}` | `principal.hostname` | Merged  
`jsonPayload._HOSTNAME` | `principal.hostname` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`rhost` | `principal.hostname` | Mapped when `kvdata` != ``  
`audit_message` | `principal.ip` | Mapped: `type=(SYSCALL/LOGIN/USER_LOGIN/USER_CMD/USER_ACCT/USER_ROLE_CHANGE/USER _START/USER_...  
`prin_ip` | `principal.ip` | Merged  
`princi_ip` | `principal.ip` | Merged  
`rhost` | `principal.ip` | Merged  
`srcIp` | `principal.ip` | Mapped: `^(?:(25[0-5]/2[0-4][0-9]/1[0-9]{2}/[1-9]?[0-9]).){3}(25[0-5]/2[0-4][0-9]/1[0-9]{2}...  
`type_crypto_props.laddr` | `principal.ip` | Merged  
`srcPort` | `principal.port` | Renamed/mapped  
`type_crypto_props.lport` | `principal.port` | Renamed/mapped  
`auth` | `principal.process.command_line` | Directly mapped  
`proctitle_value` | `principal.process.command_line` | Directly mapped  
`type_syscall_props.cmd` | `principal.process.command_line` | Directly mapped  
`event.idm.read_only_udm.target.process.file.full_path` | `principal.process.file.full_path` | Directly mapped  
`proctitle_value` | `principal.process.file.full_path` | Directly mapped  
`audit_message` | `principal.process.file.names` | Mapped: `type=(SYSCALL/LOGIN/USER_LOGIN/USER_CMD/USER_ACCT/USER_ROLE_CHANGE/USER _START/USER_...  
`filename` | `principal.process.file.names` | Merged  
`jsonPayload._PPID` | `principal.process.parent_process.pid` | Directly mapped  
`type_syscall_props.ppid` | `principal.process.parent_process.pid` | Directly mapped  
`jsonPayload._PID` | `principal.process.pid` | Directly mapped  
`pi` | `principal.process.pid` | Directly mapped  
`process_pid` | `principal.process.pid` | Directly mapped  
`type_crypto_props.spid` | `principal.process.pid` | Directly mapped  
`type_syscall_props.pid` | `principal.process.pid` | Directly mapped  
`email` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `email`  
`user_name` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `user_name`  
`type_syscall_props.UID` | `principal.user.user_display_name` | Directly mapped  
`type_syscall_props.acct` | `principal.user.user_display_name` | Directly mapped  
`jsonPayload._AUDIT_FIELD_SUID` | `principal.user.userid` | Directly mapped  
`principal_user_userid` | `principal.user.userid` | Directly mapped  
`ruser` | `principal.user.userid` | Directly mapped  
`type_crypto_props.suid` | `principal.user.userid` | Directly mapped  
`user_name` | `principal.user.userid` | Directly mapped  
`usr` | `principal.user.userid` | Directly mapped  
`a0_label` | `security_result.about.labels` | Merged  
`a1_label` | `security_result.about.labels` | Merged  
`a2_label` | `security_result.about.labels` | Merged  
`a3_label` | `security_result.about.labels` | Merged  
`audit_message` | `security_result.about.labels` | Mapped values (7 total, e.g. `type=(SYSCALL/LOGIN/USER_LOGIN/USER_CMD/USER_ACCT/USER_ROLE_CH...  
`exit_label` | `security_result.about.labels` | Merged  
`syscall_label` | `security_result.about.labels` | Merged  
`tty_label` | `security_result.about.labels` | Merged  
`jsonPayload._AUDIT_FIELD_ARCH` | `security_result.about.platform_version` | Directly mapped  
`type_syscall_props.arch` | `security_result.about.platform_version` | Directly mapped  
`type_syscall_props.key` | `security_result.about.registry.registry_key` | Directly mapped  
`product_log_id` | `security_result.about.registry.registry_value_data` | Directly mapped  
`action` | `security_result.action` | Merged  
`action_data` | `security_result.action` | Mapped: `"authentication failure", "Authentication failure", "Failed password", "Connection ...  
`audit_message` | `security_result.action` | Mapped: `type=(SYSCALL/LOGIN/USER_LOGIN/USER_CMD/USER_ACCT/USER_ROLE_CHANGE/USER _START/USER_...  
`security_action` | `security_result.action` | Merged  
`action_data` | `security_result.action_details` | Directly mapped  
`auth` | `security_result.action_details` | Mapped: `sshd` → `FAILURE`  
`status` | `security_result.action_details` | Directly mapped  
`type_crypto_props.res` | `security_result.action_details` | Renamed/mapped  
`type_syscall_props.res` | `security_result.action_details` | Directly mapped  
`a0_label` | `security_result.detection_fields` | Merged  
`a1_label` | `security_result.detection_fields` | Merged  
`a2_label` | `security_result.detection_fields` | Merged  
`a3_label` | `security_result.detection_fields` | Merged  
`audit_message` | `security_result.detection_fields` | Mapped: `type=(SYSCALL/LOGIN/USER_LOGIN/USER_CMD/USER_ACCT/USER_ROLE_CHANGE/USER _START/USER_...  
`auid_field` | `security_result.detection_fields` | Merged  
`auth` | `security_result.detection_fields` | Mapped: `sshd` → `authentication_protocol_field`, `sshd` → `authentication_mechanism_field`,...  
`authentication_mechanism_field` | `security_result.detection_fields` | Merged  
`authentication_protocol_field` | `security_result.detection_fields` | Merged  
`bootid_label` | `security_result.detection_fields` | Merged  
`connection_state_field` | `security_result.detection_fields` | Merged  
`cwd_field` | `security_result.detection_fields` | Merged  
`exit_label` | `security_result.detection_fields` | Merged  
`jsonPayload._AUDIT_TYPE_NAME` | `security_result.rule_id` | Directly mapped  
`type_name` | `security_result.rule_id` | Directly mapped  
`msg_desc` | `security_result.summary` | Directly mapped  
`secsummary` | `security_result.summary` | Directly mapped  
`type_anom_props.reason` | `security_result.summary` | Directly mapped  
`type_syscall_props.op` | `security_result.summary` | Directly mapped  
`type_syscall_props.res` | `security_result.summary` | Directly mapped  
`type_syscall_props.success` | `security_result.summary` | Directly mapped  
`type_path1_props.name` | `src.file.full_path` | Renamed/mapped  
`type_crypto_props.terminal` | `target.application` | Renamed/mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`type_crypto_props.hostname` | `target.asset.hostname` | Directly mapped  
`dst_ip` | `target.asset.ip` | Merged  
`resource.labels.project_id` | `target.cloud.project.name` | Directly mapped  
`filepath` | `target.file.full_path` | Directly mapped  
`jsonPayload._AUDIT_FIELD_FILE` | `target.file.full_path` | Directly mapped  
`target_file_full_path` | `target.file.full_path` | Directly mapped  
`jsonPayload._AUDIT_FIELD_HASH` | `target.file.sha256` | Directly mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`type_crypto_props.hostname` | `target.hostname` | Directly mapped  
`audit_message` | `target.ip` | Mapped: `type=(CRYPTO_SESSION/CRYPTO_KEY_USER)` → `tar_ip`  
`dst_ip` | `target.ip` | Merged  
`tar_ip` | `target.ip` | Merged  
`resource.labels.location` | `target.location.name` | Directly mapped  
`dst_port` | `target.port` | Directly mapped  
`target_port` | `target.port` | Directly mapped  
`type_crypto_props.rport` | `target.port` | Renamed/mapped  
`args` | `target.process.command_line` | Renamed/mapped  
`cmnd` | `target.process.command_line` | Directly mapped  
`command_line` | `target.process.command_line` | Directly mapped  
`cwd` | `target.process.file.full_path` | Directly mapped  
`jsonPayload._EXE` | `target.process.file.full_path` | Directly mapped  
`proctitle_value` | `target.process.file.full_path` | Directly mapped  
`type_anom_props.exe` | `target.process.file.full_path` | Renamed/mapped  
`type_crypto_props.exe` | `target.process.file.full_path` | Renamed/mapped  
`type_syscall_props.exe` | `target.process.file.full_path` | Directly mapped  
`type_anom_props.pid` | `target.process.pid` | Renamed/mapped  
`type_crypto_props.pid` | `target.process.pid` | Renamed/mapped  
`resource.labels.cluster_name` | `target.resource.name` | Directly mapped  
`audit_message` | `target.resource.type` | Mapped: `type=(SYSCALL/LOGIN/USER_LOGIN/USER_CMD/USER_ACCT/USER_ROLE_CHANGE/USER _START/USER_...  
`type_name` | `target.resource.type` | Mapped: `"USER_ACCT", "USER_ROLE_CHANGE","USER_MGMT"` → `SETTING`  
`target_email` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `target_email`  
`type_syscall_props.ID` | `target.user.user_display_name` | Directly mapped  
`type_syscall_props.acct` | `target.user.user_display_name` | Directly mapped  
`event.idm.read_only_udm.principal.user.userid` | `target.user.userid` | Renamed/mapped  
`jsonPayload._UID` | `target.user.userid` | Directly mapped  
`type_crypto_props.uid` | `target.user.userid` | Directly mapped  
`type_syscall_props.acct` | `target.user.userid` | Directly mapped  
`type_syscall_props.id` | `target.user.userid` | Directly mapped  
`type_syscall_props.uid` | `target.user.userid` | Directly mapped  
`user_name` | `target.user.userid` | Directly mapped  
`username` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `metadata.product_event_type` | Constant: `PAM_KRB5_AUTH_ERROR`  
N/A | `metadata.product_name` | Constant: `AuditD`  
N/A | `metadata.vendor_name` | Constant: `Linux`  
N/A | `network.application_protocol` | Constant: `SSH`  
N/A | `network.direction` | Constant: `OUTBOUND`  
N/A | `network.ip_protocol` | Constant: `TCP`  
N/A | `principal.platform` | Constant: `LINUX`  
N/A | `principal.user.userid` | Constant: `event.idm.read_only_udm.target.user.userid`  
N/A | `security_result.action_details` | Constant: `FAILURE`  
N/A | `target.resource.type` | Constant: `SETTING`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ribbon-analytics-platform-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
