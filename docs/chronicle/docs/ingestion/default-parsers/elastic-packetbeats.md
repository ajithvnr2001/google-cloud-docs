---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-packetbeats/
title: Collect Elastic Packet Beats logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:50.053720+00:00
---

# Collect Elastic Packet Beats logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-packetbeats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Elastic Packet Beats logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Elastic Packet Beats logs to Google Security Operations using Bindplane. The parser first initializes default values for various fields found in Elastic Packet Beats logs. Then, it extracts data from the log messages using a combination of `grok` patterns and `json` filters, performs data type conversions, and maps the extracted fields to the corresponding fields in the Unified Data Model (UDM) based on the event dataset type (for example, flow, dns, http, tls, dhcpv4).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later, or Linux host with `systemd`.
  * If running behind a proxy, make sure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Elastic Packet Beats management console or appliance.
  * Logstash installed and configured.



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



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: YOUR_CUSTOMER_ID
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'ELASTIC_PACKETBEATS'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `YOUR_CUSTOMER_ID` with the actual customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: YOUR_CUSTOMER_ID
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'ELASTIC_PACKETBEATS'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console, or enter the following command:
        
        net stop observiq-otel-collector && net start observiq-otel-collector
        




## Configure Syslog forwarding on Elastic Packet Beats

Since Packetbeat does not support direct syslog output, you must use Logstash as an intermediary.

