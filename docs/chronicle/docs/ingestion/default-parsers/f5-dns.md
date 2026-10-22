---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dns/
title: Collect F5 DNS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:30.864404+00:00
---

# Collect F5 DNS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect F5 DNS logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest F5 DNS logs to Google Security Operations using the Bindplane agent.

F5 BIG-IP DNS is a DNS delivery solution that generates syslog messages for DNS queries, responses, and system events. The parser extracts fields from syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the F5 BIG-IP appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to F5 BIG-IP



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
          chronicle/f5_dns:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: F5_DNS
            raw_log_field: body
        
        service:
          pipelines:
            logs/f5_dns_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/f5_dns
        




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
          chronicle/f5_dns:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: F5_DNS
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
             




## Configure a pool of remote logging servers

  1. Sign in to the **F5 BIG-IP** web UI.
  2. On the **Main** tab, go to **DNS > Delivery > Load Balancing > Pools** or **Local Traffic > Pools**.
  3. Click **Create**.
  4. Provide the following configuration details: 
     * **Name** : Enter a unique name for the pool.
     * Using **New Members** setting: 
       * Enter the Bindplane agent IP address in the **Address** field.
       * Enter the Bindplane agent port number in the **Service Port** field.
  5. Click **Add > Finished**.



## Configure the remote log destination

  1. On the **Main** tab, go to **System > Logs > Configuration > Log Destinations**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a unique name for this destination.
     * **Type** : Select **Remote High-Speed Log**.
     * **Pool Name** : Select the pool of remote log servers to which you want the BIG-IP system to send log messages.
     * **Protocol** : Select the protocol used.
  4. Click **Finished**.



## Creating a formatted remote log destination

  1. On the **Main** tab, go to **System > Logs > Configuration > Log Destinations**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a unique name for this destination.
     * **Type** : Select **Remote Syslog**.
     * **Format** : Select the log format.
     * **Forward To** : Select **High-Speed Log Destination > the destination that points to the pool of remote Syslog servers**.
  4. Click **Finished**.



## Configure Log Publisher

  1. On the **Main** tab, go to **System > Logs > Configuration > Log Publishers**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a unique name for this publisher.
     * **Destinations** : Select the newly-created destination for **Remote Syslog** from the **Available** list, and then click **Move** to move the destination to the **Selected** list.
  4. Click **Finished**.



## Configure a custom DNS logging profile

  1. On the **Main** tab, go to **DNS > Delivery > Profiles > Other > DNS Logging** or **Local Traffic > Profiles > Other > DNS Logging**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a unique name for this profile.
     * **Log Publisher** : Select the newly-created destination to which the system sends DNS log entries.
     * **Log Queries** : Select the **Enabled** checkbox.
     * **Log Responses** : Select the **Enabled** checkbox.
     * **Include Query ID** : Select the **Enabled** checkbox.
  4. Click **Finished**.



## Add the DNS profile to the DNS Listener

  1. On the **Main** tab, go to **DNS > Delivery > Listeners > select DNS listener**.
  2. From the **DNS profile** in the **Service** section, select the **DNS profile** that you configured previously.
  3. Click **Update**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`application` | `principal.application` | Directly mapped from the `application` field.  
`cipher_name` | `network.tls.cipher` | Directly mapped from the `cipher_name` field.  
`command_line` | `principal.process.command_line` | Directly mapped from the `command_line` field.  
`desc` | `security_result.description` | Directly mapped from the `desc` field.  
`desc_icrd` | `security_result.description` | Directly mapped from the `desc_icrd` field.  
`dest_ip` | `target.ip` | Directly mapped from the `dest_ip` field.  
`dest_port` | `target.port` | Directly mapped from the `dest_port` field.  
`file_path` | `principal.process.file.full_path` | Directly mapped from the `file_path` field. Set to `true` if `level` is "alert", otherwise not present. Set to `true` if `level` is "alert", otherwise not present.  
`msg3` | `security_result.description` | Directly mapped from the `msg3` field when `application` is "run-parts".  
| `metadata.event_type` | Set to `GENERIC_EVENT` if `event_type` is empty, otherwise mapped from `event_type`. Hardcoded to "DNS". Hardcoded to "F5".  
`principal_hostname` | `principal.hostname` | Directly mapped from the `principal_hostname` field.  
`proc_id` | `principal.process.pid` | Directly mapped from the `proc_id` field.  
`received_bytes` | `network.received_bytes` | Directly mapped from the `received_bytes` field.  
`resource_id` | `target.resource.id` | Directly mapped from the `resource_id` field.  
`resource_parent` | `principal.resource.parent` | Directly mapped from the `resource_parent` field.  
`response_code` | `network.http.response_code` | Directly mapped from the `response_code` field. Determined based on the `level` field.  
`src_ip` | `principal.ip` | Directly mapped from the `src_ip` field.  
`src_port` | `principal.port` | Directly mapped from the `src_port` field.  
`tls_version` | `network.tls.version` | Directly mapped from the `tls_version` field.  
`userName` | `principal.user.userid` | Directly mapped from the `userName` field.  
`when` | `event.timestamp` | Calculated from `datetime1` and `timezone` or `datetime` and `timezone`.  
`query_response_code` | `event.idm.read_only_udm.network.dns.response_code` | Mapped from changelog  
`User` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`attemptCount` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`rule_id_val` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`query_type` | `event.idm.read_only_udm.question.type` | Mapped from changelog  
`record_type` | `event.idm.read_only_udm.question.type` | Mapped from changelog  
`dns_class` | `event.idm.read_only_udm.network.dns.question.class` | Mapped from changelog  
`intermediary_host` | `event.idm.read_only_udm.network.dns.answer.data` | Mapped from changelog  
`intermediary_ip` | `event.idm.read_only_udm.network.dns.answer.data` | Mapped from changelog  
`ttl_data` | `event.idm.read_only_udm.network.dns.answer.ttl` | Mapped from changelog  
`dns_answer_domain` | `event.idm.read_only_udm.network.dns.answer.name` | Mapped from changelog  
`qclass` | `event.idm.read_only_udm.network.dns.answer.class` | Mapped from changelog  
`dns_name` | `event.idm.read_only_udm.question.name` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`dest_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`host` | `event.idm.read_only_udm.principal.ip` & `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`partition` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attempts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tty` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`start` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`end` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-dns-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
