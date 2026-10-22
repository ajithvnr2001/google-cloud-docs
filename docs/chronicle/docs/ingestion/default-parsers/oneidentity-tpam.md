---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oneidentity-tpam/
title: Collect One Identity TPAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:08.418982+00:00
---

# Collect One Identity TPAM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oneidentity-tpam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect One Identity TPAM logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest One Identity TPAM logs to Google Security Operations using Bindplane.

One Identity Privileged Access Manager (TPAM) is a legacy privileged access management solution that provides centralized password management, session monitoring, and privileged account governance for enterprise environments. TPAM generates activity logs for password retrievals, system administration actions, and privileged session activities.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and One Identity TPAM appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the One Identity TPAM web administration interface
  * TPAM appliance configured and operational



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
          chronicle/tpam:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: ONEIDENTITY_TPAM
            raw_log_field: body
            ingestion_labels:
              source: tpam
        
        service:
          pipelines:
            logs/tpam_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/tpam
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on 
      * `0.0.0.0:514` listens on all interfaces on port 514 (standard syslog port)
      * Use `0.0.0.0:1514` if running as non-root user on Linux
      * TPAM only supports UDP syslog, so `udplog` receiver is required
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Replace `YOUR_CUSTOMER_ID` with the customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Must be `ONEIDENTITY_TPAM` exactly as shown
    * `ingestion_labels`: Optional labels for filtering and organization
  * Example configuration for Linux (non-root user)
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:1514"
        
        exporters:
          chronicle/tpam:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
            endpoint: chronicle.googleapis.com
            log_type: ONEIDENTITY_TPAM
            raw_log_field: body
            ingestion_labels:
              env: production
              source: tpam
        
        service:
          pipelines:
            logs/tpam_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/tpam
        

  * Example configuration for Windows
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/tpam:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
            endpoint: chronicle.googleapis.com
            log_type: ONEIDENTITY_TPAM
            raw_log_field: body
            ingestion_labels:
              env: production
              source: tpam
        
        service:
          pipelines:
            logs/tpam_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/tpam
        




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/tpam:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ONEIDENTITY_TPAM
            raw_log_field: body
            ingestion_labels:
              source: tpam
        


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
         




## Configure One Identity TPAM syslog forwarding

Configure TPAM to forward syslog messages to the Bindplane agent.

  1. Sign in to the **One Identity TPAM** web administration interface.
  2. Navigate to **/admin**.
  3. In the left navigation menu, go to **System Status > SysLog Configuration**.
  4. In the **SysLog Configuration** page, provide the following configuration details: 
     * **SysLog Server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter the port number configured in the Bindplane agent (for example, `514` or `1514`). 
       * Default port is `514`
       * If using non-root Bindplane agent on Linux, use `1514` or higher
     * **Protocol** : TPAM only supports **UDP** for syslog transmission.
  5. Click **Save** or **Apply** to save the configuration.
  6. Click **Test Connection** if available to verify connectivity to the Bindplane agent.
  7. Enable syslog forwarding if there is a separate enable/disable toggle. Note: TPAM sends syslog messages in a custom proprietary format (not CEF compliant). The format includes two log types: 
     * **Activity Report (tpam)** : Password retrievals, system operations, and privileged access activities
     * **Sys-Admin Activity Log (sysadmin)** : Administrative actions and configuration changes


  * The syslog message format follows this structure:
        
        PAR[PID]: UserName/AdminName, Operation, ObjectType, Target/ObjectName, Role, Failed, OtherInfo
        




### Verify syslog forwarding

  1. Perform a test action in TPAM (for example, retrieve a password or modify a system).
  2. Check the Bindplane agent logs to verify syslog messages are being received:

     * **Linux:**
    
    sudo journalctl -u observiq-otel-collector -f | grep -i tpam
    

     * **Windows:**
    
    type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log" | findstr /i "tpam"
    

  3. Sign in to the Google SecOps console and verify logs are appearing in the **Search** interface.




### Troubleshooting syslog connectivity

If syslog messages are not being received:

  1. Verify network connectivity between TPAM appliance and Bindplane agent:
         
         ping <bindplane_agent_ip>
         

  2. Verify UDP port is open and listening on Bindplane agent:

     * **Linux:**
           
           sudo netstat -ulnp | grep 514
           

     * **Windows:**
           
           netstat -an | findstr :514
           

  3. Check firewall rules allow UDP traffic on the configured port:

     * Source: TPAM appliance IP address
     * Destination: Bindplane agent IP address
     * Protocol: UDP
     * Port: 514 (or configured port)



Verify TPAM syslog configuration is saved and active:

  1. Sign in to TPAM web interface

  2. Navigate to **/admin > System Status > SysLog Configuration**

  3. Verify IP address and port are correct

  4. Test connection if available




Review TPAM system logs for syslog transmission errors:

  1. Navigate to **/admin > System Status > System Logs**
  2. Look for syslog-related error messages



For additional troubleshooting information, see the [One Identity TPAM syslog troubleshooting guide](https://support.oneidentity.com/tpam/kb/4211425/troubleshooting-syslog-not-receiving-data).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
cn1 | additional.fields | Additional vendor-specific event data that cannot be adequately represented within the formal sections of the UDM model  
cn1Label | additional.fields |   
cs1 | additional.fields |   
cs1Label | additional.fields |   
cs2 | additional.fields |   
cs2Label | additional.fields |   
cs3 | additional.fields |   
cs3Label | additional.fields |   
cs4 | additional.fields |   
cs4Label | additional.fields |   
cs5 | additional.fields |   
cs5Label | additional.fields |   
cs6 | additional.fields |   
cs6Label | additional.fields |   
msg | metadata.description | Description of the event  
metadata.event_type | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
eventid | metadata.product_event_type | Product-specific event type  
logmsg | metadata.product_event_type |   
version | metadata.product_version | Version of the product  
hostname | principal.asset.hostname | Hostname of the asset associated with the principal  
groupName | principal.group.group_display_name | Display name of the group  
hostname | principal.hostname | Hostname of the principal  
cs1 | principal.user.attribute.roles | Roles associated with the user  
deviceCustomDate1 | security_result.detection_fields | Fields used in detection  
deviceCustomDate1Label | security_result.detection_fields |   
reason | security_result.summary | Summary of the security result  
destinationDnsDomain | target.domain.name | Name of the target domain  
cn1 | target.resource.product_object_id | Product-specific object ID of the target resource  
requestUrl | target.url | URL of the target  
duser | target.user.user_display_name | Display name of the target user  
duid | target.user.userid | User ID of the target user  
logmessage | metadata.product_name | Name of the product  
logtype | metadata.vendor_name | Name of the vendor  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`cn2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs2", "cs3", "cs4", "cs5", "cs6` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oneidentity-tpam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
