---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-sso-web/
title: Collect Broadcom SiteMinder Web Access Management (formerly CA SSO) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:35.456203+00:00
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

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
         tcplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
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
         
         service:
         pipelines:
             logs/source0__chronicle_w_labels-0:
             receivers:
                 - tcplog
             exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
