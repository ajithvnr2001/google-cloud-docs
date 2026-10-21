---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop-dns/
title: Collect ExtraHop Reveal(x) DNS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:02:22.266363+00:00
---

# Collect ExtraHop Reveal(x) DNS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ExtraHop Reveal(x) DNS logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ExtraHop Reveal(x) DNS logs to Google Security Operations using Bindplane. ExtraHop Reveal(x) provides passive DNS monitoring capabilities that capture and analyze all DNS transactions across the network. Organizations use Reveal(x) to detect DNS-based threats such as tunneling, domain generation algorithms (DGA), and data exfiltration through deep packet inspection of DNS traffic.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or a Linux host with `systemd`.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the ExtraHop Reveal(x) Administration page.
  * Network connectivity between the ExtraHop sensor and the Bindplane agent host on the configured syslog port.



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

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         




### Linux installation

  1. Open a terminal with **root** or **sudo** privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional installation resources

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * **Linux** : `sudo systemctl status observiq-otel-collector`
     * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/extrahop_dns:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: 'EXTRAHOP_DNS'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/extrahop_dns_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/extrahop_dns
         



  * Replace **`<CUSTOMER_ID>`** with the actual customer ID.
  * Update **`/path/to/ingestion-authentication-file.json`** to the path where the service account key file (Option 1) was saved.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/extrahop_dns:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'EXTRAHOP_DNS'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run: `sudo systemctl restart observiq-otel-collector`
  * To restart the Bindplane agent in **Windows** , use the **Services** console or run: `cmd net stop observiq-otel-collector && net start observiq-otel-collector`



## Configure ExtraHop Reveal(x) Open Data Stream for DNS syslog forwarding

### Add a syslog Open Data Stream target

  1. Sign in to the ExtraHop **Administration** page.
  2. In the **System Configuration** section, click **Open Data Streams**.
  3. Click **Add Target** and select **Syslog**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (e.g., `Google SecOps-DNS`).
     * **Host** : Enter the IP address of the **Bindplane agent** host.
     * **Port** : `514`.
     * **Protocol** : **UDP**.
  5. Click **Test** to verify connectivity, then click **Save**.



### Create a trigger to export DNS transactions

  1. Click the **System Settings** icon and select **Triggers**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : `DNS Syslog Export`.
     * **Events** : Select **DNS_REQUEST** and **DNS_RESPONSE**.
  4. In the **Editor** pane, enter the following trigger script:
         
         var obj = {
             eh_event: "dns",
             client_ip: Flow.client.ipaddr.toString(),
             server_ip: Flow.server.ipaddr.toString(),
             client_port: Flow.client.port,
             server_port: Flow.server.port,
             qname: DNS.qname,
             qtype: DNS.qtype
         };
         
         if (event === "DNS_RESPONSE") {
             obj.dns_type = "response";
             obj.rcode = DNS.errorNum;
             obj.answers = JSON.stringify(DNS.answers);
         } else {
             obj.dns_type = "request";
             obj.opcode = DNS.opcode;
         }
         
         Remote.Syslog("Chronicle-DNS").info(JSON.stringify(obj));
         

**Note:** Replace `Chronicle-DNS` in the script with the exact **Name** you gave your syslog ODS target.
  5. Click **Save**.




### Assign the trigger to devices

  1. Open the trigger you created.
  2. In the **Assignments** section, click **Assign**.
  3. Select the relevant devices or device groups and click **Assign**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`answers` | `network.dns.answers` | Parsed from raw field.  
`dst` | `target.ip` | Raw mapping.  
`dpt` | `target.port` | Raw mapping.  
`host` | `principal.hostname` | Raw mapping.  
`proto` | `network.ip_protocol` | Raw mapping.  
`qname` | `network.dns.questions.name` | Raw mapping.  
`qtype` | `network.dns.questions.type` | Raw mapping.  
`rcode` | `network.dns.response_code` | Raw mapping.  
`src` | `principal.ip` | Raw mapping.  
`spt` | `principal.port` | Raw mapping.  
`ttl` | `network.dns.answers.ttl` | Raw mapping.  
N/A | `metadata.log_type` | Set to `EXTRAHOP_DNS`.  
N/A | `metadata.product_name` | Set to `Reveal(x) DNS`.  
N/A | `metadata.vendor_name` | Set to `ExtraHop`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
