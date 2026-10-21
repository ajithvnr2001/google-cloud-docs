---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-oud/
title: Collect Oracle Unified Directory logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:54:56.042989+00:00
---

# Collect Oracle Unified Directory logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-oud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Oracle Unified Directory logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Oracle Unified Directory logs to Google Security Operations using Bindplane.

Oracle Unified Directory is an enterprise LDAP directory service for identity management. It provides a scalable, standards-based directory for storing and managing identity data, supporting authentication, authorization, and directory proxy functionality. The parser extracts fields from Oracle Unified Directory log entries and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Oracle Unified Directory server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Oracle Unified Directory server with administrator permissions



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo systemctl status observiq-otel-collector
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/oracle_oud:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ORACLE_OUD
                raw_log_field: body
        
        service:
            pipelines:
                logs/oracle_oud:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/oracle_oud
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `malachiteingestion-pa.googleapis.com`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * Adjust the `creds_file_path` depending on the platform: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



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
         




## Configure Oracle Unified Directory syslog forwarding

Oracle Unified Directory stores logs locally on the server filesystem, typically in the `OUD_INSTANCE/logs/` directory. Configure syslog forwarding using the system syslog daemon to send these logs to the Bindplane agent.

  1. Identify the Oracle Unified Directory log directory. Common log files include `access`, `errors`, `replication`, and `audit`.

  2. Configure the system syslog daemon (for example, `rsyslog`) to monitor and forward OUD log files. Create a new rsyslog configuration file:
         
         sudo nano /etc/rsyslog.d/oud-forward.conf
         

  3. Add the following content:
         
         module(load="imfile")
         input(type="imfile"
             File="/path/to/oud-instance/logs/access"
             Tag="oracle-oud"
             Severity="info"
             Facility="local0")
         input(type="imfile"
             File="/path/to/oud-instance/logs/errors"
             Tag="oracle-oud"
             Severity="error"
             Facility="local0")
         local0.* @@BINDPLANE_AGENT_IP:514
         

**Note:** Replace `/path/to/oud-instance/logs/` with the actual path to your Oracle Unified Directory log directory. Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host. Use `@@` for TCP or `@` for UDP.
  4. Restart the rsyslog service:
         
         sudo systemctl restart rsyslog
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
conn,op,msgID,oid,result,etime,filter,attrs,ou,version,type,authFailureID,authFailureReason,name,o | additional.fields | Additional metadata not covered by other UDM fields  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
operation,operation1 | metadata.product_event_type | Product-specific event type  
protocol | network.application_protocol | Application protocol used in the network connection  
hostname | principal.hostname | Hostname of the principal asset  
srcaddr | principal.ip | IP address of the principal  
srcport | principal.port | Port number used by the principal  
uid | principal.user.userid | User ID of the principal user  
operation | security_result.action_details | Details of the action taken by the security product  
reason | security_result.description | Description of the security result  
msg_data | security_result.summary | Summary of the security result  
destaddr | target.ip | IP address of the target  
destport | target.port | Port number used by the target  
| metadata.product_name | Name of the product generating the event  
| metadata.vendor_name | Name of the vendor of the product  
`authFailureID", "filter", "attrs", "changetype", "replace" and "authFailureReason` | `additional.fields` | Mapped from changelog  
`from` | `principal.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-oud-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
