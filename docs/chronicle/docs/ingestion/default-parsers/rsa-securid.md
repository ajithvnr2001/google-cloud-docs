---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rsa-securid/
title: Collect RSA SecurID Access logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:33.794599+00:00
---

# Collect RSA SecurID Access logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rsa-securid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect RSA SecurID Access logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest RSA SecurID Access logs to Google Security Operations using the Bindplane agent.

RSA SecurID Access is a multi-factor authentication and identity assurance platform for enterprise access management. It generates audit logs covering user and system activity, authentication events, and token management. The parser extracts fields from RSA SecurID log entries and maps them to the Unified Data Model (UDM), capturing user identity, authentication results, session details, and security metadata.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the RSA SecurID Access Identity Router or Authentication Manager appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the RSA SecurID Access Cloud Administration Console or Security Console with administrator permissions



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

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
          chronicle/rsa_securid:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: RSA_SECURID
            raw_log_field: body
        
        service:
          pipelines:
            logs/rsa_securid:
              receivers:
                - udplog
              exporters:
                - chronicle/rsa_securid
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * Adjust the `creds_file_path` to the path of your service account JSON key file (Option 1), depending on the platform: 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/rsa_securid:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: RSA_SECURID
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
             




## Configure RSA SecurID Access syslog forwarding

### Configure audit logging in the Cloud Administration Console

  1. Sign in to the **RSA SecurID Access Cloud Administration Console**.
  2. Go to **Platform > Audit Logging**.
  3. Click **Enabled**.
  4. Under **Output** , select **Send to syslog**.
  5. In the **Syslog Server** field, enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
  6. In the **Port** field, enter `514` (must match the Bindplane receiver port).
  7. From the **Protocol** drop-down list, select **UDP** (must match the Bindplane receiver type).
  8. Under **Event Types** , select the events to log: 
     * **User events** : Sign-in attempts, profile changes, and other user activity.
     * **Include authorization requests** : Authorization events for protected applications.
     * **System events** : Backup, firewall rule changes, and other system activity.
     * **Include system error events** : Error-level system events.
  9. Click **Save**.



### Configure logging in RSA Authentication Manager Security Console

If you are also running RSA Authentication Manager (on-premise), configure logging to send authentication and audit events to syslog:

  1. Sign in to the **RSA Authentication Manager Security Console**.
  2. Go to **Setup > System Settings > Logging**.
  3. Select an instance (for example, **Primary**) and click **Next**.
  4. Set the log levels for the following logs: 
     * **Administrative Audit Log** : Administrative actions such as user creation, token assignment, and policy changes.
     * **Runtime Audit Log** : Authentication events such as successful and failed authentication attempts.
     * **System Log** : System-level events such as service start/stop and replication status.
  5. For the **Log Data Destination** , select **Save to internal database and local operating system SysLog** for each log type.
  6. Click **Save**.



### Configure remote syslog forwarding from Authentication Manager

**For RSA Authentication Manager 8.4 or later** (uses `rsyslog`):

  1. SSH into the RSA Authentication Manager appliance.
  2. Edit the remote syslog configuration file:
         
         sudo vi /etc/rsyslog.d/remote.conf
         

  3. Add a line specifying the Bindplane agent as the remote syslog server:
         
         *.* @BINDPLANE_AGENT_IP:514
         

**Note:** Use `@@` instead of `@` for TCP. A single `@` sends over UDP. Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host.
  4. Restart the rsyslog service:
         
         sudo systemctl restart rsyslog
         




**For RSA Authentication Manager 8.1-8.3** (uses `syslog-ng`):

  1. SSH into the RSA Authentication Manager appliance.
  2. Edit the syslog-ng configuration file:
         
         sudo vi /etc/syslog-ng/syslog-ng.conf
         

  3. Locate the comment about enabling IP to send log messages to a log server and change the IP address to the IP address of the Bindplane agent host.

  4. Restart the syslog-ng service:
         
         sudo /etc/init.d/syslog restart
         

