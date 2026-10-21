---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/amd-dss-firewall/
title: Collect AMD Pensando DSS Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:41:56.802689+00:00
---

# Collect AMD Pensando DSS Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/amd-dss-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AMD Pensando DSS Firewall logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AMD Pensando DSS Firewall logs to Google Security Operations using Bindplane.

AMD Pensando Distributed Services Switch (DSS) Firewall is a hardware-accelerated stateful firewall that runs on the AMD Pensando DPU inside Aruba CX 10000 series switches. It provides microsegmentation and east-west traffic inspection at line rate. The firewall is managed through the AMD Pensando Policy and Services Manager (PSM), which provides centralized policy configuration, monitoring, and syslog export capabilities.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the AMD Pensando Policy and Services Manager (PSM) or Aruba CX 10000 switch management interface.
  * Network connectivity between the Bindplane agent host and the Aruba CX 10000 switch or PSM.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: '<CUSTOMER_ID>'
             endpoint: malachiteingestion-pa.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'AMD_DSS_FIREWALL'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         

**Note:** The `endpoint` value (`malachiteingestion-pa.googleapis.com`) is the US multi-region endpoint. If your Google SecOps tenant is in a different region, use the appropriate regional endpoint. See the [Regional endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list.


  * Replace the port and IP address as required in your infrastructure.
  * Replace `<CUSTOMER_ID>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved.



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
         




## Configure syslog forwarding on AMD Pensando DSS Firewall

The AMD Pensando DSS Firewall supports two methods for configuring syslog forwarding: through the Pensando Policy and Services Manager (PSM) web interface or through the AOS-CX CLI on the Aruba CX 10000 switch.

### Configure syslog export via Pensando PSM

  1. Sign in to the **AMD Pensando Policy and Services Manager (PSM)** web interface.
  2. Go to **Monitoring > Alerts & Events**.
  3. Select the **Destinations** tab.
  4. Click **Add Destination**.
  5. Provide the following configuration details: 
     * **Destination type** : Select **Syslog**.
     * **Server address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter the port configured in the Bindplane agent `config.yaml` (for example, `514`).
     * **Protocol** : Select **UDP** to match the Bindplane agent receiver configuration.
     * **Format** : Select **BSD (RFC 5424)**.
  6. Click **Save** to create the syslog destination.
  7. Select the **Alert Policies** tab.
  8. Click **Add Alert Policy** to define which events and alerts to forward.
  9. Select the desired event categories and severity levels.
  10. In the **Destinations** section, select the syslog destination you created.
  11. Click **Save** to activate the alert policy.

**Note:** The PSM sends syslog messages in RFC 5424 format. Ensure that the Bindplane agent receiver is configured to accept this format.



### Configure syslog via AOS-CX CLI on Aruba CX 10000

  1. Connect to the **Aruba CX 10000 switch** via SSH or console.
  2. Enter configuration mode:
         
         configure terminal
         

  3. Configure the remote syslog server with UDP (replace `<BINDPLANE_IP>` with your Bindplane agent IP address):
         
         logging <BINDPLANE_IP> udp 514 severity info
         

Or for TCP:
         
         logging <BINDPLANE_IP> tcp 1470 severity info
         

Or for TLS:
         
         logging <BINDPLANE_IP> tls 6514 severity info
         

**Note:** Default ports for AOS-CX are UDP=514, TCP=1470, TLS=6514. Specify the port explicitly to match your Bindplane agent configuration.
  4. Set the syslog facility:
         
         logging facility local0
         

  5. Save the configuration:
         
         write memory
         

  6. Exit configuration mode:
         
         exit
         




For more information about the AOS-CX logging command, see the [AOS-CX CLI Reference](https://arubanetworking.hpe.com/techdocs/AOS-CX/AOSCX-CLI-Bank/cli_832x/Content/Chp_RSyslog/RSyslog_cmds/log-10.htm).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `read_only_udm.metadata.product_event_type` | Direct mapping.  
`action` | `read_only_udm.security_result.action` | If action is "deny", set to "BLOCK". If action is "allow", set to "ALLOW".  
`column10` | `read_only_udm.network.session_id` | Direct mapping.  
`column11` | `read_only_udm.additional.fields.value.string_value` | Direct mapping. Key is hardcoded as "security_policy_id".  
`column12` | `read_only_udm.security_result.rule_id` | Direct mapping.  
`column13` | `read_only_udm.security_result.rule_name` | Direct mapping.  
`column14` | `read_only_udm.network.sent_packets` | Direct mapping.  
`column15` | `read_only_udm.network.sent_bytes` | Direct mapping.  
`column16` | `read_only_udm.network.received_packets` | Direct mapping.  
`column17` | `read_only_udm.network.received_bytes` | Direct mapping.  
`column18` | `read_only_udm.additional.fields.value.string_value` | Direct mapping. Key is hardcoded as "vlan".  
`column19` | `read_only_udm.principal.asset.software.vendor_name` | Direct mapping.  
`column19` | `read_only_udm.principal.asset.software.name` | Direct mapping.  
`column2` | `read_only_udm.metadata.product_event_type` | Direct mapping.  
`column20` | `read_only_udm.principal.asset.software.version` | Direct mapping.  
`column21` | `read_only_udm.principal.asset_id` | Concatenates "asset_id:" with the value of column21.  
`column22` | `read_only_udm.principal.asset.attribute.labels.value` | Direct mapping. Key is hardcoded as "device_name".  
`column23` | `read_only_udm.principal.asset.attribute.labels.value` | Direct mapping. Key is hardcoded as "unit_id".  
`column24` | `read_only_udm.metadata.product_version` | Direct mapping.  
`column25` | `read_only_udm.additional.fields.value.string_value` | Direct mapping. Key is hardcoded as "policy_name".  
`column25` | `read_only_udm.security_result.rule_type` | Direct mapping.  
`column4` | `read_only_udm.principal.resource.product_object_id` | Direct mapping.  
`column5` | `read_only_udm.principal.ip` | Direct mapping.  
`column6` | `read_only_udm.principal.port` | Direct mapping.  
`column7` | `read_only_udm.target.ip` | Direct mapping.  
`column8` | `read_only_udm.target.port` | Direct mapping.  
`column9` | `read_only_udm.network.ip_protocol` | Maps the numeric protocol number to its corresponding name (e.g., 6 to TCP, 17 to UDP).  
`dip` | `read_only_udm.target.ip` | Direct mapping.  
`dport` | `read_only_udm.target.port` | Direct mapping.  
`dvc` | `read_only_udm.intermediary.hostname` | If dvc is not an IP address, map to hostname. Otherwise, map to IP.  
`iflowbytes` | `read_only_udm.network.sent_bytes` | Direct mapping.  
`iflowpkts` | `read_only_udm.network.sent_packets` | Direct mapping.  
`msg_id` | `read_only_udm.additional.fields.value.string_value` | Direct mapping. Key is hardcoded as "msg_id".  
`policy_name` | `read_only_udm.additional.fields.value.string_value` | Direct mapping. Key is hardcoded as "policy_name".  
`policy_name` | `read_only_udm.security_result.rule_type` | Direct mapping.  
`proc_id` | `read_only_udm.target.process.pid` | Direct mapping.  
`proc_name` | `read_only_udm.target.application` | Direct mapping.  
`protocol_number_src` | `read_only_udm.network.ip_protocol` | Maps the numeric protocol number to its corresponding name (e.g., 6 to TCP, 17 to UDP).  
`rflowbytes` | `read_only_udm.network.received_bytes` | Direct mapping.  
`rflowpkts` | `read_only_udm.network.received_packets` | Direct mapping.  
`rule_id` | `read_only_udm.security_result.rule_id` | Direct mapping.  
`rule_name` | `read_only_udm.security_result.rule_name` | Direct mapping.  
`sd` | `read_only_udm.additional.fields.value.string_value` | Direct mapping. Key is hardcoded as "sd".  
`security_policy_id` | `read_only_udm.additional.fields.value.string_value` | Direct mapping. Key is hardcoded as "security_policy_id".  
`session_id` | `read_only_udm.network.session_id` | Direct mapping.  
`session_state` | `read_only_udm.metadata.product_event_type` | Direct mapping.  
`sip` | `read_only_udm.principal.ip` | Direct mapping.  
`software_version` | `read_only_udm.principal.asset.software.version` | Direct mapping.  
`sport` | `read_only_udm.principal.port` | Direct mapping.  
`ts` | `read_only_udm.metadata.event_timestamp` | The timestamp from the log is parsed and formatted into the UDM timestamp format.  
`vlan` | `read_only_udm.additional.fields.value.string_value` | Direct mapping. Key is hardcoded as "vlan".  
| `read_only_udm.metadata.event_type` | If both sip and dip are present, set to "NETWORK_UNCATEGORIZED". If only sip is present, set to "STATUS_UPDATE". Otherwise, set to "GENERIC_EVENT".  
| `read_only_udm.metadata.log_type` | Hardcoded to "AMD_DSS_FIREWALL".  
| `read_only_udm.metadata.product_name` | Hardcoded to "AMD_DSS_FIREWALL".  
| `read_only_udm.metadata.vendor_name` | Hardcoded to "AMD_DSS_FIREWALL".  
| `read_only_udm.principal.resource.resource_type` | Hardcoded to "VPC_NETWORK".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/amd-dss-firewall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
