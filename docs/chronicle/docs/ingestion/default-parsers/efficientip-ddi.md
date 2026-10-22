---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/efficientip-ddi/
title: Collect EfficientIP DDI logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:13.134113+00:00
---

# Collect EfficientIP DDI logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/efficientip-ddi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect EfficientIP DDI logs

**Parser Version:** 9.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest EfficientIP DDI logs into Google Security Operations using the Bindplane agent.

EfficientIP SOLIDserver is a comprehensive DDI (DNS-DHCP-IPAM) solution that delivers highly scalable, secure, and robust virtual and hardware appliances for critical network services including DNS, DHCP, IP Address Management, NTP, and TFTP. The platform provides centralized management and automation for network infrastructure with advanced monitoring and security capabilities.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or a Linux host with `systemd`
  * Network connectivity between the Bindplane agent and EfficientIP SOLIDserver appliance
  * If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
  * Administrative access to the EfficientIP SOLIDserver web console
  * SOLIDserver version 8.0 or later (tested with 8.3.x and 8.4.x)



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
         

The service status should be **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service status should be **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/efficientip_ddi:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
             customer_id: 'YOUR_CUSTOMER_ID'
             endpoint: chronicle.googleapis.com
             log_type: EFFICIENTIP_DDI
             raw_log_field: body
             ingestion_labels:
               env: production
               source: solidserver
         
         service:
           pipelines:
             logs/efficientip_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/efficientip_ddi
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on UDP port 514. 
         * For Linux non-root deployments, use port `1514` or higher.
         * Ensure that the port matches the configuration in SOLIDserver.
     * Exporter configuration:

       * `creds_file_path`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `customer_id`: Replace `YOUR_CUSTOMER_ID` with the customer ID from the previous step.

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `log_type`: Set to `EFFICIENTIP_DDI` (exact match required).

       * `ingestion_labels`: Optional labels for categorizing logs (customize as needed).




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/efficientip_ddi:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: EFFICIENTIP_DDI
            raw_log_field: body
            ingestion_labels:
              env: production
              source: solidserver
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux:

    1. Run the following command:
           
           sudo systemctl restart observiq-otel-collector
           

    2. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    3. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows:

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
           




## Configure EfficientIP DDI syslog forwarding

  1. Sign in to the **EfficientIP SOLIDserver** web console.
  2. In the left navigation, click **Administration**.
  3. In the **Monitoring** section, click **Configuration**.
  4. In the menu, click **\+ Add**.
  5. In the **Services** list, select the following services: **named** (for DNS logs)
  6. In the **Target server** field, enter the IP address and port of the Bindplane agent host in the format `<ip-address>:<port>`. 
     * Example: `192.168.1.100:514`
     * If using a non-standard port on Linux, specify the port accordingly (for example, `192.168.1.100:1514`)
  7. Click **OK** to save the configuration.

**Note:** The configuration page will refresh and display the newly added syslog forwarding rule. SOLIDserver will immediately begin forwarding DNS logs to the specified target server.



### Verify log forwarding

  1. Check the Bindplane agent logs to confirm logs are being received: 
     * **Linux** : `sudo journalctl -u observiq-otel-collector -f`
     * **Windows** : `type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"`
  2. Look for log entries containing DNS query and answer events from SOLIDserver.
  3. Sign in to the Google SecOps console and verify that EfficientIP DDI logs appear in the **Events** page.



### Supported log types

