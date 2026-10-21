---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-ips/
title: Collect Trellix IPS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:03:48.134009+00:00
---

# Collect Trellix IPS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-ips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix IPS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix IPS logs to Google Security Operations using the Bindplane agent.

Trellix IPS (formerly McAfee IPS/Network Security Platform) is a network intrusion prevention system that provides real-time detection and prevention of network-based threats, including exploits, malware, and denial-of-service attacks. It uses signature-based and behavioral analysis to inspect network traffic inline, automatically blocking malicious activity while allowing legitimate traffic to pass through.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Trellix IPS Manager (Network Security Manager) console



## Get Google SecOps Ingestion Authentication File

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

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

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
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
             customer_id: YOUR_CUSTOMER_ID_HERE
             endpoint: malachiteingestion-pa.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'MCAFEE_IPS'
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
     * Replace `YOUR_CUSTOMER_ID_HERE` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.
     * Update the `endpoint` value to match your tenant's region.



## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Trellix IPS syslog forwarding

  1. Sign in to the **Trellix Network Security Manager** (formerly McAfee Network Security Manager) console.
  2. Go to **Manager > Setup > Notification > Syslog**.
  3. Click **Enable** to enable syslog notification.
  4. Click **Add** to add a new syslog server.
  5. Provide the following configuration details: 
     * **Syslog Server IP Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or the port configured in Bindplane).
     * **Protocol** : Select **TCP**.
     * **Facility** : Select **Local0** (or as required by your environment).
  6. In the **Notification** section, select the alert severity levels to forward: 
     * **Informational**
     * **Low**
     * **Medium**
     * **High**
     * **Critical**
  7. In the **Message Format** section, select the syslog message format: 
     * Select **Standard Syslog** or **CEF** (Common Event Format) based on your requirements.
  8. Click **Save** to save the syslog server configuration.
  9. Go to **Manager > Setup > Notification > Forward Alerts**.
  10. Enable alert forwarding and select the syslog server configured in the previous steps.
  11. Select the alert types to forward: 
     * **IPS Alerts**
     * **Fault Alerts**
     * **Audit Alerts**
  12. Click **Save** to apply the configuration.

**Note:** For more information, see the [Trellix Network Security Manager documentation](https://docs.trellix.com/bundle/network-security-platform-manager-administration-guide-11.1.x/page/GUID-F5994024-5A56-4AA2-A498-B498EA1D9B5C.html).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_intermediary` | `intermediary` | Merged  
`_event_type` | `metadata.event_type` | Directly mapped  
`_network` | `network` | Renamed/mapped  
`_principal` | `principal` | Renamed/mapped  
`_security_result` | `security_result` | Merged  
`_target` | `target` | Renamed/mapped  
N/A | `intermediary` | Constant: `_intermediary`  
N/A | `metadata.product_name` | Constant: `MCafee IPS`  
N/A | `metadata.vendor_name` | Constant: `MCafee`  
N/A | `security_result` | Constant: `_security_result`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
