---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vitalqip/
title: Collect Nokia VitalQIP DDI logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:27.379330+00:00
---

# Collect Nokia VitalQIP DDI logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vitalqip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Nokia VitalQIP DDI logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Nokia VitalQIP DDI logs to Google Security Operations using Bindplane.

Nokia VitalQIP (now owned by Cygna Labs) is an enterprise-grade DDI solution providing centralized management of DNS (Domain Name System), DHCP (Dynamic Host Configuration Protocol), and IPAM (IP Address Management). VitalQIP delivers carrier-grade IP address management with scalable, secure DNS/DHCP services designed for large enterprises, telecom providers, and service providers requiring high-performance, on-premises, and hybrid cloud DDI solutions.

## Before you begin

  * Make sure you have the following prerequisites:

    * A Google SecOps instance
    * Windows Server 2016 or later, or Linux host with `systemd`
    * Network connectivity between the Bindplane agent and VitalQIP Appliance Management Software (AMS)
    * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
    * Administrative access to the VitalQIP Appliance Management Software (AMS) web interface
    * VitalQIP Appliance Manager version 1.7 or later (for multiple syslog server support)
    * At least one VitalQIP appliance (AMS, ESM, or AMM) configured in your environment



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

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
          chronicle/vitalqip:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: VITALQIP
            raw_log_field: body
            ingestion_labels:
              env: production
              source: vitalqip
        
        service:
          pipelines:
            logs/vitalqip_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/vitalqip
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on UDP port 514 
      * For Linux systems running as non-root, use port `1514` or higher
      * Adjust the port number if your environment requires a different port
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Replace `YOUR_CUSTOMER_ID` with the customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Set to `VITALQIP` (exact match for Chronicle parser)
    * `ingestion_labels`: Optional labels for filtering and organization



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/vitalqip:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VITALQIP
            raw_log_field: body
            ingestion_labels:
              env: production
              source: vitalqip
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



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
         




## Configure VitalQIP syslog forwarding

VitalQIP Appliance Manager (AM) version 1.7 and later supports configuring up to 10 remote syslog servers per appliance through the AMS web interface.

### Sign in to VitalQIP Appliance Management Software

  1. Open a web browser and navigate to your VitalQIP AMS web interface URL:

     * For non-secure connection: `http://<AMS_HOSTNAME>:<PORT>/qip`
     * For secure connection: `https://<AMS_HOSTNAME>:<PORT>/qip`
**Note:** The default non-secure port is typically 80, and the default secure port is 443 or 743.
  2. Enter your VitalQIP administrator credentials and click **Login**.




### Configure remote syslog server for appliances

  1. In the VitalQIP AMS web interface, expand the **Appliances** section in the left navigation panel.
  2. Select the appliance you want to configure for syslog forwarding (AMS, ESM, or AMM appliance).
  3. Navigate to the appliance configuration settings.
  4. Locate the **Remote Logging** or **Syslog Configuration** section.
  5. Click **Add** to add a new remote syslog server.
  6. Configure the following syslog server parameters: 
     * **Server Name** : Enter a descriptive name (for example, `Chronicle-Bindplane`)
     * **IP Address** : Enter the IP address of the Bindplane agent host
     * **Port** : Enter `514` (or the port configured in your Bindplane agent)
     * **Protocol** : Select **UDP**
     * **Facility** : Select **local0** through **local7** (or as required by your organization)
     * **Severity Level** : Select **Info** or **Debug** to capture all relevant log events
  7. Click **Save** or **Apply** to save the syslog server configuration.
  8. Deploy the configuration to the appliance: 
     1. Navigate to the appliance deployment section.
     2. Select the configuration changes.
     3. Click **Deploy** to push the syslog configuration to the appliance.
  9. Repeat steps 2-8 for each VitalQIP appliance (ESM, AMM) that you want to forward logs from.

**Note:** VitalQIP appliances generate logs for DNS queries, DHCP lease assignments, IP address allocations, administrative actions, and system events. All configured log types will be forwarded to the remote syslog server.

### Verify syslog forwarding

  1. Generate test activity in VitalQIP: 
     * Perform a DNS query
     * Allocate or release a DHCP lease
     * Make an administrative change in the VitalQIP GUI
  2. Check the Bindplane agent logs to verify log reception: 
     * **Linux** : `sudo journalctl -u observiq-otel-collector -f`
     * **Windows** : `type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"`
  3. Sign in to the Google SecOps console and verify that VitalQIP logs are appearing in the log search.



### Additional configuration notes

  * VitalQIP logs include DNS query logs, DHCP lease events, IP address management actions, and audit trails for administrator activities.
  * VitalQIP supports syslog format compliant with RFC 3164 (BSD syslog).
  * For high-volume environments, consider configuring multiple Bindplane agents with load balancing.
  * VitalQIP appliances can be configured to send logs to multiple remote syslog servers simultaneously (up to 10 servers per appliance in AM 1.7+).
  * Ensure network connectivity and firewall rules allow UDP port 514 (or your configured port) from VitalQIP appliances to the Bindplane agent host.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
tty | additional.fields | Merged with labels for terminal (tty), pwd, and subnet  
pwd | additional.fields |   
subnet | additional.fields |   
dhcp_client_ip | dhcp.ciaddr | Set for Delete Lease or Auto Release  
req_addr | dhcp.requested_address | Value copied directly  
dhcp.type | dhcp.type | Set to "RELEASE" for Delete Lease or Auto Release, "ACK" for RenewLease or GrantLease  
dhcp_client_ip | dhcp.yiaddr | Renamed for RenewLease or GrantLease  
log_msg | metadata.description | Value copied directly  
event_type | metadata.event_type | Set to event_type if not empty, else "GENERIC_EVENT"  
log_source | network.application_protocol | Set to "DNS" for named log_source, "DHCP" for dhcpd  
dhcp_domain | principal.administrative_domain | Value copied directly  
log_source | principal.application | Set if log_source does not contain / or sudo  
dns_server | principal.ip | Value copied directly  
log_source | principal.process.command_line | Set to log_source if contains / or sudo, else to cmd  
cmd | principal.process.command_line |   
pid | principal.process.pid | Value copied directly  
user | principal.user.userid | Value copied directly  
questions_name | questions.name | Value copied directly  
QTYPE | questions.type | Converted to uinteger  
client_id | target.asset_id | Set to "id: " + client_id  
dhcp_client_hostname | target.hostname | Value copied directly  
client_ip_address | target.ip | Merged from client_ip_address (DNS) or dhcp_client_ip (DHCP)  
dhcp_client_ip | target.ip |   
client_mac | target.mac | Value copied directly (after formatting)  
client_port | target.port | Converted to integer  
metadata.product_name | metadata.product_name | Set to "VITALQIP"  
metadata.vendor_name | metadata.vendor_name | Set to "NOKIA"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
