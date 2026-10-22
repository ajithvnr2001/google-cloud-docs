---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ansible-awx/
title: Collect Ansible AWX logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:08.893056+00:00
---

# Collect Ansible AWX logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ansible-awx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Ansible AWX logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Ansible AWX logs to Google Security Operations using Bindplane. Ansible AWX is an open-source web application that provides a user interface, REST API, and task engine for Ansible. It allows teams to centrally manage automation playbooks, inventories, credentials, and scheduled jobs across the organization. The parser extracts fields from JSON-formatted Ansible AWX logs and maps these values to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Ansible AWX management console with administrator permissions.



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

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/ansible_awx:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: 'ANSIBLE_AWX'
             raw_log_field: body
         
         service:
           pipelines:
             logs/ansible_awx:
               receivers:
                 - udplog
               exporters:
                 - chronicle/ansible_awx
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/ansible_awx:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'ANSIBLE_AWX'
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Configure external logging on Ansible AWX

  1. Sign in to the **Ansible AWX** web interface.
  2. Go to **Settings** from the left navigation bar.
  3. Select **Logging settings** under the **System** section.
  4. Click **Edit** at the bottom of the Logging settings page.
  5. Provide the following configuration details: 
     * **Logging Aggregator** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Logging Aggregator Port** : Enter the Bindplane agent port number (for example, `514`).
     * **Logging Aggregator Type** : Select **Other** from the dropdown.
     * **Logging Aggregator Username** : Leave blank (not required for syslog).
     * **Logging Aggregator Password/Token** : Leave blank (not required for syslog).
     * **Logging Aggregator Protocol** : Select **UDP**.
     * **Logging Aggregator Level Threshold** : Select **INFO** or your preferred log level.
     * **Enable External Logging** : Toggle to **ON**.
     * **Loggers to Send Data to the Log Aggregator Form** : Select the relevant log types: 
       * `awx` \- generic server logs
       * `activity_stream` \- record of changes to AWX objects
       * `job_events` \- Ansible callback module data
       * `system_tracking` \- system facts and configuration data
     * **Log System Tracking Facts Individually** : Toggle to **OFF** (default).
  6. Click **Save** to apply the settings.
  7. Click **Test** to verify the connection to the Bindplane agent.

