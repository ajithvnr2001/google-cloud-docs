---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/archer-irm/
title: Collect Archer IRM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:20:03.637391+00:00
---

# Collect Archer IRM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/archer-irm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Archer IRM logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Archer IRM logs to Google Security Operations using Bindplane agent.

Archer Integrated Risk Management (IRM) is a governance, risk, and compliance (GRC) platform that provides audit logging for user activities, security events, login/logout actions, and database operations. It supports syslog forwarding of CEF-formatted audit logs over TCP.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Archer application server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Archer Control Panel



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:6514"
        
        exporters:
          chronicle/archer_irm:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: ARCHER_IRM
            raw_log_field: body
        
        service:
          pipelines:
            logs/archer_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/archer_irm
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `6514` is the recommended port for Archer IRM TCP syslog
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/archer_irm:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ARCHER_IRM
            raw_log_field: body
        


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
             




## Configure syslog for Archer IRM audit logging

  1. Open the **Archer Control Panel** on the application server.
  2. Go to **Instance Management > All Instances** and double-click the target instance.
  3. On the **General** tab, find the **Audit** section and select the **Enable Audit Logging for this instance** checkbox.
  4. Provide the following configuration details: 
     * **HostName or IP Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (for example, **6514**).
     * **IP Version** : Select **IPv4**.
     * **IP Traffic Method** : Select **TCP**.
  5. Click **Test Connection** (only available when TCP is selected) to verify connectivity.
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`ArcherInstance` | `additional.fields.ArcherInstance.string_value` | Extracted from the `ArcherInstance` field in the raw log message.  
`ArcherLog` |  | This field is parsed and its data is mapped to other UDM fields.  
`ArcherVersion` | `additional.fields.ArcherVersion.string_value` | Extracted from the `ArcherVersion` field in the raw log message.  
`InputParameter` | `additional.fields.InputParameter.string_value` | Extracted from the `InputParameter` field in the raw log message.  
`LogSourceIdentifier` |  | This field is parsed and its data is mapped to other UDM fields.  
`MethodName` | `additional.fields.MethodName.string_value` | Extracted from the `MethodName` field in the raw log message.  
`OutputValues` | `additional.fields.OutputValue.string_value` | Extracted from the `OutputValues` field in the raw log message.  
`Success` | `security_result.summary` | The value is set to `Success:` concatenated with the value of the `Success` field in the raw log message.  
`UserId` | `principal.user.userid` | Extracted from the `UserId` field in the raw log message.  
`UserName` | `principal.user.user_display_name` | Extracted from the `UserName` field in the raw log message.  
`DB_DRIVER` | `target.resource.attribute.labels.db_driver.value` | Extracted from the `DB_DRIVER` field in the raw log message.  
`DB_HOST` | `target.resource.attribute.labels.db_host.value` | Extracted from the `DB_HOST` field in the raw log message.  
`DB_NAME` | `target.resource.attribute.labels.db_name.value` | Extracted from the `DB_NAME` field in the raw log message.  
`DB_PORT` | `target.resource.attribute.labels.db_port.value` | Extracted from the `DB_PORT` field in the raw log message.  
`DB_URL` | `target.resource.attribute.labels.db_url.value` | Extracted from the `DB_URL` field in the raw log message.  
`company_security_event_id` | `metadata.product_log_id` | Extracted from the `company_security_event_id` field in the raw log message.  
`create_date` | `metadata.event_timestamp` | Converted to timestamp from UNIX_MS format.  
`databasename` | `target.resource.attribute.labels.db_name.value` | Extracted from the `databasename` field in the raw log message if `DB_NAME` is not present.  
`encrypt` | `security_result.detection_fields.encrypt.value` | Extracted from the `encrypt` field in the raw log message.  
`eventid` | `metadata.product_event_type` | Extracted from the `eventid` field in the raw log message.  
`eventtime` | `metadata.event_timestamp` | Converted to timestamp from various formats.  
`integratedSecurity` | `security_result.detection_fields.integratedSecurity.value` | Extracted from the `integratedSecurity` field in the raw log message.  
N/A | `extensions.auth.type` | Set to `AUTHTYPE_UNSPECIFIED` for USER_LOGIN and USER_LOGOUT events.  
N/A | `metadata.event_type` | Set to `USER_RESOURCE_ACCESS` if the log is parsed by the grok pattern. Set to `USER_LOGIN` if `security_event_name` is `User Login`. Set to `USER_LOGOUT` if `security_event_name` is `User Logout`. Set to `USER_RESOURCE_ACCESS` if `security_event_name` contains `Security Events`. Otherwise set to `GENERIC_EVENT`.  
N/A | `metadata.log_type` | Set to `ARCHER_IRM`.  
N/A | `metadata.product_name` | Set to `Archer` if the log is parsed by the grok pattern. Otherwise set to `RSA`.  
N/A | `metadata.vendor_name` | Set to `RSA` if the log is parsed by the grok pattern. Otherwise set to `Archer`.  
N/A | `principal.ip` | Set to `1.2.3.4` if the log is parsed by the grok pattern.  
N/A | `principal.port` | Set to the value extracted from `LogSourceIdentifier` if the log is parsed by the grok pattern.  
N/A | `security_result.action` | Set to `ALLOW` if `Success` is `True`, otherwise set to `BLOCK`.  
N/A | `target.resource.resource_type` | Set to `DATABASE` if any database-related fields are present.  
`source_user` | `principal.user.userid` | Extracted from the `source_user` field in the raw log message.  
`target_user` | `target.user.userid` | Extracted from the `target_user` field in the raw log message.  
`trustServerCertificate` | `security_result.detection_fields.trustServerCertificate.value` | Extracted from the `trustServerCertificate` field in the raw log message.  
`version` | `metadata.product_version` | Extracted from the `version` field in the raw log message.  
`file_name` | `target.file.full_path` | Mapped from changelog  
`Downloaded_By` | `principal.user.user_display_name` | Mapped from changelog  
`Downloaded_By_UserName` | `principal.user.email_addresses` | Mapped from changelog  
`security_event_name` | `security_result.description` | Mapped from changelog  
`target_group` | `target.group.group_display_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/archer-irm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
