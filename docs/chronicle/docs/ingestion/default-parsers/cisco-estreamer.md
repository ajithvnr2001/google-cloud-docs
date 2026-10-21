---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-estreamer/
title: Collect Cisco eStreamer logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:18:37.758785+00:00
---

# Collect Cisco eStreamer logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-estreamer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco eStreamer logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Cisco eStreamer logs to Google Security Operations using Bindplane.  
The parser extracts fields from Cisco eStreamer syslog formatted logs with key-value pairs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Cisco Firepower Management Center (FMC).
  * A Linux system to run the eNcore CLI client.



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

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or `C:\Program Files\observIQ OpenTelemetry Collector` directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:5514"
         
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
             customer_id: YOUR_CUSTOMER_ID
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'CISCO_ESTREAMER'
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
  * Replace `YOUR_CUSTOMER_ID` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.

**Note:** Port 5514 is used to avoid requiring root privileges. If you need to use port 514, ensure the Bindplane agent has appropriate permissions.

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: YOUR_CUSTOMER_ID
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'CISCO_ESTREAMER'
            raw_log_field: body
            ingestion_labels:
        


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
         




## Configure Syslog forwarding on Cisco eStreamer

### Configure eStreamer on Firepower Management Center

  1. Sign in to the **Firepower Management Center**.
  2. Go to **System > Integration > eStreamer**.
  3. Click **eStreamer** to access the eStreamer Event Configuration.
  4. Select the check boxes next to the types of events you want to capture: 
     * **Intrusion Events** : For intrusion detection events
     * **Intrusion Event Packet Data** : For packet captures associated with intrusion events
     * **Connection Events** : For network connection data
     * **Security Intelligence Events** : For threat intelligence data
     * **File Events** : For file analysis events
     * **Malware Events** : For malware detection events
  5. Click **Save**.



### Create eStreamer Client

  1. In the **eStreamer** page, click **Create Client**.
  2. Provide the following configuration details: 
     * **Hostname** : Enter the IP address of the Linux system where eNcore client will run.
     * **Password** : Enter a password to encrypt the certificate file.
  3. Click **Save**.
  4. Download the generated PKCS12 certificate file and transfer it to your eNcore client system.



### Install and Configure eNcore CLI Client

  1. On your Linux system, download the eStreamer eNcore CLI client from Cisco.
  2. Extract the eNcore package:
         
         tar -xzf eStreamer-eNcore-*.tar.gz
         cd eStreamer-eNcore-*
         

  3. Run the setup script:
         
         ./encore.sh setup
         

  4. When prompted, choose the output format for key-value pairs (compatible with SIEM systems).

  5. Enter the FMC IP address and the PKCS12 certificate password.

  6. Configure the `estreamer.conf` file to output syslog messages to your Bindplane agent:

     * Open the `estreamer.conf` file in a text editor.
     * Locate the outputters section and configure it to send syslog to your Bindplane agent:
    
    {
      "handler": {
        "outputters": [
          {
            "name": "syslog",
            "adapter": "kvpair",
            "enabled": true,
            "stream": {
              "uri": "udp://BINDPLANE_AGENT_IP:5514"
            }
          }
        ]
      }
    }
    

  7. Replace `BINDPLANE_AGENT_IP` with the IP address of your Bindplane agent.




### Start eNcore Client

  1. Test the connection in foreground mode:
         
         ./encore.sh foreground
         

  2. Once verified, start eNcore as a background service:
         
         ./encore.sh start
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_deviceInboundInterface` | `additional.fields` | Merged  
`additional_deviceOutboundInterface` | `additional.fields` | Merged  
`additional_start` | `additional.fields` | Merged  
`has_target` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`dvchost` | `intermediary.asset.hostname` | Directly mapped  
`hostname` | `intermediary.asset.hostname` | Directly mapped  
`dvchost` | `intermediary.hostname` | Directly mapped  
`hostname` | `intermediary.hostname` | Directly mapped  
`dvcpid` | `intermediary.process.pid` | Directly mapped  
`ts` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped values (5 total, e.g. `true` → `NETWORK_HTTP`, `true` → `NETWORK_DNS`, `true` → `NETW...  
`has_target` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`product_event_type` | `metadata.product_event_type` | Directly mapped  
`product_name` | `metadata.product_name` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`vendor_name` | `metadata.vendor_name` | Directly mapped  
`app` | `network.application_protocol` | Directly mapped  
`src` | `network.dhcp.ciaddr` | Directly mapped  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`dns_question` | `network.dns.questions` | Merged  
`requestClientApplication` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`bytesIn` | `network.received_bytes` | Directly mapped  
`bytesOut` | `network.sent_bytes` | Directly mapped  
`deviceExternalId` | `principal.asset.asset_id` | Directly mapped  
`src` | `principal.asset.ip` | Merged  
`src` | `principal.ip` | Merged  
`spt` | `principal.port` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`act` | `security_result.action_details` | Directly mapped  
`category` | `security_result.category` | Merged  
`cat` | `security_result.category_details` | Merged  
`cs5` | `security_result.description` | Directly mapped  
`blockLength_label` | `security_result.detection_fields` | Merged  
`blockType_label` | `security_result.detection_fields` | Merged  
`cs1_var` | `security_result.detection_fields` | Merged  
`cs2_var` | `security_result.detection_fields` | Merged  
`cs3_var` | `security_result.detection_fields` | Merged  
`cs4_var` | `security_result.detection_fields` | Merged  
`cs5_var` | `security_result.detection_fields` | Merged  
`cs6_var` | `security_result.detection_fields` | Merged  
`suser_var` | `security_result.detection_fields` | Merged  
`cs6` | `security_result.rule_id` | Directly mapped  
`severity` | `security_result.severity_details` | Directly mapped  
`outcome` | `security_result.summary` | Directly mapped  
`destinationDnsDomain` | `target.asset.hostname` | Directly mapped  
`dst` | `target.asset.ip` | Merged  
`fname` | `target.file.full_path` | Directly mapped  
`fileType` | `target.file.mime_type` | Directly mapped  
`fileHash` | `target.file.sha256` | Directly mapped  
`fsize` | `target.file.size` | Directly mapped  
`destinationDnsDomain` | `target.hostname` | Directly mapped  
`host` | `target.hostname` | Directly mapped  
`dst` | `target.ip` | Merged  
`dpt` | `target.port` | Directly mapped  
`request` | `target.url` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `NETWORK_HTTP`  
N/A | `network.direction` | Constant: `INBOUND`  
`BLOCK` | `security_result.action` | Mapped from changelog  
`SOFTWARE_PUA` | `security_result.category` | Mapped from changelog  
`NETWORK_COMMAND_AND_CONTROL` | `security_result.category` | Mapped from changelog  
`TOR_EXIT_NODE` | `security_result.category` | Mapped from changelog  
`PHISHING` | `security_result.category` | Mapped from changelog  
`NETWORK_MALICIOUS` | `security_result.category` | Mapped from changelog  
`request` | `network.http.referral_url` | Mapped from changelog  
`destinationDnsDomain` | `network.dns.questions.name` | Mapped from changelog  
`security_result.action` | `BLOCK` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-estreamer-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
