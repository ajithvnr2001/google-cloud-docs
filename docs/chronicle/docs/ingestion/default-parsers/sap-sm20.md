---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-sm20/
title: Collect SAP SM20 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:16:52.710106+00:00
---

# Collect SAP SM20 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-sm20/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SAP SM20 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SAP SM20 logs to Google Security Operations using the Bindplane agent.

SAP SM20 is the SAP Security Audit Log that captures user authentication, authorization changes, and transaction activities within SAP systems. The Bindplane agent collects exported SAP SM20 log files directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the SAP application server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the SAP system with administrator permissions (SAP_ALL or equivalent authorization)



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

## Configure the Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - /usr/sap/<SID>/DVEBMGS00/log/audit_*
                start_at: beginning
        
        exporters:
            chronicle/sap_sm20:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: SAP_SM20
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/sap_sm20_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/sap_sm20
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Default SAP Security Audit Log locations: 
      * **Linux** : `/usr/sap/<SID>/DVEBMGS00/log/audit_*`
      * **Windows** : `C:\usr\sap\<SID>\DVEBMGS00\log\audit_*`
      * Replace `<SID>` with your SAP System ID (for example, `PRD`, `QAS`, `DEV`)
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `sap_sm20`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list
    * `SAP_SM20`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `sap_sm20_to_chronicle`: Descriptive name for the pipeline



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
             




## Configure SAP SM20 Security Audit Log

  1. Sign in to the **SAP** system using SAP GUI with an administrator account.
  2. Run transaction **SM19** (Security Audit Configuration).
  3. Activate the Security Audit Log by selecting **Security audit > Activate**.
  4. Configure the audit filters: 
     1. Click **Create** to add a new filter.
     2. Select the audit classes to capture: 
        * **Dialog login** : Logon and logoff events
        * **RFC/CPIC login** : Remote function call authentication events
        * **Transaction start** : Transaction execution events
        * **Report start** : Report execution events
        * **Change user master record** : User administration changes
     3. Set the **Client** (for example, `000`, `100`, or `*` for all clients).
     4. Set the **User** to `*` to capture events for all users.
     5. Select the **Audit severity** levels: **Critical** , **Severe** , and **Important**.
  5. Click **Save** to activate the filter.
  6. Verify the audit log file location by running transaction **SM21** or checking the profile parameter `rsau/local/file`. Default log file locations: 
     * **Linux** : `/usr/sap/<SID>/DVEBMGS00/log/audit_<date>`
     * **Windows** : `C:\usr\sap\<SID>\DVEBMGS00\log\audit_<date>`
  7. Ensure the Bindplane agent `include` path in `config.yaml` matches the audit log file location with a wildcard pattern.

