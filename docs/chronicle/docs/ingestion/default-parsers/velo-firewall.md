---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/velo-firewall/
title: Collect Arista VeloCloud SD-WAN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:51.043540+00:00
---

# Collect Arista VeloCloud SD-WAN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/velo-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Arista VeloCloud SD-WAN logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Arista VeloCloud SD-WAN (formerly VMware VeloCloud) logs to Google Security Operations using Bindplane.

Arista VeloCloud SD-WAN is a software-defined wide area networking solution that simplifies branch office networking by virtualizing WAN connections and providing centralized management through the SD-WAN Orchestrator. It delivers application-aware routing, dynamic path selection, and integrated firewall capabilities for distributed enterprise environments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Arista VeloCloud SD-WAN Orchestrator



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
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows Installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux Installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <PLACEHOLDER_CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'VELO_FIREWALL'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<PLACEHOLDER_CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <PLACEHOLDER_CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'VELO_FIREWALL'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure syslog forwarding on Arista VeloCloud SD-WAN

  1. Sign in to the **VeloCloud SD-WAN Orchestrator** web interface.
  2. Go to **Configure** > **Profiles**.
  3. Select the profile assigned to the Edge devices that you want to monitor.
  4. Click **Configure Segment** for the appropriate network segment.
  5. Select the **Syslog** tab.
  6. Click **Add Rule** to create a new syslog forwarding rule.
  7. Provide the following configuration details: 
     * **Syslog Collector IP** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
     * **Facility** : Select the appropriate syslog facility (for example, **LOCAL0**).
     * **Severity** : Select the minimum severity level to forward (for example, **INFO** to capture all informational and higher-severity events).
     * **Tag** : Optionally, enter a tag to identify these logs (for example, `velocloud`).
     * **Source Interface** : Select the management interface or appropriate source interface.
  8. In the **Roles** section, select the log categories to forward: 
     * **FIREWALL** \- to forward firewall event logs.
     * **EDGE** \- to forward Edge device operational logs.
  9. Click **Save Changes**.
  10. If you need to override the profile settings for a specific Edge, go to **Configure** > **Edges** , select the Edge, and repeat the syslog configuration under the **Device** tab.

**Note:** Changes made at the profile level apply to all Edges using that profile. Use Edge-level overrides only when specific Edges require different syslog settings.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`cloud_software_label` | `additional.fields` | Merged  
`in_label` | `additional.fields` | Merged  
`proto_label` | `additional.fields` | Merged  
`segment_label` | `additional.fields` | Merged  
`segment_name_label` | `additional.fields` | Merged  
`inter_hostname` | `intermediary.hostname` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`principal_present` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`product_event_type` | `metadata.product_event_type` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Renamed/mapped  
`BYTES_RECEIVED` | `network.received_bytes` | Directly mapped  
`BYTES_SENT` | `network.sent_bytes` | Directly mapped  
`DURATION_SECS` | `network.session_duration.seconds` | Directly mapped  
`SRC` | `principal.asset.ip` | Merged  
`SRC` | `principal.ip` | Merged  
`NAT_SRC` | `principal.nat_ip` | Merged  
`NAT_SPT` | `principal.nat_port` | Directly mapped  
`SPT` | `principal.port` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`ACTION` | `security_result.action_details` | Directly mapped  
`FW_POLICY_NAME` | `security_result.rule_name` | Directly mapped  
`REASON` | `security_result.summary` | Directly mapped  
`DEST_DOMAIN` | `target.administrative_domain` | Directly mapped  
`DEST_NAME` | `target.asset.hostname` | Directly mapped  
`DST` | `target.asset.ip` | Merged  
`DEST_NAME` | `target.hostname` | Directly mapped  
`DST` | `target.ip` | Merged  
`DPT` | `target.port` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `VELO_FIREWALL`  
N/A | `metadata.vendor_name` | Constant: `VELO_FIREWALL`  
`description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`product_event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`cloud_software` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/velo-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
