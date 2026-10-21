---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sam/
title: Collect IBM Security Access Manager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:39.962362+00:00
---

# Collect IBM Security Access Manager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM Security Access Manager logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest IBM Security Access Manager logs into Google Security Operations using Bindplane.

IBM Verify Identity Access (formerly IBM Security Access Manager / IBM Security Verify Access) is a network appliance-based security solution that provides access management, web security, and authentication services. It enforces security policies for web-based resources using a reverse proxy architecture (WebSEAL), and generates audit, authentication, authorization, and system logs critical for security monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the IBM Verify Identity Access appliance
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to the IBM Verify Identity Access Local Management Interface (LMI)



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
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: 'IBM_SAM'
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

    * `listen_address`: The IP address and port the Bindplane agent listens on for incoming syslog messages. Use `0.0.0.0:514` to listen on all interfaces on port `514`. Change the port if `514` is already in use or if you prefer a non-privileged port such as `1514`.
    * To use TCP instead of UDP, replace `udplog` with `tcplog` in both the `receivers` section and the `pipelines` section.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: The Google SecOps customer ID copied earlier.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Must be set to `IBM_SAM`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'IBM_SAM'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux, do the following:

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows, do the following:

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
         




## Configure syslog forwarding in IBM Verify Identity Access

### Add a remote syslog server definition

  1. Sign in to the IBM Verify Identity Access **Local Management Interface (LMI)**.
  2. Go to **Monitor > Logs > Remote Syslog Forwarding**.
  3. On the **Remote Syslog Forwarding** page, click **Add**.
  4. Provide the following configuration details: 
     * **Server** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter the port number that the Bindplane agent is listening on (for example, `514`).
     * **Protocol** : Select **UDP** to match the `udplog` receiver in the Bindplane agent configuration. Select **TCP** if you configured the Bindplane agent with `tcplog`.
     * **Format** : Select the syslog message format: 
       * **BSD Syslog Protocol** — RFC 3164 format (recommended for broadest compatibility).
       * **Syslog Protocol** — RFC 5424 format.
     * **Debug** : Leave unchecked unless troubleshooting is required. When enabled, additional debug information is written to the `rsyslog_forwarder` log file accessible from the **Viewing application log files** page.
  5. Click **Save**.



### Configure log sources for the remote syslog server

  1. On the **Remote Syslog Forwarding** page, select the remote syslog server entry you created.
  2. Click **Sources**.
  3. Click **Add** to add a log source.
  4. Provide the following configuration details: 
     * **Name** : Select a log source from the drop-down list. The available log sources are: 
       * **LMI Messages** — LMI application messages
       * **LMI Trace** — LMI trace and debug logs
       * **LMI Access** — LMI HTTP access logs
       * **Runtime Messages** — Runtime environment messages
       * **Runtime Trace** — Runtime trace and debug logs
       * **Runtime Audit** — Runtime audit events (authentication, authorization)
       * **Runtime Logs** — Runtime application logs
       * **WebSEAL** — Web reverse proxy logs (requires selecting an **Instance Name** and **Log File**)
       * **Authorization Server** — Authorization server logs (requires selecting an **Instance Name** and **Log File**)
       * **Policy Server** — Policy server logs (requires selecting a **Log File**)
       * **Embedded User Registry** — Embedded LDAP user registry logs
       * **Cluster** — Cluster management logs
       * **System** — Operating system-level logs
       * **DSC** — Distributed session cache logs
       * **FELB** — Front-end load balancer logs
     * **Instance Name** : This field is available only when **WebSEAL** or **Authorization Server** is selected in the **Name** field. Select the instance name from the drop-down list (for example, `default`).
     * **Log File** : This field is available when **WebSEAL** , **Authorization Server** , **Policy Server** , or **Runtime Logs** is selected in the **Name** field. Select the specific log file from the drop-down list.
     * **Tag** : Enter a unique tag name for this log source. The tag must not contain spaces (for example, `WebSEAL_Audit` or `RuntimeAudit`).
     * **Facility** : Select a syslog facility category for the forwarded log entries (for example, `local0`, `local1`, `auth`, or `user`).
     * **Severity** : Select **Informational** to capture all log entries.
  5. Click **OK**.
  6. To add additional log sources, repeat steps 3 through 5 for each source you want to forward.

