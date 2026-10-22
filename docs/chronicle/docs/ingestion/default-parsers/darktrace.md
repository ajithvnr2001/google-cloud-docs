---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/darktrace/
title: Collect Darktrace logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:27.568567+00:00
---

# Collect Darktrace logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/darktrace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Darktrace logs

**Parser Version:** 19.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Darktrace logs to Google Security Operations using the Bindplane agent.

Darktrace is an AI-powered cybersecurity platform that detects threats and anomalies in real time. The parser handles both CEF and JSON formatted Darktrace logs, extracting fields and mapping them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Darktrace appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Darktrace web UI



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
            listen_address: "0.0.0.0:10282"
        
        exporters:
          chronicle/darktrace:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: DARKTRACE
            raw_log_field: body
        
        service:
          pipelines:
            logs/darktrace_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/darktrace
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `10282` is the default Darktrace CEF syslog port (adjust as needed)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/darktrace:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: DARKTRACE
            raw_log_field: body
        


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
             




## Configure syslog on Darktrace

  1. Sign in to the **Darktrace** web UI.
  2. Go to **Admin > System Config**.
  3. Click **Verify Alert Settings**.
  4. Provide the following configuration details: 
     * **CEF Syslog Alerts** : Select **True**.
     * **CEF Syslog Server** : Enter the Bindplane IP address.
     * **CEF Syslog Server Port** : Enter the Bindplane port number (for example, `10282`).
     * **CEF Syslog TCP Alert** : Select **True**.
  5. Click **Save**.



