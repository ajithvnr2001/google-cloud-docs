---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-horizon/
title: Collect Omnissa Horizon (formerly VMware Horizon) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:01.193813+00:00
---

# Collect Omnissa Horizon (formerly VMware Horizon) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-horizon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Omnissa Horizon (formerly VMware Horizon) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Omnissa Horizon (formerly known as VMware Horizon) logs to Google Security Operations using Bindplane.

Omnissa Horizon is a virtual desktop infrastructure (VDI) platform that delivers virtual desktops and applications to end users. It provides centralized management of virtual machines, session monitoring, and policy enforcement across on-premises and hybrid cloud environments. The parser extracts fields from raw syslog messages using regular expressions (grok patterns) and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Omnissa Horizon Connection Server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Omnissa Horizon Console (administrator role)



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
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/vmware_horizon:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VMWARE_HORIZON
            raw_log_field: body
        
        service:
          pipelines:
            logs/vmware_horizon_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/vmware_horizon
        




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
          chronicle/vmware_horizon:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VMWARE_HORIZON
            raw_log_field: body
        


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
         




## Configure syslog forwarding in Omnissa Horizon (formerly VMware Horizon)

  1. Sign in to the **Omnissa Horizon Console** with an administrator account.
  2. Go to **Settings > Event Configuration**.
  3. In the **Send to syslog servers** section, click **Add**.

  4. Provide the following configuration details:

     * **Server Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
  5. Click **Save**.

  6. Verify that events are being forwarded by checking the Bindplane agent logs.

