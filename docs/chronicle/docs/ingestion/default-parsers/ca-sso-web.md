---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-sso-web/
title: Collect Broadcom SiteMinder Web Access Management (formerly CA SSO) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:33.489621+00:00
---

# Collect Broadcom SiteMinder Web Access Management (formerly CA SSO) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-sso-web/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Broadcom SiteMinder Web Access Management (formerly CA SSO) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Broadcom SiteMinder Web Access Management (formerly known as CA SSO) logs to Google Security Operations using Bindplane. The parser transforms raw JSON formatted logs into a structured Unified Data Model (UDM). It extracts fields from the raw log messages using grok patterns, renames and maps them to the UDM schema, handles different event types and user formats, and enriches the data for security analysis.

Broadcom SiteMinder Web Access Management is an enterprise web access management solution that provides centralized authentication, authorization, and single sign-on (SSO) for web applications. SiteMinder uses a Policy Server to enforce security policies and manage user sessions across web resources, generating detailed audit logs of authentication events, authorization decisions, and session activity.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open.
  * Privileged access to the Broadcom SiteMinder Policy Server Management Console.
  * An X-windows server running on the system where the Policy Server Management Console will be launched (for Linux-based Policy Servers).



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

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

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
             log_type: 'CA_SSO_WEB'
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
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



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
            log_type: 'CA_SSO_WEB'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Configure Syslog on Broadcom SiteMinder Policy Server (version 12.8)

  1. Verify that an **X-windows server** is running on your system.
  2. Open a terminal window.
  3. Set the **DISPLAY** variable with the following command:
         
         export DISPLAY=<IP_ADDRESS>:0.0
         

**Note:** Replace `<IP_ADDRESS>` with the IP address of the system from which you are connecting to the console (for example, `192.168.1.100`).
  4. Sign in to the system hosting the Policy Server Management Console.

  5. Go to the `<installation_directory>/siteminder/bin` directory.

     * Replace `<installation_directory>` with the location in the file system where the **Policy Server** is installed (for example, `/opt/CA/siteminder`).
  6. Open the console by running the following command:
         
         ./smconsole
         

  7. Click the **Data** tab.

  8. Click the **Database** drop-down list, and then select **Audit Logs**.

  9. Click the **Storage** drop-down list, and then select **Syslog**.

  10. Select the value **LOG_INFO** in the **Priority** field.

  11. Select the value **LOG_LOCAL0** in the **Facility** field.

  12. Click **OK**.




## Configure syslog forwarding to the Bindplane agent

After enabling syslog on the SiteMinder Policy Server, configure your syslog daemon to forward the SiteMinder audit logs to the Bindplane agent.

  1. Open the syslog configuration file on the Policy Server host:
         
         sudo nano /etc/rsyslog.conf
         

  2. Add the following line to forward **LOCAL0** facility logs to the Bindplane agent:
         
         local0.*    @@<BINDPLANE_IP>:514
         

**Note:** Replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent host. The `@@` prefix specifies TCP transport. Use `@` for UDP transport.
  3. Save the file and restart the syslog service:
         
         sudo systemctl restart rsyslog
         




## Restart the SiteMinder Policy Server

  1. Sign in to the system hosting the Policy Server with the same user account that installed the Policy Server originally.
  2. Open the Management Console.
  3. Click the **Status** tab, and then click the **Stop** buttons.
  4. Wait for all services to stop.
  5. In the same **Status** tab, click the **Start** buttons.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Action` | `event1.idm.read_only_udm.network.http.method` | If the Action field is not empty, it is mapped to `network.http.method`. If the value is `Visit` it is replaced with `GET`.  
| `event1.idm.read_only_udm.metadata.product_name` | Set to `Web Access Management` in the parser code.  
| `event1.idm.read_only_udm.metadata.vendor_name` | Set to `Siteminder` in the parser code.  
| `event1.idm.read_only_udm.observer.hostname` | Set to the value of `logstash.collect.host`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-sso-web-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
