---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zix-email-encryption/
title: Collect Zix Email Encryption logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:03.815356+00:00
---

# Collect Zix Email Encryption logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zix-email-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zix Email Encryption logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Zix Email Encryption logs to Google Security Operations using the Bindplane agent.

Zix Email Encryption (now OpenText ZixEncrypt) is an email encryption and DLP platform for secure email communications and compliance. It generates SMTP transaction logs and encryption event logs on the ZixGateway appliance.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Zix Email Encryption appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Zix Email Encryption appliance (ZixGateway) with administrator permissions
  * Access to Zix Email Encryption log files (SMTP transaction logs, encryption event logs)



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
          filelog:
            include:
              - /var/log/zix/*.log
              - /opt/zix/logs/*.log
            start_at: beginning
        
        exporters:
          chronicle/zix_email:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: ZIX_EMAIL_ENCRYPTION
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/zix_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/zix_email
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths or glob patterns to monitor: 
      * **Linux** : `/var/log/zix/*.log` or `/opt/zix/logs/*.log`
      * **Windows** : `C:\Program Files\Zix\logs\*.log`
      * Adjust the path to match your ZixGateway log file location
    * `start_at`: Set to `beginning` to read existing log files from the start, or `end` to only read new entries
  * **Exporter configuration:**

    * `zix_email`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `ZIX_EMAIL_ENCRYPTION`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `zix_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/zix_email:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ZIX_EMAIL_ENCRYPTION
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
             




## Configure Zix Email Encryption log collection

The Bindplane agent collects log files directly from the ZixGateway appliance file system.

### Verify log file locations

  1. Sign in to the **ZixGateway** management console.
  2. Go to **Monitoring > Logs**.
  3. Verify the log file directory:

     * **Linux** : `/var/log/zix/` or `/opt/zix/logs/`
     * **Windows** : `C:\Program Files\Zix\logs\`
**Note:** Consult the ZixGateway Administration Guide for your specific log directory path. Ensure the Bindplane agent has read access to the log directory.
  4. Confirm that SMTP transaction logs and encryption event logs are being written to the expected location.

  5. Update the `include` paths in the Bindplane agent `config.yaml` if the log directory differs from the defaults.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
intermediary | intermediary | Merged from intermediary  
relay_host | intermediary.hostname | Value copied directly from relay_host  
relay_ip | intermediary.ip | Merged from relay_ip  
relay_port | intermediary.port | Value from relay_port converted to integer  
message_details | metadata.description | Value copied directly from message_details in smtp, smtpd, cleanup, or error blocks  
principal_hostname, sender_email | metadata.event_type | Set to "EMAIL_TRANSACTION" if principal_hostname and sender_email not empty, else "NETWORK_CONNECTION" if principal_hostname and (target_host or target_ip) not empty, else "STATUS_UPDATE" if principal_hostname not empty and (target_host or target_ip) empty, else "GENERIC_EVENT"  
| metadata.product_name | Set to "Zix Email Encryption"  
| metadata.vendor_name | Set to "Zix"  
message | network.application_protocol | Set to "SMTP" if message matches smtp or smtpd  
sender_email | network.email.from | Value copied directly if sender_email matches email regex  
subject | network.email.subject | Merged from subject  
recipient_email | network.email.to | Merged from recipient_email if matches email regex  
data_size | network.received_bytes | Value from data_size converted to uinteger  
tls_cipher | network.tls.cipher | Value copied directly from tls_cipher  
cert_data | network.tls.client.certificate.issuer | Value copied directly from cert_data  
daemon | principal.application | Value copied directly from daemon  
principal_hostname | principal.hostname | Value copied directly from principal_hostname  
file | principal.process.file.full_path | Value copied directly from file  
pid | principal.process.pid | Value copied directly from pid  
| principal.resource.type | Set to "CLEANUP_MESSAGE_ID" if daemon is cleanup  
sender_email | principal.user.user_display_name | Value copied directly if sender_email does not match email regex  
user_id | principal.user.userid | Value from user_id if not empty, else from user_id in else block  
security_result | security_result | Merged from security_result  
security_action | security_result.action | Merged from security_action  
failure_reason | security_result.description | Value copied directly from failure_reason  
security_summary | security_result.summary | Value copied directly from security_summary  
file | target.file.full_path | Value copied directly from file  
target_host | target.hostname | Value copied directly from target_host  
target_ip | target.ip | Merged from target_ip  
target_port | target.port | Value from target_port converted to integer  
message_id | target.resource.name | Value copied directly from message_id  
recipient_email | target.user.user_display_name | Value copied directly if recipient_email does not match email regex  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zix-email-encryption-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
