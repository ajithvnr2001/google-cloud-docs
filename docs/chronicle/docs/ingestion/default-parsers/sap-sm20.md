---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-sm20/
title: Collect SAP SM20 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:41.379582+00:00
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
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
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
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `SAP_SM20`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `sap_sm20_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/sap_sm20:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SAP_SM20
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
