---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsa/
title: Collect Cisco Secure Web Appliance (formerly Web Security Appliance) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:08:54.035412+00:00
---

# Collect Cisco Secure Web Appliance (formerly Web Security Appliance) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wsa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Secure Web Appliance (formerly Web Security Appliance) logs

**Parser Version:** 7.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Cisco Secure Web Appliance (formerly known as Web Security Appliance) logs to Google Security Operations using Bindplane.

Cisco Secure Web Appliance is an on-premises web proxy and security gateway that protects organizations from web-based threats. It provides URL filtering, malware scanning, data loss prevention, and application visibility and control for all HTTP, HTTPS, and FTP traffic. The appliance enforces acceptable use policies and inspects encrypted traffic to detect and block advanced threats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco Secure Web Appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco Secure Web Appliance web interface



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /status observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/cisco_wsa:
            compression: gzip
            creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_WSA
            raw_log_field: body
        
        service:
          pipelines:
            logs/cisco_wsa_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/cisco_wsa
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
         




## Configure syslog forwarding on Cisco Secure Web Appliance

  1. Sign in to the **Cisco Secure Web Appliance** web interface.
  2. Go to **System Administration > Log Subscriptions**.
  3. Click **Add Log Subscription**.
  4. Select a log type from the **Log Type** dropdown. For web proxy traffic, select **Access Logs**.
  5. In the **Log Name** field, enter a descriptive name for the log subscription (for example, `chronicle-access`).
  6. Select the access log format:

     * **Squid** \- standard Squid-compatible format
     * **Apache** \- Apache-compatible format
     * **W3C Extended** \- W3C Extended Log File format with configurable fields
**Note:** The Squid format is the default and most commonly used with the CISCO_WSA parser.
  7. Specify the **Maximum File Size** before log rollover and the **Time Interval** between rollovers.

  8. Select the **Log Level**. The available options are Critical, Warning, Information, Debug, or Trace.

  9. In the **Retrieval Method** section, select **Syslog Push**.

  10. Provide the following configuration details:

     * **Hostname** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter the port number configured on the Bindplane agent (for example, `514`).
     * **Protocol** : Select **TCP**.
     * **Maximum Message Size** : Enter the maximum size of the log message in bytes to send to the remote syslog server.
     * **Facility** : Select the required syslog facility (for example, **Local0**).
**Note:** Syslog Push conforms to RFC 3164.
  11. Click **Submit**.

  12. Click **Commit Changes** to apply the configuration.

**Note:** Repeat steps 3 through 12 to create additional log subscriptions for other log types such as **L4 Traffic Monitor Logs** , **Malware Scanning Logs** , or **Authentication Logs**.**Note:** For more information, see [Cisco Secure Web Appliance User Guide](https://www.cisco.com/c/en/us/support/security/web-security-appliance/series.html).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_field` | `additional.fields` | Merged  
`case_name_label` | `additional.fields` | Merged  
`cmf_label` | `additional.fields` | Merged  
`dcf_label` | `additional.fields` | Merged  
`err_label` | `additional.fields` | Merged  
`interaction_mode_label` | `additional.fields` | Merged  
`proxy_session_id_label` | `additional.fields` | Merged  
`request_size_label` | `additional.fields` | Merged  
`total_bytes_label` | `additional.fields` | Merged  
`transaction_disposition_label` | `additional.fields` | Merged  
`auth_mechanism` | `extensions.auth.auth_details` | Directly mapped  
`wsa_hostname` | `intermediary.asset.hostname` | Directly mapped  
`wsa_hostname` | `intermediary.hostname` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`time` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`when` | `metadata.event_timestamp` | Parsed as `UNIX`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_HTTP`, `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`action` | `metadata.product_event_type` | Directly mapped  
`app_proto` | `network.application_protocol` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`referer_url` | `network.http.referral_url` | Directly mapped  
`returnCode` | `network.http.response_code` | Directly mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`response_size` | `network.received_bytes` | Directly mapped  
`bytes_sent` | `network.sent_bytes` | Directly mapped  
`size` | `network.sent_bytes` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`srcip` | `principal.asset.ip` | Merged  
`srcip` | `principal.ip` | Merged  
`process_id` | `principal.process.pid` | Directly mapped  
`_field` | `principal.resource.attribute.labels` | Merged  
`key` | `principal.resource.attribute.labels` | Mapped: `server_response` → `_field`  
`username` | `principal.user.userid` | Directly mapped  
`_security_result` | `security_result` | Merged  
`domain` | `target.administrative_domain` | Directly mapped  
`tgthost` | `target.asset.hostname` | Directly mapped  
`tgtip` | `target.asset.ip` | Merged  
`mime_type` | `target.file.mime_type` | Directly mapped  
`tgthost` | `target.hostname` | Directly mapped  
`tgtip` | `target.ip` | Merged  
`tar_city` | `target.location.city` | Directly mapped  
`tar_region` | `target.location.country_or_region` | Directly mapped  
`tar_state` | `target.location.state` | Directly mapped  
`tgtport` | `target.port` | Directly mapped  
`kerberos_enctype_label` | `target.resource.attribute.labels` | Merged  
`kerberos_keytab_label` | `target.resource.attribute.labels` | Merged  
`kerberos_kvno_label` | `target.resource.attribute.labels` | Merged  
`server_cert_organization_label` | `target.resource.attribute.labels` | Merged  
`target_kerberos_realm_label` | `target.resource.attribute.labels` | Merged  
`url` | `target.url` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_HTTP`  
N/A | `metadata.product_name` | Constant: `WSA`  
N/A | `metadata.vendor_name` | Constant: `CISCO`  
`information` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`appname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`facility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logtime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`policy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`ser_url` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`ser_msg` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`ser_data` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`srcport` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`sha_value` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`cmf` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dcf` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`err` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`case_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`total_bytes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request_size` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`transaction_disposition` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`application` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`bytes_sent` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`response_size` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`referer_url` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`wsa_hostname` | `event.idm.read_only_udm.intermediary.hostname`, `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wsa-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