**Note:** Omnissa Horizon forwards Connection Server events, agent events, administrator audit events, and alarm events through syslog. All event categories are included by default when syslog forwarding is enabled.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`ActionId` | `metadata.product_log_id` | The value of `ActionId` from the raw log is mapped to `metadata.product_log_id`.  
`admin_domain` | `principal.administrative_domain` | The value of `admin_domain` from the raw log is mapped to `principal.administrative_domain`.  
`BrokerName` | `principal.hostname` | The value of `BrokerName` from the raw log is mapped to `principal.hostname`.  
`BrokerSessionId` | `network.session_id` | The value of `BrokerSessionId` from the raw log is mapped to `network.session_id`.  
`ClientIpAddress` | `principal.ip` | The value of `ClientIpAddress` from the raw log is mapped to `principal.ip`.  
`CurrentSessionLength` | `network.session_duration.seconds` | The value of `CurrentSessionLength` from the raw log is converted to integer and then mapped to `network.session_duration.seconds`.  
`description` | `metadata.description` | The value of `description` from the raw log is mapped to `metadata.description`.  
`DesktopDisplayName` | `principal.hostname` | The value of `DesktopDisplayName` from the raw log is mapped to `principal.hostname`.  
`EventType` | `metadata.product_event_type` | The value of `EventType` from the raw log is mapped to `metadata.product_event_type`.  
`ForwardedClientIpAddress` | `principal.nat_ip` | The value of `ForwardedClientIpAddress` from the raw log is mapped to `principal.nat_ip`.  
`GlobalEntitlementName` | `target.user.group_identifiers` | The value of `GlobalEntitlementName` from the raw log is mapped to `target.user.group_identifiers`.  
`host` | `principal.hostname` | The value of `host` from the raw log is mapped to `principal.hostname`.  
`MachineDnsName` | `principal.url` | The value of `MachineDnsName` from the raw log is mapped to `principal.url`.  
`MachineName` | `intermediary.hostname` | The value of `MachineName` from the raw log is mapped to `intermediary.hostname`.  
`Module` | `additional.fields` | The key "Module" with the value of `Module` from the raw log is added to `additional.fields` array.  
`pid` | `principal.process.pid` | The value of `pid` from the raw log is mapped to `principal.process.pid`.  
`PoolId` | `additional.fields` | The key "PoolId" with the value of `PoolId` from the raw log is added to `additional.fields` array.  
`program` | `principal.application` | The value of `program` from the raw log is mapped to `principal.application`.  
`SessionType` | `additional.fields` | The key "SessionType" with the value of `SessionType` from the raw log is added to `additional.fields` array.  
`Severity` | `security_result.severity` | The value of `Severity` from the raw log is uppercased, mapped to generic severities and then mapped to `security_result.severity`.  
`timestamp` | `metadata.event_timestamp` | The value of `timestamp` from the raw log is converted to the appropriate format and then mapped to `metadata.event_timestamp`.  
`UserDisplayName` | `target.user.user_display_name` | The value of `UserDisplayName` from the raw log is mapped to `target.user.user_display_name`.  
`UserName` | `target.user.userid` | The value of `UserName` from the raw log is mapped to `target.user.userid`.  
`UserSID` | `target.user.windows_sid` | The value of `UserSID` from the raw log is mapped to `target.user.windows_sid`.  
`ViewApiMethodName` | `additional.fields` | The key "ViewApiMethodName" with the value of `ViewApiMethodName` from the raw log is added to `additional.fields` array.  
`ViewApiServiceName` | `additional.fields` | The key "ViewApiServiceName" with the value of `ViewApiServiceName` from the raw log is added to `additional.fields` array.  
| `extensions.auth.type` | The value is set to "SSO" if the `EventType` field is one of "ADMIN_USERLOGGEDOUT", "AGENT_CONNECTED", "AGENT_DISCONNECTED", "AGENT_ENDED", "AGENT_PENDING", "AGENT_PENDING_EXPIRED", "AGENT_RECONNECTED", "BROKER_DESKTOP_REQUEST", "BROKER_LMV_REMOTE_POD_DESKTOP_LAUNCH", "BROKER_MACHINE_ALLOCATED", "BROKER_USER_AUTHFAILED_BAD_USER_PASSWORD", "BROKER_USER_LOCK_SSO", "BROKER_USERLOGGEDIN", "BROKER_USERLOGGEDOUT", "VLSI_USERLOGGEDIN", "VLSI_INSUFFICIENT_PERMISSION", "VLSI_USERLOGGEDIN_REST", "TIMING_PROFILER_TUNNEL_CONNECTION", "TIMING_PROFILER_GET_LAUNCH_ITEMS", "TIMING_PROFILER_USER_AUTHENTICATION".  
| `metadata.event_type` | The value is determined by the `EventType` field. If `EventType` is one of "ADMIN_USERLOGGEDOUT", "AGENT_DISCONNECTED", "AGENT_ENDED", "AGENT_PENDING_EXPIRED", "BROKER_USER_LOCK_SSO", "BROKER_USERLOGGEDOUT" then `metadata.event_type` is "USER_LOGOUT". If `EventType` is one of "AGENT_CONNECTED", "AGENT_PENDING", "AGENT_RECONNECTED", "BROKER_USERLOGGEDIN", "VLSI_USERLOGGEDIN", "VLSI_INSUFFICIENT_PERMISSION", "VLSI_USERLOGGEDIN_REST" then `metadata.event_type` is "USER_LOGIN". If `EventType` is "TIMING_PROFILER_GET_LAUNCH_ITEMS" then `metadata.event_type` is "STATUS_UNCATEGORIZED". If `EventType` is "AGENT_SHUTDOWN" then `metadata.event_type` is "STATUS_SHUTDOWN". If `EventType` is one of "AGENT_STARTUP", "BROKER_LMV_REMOTE_POD_DESKTOP_LAUNCH" then `metadata.event_type` is "STATUS_STARTUP". Otherwise, `metadata.event_type` is "GENERIC_EVENT".  
| `metadata.log_type` | The value is set to "VMWARE_HORIZON".  
| `metadata.product_name` | The value is set to "HORIZON".  
| `metadata.vendor_name` | The value is set to "VMWARE".  
`SecurityID` | `event.idm.read_only_udm.principal.user.windows_sid` | Mapped from changelog  
`AccountName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`AccountDomain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`ObjectServer` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`ObjectName` | `event.idm.read_only_udm.target.user.windows_sid` | Mapped from changelog  
`HandleID` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`ProcessID` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`ProcessName` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`LogonID` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`ObjectType` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`AccessMask` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`TransactionID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PrivilegesUsedforAccessCheck` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Accesses` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AccessReasons` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Properties` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RestrictedSIDCount` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`usr` | `target.user.userid` | Mapped from changelog  
`MachineId` | `principal.asset.asset_id` | Mapped from changelog  
`int_host` | `intermediary.hostname` | Mapped from changelog  
`ip_1` | `principal.ip` | Mapped from changelog  
`port_number` | `principal.port` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-horizon-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
