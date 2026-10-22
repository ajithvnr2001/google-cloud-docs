---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-data-domain/
title: Collect Dell EMC Data Domain logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:11.069179+00:00
---

# Collect Dell EMC Data Domain logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-data-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Dell EMC Data Domain logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Dell EMC Data Domain logs to Google Security Operations using Bindplane. The Logstash parser code first extracts key fields from raw DELL_EMC_DATA_DOMAIN logs using grok patterns based on the log message format. Then, it maps the extracted fields to the corresponding fields in the Unified Data Model (UDM) schema, enriching the data with additional context like event type and security result.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Windows 2016 or later, or a Linux host with `systemd`
  * If running behind a proxy, firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to Dell EMC Data Domain



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

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             udplog:
                 # Replace the port and IP address as required
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/chronicle_w_labels:
                 protocol: https
                 # Region of your instance, for example us, europe, asia-southeast1
                 location: <LOCATION>
                 # Project number of the Google Cloud project linked to the instance
                 project: '<PROJECT_NUMBER>'
                 compression: gzip
                 # Adjust the path to the credentials file you downloaded in Step 1
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 # Replace with your actual customer ID from Step 2
                 customer_id: <customer_id>
                 endpoint: chronicle.googleapis.com
                 # Add optional ingestion labels for better organization
                 ingestion_labels:
                     log_type: 'DELL_EMC_DATA_DOMAIN'
                     raw_log_field: body
         
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/chronicle_w_labels
         

  3. Replace the port and IP address as required in your infrastructure.

  4. Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.

  5. Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

  6. Replace `<customer_id>` with the actual customer ID.

  7. Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
            chronicle/chronicle_w_labels:
                compression: gzip
                # Adjust the path to the credentials file you downloaded in Step 1
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                # Replace with your actual customer ID from Step 2
                customer_id: <customer_id>
                endpoint: malachiteingestion-pa.googleapis.com
                # Add optional ingestion labels for better organization
                ingestion_labels:
                    log_type: 'DELL_EMC_DATA_DOMAIN'
                    raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure Syslog for Dell EMC Data Domain

  1. Sign in to the **Dell EMC Data Domain** using CLI.
  2. Display the current configuration:
         
         log host show
         

  3. Enable sending log messages to other systems:
         
         log host enable
         

  4. Add the Bindplane agent IP to the syslog using the following command, replace `<bindplane-ip>` with the actual Bindplane agent IP address.
         
         log host add <bindplane-ip>
         

  5. Add the Bindplane agent port to the syslog using the following command, replace `<bindplane-port>` with the actual Bindplane agent port number.
         
         log server-port set <bindplane-port>
         




