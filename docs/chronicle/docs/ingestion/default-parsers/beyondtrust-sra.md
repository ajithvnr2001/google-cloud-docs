---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-sra/
title: Collect BeyondTrust Secure Remote Access (formerly BeyondTrust Privileged Remote Access) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:23:30.667135+00:00
---

# Collect BeyondTrust Secure Remote Access (formerly BeyondTrust Privileged Remote Access) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-sra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect BeyondTrust Secure Remote Access (formerly BeyondTrust Privileged Remote Access) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest BeyondTrust Secure Remote Access (formerly known as BeyondTrust Privileged Remote Access) logs to Google Security Operations using Bindplane.

BeyondTrust Secure Remote Access is a privileged access management solution that lets organizations control, monitor, and audit privileged remote access for vendors, contractors, and internal administrators connecting to critical systems. It provides credential injection, just-in-time access, and session recording. BeyondTrust Secure Remote Access logs session activity, authentication events, and administrative actions via syslog.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Administrative access to the BeyondTrust Secure Remote Access B Series Appliance interface (`/appliance`).



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
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             udplog:
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
                 log_type: 'BEYONDTRUST_REMOTE_ACCESS'
                 raw_log_field: body
                 ingestion_labels:
         
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<your_customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.

**Note:** BeyondTrust Secure Remote Access uses `local0` facility and defaults to UDP port 514 for non-TLS syslog. If you configure Syslog over TLS on the appliance, use `tcplog` as the receiver and set the port to `6514`.



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
         




## Configure BeyondTrust Secure Remote Access syslog forwarding

  1. Sign in to the BeyondTrust Secure Remote Access **B Series Appliance** interface (`/appliance`).
  2. Go to **Security** > **Appliance Administration**.
  3. Scroll down to the **Syslog** section.
  4. In the **Remote Syslog Server** field, enter the hostname or IP address of the Bindplane agent host (for example, `192.168.1.100`).
  5. Select the **Message Format** for event notification messages: 
     * **RFC 5424** \- modern syslog standard with structured data (recommended).
     * **BSD (legacy)** \- legacy BSD syslog format (RFC 3164).
     * **Syslog over TLS** \- encrypted syslog using TCP port 6514.
  6. If necessary, change the default port: 
     * RFC 5424 and BSD formats default to **UDP 514**.
     * Syslog over TLS defaults to **TCP 6514**.
  7. Click **Save**.

**Note:** You can configure up to three syslog servers on the B Series Appliance. When adding or changing a syslog server, an alert is emailed to the administrator's email address.**Note:** Events from both the `/login` administrative interface (such as user login attempts, account creation, and configuration changes) and the `/appliance` interface are sent as syslog messages. BeyondTrust Secure Remote Access logs are sent using the `local0` facility.



### Verify syslog delivery

  1. After configuring syslog forwarding, initiate a test support session or sign in to the `/login` administrative interface.
  2. On the Bindplane agent host, verify that logs are being received:
         
         sudo journalctl -u observiq-otel-collector -f
         




