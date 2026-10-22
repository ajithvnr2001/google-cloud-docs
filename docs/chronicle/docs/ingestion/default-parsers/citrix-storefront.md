---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-storefront/
title: Collect Citrix StoreFront logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:14.531828+00:00
---

# Collect Citrix StoreFront logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-storefront/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Citrix StoreFront logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Citrix StoreFront logs to Google Security Operations using Bindplane.

Citrix StoreFront is a web application that provides an enterprise application store for Citrix virtual desktops and applications. It authenticates users to Citrix Virtual Apps and Desktops sites and aggregates available resources into a single portal. StoreFront writes authentication, session launch, and service events to the Windows Event Log under Citrix-prefixed event sources.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with `systemd`
  * Network connectivity between the Bindplane agent and the internet
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Windows Server hosting Citrix StoreFront
  * Citrix StoreFront 2308 or later installed and configured



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

Install the Bindplane agent on your Windows operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Windows Event Logs and send to Google SecOps

### Locate the configuration file

  1. Open **Command Prompt** as an administrator.
  2. Navigate to the Bindplane agent installation directory and open the configuration file:
         
         notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
         




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          windowseventlog/storefront_application:
            channel: Application
            raw: true
            start_at: end
            operators:
              - type: filter
                expr: 'record["source_name"] matches "^Citrix"'
        
        processors:
          batch:
        
        exporters:
          chronicle/storefront:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds: '{
              "type": "service_account",
              "project_id": "YOUR_PROJECT_ID",
              "private_key_id": "YOUR_PRIVATE_KEY_ID",
              "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
              "client_email": "YOUR_CLIENT_EMAIL",
              "client_id": "YOUR_CLIENT_ID",
              "auth_uri": "https://accounts.google.com/o/oauth2/auth",
              "token_uri": "https://oauth2.googleapis.com/token",
              "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
              "client_x509_cert_url": "YOUR_CERT_URL"
            }'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: 'CITRIX_STOREFRONT'
            override_log_type: false
            raw_log_field: body
        
        service:
          pipelines:
            logs/storefront:
              receivers:
                - windowseventlog/storefront_application
              processors:
                - batch
              exporters:
                - chronicle/storefront
        




### Configuration parameters

Replace the following placeholders with your actual values:

  * **Exporter configuration:**

    * `YOUR_PROJECT_ID`: The project ID from your ingestion authentication file
    * `YOUR_PRIVATE_KEY_ID`: The private key ID from your ingestion authentication file
    * `YOUR_PRIVATE_KEY`: The private key from your ingestion authentication file (ensure proper escaping of newlines)
    * `YOUR_CLIENT_EMAIL`: The client email from your ingestion authentication file
    * `YOUR_CLIENT_ID`: The client ID from your ingestion authentication file
    * `YOUR_CERT_URL`: The client x509 certificate URL from your ingestion authentication file
    * `YOUR_CUSTOMER_ID`: Your Google SecOps customer ID
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.


**Note:** Instead of manually editing the `creds` field, you can save the service account JSON key file (Option 1) to a secure location and reference it using `creds_file_path`:

  * Example:
        
        exporters:
          chronicle/storefront:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: 'CITRIX_STOREFRONT'
            override_log_type: false
            raw_log_field: body
        




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/storefront:
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'CITRIX_STOREFRONT'
            override_log_type: false
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * Click **File > Save**
    * Close Notepad



## Restart the Bindplane agent to apply the changes

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
         




## Configure Citrix StoreFront event logging

By default, StoreFront 2311 and later versions log messages of level Error, Warning, and Info. For earlier versions (2308 and below), only Error-level messages are logged by default.

### Enable verbose logging (optional)

To increase the logging detail for troubleshooting purposes:

  1. Sign in to the **StoreFront server** with local administrator privileges.
  2. Open **PowerShell** as an administrator.
  3. Run the following command to enable verbose logging for all services:
         
         Set-STFDiagnostics -All -TraceLevel "Verbose" -confirm:$False
         

**Note:** If using StoreFront 2311 or later, you must add the `-Override` parameter.**Note:** This command restarts StoreFront services. Wait for the PowerShell prompt to return before continuing. While services are restarting, the StoreFront server will not be accessible to users.
  4. After troubleshooting, revert the logging level to default:
         
         Set-STFDiagnostics -All -TraceLevel "Info" -confirm:$False
         

