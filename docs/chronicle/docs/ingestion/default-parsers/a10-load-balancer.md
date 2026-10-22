---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/a10-load-balancer/
title: Collect A10 Network Load Balancer logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:27.194450+00:00
---

# Collect A10 Network Load Balancer logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/a10-load-balancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect A10 Network Load Balancer logs

**Parser Version:** 7.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest A10 Network Load Balancer logs to Google Security Operations using Bindplane agent.

A10 Networks provides application delivery controllers (ADCs) and load balancers that optimize and secure application traffic. The A10 Thunder series supports server load balancing, SSL offloading, DDoS protection, and web application firewall capabilities.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and A10 Load Balancer
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the A10 Load Balancer CLI (admin credentials)



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
          chronicle/a10_lb:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: A10_LOAD_BALANCER
            raw_log_field: body
        
        service:
          pipelines:
            logs/a10_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/a10_lb
        




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
          chronicle/a10_lb:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: A10_LOAD_BALANCER
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
             




## Configure syslog forwarding on the A10 Load Balancer

  1. Establish an SSH connection to the A10 Load Balancer using an SSH client.
  2. Enter configuration mode by running the following command:
         
         config
         

  3. Configure the remote syslog server by running the following command:
         
         logging host <BINDPLANE_IP> <PORT>
         

     * Replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * Replace `<PORT>` with the port configured in the Bindplane receiver (for example, `514`).
  4. Set the severity level by running the following command:
         
         logging level information
         

**Note:** This sends informational messages and above (warnings, errors) to the Bindplane agent. Available levels include `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, and `debugging`.
  5. Ensure syslog logging is enabled by running the following command:
         
         logging enable
         

  6. Save the configuration to ensure it persists after a reboot:
         
         write memory
         

  7. Example of a complete CLI configuration:
         
         config
         logging host 192.168.1.100 514
         logging level information
         logging enable
         write memory
         




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`dns` | `additional.fields.dns.value.string_value` | The value is taken from the `dns` field extracted by the grok pattern.  
`dns_server` | `additional.fields.dns_server.value.string_value` | The value is taken from the `dns_server` field extracted by the grok pattern.  
`gslb` | `additional.fields.gslb.value.string_value` | The value is taken from the `gslb` field extracted by the grok pattern.  
`host_name` | `principal.hostnameprincipal.asset.hostname` | The value is taken from the `host_name` field extracted by the grok pattern.  
`httpmethod` | `network.http.method` | The value is taken from the `httpmethod` field extracted by the grok pattern.  
`partion_id` | `additional.fields.partion_id.value.string_value` | The value is taken from the `partion_id` field extracted by the grok pattern.  
`prin_ip` | `principal.ipprincipal.asset.ip` | The value is taken from the `prin_ip` field extracted by the grok pattern.  
`prin_mac` | `principal.mac` | The value is taken from the `prin_mac` field extracted by the grok pattern, with dots removed and colons inserted every two characters.  
`prin_port` | `principal.port` | The value is taken from the `prin_port` field extracted by the grok pattern and converted to an integer.  
`proto` | `network.ip_protocol` | The value is taken from the `proto` field extracted by the grok pattern. If the `message` field contains `UDP`, the value is set to `UDP`.  
`sessionid` | `network.session_id` | The value is taken from the `sessionid` field extracted by the grok pattern.  
`status_code` | `network.http.response_code` | The value is taken from the `status_code` field extracted by the grok pattern and converted to an integer.  
`tar_ip` | `target.iptarget.asset.ip` | The value is taken from the `tar_ip` field extracted by the grok pattern.  
`tar_mac` | `target.mac` | The value is taken from the `tar_mac` field extracted by the grok pattern, with dots removed and colons inserted every two characters.  
`tar_port` | `target.port` | The value is taken from the `tar_port` field extracted by the grok pattern and converted to an integer.  
`time` | `metadata.event_timestamp.seconds` | The value is parsed from the `time` field extracted by the grok pattern, using multiple possible date formats.  
`url` | `target.url` | The value is taken from the `url` field extracted by the grok pattern.  
`user` | `principal.user.userid` | The value is taken from the `user` field extracted by the grok pattern.  
N/A | `metadata.event_type` | Determined by the parser logic based on the presence of principal and target information:  
-`NETWORK_CONNECTION`: if both principal and target information are present.  
-`STATUS_UPDATE`: if only principal information is present.  
-`GENERIC_EVENT`: otherwise.  
N/A | `metadata.log_type` | Hardcoded to `A10_LOAD_BALANCER`.  
N/A | `network.application_protocol` | Set to `HTTP` if the `proto` field is `HTTP`.  
`dhost` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`inter_host` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`virtualserver` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`Script_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`len` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`seq_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`desc` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`target_user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`rule_name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`vendor_severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`facility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`proxy_machine_ip` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`event_dt` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`prin_host` | `principal.hostname` | Mapped from changelog  
`app` | `target.application` | Mapped from changelog  
`device_version` | `metadata.product_version` | Mapped from changelog  
`device_vendor` | `metadata.vendor_name` | Mapped from changelog  
`device_product` | `metadata.product_name` | Mapped from changelog  
`event_name" and "device_event_class_id` | `metadata.product_event_type` | Mapped from changelog  
`severity` | `security_result.severity` | Mapped from changelog  
`src` | `principal.ip` | Mapped from changelog  
`spt` | `principal.port` | Mapped from changelog  
`dst` | `target.ip` | Mapped from changelog  
`dpt` | `target.port` | Mapped from changelog  
`msg` | `metadata.description` | Mapped from changelog  
`suser` | `principal.user.user_display_name` | Mapped from changelog  
`act" and "cn1` | `additional.fields` | Mapped from changelog  
`app_proto` | `network.application_protocol` | Mapped from changelog  
`tls_version` | `network.tls.version` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/a10-load-balancer-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
