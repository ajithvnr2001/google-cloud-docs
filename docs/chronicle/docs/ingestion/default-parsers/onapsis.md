---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onapsis/
title: Collect Onapsis Platform logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:46.968011+00:00
---

# Collect Onapsis Platform logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onapsis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Onapsis Platform logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Onapsis Platform logs to Google Security Operations using Bindplane.

Onapsis Platform is a cybersecurity solution that specializes in protecting business-critical applications such as SAP and Oracle. It provides continuous monitoring, vulnerability management, compliance auditing, and threat detection for ERP systems, delivering deep application-specific insights to help organizations secure complex environments against cyber threats, misconfigurations, and unauthorized access.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Onapsis Platform
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Onapsis Platform console
  * Onapsis Defend product for real-time threat monitoring and syslog export capabilities



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
          chronicle/onapsis:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: ONAPSIS
            raw_log_field: body
            ingestion_labels:
              env: production
              source: onapsis_defend
        
        service:
          pipelines:
            logs/onapsis_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/onapsis
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on UDP port 51. If port 514 requires root privileges on Linux, use `0.0.0.0:1514` instead and configure Onapsis to send to port 1514.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `YOUR_CUSTOMER_ID`: Replace with your Chronicle customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Set to `ONAPSIS` (Chronicle ingestion label)
    * `ingestion_labels`: Optional labels to categorize logs (customize as needed)

**Note:** Onapsis supports both UDP and TCP syslog protocols. This configuration uses UDP for lower latency. To use TCP instead, replace `udplog` with `tcplog` in both the receivers and service sections.

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/onapsis:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ONAPSIS
            raw_log_field: body
            ingestion_labels:
              env: production
              source: onapsis_defend
        


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
         




## Configure Onapsis Platform syslog forwarding

Configure Onapsis Platform to forward security events and threat monitoring logs to the Bindplane agent via syslog.

  1. Sign in to the **Onapsis Platform** console.
  2. Go to **Settings > Integrations**.
  3. In the **Integrations** section, locate the **Syslog** integration option.
  4. Click **Add** or **Configure** to create a new syslog destination.
  5. Provide the following configuration details: 
     * **Syslog server address** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or `1514` if you configured the Bindplane agent to use a non-privileged port).
     * **Protocol** : Select **UDP** (or **TCP** if you configured the Bindplane agent to use TCP).
     * **Format** : Select **Syslog** (standard syslog format) or **LEEF** (Log Event Extended Format) if integrating with IBM QRadar-compatible systems.
  6. Click **Save** or **Apply** to activate the syslog export configuration.
  7. Verify that logs are being sent by checking the Bindplane agent logs:

**Linux:**
         
         sudo journalctl -u observiq-otel-collector -f
         

**Windows:**
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         


**Note:** Onapsis Defend product provides real-time threat monitoring and security event streaming via syslog. Ensure that Onapsis Defend is configured to generate alerts for the security events you want to monitor in Google SecOps.**Note:** The syslog integration in Onapsis Platform is typically found under Settings > Integrations. The exact navigation path may vary slightly depending on your Onapsis Platform version. If you cannot locate the syslog configuration, consult your Onapsis Platform administrator or refer to the Onapsis Platform documentation for your specific version.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
bucket | additional.fields | Added as labels with keys derived from source fields  
task_sent | additional.fields |   
sub_path | additional.fields |   
facilityName | additional.fields |   
source_version | additional.fields |   
db_table | additional.fields |   
incident_type | additional.fields |   
incident_name | additional.fields |   
program_name | additional.fields |   
task_type | additional.fields |   
policy_id | additional.fields |   
name | additional.fields |   
authentication_method | additional.fields |   
alarm_profile_matches | additional.fields |   
client | additional.fields |   
db_table_pk | additional.fields |   
system_type | additional.fields |   
log_line | additional.fields |   
action | additional.fields |   
task_id | additional.fields |   
job_name | additional.fields |   
job_id | additional.fields |   
osp_link | additional.fields |   
sid | additional.fields |   
description | metadata.description | Value from description if not empty, else set to "Uploading" if log_data matches "Uploading", "Celery task sent" if matches "Celery task sent", "Calling ModuleApi.put" if matches "Calling ModuleApi.put", else from job_type  
log_data | metadata.description |   
job_type | metadata.description |   
created_at | metadata.event_timestamp | Converted using date with format yyyy-mm-ddTHH:mm:ss  
has_principal | metadata.event_type | Set to "NETWORK_UNCATEGORIZED" if has_principal, has_target, has_network true; "STATUS_UPDATE" if has_principal true; else "GENERIC_EVENT"  
has_target | metadata.event_type |   
has_network | metadata.event_type |   
http_method | network.http.method | Value copied directly  
url | network.http.referral_url | Value copied directly  
response_code | network.http.response_code | Converted to integer  
application | principal.application | Value copied directly  
host | principal.hostname | Value from host if not IP, else from src, else from terminal_source if not IP  
src | principal.hostname |   
terminal_source | principal.hostname |   
host | principal.ip | Merged from host if IP, erp_host, terminal_source if IP  
erp_host | principal.ip |   
terminal_source | principal.ip |   
asset_name | principal.resource.name | Value copied directly  
user_type | principal.user.role_name | Value copied directly  
user_name | principal.user.user_display_name | Value from user_name, merged with username  
username | principal.user.user_display_name |   
user_id | principal.user.userid | Value copied directly  
modules | security_result.detection_fields | Merged labels from modules map, vulnerabilities map, new_state  
vulnerabilities | security_result.detection_fields |   
new_state | security_result.detection_fields |   
severityName | security_result.severity | Set to "INFORMATIONAL" if severityName in ["INFO", "info"]  
file_name | target.file.full_path | Value copied directly  
dst | target.hostname | Value copied directly  
metadata.product_name | metadata.product_name | Set to "ONAPSIS"  
metadata.vendor_name | metadata.vendor_name | Set to "ONAPSIS"  
`conditions.condition_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`conditions.eval_value.success` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`conditions.matched` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`erp_event_source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`erp_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protocol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`confidence` | `event.idm.read_only_udm.security_result.confidence_details` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`success` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`inter_ip` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onapsis-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