**Note:** The default syslog port is 514 and cannot be changed in the syslog-ng configuration.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
column23, column24, column22, column26, column27, column28 | additional.fields | Merged with key-value pairs from specified columns  
| extensions.auth.mechanism | Set to "USERNAME_PASSWORD"  
| extensions.auth.type | Set to "MACHINE"  
description | metadata.description | Value copied directly  
action, username1, srcUser, has_principal, has_target, has_user | metadata.event_type | Set to USER_LOGOUT if action closed, USER_LOGIN if opened or expired password, USER_UNCATEGORIZED otherwise, then to USER_LOGIN if has_principal and has_target and has_user, NETWORK_CONNECTION if has_principal and has_target, STATUS_UPDATE if has_principal  
audit_section, column4, application | metadata.product_event_type | Value from audit_section if in tokenmgt or authn, else from column4 if csv, else from application  
column2, column6 | metadata.product_log_id | Value from column2 if in tokenmgt/authn, else from column6  
description | metadata.product_version | Extracted from description using grok pattern  
column10, column14 | network.session_id | Value from column10 if in tokenmgt or authn, else from column14  
column20, column24, hostname | principal.asset.hostname | Value from column20 if in tokenmgt, else from column24 if in else csv, else from hostname  
column4, column5, column8 | principal.asset.ip | Value from column4 if in tokenmgt, else from column5 if in authn, else from column8  
column20, column24, hostname | principal.hostname | Value from column20 if in tokenmgt, else from column24 if in else csv, else from hostname  
column4, column5, column8 | principal.ip | Value from column4 if in tokenmgt, else from column5 if in authn, else from column8  
| principal.platform | Set to "LINUX"  
process_id | principal.process.pid | Value copied directly  
column12, column13, column11, column15, column16, column17 | principal.resource.attribute.labels | Merged with labels from specified columns  
column16, column15, column19 | principal.user.first_name | Value from column16 if in tokenmgt, else from column15 if in authn, else from column19  
column17, column16, column20 | principal.user.last_name | Value from column17 if in tokenmgt, else from column16 if in authn, else from column20  
column16, column17, column15, column19, column20 | principal.user.user_display_name | Concatenated from first and last name fields  
column15, column14, column18, srcUser, username | principal.user.userid | Value from column15 if in tokenmgt, else from column14 if in authn, else from column18 if in else csv, else from srcUser if sudo, else from username  
column8, column12 | security_result.action | Set to ALLOW if column8 or column12 is SUCCESS, else BLOCK  
column8, column12 | security_result.category_details | Value from column8 if in tokenmgt/authn, else from column12  
column20 | security_result.detection_fields | Merged with detection field from column20  
column6, column10 | security_result.rule_name | Value from column6 if in tokenmgt/authn, else from column10  
column1, column5 | security_result.severity | Set to HIGH if error/warning/ERROR, CRITICAL if critical, MEDIUM if notice, LOW if information/info/INFO  
column1, column5 | security_result.severity_details | Value copied directly  
column18, column9, column13 | security_result.summary | Value from column18 if in tokenmgt, else from column9 if in authn, else from column13  
application | target.application | Value copied directly  
hostname | target.asset.hostname | Value copied directly  
column5, column4, column9 | target.asset.ip | Value from column5 if in tokenmgt, else from column4 if in authn, else from column9  
hostname | target.hostname | Value copied directly  
column5, column4, column9 | target.ip | Value from column5 if in tokenmgt, else from column4 if in authn, else from column9  
command | target.process.command_line | Value copied directly  
PWD | target.process.file.full_path | Value copied directly  
pid | target.process.pid | Value copied directly  
column11 | target.resource.product_object_id | Value copied directly  
description | target.url | Extracted from description using grok pattern  
column27, username1, username | target.user.userid | Value from column27 if in tokenmgt, else from username1 if sudo, else from username  
| metadata.product_name | Set to "RSA SECURID"  
| metadata.vendor_name | Set to "RSA"  
`time" and "column1` | `metadata.event_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-securid-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
