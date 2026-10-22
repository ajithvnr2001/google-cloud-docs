---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rapid7-nexpose/
title: Collect Rapid7 Nexpose logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:26.744862+00:00
---

# Collect Rapid7 Nexpose logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rapid7-nexpose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Rapid7 Nexpose logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Rapid7 Nexpose logs to Google Security Operations using the Bindplane agent.

Rapid7 Nexpose (now InsightVM) is an on-premises vulnerability management platform used for scanning, assessing, and prioritizing security vulnerabilities across your network. It provides a web-based Security Console accessible at `https://<host>:3780` and supports native syslog export for forwarding scan results, vulnerability discoveries, and asset change events.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Rapid7 Nexpose Security Console
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Rapid7 Nexpose Security Console with **Global Administrator** or **Security Manager** role



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

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/rapid7_nexpose:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: RAPID7_NEXPOSE
            raw_log_field: body
        
        service:
          pipelines:
            logs/rapid7_nexpose_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/rapid7_nexpose
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/rapid7_nexpose:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: RAPID7_NEXPOSE
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows, choose one of the following options:

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Services console:

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Rapid7 Nexpose syslog forwarding

  1. Sign in to the **Rapid7 Nexpose Security Console** web interface at `https://<nexpose-host>:3780`.
  2. Go to **Administration > Global Settings**.
  3. Scroll down to the **Syslog** section.
  4. Enable syslog forwarding and provide the following configuration details: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514` (or the port configured in the Bindplane agent receiver).
     * **Protocol** : Select **UDP** (or **TCP** if configured in the receiver).
  5. Click **Save**.
  6. To verify that syslog messages are being sent, run a scan and check the Bindplane agent logs for incoming messages.

**Note:** The Nexpose Security Console sends syslog messages for scan results, vulnerability discoveries, and asset changes. Ensure the Bindplane agent host is reachable from the Nexpose console on the configured port.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| additional.fields | Merged from categories array as "App Stack" key-value pairs; merged from pci fields (adjustedCVSSScore, adjustedSeverityScore, fail, status) as key-value pairs; merged from cvss v2/v3 fields as detection fields in sec_result  
asset_id | principal.asset.asset_id | Set to "assetID: %{asset_id}" if asset_id != ""  
categories | additional.fields | Merged as "App Stack" key-value list  
cve_id, cve_year | extensions.vulns.vulnerabilities.cve_id | Concatenated from cve_year and cve_id if both present  
cvss.links, cvss.v2.accessComplexity, cvss.v2.accessVector, cvss.v2.authentication, cvss.v2.availabilityImpact, cvss.v2.confidentialityImpact, cvss.v2.integrityImpact, cvss.v2.vector, cvss.v3.attackComplexity, cvss.v3.attackVector, cvss.v3.availabilityImpact, cvss.v3.confidentialityImpact, cvss.v3.integrityImpact, cvss.v3.privilegeRequired, cvss.v3.scope, cvss.v3.userInteraction, cvss.v3.vector, links | security_result.detection_fields | Merged from links and cvss.links as key-value pairs; merged from cvss v2/v3 fields as prefixed key-value pairs (e.g., "v2 accessComplexity")  
desc | extensions.vulns.vulnerabilities.description | Value copied directly from desc if present  
description | metadata.description | Value from description.text if description empty, else value copied directly  
description.text | metadata.description | Value copied directly if description empty  
event_type | metadata.event_type | Set to "SCAN_VULN_HOST" if vulnerability_description or vulnerability_data present, else "SCAN_HOST" if has_principal true, else "GENERIC_EVENT"  
has_principal |  | Set to true if ip_address, host_name, or asset_id set  
has_target |  | Set to true if target_ip set  
host_name | principal.hostname, principal.asset.hostname | Value copied directly if host_name != ""  
ip_address | principal.ip, principal.asset.ip | Value copied directly if ip_address != ""  
last_assessed_for_vulnerabilities |  | Converted to timestamp using various date formats or UNIX/UNIX_MS  
pci.adjustedCVSSScore | additional.fields | Merged as "adjustedCVSSScore" key-value pair if not empty  
pci.adjustedSeverityScore | additional.fields | Merged as "adjustedSeverityScore" key-value pair if not empty  
pci.fail | additional.fields | Merged as "fail" key-value pair if not empty  
pci.status | additional.fields | Merged as "status" key-value pair if not empty  
sec_result | security_result | Value copied directly if sec_result != ""  
target_ip | target.ip, target.asset.ip | Value copied directly if target_ip != ""  
timestamp |  | Converted using syslog timestamp formats  
title | extensions.vulns.vulnerabilities.description | Value from vulnerability.Vulnerability_Title if present  
vulnerability.Vulnerability_Severity | extensions.vulns.vulnerabilities.severity | Set to "HIGH" if "Severe", "CRITICAL" if "Critical", "MEDIUM" if "Moderate"  
vulnerability.Vulnerability_Title | extensions.vulns.vulnerabilities.description | Value copied directly  
vulnerability.vulnerability_id | extensions.vulns.vulnerabilities.vendor_vulnerability_id | Value copied directly if present  
vulnerability_data | extensions.vulns.vulnerabilities | Merged from each vulnerability object with severity, cve_id, description, vendor_vulnerability_id  
vulnerability_description | extensions.vulns.vulnerabilities.description, metadata.description | Merged as vulnerability object if present; set to metadata.description  
| metadata.product_name | Set to "Nexpose"  
| metadata.vendor_name | Set to "Rapid7"  
`categories", "pci.adjustedCVSSScore", "pci.adjustedSeverityScore", "pci.fail", and "pci.status` | `additional.fields` | Mapped from changelog  
`cvss.v2.accessComplexity", "cvss.v2.accessVector", "cvss.v2.authentication", "cvss.v2.availabilityImpact", "cvss.v2.confidentialityImpact", "cvss.v2.integrityImpact", "cvss.v2.vector", "cvss.v3.attackComplexity", "cvss.v3.attackVector", "cvss.v3.availabilityImpact", "cvss.v3.confidentialityImpact", "cvss.v3.privilegeRequired", "cvss.v3.integrityImpact", "cvss.v3.scope", "cvss.v3.userInteraction", and "cvss.v3.vector` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rapid7-nexpose-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
