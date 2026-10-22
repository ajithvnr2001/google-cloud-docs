---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-secure-workload/
title: Collect Cisco Secure Workload (formerly Tetration Analytics) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:39.275152+00:00
---

# Collect Cisco Secure Workload (formerly Tetration Analytics) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-secure-workload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Secure Workload (formerly Tetration Analytics) logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Secure Workload (formerly Tetration Analytics) logs to Google Security Operations using the Bindplane agent.

Cisco Secure Workload is an on-premises workload protection platform that provides micro-segmentation, application dependency mapping, and compliance monitoring for data center and cloud workloads. It generates logs about policy violations, flow events, and security incidents. The platform supports built-in syslog export for forwarding alert and flow data to external collectors.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco Secure Workload cluster
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco Secure Workload cluster with administrator or site admin role



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

## Get a Google SecOps customer ID

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
          chronicle/cisco_secure_workload:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CISCO_SECURE_WORKLOAD
            raw_log_field: body
        
        service:
          pipelines:
            logs/cisco_secure_workload_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cisco_secure_workload
        




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
          chronicle/cisco_secure_workload:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_SECURE_WORKLOAD
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
             




## Configure Cisco Secure Workload syslog forwarding

  1. Sign in to the **Cisco Secure Workload** web console.
  2. Go to **Manage > External Integrations > Syslog**.

**Note:** In earlier versions of Cisco Secure Workload (Tetration), navigate to **Manage > Workloads > Connectors** and add a new **Syslog** connector.
  3. Click **Create New Syslog Export** (or **Add Connector**).

  4. Provide the following configuration details:

     * **Name** : Enter a name (for example, `chronicle-syslog-export`).
     * **Host** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514` (or the port configured in the Bindplane agent receiver).
     * **Protocol** : Select **UDP**.
     * **Facility** : Select **local7** (or your preferred facility).
     * **Severity** : Select **Informational** or lower to capture all events.
  5. Click **Save**.

  6. Verify that logs are being sent by checking the Bindplane agent logs for incoming syslog messages.

**Note:** Cisco Secure Workload sends alerts, policy violation events, flow data, and enforcement events via syslog. Ensure the Bindplane agent host is reachable from the Cisco Secure Workload cluster on the configured port.



## UDM field mapping reference

Log Field | UDM Mapping | Logic  
---|---|---  
connection, event_name | additional.fields | Merged as labels if not empty  
alert_time | metadata.collected_timestamp | Converted from epoch ms to timestamp  
| metadata.event_type | Set to "NETWORK_FLOW" if has_principal is true, else "GENERIC_EVENT"  
root_scope_id | metadata.product_deployment_id | Value copied directly  
type | metadata.product_event_type | Value copied directly  
key_id | metadata.product_log_id | Value copied directly  
| metadata.product_name | Set to "SECURE WORKLOAD"  
| metadata.product_version | Set to "1"  
| metadata.vendor_name | Set to "CISCO"  
alert_details_json.protocol | network.ip_protocol | Value copied directly if type COMPLIANCE  
details.HostName | principal.asset.hostname | Value copied directly if type ENFORCEMENT  
alert_details_json.constituent_flows.0.consumer_address, details.IP | principal.asset.ip | Value from consumer_address if type COMPLIANCE, else from details.IP, then remove trailing space and beyond  
details.CurrentVersion | principal.asset.platform_software.platform_version | Value copied directly if type ENFORCEMENT  
details.Bios | principal.asset.software | Value copied directly if type ENFORCEMENT  
alert_details_json.time_range.0 | principal.domain.first_seen_time | Converted from epoch ms to timestamp if type COMPLIANCE  
alert_details_json.time_range.1 | principal.domain.last_seen_time | Converted from epoch ms to timestamp if type COMPLIANCE  
details.HostName | principal.hostname | Set to "UNKNOWN" if type COMPLIANCE, else value from details.HostName if type ENFORCEMENT  
alert_details_json.constituent_flows.0.consumer_address, details.IP | principal.ip | Value from consumer_address if type COMPLIANCE, else from details.IP, then remove trailing space and beyond  
details.Platform | principal.platform_version | Value copied directly if type ENFORCEMENT  
alert_details_json.provider_port | principal.port | Converted to integer if type COMPLIANCE  
pid | principal.process.pid | Value copied directly  
alert_details_json.provider_scope_ids, alert_details_json.provider_scope_names, alert_details_json.internal_trigger.label | principal.resource.attribute.labels | Merged as labels if type COMPLIANCE  
alert_details_json.application_id | principal.resource.product_object_id | Value copied directly if type COMPLIANCE  
details.AgentType | principal.user.attribute.roles | Value copied directly if type ENFORCEMENT  
alert_details_json.policy_category | security_result.category_details | Merged from array if type COMPLIANCE  
alert_text | security_result.description | Value copied directly  
alert_conf_id | security_result.rule_id | Value copied directly if type COMPLIANCE  
alert_details_json.internal_trigger.rules.field | security_result.rule_name | Value copied directly if type COMPLIANCE  
alert_details_json.internal_trigger.rules.type | security_result.rule_type | Value copied directly if type COMPLIANCE  
severity | security_result.severity | Value copied directly  
alert_details_json.policy_type | security_result.summary | Value copied directly if type COMPLIANCE  
alert_details_json.constituent_flows.0.provider_address | target.asset.ip | Value copied directly if type COMPLIANCE  
tenant_id | target.group.product_object_id | Value copied directly if not empty or "0"  
| target.hostname | Set to "UNKNOWN"  
alert_details_json.constituent_flows.0.provider_address | target.ip | Value copied directly if type COMPLIANCE  
alert_details_json.constituent_flows.0.consumer_port | target.port | Converted to integer if type COMPLIANCE  
alert_details_json.consumer_scope_ids, alert_details_json.consumer_scope_names | target.resource.attribute.labels | Merged as labels if type COMPLIANCE  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-secure-workload-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
