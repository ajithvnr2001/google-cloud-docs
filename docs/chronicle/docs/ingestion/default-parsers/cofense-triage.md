---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cofense-triage/
title: Collect Cofense logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:22.126865+00:00
---

# Collect Cofense logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cofense-triage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cofense logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cofense logs into Google Security Operations using the Bindplane agent.

Cofense Triage is a phishing incident response platform that automates the detection, analysis, and response to phishing emails reported by employees. It clusters similar threats, assigns risk scores, extracts indicators of compromise (IOCs), and integrates with security orchestration tools to accelerate phishing incident resolution.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cofense Triage server
  * If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
  * Privileged access to the Cofense Triage administration console
  * Cofense Triage version 1.20 or later



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

## Get the Google SecOps customer ID

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

## Configure Bindplane agent to ingest syslog and send logs to Google SecOps

### Locate the configuration file

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/cofense:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
             customer_id: 'your-customer-id'
             endpoint: chronicle.googleapis.com
             log_type: COFENSE_TRIAGE
             raw_log_field: body
         
         service:
           pipelines:
             logs/cofense_to_chronicle:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/cofense
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * `listen_address`: IP address and port to listen on:

         * `0.0.0.0:514` to listen on all interfaces on port 514 (requires root on Linux)
         * `0.0.0.0:1514` to listen on an unprivileged port (recommended for Linux non-root)
       * Receiver type options:

         * `tcplog` for TCP syslog (recommended for Cofense Triage)
         * `udplog` for UDP syslog
     * Exporter configuration:

       * `creds_file_path`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `customer_id`: Google SecOps customer ID

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cofense:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: COFENSE_TRIAGE
            raw_log_field: body
        


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
           

    3. Check the logs for errors:
           
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
           

    3. Check the logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




## Configure Cofense Triage syslog forwarding

Cofense Triage can forward phishing report events and alerts in CEF (Common Event Format) via syslog to external SIEM collectors.

### Enable syslog output in Cofense Triage

  1. Sign in to the **Cofense Triage** web interface with administrator credentials.
  2. Go to **Administration > System > Syslog**.
  3. Enable the **Syslog** toggle.
  4. Configure the following syslog parameters: 
     * **Syslog Server** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter the port matching the Bindplane agent `listen_address` (for example, `514`).
     * **Protocol** : Select **TCP** (recommended) or **UDP** to match the Bindplane agent receiver type.
     * **Format** : Select **CEF** (Common Event Format).
  5. Click **Save**.



### Configure syslog alerts

  1. In the Cofense Triage web interface, go to **Administration > System > Syslog Alerts**.
  2. Select the event types to forward: 
     * **Phishing reports** : Forwarded when new phishing reports are received and processed
     * **Cluster events** : Forwarded when reports are clustered
     * **Threat indicator events** : Forwarded when IOCs are extracted from reports
     * **Health alerts** : Forwarded for system health and performance events
  3. Click **Save**.

**Note:** Syslog alert categories and granularity depend on the Cofense Triage version and license level. Refer to the Cofense Triage documentation for your specific version.



### Verify syslog forwarding

  1. After saving the syslog configuration, trigger a test event in Cofense Triage (for example, process a phishing report).
  2. Check the Bindplane agent logs for incoming syslog messages: 
     * **Linux** : `sudo journalctl -u observiq-otel-collector -f`
     * **Windows** : `type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"`
  3. Verify that CEF-formatted messages appear in the logs, for example:
         
         CEF:0|Cofense|Triage|1.0|100|Phishing Report Processed|5|suser=reporter@company.com duser=attacker@malicious.com cs4=Urgent: Account Verification cat=Processed:Threats
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
msg, rule_id, start, rt | additional.fields | Merged with labels for msg if not empty, rule_id if not empty, start if not empty, rt if not empty  
event_data, descrip | metadata.description | Value from event_data if not empty, else descrip  
deviceCustomDate1, log_datetime | metadata.event_timestamp | Parsed from deviceCustomDate1 if not empty, else log_datetime using format MMM d yyyy HH:mm:ss or MMM d HH:mm:ss  
suser, duser, has_principal | metadata.event_type | Set to EMAIL_TRANSACTION if suser and duser match email pattern, else GENERIC_EVENT, then STATUS_UPDATE if has_principal true and was GENERIC_EVENT  
cs3 | metadata.product_log_id | Extracted from cs3 using grok pattern /%{INT:productlogid}  
| metadata.product_name | Set to "Triage"  
cs3 | metadata.url_back_to_product | Value copied directly  
| metadata.vendor_name | Set to "Cofense"  
suser | network.email.from | Value copied directly  
cs4 | network.email.subject | Value copied directly  
duser | network.email.to | Value copied directly  
host | principal.asset.hostname | Value copied directly  
ipaddress | principal.asset.ip | Value copied directly  
host | principal.hostname | Value copied directly  
ipaddress | principal.ip | Value copied directly  
processID | principal.process.pid | Value copied directly  
descrip | principal.user.userid | Extracted from descrip using grok pattern User: (%{WORD:user_id})  
cat, cs2 | security_result.action | Set to ALLOW if cat in ["health","Processed:Marketing","Processed:Non-Malicious"], BLOCK if cat == "Processed:Spam" or "Processed:Threats" or cs2 in ["PM_Intel_CoronaVirus_Keywords","PM_Intel_CredPhish_106159","VU_Potential_Credential_Stealer"]  
severity | security_result.alert_state | Set to ALERTING if severity in ["8","10","11","12","13","14"], else NOT_ALERTING  
cat, cs2, severity | security_result.category | Set to MAIL_SPAM if cat == "Processed:Spam", MAIL_PHISHING if cs2 in ["PM_Intel_CoronaVirus_Keywords","PM_Intel_CredPhish_106159","VU_Potential_Credential_Stealer"] or severity in ["8","10","11","12","13","14"]  
cat | security_result.description | Value copied directly  
severity | security_result.rule_id | Value copied directly  
cs2 | security_result.rule_name | Value copied directly  
cat, cs2 | security_result.severity | Set to INFORMATIONAL if cat in ["health","Processed:Marketing","Processed:Non-Malicious"], HIGH if cat == "Processed:Spam", CRITICAL if cat == "Processed:Threats", else HIGH if cs2 in ["PM_Intel_CoronaVirus_Keywords","PM_Intel_CredPhish_106159","VU_Potential_Credential_Stealer"]  
`msg", "rule_id", "start", and "rt` | `additional.fields` | Mapped from changelog  
`ProcessID` | `principal.process.pid` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cofense-triage-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
