---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortianalyzer/
title: Collect Fortinet FortiAnalyzer logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:10:58.197809+00:00
---

# Collect Fortinet FortiAnalyzer logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortianalyzer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet FortiAnalyzer logs

**Parser Version:** 35.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how you can ingest Fortinet FortiAnalyzer logs to Google Security Operations using Bindplane.

Fortinet FortiAnalyzer is a centralized log management, analytics, and reporting platform for Fortinet Security Fabric devices. It aggregates logs from FortiGate firewalls, FortiMail, FortiWeb, FortiSandbox, and other Fortinet products to provide unified visibility, event correlation, and compliance reporting. FortiAnalyzer can forward aggregated logs via syslog to external SIEM platforms for further analysis.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * Network connectivity between the Bindplane agent and the FortiAnalyzer appliance.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Fortinet FortiAnalyzer management console (Super_User or equivalent administrator role).



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agents**.
  3. Download the **Ingestion Authentication File**. 
  4. Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with **root** or **sudo** privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:** `bash sudo nano /opt/observiq-otel-collector/config.yaml`
  * **Windows:** `cmd notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"`



### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            # Replace the port and IP address as required
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/fortianalyzer:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
            # Replace with your actual customer ID from Step 2
            customer_id: 'your-customer-id-here'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: FORTINET_FORTIANALYZER
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/fortianalyzer_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/fortianalyzer
        




### Configuration parameters

  * **Receiver configuration:**
    * `listen_address`: IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces. Change the port if needed (for example, `1514`).
  * **Exporter configuration:**
    * `creds_file_path`: Full path to the ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Your Google SecOps customer ID.
    * `endpoint`: Regional endpoint URL (e.g., `malachiteingestion-pa.googleapis.com`).
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`).



### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`.
  * **Windows** : Click **File** > **Save**.



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
         




## Configure FortiAnalyzer syslog forwarding

Configure FortiAnalyzer to forward logs to the Bindplane agent using syslog output.

