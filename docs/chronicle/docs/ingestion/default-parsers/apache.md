---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/apache/
title: Collect Apache logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:39.571766+00:00
---

# Collect Apache logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/apache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Apache logs

**Parser Version:** 20.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Apache logs to Google Security Operations using Bindplane agent.

Apache HTTP Server is an open-source web server that serves HTTP requests and generates access and error logs. The parser handles both standard combined/common log formats and JSON-formatted logs, extracting HTTP request details, response codes, and client information.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Apache server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Apache server (root or sudo)



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
            chronicle/apache:
                protocol: https
                # Region of your instance, for example us, europe, asia-southeast1
                location: <LOCATION>
                # Project number of the Google Cloud project linked to the instance
                project: '<PROJECT_NUMBER>'
                compression: gzip
                creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: chronicle.googleapis.com
                log_type: APACHE
                raw_log_field: body
        
        service:
            pipelines:
                logs/apache_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/apache
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
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
            chronicle/apache:
                compression: gzip
                creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: APACHE
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
             




## Configure syslog in Apache

  1. Sign in to the server hosting Apache using SSH.
  2. Create a file under `/etc/rsyslog.d/` named `02-apache2.conf`:
         
         vim /etc/rsyslog.d/02-apache2.conf
         

  3. Add the following code to the file:
         
         module(load="imfile" PollingInterval="10" statefile.directory="/var/spool/rsyslog")
         
         input(type="imfile"
             File="/var/log/apache2/access.log"
             Tag="http_access"
             Severity="info"
             Facility="local6")
         
         Local6.info @<BINDPLANE_IP>:<BINDPLANE_PORT>
         
         module(load="imfile" PollingInterval="10" statefile.directory="/var/spool/rsyslog")
         
         input(type="imfile"
             File="/var/log/apache2/error.log"
             Tag="http_error"
             Severity="error"
             Facility="local7")
         
         Local7.error @<BINDPLANE_IP>:<BINDPLANE_PORT>
         

     * Replace `<BINDPLANE_IP>` and `<BINDPLANE_PORT>` with the IP address and port configured for the Bindplane agent.
     * If you are using TCP protocol, append an additional `@` to the host line (for example, `@@<BINDPLANE_IP>:<BINDPLANE_PORT>`).
  4. Restart rsyslog services:
         
         sudo service rsyslog restart
         




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`bytes` | `network.received_bytes` | Bytes received from the client.  
`bytes` | `network.sent_bytes` | Bytes sent to the client.  
`bytes_out` | `network.sent_bytes` | Bytes sent to the client.  
`bytes_received` | `network.received_bytes` | Bytes received from the client.  
`Content` | `network.http.method` | HTTP method extracted from the "Content" field.  
`Content` | `target.url` | Target URL extracted from the "Content" field.  
`cookie` | `additional.fields.value.string_value` | Value of the "cookie" field.  
`dest_ip` | `target.ip` | IP address of the target.  
`dest_name` | `target.hostname` | Hostname of the target.  
`dest_port` | `target.port` | Port of the target.  
`description` | `metadata.description` | Description of the event.  
`duration_microseconds` | `additional.fields.value.string_value` | Value of the "duration_microseconds" field.  
`file_full_path` | `target.file.full_path` | Full path of the target file.  
`hostname` | `target.hostname` | Hostname of the target.  
`http_content_type` | `additional.fields.value.string_value` | Value of the "http_content_type" field.  
`http_host` | `principal.hostname` | Hostname of the principal.  
`http_method` | `network.http.method` | HTTP method.  
`http_referrer` | `network.http.referral_url` | HTTP referrer URL.  
`http_user_agent` | `network.http.user_agent` | HTTP user agent.  
`ID` | `metadata.id` | ID of the event.  
`insertId` | `metadata.product_log_id` | Product log ID.  
`ip` | `principal.ip` | IP address of the principal.  
`jsonPayload.cIP` | `target.ip` | IP address of the target.  
`jsonPayload.cPort` | `target.port` | Port of the target.  
`jsonPayload.csBytes` | `network.sent_bytes` | Bytes sent to the client.  
`jsonPayload.csMethod` | `network.http.method` | HTTP method.  
`jsonPayload.csMimeType` | `target.file.mime_type` | MIME type of the target file.  
`jsonPayload.csReferer` | `network.http.referral_url` | HTTP referrer URL.  
`jsonPayload.csURL` | `target.url` | Target URL.  
`jsonPayload.csUserAgent` | `network.http.user_agent` | HTTP user agent.  
`jsonPayload.sHierarchy` | `additional.fields.value.string_value` | Value of the "sHierarchy" field.  
`jsonPayload.sHostname` | `principal.hostname` | Hostname of the principal.  
`jsonPayload.sIP` | `principal.ip` | IP address of the principal.  
`jsonPayload.scBytes` | `network.received_bytes` | Bytes received from the client.  
`jsonPayload.scHTTPStatus` | `network.http.response_code` | HTTP response code.  
`jsonPayload.scResultCode` | `additional.fields.value.string_value` | Value of the "scResultCode" field.  
`LastStatus` | `network.http.response_code` | HTTP response code.  
`log_level` | `security_result.severity` | Severity of the security result.  
`logName` | `security_result.category_details` | Category details of the security result.  
`method` | `network.http.method` | HTTP method.  
`pid` | `principal.process.pid` | Process ID of the principal.  
`Port` | `target.port` | Port of the target.  
`proto` | `network.application_protocol` | Application protocol.  
`referer` | `network.http.referral_url` | HTTP referrer URL.  
`RemoteHost` | `principal.ip` | IP address of the principal.  
`RemoteUser` | `principal.user.userid` | User ID of the principal.  
`resource.labels.instance_id` | `target.resource.product_object_id` | Product object ID of the target resource.  
`resource.labels.project_id` | `target.resource.attribute.labels.value` | Value of the "project_id" label.  
`resource.labels.zone` | `target.resource.attribute.cloud.availability_zone` | Availability zone of the target resource.  
`resource.type` | `target.resource.resource_type` | Resource type of the target.  
`response` | `network.http.response_code` | HTTP response code.  
`SizeBytes` | `network.received_bytes` | Bytes received from the client.  
`src_ip` | `principal.ip` | IP address of the principal.  
`src_port` | `principal.port` | Port of the principal.  
`ssl_cipher` | `network.tls.cipher` | TLS cipher.  
`ssl_version` | `network.tls.version_protocol` | TLS version protocol.  
`status` | `network.http.response_code` | HTTP response code.  
`target` | `target.url` | Target URL.  
`target_ip` | `target.ip` | IP address of the target.  
`target_port` | `target.port` | Port of the target.  
`time` | `metadata.event_timestamp` | Event timestamp.  
`uri_path` | `target.process.file.full_path` | Full path of the target file.  
`user` | `principal.user.userid` | User ID of the principal.  
`useragent` | `network.http.user_agent` | HTTP user agent.  
`version_protocol` | `network.tls.version_protocol` | TLS version protocol.  
`Workername` | `principal.hostname` | Hostname of the principal.  
`x_forwarded_for` |  | Value of the "X-Forwarded-For" header.  
| `metadata.log_type` | The value is set to "APACHE" in the parser code.  
| `metadata.product_name` | The value is set to "Apache Web Server" in the parser code.  
| `metadata.vendor_name` | The value is set to "Apache" in the parser code.  
| `metadata.event_type` | The value is determined based on the presence of principal and target information. If both principal and target are present, the event type is set to "NETWORK_HTTP". If only principal is present, the event type is set to "STATUS_UPDATE". Otherwise, it is set to "GENERIC_EVENT".  
| `additional.fields.key` | The key is set to "keep_alive", "duration_microseconds", "cookie", "http_content_type", "sHierarchy", "scResultCode" in the parser code based on the field.  
| `target.port` | If the "proto" field is "HTTP", the port is set to 80. If the "proto" field is "HTTPS", the port is set to 443. If the "proto" field is "FTP", the port is set to 21.  
| `target.resource.attribute.labels.key` | The key is set to "project_id" in the parser code.  
`client_ip_address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`server` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`bytes_in` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`PHPSESSID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AuthToken` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`response_time_microseconds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`Filename` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`kv_key` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`info` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SourceModuleName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SourceModuleType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`tls_version` | `event.idm.read_only_udm.network.tls.version` | Mapped from changelog  
`version_protocol` | `event.idm.read_only_udm.network.tls.version_protocol` | Mapped from changelog  
`syncAccuracy` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`isSynced` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`tzKnown` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_location` | `principal.location.country_or_region` | Mapped from changelog  
`proto", "proto_version", "uri_path", and "uri_query` | `additional.fields` | Mapped from changelog  
`ip_msg` | `principal.ip` | Mapped from changelog  
`msg_method` | `network.http.method` | Mapped from changelog  
`useragentvalue` | `network.http.user_agent` | Mapped from changelog  
`bytes_out` | `network.sent.bytes` | Mapped from changelog  
`XForwardedForIP" and "RemoteHost` | `principal.ip` | Mapped from changelog  
`Remoteuser` | `principal.user.userid` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/apache-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
