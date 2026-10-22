---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hillstone-ngfw/
title: Collect Hillstone Firewall logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:29.489425+00:00
---

# Collect Hillstone Firewall logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hillstone-ngfw/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Hillstone Firewall logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Hillstone Firewall logs to Google Security Operations using Bindplane.

Hillstone Firewall is a next-generation firewall that provides advanced threat detection and prevention capabilities, application control, intrusion prevention, and policy automation. The firewall offers comprehensive security features including real-time threat protection, unified threat management, and intelligent policy operation to protect network infrastructure from known and unknown threats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Hillstone Firewall
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Hillstone Firewall management console or appliance
  * Administrative credentials for the Hillstone Firewall web interface



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
          chronicle/hillstone_firewall:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: HILLSTONE_NGFW
            raw_log_field: body
            ingestion_labels:
              env: production
              source: hillstone_firewall
        
        service:
          pipelines:
            logs/hillstone_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/hillstone_firewall
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * The receiver is configured to listen on UDP port 514 on all interfaces (0.0.0.0).
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Replace `YOUR_CUSTOMER_ID` with the Customer ID from the previous step.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Set to `HILLSTONE_NGFW` exactly as shown.
    * `ingestion_labels`: Optional labels in YAML format (customize as needed).



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/hillstone_firewall:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: HILLSTONE_NGFW
            raw_log_field: body
            ingestion_labels:
              env: production
              source: hillstone_firewall
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

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

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Hillstone Firewall syslog forwarding

### Create a syslog server

  1. Sign in to the Hillstone Firewall web interface.
  2. Go to **Log > Configuration > Syslog Server** to visit the Syslog Server List page.
  3. Click **New** to create a new syslog server.
  4. In the **Syslog Server Configuration** dialog, configure the following settings: 
     * **Host name** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Binding** : Select **Virtual Router** and then select a virtual router from the drop-down list, or select **Source Interface** and then select a source interface from the drop-down list.
     * **Protocol** : Select **UDP** from the drop-down list.
     * **Port** : Enter `514`.
     * **Log Type** : Select the log types you want the syslog server to receive. Available log types include: 
       * **Event** : System and administrative activity audits, routing and networking events.
       * **Alarm** : Urgent, alert, and critical severity logs.
       * **Security** : Security events such as attack defense and application security.
       * **IPS** : Network intrusion protection events.
       * **Configuration** : Configuration changes on command line interface.
       * **Network** : Network services operations such as PPPoE and DDNS.
       * **Session** : Session logs including protocols, source and destination IP addresses and ports.
       * **NAT** : NAT logs including NAT type, source and destination IP addresses and ports.
  5. Click **OK** to save the syslog server configuration.



### Enable log forwarding for each log type

  1. Go to **Log > Configuration > Log** to visit the **Log Configuration** page.
  2. Click the tab of the log type you want to configure (for example, **Event** , **Alarm** , **Security** , **IPS** , **Configuration** , **Network** , **Session** , or **NAT**).
  3. For each log type you want to forward: 
     1. Select the **Enable** to enable the log function.
     2. Select the **Syslog server** to export logs to the syslog server.
     3. In the **Lowest severity** drop-down list, select the lowest severity level. Logs below the severity level selected here won't be exported.
     4. Click the **All syslog servers** link to verify that your configured syslog server is listed.
  4. Click **OK** to save the settings.
  5. Repeat steps 2 through 4 for each log type you want to forward to Google SecOps.



### Verify log forwarding

  1. On the Bindplane agent host, verify that syslog messages are being received:

     * **Linux:**
    
    sudo journalctl -u observiq-otel-collector -f
    

     * **Windows:**
    
    type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
    

  2. Look for log entries indicating successful receipt and forwarding of Hillstone Firewall logs.

  3. After 5 to 10 minutes, verify that logs appear in the Google SecOps console.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
start_time_label, close_time_label, state_label, vr_label | additional.fields | Additional metadata fields  
desc | metadata.description | Description of the event  
| metadata.event_type | Type of event  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor name  
protocol_number_src | network.ip_protocol | IP protocol used  
receive_bytes | network.received_bytes | Number of bytes received  
receive_packets | network.received_packets | Number of packets received  
send_bytes | network.sent_bytes | Number of bytes sent  
send_packets | network.sent_packets | Number of packets sent  
session_id | network.session_id | Session identifier  
host | principal.asset.hostname | Hostname of the principal asset  
src_ip | principal.asset.ip | IP address of the principal asset  
zone_val | principal.cloud.availability_zone | Cloud availability zone  
host | principal.hostname | Hostname of the principal  
src_ip | principal.ip | IP address of the principal  
mac_address | principal.mac | MAC address of the principal  
src_port | principal.port | Port number of the principal  
ethernet_src_label | principal.resource.attribute.labels | Labels for principal resource attributes  
id | principal.user.userid | User ID of the principal  
dst_ip | target.asset.ip | IP address of the target asset  
dst_ip | target.ip | IP address of the target  
dst_port | target.port | Port number of the target  
ethernet_dst_label | target.resource.attribute.labels | Labels for target resource attributes  
policy | target.resource.name | Name of the target resource  
policy | target.resource.type | Type of the target resource  
user | target.user.userid | User ID of the target  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hillstone-ngfw-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