**Note:** If using StoreFront 2311 or later, you must add the `-Override` parameter.



### Verify Windows Event Log events

  1. Press `Win+R`, type `eventvwr.msc`, and press Enter to open **Event Viewer**.
  2. Navigate to **Application and Services Logs > Citrix Delivery Services**.
  3. Verify that events are being logged for authentication, stores, and Receiver for Web sites.
  4. Navigate to **Windows Logs > Application**.
  5. Filter events by source names starting with **Citrix** to verify application-level events are being generated.



### Configure event log throttling (optional)

StoreFront supports event log throttling to limit the number of duplicate events. To configure throttling:

  1. Navigate to the StoreFront service configuration directories on the server: 
     * Authentication service: `C:\inetpub\wwwroot\Citrix\Authentication`
     * Store: `C:\inetpub\wwwroot\Citrix\<storename>`
     * Receiver for Web site: `C:\inetpub\wwwroot\Citrix\<storename>\Web`
  2. Open the `web.config` file in each directory using a text editor.
  3. Locate the `logger` element and configure the throttling parameters:
         
         <logger duplicateInterval="00:01:00" duplicateLimit="10">
         

     * `duplicateInterval`: The time period (hours:minutes:seconds) over which duplicate log entries are monitored
     * `duplicateLimit`: The number of duplicate entries that must be logged within the interval to trigger throttling
  4. Save the configuration files.




For more information, see the [Citrix StoreFront log files documentation](https://docs.citrix.com/en-us/storefront/current-release/logs-analytics/log-files.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`OpcodeValue_label` | `additional.fields` | Merged  
`Opcode_label` | `additional.fields` | Merged  
`ThreadID_label` | `additional.fields` | Merged  
`X-Citrix-Via_label` | `additional.fields` | Merged  
`XCitrixGateway_label` | `additional.fields` | Merged  
`keyword_label` | `additional.fields` | Merged  
`_vulns` | `extensions.vulns.vulnerabilities` | Merged  
`_intermediary` | `intermediary` | Merged  
`_intermediary_controller` | `intermediary` | Merged  
`_intermediary_hypervisor` | `intermediary` | Merged  
`_intermediary_storefront` | `intermediary` | Merged  
`description` | `metadata.description` | Directly mapped  
`EventTime` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`Machine.CreatedDate` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`Machine.LastDeregisteredDate` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`Machine.ModifiedDate` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`Machine.PoweredOnDate` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`Machine.RegistrationStateChangeDate` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`Session.EndDate` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`Session.StartDate` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`event_date` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`EventID` | `metadata.product_event_type` | Directly mapped  
`RecordNumber` | `metadata.product_log_id` | Directly mapped  
`Machine.AgentVersion` | `metadata.product_version` | Renamed/mapped  
`_network` | `network` | Renamed/mapped  
`_principal` | `principal` | Renamed/mapped  
`Channel_label` | `security_result.about.resource.attribute.labels` | Merged  
`severity` | `security_result.severity` | Mapped: `(?i)Info` → `INFORMATIONAL`, `(?i)Error` → `ERROR`, `(?i)Warning` → `MEDIUM`  
`SeverityValue` | `security_result.severity_details` | Directly mapped  
`Connection.ConnectedViaHostName` | `src.hostname` | Directly mapped  
`_target` | `target` | Renamed/mapped  
N/A | `extensions.auth.auth_details` | Constant: `ACTIVE`  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `Monitor Service OData`  
N/A | `metadata.vendor_name` | Constant: `Citrix`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
`OpcodeValue","X-Citrix-Via","ThreadID","XCitrixGateway","Opcode","Keywords", "OpcodeValue` | `additional.fields` | Mapped from changelog  
`X-Citrix-Via-VIP` | `_target.ip` | Mapped from changelog  
`Remoteadresse` | `taregt.ip` | Mapped from changelog  
`invalid_X-Forwarded-For` | `_principal.ip` | Mapped from changelog  
`Task` | `_target.resource.type` | Mapped from changelog  
`Hostname` | `_principal.hostname` | Mapped from changelog  
`SourceModuleName` | `target.resource.name` | Mapped from changelog  
`SourceModuleType` | `_principal.resource.attribute.labels` | Mapped from changelog  
`Machine.AssociatedUserUPNs` | `target.group.email_addresses` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-storefront-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