## Supported Dell EMC Data Domain sample logs

  * SYSLOG + KV
        
        <174>ddsh: {epoch=1649171401;id='AUDIT-DDSH-00001';desc='DDSH CLI command';level=3;user='dummy_user';role='se';app='ddsh';host='dd-host-1';detail='cmd=cifs show detailed-stats';}
        

  * SYSLOG
        
        <38>sshd[13244]: Accepted publickey for dd-admin from 192.0.2.1 port 57656 ssh2: RSA SHA256:+BWDxlMYuJgfC0LhzacEAUpFHlAZlNOYXAKKJ4SAipQ
        

    * JSON
    
    {
    "Timestamp": "2024-09-05T13:25:14Z",
    "EventName": "Participant left session",
    "EventType": "Session",
    "Username": "user_9999",
    "EventDetails": [
      {
        "OldValue": "",
        "NewValue": "1352719861",
        "PolicyEnforcementNewValue": null,
        "PolicyEnforcementOldValue": null,
        "PropertyName": "ID of affected participant",
        "PropertyCategory": "AffectedParticipant"
      },
      {
        "OldValue": "",
        "NewValue": "User Name 1",
        "PolicyEnforcementNewValue": null,
        "PolicyEnforcementOldValue": null,
        "PropertyName": "Name of affected participant",
        "PropertyCategory": "AffectedParticipant"
      }
    ],
    "Computer": "HOST-PC-400",
    "EventId": 35139395
    }
    

  * SYSLOG + XML
        
        <21>1 2024-08-01T12:31:40.791267+02:00 VEEM-HOST-01 Veeam_ONE_Server 7172 - [origin enterpriseId="31023"] Operation:"SendEmail" Email has been sent Data:<data><recipient>recipient@example.com</recipient><subject>VM resetting Information for Virtual Machine &quot;VM_RESTORED_2024&quot;</subject></data>
        




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
app | read_only_udm.target.application | Value is taken from the 'app' field extracted by the first grok parser.  
cmd | read_only_udm.target.process.command_line | Value is taken from the 'cmd' field extracted by the first grok parser, or from the 'detail' field if the 'cmd' field is empty.  
desc | read_only_udm.metadata.description | Value is taken from the 'desc' field extracted by the first grok parser.  
epoch | read_only_udm.metadata.event_timestamp.seconds | Value is taken from the 'epoch' field and converted to a timestamp using the 'date' filter.  
host | read_only_udm.principal.hostname | Value is taken from the 'host' field extracted by the first grok parser.  
id | read_only_udm.metadata.product_event_type | Value is taken from the 'id' field extracted by the first grok parser.  
pid | read_only_udm.target.process.pid | Value is taken from the 'pid' field extracted by the first grok parser.  
reason | read_only_udm.security_result.description | Value is taken from the 'reason' field extracted by the first grok parser.  
role | read_only_udm.principal.user.attribute.roles.name | Value is taken from the 'role' field extracted by the first grok parser.  
session_id | read_only_udm.network.session_id | Value is taken from the 'session_id' field extracted by the first grok parser.  
src_ip | read_only_udm.principal.ip | Value is taken from the 'src_ip' field extracted by the second grok parser.  
src_port | read_only_udm.principal.port | Value is taken from the 'src_port' field extracted by the second grok parser and converted to an integer.  
timestamp.nanos | read_only_udm.metadata.event_timestamp.nanos | Value is taken from the 'timestamp.nanos' field of the raw log.  
timestamp.seconds | read_only_udm.metadata.event_timestamp.seconds | Value is taken from the 'timestamp.seconds' field of the raw log.  
user | read_only_udm.target.user.userid | Value is taken from the 'user' field extracted by either the first or second grok parser.  
| read_only_udm.extensions.auth.mechanism | The value is set to "USERNAME_PASSWORD" if the 'desc' field matches specific patterns related to user login or logout events.  
| read_only_udm.metadata.event_type | The value is determined by a series of conditional statements based on the values of other fields, primarily 'desc', 'src_ip', and 'host'.  
| read_only_udm.metadata.log_type | Hardcoded to "DELL_EMC_DATA_DOMAIN".  
| read_only_udm.metadata.product_name | Hardcoded to "DELL_EMC_DATA_DOMAIN".  
| read_only_udm.metadata.vendor_name | Hardcoded to "DELL".  
| read_only_udm.network.http.method | Value is taken from the 'method' field extracted by the KV filter.  
| read_only_udm.network.http.response_code | Value is taken from the 'response_code' field extracted by the KV filter and converted to an integer.  
| read_only_udm.network.ip_protocol | Value is derived from the 'protocol_number_src' field using a lookup table and the 'parse_ip_protocol.include' configuration.  
| read_only_udm.security_result.severity | The value is set to "MEDIUM" if the 'message' field contains the string "NOTICE".  
| read_only_udm.target.file.sha256 | Value is taken from the 'sha256' field extracted by the second grok parser, converted to lowercase, and validated as a hexadecimal string.  
| read_only_udm.target.process.file.full_path | Value is taken from either the 'path' or 'file' field, depending on which one is not empty.  
| read_only_udm.target.url | Value is taken from the 'uri' field extracted by the KV filter.  
`host` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`host` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`inter_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-emc-data-domain-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
