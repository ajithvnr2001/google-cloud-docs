---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nginx/
title: Collect NGINX logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:24.701572+00:00
---

# Collect NGINX logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nginx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect NGINX logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest NGINX logs to Google Security Operations using the Bindplane agent.

NGINX is a web server and reverse proxy that generates syslog messages for HTTP access events, error events, authentication activity, and process information. The parser extracts fields from multiple log formats (syslog, JSON, access logs) using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the NGINX server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the NGINX host



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
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/nginx:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: NGINX
            raw_log_field: body
        
        service:
          pipelines:
            logs/nginx_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/nginx
        




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
          chronicle/nginx:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: NGINX
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
             




## Configure NGINX to forward logs to Bindplane

  1. Open the NGINX configuration file (for example, `/etc/nginx/nginx.conf`):
         
         sudo vi /etc/nginx/nginx.conf
         

  2. Edit the configuration, replacing `<BINDPLANE_SERVER>` and `<BINDPLANE_PORT>` with your values:
         
         http {
             access_log syslog:server=<BINDPLANE_SERVER>:<BINDPLANE_PORT>,facility=local7,tag=nginx_access;
             error_log syslog:server=<BINDPLANE_SERVER>:<BINDPLANE_PORT>,facility=local7,tag=nginx_error;
         }
         

  3. Restart NGINX to apply the changes:
         
         sudo systemctl reload nginx
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_Internal_WorkspaceResourceId` | `target.resource.product_object_id` | Directly mapped  
`Computer` | `principal.asset.hostname` | Directly mapped  
`Facility` | `additional.fields[`facility`]` | Directly mapped  
`HostName` | `principal.asset.hostname` | Directly mapped if `src_ip` is not present  
`ProcessName` | `principal.application` | Directly mapped  
`SeverityLevel` | `security_result.severity` | Mapped to INFORMATIONAL if the value is `info`  
`SourceSystem` | `principal.asset.platform` | Mapped to LINUX if the value matches `Linux`  
`SyslogMessage` | Multiple fields | Parsed using grok to extract `time`, `method`, `target_path`, `protocol`, `response_code`, `referral_url`, `user_agent`, `target_ip`, `target_host`, and `cache`  
`TenantId` | `additional.fields[`TenantId`]` | Directly mapped  
`acct` | `principal.user.user_id` | Directly mapped if not empty or `?`  
`addr` | `principal.asset.ip` | Directly mapped  
`audit_epoch` | `metadata.event_timestamp` | Converted to timestamp using the `UNIX` format. Nanoseconds are extracted from the original log message.  
`cache` | `additional.fields[`cache`]` | Directly mapped  
`collection_time.nanos` | `metadata.event_timestamp.nanos` | Used for nanoseconds of the event timestamp if available  
`collection_time.seconds` | `metadata.event_timestamp.seconds` | Used for seconds of the event timestamp if available  
`data` | Multiple fields | The main source of data, parsed differently based on the log format (Syslog, JSON, or other)  
`exe` | `target.process.command_line` | Directly mapped after removing backslashes and quotes  
`hostname` | `principal.asset.hostname` OR `principal.asset.ip` | If it is an IP address, mapped to `principal.asset.ip`. Otherwise, mapped to `principal.asset.hostname`  
`msg` | `metadata.description` | Directly mapped as the description  
`node` | `target.asset.hostname` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`protocol` | `network.application_protocol` | Mapped to HTTP if the value matches `HTTP`  
`referral_url` | `network.http.referral_url` | Directly mapped if not empty or `-`  
`res` | `security_result.action_details` | Directly mapped  
`response_code` | `network.http.response_code` | Directly mapped and converted to integer  
`ses` | `network.session_id` | Directly mapped  
`src_ip` | `principal.asset.ip` | Directly mapped  
`target_host` | `target.asset.hostname` | Directly mapped  
`target_ip` | `target.asset.ip` | Directly mapped, after converting the string representation to a JSON array and then extracting individual IPs  
`target_path` | `target.url` | Directly mapped  
`time` | `metadata.event_timestamp` | Parsed to extract the timestamp using the format `dd/MMM/yyyy:HH:mm:ss Z`  
`user_agent` | `network.http.user_agent` | Directly mapped if not empty or `-`  
| `metadata.event_type` | Set to `GENERIC_EVENT` initially, then potentially overwritten based on other fields like `terminal` and `protocol`. Defaults to `USER_UNCATEGORIZED` if the main grok pattern does not match. Set to `NETWORK_HTTP` if `protocol` is HTTP and `target_ip` is present, and `STATUS_UPDATE` if `protocol` is HTTP but `target_ip` is not present  
| `metadata.log_type` | Set to `NGINX`  
| `metadata.product_name` | Set to `NGINX`  
| `metadata.vendor_name` | Set to `NGINX`  
| `network.ip_protocol` | Set to `TCP` if `terminal` is `sshd` or `ssh`, or if the main grok pattern does not match  
| `principal.asset_id` | Set to `GCP.GCE:0001` if `terminal` is `sshd` or `ssh`. Set to `GCP.GCE:0002` if the main grok pattern does not match  
| `extensions.auth.type` | Set to `MACHINE` if `terminal` is `sshd` or `ssh`  
`log_hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`ip_part` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`domain_part` | `event.idm.read_only_udm.intermediary.administrative_domain` | Mapped from changelog  
`location_part` | `event.idm.read_only_udm.intermediary.location.name` | Mapped from changelog  
`labels.compute_googleapis_com/resource_name` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`resource.labels.instance_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`resource.labels.project_id` | `event.idm.read_only_udm.target.resource_ancestors.name` | Mapped from changelog  
`resource.labels.zone` | `event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone` | Mapped from changelog  
`resource.type` | `event.idm.read_only_udm.target.resource.resource_type` | Mapped from changelog  
`insertId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`jsonPayload.latency` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`remoteIp` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`jsonPayload.requestMethod` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`jsonPayload.requestSize` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`jsonPayload.requestUrl` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`jsonPayload.responseSize` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`jsonPayload.serverIp` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`jsonPayload.status` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`jsonPayload.userAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`jsonPayload.userAgent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`labels` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`terminal` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.labels` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource.type` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource.name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`user_agent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nginx-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
