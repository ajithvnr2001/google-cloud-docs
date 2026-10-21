---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/varonis/
title: Collect Varonis logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:27:12.030331+00:00
---

# Collect Varonis logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/varonis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Varonis logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Varonis logs to Google Security Operations using the Bindplane agent.

Varonis is a data security and analytics platform that generates CEF and LEEF-formatted syslog messages for file access events, permission changes, authentication activity, and DatAlert security alerts. The parser extracts fields from CEF, LEEF, and key-value formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Varonis server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Varonis



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
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/varonis:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: VARONIS
                raw_log_field: body
        
        service:
            pipelines:
                logs/varonis_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/varonis
        




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
             




## Configure syslog export in Varonis

  1. Sign in to the **Varonis** web UI.
  2. Go to **Tools > DatAlert > Select DatAlert**.
  3. Select **Configuration**.
  4. Provide the following configuration details: 
     * **Syslog Message IP Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (for example, `514` for **UDP**).
     * **Facility name** : Select a facility.
  5. Click **Apply**.



## Configure syslog format in Varonis

  1. Go to **Tools > DatAlert > Alert Templates**.
  2. Click **Edit Alert Template** and select **External system default template**.
  3. In **Apply to alert methods** , select **Syslog message** from the list.
  4. Select **Rules > Alert Method** from the menu.
  5. Select **Syslog message**.
  6. Click **OK**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`act` | `security_result.summary` | Value from the `act` field in the CEF message.  
`cn1` | `security_result.rule_id` | Value from the `cn1` field in the CEF message.  
`cs1` | `network.email.to` | Value from the `cs1` field in the CEF message, specifically the email recipient.  
`cs2` | `security_result.rule_name` | Value from the `cs2` field in the CEF message.  
`device_version` | `metadata.product_version` | Value from the `device_version` field in the CEF message.  
`dhost` | `principal.hostname` | Value from the `dhost` field in the CEF message, representing the principal hostname. If `file_server` is present and not "DirectoryServices", it overwrites this value.  
`duser` | `target.user.userid` | Value from the `duser` field in the CEF message. Undergoes gsub transformation to remove backslashes and split into `target.user.userid` and `target.administrative_domain`.  
`dvchost` | `target.hostname` | Value from the `dvchost` field in the CEF message.  
`filePath` | `target.file.full_path` | Value from the `filePath` field in the CEF message.  
`rt` | `metadata.event_timestamp` | Value from the `rt` field in the CEF message, parsed as a timestamp.  
`severity` | `security_result.severity` | Value from the `severity` field in the CEF message or LEEF message. Converted to uppercase. Mapped to UDM severity values (LOW, INFORMATIONAL, MEDIUM, HIGH, CRITICAL) based on numeric value or keyword.  
`Acting Object` | `target.user.user_display_name` | Value from the `Acting Object` field in the key-value data. Split by "\" to extract the display name.  
`Acting Object SAM Account Name` | `target.user.userid` | Value from the `Acting Object SAM Account Name` field in the key-value data.  
`Device hostname` | `target.hostname` | Value from the `Device hostname` field in the key-value data.  
`Device IP address` | `target.ip` | Value from the `Device IP address` field in the key-value data.  
`Event Time` | `metadata.event_timestamp` | Value from the `Event Time` field in the key-value data, parsed as a timestamp.  
`Event Type` | `target.application`, `metadata.event_type` | Value from the `Event Type` field in the key-value data. Used to derive `metadata.event_type` (FILE_OPEN, USER_CHANGE_PERMISSIONS, USER_CHANGE_PASSWORD, USER_UNCATEGORIZED).  
`File Server/Domain` | `principal.hostname` | Value from the `File Server/Domain` field in the key-value data. If not "DirectoryServices", it overwrites the `principal.hostname` derived from `dhost`.  
`Path` | `target.file.full_path` | Value from the `Path` field in the key-value data.  
`Rule Description` | `metadata.description` | Value from the `Rule Description` field in the key-value data.  
`Rule ID` | `security_result.rule_id` | Value from the `Rule ID` field in the key-value data.  
`Rule Name` | `security_result.rule_name` | Value from the `Rule Name` field in the key-value data.  
`intermediary_host` | `intermediary.hostname` | Value extracted by grok, representing the intermediary hostname.  
`log_type` | `metadata.log_type` | Hardcoded to `VARONIS`.  
`metadata.event_type` | `metadata.event_type` | Derived based on the values of `evt_typ`, `act`, and `filepath`. Defaults to STATUS_UPDATE if `event_type` is GENERIC_EVENT and `principal_hostname` is present.  
`metadata.product_name` | `metadata.product_name` | Hardcoded to `VARONIS`, but can be overwritten by the `product_name` field from the LEEF message.  
`metadata.vendor_name` | `metadata.vendor_name` | Hardcoded to `VARONIS`, but can be overwritten by the `vendor` field from the LEEF message.  
`prin_host` | `principal.hostname` | Value extracted by grok, representing the principal hostname.  
`product_name` | `metadata.product_name` | Value from the LEEF message.  
`security_result.action` | `security_result.action` | Derived from the `result` or `Event Status` field. Set to "ALLOW" if the result is `Success`, otherwise set to `BLOCK`.  
`timestamp` | `timestamp`, `metadata.event_timestamp` | The event timestamp is derived from various fields (`datetime1`, `event_time`, `start_datetime`, `datetime2`) based on availability. The `create_time` from the raw log is used as a fallback and mapped to both `timestamp` and `metadata.event_timestamp` if no other timestamp fields are available.  
`vendor` | `metadata.vendor_name` | Value from the LEEF message.  
`fname` | `event.idm.read_only_udm.target.file.names` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`cs7` | `event.idm.read_only_udm.security_result.url_back_to_product` | Mapped from changelog  
`usrName` | `principal.user.userid` | Mapped from changelog  
`Event_Type` | `metadata.product_event_type` | Mapped from changelog  
`domain` | `prinicipal.administrative_domain` | Mapped from changelog  
`proto", "cat", "Event_Additional_Data", "Event_Status", "Email_Attachment_Name", "Email_Date", "Account_of_Changed_Permissions", "Permissions_Changes", "Permissions_before_Change", and "Permissions_after_Change` | `additional.fields` | Mapped from changelog  
`Affected_Object_Path` | `taregt.file.full_path` | Mapped from changelog  
`Affected_Object` | `security_result.detection_fields` | Mapped from changelog  
`src` | `principal.ip` | Mapped from changelog  
`Alert_ID` | `security_result.rule_id` | Mapped from changelog  
`Email_Recipients` | `network.email.to` | Mapped from changelog  
`Email_Item", "Mailbox_Access_by_Owner", "Threshold_Value", "Threshold_First_Timestamp", "Event_by_MailboxOwner", and "Email_Sender` | `additional.fields` | Mapped from changelog  
`Email_Sender` | `network.email.from` | Mapped from changelog  
`accountName` | `target.user.userid` | Mapped from changelog  
`Device_Name` | `taregt.hostname` | Mapped from changelog  
`Event_Type_ID` | `metadata.product_log_id` | Mapped from changelog  
`Event_File_Server_Domain` | `target.administrative_domain` | Mapped from changelog  
`Alert_Page_URL` | `taregt.url` | Mapped from changelog  
`devTime` | `metadata.event_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/varonis-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
