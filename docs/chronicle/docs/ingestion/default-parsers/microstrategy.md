---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microstrategy/
title: Collect MicroStrategy logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:46.524809+00:00
---

# Collect MicroStrategy logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microstrategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect MicroStrategy logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest MicroStrategy logs to Google Security Operations using Bindplane.

MicroStrategy is a business intelligence and analytics platform. It generates audit logs for report execution, user sessions, data access, and admin operations. The parser extracts fields from MicroStrategy log messages and maps them to the Unified Data Model (UDM), capturing user identity, session details, server information, and security metadata.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the MicroStrategy Intelligence Server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the MicroStrategy Intelligence Server (administrator role or server filesystem access)



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/microstrategy:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: MICROSTRATEGY
            raw_log_field: body
        
        service:
          pipelines:
            logs/microstrategy:
              receivers:
                - tcplog
              exporters:
                - chronicle/microstrategy
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * Adjust the `creds_file_path` to the path of your service account JSON key file (Option 1), depending on the platform: 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/microstrategy:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: MICROSTRATEGY
            raw_log_field: body
        


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
         




## Configure MicroStrategy syslog forwarding

MicroStrategy Intelligence Server writes log files locally to the filesystem. Configure syslog forwarding using the system syslog daemon to send these logs to the Bindplane agent.

  1. Locate the MicroStrategy log directory:

     * **Windows** : `C:\Program Files\Common Files\MicroStrategy\Log\`
     * **Linux** : `/var/log/Strategy/`
**Note:** The primary log file is `DSSErrors.log`. Check your MicroStrategy configuration for the actual log directory location.
  2. Configure the system syslog daemon to monitor and forward MicroStrategy log files to the Bindplane agent.




**On Linux (rsyslog):**

  1. Create a new rsyslog configuration file:
         
         sudo nano /etc/rsyslog.d/microstrategy-forward.conf
         

  2. Add the following content to forward MicroStrategy logs:
         
         module(load="imfile")
         input(type="imfile"
             File="/var/log/Strategy/DSSErrors.log"
             Tag="microstrategy"
             Severity="info"
             Facility="local0")
         local0.* @BINDPLANE_AGENT_IP:514
         

**Note:** Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host. Use `@@` instead of `@` for TCP.
  3. Restart the rsyslog service:
         
         sudo systemctl restart rsyslog
         




**On Windows:**

Use a log forwarder utility (such as NXLog or Snare) to monitor the MicroStrategy log directory and forward events via syslog to the Bindplane agent IP and port.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
Account_Creation_Timestamp, Account_Modification_Timestamp, Timestamp | additional.fields | Merged with labels created from fields if not empty  
Authentication_message | metadata.description | Value copied directly  
Event_start | metadata.event_timestamp | Converted using date filter with format "MMM dd HH:mm:ss"  
| metadata.event_type | Set to "USER_UNCATEGORIZED" if has_principal and has_target, else "STATUS_UPDATE" if has_principal, else "GENERIC_EVENT"  
Session | network.session_id | Value copied directly  
Source_server | principal.application | Value copied directly  
Hostname | principal.asset.hostname | Value copied directly  
server_ip | principal.asset.ip | Value copied directly  
Hostname | principal.hostname | Value copied directly  
server_ip | principal.ip | Value copied directly  
level | principal.platform_patch_level | Value copied directly  
User_Group_Name | principal.user.group_identifiers | Value copied directly  
Account_Name, User | principal.user.user_display_name | Value from Account_Name if not empty, else User  
id, Account_Login, Account | principal.user.userid | Value from id if not empty, else Account_Login if not empty, else Account  
Log_level | security_result.detection_fields | Merged with label created from field if not empty  
Source_host | src.asset.hostname | Value copied directly  
Source_host | src.hostname | Value copied directly  
module | target.application | Value copied directly  
client_ip | target.asset.ip | Value copied directly  
client_ip | target.ip | Value copied directly  
PID | target.process.pid | Value copied directly  
Thread_ID, SID, method, Account_Status_DESC | target.resource.attribute.labels | Merged with labels created from fields if not empty  
OID | target.resource.id | Value copied directly  
Object_Owner_Name | target.resource.name | Value copied directly  
user | target.user.user_display_name | Value copied directly  
UID | target.user.userid | Value copied directly  
| metadata.product_name | Set to "MICROSTRATEGY"  
| metadata.vendor_name | Set to "MICROSTRATEGY"  
`Hostname` | `principal.hostname, principal.asset.hostname` | Mapped from changelog  
`Source_host` | `src.hostname, src.asset.hostname` | Mapped from changelog  
`server_ip` | `principal.ip, principal.asset.ip` | Mapped from changelog  
`client_ip` | `target.ip, target.asset.ip` | Mapped from changelog  
`Account_Creation_Timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Account_Modification_Timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microstrategy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
