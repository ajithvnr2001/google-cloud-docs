---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-emailsecurity/
title: Collect Forcepoint Email Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:08.842912+00:00
---

# Collect Forcepoint Email Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-emailsecurity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Forcepoint Email Security logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Forcepoint Email Security logs to Google Security Operations using BindPlane. The parser first extracts fields from the JSON-formatted logs and initializes some UDM fields with empty values. Then, it maps the extracted fields to their corresponding fields within the Chronicle UDM structure based on specific conditions and data manipulations, ultimately creating a unified representation of the email security event. 

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the BindPlane agent requirements
  * Privileged access to the Forcepoint Email Security appliance or management console



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
  3. Copy and save the **customer ID** from the **Organization Details** section.



## Install BindPlane Agent

Install the BindPlane agent on your Windows or Linux operating system according to the following instructions.

### Windows Installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux Installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional Installation Resources

  * For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).
  * **Alternative:** You can also use the [BindPlane OP managed installation workflow](https://docs.bindplane.com/deployment/virtual-machine/collector/install-and-uninstall-bindplane-collectors) for centralized agent management.

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure BindPlane Agent to ingest Syslog and send to Google SecOps

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
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'FORCEPOINT_EMAILSECURITY'
             raw_log_field: body
             ingestion_labels:
         
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

  6. Replace `<CUSTOMER_ID>` with the actual Customer ID.

  7. Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'FORCEPOINT_EMAILSECURITY'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart BindPlane Agent to apply the changes

  1. To restart the BindPlane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the BindPlane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Forcepoint Email Security

  1. Sign in to the **Forcepoint Email Security Management Console**.
  2. Go to **Settings > Integrations > SIEM Integration**.
  3. Click **Enable SIEM Integration**.
  4. Provide the following configuration details:

     * **Format** : Select **LEEF** (Log Event Extended Format).
     * **Syslog Server** : Enter the BindPlane Agent IP address.
     * **Syslog Port** : Enter the BindPlane Agent port number (for example, `514`).
     * **Protocol** : Select **UDP** or **TCP** , depending on your actual BindPlane Agent configuration.
     * **Facility** : Select the syslog facility code (for example, `Local0`).
     * **Severity** : Select the severity level for log events.
  5. Click **Save**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
Action | security_result.action_details | Directly mapped from the "Action" field in the raw log.  
AttachmentFilename | additional.fields.value.list_value.values.string_value (key: Attachments_FileNames) | The "AttachmentFilename" field is split by comma and then each value is added as a string_value to the "additional.fields" array with the key "Attachments_FileNames".  
AttachmentFileType | additional.fields.value.list_value.values.string_value (key: AttachmentsFileType) | The "AttachmentFileType" field is split by comma and then each value is added as a string_value to the "additional.fields" array with the key "AttachmentsFileType".  
AttachmentSize | additional.fields.value.list_value.values.string_value (key: AttachmentsSize) | The "AttachmentSize" field is split by comma and then each value is added as a string_value to the "additional.fields" array with the key "AttachmentsSize".  
DateTime |  | Not mapped in the provided UDM.  
EnvelopeSender | network.email.from | Directly mapped from the "EnvelopeSender" field in the raw log.  
EventReceivedTime | metadata.event_timestamp | Parsed to a timestamp format and mapped to "metadata.event_timestamp".  
FilteringReason | security_result.category_details | Directly mapped from the "FilteringReason" field in the raw log.  
MessageSandboxing | security_result.detection_fields.value (key: MessageSandboxing) | Directly mapped from the "MessageSandboxing" field in the raw log and added as a key-value pair to the "security_result.detection_fields" array.  
MessageSize | security_result.detection_fields.value (key: MessageSize) | Directly mapped from the "MessageSize" field in the raw log and added as a key-value pair to the "security_result.detection_fields" array.  
nxlog_filename | additional.fields.value.string_value (key: nxlog_filename) | Directly mapped from the "nxlog_filename" field in the raw log and added as a key-value pair to the "additional.fields" array.  
RecipientAddress | network.email.to | Directly mapped from the "RecipientAddress" field in the raw log.  
SenderIP | principal.asset.ip, principal.ip | Directly mapped from the "SenderIP" field in the raw log.  
SenderIPCountry | principal.location.country_or_region | Directly mapped from the "SenderIPCountry" field in the raw log.  
SourceModuleName | principal.resource.attribute.labels.value (key: SourceModuleName) | Directly mapped from the "SourceModuleName" field in the raw log and added as a key-value pair to the "principal.resource.attribute.labels" array.  
SourceModuleType | principal.resource.attribute.labels.value (key: SourceModuleType) | Directly mapped from the "SourceModuleType" field in the raw log and added as a key-value pair to the "principal.resource.attribute.labels" array.  
SpamScore | security_result.detection_fields.value (key: SpamScore) | Directly mapped from the "SpamScore" field in the raw log and added as a key-value pair to the "security_result.detection_fields" array.  
Subject | network.email.subject | Directly mapped from the "Subject" field in the raw log.  
VirusName | security_result.detection_fields.value (key: VirusName) | Directly mapped from the "VirusName" field in the raw log and added as a key-value pair to the "security_result.detection_fields" array.  
| metadata.event_type | The value is determined based on the presence of other fields. If "has_network_email_data" is true, the value is set to "EMAIL_TRANSACTION". If "has_principal" is true, the value is set to "STATUS_UPDATE". Otherwise, it defaults to "GENERIC_EVENT".  
| metadata.product_name | The value is set to "FORCEPOINT EMAILSECURITY".  
| metadata.vendor_name | The value is set to "FORCEPOINT EMAILSECURITY".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-emailsecurity-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
