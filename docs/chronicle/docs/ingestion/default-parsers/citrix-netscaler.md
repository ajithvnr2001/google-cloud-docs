---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-netscaler/
title: Collect NetScaler (formerly Citrix NetScaler) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:51.179934+00:00
---

# Collect NetScaler (formerly Citrix NetScaler) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-netscaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect NetScaler (formerly Citrix NetScaler) logs

**Parser Version:** 28.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest NetScaler (formerly known as Citrix NetScaler) logs to Google Security Operations using Bindplane.

The parser extracts fields from NetScaler syslog and key-value formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

**Note:** Certain critical security logs, such as Web Server Access logs (`/var/log/httpaccess.log`), Error logs (`/var/log/httperror*`), and internal system messages (`/var/log/messages`), reside on the appliance's local file system. Because security agents cannot be installed directly on a hardened NetScaler appliance, these logs must be collected either by configuring NetScaler to stream these specific events using the Audit Syslog pipeline, or by using an intermediate Linux server to periodically pull these files (via `SCP` or `SFTP`) and forwarding them to Google SecOps using Bindplane.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the NetScaler web interface



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
            log_type: 'CITRIX_NETSCALER'
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

Replace the following placeholders:

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
    * `log_type`: Log type exactly as it appears in Google SecOps (`CITRIX_NETSCALER`)



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'CITRIX_NETSCALER'
            raw_log_field: body
            ingestion_labels:
        


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
         




## Configure syslog forwarding on NetScaler

  1. Sign in to the **NetScaler** web interface (NSIP).
  2. Go to **System > Auditing > Syslog**.
  3. Click **Servers** tab.
  4. Click **Add** to create a new syslog server.
  5. Provide the following configuration details:

     * **Name** : Enter a descriptive name (for example, `Google-SecOps-Bindplane`).
     * **Server IP** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Log Level** : Select all applicable levels:

       * **ALL** (recommended for comprehensive logging)

**Note:** Verify your NetScaler version and auditing configuration to ensure standard HTTP/Web server events are included in this Syslog stream.
     * **Facility** : Select **LOCAL0** (or your preferred facility).

     * **Date Format** : Select **MMDDYYYY**.

     * **Time Zone** : Select **GMT_TIME** (UTC recommended).

     * **TCP Logging** : Select **NONE** (for UDP).

     * **Log Facility** : Select **LOCAL0**.

  6. Click **Create**.

  7. Go to the **Policies** tab.

  8. Click **Add** to create a new syslog audit policy.

  9. Provide the following configuration details:

     * **Name** : Enter a descriptive name (for example, `Google-SecOps-Policy`).
     * **Server** : Select the syslog server created earlier.
  10. Click **Create**.

  11. Bind the policy globally:

     1. Go to **System > Auditing**.
     2. Click **Global Bindings** under **Syslog Audit Policies**.
     3. Click **Add Binding**.
     4. Select the policy created earlier.
     5. Click **Bind**.
  12. Verify syslog messages are being sent by checking the Bindplane agent logs.



  * Alternatively, configure via CLI:
        
        add audit syslogAction Google-SecOps-Bindplane BINDPLANE_IP -serverPort 514 -logLevel ALL -dateFormat MMDDYYYY -timeZone GMT_TIME
        add audit syslogPolicy Google-SecOps-Policy ns_true Google-SecOps-Bindplane
        bind audit syslogGlobal -policyName Google-SecOps-Policy -priority 100
        




Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.

**Note:** The parser is equipped to parse both standard Syslog events and HTTP access logs. Ensure your ingestion method is correctly configured to supply the raw fields listed in the following table.

## UDM mapping table

