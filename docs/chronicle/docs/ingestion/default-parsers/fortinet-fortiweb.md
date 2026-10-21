---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiweb/
title: Collect Fortinet FortiWeb logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:16:22.015912+00:00
---

# Collect Fortinet FortiWeb logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiweb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet FortiWeb logs

**Parser Version:** 28.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortinet FortiWeb logs to Google Security Operations using Bindplane.

The parser extracts fields from Fortinet FortiWeb KV formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Fortinet FortiWeb web interface



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/chronicle_w_labels:
                compression: gzip
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: 'FORTINET_FORTIWEB'
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

      * `creds_file_path`: Full path to ingestion authentication file: 
        * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
        * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
      * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section
      * `endpoint`: Regional endpoint URL: 
        * **US** : `malachiteingestion-pa.googleapis.com`
        * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
        * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
        * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
      * `log_type`: Log type exactly as it appears in Chronicle (`FORTINET_FORTIWEB`)



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
             




## Configure Fortinet FortiWeb syslog forwarding

  1. Sign in to the **FortiWeb** web interface.
  2. Go to **Log & Report > Log Config > Other Log Settings**.
  3. Under **Syslog Policy** , click **Create New** to add a new syslog policy.
  4. Provide the following configuration details: 
     * **Policy Name** : Enter a descriptive name (for example, `Google-SecOps-Bindplane`).
     * **IP Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Enable** : Select **Enable**.
     * **Facility** : Select **local0** (or your preferred facility).
     * **Log Level** : Select **information** (or your preferred level).
  5. In the **Log Type** section, enable the following: 
     * **Attack Log**
     * **Event Log**
     * **Traffic Log**
  6. Click **OK** to save.
  7. Verify syslog messages are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
