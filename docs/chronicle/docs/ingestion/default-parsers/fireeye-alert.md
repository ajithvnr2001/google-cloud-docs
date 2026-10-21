---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-alert/
title: Collect Trellix (formerly FireEye) alert logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:25.229548+00:00
---

# Collect Trellix (formerly FireEye) alert logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix (formerly FireEye) alert logs

**Parser Version:** 10.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix (formerly known as FireEye) alert logs to Google Security Operations using the Bindplane agent.

Trellix is a network security platform that detects advanced threats, malware, and zero-day exploits. It generates alert logs for detected threats, malicious activity, and security events in CEF, JSON, and XML formats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Trellix appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Trellix appliance with administrator permissions



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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
            chronicle/fireeye_alert:
                compression: gzip
                creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FIREEYE_ALERT
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/fireeye_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/fireeye_alert
        




### Configuration parameters

Replace the following placeholders:

**Receiver configuration:**

  * `tcplog`: The receiver type based on protocol: 
    * `udplog` for UDP syslog
    * `tcplog` for TCP syslog
  * `0.0.0.0`: IP address to listen on: 
    * `0.0.0.0` to listen on all interfaces (recommended)
    * Specific IP address to listen on one interface
  * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)



**Exporter configuration:**

  * `fireeye_alert`: Descriptive name for the exporter
  * `creds_file_path`: Full path to ingestion authentication file: 
    * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * `<customer_id>`: Customer ID from the previous step
  * `endpoint`: Regional endpoint URL: 
    * **US** : `malachiteingestion-pa.googleapis.com`
    * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
    * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
    * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
  * `FIREEYE_ALERT`: Log type exactly as it appears in Google SecOps
  * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)



**Pipeline configuration:**

  * `fireeye_to_chronicle`: Descriptive name for the pipeline



### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

  * To restart the Bindplane agent in Windows, choose one of the following options:

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Services console:

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:
             
             ```cmd
             sc query observiq-otel-collector
             ```
             

      5. Check logs for errors:
             
             ```cmd
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             ```
             




## Configure FireEye syslog forwarding

FireEye (Trellix) appliances forward alerts as rsyslog notifications. Configure them either from the appliance web UI or from the appliance command-line interface. Both methods produce the same result, so use whichever suits your operations model.

**Note:** The Google SecOps parser for this log type reads CEF, JSON, and key-value syslog messages. Select **CEF** (recommended) or **JSON** as the notification format. The parser contains no handling for **LEEF** , **CSV** , or **XML**. **Text** is also unsuitable, because a message that matches none of the parser's syslog patterns and carries no key-value pairs is discarded as unsupported.

### Method 1: Configure rsyslog notifications using the web UI

  1. Sign in to the **FireEye** appliance web UI with an account that has Admin or Operator access.
  2. Go to **Settings > Notifications**.
  3. Select the **RSYSLOG** tab.
  4. Optional: In the **Rsyslog Settings** area, set the values that servers configured as **Default** inherit, and then click **Apply Settings** : 
     * **Default format** : Select **CEF**.
     * **Default delivery** : Select **Per Event**.
     * **Default send as** : Select **Alert**.
  5. Under **View and add Rsyslog Servers** , click **Add Rsyslog Server**.
  6. Provide the following configuration details: 
     * **Server Name** : Enter a descriptive name for the entry (for example, `secops-bindplane`).
     * **IP Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Enabled** : Select the checkbox so that the appliance sends notifications to this server.
     * **Delivery** : Select **Per Event** to send a notification each time an alert is generated.
     * **Notification** : Select **All Events** , or select the specific alert types you want to forward.
     * **Format** : Select **CEF**. If you select **JSON** instead, also select a detail level of **Normal** , **Concise** , or **Extended**.
     * **Send as** : Select **Alert**.
     * **Protocol** : Select **TCP** to match the `tcplog` receiver configured earlier. Select **UDP** , which is the appliance default, only if you changed the receiver to `udplog`.
  7. Click **Add New Rsyslog Server**.

**Note:** The web UI has no port setting. The appliance sends notifications to the standard syslog port (`514`), so configure the Bindplane agent receiver to listen on port `514`. To use a different port, set it from the CLI with `fenotify rsyslog trap-sink <sink_name> port <port_number>`, as described in Method 2.



