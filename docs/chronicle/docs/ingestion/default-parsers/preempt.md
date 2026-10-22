---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/preempt/
title: Collect Preempt logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:53.862297+00:00
---

# Collect Preempt logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/preempt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Preempt logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Preempt logs to Google Security Operations using the Bindplane agent.

Preempt Security is an identity threat detection and response platform that generates security alerts for Active Directory threats, including anomalous authentication behavior, privilege escalation, and lateral movement. It exports logs in CEF (Common Event Format) format via syslog.

**Note:** Preempt Security was acquired by CrowdStrike in September 2020 and has been fully integrated into **CrowdStrike Falcon Identity Protection**. The standalone Preempt product is no longer available. If you have migrated to CrowdStrike Falcon Identity Protection, see the [Collect CrowdStrike Falcon logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-edr) guide instead.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Preempt server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Preempt management console with administrator permissions



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/preempt:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: PREEMPT
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/preempt_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/preempt
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: Receives syslog over TCP. Use `udplog` if your Preempt deployment forwards over UDP.
    * `0.0.0.0:514`: Listens on all interfaces on port 514. Change the port if needed (for example, `1514` for non-root Linux).
  * **Exporter configuration:**

    * `<CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<CUSTOMER_ID>`: Customer ID from the **Get Google SecOps customer ID** step.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/preempt:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: PREEMPT
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
             




## Configure Preempt syslog forwarding

**Note:** Preempt Security is a deprecated product. These instructions apply to legacy Preempt deployments only. If you have migrated to CrowdStrike Falcon Identity Protection, use the CrowdStrike integration guide instead.

  1. Sign in to the **Preempt management console**.
  2. Navigate to **Settings > SIEM Integration**.
  3. Enable syslog forwarding.
  4. Provide the following configuration details: 
     * **Protocol** : Select **TCP** (must match the Bindplane agent receiver configuration).
     * **Format** : Select **CEF**.
     * **Syslog server address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
  5. Select the event types to forward: 
     * Alerts
     * Policy violations
     * Anomalous authentication events
  6. Click **Save** or **Apply**.
  7. Verify that logs are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
event_id, _target | metadata.event_type | Set to "SCAN_NETWORK" if _target not empty and event_id == "SUSPICIOUS_DOMAIN_ACTIVITY"; "USER_UNCATEGORIZED" if _target not empty and event_id in ["UNUSUAL_ENDPOINT_ACCESS", "UNUSUAL_ACTIVITY", "UNUSUAL_ENDPOINT_USE"]; "NETWORK_UNCATEGORIZED" if event_id == "APPLIANCE_CONNECTIVITY_FAILURE"; else "GENERIC_EVENT"  
event_id | metadata.product_event_type | Value copied directly  
version | metadata.product_version | Value copied directly  
cs1 | metadata.url_back_to_product | Value from cs1 if cs1Label == "incidentLink"  
| network.ip_protocol | Set to "TCP" if event_id == "APPLIANCE_CONNECTIVITY_FAILURE"  
dhost, host | principal.hostname | Value from dhost if dhost not empty and not IP, else from host if host not empty and not IP  
dhost, host | principal.ip | Value from dhost if dhost is IP, else from host if host is IP  
description, event_name, act, cs5, cs2, externalId, cn2 | security_result.description | If description not empty, value from description; else concatenated from event_name, act, status from cs5 if cs5Label == "status" or cs2 if cs2Label == "status", IncidentID from externalId, CompromisedEntities from cn2  
cs1 | security_result.rule_name | Value from cs1 if cs1Label == "ruleName"  
severity | security_result.severity | Converted from integer: HIGH if > 7, MEDIUM if > 4, LOW if > 2, INFORMATIONAL if > 0, else UNKNOWN_SEVERITY; or set to LOW if cat == "Policy Log" and severity == "INFO"  
severity | security_result.severity_details | Value copied directly  
act, event_name | security_result.summary | Value from act if not empty, else from event_name  
destinationServiceName | target.application | Value from destinationServiceName if event_id == "APPLIANCE_CONNECTIVITY_FAILURE"  
shost | target.hostname | Value copied directly  
src, dst | target.ip | Value from src, or dst if event_id == "APPLIANCE_CONNECTIVITY_FAILURE"  
suser | target.user.userid | Value copied directly  
vendor | metadata.vendor_name | Value from vendor if not empty, else set to "PreemptSecurity"  
product | metadata.product_name | Value from product if not empty, else set to "PBF"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/preempt-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