This integration collects the following log types from EfficientIP SOLIDserver:

  * **DNS query logs** : Client DNS queries with query type, domain name, and client IP
  * **DNS answer logs** : DNS responses with answer records, TTL, and response codes
  * **DHCP logs** : DHCP operations including DISCOVER, OFFER, REQUEST, ACK, NAK, RELEASE, and INFORM
  * **DNS Guardian logs** : Security events including suspicious behavior detection, arming/disarming triggers
  * **DNS zone transfer logs** : Zone transfer operations and notifications
  * **DNS error logs** : Format errors, SERVFAIL, REFUSED, and other DNS errors



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
ip_version | additional.fields | Merged as label with key "ip_version" if not empty  
message_size | additional.fields | Merged as label with key "message_size" if not empty  
domain_name | additional.fields | Merged as label with key "domain_name" if not empty  
N/A | intermediary | Merged from intermediary object  
description | metadata.description | Value copied directly if not empty  
msg2 | metadata.description | Set to msg2 if event_type is GENERIC_EVENT and description is empty  
su_cmd | metadata.event_type | Set to "PROCESS_OPEN" if su_cmd is "sudo"  
activity_type | metadata.event_type | Set to "NETWORK_DNS" if activity_type matches dns and has_dns_questions is true  
message | metadata.event_type | Set to "NETWORK_DHCP" if message matches dhcp  
inner_message | metadata.event_type | Set to "NETWORK_UNCATEGORIZED" if inner_message matches specific patterns and has_principal and has_target are true  
process | metadata.event_type | Set to "NETWORK_DNS" if process is "named" and has_dns_questions is true; set to "STATUS_UPDATE" if process is "named" and has_principal is true; set to "GENERIC_EVENT" if process is "named"; set to "NETWORK_DHCP" if process is "dhcpd"  
PWD | metadata.event_type | Set to "PROCESS_OPEN" if PWD not empty and has_target or has_principal is true  
activity_type | metadata.product_event_type | Value copied directly  
N/A | metadata.vendor_name | Set to "EFFICIENTIP_DDI"  
N/A | metadata.product_name | Set to "EFFICIENTIP_DDI DHCP"  
activity_type | network.application_protocol | Set to "DNS" if activity_type matches dns and has_dns_questions is true  
message | network.application_protocol | Set to "DHCP" if message matches dhcp  
process | network.application_protocol | Set to "DNS" if process is "named"; set to "DHCP" if process is "dhcpd"  
src_mac | network.dhcp.chaddr | Value copied directly if process is "dhcpd"  
src_ip | network.dhcp.ciaddr | Value copied directly if dhcp_info is "REQUEST"  
giaddr | network.dhcp.giaddr | Value copied directly  
dhcp_info | network.dhcp.opcode | Set to "BOOTREQUEST" if dhcp_info is "INFORM", "DISCOVER", or "REQUEST"; set to "BOOTREPLY" if dhcp_info is "OFFER" or "ACK"  
siaddr | network.dhcp.siaddr | Value copied directly  
transaction_id | network.dhcp.transaction_id | Value converted to uinteger if not empty or "0"  
dhcp_info | network.dhcp.type | Set to "INFORM" if dhcp_info is "INFORM"; set to "DISCOVER" if "DISCOVER"; set to "OFFER" if "OFFER"; set to "REQUEST" if "REQUEST"; set to "ACK" if "PACK"  
yiaddr | network.dhcp.yiaddr | Value copied directly  
src_ip | network.dhcp.yiaddr | Set to src_ip if process is "dhcpd" and yiaddr is empty  
answer_rrs | network.dns.answers | Merged from answer object for each rd in answer_rrs  
N/A | network.dns.questions | Merged from questions object if has_dns_questions is true  
rcode | network.dns.response_code | Value converted to uinteger  
response_code | network.dns.response_code | Value mapped to numeric code and converted to uinteger  
transport | network.ip_protocol | Value uppercased if matches udp or tcp  
observer | observer.ip | Value converted to ipaddress  
su_cmd | principal.application | Value copied directly if su_cmd is "sudo"  
process | principal.application | Set to process if process is "named" or "dhcpd"  
host | principal.asset.hostname | Value copied directly if not empty  
hostname | principal.asset.hostname | Value copied directly if not empty and host is empty  
src_ip | principal.asset.ip | Value copied directly  
asset_id | principal.asset_id | Concatenated as "ID:" + asset_id  
host | principal.hostname | Value copied directly if not empty  
hostname | principal.hostname | Value copied directly if not empty and host is empty  
domain_name | principal.hostname | Value copied directly if description contains hostname and host/hostname are empty  
src_ip | principal.ip | Value copied directly if converted to ipaddress succeeds; extracted from description if src_ip is empty  
src_mac | principal.mac | Value copied directly  
src_port | principal.port | Value converted to integer  
process_id | principal.process.pid | Value copied directly  
source_user | principal.user.userid | Value copied directly  
N/A | security_result | Merged from sec_result  
dst_ip | target.asset.ip | Value copied directly  
file_path | target.file.full_path | Value copied directly  
dst_ip | target.hostname | Value copied directly if not a valid ipaddress  
host | target.hostname | Value copied directly if inner_message matches specific patterns  
dst_ip | target.ip | Value copied directly  
dst_port | target.port | Value converted to integer  
target_cmd_line | target.process.command_line | Value copied directly  
target_user | target.user.userid | Value copied directly  
`RR_msg` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`client_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`key_office` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rrset_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`updating_zone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`view_office` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/efficientip-ddi-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