### Configure Packetbeat to send logs to Logstash

  1. Sign in to the **Elastic Packet Beats Management Console**.
  2. Go to **Settings > Log Forwarding**.
  3. Click the **\+ Add** or **Enable** button.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Logstash Output`).
     * **Host** : Enter the Logstash server IP address.
     * **Port** : Enter the Logstash beats input port (typically 5044).
     * **Protocol** : Select **Beats protocol**.
     * **Format** : Select **JSON**.
     * **Timezone** : Select UTC time zone for universal consistency across systems.
     * Go to the **Events** section and select the relevant log types or **all**.
  5. Save the configuration.

**Alternative: Edit packetbeat.yml directly:**
         
         # /etc/packetbeat/packetbeat.yml
         packetbeat.protocols:
           - type: dns
             ports: [53]
           - type: http
             ports: [80, 8080, 8000, 5000, 8002]
             send_headers: true
             send_all_headers: true
           - type: tls
             ports: [443, 993, 995, 5223, 8443, 8883, 9243]
           - type: dhcpv4
             ports: [67, 68]
         
         # Enable processors for additional fields
         processors:
           - add_network_direction:
               source: private
               destination: private
               internal_networks:
                 - private
           - community_id:
         
         # Send to Logstash using beats protocol
         output.logstash:
           hosts: ["LOGSTASH_IP:5044"]
         

Replace `LOGSTASH_IP` with your Logstash server's IP address.




### Configure Logstash to forward to BindPlane using Syslog

  1. Create a Logstash pipeline configuration file:
         
         sudo nano /etc/logstash/conf.d/packetbeat-to-bindplane.conf
         

  2. Add the following configuration:
         
         # Receive from Packetbeat
         input {
           beats {
             port => 5044
           }
         }
         
         # Optional: Add filters for data enrichment
         filter {
           # Preserve original message structure
           mutate {
             copy => { "@metadata" => "[@metadata_backup]" }
           }
         }
         
         # Send to BindPlane via syslog
         output {
           syslog {
             host => "BINDPLANE_IP"
             port => 514
             protocol => "udp"
             rfc => "rfc5424"
             facility => "local0"
             severity => "informational"
             sourcehost => "%{[agent][hostname]}"
             appname => "packetbeat"
             procid => "%{[agent][id]}"
             msgid => "ELASTIC_PACKETBEATS"
             structured_data => "packetbeat@32473"
             message => "%{message}"
           }
         }
         

Replace `BINDPLANE_IP` with your BindPlane agent's IP address.



  * Restart Logstash to apply the configuration:
        
        sudo systemctl restart logstash
        




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
@timestamp | metadata.event_timestamp | Directly mapped from the raw log field `@timestamp`.  
agent.hostname | observer.hostname | Directly mapped from the raw log field `agent.hostname`.  
agent.id | observer.asset_id | Concatenated with `agent.type` to form the `observer.asset_id` field.  
agent.type | observer.application | Directly mapped from the raw log field `agent.type`.  
agent.version | observer.platform_version | Directly mapped from the raw log field `agent.version`.  
audit_category | security_result.category_details | Directly mapped from the raw log field `audit_category`.  
audit_cluster_name | additional.fields.audit_cluster_name.value.string_value | Directly mapped from the raw log field `audit_cluster_name`.  
audit_node_host_address | observer.ip | Directly mapped from the raw log field `audit_node_host_address`.  
audit_node_id | additional.fields.audit_node_id.value.string_value | Directly mapped from the raw log field `audit_node_id`.  
audit_node_name | additional.fields.audit_node_name.value.string_value | Directly mapped from the raw log field `audit_node_name`.  
audit_request_effective_user | observer.user.userid | Directly mapped from the raw log field `audit_request_effective_user`.  
audit_request_initiating_user | additional.fields.audit_request_initiating_user.value.string_value | Directly mapped from the raw log field `audit_request_initiating_user`.  
audit_request_remote_address | observer.ip | Directly mapped from the raw log field `audit_request_remote_address` if it's different from `audit_node_host_address`.  
client.bytes | network.received_bytes (INBOUND) / network.sent_bytes (OUTBOUND) | Mapped based on the `network.direction` field. If INBOUND, it's mapped to `network.received_bytes`. If OUTBOUND, it's mapped to `network.sent_bytes`.  
client.ip | target.ip (INBOUND) / principal.ip (OUTBOUND) | Mapped based on the `network.direction` field. If INBOUND, it's mapped to `target.ip`. If OUTBOUND, it's mapped to `principal.ip`.  
client.port | target.port (INBOUND) / principal.port (OUTBOUND) | Mapped based on the `network.direction` field. If INBOUND, it's mapped to `target.port`. If OUTBOUND, it's mapped to `principal.port`.  
cluster.uuid | additional.fields.uuid.value.string_value | Directly mapped from the raw log field `cluster.uuid`.  
component | additional.fields.component.value.string_value | Directly mapped from the raw log field `component`.  
destination.bytes | network.sent_bytes | Directly mapped from the raw log field `destination.bytes` for FLOW events.  
destination.ip | target.ip | Directly mapped from the raw log field `destination.ip` if `network.direction` is not INBOUND or OUTBOUND.  
destination.mac | target.mac | Directly mapped from the raw log field `destination.mac` for FLOW events.  
destination.port | target.port | Directly mapped from the raw log field `destination.port` for FLOW events.  
dhcpv4.assigned_ip | network.dhcp.requested_address | Directly mapped from the raw log field `dhcpv4.assigned_ip`.  
dhcpv4.client_ip | network.dhcp.yiaddr (ACK) / network.dhcp.ciaddr (REQUEST) / source.ip (REQUEST, if dhcpv4.client_ip is empty) | Mapped based on the `network.dhcp.type` field. If ACK, it's mapped to `network.dhcp.yiaddr`. If REQUEST, it's mapped to `network.dhcp.ciaddr`. If REQUEST and `dhcpv4.client_ip` is empty, it's mapped to `source.ip`.  
dhcpv4.client_mac | network.dhcp.client_identifier | Directly mapped from the raw log field `dhcpv4.client_mac` after converting it to bytes.  
dhcpv4.op_code | network.dhcp.opcode | Mapped to `network.dhcp.opcode` based on the value of `dhcpv4.op_code`. If `dhcpv4.op_code` is `BOOTREPLY` or `BOOTREQUEST`, the value is directly mapped. Otherwise, it's mapped to `UNKNOWN_OPCODE`.  
dhcpv4.option.hostname | network.dhcp.client_hostname | Directly mapped from the raw log field `dhcpv4.option.hostname`.  
dhcpv4.option.ip_address_lease_time_sec | network.dhcp.lease_time_seconds | Directly mapped from the raw log field `dhcpv4.option.ip_address_lease_time_sec` after converting it to an unsigned integer.  
dhcpv4.option.message_type | network.dhcp.type | Mapped to `network.dhcp.type` based on the value of `dhcpv4.option.message_type`. The mapping is as follows: `ack` -> `ACK`, `nack` -> `NAK`, `discover` -> `DISCOVER`, `offer` -> `OFFER`, `request` -> `REQUEST`, `decline` -> `DECLINE`, `release` -> `RELEASE`, `info` -> `INFORM`. If the value is not one of these, it's mapped to `UNKNOWN_MESSAGE_TYPE`.  
dhcpv4.option.server_identifier | network.dhcp.sname | Directly mapped from the raw log field `dhcpv4.option.server_identifier`.  
dns.answers.data | network.dns.answers.data | Directly mapped from the raw log field `dns.answers.data`.  
dns.answers.class | network.dns.answers.class | Mapped to `network.dns.answers.class` based on the value of `dns.answers.class`. The mapping is as follows: `IN` -> 1, `NONE` -> 254, `ANY` -> 255.  
dns.answers.name | network.dns.answers.name | Directly mapped from the raw log field `dns.answers.name`.  
dns.answers.ttl | network.dns.answers.ttl | Directly mapped from the raw log field `dns.answers.ttl` after converting it to an unsigned integer.  
dns.answers.type | network.dns.answers.type | Mapped to `network.dns.answers.type` based on the value of `dns.answers.type`. The mapping is as follows: `A` -> 1, `NS` -> 2, `CNAME` -> 5, `SOA` -> 6, `PTR` -> 12, `MX` -> 15, `TXT` -> 16, `AAAA` -> 28, `SRV` -> 33, `NAPTR` -> 35, `DS` -> 43, `DNSKEY` -> 48, `IXFR` -> 251, `AXFR` -> 252, `TYPE99` -> 99, `TKEY` -> 249, `ANY` -> 255, `ALL` -> 255, `URI` -> 256, `NULL` -> 0.  
dns.flags.authoritative | network.dns.authoritative | Directly mapped from the raw log field `dns.flags.authoritative` if it's true.  
dns.flags.recursion_available | network.dns.recursion_available | Directly mapped from the raw log field `dns.flags.recursion_available` if it's true.  
dns.flags.recursion_desired | network.dns.recursion_desired | Directly mapped from the raw log field `dns.flags.recursion_desired` if it's true.  
dns.flags.truncated_response | network.dns.truncated | Directly mapped from the raw log field `dns.flags.truncated_response` if it's true.  
dns.id | network.dns.id | Directly mapped from the raw log field `dns.id` after converting it to an unsigned integer.  
dns.question.class | network.dns.questions.class | Mapped to `network.dns.questions.class` based on the value of `dns.question.class`. The mapping is as follows: `IN` -> 1, `NONE` -> 254, `ANY` -> 255.  
dns.question.name | network.dns.questions.name | Directly mapped from the raw log field `dns.question.name`.  
dns.question.type | network.dns.questions.type | Mapped to `network.dns.questions.type` based on the value of `dns.question.type`. The mapping is as follows: `A` -> 1, `NS` -> 2, `CNAME` -> 5, `SOA` -> 6, `PTR` -> 12, `MX` -> 15, `TXT` -> 16, `AAAA` -> 28, `SRV` -> 33, `NAPTR` -> 35, `DS` -> 43, `DNSKEY` -> 48, `IXFR` -> 251, `AXFR` -> 252, `TYPE99` -> 99, `TKEY` -> 249, `ANY` -> 255, `ALL` -> 255, `URI` -> 256, `NULL` -> 0.  
dns.resolved_ip | network.dns.additional.data | Each element in the `dns.resolved_ip` array is processed and mapped to the `network.dns.additional.data` field.  
dns.response_code | network.dns.response_code | Mapped to `network.dns.response_code` based on the value of `dns.response_code`. The mapping is as follows: `NOERROR` -> 0, `FORMERR` -> 1, `SERVFAIL` -> 2, `NXDOMAIN` -> 3, `NOTIMP` -> 4, `REFUSED` -> 5, `YXDOMAIN` -> 6, `YXRRSET` -> 7, `NXRRSET` -> 8, `NOTAUTH` -> 9, `NOTZONE` -> 10.  
error.message | security_result.summary | Concatenated with `status` to form the `security_result.summary` field for HTTP events.  
event.dataset | metadata.product_event_type | Directly mapped from the raw log field `event.dataset`.  
flow.final |  | Used to determine if the flow is final. If not, the event is dropped.  
flow.id | network.session_id | Directly mapped from the raw log field `flow.id` for FLOW events.  
headers.accept_encoding | security_result.about.labels.Accept-Encoding | Directly mapped from the raw log field `headers.accept_encoding`.  
headers.content_length | additional.fields.content_length.value.string_value | Directly mapped from the raw log field `headers.content_length`.  
headers.content_type | additional.fields.content_type.value.string_value | Directly mapped from the raw log field `headers.content_type`.  
headers.http_accept | additional.fields.http_accept.value.string_value | Directly mapped from the raw log field `headers.http_accept`.  
headers.http_host | principal.hostname, principal.asset.hostname | Directly mapped from the raw log field `headers.http_host`.  
headers.http_user_agent | network.http.user_agent | Directly mapped from the raw log field `headers.http_user_agent`.  
headers.request_method | network.http.method | Directly mapped from the raw log field `headers.request_method`.  
headers.x_b3_parentspanid | additional.fields.x_b3_parentspanid.value.string_value | Directly mapped from the raw log field `headers.x_b3_parentspanid`.  
headers.x_b3_sampled | additional.fields.x_b3_sampled.value.string_value | Directly mapped from the raw log field `headers.x_b3_sampled`.  
headers.x_envoy_attempt_count | security_result.about.labels.x_envoy_attempt_count | Directly mapped from the raw log field `headers.x_envoy_attempt_count`.  
headers.x_envoy_original_path | additional.fields.x_envoy_original_path.value.string_value | Directly mapped from the raw log field `headers.x_envoy_original_path`.  
headers.x_forwarded_client_cert | additional.fields.client_cert.value.string_value | Directly mapped from the raw log field `headers.x_forwarded_client_cert`.  
headers.x_forwarded_for | principal.ip, principal.asset.ip | Directly mapped from the raw log field `headers.x_forwarded_for` after extracting the IP address using grok.  
headers.x_forwarded_proto | additional.fields.x_forwarded_proto.value.string_value | Directly mapped from the raw log field `headers.x_forwarded_proto`.  
headers.x_request_id | additional.fields.x_request_id.value.string_value | Directly mapped from the raw log field `headers.x_request_id`.  
host | principal.ip, principal.asset.ip | Directly mapped from the raw log field `host` after extracting the IP address using grok.  
http.request.method | network.http.method | Directly mapped from the raw log field `http.request.method`.  
level | security_result.severity | Mapped to `security_result.severity` based on the value of `level`. The mapping is as follows: `INFO` -> `INFORMATIONAL`, `ERROR` -> `ERROR`, `WARNING` -> `LOW`.  
logger | additional.fields.logger.value.string_value | Directly mapped from the raw log field `logger`.  
method |  | Used to determine if the event is a DNS event.  
msg | security_result.description | Directly mapped from the raw log field `msg` after removing double quotes.  
network.community_id | network.community_id | Directly mapped from the raw log field `network.community_id`.  
network.direction | network.direction | Directly mapped from the raw log field `network.direction` after converting it to uppercase. If the value is `INGRESS` or `INBOUND`, it's mapped to `INBOUND`. If the value is `EGRESS` or `OUTBOUND`, it's mapped to `OUTBOUND`.  
network.protocol | network.application_protocol | Directly mapped from the raw log field `network.protocol`.  
network.transport | network.ip_protocol | Directly mapped from the raw log field `network.transport` for TLS events.  
server.bytes | network.sent_bytes (INBOUND) / network.received_bytes (OUTBOUND) | Mapped based on the `network.direction` field. If INBOUND, it's mapped to `network.sent_bytes`. If OUTBOUND, it's mapped to `network.received_bytes`.  
server.domain | principal.hostname, principal.asset.hostname (INBOUND) / target.hostname, target.asset.hostname (OUTBOUND) | Mapped based on the `network.direction` field. If INBOUND, it's mapped to `principal.hostname`. If OUTBOUND, it's mapped to `target.hostname`.  
server.ip | principal.ip, principal.asset.ip (INBOUND) / target.ip, target.asset.ip (OUTBOUND) | Mapped based on the `network.direction` field. If INBOUND, it's mapped to `principal.ip`. If OUTBOUND, it's mapped to `target.ip`.  
server.port | principal.port (INBOUND) / target.port (OUTBOUND) | Mapped based on the `network.direction` field. If INBOUND, it's mapped to `principal.port`. If OUTBOUND, it's mapped to `target.port`.  
source.bytes | network.received_bytes | Directly mapped from the raw log field `source.bytes` for FLOW events.  
source.ip | principal.ip, principal.asset.ip | Directly mapped from the raw log field `source.ip` for FLOW events.  
source.mac | principal.mac | Directly mapped from the raw log field `source.mac` for FLOW events.  
source.port | principal.port | Directly mapped from the raw log field `source.port` for FLOW events.  
status | metadata.description, security_result.summary | Mapped to `metadata.description` if `level` is empty. Concatenated with `error.message` to form the `security_result.summary` field for HTTP and TLS events.  
tls.client.ja3 | network.tls.client.ja3 | Directly mapped from the raw log field `tls.client.ja3`.  
tls.client.server_name | network.tls.client.server_name | Directly mapped from the raw log field `tls.client.server_name`.  
tls.client.supported_ciphers | network.tls.client.supported_ciphers | Each element in the `tls.client.supported_ciphers` array is processed and mapped to the `network.tls.client.supported_ciphers` array.  
tls.cipher | network.tls.cipher | Directly mapped from the raw log field `tls.cipher`.  
tls.detailed.server_certificate.not_after | network.tls.server.certificate.not_after | Directly mapped from the raw log field `tls.detailed.server_certificate.not_after` after converting it to a timestamp.  
tls.detailed.server_certificate.not_before | network.tls.server.certificate.not_before | Directly mapped from the raw log field `tls.detailed.server_certificate.not_before` after converting it to a timestamp.  
tls.detailed.server_certificate.serial_number | network.tls.server.certificate.serial | Directly mapped from the raw log field `tls.detailed.server_certificate.serial_number`.  
tls.detailed.server_certificate.version | network.tls.server.certificate.version | Directly mapped from the raw log field `tls.detailed.server_certificate.version` after converting it to a string.  
tls.established | network.tls.established | Directly mapped from the raw log field `tls.established`.  
tls.next_protocol | network.tls.next_protocol | Directly mapped from the raw log field `tls.next_protocol`.  
tls.resumed | network.tls.resumed | Directly mapped from the raw log field `tls.resumed`.  
tls.server.hash.sha1 | network.tls.server.certificate.sha1 | Directly mapped from the raw log field `tls.server.hash.sha1` after converting it to lowercase.  
tls.server.issuer | network.tls.server.certificate.issuer | Directly mapped from the raw log field `tls.server.issuer`.  
tls.server.subject | network.tls.server.certificate.subject | Directly mapped from the raw log field `tls.server.subject`.  
tls.version | network.tls.version | Directly mapped from the raw log field `tls.version`.  
tls.version_protocol | network.tls.version_protocol | Directly mapped from the raw log field `tls.version_protocol`.  
type |  | Used to determine if the event is a DNS event.  
url.full | principal.url (INBOUND) / target.url (OUTBOUND) | Mapped based on the `network.direction` field. If INBOUND, it's mapped to `principal.url`. If OUTBOUND, it's mapped to `target.url`.  
user_id | target.user.userid | Directly mapped from the raw log field `user_id`.  
user_name | target.user.user_display_name | Directly mapped from the raw log field `user_name`.  
| metadata.event_type | Set to `GENERIC_EVENT` by default. Changed to specific event types based on the log source and event data.  
| metadata.vendor_name | Set to `Elastic` by default.  
| metadata.product_name | Set to `PacketBeat` by default.  
| security_result.action | Set to `ALLOW` by default.  
| metadata.log_type | Set to `ELASTIC_PACKETBEATS` by default.  
`rCode` | `dns.response_code` | Mapped from changelog  
`dhcpv4.flags", "dhcpv4.hardware_type", "dhcpv4.option.rebinding_time_sec", "dhcpv4.option.rebinding_time_sec", "dhcpv4.option.renewal_time_sec", and "dhcpv4.option.max_dhcp_message_size` | `security_result.detection_fields` | Mapped from changelog  
`dhcpv4.option.parameter_request_list", and "dhcpv4.option.dns_servers` | `additional.fields` | Mapped from changelog  
`dhcpv4.hops` | `network.dhcp.hops` | Mapped from changelog  
`dhcpv4.relay_ip` | `network.dhcp.giaddr` | Mapped from changelog  
`dhcpv4.option.domain_name` | `network.dhcp.client_hostname` | Mapped from changelog  
`dhcpv4.option.router` | `network.dhcp.ciaddr` | Mapped from changelog  
`dhcpv4.seconds` | `network.dhcp.seconds` | Mapped from changelog  
`headers.accept_encoding" and "headers.x_envoy_attempt_count` | `security_result.about.labels` | Mapped from changelog  
`headers.content_length", "headers.content_type", "headers.x_forwarded_proto", "headers.x_b3_sampled", "headers.http_accept", "headers.x_b3_parentspanid", "headers.x_envoy_original_path", "client_cert" and "headers.x_request_id` | `additional.labels` | Mapped from changelog  
`headers.x_forwarded_for" and "host` | `principal.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-packetbeats-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