## Supported Darktrace sample logs

  * SYSLOG + KV (CEF)
        
        {
        "acknowledged": false,
        "commentCount": 0,
        "pbid": 900000001,
        "time": 1604055367000,
        "creationTime": 1604055367000,
        "model": {
            "name": "Compromise::Agent Beacon to New Endpoint",
            "uuid": "dfd6f10b-b91c-4244-9fd5-7c35caf21b33",
            "description": "A device is initiating multiple connections to a new external endpoint...",
            "priority": 2,
            "category": "Informational",
            "mitre": {
            "tactics": [
                "command-and-control"
            ],
            "techniques": [
                "T1071.001"
            ]
            }
        },
        "triggeredComponents": [
            {
            "time": 1677679818000,
            "ip": " ",
            "port": 443,
            "metric": {
                "name": "externalconnections"
            },
            "triggeredFilters": [
                {
                "filterType": "Connection hostname",
                "trigger": {
                    "value": "beacon.external.io"
                }
                }
            ]
            }
        ],
        "score": 0.85,
        "device": {
            "did": 90001,
            "macaddress": " ",
            "ip": " ",
            "hostname": "user-laptop-1"
        }
        }
        

  * SYSLOG + JSON
        
        {
        "dpi_engine": "dt-sensor-101",
        "proto": "tcp",
        "source_ip": " ",
        "source_port": 51000,
        "dest_ip": " ",
        "dest_port": 389,
        "src": " ",
        "dst": " ",
        "details": "AP request: srealm is [TESTDOMAIN.LOCAL], service is [LDAP/DC99.testdomain.local/testdomain.local], ST cipher is [aes256-cts-hmac-sha1-96]",
        "epochdate": 1690471502.2252,
        "@host": "log-collector-host",
        "uid": "ABCDEFGHIJ1234567890",
        "note": "KERBEROS::App",
        "@type": "notice"
        }
        




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
darktraceUrl | security_result.url_back_to_product | The value is taken from the `darktraceUrl` field.  
darktrace_host | observer.hostname | The value is taken from the `darktrace_host` field if it is not an IP address.  
darktrace_ip | observer.ip | The value is taken from the `darktrace_ip` field.  
darktrace_user | observer.user.userid | The value is taken from the `darktrace_user` field.  
description | security_result.summary, metadata.description | The value is taken from the `description` field.  
device.customFields.DT-AUTO.macaddress | principal.mac | The value is taken from the `device.customFields.DT-AUTO.macaddress` field.  
device.did | principal.asset.asset_id | The value is taken from the `device.did` field, converted to a string, and prefixed with `Device ID:`.  
device.firstSeen | principal.asset.first_seen_time | The value is taken from the `device.firstSeen` field, converted to a string, and parsed as a UNIX timestamp in milliseconds.  
device.hostname | principal.hostname, principal.asset.hostname | The value is taken from the `device.hostname` field.  
device.ip | principal.ip, principal.asset.ip | The value is taken from the `device.ip` field if it matches the IP address format.  
device.ips.0.subnet | additional.fields.subnet | The value is taken from the `device.ips.0.subnet` field and prefixed with `subnet`.  
device.ips.ip | principal.ip, principal.asset.ip | The value is taken from the `device.ips.ip` field for each IP address in the list.  
device.lastSeen | principal.asset.last_discover_time | The value is taken from the `device.lastSeen` field, converted to a string, and parsed as a UNIX timestamp in milliseconds.  
device.macaddress | principal.mac | The value is taken from the `device.macaddress` field.  
device.objecttype | principal.asset.type | If the value is `device`, the UDM field is set to `WORKSTATION`.  
device.sid | principal.resource.attribute.labels.sid | The value is taken from the `device.sid` field and converted to a string.  
device.typelabel | principal.resource.attribute.labels.typelabel | The value is taken from the `device.typelabel` field.  
device.typename | principal.resource.attribute.labels.typename | The value is taken from the `device.typename` field.  
dst | target.ip, target.asset.ip | The value is taken from the `dst` field.  
dpt | target.port | The value is taken from the `dpt` field and converted to an integer.  
dvc | principal.ip, principal.asset.ip | If the value of `dvc` is an IP address, it is added to the UDM field.  
dvchost | principal.hostname, principal.asset.hostname | The value is taken from the `dvchost` field.  
endpoint | target.url | The value is taken from the `endpoint` field.  
event_time | metadata.event_timestamp | The value is taken from the `event_time` field and parsed as an ISO8601 timestamp.  
externalId | metadata.product_log_id | The value is taken from the `externalId` field.  
incidentEventUrl | principal.url | The value is taken from the `incidentEventUrl` field.  
ip | principal.ip, principal.asset.ip | The value is taken from the `ip` field if it matches the IP address format.  
issue_msg | security_result.summary | The value is taken from the `issue_msg` field.  
message | security_result.description | The value is taken from the `message` field.  
method | network.http.method | The value is taken from the `method` field.  
model.description | metadata.description | The value is taken from the `model.description` field.  
model.name | metadata.product_event_type | The value is taken from the `model.name` field.  
model.now.category | security_result.severity | If the value is `critical`, the UDM field is set to `CRITICAL`. If the value is `Informational`, the UDM field is set to `INFORMATIONAL`. If the value is `Suspicious`, the UDM field is set to `HIGH` and the category is set to `NETWORK_SUSPICIOUS`.  
model.now.description | metadata.description | The value is taken from the `model.now.description` field.  
model.now.message | security_result.description | The value is taken from the `model.now.message` field.  
model.now.name | metadata.product_event_type | The value is taken from the `model.now.name` field.  
model.now.pid | principal.process.pid | The value is taken from the `model.now.pid` field and converted to a string.  
model.now.uuid | principal.user.userid | The value is taken from the `model.now.uuid` field and the event type is set to `USER_UNCATEGORIZED`.  
model.pid | principal.process.pid | The value is taken from the `model.pid` field and converted to a string.  
model.then.description | principal.resource.attribute.labels.Model Then Description | The value is taken from the `model.then.description` field.  
model.then.name | principal.resource.attribute.labels.Model Then Name | The value is taken from the `model.then.name` field.  
model.then.pid | principal.resource.attribute.labels.Model Then Pid | The value is taken from the `model.then.pid` field and converted to a string.  
model.then.uuid | principal.resource.attribute.labels.Model Then UUID | The value is taken from the `model.then.uuid` field.  
model.uuid | principal.user.userid | The value is taken from the `model.uuid` field and the event type is set to `USER_UNCATEGORIZED`.  
relatedBreaches.0.modelName | security_result.description | The value is taken from the `relatedBreaches.0.modelName` field.  
score | security_result.priority, security_result.priority_details | If the value is between 0.8 and 1, the priority is set to `HIGH_PRIORITY`. If the value is between 0.5 and 0.79, the priority is set to `MEDIUM_PRIORITY`. If the value is between 0 and 0.49, the priority is set to `LOW_PRIORITY`. The priority details are set to `Score :` followed by the value of `score` converted to a string.  
severity | security_result.severity | If the value is 2, the UDM field is set to `MEDIUM`. If the value is greater than 2, the UDM field is set to `HIGH`.  
shost | principal.hostname, principal.asset.hostname | The value is taken from the `shost` field.  
smac | principal.mac | The value is taken from the `smac` field.  
src | principal.ip, principal.asset.ip | The value is taken from the `src` field.  
status | network.http.response_code | The value is taken from the `status` field and converted to a string.  
summary | metadata.description | The value is taken from the `summary` field.  
time |  | The value is taken from the `time` field, converted to a string, and parsed as a UNIX timestamp in milliseconds.  
timestamp |  | The value is taken from the `timestamp` field and parsed as either an ISO8601 timestamp or a UNIX timestamp in milliseconds.  
title | security_result.summary | The value is taken from the `title` field.  
triggeredComponents.ip | intermediary.ip | The value is taken from the `triggeredComponents.ip` field if it matches the IP address format.  
triggeredComponents.port | intermediary.port | The value is taken from the `triggeredComponents.port` field and converted to an integer.  
username | principal.user.userid | The value is taken from the `username` field.  
| metadata.vendor_name | Set to `DARKTRACE`.  
| metadata.product_name | Set to `DCIP`.  
| metadata.log_type | Set to `DARKTRACE`.  
| network.ip_protocol | Set to `TCP` if `issue_msg` doesn't contain `UDP`. Otherwise set to `UDP`.  
| security_result.action | Set to `BLOCK` if `status` is `401`, otherwise set to `ALLOW`.  
| security_result.severity | Set to `INFORMATIONAL`.  
| network.application_protocol | Set to `HTTP` if `method` is not empty.  
| metadata.event_type | Set to `NETWORK_HTTP` if `method` is not empty. Set to `USER_LOGIN` if `description` contains `logged into \\\\S+ over ssh`. Set to `NETWORK_CONNECTION` if `target_ip` is not empty. Otherwise, set to `STATUS_UPDATE`.  
| extensions.auth.type | Set to `MACHINE` if `description` contains `logged into \\\\S+ over ssh`.  
| security_result.category | Set to `DATA_EXFILTRATION` if `issue_msg` contains `Exfiltration`. Set to `NETWORK_MALICIOUS` if `issue_msg` contains `Compromise`. Otherwise, set to `NETWORK_SUSPICIOUS`.  
`percentScore` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`device.credentials` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`url` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`iris-event-type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`inhibitor` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`inhibitor` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`inhibitor` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`device.os` | `event.idm.read_only_udm.principal.platform` | Mapped from changelog  
`device.typename` | `event.idm.read_only_udm.principal.asset.type` | Mapped from changelog  
`device.ossource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`model.tags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`codeid` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`inhibitor` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`host_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`technique_data` | `event.idm.read_only_udm.security_result.attack_details.techniques` | Mapped from changelog  
`tactics_data` | `event.idm.read_only_udm.security_result.attack_details.tactics` | Mapped from changelog  
`model.created.userid` | `principal.user.userid` | Mapped from changelog  
`model.edited.userid` | `additional.fields` | Mapped from changelog  
`direction` | `network.direction` | Mapped from changelog  
`filterType" under "triggeredFilters` | `additional.fields` | Mapped from changelog  
`trigger.value" under "triggeredFilters` | `additional.fields` | Mapped from changelog  
`from` | `principal.user.email_addresses` | Mapped from changelog  
`subject` | `metadata.description` | Mapped from changelog  
`anomaly_score", "tags", "link_hosts", and "message_id` | `additional.fields` | Mapped from changelog  
`recipients` | `observer.user.email_addresses` | Mapped from changelog  
`attachment_sha1s" and "attachment_sha256s` | `security_result.detection_fields` | Mapped from changelog  
`triggeredFilter.trigger.value` | `target.ip` | Mapped from changelog  
`from` | `network.email.from` | Mapped from changelog  
`subject` | `network.email.subject` | Mapped from changelog  
`attachment_sha1s", "attachment_sha256s", "recipients", "link_hosts", "tags", "actions", "anomaly_score", "message_id` | `security_result.detection_fields` | Mapped from changelog  
`model.name` | `principal.user.user_display_name` | Mapped from changelog  
`breachUrl` | `security_result.url_back_to_product` | Mapped from changelog  
`device.typelabel", "device.sid", "device.typename` | `principal.resource.attribute.labels` | Mapped from changelog  
`device.ips.0.subnet` | `additional_fields` | Mapped from changelog  
`device.device.lastSeen` | `principal.asset.last_seen_time` | Mapped from changelog  
`mitreTechniques` | `security_result.attack_details.techniques` | Mapped from changelog  
`details` | `sec_result.about.resource.attribute.labels` | Mapped from changelog  
`principal_port_no` | `principal.port` | Mapped from changelog  
`location` | `principal.location.country_or_region` | Mapped from changelog  
`target_host` | `target.hostname` | Mapped from changelog  
`source_ip` | `principal.ip` | Mapped from changelog  
`source_port` | `principal.port` | Mapped from changelog  
`dest_ip` | `target.ip` | Mapped from changelog  
`dest_port` | `target.port` | Mapped from changelog  
`@host` | `principal.hostname` | Mapped from changelog  
`note` | `principal.application` | Mapped from changelog  
`@type` | `sec_result.about.resource.attribute.labels` | Mapped from changelog  
`opcode` | `sec_result.about.resource.attribute.labels` | Mapped from changelog  
`trans_id` | `sec_result.about.resource.attribute.labels` | Mapped from changelog  
`query_class` | `sec_result.about.resource.attribute.labels` | Mapped from changelog  
`deviceMacAddress` | `principal.mac` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/darktrace-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