action | additional.fields[].value.string_value | Value is directly mapped.  
action | security_result.action_details | If action is "Allow" or "accept", security_result.action_details is set to "ALLOW". If action is "Denied", "deny", "block", or "Block", security_result.action_details is set to "BLOCK".  
app | network.application_protocol | Value is directly mapped after being uppercased. Only if value is one of HTTPS, HTTP, DNS, DHCP, SMB.  
app_name | additional.fields[].key | Key is set to "appName".  
app_name | additional.fields[].value.string_value | Value is directly mapped.  
backend_service | additional.fields[].key | Key is set to "backend_service".  
backend_service | additional.fields[].value.string_value | Value is directly mapped.  
cat | security_result.category_details | Value is directly mapped.  
client_level | security_result.category | If client_level is "Malicious", security_result.category is set to "NETWORK_MALICIOUS".  
cn1 | additional.fields[].value.string_value | Mapped to threatWeight field.  
cn1Label | additional.fields[].key | Key is set to cn1Label value.  
cn2 | additional.fields[].value.string_value | Mapped to length field.  
cn2Label | additional.fields[].key | Key is set to cn2Label value.  
cn3 | additional.fields[].value.string_value | Mapped to signatureID field.  
cn3Label | additional.fields[].key | Key is set to cn3Label value.  
cs1 | additional.fields[].value.string_value | Value is directly mapped.  
cs1Label | additional.fields[].key | Key is set to cs1Label value.  
cs1 | principal.user.product_object_id | Value is directly mapped when cs1Label matches "userID" (case-insensitive).  
cs2 | additional.fields[].value.string_value | Value is directly mapped.  
cs2Label | additional.fields[].key | Key is set to cs2Label value.  
cs2 | principal.user.userid | Value is directly mapped when cs2Label matches "userName" (case-insensitive) and suid is empty.  
cs3 | additional.fields[].value.string_value | Value is directly mapped.  
cs3Label | additional.fields[].key | Key is set to cs3Label value.  
cs3 | metadata.severity | Value is directly mapped when cs3Label is "level" and cs3 is not empty.  
cs4 | additional.fields[].value.string_value | Mapped to subType field.  
cs4Label | additional.fields[].key | Key is set to cs4Label value.  
cs5 | additional.fields[].value.string_value | Mapped to threatLevel field.  
cs5Label | additional.fields[].key | Key is set to cs5Label value.  
cs6 | additional.fields[].value.string_value | Mapped to owaspTop10 field.  
cs6Label | additional.fields[].key | Key is set to cs6Label value.  
date | metadata.event_timestamp.seconds | Combined with time and parsed to generate epoch seconds.  
dev_id | principal.resource.id | Value is directly mapped.  
devname | principal.resource.name | Value is directly mapped.  
device_event_class_id | metadata.product_event_type | Used in CEF parsing.  
device_product | metadata.product_name | Used in CEF parsing.  
device_vendor | metadata.vendor_name | Used in CEF parsing.  
device_version | metadata.product_version | Used in CEF parsing.  
dhost | target.hostname | Value is directly mapped.  
dpt | target.port | Value is directly mapped and converted to integer.  
dst | target.ip | Value is directly mapped.  
dst_port | target.port | Value is directly mapped and converted to integer.  
dstepid | target.process.pid | Value is directly mapped.  
dsteuid | target.user.userid | Value is directly mapped.  
event_name | metadata.product_event_type | Used in CEF parsing.  
http_agent | network.http.parsed_user_agent | Value is parsed as a user agent string.  
http_method | network.http.method | Value is directly mapped.  
http_refer | network.http.referral_url | Value is directly mapped.  
http_session_id | network.session_id | Value is directly mapped.  
http_url | target.url | Value is directly mapped.  
http_version | metadata.product_version | Value is directly mapped.  
length | additional.fields[].key | Key is set to "length".  
length | additional.fields[].value.string_value | Value is directly mapped.  
log_type | metadata.log_type | Hardcoded to "FORTINET_FORTIWEB".  
main_type | additional.fields[].key | Key is set to "mainType".  
main_type | additional.fields[].value.string_value | Value is directly mapped.  
message | Various fields | Parsed using grok and kv filters to extract different fields.  
ml_allow_method | additional.fields[].key | Key is set to "ml_allow_method".  
ml_allow_method | additional.fields[].value.string_value | Value is directly mapped.  
ml_arg_dbid | additional.fields[].key | Key is set to "ml_arg_dbid".  
ml_arg_dbid | additional.fields[].value.string_value | Value is directly mapped.  
ml_domain_index | additional.fields[].key | Key is set to "ml_domain_index".  
ml_domain_index | additional.fields[].value.string_value | Value is directly mapped.  
ml_log_arglen | additional.fields[].key | Key is set to "ml_log_arglen".  
ml_log_arglen | additional.fields[].value.string_value | Value is directly mapped.  
ml_log_hmm_probability | additional.fields[].key | Key is set to "ml_log_hmm_probability".  
ml_log_hmm_probability | additional.fields[].value.string_value | Value is directly mapped.  
ml_log_sample_arglen_mean | additional.fields[].key | Key is set to "ml_log_sample_arglen_mean".  
ml_log_sample_arglen_mean | additional.fields[].value.string_value | Value is directly mapped.  
ml_log_sample_prob_mean | additional.fields[].key | Key is set to "ml_log_sample_prob_mean".  
ml_log_sample_prob_mean | additional.fields[].value.string_value | Value is directly mapped.  
ml_svm_accuracy | additional.fields[].key | Key is set to "ml_svm_accuracy".  
ml_svm_accuracy | additional.fields[].value.string_value | Value is directly mapped.  
ml_svm_log_main_types | additional.fields[].key | Key is set to "ml_svm_log_main_types".  
ml_svm_log_main_types | additional.fields[].value.string_value | Value is directly mapped.  
ml_svm_log_match_types | additional.fields[].key | Key is set to "ml_svm_log_match_types".  
ml_svm_log_match_types | additional.fields[].value.string_value | Value is directly mapped.  
ml_url_dbid | additional.fields[].key | Key is set to "ml_url_dbid".  
ml_url_dbid | additional.fields[].value.string_value | Value is directly mapped.  
monitor_status | additional.fields[].key | Key is set to "monitor_status".  
monitor_status | additional.fields[].value.string_value | Value is directly mapped.  
msg | metadata.description | Value is directly mapped.  
owasp_top10 | additional.fields[].key | Key is set to "owaspTop10".  
owasp_top10 | additional.fields[].value.string_value | Value is directly mapped.  
principal_app | principal.application | Value is directly mapped.  
principal_host | principal.hostname | Value is directly mapped.  
proto | network.ip_protocol | Value is directly mapped after being uppercased.  
request | target.url | Value is directly mapped.  
requestMethod | network.http.method | Value is directly mapped.  
rt | metadata.event_timestamp.seconds | Parsed as milliseconds since epoch and converted to seconds.  
security_result.severity | security_result.severity | Derived from severity_level. Mapped to different UDM severity values based on the raw log value. Defaults to UNKNOWN_SEVERITY if no match is found.  
server_pool_name | additional.fields[].key | Key is set to "server_pool_name".  
server_pool_name | additional.fields[].value.string_value | Value is directly mapped.  
service | network.application_protocol | Value is directly mapped after being uppercased.  
service | target.application | Value is directly mapped after being uppercased if it's not one of HTTPS, HTTP, DNS, DHCP, or SMB.  
severity | security_result.severity | If severity is empty and cs3Label is "level", the value of cs3 is used. Then mapped to a UDM severity value (LOW, HIGH, etc.).  
signature_id | security_result.rule_id | Value is directly mapped.  
signature_subclass | security_result.detection_fields[].key | Key is set to "signature_subclass".  
signature_subclass | security_result.detection_fields[].value | Value is directly mapped.  
src | principal.ip | Value is directly mapped.  
src_country | principal.location.country_or_region | Value is directly mapped.  
src_ip | principal.ip | Value is directly mapped.  
src_port | principal.port | Value is directly mapped and converted to integer.  
srccountry | principal.location.country_or_region | Value is directly mapped.  
sub_type | additional.fields[].key | Key is set to "subType".  
sub_type | additional.fields[].value.string_value | Value is directly mapped.  
subtype | target.resource.resource_subtype | Value is directly mapped.  
suid | principal.user.userid | Value is directly mapped.  
threat_level | additional.fields[].key | Key is set to "threatLevel".  
threat_level | additional.fields[].value.string_value | Value is directly mapped.  
threat_weight | security_result.detection_fields[].key | Key is set to "threat_weight".  
threat_weight | security_result.detection_fields[].value | Value is directly mapped.  
time | metadata.event_timestamp.seconds | Combined with date and parsed to generate epoch seconds.  
user_id | principal.user.product_object_id | Value is directly mapped.  
user_name | additional.fields[].key | Key is set to "userName".  
user_name | additional.fields[].value.string_value | Value is directly mapped.  
user_name | principal.user.userid | Value is directly mapped.  
N/A | metadata.event_type | Set to "NETWORK_CONNECTION" if both principal.ip and target.ip are present. Set to "USER_UNCATEGORIZED" if principal.ip and principal.user are present. Set to "STATUS_UPDATE" if only principal.ip is present. Otherwise, set to "GENERIC_EVENT".  
N/A | metadata.log_type | Hardcoded to "FORTINET_FORTIWEB".  
N/A | metadata.product_name | Hardcoded to "FORTINET FORTIWEB" or "FortiWEB Cloud" based on the log format.  
N/A | metadata.vendor_name | Hardcoded to "FORTINET" or "Fortinet" based on the log format.  
N/A | principal.resource.resource_type | Hardcoded to "DEVICE" if dev_id is present.  
`http_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`timezone` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`eventtime` | `event1.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`http_request_time` | `event1.idm.read_only_udm.additional.fields` | Mapped from changelog  
`http_response_time` | `event1.idm.read_only_udm.additional.fields` | Mapped from changelog  
`subtype` | `event1.idm.read_only_udm.additional.fields` | Mapped from changelog  
`original_src` | `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`attack_type` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`matched_pattern` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`principal_hostnamne` | `principal.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiweb-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