### Method 2: Configure rsyslog notifications using the CLI

  1. Sign in to the FireEye appliance command-line interface with an account that has Admin or Operator access.
  2. Enter configuration mode:
         
         hostname > enable
         hostname # configure terminal
         

  3. Activate rsyslog notifications:
         
         hostname (config) # fenotify rsyslog enable
         

  4. Create a trap sink for the Bindplane agent and enable it:
         
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane enable
         

**Note:** The trap sink name is a short label without spaces that identifies the destination. Reuse the same name in every command that follows.
  5. Set the destination address, the transport protocol, and the port:
         
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane address <BINDPLANE_IP>
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane protocol tcp
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane port 514
         

     * `<BINDPLANE_IP>`: The IP address or domain name of the Bindplane agent host.
**Note:** Use `tcp` to match the `tcplog` receiver configured earlier, or `udp` if you changed the receiver to `udplog`. Set `port` to the port that the receiver listens on.
  6. Set the message format, the delivery schedule, and the severity:
         
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane prefer message format cef
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane prefer message delivery per-event
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane prefer message send-as alert
         

     * `prefer message format`: Use `cef`. For JSON, use `json-normal`, `json-concise`, or `json-extended`. Don't use `csv`, `leef`, or any `text-` or `xml-` value.
     * `prefer message delivery`: Use `per-event` to send information about each event when the event is triggered.
     * `prefer message send-as`: Use `alert`, which is severity 1.
  7. Select which alerts generate a notification for this trap sink:
         
         hostname (config) # fenotify rsyslog trap-sink secops-bindplane prefer notification all-events
         

     * `all-events`: All events except riskware.
     * `all-riskware`: The `riskware-object` and `riskware-callback` events.
     * Individual types: `domain-match`, `infection-match`, `malware-callback`, `malware-object`, `riskware-callback`, `riskware-object`, `web-infection`, and `ips-event` on IPS-enabled appliances.
  8. Save the configuration:
         
         hostname (config) # write memory
         




### Verify the configuration

  1. To review the active rsyslog settings, run the following command in enable mode:
         
         hostname # show fenotify rsyslog
         

The output lists the global **Configuration** values, the enabled **Alerts** types, and the per-server **Consumers** values.

  2. To generate a test event from the web UI, go to **Settings > Notifications**, select an event type in the drop-down list below the table, and then click **Test-Fire**.

  3. To generate a test event from the CLI instead, run the following command in configuration mode:
         
         hostname (config) # fenotify test-fire <EVENT_TYPE>
         

  4. Confirm that the Bindplane agent host receives the messages, and then confirm that the events appear in Google SecOps.

