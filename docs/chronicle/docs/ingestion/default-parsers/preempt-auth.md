---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/preempt-auth/
title: Collect Preempt Auth logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:12:42.911274+00:00
---

# Collect Preempt Auth logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/preempt-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Preempt Auth logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Preempt Auth logs to Google Security Operations using the Bindplane agent.

Preempt Auth is an authentication event monitoring solution that generates detailed authentication logs for Active Directory environments. It captures successful and failed login events, LDAP searches, service access, and authentication types across endpoints.

**Note:** Preempt Security was acquired by CrowdStrike in September 2020 and has been fully integrated into **CrowdStrike Falcon Identity Protection**. The standalone Preempt product is no longer available. If you have migrated to CrowdStrike Falcon Identity Protection, refer to the [Collect CrowdStrike Falcon logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-edr) guide instead.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Preempt server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Preempt Auth (CrowdStrike Identity Protection) with administrator permissions



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/preempt_auth:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: PREEMPT_AUTH
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/preempt_auth_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/preempt_auth
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: Receives syslog over TCP. Use `udplog` if your Preempt deployment forwards over UDP.
    * `0.0.0.0:514`: Listens on all interfaces on port 514. Change the port if needed (for example, `1514` for non-root Linux).
  * **Exporter configuration:**

    * `<CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<CUSTOMER_ID>`: Customer ID from the **Get Google SecOps customer ID** step.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/preempt_auth:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: PREEMPT_AUTH
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
             




## Configure Preempt Auth syslog forwarding

**Note:** Preempt Auth is a deprecated product. These instructions apply to legacy Preempt deployments only. If you have migrated to CrowdStrike Falcon Identity Protection, use the CrowdStrike integration guide instead.

  1. Sign in to the **Preempt management console**.
  2. Navigate to **Settings > SIEM Integration**.
  3. Enable syslog forwarding for authentication events.
  4. Provide the following configuration details: 
     * **Protocol** : Select **TCP** (must match the Bindplane agent receiver configuration).
     * **Syslog server address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
  5. Select the authentication event types to forward: 
     * Successful authentication events
     * Failed authentication events
     * LDAP searches
     * Service access events
  6. Click **Save** or **Apply**.
  7. Verify that logs are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
authenticationType | extensions.auth.type | Set to "SSO" if authenticationType matches SSO_LOGIN or LDAP_AUTHENTICATION; "MACHINE" if DOMAIN_LOGIN; "AUTHTYPE_UNSPECIFIED" if NTLM_AUTHENTICATION  
| extensions.auth.mechanism | Set to "MECHANISM_UNSPECIFIED"  
inter_ip | intermediary.hostname | Set if inter_ip is not a valid IP address  
inter_ip | intermediary.ip | Set if inter_ip is a valid IP address  
eventLabel | metadata.description | Value copied directly  
eventType | metadata.event_type | Set to "USER_LOGIN" if eventType is SUCCESSFUL_AUTHENTICATION or FAILED_AUTHENTICATION; "SERVICE_UNSPECIFIED" if SERVICE_ACCESS or LDAP_SEARCH and principal_host_set is true  
eventType | metadata.product_event_type | Value copied directly  
endpointDisplayName, ipAddress | principal.hostname | Set if endpointDisplayName != ipAddress and endpointDisplayName != ""  
ipAddress, inter_ip | principal.ip | Value from ipAddress if ipAddress != inter_ip, else from inter_ip  
networkType | principal.resource.name | Value copied directly  
| principal.resource.type | Set to "Network type"  
userDisplayName | principal.user.email_addresses | Set if userDisplayName matches email regex  
userDisplayName | principal.user.user_display_name | Value copied directly  
userEntity.secondaryDisplayName, userDisplayName | principal.user.userid | Value from userEntity.secondaryDisplayName if not empty, else from userDisplayName if userEntity.secondaryDisplayName is empty  
eventType | security_result.action | Set to "ALLOW" if SUCCESSFUL_AUTHENTICATION, "BLOCK" if FAILED_AUTHENTICATION  
eventSeverity | security_result.severity_details | Value copied directly  
authenticationType | security_result.summary | Value copied directly  
targetEntity.primaryDisplayName, targetServiceIdentifier, eventType, targetEntity.type | target.application | Value from targetEntity.primaryDisplayName if targetEntity.type == "CLOUD_SERVICE"; else from targetServiceIdentifier if targetServiceIdentifier != "" and not previously set; else "LDAP" if eventType == "LDAP_SEARCH" and not previously set  
targetEntity.primaryDisplayName, targetEntity.type | target.hostname | Set if targetEntity.type == "ENDPOINT"  
targetServiceType | target.resource.name | Set if targetServiceType != "" and != "UNKNOWN"  
targetServiceType | target.resource.type | Set to "Service Type" if targetServiceType != "" and != "UNKNOWN"  
targetEntity.primaryDisplayName, targetEntity.type | target.user.user_display_name | Set if targetEntity.type == "USER"  
targetEntity.secondaryDisplayName, targetEntity.type | target.user.userid | Set if targetEntity.type == "USER"  
| metadata.product_name | Set to "PREEMPT_AUTH"  
| metadata.vendor_name | Set to "Preempt"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