**Note:** The SAP Security Audit Log generates files with date-based naming (for example, `audit_20260311`). Use a wildcard pattern such as `audit_*` in the Bindplane agent configuration to capture all log files. The Bindplane agent service account must have read access to the SAP log directory.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
WP_TYP, ALGREPNA, ALGAREA, ALGFILENO, ALGFILEPOS, ALGINST, ALGSUBID, UTCDIFF, ALGTASKNO, ALGTASKTYPE, ALGTCODE, log_event.log_event.ALGAREA, log_event.fields.EVENT_SUBTYPE, log_event.log_event.ALGFILENO, log_event.log_event.ALGFILEPOS, log_event.log_event.ALGREPNA, log_event.log_event.ALGSUBID, log_event.log_event.ALGSYSTEM, log_event.log_event.UTCDIFF, log_event.log_event.UTCSIGN, log_event.log_event.ALGTASKNO, log_event.log_event.ALGTASKTYPE, log_event.log_event.ALGTCODE, log_event.log_event.WP_TYP | additional.fields | Merged with label objects for each non-empty field  
| extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED" if event_type is USER_LOGIN  
WP_SERVER, log_event.log_event.WP_SERVER | intermediary.hostname | Value from WP_SERVER if not empty, overwritten by log_event.log_event.WP_SERVER if not empty  
ALGTEXT, log_event.log_event.ALGTEXT | metadata.description | Value from ALGTEXT if not empty, overwritten by log_event.log_event.ALGTEXT if not empty  
| metadata.event_type | Set to USER_LOGIN if ALGTEXT or log_event.log_event.ALGTEXT contains "logon successful" and has_principal and has_target, else PROCESS_LAUNCH if has_principal and has_target_process, else STATUS_UPDATE if has_principal, else GENERIC_EVENT; in 0035 branch, STATUS_UPDATE if has_principal, else GENERIC_EVENT  
log_event.fields.EVENT_TYPE | metadata.product_event_type | Value copied directly  
session_id | network.session_id | Value copied directly  
INSTANCE_NAME, ALGSYSTEM, log_event.host, log_event.log_event.INSTANCE_NAME, log_event.log_event.ALGSYSTEM | principal.asset.hostname | Value from INSTANCE_NAME if not empty, overwritten by ALGSYSTEM if not empty, then by log_event.host if not empty, then by log_event.log_event.INSTANCE_NAME if not empty, then by log_event.log_event.ALGSYSTEM if not empty  
ip | principal.asset.ip | Value copied directly  
INSTANCE_NAME, ALGSYSTEM, log_event.host, log_event.log_event.INSTANCE_NAME, log_event.log_event.ALGSYSTEM | principal.hostname | Value from INSTANCE_NAME if not empty, overwritten by ALGSYSTEM if not empty, then by log_event.host if not empty, then by log_event.log_event.INSTANCE_NAME if not empty, then by log_event.log_event.ALGSYSTEM if not empty  
ip | principal.ip | Value copied directly  
log_event.source, log_event.sourcetype | principal.labels | Merged with label objects for log_event.source and log_event.sourcetype if not empty  
TXSUBCLSID, log_event.log_event.TXSUBCLSID | security_result.description | Value from TXSUBCLSID if not empty, overwritten by log_event.log_event.TXSUBCLSID if not empty  
TXSEVERITY, log_event.log_event.TXSEVERITY | security_result.severity | Set to "CRITICAL" if TXSEVERITY matches (?i)Severe|critical, overwritten if log_event.log_event.TXSEVERITY matches (?i)Severe|critical  
WP_STATUS, log_event.log_event.WP_STATUS | security_result.summary | Value from WP_STATUS if not empty, overwritten by log_event.log_event.WP_STATUS if not empty  
application | target.application | Value copied directly  
ALGLTERM, log_event.log_event.INSTANCE_NAME, log_event.log_event.ALGLTERM | target.asset.hostname | Set to ALGLTERM if ALGLTERM is not an IP, overwritten by log_event.log_event.INSTANCE_NAME if not empty, overwritten by log_event.log_event.ALGLTERM if log_event.log_event.ALGLTERM is not an IP  
ALGLTERM, log_event.log_event.IPADDRESS, log_event.log_event.ALGLTERM | target.asset.ip | Set to IP extracted from ALGLTERM if ALGLTERM is IP, overwritten by IP from log_event.log_event.IPADDRESS if it's IP, overwritten by IP from log_event.log_event.ALGLTERM if it's IP  
ALGLTERM, log_event.log_event.INSTANCE_NAME, log_event.log_event.ALGLTERM | target.hostname | Set to ALGLTERM if ALGLTERM is not an IP, overwritten by log_event.log_event.INSTANCE_NAME if not empty, overwritten by log_event.log_event.ALGLTERM if log_event.log_event.ALGLTERM is not an IP  
ALGLTERM, log_event.log_event.IPADDRESS, log_event.log_event.ALGLTERM | target.ip | Set to IP extracted from ALGLTERM if ALGLTERM is IP, overwritten by IP from log_event.log_event.IPADDRESS if it's IP, overwritten by IP from log_event.log_event.ALGLTERM if it's IP  
log_event.log_event.ALGCLIENT, log_event.log_event.ALGINST | target.labels | Merged with label objects for log_event.log_event.ALGCLIENT and log_event.log_event.ALGINST if not empty  
WP_PID, log_event.log_event.WP_PID | target.process.pid | Value from WP_PID if not empty, overwritten by log_event.log_event.WP_PID if not empty  
ALGCLIENT, ALGINST | target.resource.attribute.labels | Merged with label objects for ALGCLIENT and ALGINST if not empty  
resource_id | target.resource.product_object_id | Value copied directly  
ALGUSER, log_event.log_event.ALGUSER | target.user.userid | Value from ALGUSER if not empty, overwritten by log_event.log_event.ALGUSER if not empty  
| metadata.product_name | Set to "SAP_SM20"  
| metadata.vendor_name | Set to "SAP_SM20"  
`session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`application` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`resource_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`date` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`ALGCLIENT" and "ALGINST` | `target.resource.attribute.labels` | Mapped from changelog  
`WP_TYP", "ALGREPNA", "ALGAREA", "ALGFILENO", "ALGFILEPOS", "ALGSUBID", "UTCDIFF", "ALGTASKNO", "ALGTASKTYPE", "ALGTCODE` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-sm20-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
