---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-webproxy/
title: Collect Fortinet Web Proxy logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:20.046207+00:00
---

# Collect Fortinet Web Proxy logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-webproxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet Web Proxy logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortinet Web Proxy logs to Google Security Operations using the Bindplane agent.

Fortinet FortiGate web proxy generates logs for explicit and transparent proxy sessions, capturing HTTP/HTTPS traffic, URL filtering decisions, and web access events. The logs use syslog key-value format and include network metadata, security actions, and user identity information.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the FortiGate appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the FortiGate appliance with administrator permissions



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
          chronicle/fortinet_webproxy:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: FORTINET_WEBPROXY
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/webproxy_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/fortinet_webproxy
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `fortinet_webproxy`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `FORTINET_WEBPROXY`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `webproxy_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/fortinet_webproxy:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: FORTINET_WEBPROXY
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
             




## Configure Fortinet FortiGate web proxy syslog forwarding

  1. Sign in to the **FortiGate** web interface.
  2. Go to **Log & Report > Log Settings**.
  3. Scroll down to the **Remote Logging and Archiving** section.
  4. Under **Syslog** , click **Add**.
  5. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle-Bindplane`).
     * **IP Address/FQDN** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Protocol** : Select **UDP**.
     * **Minimum Level** : Select **Information** or **Notification**.
  6. Ensure the **Web Proxy** log category is enabled. Alternatively, use the CLI to configure the syslog filter:
         
         config log syslogd setting
             set status enable
             set server <BINDPLANE_AGENT_IP>
             set port 514
         end
         config log syslogd filter
             set filter "logid(0300)"
             set filter-type include
         end
         

     * The `0300` log ID range covers web proxy events. Adjust the filter according to your environment.
     * Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.
  7. Click **OK** to save.

  8. Click **Apply** at the top right to apply the configuration.

  9. Verify that syslog messages are being received by checking the Bindplane agent logs.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
group, profile, agent, subtype, catdesc, reqtype | additional.fields | Merged with labels created from each field  
action, has_network, has_principal, has_target | metadata.event_type | Set to USER_LOGIN if action is auth-logon, else NETWORK_HTTP if has_network true, else NETWORK_CONNECTION if has_principal and has_target true, else STATUS_UPDATE if has_principal true, else GENERIC_EVENT  
eventtype | metadata.product_event_type | Value copied directly  
logid | metadata.product_log_id | Value copied directly  
| metadata.product_name | Set to "FORTINET_WEBPROXY"  
| metadata.vendor_name | Set to "FORTINET_WEBPROXY"  
service | network.application_protocol | Value copied directly if service in HTTP, HTTPS  
direction | network.direction | Set to INBOUND if direction in incoming, inbound, response, else OUTBOUND if in outgoing, outbound  
httpmethod | network.http.method | Value copied directly if httpmethod in GET, POST  
referralurl | network.http.referral_url | Value copied directly  
proto, subtype, service | network.ip_protocol | Set to UDP if proto=17, TCP if proto=6 or subtype=wad, IP6IN4 if proto=41, ICMP if service=PING or proto=1 or service matches ICMP  
rcvdbyte | network.received_bytes | Converted to unsigned integer  
sentbyte | network.sent_bytes | Converted to unsigned integer  
sessionid | network.session_id | Value copied directly  
devname | principal.asset.hostname | Value copied directly  
srcip | principal.asset.ip | Value copied directly  
devname | principal.hostname | Value copied directly  
srcip | principal.ip | Value copied directly  
srccountry | principal.location.country_or_region | Value copied directly if not Reserved and not empty  
srcport | principal.port | Converted to integer  
srcuuid | principal.user.product_object_id | Value copied directly  
vd | principal.user.user_display_name | Value copied directly  
user | principal.user.userid | Value copied directly  
filtername | security_result.about.resource.attribute.labels | Merged with label created from filtername if not empty and not -  
action | security_result.action | Set to BLOCK if action=blocked, ALLOW if action in accept, passthrough  
devid, policyid, srcintf, srcintfrole, ratemethod, cat | security_result.detection_fields | Merged with labels created from each field  
msg | security_result.description | Value copied directly  
poluuid | security_result.rule_id | Value copied directly  
policytype | security_result.rule_type | Value copied directly  
level | security_result.severity | Set to HIGH if level=warning, MEDIUM if level=notice  
type | security_result.summary | Value copied directly  
dstip | target.asset.ip | Value copied directly  
filename | target.file.full_path | Value copied directly  
filetype | target.file.mime_type | Value copied directly  
filesize | target.file.size | Converted to unsigned integer  
hostname | target.hostname | Value copied directly  
dstip | target.ip | Value copied directly  
dstcountry | target.location.country_or_region | Value copied directly  
dstport | target.port | Converted to integer  
dstintf, dstintfrole | target.resource.attribute.labels | Merged with labels created from each field  
dstuuid | target.resource.product_object_id | Value copied directly  
url | target.url | Value copied directly  
`eventtime` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`ts` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`transid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`method` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-webproxy-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