Log field | UDM mapping  
---|---  
aaa_info_flags | additional.fields  
aaa_trans_id | security_result.detection.fields  
aaad_flags | additional.fields  
aaad_resp | additional.fields  
aaaFlags | additional.fields  
aaaFlags2 | additional.fields  
act | securtiy_result.action_details,, security_result.action  
action | security_result.action  
ADM_User | additional.fields  
allowed_interface | security_result.detection.fields  
applicationname | target.application  
auth_type | additional.fields  
authActionLen | security_result.detection_fields  
AuthAgent | additional.fields  
AuthDuration | network.session_duration.seconds  
authnvs | additional.fields  
authorizationStatus | security_result.detection.fields  
AuthStage | additional.fields  
Authtype | additional.fields  
C | principal.location.country_or_region  
caseId | additional.fields  
cfg_limit | additional.fields  
cgp_tag | sec_result.detection_fields  
channel_id_X | additional.fields  
channel_id_X_val | additional.fields  
channel_update_begin | additional.fields  
channel_update_end | additional.fields  
cipher_suite | network.tls.cipher  
client_fip | target.ip target.asset.ip  
client_fport | target.port  
client_ip | principal.ip,, principal.asset.ip  
client_port | principal.port  
Client_security_expression | additional.fields  
client_type | additional.fields  
client_version | network.tls.version  
client.nat.ip | principal.nat_ip,, principal.asset.nat_ip  
clientside_jitter | additional.fields  
clientside_packet_retransmits | additional.fields  
clientside_rtt | additional.fields  
clientside_rxbytes | network.sent_bytes  
clientside_txbytes | network.received_bytes  
ClientVersion | network.tls.version_protocol  
CN | principal.resource.attribute.labels  
cn1 | additional.fields  
cn2 | additional.fields  
code | additional.fields  
commandExecutionStatus | security_result.action_details  
Compression_ratio_recv | additional.fields  
Compression_ratio_send | additional.fields  
configurationCmd | security_result.detection.fields  
connectionId | network.session_id  
copied_nsb | sec_result.detection_fields  
core_id | additional.fields  
core_refmask | additional.fields  
cs1 | additional.fields  
cs2 | additional.fields  
cs4 | additional.fields  
cs5 | additional.fields  
cs6 | additional.fields  
CSappid | additional.fields  
CSAppname | -  
csg_flags | additional.fields  
ctx_flags | additional.fields  
cur_attempts | additional.fields  
CurfactorPolname | additional.fields  
customername | additional.fields  
days_for_pwd_exp | additional.fields  
days_for_pwd_exp_STR | additional.fields  
delinkTime | additional.fields  
Denied_by_policy | security_result.rule_name  
desc | metadata.description  
destination.ip | target.ip,, target.asset.ip  
destination.port | target.resource.attribute.labels  
device_event_class_id | metadata.product_event_type  
device_version | metadata.product_version  
Deviceid | target.resource.product_object_id  
Devicetype | additional.fields  
dht_delete_status | additional.fields  
diagnostic_info | additional.fields  
digestSignatureAlgorithm | security_result.detection_fields  
dns_additional_count | additional.fields  
dns_answer_count | additional.fields  
dns_authority_count | additional.fields  
dns_flags | additional.fields  
dns_flags_raw | network.dns.recursion_desired  
dns_flags_raw | network.dns.recursion_available  
dns_id | network.dns.id  
dns_question_count | additional.fields  
dns_question_name | network.dns.question.name  
domain | security_result.detection.fields,, additional.fields  
domain | target.administrative_domain  
ecs_version | additional.fields  
encrypt_status | security_result.detection_fields  
end_time | additional.fields  
End_time | additional.fields  
entityName | target.resource.name  
Error Code | additional.fields  
event_id | metadata.product_log_id  
event_name | metadata.product_event_type  
event_type | sec_result.summary  
expired_refmask | additional.fields  
factor | security_result.detection.fields  
flags | additional.fields  
flags2 | additional.fields  
flags3 | additional.fields  
flags4 | additional.fields  
func | security_result.detection_fields  
geolocation | location.country_region  
Group(s) | target.user.group_identifiers  
Group(s) | target.user.group.identifiers  
handshake_time | network.session_duration.seconds  
HandshakeTime | additional.fields  
host_hostname | principal.hostname  
host_ip | principal.ip principal.asset.ip  
host.name | target.hostname,, target.asset.hostname  
hostname | intermediary.hostname,, intermediary.asset.hostname  
hostname | target.hostname,, target.asset.hostname  
hostname_1 | target.hostname,, target.asset.hostname  
http_method | network.http.method  
Http_resources_accessed | security_result.detection.fields  
http_uri | target.url  
HTTPS | network.application_protocol  
ica_conn_owner_refmask | sec_result.detection_fields  
ica_rtt | additional.fields  
ica_uuid | network.session_id  
ICAUUID | network.session_id  
id | metadata.id  
init_icamode_homepage | additional.fields  
inter_hostname | intermediary.hostname  
interfaceKind | security_result.detection.fields  
ip | intermediary.asset.ip  
ip_x | principal.ip principal.asset.ip  
ipaddress | target.ip,, target.asset.ip  
is_post | additional.fields  
IssuerName | network.tls.server.certificate.issuer  
L | principal.location.city  
last_contact | additional.fields  
loc | target.url  
localdate | additional.fields  
lock_duration | additional.fields  
log_action | sec_result.detection_fields  
log_action | security_result.detection.fields  
log_category | additional.fields  
log_data | additional.fields  
log_format | additional.fields  
log_timestamp | additional.fields  
log_type | additional.fields  
log.syslog.priority | additional.fields  
login_count | sec_result.detection_fields  
login_count | security_result.detection_fields  
LogoutMethod | additional.fields  
max_attempts | additional.fields  
message_content | security_result.summary  
message_id | metadata.product_log_id  
message_status_code | additional.fields  
method | network.http.method  
monitored_resource | additional.fields  
msg | metadata.description  
msi_client_cookie | additional.fields  
msticks | additional.fields  
Nat_ip | additional.fields,, principal.nat_ip,, principal.asset.nat_ip, (If the Nat_ip isn't an IP address, it is in additional.fields.)  
netscaler_principal_ip_context | principal.resource.attribute.labels  
netscaler_tag | intermediary.asset.product_object_id  
netscaler_target_ip_context | target.resource.attribute.labels  
new_webview | additional.fields  
newWebview | additional.fields  
NonHttp_services_accessed | security_result.detection.fields  
nsPartitionName | additional.fields  
on_port | additional.fields  
Organization | principal.resource.attribute.labels  
OU | principal.resource.attribute.labels  
owner_from | additional.fields  
owner_id | additional.fields  
pcb_devno | additional.fields  
pcbdevno | additional.fields  
Policyname | security_result.rule_name  
port | principal.port  
port_details | principal.port  
prin_ip | principal.ip principal.asset.ip  
prin_user | principal.user.userid  
principal_ip | principal.ip,, principal.asset.ip  
principal_port | principal.port  
prod_event_type | metadata.product_event_type  
protocol | network.ip_protocol  
protocol_feature | security_result.detection.fields  
ProtocolVersion | network.tls.protocol_version  
pwdlen | additional.fields  
pwdlen2 | additional.fields  
q_flags | additional.fields  
reason_val | security_result.description  
receiver_version | additional.fields  
record_type | network.dns.question.type  
refmask | additional.fields  
remote_ip | principal.ip principal.asset.ip  
remote_port | principal.port  
request | target.url  
ReqURL | additional.fields  
resource_cmd | target.resource.name  
resource_name | principal.resource.name  
response | additional.fields  
response_code | additional.fields  
rule_id | security_result.rule.id  
rule_name | security_result.rule_name  
SerialNumber | network.tls.server.certificate.serial  
server_authenticated | additional.fields  
serverside_jitter | additional.fields  
serverside_packet_retransmits | additional.fields  
serverside_rtt | additional.fields  
service_name | principal.applications  
sess_flags2: | additional.fields  
sess_seq | network.session_id  
sessFlags2 | additional.fields  
Session | additional.fields  
session_cookie | security_result.detection_fields  
session_guid | network.session_id  
session_id_label | network.session_id  
session_setup_time | additional.fields  
session_type | sec_result.description  
SessionId | network.session_id  
skip_code | additional.fields  
source_file | additional.fields  
source_hostname | principal.hostname,, principal.asset.hostname  
source_line | additional.fields  
source.ip | principal.ip,, principal.asset.ip  
source.port | principal.resource.attribute.labels  
spcb_id | security_result.detecrion.fields  
SPCBId | sec_result.detection_fields  
spt | principal.port  
src | principal.ip principal.asset.ip  
src_hostname | principal.hostname principal.asset.hostname  
src_ip | principal.ip principal.asset.ip  
src_ip1 | src.ip,, src.asset.ip  
src_port | principal.port  
ssid | network.session_id  
SSLVPN_client_type | additional.fields  
SSO | additional.fields  
sso | additional.fields  
sso_auth_type | additional.fields  
sso_flags | security_result.detection_fields  
sso_state | additional.fields  
SSOduration | additional.fields  
SSOurl | additional.fields  
ssoUsername | additional.fields  
ssoUsername2 | additional.fields  
ST | principal.location.state  
sta_port | additional.fields  
sta_ticket | additional.fields  
start_time | additional.fields  
Start_time | additional.fields  
State | security_result.action_details  
state | additional.fields  
state_value | additional.fields  
StatusCode | additional.fields  
SubjectName | network.tls.client.certificate.subject  
summ | security_result.summary  
summary | security_result.summary  
sysCmdPolLen | security_result.detection.fields  
syslog_priority | additional.fields  
tags | additional.fields  
tar_ip | target.ip target.asset.ip  
tar_port | target.port  
target_id | target.resource.id  
target_port | target.port  
TCP | network.ip_protocol  
timeout_ms | additional.fields  
timestamp | metadata.event_timestamp  
Total_bytes_send | network.sent_bytes  
Total_compressedbytes_recv | additional.fields  
Total_compressedbytes_send | additional.fields  
Total_policies_allowed | security_result.detection.fields  
Total_policies_denied | security_result.detection.fields  
Total_TCP_connections | security_result.detection.fields  
Total_UDP_flows | security_result.detection.fields  
track_flags | additional.fields  
trans_id | -  
tt | metadata.event_timestamp  
User | principal.user.userid  
user_agent.original | network.http.user_agent  
user_email | principal.user.email_addresses  
user_id | principal.user.userid  
user.domain | target.administrative_domain  
user.name | principal.user.user_display_name  
userids | target.user.userid  
ValidFrom | network.tls.server.certificate.not_before  
ValidTo | network.tls.server.certificate.not_after  
version | additional.fields  
VPNexportState | additional.fields  
Vport | target.port  
Vserver Timestamp | additional.fields  
vserver_id | target.resource.product_object_id  
Vserver_ip | target.ip,, target.asset.ip  
vserver_port | target.port  
Vserver_port | target.port  
vserver_timestamp | additional.fields  
vserver.ip | target.ip,, target.asset.ip  
wirep | additional.fields  
wirep_name | additional.fields  
wirep_ref_cnt | additional.fields  
`url_value` | `event.idm.read_only_udm.target.url`  
`host_port` | `event.idm.read_only_udm.additional.fields`  
`region` | `event.idm.read_only_udm.principal.location.country_or_region`  
`NAT_IP` | `event.idm.read_only_udm.principal.nat_ip` and `event.idm.read_only_udm.principal.asset.nat_ip`  
`USER` | `event.idm.read_only_udm.target.user.userid`  
`URL` | `event.idm.read_only_udm.additional.fields`  
`proxy_action` | `event.idm.read_only_udm.security_result.action_details`  
`SRC_IP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`  
`HOST` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`  
`url_port` | `event.idm.read_only_udm.target.port`  
`User-Agent` | `event.idm.read_only_udm.network.http.user_agent`  
`User-Agent` | `event.idm.read_only_udm.network.http.parsed_user_agent`  
`PROXY_IP` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`  
`proxy_action` | `event.idm.read_only_udm.security_result.action`  
`v_ip` | `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip`  
`v_port` | `event.idm.read_only_udm.observer.port`  
`gwip` | `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip`  
`gwport` | `event.idm.read_only_udm.observer.port`  
`Username` | `event.idm.read_only_udm.principal.user.userid`  
`VPNfqdn` | `event.idm.read_only_udm.target.hostname`  
`VPNfqdn` | `event.idm.read_only_udm.target.asset.hostname`  
`VPNfqdn` | `event.idm.read_only_udm.target.ip`  
`VPNfqdn` | `event.idm.read_only_udm.target.asset.ip`  
`Remote ip` | `event.idm.read_only_udm.principal.ip`  
`Remote ip` | `event.idm.read_only_udm.principal.asset.ip`  
`Remote ip` | `event.idm.read_only_udm.principal.port`  
`BackendIP` | `event.idm.read_only_udm.target.ip`  
`BackendIP` | `event.idm.read_only_udm.target.asset.ip`  
`BackendIP` | `event.idm.read_only_udm.target.port`  
`ts` | `event.idm.read_only_udm.metadata.event_timestamp`  
`id` | `event.idm.read_only_udm.metadata.product_log_id`  
`policy` | `event.idm.read_only_udm.security_result.detection_fields`  
`Nat_ip` | `event.idm.read_only_udm.principal.nat_ip`  
`v_ip` | `event.idm.read_only_udm.intermediary.ip`  
`v_port` | `event.idm.read_only_udm.intermediary.port`  
`event_id` | `event.idm.read_only_udm.additional.fields`  
`Nat_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`  
`Nat_port` | `event.idm.read_only_udm.principal.nat_port`  
`v_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`  
`v_port` | `event.idm.read_only_udm.target.port`  
`delinkTime` | `event.idm.read_only_udm.additional.fields`  
`hostname` | `event.idm.read_only_udm.intermediary.hostname`  
`intermediary_ip` | `intermediary.ip`  
`Remote_ip` | `target.ip`  
`VserverIP` | `src.ip`  
`VserverPort` | `src.port`  
`Start_time` | `sec_result.first_discovered_time`  
`End_time` | `sec_result.last_discovered_time`  
`prin_ip` | `principal.ip and principal.asset.ip`  
`user_prin` | `principal.user.userid`  
`trans id` | `security_result.detection_fields`  
`request` | `principal.url`  
`Client_ip` | `principal.ip`  
`Errmsg` | `metadata.description`  
`Sessionid` | `network.session_id`  
`user_name" and "user` | `target.user.userid`  
`Authentication details` | `security_result.description`  
`Browser` | `network.http.parsed_user_agent`  
`ClientIP` | `principal.asset.ip`  
`type", "aaa_trans_id", "pcb_trans_id", "pcb_state", "pcb_label", "trans_id", "authPolicyLen", "login_attempts", "PromptLen", "partitionLen", "cmdPolicyLen", and "ssh_pubkey_len` | `security_result.detection_fields`  
`principal_hostname` | `principal.hostname`  
`hostname` | `observer.asset.hostname`  
`cip", "ServerIP", "VIP", "VserverServiceIP", and "Remote_ip` | `target.asset.ip`  
`startTime", "endTime", "Duration` | `security_result.detection_fields`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-netscaler-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
