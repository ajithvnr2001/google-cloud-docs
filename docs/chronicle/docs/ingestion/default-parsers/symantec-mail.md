---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-mail/
title: Collect Symantec Messaging Gateway logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:45.838184+00:00
---

# Collect Symantec Messaging Gateway logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec Messaging Gateway logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec Messaging Gateway logs to Google Security Operations using Bindplane.

Symantec Messaging Gateway is an email security gateway that provides antispam, antimalware, and content filtering for enterprise email. It supports native syslog forwarding for email processing events, policy enforcement, and system health logs.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Symantec Messaging Gateway appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Symantec Messaging Gateway management console



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
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/symantec_mail:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: SYMANTEC_MAIL
            raw_log_field: body
        
        service:
          pipelines:
            logs/symantec_mail_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/symantec_mail
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
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
          chronicle/symantec_mail:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SYMANTEC_MAIL
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Configure Symantec Messaging Gateway syslog forwarding

  1. Sign in to the **Symantec Messaging Gateway** management console.
  2. Go to **Administration > Settings > Logs**.
  3. Click the **Remote** tab.
  4. Enable **Syslogs**.
  5. Configure the remote syslog server: 
     * **Host** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
file.fileNameOrURL | about.file.full_path | Value copied directly for FILE_INCLUDED  
file.md5 | about.file.md5 | Value copied directly for FILE_INCLUDED  
file.fileType | about.file.mime_type | Value copied directly for FILE_INCLUDED  
file.sha256 | about.file.sha256 | Value copied directly for FILE_INCLUDED  
file.fileSize | about.file.size | Converted to uinteger for FILE_INCLUDED  
file.urlCategories, file.urlRiskScore | about.labels | Merged labels for LINK_INCLUDED  
file.fileNameOrURL | about.url | Value copied directly for LINK_INCLUDED  
emailInfo.longMsgRef, emailInfo.messageId, emailInfo.isOutbound, emailInfo.HELOString, emailInfo.authResults.raw_header, emailInfo.authResults.dkim, emailInfo.authResults.dkim_signing_domain, emailInfo.authResults.spf, emailInfo.authResults.dmarc, emailInfo.authResults.dmarc_policy, emailInfo.authResults.dmarc_override_action, emailInfo.tlsInfo.tlsAdvertised, emailInfo.tlsInfo.tlsUsed, emailInfo.tlsInfo.tlsKeyLength, emailInfo.tlsInfo.tlsFallbackReason, emailInfo.tlsInfo.tlsForwardSecrecy, emailInfo.tlsInfo.tlsNegotiationFailed, emailInfo.messageSize, emailInfo.avQuarantinePenId, emailInfo.rawHeaderFrom, emailInfo.headerReplyTo, emailInfo.newDomainAge, emailInfo.timeInCynicSandboxMs, incidents | additional.fields | Merged as labels  
emailInfo.mailProcessingStartTime, @timestamp | metadata.event_timestamp | Converted from mailProcessingStartTime if present, else from @timestamp  
| metadata.event_type | Set to "EMAIL_TRANSACTION" if email_from_present and email_to_present, else "NETWORK_CONNECTION" if has_principal and has_target, else "USER_UNCATEGORIZED" if has_user, else "STATUS_UPDATE" if has_principal, else "GENERIC_EVENT"  
emailInfo.xMsgRef | metadata.product_log_id | Value copied directly  
emailInfo.headerFrom | network.email.from | Value copied directly if matches email pattern  
emailInfo.subject | network.email.subject | Value copied directly  
emailInfo.envTo, emailInfo.headerTo | network.email.to | Merged from envTo and headerTo if match email pattern  
emailInfo.tlsInfo.tlsCipher | network.tls.cipher | Value copied directly  
emailInfo.senderMailserver | network.tls.client.server_name | Value copied directly  
emailInfo.tlsInfo.tlsPolicy | network.tls.version | Value copied directly  
emailInfo.tlsInfo.tlsProtocol | network.tls.version_protocol | Value copied directly  
emailInfo.senderMailserver | principal.hostname | Value copied directly  
emailInfo.senderIp | principal.ip | Value copied directly  
emailInfo.country | principal.location.country_or_region | Value copied directly  
emailInfo.envFrom | principal.user.email_addresses | Value copied directly  
| metadata.product_name | Set to "SYMANTEC_MAIL"  
| metadata.vendor_name | Set to "SYMANTEC_MAIL"  
`hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`process` | `event.idm.read_only_udm.principal.process.file.names` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`tag` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`loglevel` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`log_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`internal_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ruleset` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ttl` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`allow_redirect` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`transaction_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`component` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msg_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`status` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.metadata.ingestion_labels` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`emailInfo.longMsgRef", "emailInfo.messageId", "emailInfo.isOutbound", "emailInfo.HELOString", "emailInfo.authResults.raw_header", "emailInfo.authResults.dkim", "emailInfo.authResults.dkim_signing_domain", "emailInfo.authResults.spf", "emailInfo.authResults.dmarc", "emailInfo.authResults.dmarc_policy", "emailInfo.authResults.dmarc_override_action", "emailInfo.tlsInfo.tlsAdvertised", "emailInfo.tlsInfo.tlsUsed", "emailInfo.tlsInfo.tlsKeyLength", "emailInfo.tlsInfo.tlsFallbackReason", "emailInfo.tlsInfo.tlsForwardSecrecy", "emailInfo.tlsInfo.tlsNegotiationFailed", "emailInfo.messageSize", "emailInfo.avQuarantinePenId", "emailInfo.rawHeaderFrom", "emailInfo.headerReplyTo", "emailInfo.newDomainAge", "emailInfo.timeInCynicSandboxMs", and "incidents` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-mail-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
