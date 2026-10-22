---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-silverline/
title: Collect F5 Silverline logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:36.546390+00:00
---

# Collect F5 Silverline logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-silverline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect F5 Silverline logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest F5 Silverline logs to Google Security Operations using Bindplane.

F5 Silverline is a cloud-based security service platform that provides DDoS protection, Web Application Firewall (WAF), and IP Intelligence services. The platform protects applications and infrastructure from distributed denial-of-service attacks, web application exploits, and malicious traffic through F5's global scrubbing centers and security operations center.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the internet
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Access to the F5 Silverline portal with administrative privileges
  * Firewall rules allowing inbound TLS+TCP traffic on port 6514 to the Bindplane agent host



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

  * Locate the configuration file

    * **Linux:**
          
          sudo nano /opt/observiq-otel-collector/config.yaml
          

    * **Windows:**
          
          notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
          




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:6514"
        
        exporters:
          chronicle/f5_silverline:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: F5_SILVERLINE
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/silverline_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/f5_silverline
        




### Configuration parameters

Replace the following placeholders:

  * **`<CREDS_FILE_PATH>`**: Full path to the service account JSON key file (Option 1): 
    * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * **`<CUSTOMER_ID>`**: Your Google SecOps customer ID from the previous step
  * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
  * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * `endpoint`: Keep set to `chronicle.googleapis.com`.

**Note:** F5 Silverline enforces TLS+TCP communication on port 6514 by default. The Bindplane agent receives the TLS-encrypted syslog messages and forwards them to Chronicle.

  * **Example configuration**
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:6514"
        
        exporters:
          chronicle/f5_silverline:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
            endpoint: chronicle.googleapis.com
            log_type: F5_SILVERLINE
            raw_log_field: body
            ingestion_labels:
              env: production
              source: silverline
        
        service:
          pipelines:
            logs/silverline_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/f5_silverline
        




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/f5_silverline:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: F5_SILVERLINE
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
         




## Configure F5 Silverline syslog forwarding

  1. Sign in to the **F5 Silverline portal** at `https://portal.f5silverline.com`.
  2. Go to **Config > Log Export**.
  3. In the **IP address** field, enter the IP address of the Bindplane agent host.
  4. In the **Port** field, enter `6514`.
  5. In the **Protocol** dropdown, select **TCP**.
  6. In the **Format** dropdown, select **Auto**.
  7. Click **Save** to apply the configuration.

**Note:** F5 Silverline automatically enforces TLS encryption for TCP connections on port 6514. The destination host must support TLS+TCP communication.

### Log types forwarded

F5 Silverline forwards the following log types through syslog:

  * **DDoS Mitigation Logs** : Information about DDoS attacks, mitigation actions, and filtered traffic
  * **WAF Logs** : Web Application Firewall violation events, attack types, and blocked requests
  * **IP Intelligence Logs** : Threat intelligence data about malicious IP addresses
  * **Network Traffic Logs** : Network-level traffic analysis and anomaly detection
  * **Proxy Logs** : HTTP/HTTPS proxy events and connection details



### Verify log export

  1. In the F5 Silverline portal, go to **Config > Log Export**.
  2. Verify the connection status shows as **Active** or **Connected**.
  3. Check the Bindplane agent logs to confirm syslog messages are being received:

**Linux:**
         
         sudo journalctl -u observiq-otel-collector -f
         

**Windows:**
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         

  4. In the Google SecOps console, go to **SIEM > Search** and search for `metadata.log_type = "F5_SILVERLINE"` to verify logs are being ingested.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
