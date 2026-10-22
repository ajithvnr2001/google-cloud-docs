---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tetragon-ebpf-audit-logs/
title: Collect Tetragon eBPF audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:01.745259+00:00
---

# Collect Tetragon eBPF audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tetragon-ebpf-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tetragon eBPF audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tetragon eBPF audit logs to Google Security Operations using the Bindplane agent.

Tetragon is an eBPF-based Kubernetes security observability platform for runtime enforcement, process monitoring, and network policy auditing. It generates structured JSON log events on Kubernetes nodes that capture process execution, network connections, and policy violations.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Kubernetes nodes running Tetragon
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * A Kubernetes cluster with Tetragon deployed and producing audit logs
  * Access to Tetragon log output on the node file system



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

Install the Bindplane agent on your Linux operating system according to the following instructions.

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

## Configure Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * Use the following to locate the configuration file:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          filelog:
            include:
              - /var/log/tetragon/*.json
              - /var/run/cilium/tetragon/tetragon.log
            start_at: beginning
            poll_interval: 5s
        
        exporters:
          chronicle/tetragon_ebpf:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: TETRAGON_EBPF_AUDIT_LOGS
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/tetragon_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/tetragon_ebpf
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `include`: Paths to Tetragon log files: 
      * `/var/log/tetragon/*.json` for default Tetragon JSON export logs
      * `/var/run/cilium/tetragon/tetragon.log` for the Tetragon daemon log
      * Adjust paths based on your Tetragon deployment and log export configuration
    * `start_at`: Set to `beginning` to read existing logs, or `end` to read only new entries
    * `poll_interval`: How often to check for new log data (default: `5s`)
  * **Exporter configuration:**

    * `tetragon_ebpf`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `TETRAGON_EBPF_AUDIT_LOGS`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `tetragon_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/tetragon_ebpf:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: TETRAGON_EBPF_AUDIT_LOGS
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file: * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           




## Configure Tetragon log export

Tetragon emits structured JSON events that can be exported to local files for collection by the Bindplane agent.

### Export Tetragon events to a log file

  1. If Tetragon is deployed using Helm, configure the export path in the Helm values:
         
         export:
           stdout:
             enabledCommand: true
             enabledArgs: true
           filenames:
             - /var/log/tetragon/tetragon.json
         

  2. Alternatively, redirect Tetragon events using `tetra` CLI:
         
         tetra getevents -o json > /var/log/tetragon/tetragon.json &
         

  3. Verify that JSON log events are being written to the configured path:
         
         tail -f /var/log/tetragon/tetragon.json
         

  4. Ensure the Bindplane agent has read permissions on the Tetragon log directory and files:
         
         sudo chmod -R 644 /var/log/tetragon/
         

**Note:** If Tetragon runs in a Kubernetes pod, you may need to mount the log directory as a hostPath volume or use a DaemonSet to export logs to each node's file system where the Bindplane agent can read them.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
jsonPayload.node_name, jsonPayload.process_kprobe.action, arg.sock_arg.sport, arg.sock_arg.dport, arg.sock_arg.protocol, jsonPayload.process_kprobe.function_name, labels.k8s-pod/app_kubernetes_io/instance, labels.k8s-pod/app_kubernetes_io/name, labels.k8s-pod/helm_sh/chart, labels.k8s-pod/controller-revision-hash, labels.k8s-pod/app_kubernetes_io/managed-by | additional.fields | Merged with labels created from these fields under respective conditions  
| metadata.event_type | Set to "GENERIC_EVENT", then "NETWORK_CONNECTION" if principal_present and target_present, else "STATUS_UPDATE" if principal_present  
insertId | metadata.product_log_id | Value copied directly  
| metadata.product_name | Set to "TETRAGON_EBPF_AUDIT_LOGS"  
| metadata.vendor_name | Set to "TETRAGON_EBPF_AUDIT_LOGS"  
arg.sock_arg.protocol | network.ip_protocol | Extracted protocol number using grok pattern 'IPPROTO_%{GREEDYDATA}', mapped to IP protocol enum  
arg.sock_arg.saddr | principal.ip | Value copied directly (last if multiple args)  
arg.sock_arg.sport | principal.port | Converted to integer from arg.sock_arg.sport (for index 0)  
jsonPayload.process_kprobe.process.cwd | principal.process.file.full_path | Value copied directly  
jsonPayload.process_kprobe.parent.cwd | principal.process.parent_process.file.full_path | Value copied directly  
jsonPayload.process_kprobe.parent.pid | principal.process.parent_process.pid | Converted to string  
jsonPayload.process_kprobe.process.pid | principal.process.pid | Converted to string  
logName, jsonPayload.process_kprobe.policy_name, jsonPayload.process_kprobe.process.binary, jsonPayload.process_kprobe.process.docker, jsonPayload.process_kprobe.process.exec_id, jsonPayload.process_kprobe.process.flags, jsonPayload.process_kprobe.process.parent_exec_id, jsonPayload.process_kprobe.process.auid, jsonPayload.process_kprobe.process.tid, jsonPayload.process_kprobe.process.uid | security_result.detection_fields | Merged with labels created from these fields  
severity | security_result.severity | Uppercased, set to mapped value if in predefined list or matches Info  
severity | security_result.severity_details | Set to uppercased severity if not matching predefined  
resource.labels.project_id | target.cloud.project.name | Value copied directly  
arg.sock_arg.daddr | target.ip | Value copied directly (last if multiple args)  
resource.labels.location | target.location.name | Value copied directly  
resource.labels.namespace_name | target.namespace | Value copied directly  
arg.sock_arg.dport | target.port | Converted to integer from arg.sock_arg.dport (for index 0)  
resource.labels.pod_name, resource.labels.container_name, labels.k8s-pod/app_kubernetes_io/instance, labels.k8s-pod/app_kubernetes_io/name, labels.k8s-pod/helm_sh/chart, labels.k8s-pod/controller-revision-hash, labels.k8s-pod/app_kubernetes_io/managed-by | target.resource.attribute.labels | Merged with labels created from these fields  
resource.labels.cluster_name | target.resource.name | Value copied directly  
resource.type | target.resource.resource_subtype | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tetragon-ebpf-audit-logs-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
