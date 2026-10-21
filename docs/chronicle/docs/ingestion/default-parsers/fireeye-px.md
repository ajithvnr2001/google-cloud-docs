---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-px/
title: Collect Trellix (formerly FireEye) PX logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:20:04.711059+00:00
---

# Collect Trellix (formerly FireEye) PX logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-px/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix (formerly FireEye) PX logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest FireEye (now known as Trellix) PX logs to Google Security Operations using the Bindplane agent.

Trellix PX (Network Forensics) captures full network packets and generates metadata logs about captured sessions, detected threats, and network artifacts. The parser maps these logs to the Unified Data Model (UDM), extracting network connection details, DNS queries and responses, HTTP metadata, and flow-level attributes.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Trellix PX appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Trellix PX appliance with administrator role



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
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/fireeye_px:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FIREEYE_PX
                raw_log_field: body
        
        service:
            pipelines:
                logs/fireeye_px_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/fireeye_px
        




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
             




## Configure FireEye PX syslog forwarding

  1. Sign in to the **FireEye PX** web management interface.
  2. Go to **Settings > Notifications > Syslog**.
  3. Click **Add Syslog Server** (or edit an existing entry).
  4. Provide the following configuration details: 
     * **Server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
  5. Select the event types to forward: 
     * Session metadata
     * Detected threats
     * Network artifacts
     * DNS queries and responses
     * HTTP metadata
  6. Click **Save**.
  7. Verify logs are being received by checking the Bindplane agent logs.

**Note:** FireEye PX also supports REST API-based log export. For syslog forwarding, ensure that the PX appliance has network connectivity to the Bindplane agent on the configured port.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
dns.authorities.0.rrname | dns_answers.name | Value copied directly if not empty  
dns.authorities.0.ttl | dns_answers.ttl | Converted to string then to uinteger if not empty  
dns.authorities.0.rrtype | dns_answers.type | Mapped to numeric value based on rrtype string (A=1, AAAA=28, etc.), then converted to uinteger if not empty  
dns.dnsQName | dns_question.name | Value copied directly if not empty  
dns.dnsQRType | dns_question.type | Mapped to numeric value based on rrtype string (A=1, AAAA=28, etc.), then converted to uinteger if not empty  
dns.dnsFlags, pxflow.octetDeltaCount, pxflow.octetDeltaCountReverse | event.idm.read_only_udm.additional.fields | Merged as labels (flags_label, octetDeltaCount_label, octetDeltaCountReverse_label) if not empty  
event_type | metadata.event_type | Set to NETWORK_HTTP if event_type == "http" and has_principal and has_target; NETWORK_DNS if event_type == "dns" and has_principal and has_target; NETWORK_CONNECTION otherwise if has_principal and has_target; GENERIC_EVENT if not  
pxuuid | metadata.product_log_id | Value copied directly if not empty  
dns_answers | network.dns.answers | Merged directly if not empty  
dns.dnsId | network.dns.id | Renamed and converted to uinteger if not empty  
dns_question | network.dns.questions | Merged directly if not empty  
dns.rcode | network.dns.response_code | Mapped to numeric response code based on rcode string (NOERROR=0, FORMERR=1, etc.), then converted to uinteger  
http.httpMethod | network.http.method | Value copied directly if not empty  
http.http_user_agent | network.http.user_agent | Value copied directly if not empty  
protocolIdentifierName | network.ip_protocol | Value copied directly if not empty  
flow_id | network.session_id | Converted to string then copied directly if not empty  
pxflow.egressInterface | principal.asset.attribute.labels | Merged as egress_interface label if not empty  
http.httpHost | principal.hostname | Value copied directly and sets has_principal to true if not empty  
sourceIPv4Address | principal.ip | Extracted using grok pattern %{IP:ip}, merged if grok succeeds  
pxflow.sourceEtherAddress | principal.mac | Merged directly and sets has_principal to true if not empty  
sourceTransportPort | principal.port | Renamed and converted to integer if not empty  
sensor | security_result.about.labels | Merged as sensor_label if not empty  
in_iface | security_result.rule_labels | Merged as in_iface_label if not empty  
pxflow.ingressInterface | target.asset.attribute.labels | Merged as ingress_interface label if not empty  
destinationIPv4Address | target.ip | Extracted using grok pattern %{IP:ip}, merged if grok succeeds  
pxflow.destinationEtherAddress | target.mac | Merged directly and sets has_target to true if not empty  
destinationTransportPort | target.port | Renamed and converted to integer if not empty  
http.httpURL | target.url | Value copied directly if not empty  
| metadata.vendor_name | Set to "Fireeye"  
| metadata.product_name | Set to "PX"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-px-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
