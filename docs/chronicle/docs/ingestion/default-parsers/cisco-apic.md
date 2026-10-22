---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-apic/
title: Collect Cisco APIC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:22.988151+00:00
---

# Collect Cisco APIC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-apic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco APIC logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco APIC logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from Cisco APIC syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco APIC management console



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



## Install Bindplane agent

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

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows: `yaml receivers: udplog: # Replace the port and IP address as required listen_address: "0.0.0.0:514" exporters: chronicle/chronicle_w_labels: protocol: https # Region of your instance, for example us, europe, asia-southeast1 location: <LOCATION> # Project number of the Google Cloud project linked to the instance project: '<PROJECT_NUMBER>' compression: gzip # Adjust the path to the credentials file you downloaded in Step 1 creds_file_path: '/path/to/ingestion-authentication-file.json' # Replace with your actual customer ID from Step 2 customer_id: YOUR_CUSTOMER_ID endpoint: chronicle.googleapis.com # Specify the log type that matches your Chronicle feed configuration # Commonly used: CISCO_ACI or CISCO_APIC depending on your setup log_type: 'CISCO_APIC' raw_log_field: body ingestion_labels: service: pipelines: logs/source0__chronicle_w_labels-0: receivers: - udplog exporters: - chronicle/chronicle_w_labels`


  * Replace the port and IP address as required in your infrastructure: 
    * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
    * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * Replace `YOUR_CUSTOMER_ID` with the actual Customer ID.
    * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.
    * Ensure the `log_type` value matches the Log type selected in your Google SecOps feed configuration.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: YOUR_CUSTOMER_ID
            endpoint: malachiteingestion-pa.googleapis.com
            # Specify the log type that matches your Chronicle feed configuration
            # Commonly used: CISCO_ACI or CISCO_APIC depending on your setup
            log_type: 'CISCO_APIC'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Cisco APIC

### Configure Management Contracts (Troubleshooting)

If syslog messages are not reaching Google SecOps, verify the management access configuration:

  1. Sign in to the **Cisco APIC console**.
  2. Go to **Tenants > mgmt > Security Policies**.
  3. Check that the management contracts allow UDP port 514: 
     * **For Out-of-Band management > ensure the OOB contract permits UDP port 514**.
     * **For In-Band management > ensure the INB contract permits UDP port 514**.
  4. If required, create or modify filters to allow UDP port 514 for the selected management EPG.



### Create Syslog Monitoring Destination Group

  1. Go to **Admin > External Data Collectors > Monitoring Destinations > Syslog**.
  2. Click the **+** sign to **Create Syslog Monitoring Destination Group**.
  3. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps-Syslog`).
     * **Description** : Enter a description (for example, `Syslog destination for Google Security Operations`).
     * **Admin State** : Select **enabled**.
     * **Format** : Select **aci** (recommended) or **nxos**.
  4. Click **Next**.
  5. In the **Create Syslog Remote Destination** section, provide the following configuration details: 
     * **Host Name/IP** : Enter the Bindplane agent IP address.
     * **Name** : Enter a descriptive name for the destination.
     * **Admin State** : Select **enabled**.
     * **Severity** : Select **information** (or your preferred severity level).
     * **Port** : Enter **514** (or the port configured on the Bindplane agent).
     * **Management EPG** : Select appropriate management EPG: 
       * **default (Out-of-Band)** for OOB management
       * **inb-default** for In-Band management
     * **Forwarding Facility** : Select **local7** (or your preferred facility).
  6. Click **OK**.
  7. Review the configuration and click **Finish**.



### Configure syslog sources

Configure syslog sources to send different types of events to the destination group:

#### Configure Fabric Policy Syslog Source

  1. Go to **Fabric > Fabric Policies > Monitoring Policies**.
  2. Expand **default** and select **Callhome/SNMP/Syslog**.
  3. Click the **+** sign to create a syslog source.
  4. Provide the following configuration details: 
     * **Source Name** : Enter a name (for example, `fabric-syslog-source`).
     * **Min Severity** : Select **information**.
     * **Include** : Select **Check All** to include Audit logs, Events, Faults, and Session logs.
     * **Destination Group** : Select the syslog monitoring destination group created earlier.
  5. Click **Submit**.



#### Configure Common Policy Syslog Source

  1. Go to **Fabric > Fabric Policies > Monitoring Policies**.
  2. Expand **common** and select **Callhome/SNMP/Syslog**.
  3. Click **+** to create a syslog source.
  4. Provide the following configuration details: 
     * **Source Name** : Enter a name (for example, `common-syslog-source`).
     * **Min Severity** : Select **information**.
     * **Include** : Select **Check All** to include Audit logs, Events, Faults, and Session logs.
     * **Destination Group** : Select the syslog monitoring destination group created earlier.
  5. Click **Submit**.



#### Configure Access Policy Syslog Source

  1. Go to **Fabric > Access Policies > Monitoring Policies**.
  2. Expand **default** and select **Callhome/SNMP/Syslog**.
  3. Click the **+** sign to create a syslog source.
  4. Provide the following configuration details: 
     * **Source Name** : Enter a name (for example, `access-syslog-source`).
     * **Min Severity** : Select **information**.
     * **Include** : Select **Check All** to include Audit logs, Events, Faults, and Session logs.
     * **Destination Group** : Select the syslog monitoring destination group created earlier.
  5. Click **Submit**.



### Configure System Message Policy (optional)

  1. Go to **Fabric > Fabric Policies > Monitoring Policies**.
  2. Expand **common > System Message Policies**.
  3. Select **Policy for System Syslog Messages**.
  4. Select the **default** facility.
  5. Change **Severity** to **information**.
  6. Click **Update**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`fault_cause_label` | `additional.fields` | Merged  
`ts` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`lifecycle_state` | `metadata.product_event_type` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`prin_ip` | `principal.asset.ip` | Merged  
`host` | `principal.hostname` | Directly mapped  
`prin_ip` | `principal.ip` | Merged  
`mac` | `principal.mac` | Merged  
`desc` | `security_result.description` | Directly mapped  
`severity_detail` | `security_result.severity_details` | Directly mapped  
N/A | `metadata.product_name` | Constant: `CISCO APIC`  
N/A | `metadata.vendor_name` | Constant: `CISCO`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-apic-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