**Note:** In deployments managed by a Central Management (CM) appliance, you can configure the rsyslog notifications on the CM appliance. For more information, see [Setting up rsyslog servers using the Web UI](https://docs.trellix.com/bundle/cm_11.x_sag/page/UUID-1c48cbd1-b3dd-4f13-123f-737abab2e92e.html).**Note:** On Trellix Endpoint Security (HX) appliances, the same **Settings > Notifications > rsyslog** page is used, but the layout differs: select the **Event type** checkbox, type the server name in the **Add Rsyslog Server** column, click **Add Rsyslog Server** , enter the address in the **IP Address** column, and then click **Update**. For more information, see [Configure Trellix Endpoint Security (HX)](https://docs.trellix.com/bundle/enterprise-security-manager-data-source-configuration-guide/page/UUID-af8cf44f-ce22-848a-e8ac-f5ce103c139a.html).



For the vendor procedures that these steps follow, see [Adding system log servers using the Web UI](https://docs.trellix.com/bundle/nx_10.x_ug/page/UUID-3d5908b3-66c7-29be-9572-f4e1d5a15aae.html), [Adding system log servers using the CLI](https://docs.trellix.com/bundle/nx_10.x_ug/page/UUID-ad6b2341-5559-4c4c-2ddc-43be103bb560.html), [Customizing system log server notifications using the CLI](https://docs.trellix.com/bundle/nx_10.x_ug/page/UUID-972cb083-1d76-8d38-e015-5062056b5509.html), and [Testing IPS event notifications](https://docs.trellix.com/bundle/nx_10.0.0_ips/page/UUID-24cc5c7e-a7cf-ff64-48be-b2e84d0391ce.html). For the full syntax and the accepted values of every `fenotify rsyslog` command, see the [CLI Command Reference](https://docs.trellix.com/bundle/cli_cr/page/UUID-600699ad-6f5d-363b-02e6-ee6b3303ead2.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_source` | `additional.fields` | Merged  
`appliance_id_label` | `additional.fields` | Merged  
`appliance_id_label_2nd` | `additional.fields` | Merged  
`appliance_label` | `additional.fields` | Merged  
`begin_label` | `additional.fields` | Merged  
`cache_control_label` | `additional.fields` | Merged  
`channel_label` | `additional.fields` | Merged  
`content_length_label` | `additional.fields` | Merged  
`content_type_label` | `additional.fields` | Merged  
`cost_label` | `additional.fields` | Merged  
`end_label` | `additional.fields` | Merged  
`match_count_label` | `additional.fields` | Merged  
`msg_label` | `additional.fields` | Merged  
`success_label` | `additional.fields` | Merged  
`dvc` | `intermediary.asset.hostname` | Directly mapped  
`dvc` | `intermediary.asset.ip` | Merged  
`msg` | `intermediary.email` | Directly mapped  
`dvc` | `intermediary.hostname` | Directly mapped  
`sensor` | `intermediary.hostname` | Directly mapped  
`dvc` | `intermediary.ip` | Merged  
`intermediary_host` | `intermediary.labels` | Merged  
`dvcmac` | `intermediary.mac` | Merged  
`desc` | `metadata.description` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`name` | `metadata.description` | Directly mapped  
`alert.occurred` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSS`  
`end` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss ZZZ`  
`rt` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss ZZZ`  
`start` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss ZZZ`  
`event_type` | `metadata.event_type` | Mapped: `filewriteevent` → `FILE_MODIFICATION`, `"processevent","urlmonitorevent"` → `SCAN_P...  
`event_type1` | `metadata.event_type` | Directly mapped  
`file_event_subtype` | `metadata.event_type` | Mapped: `FILE_OPERATION_CLOSED` → `SCAN_PROCESS`  
`has_email_info` | `metadata.event_type` | Mapped: `true` → `EMAIL_TRANSACTION`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `EMAIL_TRANSACTION`, `true` → `STATUS_UPDATE`  
`type` | `metadata.event_type` | Mapped: `"Event::Endpoint::UpdateSuccess","Event::Endpoint::UpdateFailure"` → `STATUS_UPDATE`  
`event_type` | `metadata.product_event_type` | Directly mapped  
`type` | `metadata.product_event_type` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`product` | `metadata.product_name` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`applicationProtocol` | `network.application_protocol` | Directly mapped  
`ver_proto` | `network.application_protocol` | Mapped: `HTTP/1.1` → `HTTP`  
`alert.src.smtp-mail-from` | `network.email.from` | Directly mapped  
`mails` | `network.email.to` | Merged  
`httpmethod` | `network.http.method` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`urlMonitorEvent_urlMethod` | `network.http.method` | Directly mapped  
`User-Agent` | `network.http.parsed_user_agent` | Renamed/mapped  
`http_user_agent` | `network.http.parsed_user_agent` | Renamed/mapped  
`Referer` | `network.http.referral_url` | Directly mapped  
`urlMonitorEvent_requestUrl` | `network.http.referral_url` | Directly mapped  
`User-Agent` | `network.http.user_agent` | Directly mapped  
`http_user_agent` | `network.http.user_agent` | Directly mapped  
`urlMonitorEvent_userAgent` | `network.http.user_agent` | Directly mapped  
`alert.explanation.cnc-services.cnc-service.protocol` | `network.ip_protocol` | Directly mapped  
`alert.explanation.protocol` | `network.ip_protocol` | Directly mapped  
`ver_proto` | `network.tls.version_protocol` | Directly mapped  
`devicePayloadId` | `principal.application` | Directly mapped  
`process` | `principal.application` | Directly mapped  
`principal_hostname` | `principal.asset.hostname` | Directly mapped  
`sourceDnsDomain` | `principal.asset.hostname` | Directly mapped  
`agent_info.primary_ip_address` | `principal.asset.ip` | Merged  
`alert.src.ip` | `principal.asset.ip` | Merged  
`host_name` | `principal.asset.ip` | Directly mapped  
`source_info.ip` | `principal.asset.ip` | Merged  
`src` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`type` | `principal.asset.ip` | Mapped: `"Event::Endpoint::UpdateSuccess","Event::Endpoint::UpdateFailure"` → `source_info.ip`  
`vulnerability` | `principal.asset.vulnerabilities` | Merged  
`path` | `principal.file.full_path` | Directly mapped  
`alert.explanation.os-changes.file.processinfo.md5sum` | `principal.file.md5` | Directly mapped  
`alert.explanation.os-changes.file.processinfo.sha1sum` | `principal.file.sha1` | Directly mapped  
`filesize` | `principal.file.size` | Directly mapped  
`Host` | `principal.hostname` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`sourceDnsDomain` | `principal.hostname` | Directly mapped  
`agent_info.primary_ip_address` | `principal.ip` | Merged  
`alert.src.ip` | `principal.ip` | Merged  
`host_name` | `principal.ip` | Directly mapped  
`source_info.ip` | `principal.ip` | Merged  
`src` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`type` | `principal.ip` | Mapped: `"Event::Endpoint::UpdateSuccess","Event::Endpoint::UpdateFailure"` → `source_info.ip`  
`prinicipal_vlan` | `principal.labels` | Merged  
`country` | `principal.location.country_or_region` | Directly mapped  
`agent_info.primary_mac` | `principal.mac` | Merged  
`alert.src.mac` | `principal.mac` | Merged  
`appliance-id` | `principal.mac` | Merged  
`smac` | `principal.mac` | Merged  
`os_platform` | `principal.platform` | Mapped: `"linux","LINUX","lin"` → `LINUX`, `"windows","WINDOWS","win"` → `WINDOWS`, `"mac","...  
`os_kernel_version` | `principal.platform_patch_level` | Directly mapped  
`alert.explanation.os-changes.osinfo` | `principal.platform_version` | Directly mapped  
`alert.src.port` | `principal.port` | Directly mapped  
`src_port` | `principal.port` | Directly mapped  
`alert.explanation.os-changes.file.processinfo.ppid` | `principal.process.parent_process.pid` | Directly mapped  
`alert.explanation.os-changes.file.processinfo.pid` | `principal.process.pid` | Directly mapped  
`process_id` | `principal.process.pid` | Directly mapped  
`id` | `principal.resource.id` | Directly mapped  
`email` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `email`  
`s_result` | `security_result` | Merged  
`sec_result` | `security_result` | Merged  
`alert_smtp_header` | `security_result.about.labels` | Merged  
`alert_smtp_last_malware` | `security_result.about.labels` | Merged  
`alert_smtp_queue_id` | `security_result.about.labels` | Merged  
`alert_smtp_subject` | `security_result.about.labels` | Merged  
`endpoint_type_label` | `security_result.about.labels` | Merged  
`type` | `security_result.about.labels` | Mapped: `"Event::Endpoint::UpdateSuccess","Event::Endpoint::UpdateFailure"` → `endpoint_type...  
`proto` | `security_result.about.network.application_protocol` | Directly mapped  
`http_method` | `security_result.about.network.http.method` | Directly mapped  
`alert.smtp-message.id` | `security_result.about.resource.id` | Directly mapped  
`alert.src.url` | `security_result.about.url` | Directly mapped  
`temp_url` | `security_result.about.url` | Directly mapped  
`action` | `security_result.action` | Merged  
`alert.action` | `security_result.action_details` | Directly mapped  
`threat_attribution` | `security_result.action_details` | Directly mapped  
`category` | `security_result.category` | Merged  
`category_details` | `security_result.category_details` | Merged  
`group` | `security_result.category_details` | Merged  
`indicator.category` | `security_result.category_details` | Merged  
`type` | `security_result.category_details` | Mapped: `"Event::Endpoint::UpdateSuccess","Event::Endpoint::UpdateFailure"` → `group`  
`act` | `security_result.description` | Directly mapped  
`indicator.name` | `security_result.description` | Directly mapped  
`ack_field` | `security_result.detection_fields` | Merged  
`analysis_field` | `security_result.detection_fields` | Merged  
`attack_mode_label` | `security_result.detection_fields` | Merged  
`build_field` | `security_result.detection_fields` | Merged  
`bytes_available_label` | `security_result.detection_fields` | Merged  
`chunk_id_label` | `security_result.detection_fields` | Merged  
`chunk_len_label` | `security_result.detection_fields` | Merged  
`chunks_label` | `security_result.detection_fields` | Merged  
`classtype_label` | `security_result.detection_fields` | Merged  
`cn1_label` | `security_result.detection_fields` | Merged  
`cnc_service_type` | `security_result.detection_fields` | Merged  
`cs1_label` | `security_result.detection_fields` | Merged  
`cs3_label` | `security_result.detection_fields` | Merged  
`cs4_label` | `security_result.detection_fields` | Merged  
`data_label` | `security_result.detection_fields` | Merged  
`detection_infection_type` | `security_result.detection_fields` | Merged  
`display_msg_label` | `security_result.detection_fields` | Merged  
`dpt_label` | `security_result.detection_fields` | Merged  
`flex_string1_Label` | `security_result.detection_fields` | Merged  
`flex_string1_label` | `security_result.detection_fields` | Merged  
`flex_string2_Label` | `security_result.detection_fields` | Merged  
`flex_string2_label` | `security_result.detection_fields` | Merged  
`header` | `security_result.detection_fields` | Merged  
`id_field` | `security_result.detection_fields` | Merged  
`job_id_label` | `security_result.detection_fields` | Merged  
`mode_field` | `security_result.detection_fields` | Merged  
`mvx_status_label` | `security_result.detection_fields` | Merged  
`qid_label` | `security_result.detection_fields` | Merged  
`request_label` | `security_result.detection_fields` | Merged  
`retroactive_field` | `security_result.detection_fields` | Merged  
`sc_version_field` | `security_result.detection_fields` | Merged  
`sequence_field` | `security_result.detection_fields` | Merged  
`sig_id_label` | `security_result.detection_fields` | Merged  
`sig_name_label` | `security_result.detection_fields` | Merged  
`sig_revision_label` | `security_result.detection_fields` | Merged  
`spt_label` | `security_result.detection_fields` | Merged  
`sub_id_label` | `security_result.detection_fields` | Merged  
`tests_downloaded_at_field` | `security_result.detection_fields` | Merged  
`tests_executed_at_field` | `security_result.detection_fields` | Merged  
`tests_name_field` | `security_result.detection_fields` | Merged  
`tests_original_field` | `security_result.detection_fields` | Merged  
`tests_sha512_field` | `security_result.detection_fields` | Merged  
`tests_sid_field` | `security_result.detection_fields` | Merged  
`tests_stype_field` | `security_result.detection_fields` | Merged  
`tests_submitted_at_field` | `security_result.detection_fields` | Merged  
`tests_type_field` | `security_result.detection_fields` | Merged  
`tid_label` | `security_result.detection_fields` | Merged  
`timestamp_field` | `security_result.detection_fields` | Merged  
`url_field` | `security_result.detection_fields` | Merged  
`value_field` | `security_result.detection_fields` | Merged  
`written_size_label` | `security_result.detection_fields` | Merged  
`alert.uuid` | `security_result.rule_id` | Directly mapped  
`alert.version` | `security_result.rule_version` | Directly mapped  
`severity` | `security_result.severity` | Mapped: `"low","NOTICE"` → `LOW`, `INFO` → `INFORMATIONAL`, `medium` → `MEDIUM`, `high` → `H...  
`action_taken` | `security_result.summary` | Directly mapped  
`risk_summary` | `security_result.summary` | Directly mapped  
`alert.id` | `security_result.threat_id` | Directly mapped  
`alert.name` | `security_result.threat_name` | Directly mapped  
`ele.infection.infection-name` | `security_result.threat_name` | Directly mapped  
`threat_name` | `security_result.threat_name` | Directly mapped  
`alert.alert-url` | `security_result.url_back_to_product` | Directly mapped  
`url` | `security_result.url_back_to_product` | Directly mapped  
`dst_hostname` | `target.asset.hostname` | Directly mapped  
`dvchost` | `target.asset.hostname` | Directly mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`alert.dst.ip` | `target.asset.ip` | Merged  
`dst` | `target.asset.ip` | Merged  
`dst_ip` | `target.asset.ip` | Merged  
`urlMonitorEvent_remoteIpAddress` | `target.asset.ip` | Merged  
`alert.explanation.os-changes.file.processinfo.imagepath` | `target.file.full_path` | Directly mapped  
`file_fullpath` | `target.file.full_path` | Directly mapped  
`fname` | `target.file.full_path` | Directly mapped  
`agent_info.md5values` | `target.file.md5` | Directly mapped  
`ele.action.actioned-object.file-object.md5sum` | `target.file.md5` | Directly mapped  
`file_md5` | `target.file.md5` | Directly mapped  
`fileType` | `target.file.mime_type` | Directly mapped  
`ele.action.actioned-object.file-object.sha1sum` | `target.file.sha1` | Directly mapped  
`ele.action.actioned-object.file-object.sha256sum` | `target.file.sha256` | Directly mapped  
`fileHash` | `target.file.sha256` | Directly mapped  
`file_size` | `target.file.size` | Directly mapped  
`fsize` | `target.file.size` | Directly mapped  
`dst_hostname` | `target.hostname` | Directly mapped  
`dvchost` | `target.hostname` | Directly mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`alert.dst.ip` | `target.ip` | Merged  
`dst` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`urlMonitorEvent_remoteIpAddress` | `target.ip` | Merged  
`alert.explanation.cnc-services.cnc-service.location` | `target.location.country_or_region` | Directly mapped  
`alert.dst.mac` | `target.mac` | Merged  
`dmac` | `target.mac` | Merged  
`alert.dst.port` | `target.port` | Directly mapped  
`dst_port` | `target.port` | Renamed/mapped  
`urlMonitorEvent_remotePort` | `target.port` | Directly mapped  
`cmd` | `target.process.command_line` | Directly mapped  
`ele.action.actioned-object.file-object.file-path` | `target.process.file.full_path` | Directly mapped  
`file_event_filepath` | `target.process.file.full_path` | Directly mapped  
`process_event_process_path` | `target.process.file.full_path` | Directly mapped  
`process_path` | `target.process.file.full_path` | Directly mapped  
`urlMonitorEvent_processPath` | `target.process.file.full_path` | Directly mapped  
`md5sum_data` | `target.process.file.md5` | Directly mapped  
`process_md5` | `target.process.file.md5` | Renamed/mapped  
`sha1_data` | `target.process.file.sha1` | Directly mapped  
`sha256_data` | `target.process.file.sha256` | Directly mapped  
`file_event_actor_process_path` | `target.process.parent_process.file.full_path` | Directly mapped  
`parent_process_path` | `target.process.parent_process.file.full_path` | Directly mapped  
`process_event_parent_path` | `target.process.parent_process.file.full_path` | Directly mapped  
`file_event_actor_process_pid` | `target.process.parent_process.pid` | Directly mapped  
`parent_process_pid` | `target.process.parent_process.pid` | Directly mapped  
`process_event_parentPid` | `target.process.parent_process.pid` | Directly mapped  
`alert.explanation.os-changes.file.processinfo.tid` | `target.process.pid` | Directly mapped  
`process_event_pid` | `target.process.pid` | Directly mapped  
`process_pid` | `target.process.pid` | Directly mapped  
`urlMonitorEvent_pid` | `target.process.pid` | Directly mapped  
`scanned_registry_key` | `target.registry.registry_key` | Directly mapped  
`scanned_registry_value` | `target.registry.registry_value_data` | Directly mapped  
`customer_id` | `target.resource.id` | Directly mapped  
`alert.explanation.cnc-services.cnc-service.url` | `target.url` | Directly mapped  
`email` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `email`  
`tar_email` | `target.user.email_addresses` | Merged  
`file_event_actor_process_username` | `target.user.user_display_name` | Directly mapped  
`process_event_username` | `target.user.user_display_name` | Directly mapped  
`urlMonitorEvent_username` | `target.user.user_display_name` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `FIREEYE_ALERT`  
N/A | `metadata.vendor_name` | Constant: `FIREEYE_ALERT`  
N/A | `network.application_protocol` | Constant: `SMTP`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `security_result.about.resource.type` | Constant: `Email`  
N/A | `security_result.confidence` | Constant: `HIGH_CONFIDENCE`  
N/A | `security_result.severity` | Constant: `LOW`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-alert-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
