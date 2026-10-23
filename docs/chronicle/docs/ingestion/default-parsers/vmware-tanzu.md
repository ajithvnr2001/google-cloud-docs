---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-tanzu/
title: Collect VMware Tanzu logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:59.699295+00:00
---

# Collect VMware Tanzu logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-tanzu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect VMware Tanzu logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest VMware Tanzu logs to Google Security Operations using the Bindplane agent.

VMware Tanzu is a Kubernetes platform that generates JSON and syslog-formatted audit logs for Kubernetes API server events, resource access, authentication decisions, and configuration changes. The parser extracts fields from JSON-formatted audit logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Tanzu Operations Manager
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to VMware Tanzu



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
          chronicle/vmware_tanzu:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VMWARE_TANZU
            raw_log_field: body
        
        service:
          pipelines:
            logs/vmware_tanzu_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/vmware_tanzu
        




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
          chronicle/vmware_tanzu:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VMWARE_TANZU
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
             




## Configure syslog for VMware Tanzu

  1. Sign in to the **Tanzu Operations Manager** web UI.
  2. Select your **User name** and then click **Settings**.
  3. Select **Syslog**.
  4. Click **Yes** to send system logs to a remote server.
  5. Provide the following configuration details: 
     * **Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number.
     * **Transport Protocol** : Select **UDP** or **TCP** , depending on your Bindplane agent configuration.
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`annotations.authorization.k8s.io/decision` | `security_result.action` | If the annotation `authorization.k8s.io/decision` exists, its value is converted to uppercase. If the uppercase value is "ALLOW", the UDM field is set to ALLOW. Otherwise, it's set to BLOCK.  
`annotations.authorization.k8s.io/reason` | `security_result.description` | If the annotation `authorization.k8s.io/reason` exists, its value (with double quotes removed) is used.  
`apiVersion` | `metadata.product_version` | Directly mapped.  
`auditID` | `metadata.product_log_id` | Directly mapped.  
`kind` | `metadata.product_event_type` | Directly mapped.  
`objectRef.name` | `target.resource.name` | Directly mapped.  
`objectRef.namespace` | `target.resource.attribute.labels.key`, `target.resource.attribute.labels.value` | The `key` is set to "namespace", and the `value` is taken from `objectRef.namespace`.  
`objectRef.resource` | `target.resource.resource_subtype` | Directly mapped.  
`objectRef.resourceVersion` | `target.resource.attribute.labels.key`, `target.resource.attribute.labels.value` | The `key` is set to "resourceVersion", and the `value` is taken from `objectRef.resourceVersion`.  
`objectRef.uid` | `target.resource.product_object_id` | Directly mapped.  
`requestReceivedTimestamp` / `timestamp` | `metadata.event_timestamp` | The parser tries to parse `requestReceivedTimestamp` first. If it's not present, it uses the `timestamp` field extracted from the syslog prefix.  
`requestURI` | `target.url` | Directly mapped.  
`responseStatus.code` | `network.http.response_code` | Directly mapped after being converted to an integer.  
`sourceIPs` | `principal.ip` | All IP addresses in the `sourceIPs` array are added to the `principal.ip` array.  
`stage` | `metadata.description` | Directly mapped.  
`stageTimestamp` | `metadata.collected_timestamp` | Directly mapped.  
`user.groups` | `principal.user.group_identifiers` | All groups in the `user.groups` array are added to the `principal.user.group_identifiers` array.  
`user.uid` | `principal.user.userid` | Directly mapped.  
`user.username` | `principal.user.user_display_name` | Directly mapped.  
`verb` | `network.http.method` | Directly mapped after being converted to uppercase. Determined by the `verb` field. If `verb` is "CREATE", the event type is `USER_RESOURCE_CREATION`. If `verb` is "PATCH" or "UPDATE", the event type is `USER_RESOURCE_UPDATE_CONTENT`. If `verb` is "DELETE", the event type is `USER_RESOURCE_DELETION`. Otherwise, if `verb` is not empty, the event type is `USER_RESOURCE_ACCESS`. If none of these conditions are met, the event type is set to `GENERIC_EVENT`. Hardcoded to "VMWARE_TANZU". Hardcoded to "VMWARE". Hardcoded to "VMWARE_TANZU". Hardcoded to "CLUSTER".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-tanzu-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
