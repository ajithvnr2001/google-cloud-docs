---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/automation-anywhere/
title: Collect Automation Anywhere logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:41:17.141553+00:00
---

# Collect Automation Anywhere logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/automation-anywhere/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Automation Anywhere logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Automation Anywhere logs to Google Security Operations using the Bindplane agent.

Automation Anywhere is a robotic process automation platform that generates audit logs for user activities, bot deployments, configuration changes, and system events through its Control Room.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Automation Anywhere Control Room
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Automation Anywhere



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**
  4. Save the file securely on the system where the Bindplane agent will be installed.

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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/automation_anywhere:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: AUTOMATION_ANYWHERE
                raw_log_field: body
        
        service:
            pipelines:
                logs/automation_anywhere_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/automation_anywhere
        




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
             




## Configure syslog on Automation Anywhere

  1. Sign in to the **Automation Anywhere Control Room** web UI.
  2. Go to **Administration > Settings > Network settings**.
  3. Click **+** (plus).
  4. Provide the syslog configuration details: 
     * **Syslog server** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane port number (for example, `514` for UDP).
     * **Protocol** : Select **UDP**.
     * (Optional) **Use Secure Connection** : This configuration is available only for **TCP** communication.
  5. Click **Save changes**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
ACTIVITY AT | metadata.event_timestamp | The timestamp of the event is taken from the `ACTIVITY AT` field in the raw log.  
ACTION TAKEN BY | target.user.userid | The user who performed the action is taken from the `ACTION TAKEN BY` field in the raw log.  
ACTION TYPE | security_result.summary | A summary of the action taken is taken from the `ACTION TYPE` field in the raw log.  
ITEM NAME | target.file.full_path | The name of the file or item involved in the event is taken from the `ITEM NAME` field in the raw log.  
REQUEST ID | target.user.product_object_id | A unique identifier for the request is taken from the `REQUEST ID` field in the raw log.  
SOURCE | metadata.product_event_type | The source of the event is taken from the `SOURCE` field in the raw log.  
SOURCE DEVICE | target.hostname | target.ip | If the `SOURCE DEVICE` field contains a valid IP address, it is mapped to target.ip. Otherwise, it is mapped to target.hostname.  
STATUS | security_result.action | The security action (ALLOW, BLOCK, UNKNOWN_ACTION) is determined based on the `STATUS` field in the raw log: `Successful` maps to ALLOW, `Unsuccessful` maps to BLOCK, `Unknown` maps to UNKNOWN_ACTION.  
- | metadata.event_type | The event type is determined based on the `ACTION TYPE` field in the raw log using a series of regular expression matches. If no match is found, it defaults to `GENERIC_EVENT`.  
- | metadata.log_type | Set to `AUTOMATION_ANYWHERE`.  
- | metadata.product_name | Set to `AUTOMATION_ANYWHERE`.  
- | metadata.vendor_name | Set to `AUTOMATION_ANYWHERE`.  
- | extensions.auth | An empty object is added for USER_LOGIN events.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/automation-anywhere-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
