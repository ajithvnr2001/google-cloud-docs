---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kemp-loadbalancer/
title: Collect Kemp Load Balancer logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:06.009458+00:00
---

# Collect Kemp Load Balancer logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kemp-loadbalancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Kemp Load Balancer logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Progress Kemp LoadMaster logs to Google Security Operations using the Bindplane agent.

Progress Kemp LoadMaster (formerly Kemp Load Balancer) is an application delivery controller (ADC) that provides load balancing, SSL offloading, and traffic management for enterprise applications. It distributes incoming traffic across multiple servers to ensure high availability, optimize performance, and enhance the security of web-based applications and services.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Progress Kemp LoadMaster web user interface (WUI)



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



## Install Bindplane Agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows Installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux Installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional Installation Resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane Agent to ingest Syslog and send to Google SecOps

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
               customer_id: YOUR_CUSTOMER_ID_HERE
               endpoint: chronicle.googleapis.com
               # Add optional ingestion labels for better organization
               log_type: 'KEMP_LOADBALANCER'
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

  4. Replace `YOUR_CUSTOMER_ID_HERE` with the actual Customer ID.

  5. Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.

  6. Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

  7. Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: YOUR_CUSTOMER_ID_HERE
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'KEMP_LOADBALANCER'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart Bindplane Agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Progress Kemp LoadMaster syslog forwarding

  1. Sign in to the **Progress Kemp LoadMaster** web user interface (WUI).
  2. Go to **System Configuration > Logging Options > Syslog Options**.
  3. In the **Remote Syslog Host** field, enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
  4. In the **Remote Syslog Port** field, enter `514` (or the port configured in Bindplane).
  5. Set the **Info Syslog Messages** option to **Yes** to enable informational log messages.
  6. Set the **Warning Syslog Messages** option to **Yes** to enable warning messages.
  7. Set the **Error Syslog Messages** option to **Yes** to enable error messages.
  8. Set the **Critical Syslog Messages** option to **Yes** to enable critical messages.
  9. Set the **Emergency Syslog Messages** option to **Yes** to enable emergency messages.
  10. Click **Set Syslog Parameters** to save the configuration.
  11. To enable WAF syslog logging, go to **System Configuration > Logging Options > WAF Syslog Options**.
  12. Set the **Remote Syslog** option to **Yes**.
  13. Click **Set WAF Syslog Parameters** to save.

**Note:** For more information, see the [Progress Kemp LoadMaster documentation](https://support.kemptechnologies.com/hc/en-us/articles/202040805-Syslog-for-the-LoadMaster).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`hlen_label` | `additional.fields` | Merged  
`meta_sequenceId_label` | `additional.fields` | Merged  
`nhdrs_label` | `additional.fields` | Merged  
`intermediary` | `intermediary` | Merged  
`inter_hostname` | `intermediary.hostname` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`event_type` | `metadata.event_type` | Renamed/mapped  
`log_event` | `metadata.product_event_type` | Directly mapped  
`sequenceId` | `metadata.product_log_id` | Directly mapped  
`ftpmethod` | `network.ftp.command` | Directly mapped  
`http_method` | `network.http.method` | Directly mapped  
`http_response_code` | `network.http.response_code` | Directly mapped  
`process_name` | `principal.application` | Directly mapped  
`src_ip` | `principal.ip` | Merged  
`srcip` | `principal.ip` | Merged  
`src_port` | `principal.port` | Directly mapped  
`srcport` | `principal.port` | Directly mapped  
`sec_result` | `security_result` | Merged  
`sshd` | `target.application` | Directly mapped  
`filename` | `target.file.full_path` | Directly mapped  
`file_size` | `target.file.size` | Renamed/mapped  
`dest_ip` | `target.ip` | Merged  
`dstip` | `target.ip` | Merged  
`vs` | `target.ip` | Merged  
`dest_port` | `target.port` | Directly mapped  
`dstport` | `target.port` | Directly mapped  
`vs_port` | `target.port` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`http_path` | `target.url` | Directly mapped  
`resource` | `target.url` | Directly mapped  
`user` | `target.user.userid` | Directly mapped  
N/A | `additional.fields` | Constant: `meta_sequenceId_label`  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `intermediary` | Constant: `intermediary`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `KEMP_LOADBALANCER`  
N/A | `metadata.vendor_name` | Constant: `KEMP`  
N/A | `network.application_protocol` | Constant: `HTTP`  
N/A | `principal.ip` | Constant: `src_ip`  
N/A | `security_result` | Constant: `sec_result`  
N/A | `target.ip` | Constant: `dest_ip`  
`meta_sequenceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_type` | `USER_UNCATEGORIZED` | Mapped from changelog  
  
For more information about the parser field mapping, see the [KEMP_LOADBALANCER parser reference](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kemp-loadbalancer).

## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kemp-loadbalancer-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
