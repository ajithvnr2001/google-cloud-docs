---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-firewall/
title: Collect Windows Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:54:11.130162+00:00
---

# Collect Windows Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Windows Firewall logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Windows Firewall logs to Google Security Operations using Bindplane.

Windows Firewall is a built-in Windows host firewall that generates connection allow/block, rule change, and service event logs. The Bindplane agent collects the firewall log files directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with `observiq-otel-collector` service support
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Windows host(s) generating firewall logs



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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

## Configure Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - C:\Windows\system32\LogFiles\Firewall\pfirewall.log
                start_at: beginning
        
        exporters:
            chronicle/windows_firewall:
                compression: gzip
                creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: WINDOWS_FIREWALL
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/firewall_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/windows_firewall
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Default Windows Firewall log location: 
      * `C:\Windows\system32\LogFiles\Firewall\pfirewall.log`
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `windows_firewall`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `WINDOWS_FIREWALL`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `firewall_to_chronicle`: Descriptive name for the pipeline



### Save the configuration file

  * After editing, save the file: 
    * **Windows** : Click **File > Save**



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
         




## Configure Windows Firewall logging

  1. Open **Windows Defender Firewall with Advanced Security** by pressing `Win+R`, typing `wf.msc`, and pressing Enter.
  2. In the left pane, right-click **Windows Defender Firewall with Advanced Security on Local Computer** and select **Properties**.
  3. Select the appropriate profile tab (**Domain Profile** , **Private Profile** , or **Public Profile**).
  4. Under **Logging** , click **Customize**.
  5. Provide the following configuration details: 
     * **Log dropped packets** : Select **Yes**.
     * **Log successful connections** : Select **Yes**.
     * **Name** : Verify the log file path is `%systemroot%\system32\LogFiles\Firewall\pfirewall.log` (default).
     * **Size limit (KB)** : Set to at least `4096` to capture sufficient log data.
  6. Click **OK** to save the logging settings.
  7. Repeat steps 3-6 for each profile tab (**Domain** , **Private** , **Public**) as needed.
  8. Verify that the log file is being written at `C:\Windows\system32\LogFiles\Firewall\pfirewall.log`.
  9. Ensure the Bindplane agent `include` path in `config.yaml` matches the firewall log file path.

**Note:** By default, Windows Firewall only logs dropped packets. To capture all connection events for security monitoring, enable both **Log dropped packets** and **Log successful connections**. The Bindplane agent service account must have read access to the log file.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
tcpflags, tcpsyn, tcpack, tcpwin, icmptype, icmpcode | about.labels | Merged as key-value pairs if field != "-"  
timestamp | metadata.event_timestamp | Parsed using format yyyy-MM-dd HH:mm:ss  
| metadata.event_type | Set to "NETWORK_CONNECTION"  
direction | network.direction | Set to "OUTBOUND" if direction in ["SEND", "FORWARD"]; "INBOUND" if direction == "RECEIVE"  
protocol | network.ip_protocol | Value copied directly if protocol in ["TCP", "UDP", "ICMP"]  
size | network.received_bytes | Converted to uinteger if direction == "RECEIVE" and size != "-"  
size | network.sent_bytes | Converted to uinteger if direction in ["SEND", "FORWARD"] and size != "-"  
src_ip | principal.ip | Value copied directly  
src_port | principal.port | Converted to integer if src_port != "-"  
action | security_result.action | Set to "BLOCK" if action == "DROP"; "ALLOW" if action == "ALLOW"  
info | security_result.summary | Value copied directly if info != "-"  
dst_ip | target.ip | Value copied directly  
dst_port | target.port | Converted to integer if dst_port != "-"  
| metadata.product_name | Set to "Windows Firewall"  
| metadata.vendor_name | Set to "Microsoft"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
