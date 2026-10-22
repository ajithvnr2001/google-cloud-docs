---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bro-tsv/
title: Collect Zeek (formerly Bro) TSV logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:05.627173+00:00
---

# Collect Zeek (formerly Bro) TSV logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bro-tsv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zeek (formerly Bro) TSV logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Zeek (formerly Bro) TSV logs to Google Security Operations using the Bindplane agent.

Zeek (formerly Bro) is a network security monitoring platform that passively analyzes network traffic and generates detailed, tab-separated log files covering connections, DNS queries, HTTP transactions, SSL/TLS sessions, and file analysis. Zeek sensors produce TSV log files under `/opt/zeek/logs/` or `/usr/local/zeek/logs/` by default.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Zeek sensor host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Zeek sensor host with permissions to read log files
  * Access to Zeek TSV log files on the sensor file system (typically under `/opt/zeek/logs/` or `/usr/local/zeek/logs/`)



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

## Get a Google SecOps customer ID

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
          chronicle/bro_tsv:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: BRO_TSV
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/bro_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/bro_tsv
        




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

    * `bro_tsv`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `BRO_TSV`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `bro_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/bro_tsv:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BRO_TSV
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
             




## Configure Zeek syslog forwarding

Zeek generates TSV log files locally. To forward these logs using syslog to the Bindplane agent, configure a syslog daemon on the Zeek sensor host.

  1. Sign in to the Zeek sensor host with root or sudo privileges.
  2. Install and configure `rsyslog` or `syslog-ng` if not already present.
  3. Create an rsyslog configuration file to forward Zeek logs:
         
         sudo nano /etc/rsyslog.d/zeek-forward.conf
         

  4. Add the following configuration to forward Zeek logs to the Bindplane agent:
         
         module(load="imfile")
         input(type="imfile"
             File="/opt/zeek/logs/current/*.log"
             Tag="zeek:"
             Severity="info"
             Facility="local6")
         local6.* @<BINDPLANE_AGENT_IP>:514
         

     * Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.
     * Replace `/opt/zeek/logs/current/*.log` with the actual path to your Zeek log files if different.
     * Use `@@` instead of `@` for TCP forwarding (must match the Bindplane agent receiver type).
  5. Restart rsyslog to apply the changes:
         
         sudo systemctl restart rsyslog
         

  6. Verify that syslog messages are being received by checking the Bindplane agent logs.

**Note:** Zeek rotates log files hourly by default. The `current/` directory contains the active log files. Adjust the rsyslog `imfile` path to match your Zeek log rotation configuration.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
rtt, operation, tunnel_type, action, cmd, arg, rows | additional.fields | Merged from additional_rtt, additional_op, additional_tt, additional_action, additional_cmd, additional_arg, additional_rows  
| extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED"  
conn_state, action, error, desc | metadata.description | Set to conn_state description for bro_conn, action for bro_smb_files, "KERBEROS: %{error}" for bro_kerberos, desc for AsymPayloadFlow, constant for others  
bro_type, qerror, next_protocol, protocol | metadata.event_type | Set to GENERIC_EVENT by default, NETWORK_DNS for dns, NETWORK_CONNECTION for conn/ntlm/smb_mapping/dce_rpc/tunnel/mysql/ssh/udp/tcp, NETWORK_DHCP for dhcp, NETWORK_HTTP for http/ssl if next_protocol http, NETWORK_UNCATEGORIZED for smb_files/files/x509, USER_LOGIN for radius, NETWORK_FTP for ftp, NETWORK_UNCATEGORIZED if qerror query_not_present  
bro_type, prod_event | metadata.product_event_type | Value from bro_type if not empty, else from prod_event  
uid, id | metadata.product_log_id | Value from uid if available, else from id  
| metadata.product_name | Set to "Bro"  
| metadata.vendor_name | Set to "Zeek"  
service_proto, source | network.application_protocol | Mapped from service_proto for conn, mapped from source for files, constant for others  
hostname | network.dhcp.client_hostname | Value copied directly  
lease_time | network.dhcp.lease_time_seconds | Converted to uinteger  
dhcp_info | network.dhcp.type | Set to "ACK" if =~ "ACK", "RELEASE" if =~ "RELEASE", "INFORM" if =~ "INFORM", "DISCOVER" if =~ "DISCOVER", "OFFER" if =~ "OFFER", "REQUEST" if =~ "REQUEST"  
assigned_ip | network.dhcp.yiaddr | Value copied directly  
direction | network.direction | Value copied directly  
answer_list | network.dns.answers | Value copied directly  
trans_id | network.dns.id | Converted to uinteger  
q | network.dns.questions | Merged from q  
rcode | network.dns.response_code | Converted to uinteger if not "-"  
command | network.ftp.command | Value copied directly  
method | network.http.method | Value copied directly  
referrer | network.http.referral_url | Value copied directly  
status_code | network.http.response_code | Converted to integer  
user_agent | network.http.user_agent | Value copied directly  
proto, protocol | network.ip_protocol | Value from proto for conn, "UDP" for udp, "TCP" for tcp  
id_resp_bytes, received_bytes | network.received_bytes | Converted to uinteger from id_resp_bytes for conn, received_bytes for files  
id_orig_bytes | network.sent_bytes | Converted to uinteger  
uid | network.session_id | Value copied directly  
cipher | network.tls.cipher | Value copied directly  
client_issuer | network.tls.client.certificate.issuer | Value copied directly  
client_subject | network.tls.client.certificate.subject | Value copied directly  
client | network.tls.client.certificate.version | Value copied directly  
ja3 | network.tls.client.ja3 | Value copied directly  
curve | network.tls.curve | Value copied directly  
established | network.tls.established | Value copied directly  
next_protocol | network.tls.next_protocol | Value copied directly  
resumed | network.tls.resumed | Value copied directly  
issuer, certificate.issuer | network.tls.server.certificate.issuer | Value from issuer for ssl, certificate.issuer for x509  
certificate.not_valid_after | network.tls.server.certificate.not_after | Converted using date filter  
certificate.not_valid_before | network.tls.server.certificate.not_before | Converted using date filter  
certificate.serial | network.tls.server.certificate.serial | Value copied directly  
subject, certificate.subject | network.tls.server.certificate.subject | Value from subject for ssl, certificate.subject for x509  
certificate.version | network.tls.server.certificate.version | Converted to string  
ja3s | network.tls.server.ja3s | Value copied directly  
version | network.tls.version | Value copied directly  
domain | principal.administrative_domain | Value copied directly  
file_size | principal.file.size | Converted to uinteger  
client_host, _system_name, _HostName | principal.hostname | Value from client_host for kerberos, _system_name for x509, _HostName if extracted  
id.orig_h | principal.ip | Merged from id.orig_h  
mac | principal.mac | Value copied directly  
id.orig_p | principal.port | Converted to integer, value from id.orig_p or reversed for conn if not local_orig  
user_email | principal.user.email_addresses | Merged from user_email  
user, username, user_name | principal.user.userid | Value from user for ftp, username for radius, user_name for kerberos  
qclass | q.class | Converted to uinteger  
qname, q.name | q.name | Value from qname or q.name  
qtype | q.type | Converted to uinteger  
result, auth_success | security_result | Merged from security_result with action BLOCK for radius failed, ALLOW/BLOCK/UNKNOWN for ssh  
uri | target.administrative_domain | Extracted from uri using grok  
full_file_path, fuid | target.file.full_path | Value from full_file_path for smb_files, fuid for files  
md5 | target.file.md5 | Value copied directly  
mime_type | target.file.mime_type | Value copied directly  
sha1 | target.file.sha1 | Value copied directly  
size, file_size | target.file.size | Converted to uinteger from size for smb_files, file_size for files  
server_host, host, CN, server | target.hostname | Value from server_host for kerberos, host for http, CN for x509, server for ssh  
id.resp_h | target.ip | Merged from id.resp_h  
host_key, host_key_alg, kex_alg, mac_alg, compression_alg, cipher_alg, auth_attempts | target.labels | Merged from various label objects  
id.resp_p | target.port | Converted to integer, value from id.resp_p or reversed for conn if not local_orig  
path, named_pipe | target.resource.name | Value from path for smb_mapping, named_pipe for dce_rpc  
share_type | target.resource.type | Value from share_type for smb_mapping, "PIPE" for dce_rpc  
url | target.url | Concatenated from host and uri  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bro-tsv-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
