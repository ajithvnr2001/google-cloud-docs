---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-flexprotect/
title: Collect Imperva FlexProtect logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:44.446983+00:00
---

# Collect Imperva FlexProtect logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-flexprotect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Imperva FlexProtect logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Imperva FlexProtect logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from Imperva FlexProtect syslog formatted logs in CEF (Common Event Format) with key-value extensions. It uses grok and/or kv to parse the CEF message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type. Imperva FlexProtect provides flexible deployment of Imperva security solutions (SecureSphere, Cloud WAF, Bot Protection) across hybrid cloud environments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Imperva FlexProtect management console or individual product consoles



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

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
             customer_id: <CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'IMPERVA_FLEXPROTECT'
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
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



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
            log_type: 'IMPERVA_FLEXPROTECT'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Imperva FlexProtect

### For SecureSphere Component (on-premises/cloud)

  1. Sign in to the **Imperva SecureSphere Management Console**.
  2. Go to **Configuration** > **Action Sets**.
  3. Click **Add** to create a new Action Set.
  4. Click **Add Action** and provide the following configuration details:

     * **Name** : Enter a descriptive name (for example, `Google SecOps Syslog`).
     * **Action Type** : Select **Syslog**.
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (default 514).
     * **Protocol** : Select **UDP** or **TCP**.
     * **Syslog Log Level** : Select **DEBUG**.
     * **Syslog Facility** : Select **LOCAL0**.
     * **Format** : Select **CEF** (Common Event Format).
  5. Save the action configuration and apply it to relevant security policies.




### For Cloud WAF/Incapsula Component

  1. Sign in to the **Imperva Cloud Console**.
  2. Go to **Logs** > **Log Setup**.
  3. Configure syslog destination: 
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (default 514).
     * **Protocol** : Select **UDP** or **TCP**.
     * **Format** : Select **CEF**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
act | read_only_udm.security_result.action_details | Directly mapped from the `act` field.  
app | read_only_udm.network.application_protocol | Directly mapped from the `app` field.  
ccode | read_only_udm.principal.location.country_or_region | Directly mapped from the `ccode` field.  
cicode | read_only_udm.principal.location.city | Directly mapped from the `cicode` field.  
cn1 | read_only_udm.network.http.response_code | Directly mapped from the `cn1` field after converting to integer.  
cs1 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs1` field.  
cs2 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs2` field.  
cs3 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs3` field.  
cs4 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs4` field.  
cs5 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs5` field.  
cs6 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs6` field.  
cs7 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs7` field.  
cs8 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs8` field.  
cs9 | read_only_udm.additional.fields.value.string_value | Directly mapped from the `cs9` field.  
cpt | read_only_udm.principal.port | Directly mapped from the `cpt` field after converting to integer.  
Customer | read_only_udm.principal.user.user_display_name | Directly mapped from the `Customer` field.  
deviceExternalId | read_only_udm.about.asset.asset_id | The value is derived by concatenating "Incapsula.SIEMintegration:" with the `deviceExternalId` field.  
deviceFacility | read_only_udm.principal.location.city | Directly mapped from the `deviceFacility` field.  
dproc | read_only_udm.target.process.command_line | Directly mapped from the `dproc` field.  
end | read_only_udm.security_result.detection_fields.value | Directly mapped from the `end` field.  
fileId | read_only_udm.network.session_id | Directly mapped from the `fileId` field.  
filePermission | read_only_udm.about.resource.attribute.permissions.name | Directly mapped from the `filePermission` field.  
in | read_only_udm.network.received_bytes | Directly mapped from the `in` field.  
qstr | read_only_udm.security_result.detection_fields.value | Directly mapped from the `qstr` field.  
request | read_only_udm.target.url | Directly mapped from the `request` field.  
requestClientApplication | read_only_udm.network.http.user_agent | Directly mapped from the `requestClientApplication` field.  
requestMethod | read_only_udm.network.http.method | Directly mapped from the `requestMethod` field.  
siteid | read_only_udm.security_result.detection_fields.value | Directly mapped from the `siteid` field.  
sip | read_only_udm.target.ip | Directly mapped from the `sip` field.  
sourceServiceName | read_only_udm.principal.application | Directly mapped from the `sourceServiceName` field.  
spt | read_only_udm.target.port | Directly mapped from the `spt` field after converting to integer.  
src | read_only_udm.principal.ip | Directly mapped from the `src` field.  
start | read_only_udm.security_result.detection_fields.value | Directly mapped from the `start` field.  
suid | read_only_udm.principal.user.userid | Directly mapped from the `suid` field.  
ver | read_only_udm.network.tls.version | Directly mapped from the `ver` field.  
| read_only_udm.about.asset.asset_id | The value is derived by concatenating "Incapsula.SIEMintegration:" with the `deviceExternalId` field.  
| read_only_udm.additional.fields.key | Value is determined by the parser logic based on the field's label, for example:   
\- `cs1Label` maps to "Cap Support"   
\- `cs2Label` maps to "Javascript Support"   
\- `cs3Label` maps to "CO Support"   
\- `cs4Label` maps to "VID"   
\- `cs5Label` maps to "clappsig"   
\- `cs6Label` maps to "clapp"   
\- `cs7Label` maps to "latitude"   
\- `cs8Label` maps to "longitude"   
\- `cs9Label` maps to "Rule name"  
| read_only_udm.metadata.event_timestamp.nanos | Directly mapped from the `collection_time.nanos` field.  
| read_only_udm.metadata.event_timestamp.seconds | Directly mapped from the `collection_time.seconds` field.  
| read_only_udm.metadata.event_type | The value is determined based on the presence of `src` and `sip` fields:   
\- If both are present, the value is set to "NETWORK_HTTP".   
\- If only `src` is present, the value is set to "USER_UNCATEGORIZED".   
\- Otherwise, the value is set to "GENERIC_EVENT".  
| read_only_udm.metadata.product_event_type | The value is derived by concatenating "[", the numerical value from the CEF header field at index 4, "] - ", and the text description from the CEF header field at index 4.  
| read_only_udm.metadata.product_name | Value is statically set to "SIEMintegration".  
| read_only_udm.metadata.product_version | Value is statically set to "1".  
| read_only_udm.metadata.vendor_name | Value is statically set to "Incapsula".  
| read_only_udm.security_result.detection_fields.key | Value is statically set to either "siteid", "event_start_time", "event_end_time", or "qstr" based on the corresponding field being processed.  
| read_only_udm.security_result.severity | Value is statically set to "LOW".  
| read_only_udm.target.port | Directly mapped from the `spt` field after converting to integer.  
`qstr` | `security_results.detection_fields` | Mapped from changelog  
`siteid` | `security_results.detection_fields` | Mapped from changelog  
`device_facility` | `principal.location.city` | Mapped from changelog  
`start` | `security_result.detection_fields.event_start_time` | Mapped from changelog  
`cs8Label` | `additional_cs8.key` | Mapped from changelog  
`cs8` | `additional_cs8.value.string_value` | Mapped from changelog  
`cs9Label` | `additional_cs9.key` | Mapped from changelog  
`cs9` | `additional_cs9.value.string_value` | Mapped from changelog  
`end` | `security_result.detection_fields.event_end_time` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-flexprotect-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