For more information, see the [BeyondTrust Privileged Remote Access syslog documentation](https://docs.beyondtrust.com/pra/docs/syslog).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_field` | `additional.fields` | Merged  
`additional_device_product` | `additional.fields` | Merged  
`additional_device_vendor` | `additional.fields` | Merged  
`additional_dst_priv` | `additional.fields` | Merged  
`additional_event_name` | `additional.fields` | Merged  
`additional_external_key_label` | `additional.fields` | Merged  
`additional_jumpGroupId` | `additional.fields` | Merged  
`additional_jumpGroupName` | `additional.fields` | Merged  
`additional_jumpGroupType` | `additional.fields` | Merged  
`additional_jumpointId` | `additional.fields` | Merged  
`additional_jumpointName` | `additional.fields` | Merged  
`additional_segment_number` | `additional.fields` | Merged  
`additional_site_id` | `additional.fields` | Merged  
`additional_total_segments` | `additional.fields` | Merged  
`appliance_identifier_label` | `additional.fields` | Merged  
`appliance_label` | `additional.fields` | Merged  
`eventid_label` | `additional.fields` | Merged  
`eventsubject_label` | `additional.fields` | Merged  
`eventtype_label` | `additional.fields` | Merged  
`format_version_label` | `additional.fields` | Merged  
`nvps_actiontype_label` | `additional.fields` | Merged  
`nvps_authenticationtype_label` | `additional.fields` | Merged  
`nvps_createdate_label` | `additional.fields` | Merged  
`nvps_eventseverity_label` | `additional.fields` | Merged  
`nvps_subjectdescription_label` | `additional.fields` | Merged  
`product_label` | `additional.fields` | Merged  
`eventName` | `extensions.auth.auth_details` | Directly mapped  
`mechanism` | `extensions.auth.mechanism` | Merged  
`target` | `extensions.auth.type` | Mapped: `"rep_client", "web/login"` → `MACHINE`, `"rep_client", "web/login"` → `SSO`, `rep_c...  
`intermediary_hostname` | `intermediary.asset.hostname` | Directly mapped  
`intermediary_ip` | `intermediary.asset.ip` | Merged  
`intermediary_hostname` | `intermediary.hostname` | Directly mapped  
`intermediary_ip` | `intermediary.ip` | Merged  
`msg` | `metadata.description` | Directly mapped  
`datetime` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`eventdate` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestampvalue` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZZ`  
`when` | `metadata.event_timestamp` | Parsed as `UNIX`  
`device_vendor` | `metadata.event_type` | Mapped: `Bomgar` → `GENERIC_EVENT`  
`eventName` | `metadata.event_type` | Mapped: `(?i)login` → `USER_LOGIN`, `(?i)logout` → `USER_LOGOUT`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`category` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`id` | `metadata.product_event_type` | Directly mapped  
`nvps_auditid` | `metadata.product_log_id` | Directly mapped  
`product_log_id` | `metadata.product_log_id` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`sessionId` | `network.session_id` | Directly mapped  
`agentid` | `observer.application` | Directly mapped  
`product_event_type` | `principal.asset.hostname` | Directly mapped  
`nvps_ipaddress` | `principal.asset.ip` | Merged  
`sourceip` | `principal.asset.ip` | Merged  
`product_event_type` | `principal.hostname` | Directly mapped  
`nvps_ipaddress` | `principal.ip` | Merged  
`sourceip` | `principal.ip` | Merged  
`srcHost` | `principal.ip` | Merged  
`who_ip` | `principal.ip` | Merged  
`process_id` | `principal.process.pid` | Directly mapped  
`srcUser` | `principal.user.user_display_name` | Directly mapped  
`user_display_name` | `principal.user.user_display_name` | Directly mapped  
`srcUid` | `principal.user.userid` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`userid` | `principal.user.userid` | Directly mapped  
`who` | `principal.user.userid` | Directly mapped  
`security_action` | `security_result.action` | Merged  
`status` | `security_result.action_details` | Directly mapped  
`reason` | `security_result.description` | Directly mapped  
`severity` | `security_result.severity` | Mapped values (5 total, e.g. `0` → `UNKNOWN_SEVERITY`, `1` → `LOW`, `2` → `MEDIUM`)  
`eventName` | `security_result.summary` | Directly mapped  
`eventname` | `security_result.summary` | Directly mapped  
`nvps_systemname` | `target.application` | Directly mapped  
`target` | `target.application` | Directly mapped  
`filePath` | `target.file.full_path` | Directly mapped  
`fsize` | `target.file.size` | Directly mapped  
`deviceHost` | `target.hostname` | Directly mapped  
`site` | `target.hostname` | Directly mapped  
`dstHost` | `target.ip` | Merged  
`nvps_username_label` | `target.resource.attribute.labels` | Merged  
`nvps_appuserid` | `target.user.product_object_id` | Directly mapped  
`dstUser` | `target.user.user_display_name` | Directly mapped  
`dstUid` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `BeyondTrust Secure Remote Access`  
N/A | `metadata.vendor_name` | Constant: `BeyondTrust`  
N/A | `security_result.severity` | Constant: `UNKNOWN_SEVERITY`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
