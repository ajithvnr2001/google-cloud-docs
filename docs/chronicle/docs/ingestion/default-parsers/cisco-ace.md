---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ace/
title: Collect Cisco Application Control Engine (ACE) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:06:13.053864+00:00
---

# Collect Cisco Application Control Engine (ACE) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Application Control Engine (ACE) logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Application Control Engine (ACE) logs to Google Security Operations using Bindplane. The parser extracts security-relevant information from the SYSLOG messages. It uses regular expressions to identify specific event types, extracts key data points like source or destination IP addresses and ports, and structures them into a Unified Data Model (UDM) for consistent analysis.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Windows 2016 or later or a Linux host with `systemd`
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to Cisco Application Control Engine



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**. Save the file securely on the system where Bindplane will be installed.



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

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
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
                 customer_id: <customer_id>
                 endpoint: malachiteingestion-pa.googleapis.com
                 # Add optional ingestion labels for better organization
                 log_type: 'CISCO_ACE'
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
     * Replace `<customer_id>` with the actual customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the path where the authentication file was saved in the [Get Google SecOps ingestion authentication file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ace#get-auth-file) section.



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure the syslog on Cisco Application Control Engine (ACE)

  1. Sign in to the Cisco ACE device.
  2. Go to the **Main Menu > Advanced Options > Syslog Configuration**.
  3. Click **Add First Server** and then click **OK**.
  4. Enter the Bindplane agent IP address and port number in the First Syslog Server field.
  5. Click **OK** ; the system will restart with new settings.
  6. Click **OK** again.
  7. Click **Return**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
action | security_result.action_details | Value taken from `action` field after lowercase operation.  
action | security_result.action | If `action` is `built`, set to `ALLOW`. If `action` is `teardown`, set to `BLOCK`.  
bytes | network.sent_bytes | Only populated for event_id `302025`.  
dst_interface | target.resource.attribute.labels.value |   
dst_ip | target.ip |   
dst_port | target.port |   
event_id | metadata.product_event_type |   
icmp_code_laddr | additional.fields.value.string_value | Key is `icmp_code_laddr`.  
icmp_code_xlated | additional.fields.value.string_value | Key is `icmp_code_xlated`.  
icmp_seq_num | additional.fields.value.string_value | Key is `icmp_seq_num`.  
protocol | network.ip_protocol |   
protocol | metadata.description | Used to populate the description for specific event types.  
src_interface | principal.resource.attribute.labels.value |   
src_ip | principal.ip |   
src_port | principal.port |   
timestamp | metadata.event_timestamp.seconds | Converted to epoch seconds.  
| metadata.log_type | Hardcoded to `CISCO_ACE`.  
| metadata.event_type | Set to `NETWORK_CONNECTION` for event IDs 302024, 302025, 302022, 302023, 302026, 302027. Set to `SCAN_UNCATEGORIZED` for event ID 400000.  
| target.resource.attribute.labels.key | Hardcoded to `Connection Interface`.  
| principal.resource.attribute.labels.key | Hardcoded to `Connection Interface`.  
`icmp_code_laddr","icmp_code_xlated","icmp_seq_num` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ace-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
