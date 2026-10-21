---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-cef/
title: Collect Imperva CEF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:16:39.779461+00:00
---

# Collect Imperva CEF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-cef/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Imperva CEF logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Imperva CEF logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from Imperva syslog formatted logs in CEF (Common Event Format). It uses grok and/or kv to parse the CEF message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Imperva management console or appliance



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
             log_type: 'IMPERVA_CEF'
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
            log_type: 'IMPERVA_CEF'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Imperva WAF Gateway (SecureSphere) to send CEF over syslog

  1. In the MX console, create an Action Set:

     * Navigate to **Policies > Action Sets**.
     * Click **New** and name it (for example, `Google SecOps CEF`).
  2. Add the CEF syslog Action Interface:

     * In **Available Action Interfaces** , open **System Log** and add one or more of the following (as needed): 
       * **Log Security Event to System Log (syslog) using the CEF standard**
       * **Log Network Security Event to System Log (syslog) using the CEF standard**
       * **Log System Event to System Log (syslog) using the CEF standard**
       * **Log Custom Security Event to System Log (syslog) using the CEF standard**
  3. Configure Action Interface parameters:

     * **Syslog Host** : Enter your Bindplane agent IP address. To use a non-default port, append `:PORT` (default is 514 if you don't specify one). Example: `10.0.0.10:514`.
     * **Facility** / **Log Level** : Set per your policy requirements.
     * **Message** : Leave vendor defaults for CEF unless you have a custom mapping.
  4. Attach the Action Set to policies:

     * For **Security / Network Security** events: Open the relevant policy(ies) and set **Followed Action** to your Action Set.
     * For **System Events** : Create or verify a **System Events** policy and set **Followed Action** to your Action Set so those events are also sent via CEF.
  5. (Optional) Configure gateway-specific targets:

     * If different gateway groups must send to different syslog servers, configure each **Gateway Group > External Logger** and enable **"Use gateway configuration if exists"** in the policy.
**Note:** For Imperva Cloud WAF (Incapsula), the configuration differs. Cloud WAF provides **Log Integration** (pull or push of log files) using API or designated storage, not direct syslog from the portal. Consult Imperva documentation for Cloud WAF log export options.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`act` | `security_result.action` | Derived. If `act` is "allowed", "alert", starts with "REQ_PASSED", or starts with "REQ_CACHED", then `action` is "ALLOW". If `act` is "deny", "blocked", starts with "REQ_BLOCKED", or starts with "REQ_CHALLENGE", then `action` is "BLOCK". If `act` matches regex `(?i)REQ_BAD`, then `action` is "FAIL". Otherwise, `action` is "UNKNOWN_ACTION". `security_result.action` is then set to the value of `action`.  
`act` | `security_result.action_details` | Derived. Based on the value of `act`, a detailed description is generated. Examples: "REQ_CACHED_FRESH: response was returned from the data center's cache", "REQ_BLOCKED: the request was blocked".  
`app` | `network.application_protocol` | Directly mapped after being converted to uppercase.  
`cs1` | `security_result.detection_fields.value` | Conditionally mapped if `cs1` is not empty or "NA". `security_result.detection_fields.key` is set to the value of `cs1Label`.  
`cs1Label` | `security_result.detection_fields.key` | Conditionally mapped if `cs1` is not empty or "NA". `security_result.detection_fields.value` is set to the value of `cs1`.  
`cs2` | `security_result.detection_fields.value` | Conditionally mapped if not empty. `security_result.detection_fields.key` is set to the value of `cs2Label`.  
`cs2Label` | `security_result.detection_fields.key` | Conditionally mapped if `cs2` is not empty. `security_result.detection_fields.value` is set to the value of `cs2`.  
`cs3` | `security_result.detection_fields.value` | Conditionally mapped if not empty or "-". `security_result.detection_fields.key` is set to the value of `cs3Label`.  
`cs3Label` | `security_result.detection_fields.key` | Conditionally mapped if `cs3` is not empty or "-". `security_result.detection_fields.value` is set to the value of `cs3`.  
`cs4` | `security_result.detection_fields.value` | Conditionally mapped if not empty. `security_result.detection_fields.key` is set to the value of `cs4Label`.  
`cs4Label` | `security_result.detection_fields.key` | Conditionally mapped if `cs4` is not empty. `security_result.detection_fields.value` is set to the value of `cs4`.  
`cs5` | `security_result.detection_fields.value` | Conditionally mapped if not empty. `security_result.detection_fields.key` is set to the value of `cs5Label`.  
`cs5Label` | `security_result.detection_fields.key` | Conditionally mapped if `cs5` is not empty. `security_result.detection_fields.value` is set to the value of `cs5`.  
`cs6` | `security_result.detection_fields.value` | Conditionally mapped if not empty. `security_result.detection_fields.key` is set to the value of `cs6Label`.  
`cs6Label` | `security_result.detection_fields.key` | Conditionally mapped if `cs6` is not empty. `security_result.detection_fields.value` is set to the value of `cs6`.  
`cs7` | `principal.location.region_latitude` | Conditionally mapped if `cs7Label` is "latitude".  
`cs8` | `principal.location.region_longitude` | Conditionally mapped if `cs8Label` is "longitude".  
`cn1` | `security_result.detection_fields.value` | Conditionally mapped if not empty and `cn1Label` is not empty. `security_result.detection_fields.key` is set to the value of `cn1Label`.  
`cn1Label` | `security_result.detection_fields.key` | Conditionally mapped if `cn1` and `cn1Label` are not empty. `security_result.detection_fields.value` is set to the value of `cn1`.  
`fileType` | `security_result.detection_fields.value` | Conditionally mapped if not empty. `security_result.detection_fields.key` is set to "fileType".  
`filePermission` | `security_result.detection_fields.value` | Conditionally mapped if not empty. `security_result.detection_fields.key` is set to "filePermission".  
`request` | `target.url` | Directly mapped.  
`requestClientApplication` | `network.http.user_agent` | Conditionally mapped if not empty. Overwrites the value mapped from the `user_agent` field extracted from the `requestContext` or `requestClientApplication` key-value pairs in the CEF payload.  
`requestMethod` | `network.http.method` | Directly mapped.  
`siteid` | `security_result.detection_fields.value` | Conditionally mapped if not empty. `security_result.detection_fields.key` is set to "siteid".  
`sourceServiceName` | `target.hostname` | Directly mapped. Overwrites the value of `dhost` if present.  
`src` | `principal.ip` | Directly mapped.  
`start` | `metadata.event_timestamp.seconds` | Extracted using a grok pattern and converted to a timestamp. Used as a fallback for `deviceReceiptTime` if it's not present. If both `deviceReceiptTime` and `start` are empty, the log timestamp is used.  
`suid` | `principal.user.userid` | Conditionally mapped if not empty.  
N/A | `metadata.event_type` | Hardcoded to "NETWORK_HTTP".  
N/A | `metadata.log_type` | Directly mapped from the top-level `log_type` field.  
N/A | `metadata.product_event_type` | Mapped from `csv.event_id` if not empty.  
N/A | `metadata.product_name` | Hardcoded to "Web Application Firewall".  
N/A | `metadata.vendor_name` | Hardcoded to "Imperva".  
`kv.act` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`kv.sourceServiceName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`cicode` | `event.idm.read_only_udm.principal.location.city` | Mapped from changelog  
`ccode` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`Customer` | `event.idm.read_only_udm.network.organization_name` | Mapped from changelog  
`tls_cipher` | `event.idm.read_only_udm.network.tls.cipher` | Mapped from changelog  
`cpt` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`fileId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`dproc` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`deviceFacility` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`deviceExternalId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`end` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-cef-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