**Note:** For comprehensive security monitoring, configure at minimum the following sources: **Runtime Audit** , **WebSEAL** , **Authorization Server** , and **Runtime Messages**.
  7. Click **Save** to apply the log source configuration.

**Note:** The configuration is not saved on the server until you click **Save**. All log sources must be configured and saved together.
  8. To activate the changes, navigate to the top of the page and click **Deploy Pending Changes**. The syslog forwarding configuration is not active until deployed.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
sha256_value | additional.fields | Merged with map {key: "sha256_value", value: {string_value: sha256_value}} and map {key: "connection_type", value: {string_value: connection_type}}  
connection_type | additional.fields |   
dvc_ip | intermediary.hostname | Value copied directly if dvc_ip is not a valid IP  
dvc_ip | intermediary.ip | Set to dvc_ip if it's a valid IP; merge additional IPs from ip_address that are valid, not equal to src_ip or dst_ip, not empty, not "-"  
ip_address | intermediary.ip |   
ts | metadata.collected_timestamp | Parsed from ts2 if present using yyyy-MM-ddTHH:mm:ss, else from ts using ISO8601, MMM dd HH:mm:ss, MMM d HH:mm:ss  
ts2 | metadata.collected_timestamp |   
description | metadata.description | Value copied directly  
timestamp | metadata.event_timestamp | Parsed using date formats dd/MMM/yyyy:HH:mm:ss Z or yyyy-MM-dd-HH:mm:ss.SSSZZI  
src_ip | metadata.event_type | Set to "NETWORK_HTTP" if principal (src_ip or src_host) and target (dst_ip or target_hostname) and http (method or response_code) present, "NETWORK_CONNECTION" if principal and target, "STATUS_UPDATE" if principal, else "GENERIC_EVENT"  
src_host | metadata.event_type |   
dst_ip | metadata.event_type |   
target_hostname | metadata.event_type |   
method | metadata.event_type |   
response_code | metadata.event_type |   
product_event_type | metadata.product_event_type | Value copied directly  
metadata.product_name | metadata.product_name | Set to "IBM_SAM"  
metadata.vendor_name | metadata.vendor_name | Set to "IBM"  
proto | network.application_protocol | Value copied directly if in HTTP, HTTPS  
version | network.application_protocol_version | Value copied directly  
method | network.http.method | Value from method_value if not empty, else method  
method_value | network.http.method |   
response_code | network.http.response_code | Converted to integer  
ip_protocol_value | network.ip_protocol | Value copied directly if in TCP, UDP, ICMP  
rcv_bytes | network.received_bytes | Converted to uinteger  
sent_bytes | network.sent_bytes | Converted to uinteger  
request_id | network.session_id | Value copied directly  
src_application | principal.application | Value copied directly  
src_host | principal.asset.hostname | Value copied directly  
src_ip | principal.asset.ip | Value copied directly if not empty, space, null, N/A, -  
file_name | principal.file.full_path | Value copied directly  
src_host | principal.hostname | Value copied directly  
src_ip | principal.ip | Value copied directly if not empty, space, null, N/A, -  
src_port | principal.port | Converted to integer  
pid | principal.process.pid | Value copied directly  
src_resource | principal.resource.name | Value copied directly  
user_name | principal.user.userid | Value copied directly if not unauthenticated or empty  
description | security_result.action | Set to "BLOCK" if description contains "could not establish a secure connection" or "could not be determined" or "have expired"  
severity | security_result.severity | Value copied directly, with WARNING mapped to MEDIUM  
user_name | security_result.summary | Set to "unauthenticated" if user_name == "unauthenticated"  
target_hostname | target.asset.hostname | Value copied directly  
dst_ip | target.asset.ip | Value copied directly if not empty, space, null, N/A, -  
target_hostname | target.hostname | Value copied directly  
dst_ip | target.ip | Value copied directly if not empty, space, null, N/A, -  
url | target.url | Concatenated from url and url1  
url1 | target.url |   
`ip_protocol_value` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`method_value` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`sha256_value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-sam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