content_length, geo_location, policy_apply_date, policy_name, flow_id, errdefs_msgno, ip_intelligence_threat_name, log_type, loglevel, msg_type, proxy_id, request_side, tmm_unit, disable_asm, disable_bot, policy_name, http_class_name, reason, protocol, mitigation, countermeasure, blacklisted, msg_type, proxy_id, request_side, route_domain, sa_translation_type, sa_translation_pool, translated_vlan, translated_source_port, translated_source_ip, translated_route_domain, translated_ip_protocol, translated_dest_port | additional.fields | Merged as labels into additional.fields if not empty  
app_protocol_output | event.idm.read_only_udm.network.application_protocol | Value copied directly if not empty  
method | event.idm.read_only_udm.network.http.method | Value copied directly  
response_code | event.idm.read_only_udm.network.http.response_code | Value copied directly  
source_ip, vs_ip | event.idm.read_only_udm.src.asset.ip | Value from vs_ip if not empty, else source_ip  
vs_port, src_port | event.idm.read_only_udm.src.port | Value from vs_port if not empty, else src_port  
x_forwarded_for_header_value, header_ip | intermediary.asset.ip | Value from header_ip if not empty, else x_forwarded_for_header_value  
x_forwarded_for_header_value, header_ip | intermediary.ip | Value from header_ip if not empty, else x_forwarded_for_header_value  
errdefs_msg_name | metadata.description | Value copied directly if not empty  
ts | metadata.event_timestamp | Parsed from ts using date match with format MMM dd HH:mm:ss or MMM d HH:mm:ss  
event_type | metadata.event_type | Value copied directly  
support_id | metadata.product_log_id | Value copied directly if not empty  
protocol | network.application_protocol | Set to protocol if equals HTTPS  
method, uri_data | network.http.method | Value from uri_data if not empty, else method  
response_code | network.http.response_code | Value copied directly, then converted to integer  
user_agent | network.http.user_agent | Value copied directly  
ip_protocol | network.ip_protocol | Set to "TCP" if matches tcp  
virtualserver | network.tls.client.server_name | Value copied directly if not empty  
web_application_name | principal.application | Value copied directly  
hostname | principal.asset.hostname | Value copied directly  
ip_client, source_ip, client_ip, addr, source_ip, vs_ip | principal.asset.ip | Value from ip_client if type=waf; source_ip if type=ipi; client_ip if type=irule; vs_ip if not empty in kvdata, else source_ip if not empty, else client_ip if not empty, else addr if not empty, else ip_client  
host, hostname | principal.hostname | Value from hostname if not empty, else host  
ip_client, source_ip, client_ip, addr, source_ip, vs_ip | principal.ip | Value from ip_client if type=waf; source_ip if type=ipi; client_ip if type=irule; vs_ip if not empty in kvdata, else source_ip if not empty, else client_ip if not empty, else addr if not empty, else ip_client  
geo_location, client_ip_geo_location | principal.location.name | Value from client_ip_geo_location if not empty, else geo_location  
snat_ip | principal.nat_ip | Value copied directly  
snat_port | principal.nat_port | Value copied directly, then converted to integer  
client_port, source_port, client_port | principal.port | Value from client_port if type=irule; source_port if not empty in kvdata, else client_port  
host, data.uri, client_request_uri | principal.url | Value from data.uri if type=irule; client_request_uri if not empty in kvdata, else host  
service_id | principal.user.product_object_id | Value copied directly  
sec_action | security_result.action | Set to BLOCK if request_status in [Blocking, blocked, drop, challenged] or action in [Blocking, blocked, drop]; ALLOW if request_status in [allow, Allow] or action in [allow, Allow, accept]; else UNKNOWN_ACTION  
action, request_status, data.action | security_result.action_details | Value from data.action if type=irule; request_status if kvdata; action if type=ipi  
attack_type | security_result.category_details | Value copied directly if not empty  
sub_violations, context_name, sub_violations | security_result.description | Value from sub_violations if type=waf or kvdata; context_name if type=ipi  
request_status | security_result.detection_fields | Added as label to security_result.detection_fields  
ip_intelligence_policy_name, irule, irule, ip_intelligence_policy_name | security_result.rule_name | Value from irule if type=irule or kvdata; ip_intelligence_policy_name if type=ipi or kvdata  
irule-version | security_result.rule_version | Value copied directly  
severity | security_result.severity | Set to CRITICAL if Critical; ERROR if Error; INFORMATIONAL if Informational; HIGH if 5  
violations, data.action | security_result.summary | Value from violations if type=waf; data.action if type=irule  
ip_intelligence_threat_name | security_result.threat_name | Value copied directly  
source_ip | src.asset.ip | Value copied directly  
src_port, source_port | src.port | Value copied directly, then converted to integer  
dest_ip, bigip_mgmt_ip, dest_ip, server_ip, bigip_mgmt_ip, dest_ip, t_ip | target.asset.ip | Value from dest_ip if type=waf; dest_ip if type=ipi; server_ip if type=irule; bigip_mgmt_ip if not empty in kvdata, else dest_ip if not empty, else t_ip  
dest_ip, bigip_mgmt_ip, dest_ip, server_ip, bigip_mgmt_ip, dest_ip, t_ip | target.ip | Value from dest_ip if type=waf; dest_ip if type=ipi; server_ip if type=irule; bigip_mgmt_ip if not empty in kvdata, else dest_ip if not empty, else t_ip  
dest_port, dest_port, server_port, dest_port, dst_port | target.port | Value copied directly, then converted to integer  
uri | target.url | Value copied directly  
| metadata.vendor_name | Set to "SILVERLINE"  
| metadata.product_name | Set to "SILVERLINE"  
`inter_application` | `event.idm.read_only_udm.intermediary.application` | Mapped from changelog  
`msg1` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`prin_host` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`prin_ip` | `event.idm.read_only_udm.principal.ip ,`event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`tar_host` | `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`Cipher` | `event.idm.read_only_udm.network.tls.cipher` | Mapped from changelog  
`process_pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`sec_rule_details` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`EventType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`app` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`session` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`sn` | `event.idm.read_only_udm.network.tls.client.certificate.serial` | Mapped from changelog  
`type_value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`idx` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`C_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`O_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OU_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CN_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`verify` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_priority` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`x_forwarded_for_header_value` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`x_forwarded_for_header_value` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`host` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`sub_violations` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`web_application_name` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`uri` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`policy_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`http_class_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ip_client` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`ip_client` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`geo_location` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`request_status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`support_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`client_ip_geo_location` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`client_request_uri` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`rule` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`reason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`t_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`t_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`mitigation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dst_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`countermeasure` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`blacklisted` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.src.ip` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.src.asset.ip` | Mapped from changelog  
`addr` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`addr` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`ts` | `event.idm.read_only_udm.metadata.timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-silverline-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