**Note:** The **Test** button may show an error when using UDP protocol. This is expected behavior and UDP logging will still work correctly.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`logger_name` | `intermediary.application` | Directly mapped  
`RenderedMessage` | `metadata.description` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`event1` | `metadata.description` | Directly mapped  
`message` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSZ`  
`principal_present` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`target_present` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`  
`user_present` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`event1_data.uuid` | `metadata.product_log_id` | Directly mapped  
`Properties.Method` | `network.http.method` | Directly mapped  
`agent.type` | `observer.application` | Directly mapped  
`agent.id` | `observer.asset_id` | Directly mapped  
`agent.type` | `observer.asset_id` | Directly mapped  
`agent.hostname` | `observer.hostname` | Directly mapped  
`ephemeral_id_label` | `observer.labels` | Merged  
`agent.version` | `observer.platform_version` | Directly mapped  
`agent.name` | `observer.user.userid` | Directly mapped  
`Properties.applicationName` | `principal.application` | Directly mapped  
`Properties.MachineName` | `principal.asset.asset_id` | Directly mapped  
`Properties.Host` | `principal.asset.hostname` | Directly mapped  
`event1_data.remote_addr` | `principal.asset.hostname` | Directly mapped  
`principal_device` | `principal.asset.hostname` | Directly mapped  
`principal_hostname` | `principal.asset.hostname` | Directly mapped  
`Properties.ClientIP` | `principal.asset.ip` | Merged  
`ip_address` | `principal.asset.ip` | Merged  
`principal_ip` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`Properties.Host` | `principal.hostname` | Directly mapped  
`event1_data.remote_addr` | `principal.hostname` | Directly mapped  
`principal_device` | `principal.hostname` | Directly mapped  
`principal_hostname` | `principal.hostname` | Directly mapped  
`Properties.ClientIP` | `principal.ip` | Merged  
`ip_address` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`src_port` | `principal.port` | Directly mapped  
`event1_data.task_path` | `principal.process.file.full_path` | Directly mapped  
`process_pid` | `principal.process.pid` | Directly mapped  
`availability_zone` | `principal.resource.attribute.labels` | Merged  
`connectionid_label` | `principal.resource.attribute.labels` | Merged  
`endpointname_label` | `principal.resource.attribute.labels` | Merged  
`machine_type` | `principal.resource.attribute.labels` | Merged  
`provider` | `principal.resource.attribute.labels` | Merged  
`cloud.instance.name` | `principal.resource.name` | Directly mapped  
`cloud.instance.id` | `principal.resource.product_object_id` | Directly mapped  
`Properties.UserName` | `principal.user.userid` | Directly mapped  
`user_name` | `principal.user.userid` | Directly mapped  
`event1_display` | `security_result.description` | Directly mapped  
`ca_id_label` | `security_result.detection_fields` | Merged  
`cf_component_label` | `security_result.detection_fields` | Merged  
`container_hash_label` | `security_result.detection_fields` | Merged  
`container_image_label` | `security_result.detection_fields` | Merged  
`container_name_label` | `security_result.detection_fields` | Merged  
`messagetemplate_label` | `security_result.detection_fields` | Merged  
`parent_uuid_label` | `security_result.detection_fields` | Merged  
`requestid_label` | `security_result.detection_fields` | Merged  
`requestpath_label` | `security_result.detection_fields` | Merged  
`serviceNowId_label` | `security_result.detection_fields` | Merged  
`sourcecontext_label` | `security_result.detection_fields` | Merged  
`stream_label` | `security_result.detection_fields` | Merged  
`task_label` | `security_result.detection_fields` | Merged  
`task_uuid_label` | `security_result.detection_fields` | Merged  
`threadid_label` | `security_result.detection_fields` | Merged  
`wf_env_label` | `security_result.detection_fields` | Merged  
`wf_id_label` | `security_result.detection_fields` | Merged  
`level` | `security_result.severity` | Mapped: `"DEBUG", "INFO", "AUDIT"` → `INFORMATIONAL`, `WARNING` → `MEDIUM`  
`level` | `security_result.severity_details` | Directly mapped  
`log` | `security_result.summary` | Directly mapped  
`host.fqdn` | `target.administrative_domain` | Directly mapped  
`host.id` | `target.asset.asset_id` | Directly mapped  
`codename_label` | `target.asset.attribute.labels` | Merged  
`json_data` | `target.asset.attribute.labels` | Mapped: `host.*os.*platform` → `codename_label`, `host.*os.*platform` → `os_name_label`  
`os_name_label` | `target.asset.attribute.labels` | Merged  
`hardware` | `target.asset.hardware` | Merged  
`json_data` | `target.asset.hardware` | Mapped: `host.*os.*platform` → `hardware`  
`host.hostname` | `target.asset.hostname` | Directly mapped  
`kubernetes.host` | `target.asset.hostname` | Directly mapped  
`target_device` | `target.asset.hostname` | Directly mapped  
`ips` | `target.asset.ip` | Merged  
`json_data` | `target.asset.ip` | Mapped: `host.*os.*platform` → `ips`  
`target_ip` | `target.asset.ip` | Merged  
`kubernetes.docker_id` | `target.asset_id` | Directly mapped  
`host.hostname` | `target.hostname` | Directly mapped  
`kubernetes.host` | `target.hostname` | Directly mapped  
`target_device` | `target.hostname` | Directly mapped  
`target_ip` | `target.ip` | Merged  
`json_data` | `target.mac` | Mapped: `host.*os.*platform` → `macs`  
`macs` | `target.mac` | Merged  
`kubernetes.namespace_name` | `target.namespace` | Directly mapped  
`json_data` | `target.platform` | Mapped: `host.*os.*platform` → `LINUX`  
`host.os.kernel` | `target.platform_patch_level` | Directly mapped  
`host.os.version` | `target.platform_version` | Directly mapped  
`io_instance_label` | `target.resource.attribute.labels` | Merged  
`io_name_label` | `target.resource.attribute.labels` | Merged  
`pod_id_label` | `target.resource.attribute.labels` | Merged  
`pod_template_hash_label` | `target.resource.attribute.labels` | Merged  
`cluster_name` | `target.resource.name` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `ANSIBLE_AWX`  
N/A | `metadata.vendor_name` | Constant: `ANSIBLE_AWX`  
N/A | `network.ip_protocol` | Constant: `TCP`  
N/A | `principal.resource.resource_type` | Constant: `VIRTUAL_MACHINE`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.platform` | Constant: `LINUX`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ansible-awx-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
