---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-trap/
title: Collect Proofpoint Threat Response (TRAP) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:25.946946+00:00
---

# Collect Proofpoint Threat Response (TRAP) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-trap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint Threat Response (TRAP) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint Threat Response (TRAP) logs to Google Security Operations using the Bindplane agent.

Proofpoint Threat Response Auto-Pull (TRAP) is a security orchestration platform for automated threat response and remediation. It integrates with email, endpoint, and network security tools to accelerate incident investigation and containment.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Proofpoint TRAP server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Proofpoint TRAP management console with administrator permissions



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/proofpoint_trap:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: PROOFPOINT_TRAP
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/trap_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/proofpoint_trap
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: Receives syslog over TCP. Use `udplog` if you configure UDP transport in TRAP.
    * `0.0.0.0:514`: Listens on all interfaces on port 514. Change the port if needed (for example, `1514` for non-root Linux).
  * **Exporter configuration:**

    * `<CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<CUSTOMER_ID>`: Customer ID from the **Get Google SecOps customer ID** step.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/proofpoint_trap:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: PROOFPOINT_TRAP
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
             




## Configure Proofpoint TRAP syslog forwarding

  1. Sign in to the **Proofpoint TRAP** management console (typically at `https://trap-server:8080`).
  2. Navigate to **Monitoring > Logging**.
  3. Configure the syslog destination: 
     * **Host** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Severity** : Select the minimum severity level for log forwarding.
  4. Click **Save**.
  5. Verify that logs are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_field` | `additional.fields` | Merged  
`additional_modulesRun` | `additional.fields` | Merged  
`alternateGraphApiEndpoint_additional` | `additional.fields` | Merged  
`azureAdAuthEndpoint_additional` | `additional.fields` | Merged  
`clientId_additional` | `additional.fields` | Merged  
`clientSecret_additional` | `additional.fields` | Merged  
`disposition_additional_data` | `additional.fields` | Merged  
`disposition_data_available` | `additional.fields` | Mapped: `true` → `disposition_additional_data`  
`exchangeAPI_additional` | `additional.fields` | Merged  
`exchangeAuthType_additional` | `additional.fields` | Merged  
`graphApiEndpoint_additional` | `additional.fields` | Merged  
`headers_X-Forefront-Antispam-Report` | `additional.fields` | Merged  
`headers_accept_lang_label` | `additional.fields` | Merged  
`headers_authentication_results_label` | `additional.fields` | Merged  
`headers_content_language_label` | `additional.fields` | Merged  
`headers_content_transfer_encoding_label` | `additional.fields` | Merged  
`headers_content_type_label` | `additional.fields` | Merged  
`headers_date_label` | `additional.fields` | Merged  
`headers_message_id_label` | `additional.fields` | Merged  
`headers_mime_version_label` | `additional.fields` | Merged  
`headers_received_label` | `additional.fields` | Merged  
`headers_return_path_label` | `additional.fields` | Merged  
`headers_thread_index_label` | `additional.fields` | Merged  
`headers_thread_topic_label` | `additional.fields` | Merged  
`headers_x_ms_exchange_antispam_feedbackprocessing_scenario_label` | `additional.fields` | Merged  
`headers_x_ms_exchange_antispam_feedcategory_label` | `additional.fields` | Merged  
`headers_x_ms_exchange_antispam_feedtype_label` | `additional.fields` | Merged  
`headers_x_ms_exchange_organization_antispam_feedcategory_label` | `additional.fields` | Merged  
`incident_display_id_label` | `additional.fields` | Merged  
`incident_id_label` | `additional.fields` | Merged  
`incident_link_attribute_label` | `additional.fields` | Merged  
`incident_title_label` | `additional.fields` | Merged  
`privateKey_additional` | `additional.fields` | Merged  
`source_type_additional_data` | `additional.fields` | Merged  
`source_type_data_available` | `additional.fields` | Mapped: `true` → `source_type_additional_data`  
`sourcesData_name_label` | `additional.fields` | Merged  
`sourcesData_type_label` | `additional.fields` | Merged  
`sources_id_label` | `additional.fields` | Merged  
`sources_type_label` | `additional.fields` | Merged  
`tap_threat_additional_data` | `additional.fields` | Merged  
`tap_threat_data_available` | `additional.fields` | Mapped: `true` → `tap_threat_additional_data`  
`tenantId_additional` | `additional.fields` | Merged  
`url_list` | `additional.fields` | Merged  
`auth_details` | `extensions.auth.auth_details` | Directly mapped  
`proofpoint_trap_host` | `intermediary.hostname` | Directly mapped  
`proofpoint_trap_host` | `intermediary.ip` | Merged  
`url_label` | `intermediary.labels` | Merged  
`desc` | `metadata.description` | Directly mapped  
`createdAt` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`created_at` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`data.received` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event1.description.created_at` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event1.description.updated_at` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`eventTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`received` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`ts` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`updatedAt` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`application` | `metadata.event_type` | Mapped: `CROND` → `PROCESS_UNCATEGORIZED`, `system-modules.authlookup` → `USER_LOGIN`  
`has_network_email` | `metadata.event_type` | Mapped: `true` → `EMAIL_TRANSACTION`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `EMAIL_TRANSACTION`  
`event1.description.id` | `metadata.product_log_id` | Directly mapped  
`event_id` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`has_principal` | `metadata.product_name` | Mapped: `true` → `PROOFPOINT_TRAP`  
`source` | `metadata.product_name` | Directly mapped  
`has_principal` | `metadata.vendor_name` | Mapped: `true` → `PROOFPOINT`  
`attackDirection` | `network.direction` | Mapped: `inbound` → `INBOUND`, `outbound` → `OUTBOUND`  
`cc` | `network.email.cc` | Mapped: `^.+@.+$` → `cc`  
`emaildata.sender.email` | `network.email.from` | Directly mapped  
`event1.description.headers.From` | `network.email.from` | Directly mapped  
`fromadd` | `network.email.from` | Directly mapped  
`principal_user2` | `network.email.from` | Directly mapped  
`send_email` | `network.email.from` | Directly mapped  
`sender_address` | `network.email.from` | Directly mapped  
`email_id` | `network.email.mail_id` | Directly mapped  
`event1.description.messageid` | `network.email.mail_id` | Directly mapped  
`messageID` | `network.email.mail_id` | Directly mapped  
`event1.description.headers.Reply-To` | `network.email.reply_to` | Directly mapped  
`reply` | `network.email.reply_to` | Directly mapped  
`email_subject` | `network.email.subject` | Merged  
`emaildata.subject` | `network.email.subject` | Merged  
`event1.description.subject` | `network.email.subject` | Merged  
`index` | `network.email.subject` | Mapped: `0` → `emaildata.subject`  
`subject` | `network.email.subject` | Merged  
`emaildata.recipient.email` | `network.email.to` | Merged  
`event1.description.headers.To` | `network.email.to` | Merged  
`index` | `network.email.to` | Mapped: `0` → `emaildata.recipient.email`, `0` → `to_email`  
`principal_user1` | `network.email.to` | Merged  
`recipient_address` | `network.email.to` | Mapped: `^.+@.+$` → `recipient_address`  
`to` | `network.email.to` | Mapped: `^.+@.+$` → `to`  
`to_email` | `network.email.to` | Merged  
`http_method` | `network.http.method` | Directly mapped  
`http_url` | `network.http.referral_url` | Directly mapped  
`ses_id` | `network.session_id` | Directly mapped  
`application` | `principal.application` | Directly mapped  
`senderIP` | `principal.asset.ip` | Merged  
`sender_IP` | `principal.asset.ip` | Merged  
`msgparts.md5` | `principal.file.md5` | Directly mapped  
`msgparts.filename` | `principal.file.names` | Merged  
`msgparts.sha256` | `principal.file.sha1` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`senderIP` | `principal.ip` | Merged  
`sender_IP` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`file_name` | `principal.process.file.full_path` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`attachment_label` | `principal.resource.attribute.labels` | Merged  
`title_label` | `principal.resource.attribute.labels` | Merged  
`ewsUrl` | `principal.url` | Directly mapped  
`principal_link` | `principal.url` | Directly mapped  
`sender_vap_label` | `principal.user.attribute.labels` | Merged  
`emaildata.sender.email` | `principal.user.email_addresses` | Merged  
`index` | `principal.user.email_addresses` | Mapped: `0` → `emaildata.sender.email`  
`principal_user1` | `principal.user.email_addresses` | Merged  
`principal_user2` | `principal.user.email_addresses` | Merged  
`sender` | `principal.user.email_addresses` | Merged  
`assignedUserName` | `principal.user.user_display_name` | Directly mapped  
`username` | `principal.user.user_display_name` | Directly mapped  
`assignedUserId` | `principal.user.userid` | Directly mapped  
`principal_user1` | `principal.user.userid` | Directly mapped  
`principal_user2` | `principal.user.userid` | Directly mapped  
`sender_email` | `principal.user.userid` | Directly mapped  
`src_user` | `principal.user.userid` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`index` | `security_result` | Mapped: `0` → `sec_res2`  
`sec_res` | `security_result` | Merged  
`sec_res2` | `security_result` | Merged  
`sec_result` | `security_result` | Merged  
`state` | `security_result.alert_state` | Mapped: `"OPEN", "IN_PROGRESS"` → `ALERTING`, `CLOSED` → `NOT_ALERTING`  
`QID_field` | `security_result.detection_fields` | Merged  
`alert_type_label` | `security_result.detection_fields` | Merged  
`body_label` | `security_result.detection_fields` | Merged  
`body_type_label` | `security_result.detection_fields` | Merged  
`cluster_label` | `security_result.detection_fields` | Merged  
`completelyRewritten_field` | `security_result.detection_fields` | Merged  
`disposition_label` | `security_result.detection_fields` | Merged  
`dkim1_label` | `security_result.detection_fields` | Merged  
`dkim2_label` | `security_result.detection_fields` | Merged  
`dkim3_label` | `security_result.detection_fields` | Merged  
`dmarc_label` | `security_result.detection_fields` | Merged  
`event_id_label` | `security_result.detection_fields` | Merged  
`header_d1_label` | `security_result.detection_fields` | Merged  
`header_d2_label` | `security_result.detection_fields` | Merged  
`header_d3_label` | `security_result.detection_fields` | Merged  
`header_from_label` | `security_result.detection_fields` | Merged  
`header_s1_label` | `security_result.detection_fields` | Merged  
`header_s2_label` | `security_result.detection_fields` | Merged  
`header_s3_label` | `security_result.detection_fields` | Merged  
`impostorScore_field` | `security_result.detection_fields` | Merged  
`index` | `security_result.detection_fields` | Mapped: `0` → `messageId_label`  
`key_data` | `security_result.detection_fields` | Merged  
`mailfrom_label` | `security_result.detection_fields` | Merged  
`malwareScore_field` | `security_result.detection_fields` | Merged  
`messageId_label` | `security_result.detection_fields` | Merged  
`messageSize_field` | `security_result.detection_fields` | Merged  
`phishScore_field` | `security_result.detection_fields` | Merged  
`quarantineFolder_label` | `security_result.detection_fields` | Merged  
`quarantineRule_label` | `security_result.detection_fields` | Merged  
`spamScore_field` | `security_result.detection_fields` | Merged  
`spf_label` | `security_result.detection_fields` | Merged  
`state_label` | `security_result.detection_fields` | Merged  
`severity` | `security_result.severity` | Mapped: `Info` → `INFORMATIONAL`  
`severity` | `security_result.severity_details` | Directly mapped  
`state` | `security_result.summary` | Directly mapped  
`cmd` | `target.process.command_line` | Directly mapped  
`pwd` | `target.process.file.full_path` | Directly mapped  
`recipient_vap_label` | `target.user.attribute.labels` | Merged  
`email` | `target.user.email_addresses` | Merged  
`emaildata.abuseReporterAddress` | `target.user.email_addresses` | Merged  
`index` | `target.user.email_addresses` | Mapped: `0` → `emaildata.abuseReporterAddress`  
`recipient_email` | `target.user.email_addresses` | Merged  
`dst_user` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `EMAIL_TRANSACTION`  
N/A | `metadata.product_name` | Constant: `PROOFPOINT_TRAP`  
N/A | `metadata.vendor_name` | Constant: `PROOFPOINT`  
N/A | `network.application_protocol` | Constant: `HTTP`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `security_result.alert_state` | Constant: `ALERTING`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
`received_at` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`sources.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`created_at` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`received_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`titlePII` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pps_guid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`email_recipient_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`email_message_size` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`remediation_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tap_false_positive` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`abuse_reporter_rank` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`quarantine_strategy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mime_content_expired` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mime_content_present` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`click_block_exclusive` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`remediation_status_context` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`last_known_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`clear_confidence` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message_status.is_read` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message_status.permitted_clicks` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message_status.message_delivered` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sender_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tenant_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`created_at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`message_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`updated_at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`disposition` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`received_at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tap_cleared` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`body_expired` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`body_present` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`clear_verdict` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tap_threat_types` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`incident.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`incident.title` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`incident.display_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`incident.link_attribute` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sender_address` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
`email_id` | `event.idm.read_only_udm.network.email.mail_id` | Mapped from changelog  
`email_subject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`recipient_address` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`assignedUserName` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`assignedUserId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`state` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`createdAt` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`updatedAt` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`tenantId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`closedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`displayId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`assignedTeamName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`assignedTeamId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`messageCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vap` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vip` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`commentCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dispositions` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sourceTypes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sourcesData` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`state` | `event.idm.read_only_udm.security_result.alert_state` | Mapped from changelog  
`event1.description.messageid` | `event.idm.read_only_udm.network.email.mail_id` | Mapped from changelog  
`event1.description.sender.email` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`event1.description.recipient.email` | `event.idm.read_only_udm.target.user.email_addresses` | Mapped from changelog  
`event1.description.subject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`event1.description.created_at` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`event1.description.updated_at` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`event1.description.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`event1.description.headers.From` | `event.idm.read_only_udm.sec_result.detection_fields` | Mapped from changelog  
`event1.description.headers.To` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`event1.description.headers.Reply-To` | `event.idm.read_only_udm.network.email.reply_to` | Mapped from changelog  
`event1.description.headers.Received-SPF` | `event.idm.read_only_udm.sec_result.description` | Mapped from changelog  
`event1.description.headers.DKIM-Signature` | `event.idm.read_only_udm.sec_result.detection_fields` | Mapped from changelog  
`event1.description.sender.vap` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`event1.description.recipient.vap` | `event.idm.read_only_udm.target.user.attribute.labels` | Mapped from changelog  
`event1.description.hosts.url` | `event.idm.read_only_udm.intermediary.labels` | Mapped from changelog  
`event1.description.urls` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`event1.description.severity` | `event.idm.read_only_udm.sec_result.severity` | Mapped from changelog  
`event1.description.state` | `event.idm.read_only_udm.sec_result.summary` | Mapped from changelog  
`mailfrom", "spf", "dkim1", "header_s1", "header_d1", "dkim2", "header_s2", "header_d2", and "dmarc` | `security_result.detection_fields` | Mapped from changelog  
`users` | `principal.user.userid` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-trap-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