### Configure syslog server in FortiAnalyzer

  1. Sign in to the **FortiAnalyzer** web interface.
  2. Go to **System Settings** > **Log Forwarding**.
  3. Click **Create New** to add a new log forwarding rule.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle-Bindplane`).
     * **Status** : Select **Enable**.
     * **Remote Server Type** : Select **Syslog**.
     * **Server IP/FQDN** : Enter the IP address of the Bindplane agent host.
     * **Server Port** : Enter `514` (or the port configured in the Bindplane agent).
     * **Reliable syslog (RFC 6587)** : Select **Enable** to use TCP transport.
     * **Log Forwarding Format** : Select **Default** or **CEF** based on your requirements.
  5. In the **Log Filters** section, configure the log types to forward: 
     * Select the **ADOM** (Administrative Domain) from which to forward logs.
     * Select the device types and log categories to include (Traffic, Event, Security, DNS, SSH, SSL logs).
  6. Click **OK** to save the configuration.



### Verify log forwarding

  1. Go to **System Settings** > **Log Forwarding**.
  2. Verify the forwarding rule shows status as **Enabled**.
  3. Monitor the **Statistics** column to confirm logs are being forwarded.
  4. Verify logs are being received by checking the Bindplane agent logs.

**Note:** For FortiAnalyzer CLI-based configuration, refer to the Fortinet FortiAnalyzer Administration Guide for the `config system log-forward` command.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`devname` | `principal.hostname` | Taken from `devname`.  
`srcip` | `principal.ip` | Taken from `srcip`.  
`srcport` | `principal.port` | Converted to integer.  
`srcintf` | `additional.fields` | Key: `srcintf`.  
`dstip` | `target.ip` | Taken from `dstip`.  
`dstport` | `target.port` | Converted to integer.  
`dstintf` | `additional.fields` | Key: `dstintf`.  
`proto` | `network.ip_protocol` | Mapped (6=TCP, 17=UDP, 1=ICMP).  
`action` | `security_result.action` | `accept/pass` → **ALLOW** ; `deny/drop/block` → **BLOCK**.  
`policyid` | `security_result.rule_id` | Taken from `policyid`.  
`policyname` | `security_result.rule_name` | Taken from `policyname`.  
`user` | `principal.user.userid` | Taken from `user`.  
`app` | `target.application` | Taken from `app`.  
`sentbyte` | `network.sent_bytes` | Converted to unsigned integer.  
`rcvdbyte` | `network.received_bytes` | Converted to unsigned integer.  
`severity` | `security_result.severity` | `information` → **INFORMATIONAL** , `warning` → **MEDIUM** , `error` → **ERROR** , `critical/alert/emergency` → **HIGH**.  
`logid` | `metadata.product_log_id` | Taken from `logid`.  
`type` | `metadata.product_event_type` | Taken from `type`.  
`subtype` | `metadata.product_event_type` | Appended to type.  
`level` | `security_result.severity_details` | Taken from `level`.  
N/A | `metadata.vendor_name` | Set to **Fortinet**.  
N/A | `metadata.product_name` | Set to **FortiAnalyzer**.  
`attack` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`alert_sub_type` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`Details.SourcePort` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`Details.DestinationPort` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`inter_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`observer_application` | `event.idm.read_only_udm.observer.application` | Mapped from changelog  
`event_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`alert_time` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`details.Bios` | `event.idm.read_only_udm.principal.asset.product_object_id` | Mapped from changelog  
`details.HostName` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`details.IP` | `event.idm.read_only_udm.principal.nat_ip` | Mapped from changelog  
`agent_uuid` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`alert_name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`Details.SourceAddress` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`Details.DestinationAddress` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`Details.Protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`ref` | `event.idm.read_only_udm.security_result.about.url` | Mapped from changelog  
`Details.status` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`log_verbosity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`root_scope_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`timestamp_details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`observer_application_pid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Details.ConsumerScopes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Details.ProviderScopes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_dst_location` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`user_dst_network_zone` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`user_dst_ownership` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`host_name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`forwardedfor` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`tenant_id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`details.AgentType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`details.CurrentVersion` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`details.Platform` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`scope_name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`scope_id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`vrf_id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`Details.user_src_app_name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`Details.user_src_environment` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`Details.user_src_location` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`Details.user_src_network_zone` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`Details.user_src_ownership` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert_text` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`attackid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`key_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`individual_alert` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`summary_alert_freq` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert_grain` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`IsConsumerMalicious` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`IsProviderMalicious` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`from` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
`to` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`subject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`size` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`attachment` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`qtype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`xid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.action` to `ALLOW` when `action` is equal to `ip-conn` | Mapped from changelog  
`unauthuser` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`app_protocol_src` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cloudaction` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`itime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`shapingpolicyname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mastersrcmac` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dstdevtype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`eventsubtype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pdstport` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`psrcport` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`clouduser` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`unauthusersource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`devid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`incidentserialno` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`poluuid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`http_retcode` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`http_method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`http_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`http_agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`srcfamily` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`cipher_suite` | `event.idm.read_only_udm.network.tls.cipher` | Mapped from changelog  
`policy` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`http_response_bytes` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`http_request_bytes` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`osname` | `event.idm.read_only_udm.principal.platform` | Mapped from changelog  
`dstosname` | `event.idm.read_only_udm.target.platform` | Mapped from changelog  
`scertcname` | `event.idm.read_only_udm.network.tls.client.certificate.subject` | Mapped from changelog  
`dstswversion` | `event.idm.read_only_udm.target.platform_version` | Mapped from changelog  
`dsthwvendor` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`filesize` | `event.idm.read_only_udm.target.file.size` | Mapped from changelog  
`http_version` | `event.idm.read_only_udm.network.application_protocol_version` | Mapped from changelog  
`x509_cert_subject` | `event.idm.read_only_udm.network.tls.server.certificate.subject` | Mapped from changelog  
`srcswversion` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`tlsver` | `event.idm.read_only_udm.network.tls.version` | Mapped from changelog  
`original_src` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`http_host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`http_refer` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`agent` | `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`dstname` | `target.hostname` | Mapped from changelog  
`catdesc` | `security_result.rule_name` | Mapped from changelog  
`crscore` | `security_result.detection_fields` | Mapped from changelog  
`method` | `network.http.method` | Mapped from changelog  
`filename` | `target.file.full_path` | Mapped from changelog  
`dstuser` | `target.user.userid` | Mapped from changelog  
`fsaverdict` | `additional.fields` | Mapped from changelog  
`type", "subtype", and "level` | `metadata.ingestion_labels` | Mapped from changelog  
`logdesc` | `metadata.description` | Mapped from changelog  
`srcname` | `principal.hostname` | Mapped from changelog  
`httpmethod` | `network.http.method` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortianalyzer-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
