---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-central/
title: Collect Sophos Central logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:39.697794+00:00
---

# Collect Sophos Central logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-central/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Sophos Central logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Sophos Central logs by using Bindplane. The parser transforms JSON logs into a unified data model (UDM). It extracts fields from nested JSON structures, maps them to UDM fields, and performs event categorization based on the type field, enriching the data with specific details and actions for different Sophos Central event types.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * You are using Windows 2016 or later, or a Linux host with systemd.
  * You have an additional Windows or Linux machine, capable of continuously running Python.
  * If running behind a proxy, make sure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Sophos Central Admin console.



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

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

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
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'SOPHOS_CENTRAL'
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

  6. Replace `<customer_id>` with the actual **Customer ID**.

  7. Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'SOPHOS_CENTRAL'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         /opt/observiq-otel-collector/config.yaml
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop BindPlaneAgent && net start BindPlaneAgent
         




## Configure Sophos Central API access

  1. Sign in to **Sophos Central Admin**.
  2. Select **Global Settings** > **API Token Management**.
  3. Click **Add Token** to create a new token.
  4. Enter a token name and click **Save**. The **API Token Summary** for the provided token is displayed.
  5. In the **API Token Summary** section, click **Copy** to copy the API access URL and headers.



## Install Python on the additional machine

  1. Open the web browser and go to the [Python website](https://www.python.org).
  2. Click **Download Python** for your operating system (Windows or Mac).
  3. Install Python:

     * On Windows: 
       1. Run the installer.
       2. Check the box that says **Add Python to PATH**.
       3. Click **Install Now**.
     * On Mac: 
       1. Python may already be installed; if not, you can install the latest version using the terminal.
       2. Open **Terminal** and type the following command to verify:
    
    python --version
    




## Download the Sophos integration script

  1. Go to the GitHub page for the [Sophos Central SIEM Integration Repository](https://github.com/sophos/Sophos-Central-SIEM-Integration).
  2. Click the green **Code button** > **Download ZIP**.
  3. Extract the ZIP file.



## Set up the script configuration

  1. Find and open the `config.ini` file with a text editor.
  2. Edit the configuration file: 
     * **API Token:** Enter the API Key copied earlier from Sophos Central.
     * **Syslog Server Details:** Enter the details of your syslog server.
     * **Host:** Enter the Bindplane IP address.
     * **Port:** Enter the Bindplane port number.
     * **Protocol:** Enter **UDP** (you can also use **TCP** or **TLS** depending on your setup).
  3. **Save** the file.



## Run the script

  1. Go to the script folder. 
     * On Windows: 
       1. Press the **Windows** key and type `cmd`.
       2. Click **Command Prompt**.
       3. Navigate to the folder: `cmd cd C:\Users\YourName\Downloads\Sophos-Central-SIEM-Integration`
     * On macOS: 
       1. Go to **Applications** > **Utilities**.
       2. Open **Terminal**.
       3. Navigate to the folder: `bash cd /Users/YourName/Downloads/Sophos-Central-SIEM-Integration`
  2. Run the script:

     * Type the following command to start the script:
    
    python siem.py
    

**Note:** The script will start fetching logs from Sophos Central and forwarding them to your syslog server in JSON format.



## Automate the script to run continuously

### On Windows (using Task Scheduler)

  1. Open the **Task Scheduler** by typing "Task Scheduler" in the Start menu.
  2. Click **Create Task**.
  3. In the **General** tab: 
     * Name your task (e.g., `Sophos Central Log Export`).
  4. In the **Triggers** tab: 
     * Click **New** and set the task to run **Daily** or **At startup**.
  5. In the **Actions** tab: 
     * Click **New** and select **Start a program**.
     * Browse for the `python.exe` executable (usually found at `C:\PythonXX\python.exe`).
     * In the **Add arguments** field, type the path to the script (e.g., `C:\Users\YourName\Downloads\Sophos-Central-SIEM-Integration\siem.py`).
  6. Click **OK** to save the task.



### On Mac (using Cron Jobs)

  1. Open the **Terminal**.
  2. Type `crontab -e` and press **Enter**.
  3. Add a new line at the end of the file:
         
         * * * * * /usr/bin/python /Users/YourName/Downloads/Sophos-Central-SIEM-Integration/siem.py
         

**Note:** This will run the script **every minute**. Adjust the time based on your needs.
  4. **Save** and exit the editor.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`created_at_label` | `additional.fields` | Merged  
`datastream_label` | `additional.fields` | Merged  
`security_result.description` | `metadata.description` | Renamed/mapped  
`end` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`when` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `FILE_OPEN`, `true` → `NETWORK_CONNECTION`, `true` → `SCAN_UNCATEGORIZED`  
`type` | `metadata.event_type` | Mapped values (14 total, e.g. `Event::Endpoint::DataLossPreventionAutomaticallyAllowed` → `F...  
`type` | `metadata.product_event_type` | Directly mapped  
`type` | `network.direction` | Mapped: `Event::Endpoint::WebControlViolation` → `OUTBOUND`, `Event::Endpoint::WindowsFirewa...  
`type` | `network.ip_protocol` | Mapped: `Event::Endpoint::WebControlViolation` → `TCP`  
`dhost` | `principal.asset.hostname` | Directly mapped  
`location` | `principal.asset.hostname` | Directly mapped  
`data.source_info.ip` | `principal.asset.ip` | Merged  
`source_info.ip` | `principal.asset.ip` | Merged  
`dhost` | `principal.hostname` | Directly mapped  
`location` | `principal.hostname` | Directly mapped  
`data.source_info.ip` | `principal.ip` | Merged  
`source_info.ip` | `principal.ip` | Merged  
`type` | `principal.user.attribute.labels` | Mapped: `Event::Endpoint::DataLossPreventionAutomaticallyAllowed` → `username_label`  
`username_label` | `principal.user.attribute.labels` | Merged  
`Username` | `principal.user.user_display_name` | Directly mapped  
`source` | `principal.user.user_display_name` | Directly mapped  
`source` | `principal.user.userid` | Directly mapped  
`suser` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`endpoint_type_label` | `security_result.about.labels` | Merged  
`sec_action` | `security_result.action` | Merged  
`type` | `security_result.action` | Mapped: `Event::Endpoint::DataLossPreventionAutomaticallyAllowed` → `sec_action`, `Event::En...  
`group` | `security_result.category_details` | Merged  
`name` | `security_result.description` | Directly mapped  
`type` | `security_result.description` | Mapped: `Event::Endpoint::(UpdateRebootRequired/ServiceNotRunning/NonCompliant/OutOfDate)` →...  
`duid_label` | `security_result.detection_fields` | Merged  
`id_label` | `security_result.detection_fields` | Merged  
`rule` | `security_result.rule_name` | Directly mapped  
`rules` | `security_result.rule_name` | Directly mapped  
`severity` | `security_result.severity` | Mapped: `low` → `LOW`, `medium` → `MEDIUM`, `high` → `HIGH`  
`security_result.description` | `security_result.summary` | Renamed/mapped  
`app` | `target.application` | Directly mapped  
`application` | `target.application` | Directly mapped  
`dhost` | `target.asset.hostname` | Directly mapped  
`endpoint_id` | `target.asset_id` | Directly mapped  
`f_path` | `target.file.full_path` | Directly mapped  
`f_size` | `target.file.size` | Renamed/mapped  
`dhost` | `target.hostname` | Directly mapped  
`application` | `target.process.file.full_path` | Directly mapped  
`core_remedy_items.items.0.descriptor` | `target.process.file.full_path` | Directly mapped  
`data.core_remedy_items.items.0.descriptor` | `target.process.file.full_path` | Directly mapped  
`file_path_1` | `target.process.file.full_path` | Directly mapped  
`customer_id` | `target.resource.id` | Directly mapped  
`p_device` | `target.resource.name` | Directly mapped  
`scan_name` | `target.resource.name` | Directly mapped  
`type` | `target.resource.name` | Mapped: `Event::Endpoint::SavDisabled` → `Real time protection`, `Event::Endpoint::Registere...  
`type` | `target.resource.type` | Mapped values (5 total, e.g. `Event::Endpoint::SavDisabled` → `SETTING`, `Event::Endpoint::R...  
`url` | `target.url` | Directly mapped  
`principal.user.userid` | `target.user.userid` | Directly mapped  
`suser` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `Sophos Central`  
N/A | `metadata.vendor_name` | Constant: `Sophos`  
N/A | `network.direction` | Constant: `OUTBOUND`  
N/A | `network.ip_protocol` | Constant: `TCP`  
N/A | `security_result.description` | Constant: `security_result.summary`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `target.resource.name` | Constant: `Real time protection`  
N/A | `target.resource.type` | Constant: `SETTING`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-central-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
