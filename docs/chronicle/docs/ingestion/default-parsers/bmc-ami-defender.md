---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-ami-defender/
title: Collect BMC AMI Defender logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:00.627212+00:00
---

# Collect BMC AMI Defender logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-ami-defender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect BMC AMI Defender logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest BMC AMI Defender logs to Google Security Operations using Bindplane agent.

BMC AMI Datastream for z/OS is a mainframe agent program that monitors z/OS system activity and collects, processes, and delivers System Management Facility (SMF) records to distributed SIEM systems in real time. The agent reformats SMF records from RACF, ACF2, Top Secret, TCP/IP, CICS, IMS, and other z/OS system and application events as RFC 3164 compliant syslog messages and transmits them via UDP, TCP, or TLS protocols.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd` for the Bindplane agent
  * Network connectivity between the Bindplane agent host and the z/OS LPAR running BMC AMI Datastream
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * BMC AMI Datastream for z/OS version 6.1 or later installed and running on the z/OS LPAR
  * Access to edit parameter files in the amihlq.PARM data set on z/OS (typically requires TSO/ISPF access or batch job submission authority)
  * Authority to modify BMC AMI Datastream configuration (typically requires RACF READ access to the parameter data sets)



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

**Note:** The `customer ID` is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

  * Windows installation

    1. Open **Command Prompt** or **PowerShell** as an administrator.
    2. Run the following command:
           
           msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
           

    3. Wait for the installation to complete.

    4. Verify the installation by running:
           
           sc query observiq-otel-collector
           

The service should show as **RUNNING**.

  * Linux installation

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

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:1514"
         
         exporters:
           chronicle/bmc_datastream:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
             customer_id: 'your-customer-id-here'
             endpoint: chronicle.googleapis.com
             log_type: BMC_AMI_DEFENDER
             raw_log_field: body
         
         service:
           pipelines:
             logs/datastream_to_chronicle:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/bmc_datastream
         

  2. Replace the following placeholders:

     * Receiver configuration:

`listen_address`: IP address and port to listen on:

       * `0.0.0.0:1514` to listen on all interfaces on port 1514 (recommended for Linux non-root)
       * `0.0.0.0:514` to listen on all interfaces on standard syslog port (requires root on Linux)
       * Specific IP address to listen on one interface
     * Exporter configuration:

       * `creds_file_path`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `customer_id`: Your `customer ID`. For details, see Get Google SecOps customer ID.

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `log_type`: `BMC_AMI_DEFENDER`




### Example configuration for UDP syslog

  * If you prefer UDP transport (lower latency, fire-and-forget):
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/bmc_datastream:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
            endpoint: chronicle.googleapis.com
            log_type: BMC_AMI_DEFENDER
            raw_log_field: body
        
        service:
          pipelines:
            logs/datastream_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/bmc_datastream
        




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/bmc_datastream:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BMC_AMI_DEFENDER
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
           




## Configure BMC AMI Defender syslog forwarding

### Edit the parameter file using TSO/ISPF

  1. Sign in to TSO/ISPF on the z/OS LPAR where BMC AMI Datastream is installed.
  2. From the **ISPF Primary Option Menu** , enter **2** to select **EDIT**.
  3. On the **Edit - Entry Panel** , enter the following:

     * **ISPF Library** : Enter the parameter data set name in the format `'amihlq.PARM'` where amihlq is the high-level qualifier chosen during installation (for example, `'PROD.CZAGENT.PARM'`).
     * **Member** : Enter `$$$CONFG`.
  4. Press **Enter** to open the member for editing.




### Configure the SIEM type

  1. In the `$$$CONFG` member, locate the section labeled **Switches for setting the SIEM type**.
  2. Uncomment one SIEM type by removing the leading semicolon from the appropriate line:

     * For standard syslog format, uncomment: `SWITCH ON(RFC 3164)`
     * For Common Event Format, uncomment: `SWITCH ON(CEF)`
     * For JSON format, uncomment: `SWITCH ON(JSON)`
     * For IBM QRadar LEEF format, uncomment: `SWITCH ON(LEEF)`
     * For Splunk format, uncomment: `SWITCH ON(Splunk)`
**Note:** Enable only one SIEM type. For Google SecOps, RFC 3164, CEF, or JSON formats are recommended.
  3. Press **F3** to save and exit the member.




### Configure the syslog server

  1. From the **Edit - Entry Panel** , enter the following:

     * **ISPF Library** : Enter `'amihlq.PARM'` (same as before).
     * **Member** : Enter `$$$SERVR`.
  2. Press **Enter** to open the member for editing.

  3. Locate the section corresponding to your selected SIEM type. For example:

     * For RFC 3164: Locate the section labeled `; RFC 3164`
     * For CEF: Locate the section labeled `; CEF - TRANS(TCP) Recommended`
     * For JSON: Locate the section labeled `; JSON - TRANS(TCP) Recommended`
  4. Uncomment the SERVER statement by removing the leading semicolon.

  5. Edit the SERVER statement with the following values:

     * Replace `ip.addr.example` with the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * If using TCP (recommended), the statement should look like:
           
           SERVER 192.168.1.100:1514 TRANS(TCP) MAXMSG(2000)
           

     * If using UDP, the statement should look like:
           
           SERVER 192.168.1.100:514 TRANS(UDP) MAXMSG(2000)
           

**Note:** The port number must match the port configured in the Bindplane agent config.yaml file. Use port 1514 for TCP or 514 for UDP.
  6. If you selected CEF, JSON, or Splunk format and are using TCP transport, locate the OPTIONS statement section and uncomment the FRAMING parameter:
         
         OPTIONS FRAMING(OCTETCOUNT)
         

  7. Press **F3** to save and exit the member.




### Refresh the BMC AMI Datastream configuration

  1. From the **ISPF Primary Option Menu** , enter **6** to select **COMMAND**.
  2. On the **TSO Command Processor** screen, enter the following MVS console command:
         
         F czagentname,PARMS
         

Replace `czagentname` with the name of the BMC AMI Datastream started task (typically `CZAGENT` or the instance name configured during installation).

  3. Press **Enter** to execute the command.

  4. Verify the configuration was refreshed by checking the system log for message **CZA0001I** indicating the parameter file was successfully processed.




### Verify syslog transmission

  1. From the **ISPF Primary Option Menu** , enter **6** to select **COMMAND**.
  2. Enter the following command to display BMC AMI Datastream statistics:
         
         F czagentname,STATS
         

  3. Press **Enter** to execute the command.

  4. Check the system log for message **CZA0350I** showing the number of messages sent to the syslog server.

  5. Verify the Bindplane agent is receiving messages by checking the Bindplane agent logs:

     * **Linux** : `sudo journalctl -u observiq-otel-collector -f`
     * **Windows** : Check `C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log`



### Alternative: Edit parameter file using batch job

If you do not have TSO/ISPF access, you can edit the parameter files using a batch job:

  1. Create a batch job with the following JCL:
         
         //EDITPARM JOB (ACCT),'EDIT DATASTREAM PARMS',
         //         CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID
         //STEP1    EXEC PGM=IEBGENER
         //SYSPRINT DD SYSOUT=*
         //SYSIN    DD DUMMY
         //SYSUT1   DD *
         SWITCH ON(RFC 3164)
         /*
         //SYSUT2   DD DSN=amihlq.PARM($$$CONFG),DISP=SHR
         //STEP2    EXEC PGM=IEBGENER
         //SYSPRINT DD SYSOUT=*
         //SYSIN    DD DUMMY
         //SYSUT1   DD *
         SERVER 192.168.1.100:1514 TRANS(TCP) MAXMSG(2000)
         /*
         //SYSUT2   DD DSN=amihlq.PARM($$$SERVR),DISP=SHR
         

  2. Replace `amihlq` with the high-level qualifier for your BMC AMI Datastream installation.

  3. Replace `192.168.1.100:1514` with the IP address and port of your Bindplane agent host.

  4. Submit the job and verify successful completion (return code 0).

  5. Issue the MODIFY command to refresh the configuration as described in the previous section.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
aceeadsp | security_result.detection_fields | Fields that were used to determine the security result  
aceeaudt | security_result.detection_fields | Fields that were used to determine the security result  
aceeflg1 | security_result.detection_fields | Fields that were used to determine the security result  
aceelogu | security_result.detection_fields | Fields that were used to determine the security result  
aceeoper | security_result.detection_fields | Fields that were used to determine the security result  
aceepriv | security_result.detection_fields | Fields that were used to determine the security result  
aceeracf | security_result.detection_fields | Fields that were used to determine the security result  
aceeroa | security_result.detection_fields | Fields that were used to determine the security result  
aceespec | security_result.detection_fields | Fields that were used to determine the security result  
additional.fields | additional.fields | Additional information about the event  
auth | security_result.detection_fields | Fields that were used to determine the security result  
auth_audit | security_result.detection_fields | Fields that were used to determine the security result  
auth_bypass | security_result.detection_fields | Fields that were used to determine the security result  
auth_exit | security_result.detection_fields | Fields that were used to determine the security result  
auth_normal | security_result.detection_fields | Fields that were used to determine the security result  
auth_oper | security_result.detection_fields | Fields that were used to determine the security result  
auth_soft | security_result.detection_fields | Fields that were used to determine the security result  
auth_special | security_result.detection_fields | Fields that were used to determine the security result  
auth_trusted | security_result.detection_fields | Fields that were used to determine the security result  
authinfo | security_result.description | Description of the security result  
event | metadata.product_event_type | Product-specific event type  
event_type | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
eventdesc | metadata.description | Description of the event  
group | additional.fields | Additional information about the event  
hostname | principal.hostname, principal.asset.hostname | Hostname of the principal, Hostname of the asset  
jobid | security_result.detection_fields | Fields that were used to determine the security result  
jobnm | additional.fields | Additional information about the event  
jsauth | security_result.detection_fields | Fields that were used to determine the security result  
name | principal.user.user_display_name | Display name of the user  
pgm | security_result.detection_fields | Fields that were used to determine the security result  
privstatd | security_result.detection_fields | Fields that were used to determine the security result  
reas_always | security_result.detection_fields | Fields that were used to determine the security result  
reas_audit | security_result.detection_fields | Fields that were used to determine the security result  
reas_cmdviol | security_result.detection_fields | Fields that were used to determine the security result  
reas_globalaudit | security_result.detection_fields | Fields that were used to determine the security result  
reas_setropts | security_result.detection_fields | Fields that were used to determine the security result  
reas_special | security_result.detection_fields | Fields that were used to determine the security result  
reas_user | security_result.detection_fields | Fields that were used to determine the security result  
reas_verify | security_result.detection_fields | Fields that were used to determine the security result  
rtype | additional.fields | Additional information about the event  
saf | additional.fields | Additional information about the event  
safd | additional.fields | Additional information about the event  
security_result.detection_fields | security_result.detection_fields | Fields that were used to determine the security result  
severity | security_result.severity, security_result.severity_details | Severity of the security result, Detailed severity information  
sid | additional.fields | Additional information about the event  
timestamp | metadata.event_timestamp | Timestamp when the event occurred  
tokflg1 | security_result.detection_fields | Fields that were used to determine the security result  
tokflg3 | security_result.detection_fields | Fields that were used to determine the security result  
tokpriv | security_result.detection_fields | Fields that were used to determine the security result  
toksus | security_result.detection_fields | Fields that were used to determine the security result  
tokudus | security_result.detection_fields | Fields that were used to determine the security result  
userid | principal.user.userid | User ID  
violation | security_result.detection_fields | Fields that were used to determine the security result  
user_warning | security_result.detection_fields | Fields that were used to determine the security result  
worktyped | additional.fields | Additional information about the event  
| metadata.product_name | Name of the product  
| metadata.vendor_name | Vendor/company name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bmc-ami-defender-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
