---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-email/
title: Collect Barracuda Email Security Gateway logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:34.580296+00:00
---

# Collect Barracuda Email Security Gateway logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/barracuda-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Barracuda Email Security Gateway logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Barracuda Email Security Gateway logs to Google Security Operations using Bindplane.

Barracuda Email Security Gateway is an email security appliance that provides inbound filtering for spam, viruses, spoofing, and phishing attacks. It also provides outbound filtering for data loss prevention and email encryption. The gateway logs all email transactions, policy actions, and threat detections via syslog.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Barracuda Email Security Gateway management console.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agent**.
  3. Download the **Ingestion Authentication File**. 
     * Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional Installation Resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             tcplog:
                 # Replace the port and IP address as required
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/chronicle_w_labels:
                 compression: gzip
                 # Adjust the path to the credentials file you downloaded in Step 1
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 # Replace with your actual customer ID from Step 2
                 customer_id: <your_customer_id>
                 endpoint: malachiteingestion-pa.googleapis.com
                 # Add optional ingestion labels for better organization
                 log_type: 'BARRACUDA_EMAIL'
                 raw_log_field: body
                 ingestion_labels:
         
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - tcplog
                     exporters:
                         - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<your_customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.



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
         




## Configure syslog forwarding on Barracuda Email Security Gateway

  1. Sign in to the **Barracuda Email Security Gateway** web interface.
  2. Go to **ADVANCED > Advanced Networking**.
  3. In the **Syslog** section, configure the following fields: 
     * **Syslog Server** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
     * **Syslog Port** : Enter `514` (or your configured Bindplane agent port).
     * **Syslog Protocol** : Select **TCP**.
  4. Click **Save Changes**.

**Note:** Mail syslog data includes the connecting IP address, envelope From address, envelope To address, and spam score for transmitted messages. The data appears on the mail facility at the debug priority level. If there are firewalls between the Barracuda Email Security Gateway and the Bindplane agent host, ensure that port 514 is open.



### Verify syslog delivery

  1. After configuring syslog forwarding, send a test email through the gateway.
  2. To confirm that the gateway is sending syslog data, go to **ADVANCED > Troubleshooting** and view the **Syslog** section to monitor real-time mail syslog output.
  3. On the Bindplane agent host, verify that logs are being received:
         
         sudo journalctl -u observiq-otel-collector -f
         




For more information, see the [Barracuda Email Security Gateway syslog documentation](https://campus.barracuda.com/product/emailsecuritygateway/doc/171802918/syslog-and-the-barracuda-email-security-gateway/).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`dst_domain` | `target.hostname` | Value of `dst_domain` field.  
`dst_domain` | `target.asset.hostname` | Value of `dst_domain` field.  
`geoip` | `target.location.country_or_region` | Value of `geoip` field.  
`hdr_from` | `network.email.from` | Value of `hdr_from` field if it is an email address.  
`hdr_to` | `network.email.to` | Value of `hdr_to` field if it is an email address, otherwise parsed from JSON array in `hdr_to` field.  
`host` | `principal.hostname` | Value of `host` field.  
`host` | `principal.asset.hostname` | Value of `host` field.  
`message_id` | `network.email.mail_id` | Value of `message_id` field.  
`product_log_id` | `metadata.product_log_id` | Value of `product_log_id` field.  
`queue_id` | `security_result.detection_fields` | Value of `queue_id` field.  
`recipient_email` | `network.email.to` | Value of `recipient_email` field if it is not empty or `-`.  
`recipients.action` | `security_result.action` | Mapped to ALLOW if value is "allowed", otherwise mapped to BLOCK.  
`recipients.action` | `security_result.action_details` | Value of `recipients.action` field.  
`recipients.delivery_detail` | `security_result.detection_fields` | Value of `recipients.delivery_detail` field.  
`recipients.delivered` | `security_result.detection_fields` | Value of `recipients.delivered` field.  
`recipients.email` | `network.email.to` | Value of `recipients.email` field if it is an email address.  
`recipients.reason` | `security_result.detection_fields` | Value of `recipients.reason` field.  
`recipients.reason_extra` | `security_result.detection_fields` | Value of `recipients.reason_extra` field.  
`recipients.taxonomy` | `security_result.detection_fields` | Value of `recipients.taxonomy` field.  
`service` | `security_result.summary` | Value of `service` field.  
`size` | `network.received_bytes` | Value of `size` field converted to an unsigned integer.  
`src_ip` | `principal.ip` | Value of `src_ip` field if it is not empty or `0.0.0.0`.  
`src_ip` | `principal.asset.ip` | Value of `src_ip` field if it is not empty or `0.0.0.0`.  
`src_ip` | `security_result.about.ip` | Value of `src_ip` field if it is not empty or `0.0.0.0`.  
`subject` | `network.email.subject` | Value of `subject` field.  
`target_ip` | `target.ip` | Value of `target_ip` field.  
`target_ip` | `target.asset.ip` | Value of `target_ip` field.  
`timestamp` | `metadata.event_timestamp` | Parsed timestamp from the log entry.  
| `metadata.event_type` | Hardcoded to `EMAIL_TRANSACTION`.  
| `metadata.log_type` | Hardcoded to `BARRACUDA_EMAIL`.  
| `metadata.vendor_name` | Hardcoded to "Barracuda".  
| `network.application_protocol` | Set to `SMTP` if `process` field contains "smtp".  
| `network.direction` | Set to `INBOUND` if `process` field contains "inbound", set to `OUTBOUND` if `process` field contains "outbound".  
| `security_result.action` | Set based on a combination of `action`, `action_code`, `service`, and `delivered` fields.  
| `security_result.category` | Set based on a combination of `action`, `reason`, and other fields.  
`auth_serv` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`spf_sender_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`dkim_result` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dmarc_result` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dkim_domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`header_from` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`spf_result` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`smtp_mailfrom` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`gateway` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`attachment.name` | `event.idm.read_only_udm.target.file.names` | Mapped from changelog  
`attachment.md5` | `event.idm.read_only_udm.about` | Mapped from changelog  
`intermediary` | `event.idm.read_only_udm.intermediary` | Mapped from changelog  
`account_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`domain_id` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`tls` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`env_from` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`hdr_auth_results` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`recipient_count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ptr_record` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`log_header_end` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.affected_mailboxes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.attachment` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.body_text` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`accountId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`accessTokenId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`payload.type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`payload.incident_id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`payload.messages_received` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`payload.matched_email_count` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`product` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`payload.sender` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`payload.recipient` | `event.idm.read_only_udm.target.user.email_addresses` | Mapped from changelog  
`payload.subject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`payload.date` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`payload.category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`payload.created_by` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`payload.sender_display_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`payload.sender_email` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`payload.login_country` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`payload.login_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`payload.login_user_agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`payload.user_display_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`payload.user_email` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`payload.body_links` | `event.idm.read_only_udm.security_result.about.url` | Mapped from changelog  
`payload.sender_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`attachments` | `additional.fields` | Mapped from changelog  
`recipients.delivery_detail", "recipients.reason", "recipients.taxonomy", "recipients.reason_extra" and "recipient.delivered` | `security_result.detection_fields` | Mapped from changelog  
`sender_email` | `network.email.from` | Mapped from changelog  
`security_result.action` | `QUARANTINE` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-email-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
