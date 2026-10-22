---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/suricata-eve/
title: Collect Suricata EVE logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:02.977610+00:00
---

# Collect Suricata EVE logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/suricata-eve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Suricata EVE logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Suricata EVE logs to Google Security Operations using Bindplane.

Suricata is an open-source high-performance network threat detection engine that provides intrusion detection (IDS), intrusion prevention (IPS), and network security monitoring capabilities. The EVE (Extensible Event Format) log output provides comprehensive JSON-formatted logs covering alerts, flows, DNS, HTTP, TLS, and file transaction data. The parser extracts fields from Suricata EVE JSON formatted logs. It parses the JSON message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Suricata host (root or sudo)



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

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
          chronicle/chronicle_w_labels:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: 'SURICATA_EVE'
            raw_log_field: body
            ingestion_labels:
        
        service:
          pipelines:
            logs/source0__chronicle_w_labels-0:
              receivers:
                - udplog
              exporters:
                - chronicle/chronicle_w_labels
        




### Configuration parameters

  * Replace the following placeholders:

    * **Receiver configuration:**

      * `udplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog
      * `0.0.0.0`: IP address to listen on (`0.0.0.0` to listen on all interfaces)
      * `514`: Port number to listen on (standard syslog port)
    * **Exporter configuration:**

      * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
        * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
        * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
      * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section
      * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
      * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
      * `endpoint`: Keep set to `chronicle.googleapis.com`.
      * `log_type`: Log type exactly as it appears in Chronicle (`SURICATA_EVE`)



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'SURICATA_EVE'
            raw_log_field: body
            ingestion_labels:
        


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

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Suricata EVE syslog forwarding

  1. Open the **Suricata** configuration file (typically `/etc/suricata/suricata.yaml`).
  2. Locate the `outputs` section and configure the **EVE log** output for syslog:
         
         outputs:
           - eve-log:
               enabled: yes
               filetype: syslog
               identity: "suricata"
               facility: local5
               level: Info
               types:
                 - alert:
                     payload: yes
                     payload-printable: yes
                     packet: yes
                     metadata: yes
                 - http:
                     extended: yes
                 - dns:
                     query: yes
                     answer: yes
                 - tls:
                     extended: yes
                 - files:
                     force-magic: no
                 - flow
                 - netflow
                 - anomaly:
                     enabled: yes
                 - stats:
                     enabled: yes
         

  3. If the syslog daemon is not configured to forward to Bindplane, configure rsyslog or syslog-ng:

     * **For rsyslog** (edit `/etc/rsyslog.conf` or create `/etc/rsyslog.d/suricata.conf`):
           
           local5.* @BINDPLANE_IP:514
           

       * Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.
       * Use `@` for UDP or `@@` for TCP.
     * **For syslog-ng** (edit `/etc/syslog-ng/syslog-ng.conf`):
           
           destination d_bindplane { udp("BINDPLANE_IP" port(514)); };
           filter f_suricata { facility(local5); };
           log { source(s_src); filter(f_suricata); destination(d_bindplane); };
           

  4. Restart the syslog daemon:
         
         sudo systemctl restart rsyslog
         

  5. Restart Suricata:
         
         sudo systemctl restart suricata
         

  6. Verify syslog messages are being sent by checking the Bindplane agent logs.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
timestamp | metadata.event_timestamp | Event timestamp  
event_type | metadata.product_event_type | Type of EVE event (e.g., alert, flow, dns, http, tls)  
src_ip | principal.ip | Source IP address  
src_port | principal.port | Source port number  
dest_ip | target.ip | Destination IP address  
dest_port | target.port | Destination port number  
proto | network.ip_protocol | Network protocol (e.g., TCP, UDP, ICMP)  
flow_id | network.session_id | Unique flow identifier  
alert.signature | security_result.rule_name | Alert signature name  
alert.signature_id | security_result.rule_id | Alert signature identifier  
alert.severity | security_result.severity | Alert severity level  
alert.category | security_result.category_details | Alert classification category  
alert.action | security_result.action | Action taken (e.g., allowed, blocked)  
alert.rev | security_result.rule_version | Rule revision number  
http.hostname | target.hostname | HTTP request hostname  
http.url | target.url | HTTP request URL  
http.http_method | network.http.method | HTTP request method  
http.status | network.http.response_code | HTTP response status code  
http.http_user_agent | network.http.user_agent | HTTP user agent string  
http.http_refer | network.http.referral_url | HTTP referrer URL  
http.length | additional.fields | HTTP content length  
dns.type | network.dns.type | DNS query or response  
dns.rrname | network.dns.questions.name | DNS query name  
dns.rrtype | network.dns.questions.type | DNS query type  
dns.rdata | network.dns.answers.data | DNS response data  
tls.subject | network.tls.client.subject | TLS certificate subject  
tls.issuerdn | network.tls.client.issuer | TLS certificate issuer  
tls.sni | network.tls.client.server_name | TLS Server Name Indication  
tls.version | network.tls.version | TLS version  
tls.ja3.hash | network.tls.client.ja3 | JA3 client fingerprint hash  
tls.ja3s.hash | network.tls.server.ja3s | JA3S server fingerprint hash  
app_proto | network.application_protocol | Application layer protocol detected  
flow.bytes_toserver | network.sent_bytes | Bytes sent from client to server  
flow.bytes_toclient | network.received_bytes | Bytes sent from server to client  
flow.pkts_toserver | additional.fields | Packets sent from client to server  
flow.pkts_toclient | additional.fields | Packets sent from server to client  
in_iface | additional.fields | Input network interface  
community_id | network.community_id | Network community ID flow hash  
`flow.src_ip` | `event.idm.read_only_udm.principal.ip` / `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`alert.source.ip` | `event.idm.read_only_udm.principal.ip` / `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`flow.dest_ip` | `event.idm.read_only_udm.target.ip` / `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`alert.target.ip` | `event.idm.read_only_udm.target.ip` / `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`flow.pkts_toserver` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flow.pkts_toclient` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.source.port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.target.port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.rule` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.metadata.attack_target` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.metadata.confidence` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.metadata.deployment` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.metadata.tag` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dhcp.client_ip` | `event.idm.read_only_udm.network.dhcp.ciaddr` | Mapped from changelog  
`dhcp.client_id` | `event.idm.read_only_udm.network.dhcp.client_identifier` | Mapped from changelog  
`dhcp.params` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dhcp.hostname` | `event.idm.read_only_udm.network.dhcp.client_hostname` | Mapped from changelog  
`dhcp.vendor_class_identifier` | `event.idm.read_only_udm.network.dhcp.options` | Mapped from changelog  
`dhcp.type` | `event.idm.read_only_udm.network.dhcp.opcode` | Mapped from changelog  
`dhcp.dhcp_type` | `event.idm.read_only_udm.network.dhcp.type` | Mapped from changelog  
`dhcp.assigned_ip` | `event.idm.read_only_udm.network.dhcp.yiaddr` | Mapped from changelog  
`dhcp.client_mac` | `event.idm.read_only_udm.network.dhcp.chaddr` | Mapped from changelog  
`dns.qr` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns_qr` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tls.ja3.string` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tls_ja3_string` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tls.ja3s.string` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tls_ja3s_string` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tls.ja4` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tls_ja4` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns.version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns.opcode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns_opcode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns.tx_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns_tx_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns.flags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns_flags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`audata.soa.mname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`soa_mname_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`audata.soa.rname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`soa_rname_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`audata.soa.serial` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`soa_serial_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`audata.soa.refresh` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`soa_refresh_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`audata.soa.retry` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`soa_retry_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`audata.soa.expire` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`soa_expire_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`audata.soa.minimum` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`soa_minimum_%{index}` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dns.rd` | `event.idm.read_only_udm.network.dns.recursion_desired` | Mapped from changelog  
`dns.ra` | `event.idm.read_only_udm.network.dns.recursion_available` | Mapped from changelog  
`dns.answers` | `event.idm.read_only_udm.network.dns.answers` | Mapped from changelog  
`dns.authorities` | `event.idm.read_only_udm.network.dns.answers` | Mapped from changelog  
`event_type` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`dns.answers.ttl` | `event.idm.read_only_udm.network.dns.answers.ttl` | Mapped from changelog  
`dns.authorities.ttl` | `event.idm.read_only_udm.network.dns.answers.ttl` | Mapped from changelog  
`dns.authorities.rrtype` | `event.idm.read_only_udm.network.dns.answers.type` | Mapped from changelog  
`dns.answers.rrtype` | `event.idm.read_only_udm.network.dns.answers.type` | Mapped from changelog  
`dns.authorities.rrname` | `event.idm.read_only_udm.network.dns.answers.name` | Mapped from changelog  
`dns.answers.rrname` | `event.idm.read_only_udm.network.dns.answers.name` | Mapped from changelog  
`dns.answers.rdata` | `event.idm.read_only_udm.network.dns.answers.data` | Mapped from changelog  
`dns.rcode` | `event.idm.read_only_udm.network.dns.response_code` | Mapped from changelog  
`ssh.server.hassh.software_version", "ssh.server.hassh.proto_version", "ssh.server.hassh.string", "ssh.client.hassh.software_version", "ssh.client.hassh.proto_version", "ssh.client.hassh.string` | `additional.fields` | Mapped from changelog  
`alert.metadata.stamus_classification` | `additional.fields` | Mapped from changelog  
`alert.metadata.sightings_key` | `additional.fields` | Mapped from changelog  
`alert.metadata.sightings_asset` | `additional.fields` | Mapped from changelog  
`discovery` | `additional.fields` | Mapped from changelog  
`dns.id` | `network.dns.id` | Mapped from changelog  
`see_id` | `network.session_id` | Mapped from changelog  
`payload_printable` | `additional.fields` | Mapped from changelog  
`process.executable` | `principal.process.file.full_path` | Mapped from changelog  
`process.pid` | `principal.process.pid` | Mapped from changelog  
`process.command_line` | `principal.process.command_line` | Mapped from changelog  
`service.type` | `additional.fields` | Mapped from changelog  
`event.dataset` | `about.labels` | Mapped from changelog  
`event.module` | `about.labels` | Mapped from changelog  
`event.duration` | `about.labels` | Mapped from changelog  
`agent.id` | `metadata.product_log_id` | Mapped from changelog  
`agent.type` | `metadata.product_event_type` | Mapped from changelog  
`agent.version` | `metadata.product_version` | Mapped from changelog  
`agent.hostname` | `principal.hostname` | Mapped from changelog  
`agent.name` | `principal.hostname` | Mapped from changelog  
`agent.ephemeral_id` | `additional.fields` | Mapped from changelog  
`ecs.version` | `principal.asset.attribute.labels` | Mapped from changelog  
`process.args` | `about.file.capabilities_tags` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/suricata-eve-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
