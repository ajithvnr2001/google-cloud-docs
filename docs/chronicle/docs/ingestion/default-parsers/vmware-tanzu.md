---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-tanzu/
title: Collect VMware Tanzu logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:16.938891+00:00
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



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
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

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
