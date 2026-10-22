---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ise/
title: Collect Cisco ISE logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:56.071195+00:00
---

# Collect Cisco ISE logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ise/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco ISE logs

**Parser Version:** 34.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco ISE logs to Google Security Operations using Bindplane.

The parser extracts fields from Cisco ISE syslog and CSV formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco ISE Administration portal



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
          chronicle/chronicle_w_labels:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: 'CISCO_ISE'
            raw_log_field: body
            ingestion_labels:
        
        service:
          pipelines:
            logs/source0__chronicle_w_labels-0:
              receivers:
                - udplog
              exporters:
                - chronicle/chronicle_w_labels
        




### Configuration parameters

  * Replace the following placeholders:

    * **Receiver configuration:**

      * `udplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog
      * `0.0.0.0`: IP address to listen on (`0.0.0.0` to listen on all interfaces)
      * `514`: Port number to listen on (standard syslog port)
    * **Exporter configuration:**

      * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
        * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
        * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
      * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section
      * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
      * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
      * `endpoint`: Keep set to `chronicle.googleapis.com`.
      * `log_type`: Log type exactly as it appears in Chronicle (`CISCO_ISE`)



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'CISCO_ISE'
            raw_log_field: body
            ingestion_labels:
        


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

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Syslog forwarding on Cisco ISE

  1. Sign in to the **Cisco ISE Administration** portal.
  2. Go to **Administration > System > Logging > Remote Logging Targets**.
  3. Click **Add** to create a new remote logging target.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google-SecOps-Bindplane`).
     * **Description** : Enter a description (optional).
     * **IP Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Facility Code** : Select **LOCAL6** (or your preferred facility).
     * **Maximum Length** : Enter `8192` (or the maximum supported value).
     * **Include Alarms in Syslog Messages** : Check if you want to include alarms.
  5. Click **Save**.
  6. Go to **Administration > System > Logging > Logging Categories**.
  7. Select each logging category you want to forward and click **Edit** : 
     * **AAA Audit**
     * **AAA Diagnostics**
     * **Accounting**
     * **Administrator Audit**
     * **Posture and Client Provisioning Audit**
     * **Profiler**
     * **System Diagnostics**
  8. In the **Targets** section, move the remote logging target `Google-SecOps-Bindplane` from **Available** to **Selected**.
  9. Click **Save**.
  10. Verify syslog messages are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Device_IP_Address` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`DeviceIPAddress` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`DevicePort` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`NetworkDeviceName` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`DestinationIPAddress` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`DestinationPort` | `event.idm.read_only_udm.intermediary.port` | Mapped from changelog  
`DeviceIPAddress` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`DevicePort` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`nas_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Acct-Multi-Session-Id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Certificate` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`expiry_date` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Model Name` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Mapped from changelog  
`FramedIPAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`FramedIPAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`undefined-186` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`undefined-187` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`undefined-188` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Service` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Privilege-Level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Authen-Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Authen-Method` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Service-Argument` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`MatchedCommandSet` | `event.idm.read_only_udm.security_result.rule_labels` | Mapped from changelog  
`SelectedCommandSet` | `event.idm.read_only_udm.security_result.rule_labels` | Mapped from changelog  
`NAS-IP-Address` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`ServiceSelectionMatchedRule` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EapAuthentication` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ACSVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NetworkDeviceGroups_Device_Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NetworkDeviceGroups_Location` | `event.idm.read_only_udm.intermediary.location.country_or_region` | Mapped from changelog  
`EnableFlag` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LicenseTypes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NetworkDeviceName` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`r_ip_or_host` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`r_ip_or_host` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`intermediary` | `event.idm.read_only_udm.intermediary` | Mapped from changelog  
`DestinationPort` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`NAS-Port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`NAS-IP-Address` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`SSID` | `event.idm.read_only_udm.intermediary.mac` | Mapped from changelog  
`UserName` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`User-Name` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`CPMSessionID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TotalAuthenLatency` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ClientLatency` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IdentityPolicyMatchedRule` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EndPointMatchedProfile` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RadiusFlowType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`IsThirdPartyDeviceFlow` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SelectedAuthorizationProfiles` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SSID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AcsSessionID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SelectedAccessService` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AuthenticationIdentityStore` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`allowEasyWiredSession` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ConfigVersionId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RequestLatency` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Service-Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Class` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Called-Station-ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Calling-Station-ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Acct-Session-Id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Protocol` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PostureAssessmentStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`r_total_seg` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`r_seg_num` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EapTunnel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cisco-av-pair` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Framed-MTU` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Airespace-Wlan-Id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NAS-Identifier` | `event.idm.read_only_udm.principal.labels` | Mapped from changelog  
`Chargeable-User-Identity` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`UserType` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`AuthenticationMethod` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`SelectedAuthenticationIdentityStores` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`r_ip_or_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`r_ip_or_host` | `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`NAS-IP-Address` | `event.idm.read_only_udm.principal.nat_ip` | Mapped from changelog  
`DestinationIPAddress` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`Device_IP_Address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`UserName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`User-Name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`NetworkDeviceProfileId` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`EndpointMacAddress` | `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`ISELocalAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`ISELocalAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`NetworkDeviceProfileName` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`MacAddress` | `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`IpAddress` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`PortalName` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`NADAddress` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`AuditSessionId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ResponseTime` | `event.idm.read_only_udm.additional_fields` | Mapped from changelog  
`EndPointMACAddress` | `principal.asset.mac` | Mapped from changelog  
`CPMSessionID` | `network.session_id` | Mapped from changelog  
`StepLatency` | `additional.fields` | Mapped from changelog  
`TotalAuthenLatency` | `sec_result.detection_fields` | Mapped from changelog  
`ClientLatency` | `sec_result.detection_fields` | Mapped from changelog  
`HostIdentityGroup` | `additional_fields` | Mapped from changelog  
`ntp_server_1", "ntp_server_2", and "ntp_server_3` | `target.ip` | Mapped from changelog  
`column11` | `metadata.description` | Mapped from changelog  
`column14` | `metadata.product_log_id` | Mapped from changelog  
`column16` | `principal.hostname` | Mapped from changelog  
`user` | `principal.user.userid` | Mapped from changelog  
`Source` | `principal.ip` | Mapped from changelog  
`localport` | `principal.port` | Mapped from changelog  
`dc-protocol-map" , "audit-session-id" , "vlan-id" , "method" , "cisco-wlan-ssid" , "SelectedAccessService" , and "Network_Device_Profile` | `security_result.detection_fields` | Mapped from changelog  
`threshold_value` | `additional.fields` | Mapped from changelog  
`used_space_value` | `additional.fields` | Mapped from changelog  
`Nas-Port-id` | `security_result.detection_fields` | Mapped from changelog  
`UserName` | `principal.mac` | Mapped from changelog  
`SSID` | `security_result.detection_fields` | Mapped from changelog  
`RadiusFlowType` | `security_result.detection_fields` | Mapped from changelog  
`ExternalGroups` | `additional.fields` | Mapped from changelog  
`msg_sev` | `security_result.severity_details` | Mapped from changelog  
`r_total_seg", "r_seg_num", "msg_code", and "r_msg_id` | `security_result.detection_fields` | Mapped from changelog  
`r_cat_name` | `security_result.category_details` | Mapped from changelog  
`msg_text" and "msg_class` | `metadata.description` | Mapped from changelog  
`EndpointSourceEvent", "NASIdentifier", "NAS-Port-Type", "NAS-Port-Id", "ProfilerServer` | `security_result.detection_fields` | Mapped from changelog  
`cisco-av-pair=dhcp-option=host-name` | `target.hostname` | Mapped from changelog  
`FramedIPAddress` | `security_result.detection_fields` | Mapped from changelog  
`logstash.irm_region` | `additional.fields` | Mapped from changelog  
`logstash.irm_environment` | `additional.fields` | Mapped from changelog  
`logstash.irm_site` | `additional.fields` | Mapped from changelog  
`logstash.ingest.timestamp` | `metadata.ingested_timestamp` | Mapped from changelog  
`logstash.process.timestamp` | `metadata.collected_timestamp` | Mapped from changelog  
Log field | UDM mapping | Remark  
---|---|---  
`AAA_Event` | `security_result.detection_fields` |   
`AAA_Security_Result.detection_fields` | `aaa_service` |   
`ac-user-agent` | `network.http.user_agent` |   
`Acct-Authentic` | `security_result.detection_fields` |   
`Acct-Delay-Time` | `security_result.detection_fields` |   
`Acct-Input-Octets` | `security_result.detection_fields` |   
`Acct-Input-Packets` | `security_result.detection_fields` |   
`Acct-Output-Octets` | `security_result.detection_fields` |   
`Acct-Output-Packets` | `security_result.detection_fields` |   
`Acct-Session-Id` | `sec_result.detection_fields`  
`additional.fields` |   
`Acct-Session-Time` | `security_result.detection_fields` |   
`Acct-Status-Type` | `security_result.detection_fields` |   
`Acct-Terminate-Cause` | `security_result.detection_fields` |   
`AcctReply-Status` | `security_result.detection_fields` |   
`AcctRequest-Flags` | `security_result.detection_fields` |   
`ACS_CiscoSecure_Defined_ACL` | `security_result.detection_fields` |   
`AcsSessionID` | `sec_result.detection_fields`  
`additional.fields` |   
`Action` | `security_result.action_details` |   
`action_details` | `security_result.action_details` |   
`ActiveSessionCount` | `security_result.detection_fields` |   
`ad_identifier` | `about.hostname` |   
`ad_join_point` | `principal.administrative_domain` |   
`ad_operating_system` | `principal.platform` |   
`AD-Account-Name` | `principal.user.userid`  
`target.hostname` |   
`AD-Domain` | `principal.group.group_display_name` |   
`AD-Domain-Controller` | `target.administrative_domain` |   
`AD-Error-Details` | `security_result.description` |   
`AD-Forest` | `target.resource.attribute.labels` |   
`AD-Groups-Names` | `principal.user.group_identifiers` |   
`AD-Host-Candidate-Identities` | `sec_result.detection_fields` |   
`AD-IP-Address` | `target.ip`  
`target.asset.ip` |   
`AD-Log-Id` | `sec_result.detection_fields` |   
`AD-Site` | `target.location.name` |   
`AD-Srv-Query` | `security_result.detection_fields` |   
`AD-Srv-Record` | `security_result.detection_fields` |   
`AD-User-Candidate-Identities` | `principal.user.attribute.labels` |   
`AD-User-DNS-Domain` | `network.dns_domain` |   
`AD-User-Join-Point` | `target.hostname`  
`target.asset.hostname` |   
`AD-User-NetBios-Name` | `principal.user.attribute.labels` |   
`AD-User-Qualified-Name` | `principal.user.email_addresses` |   
`AD-User-Resolved-DNs` | `principal.user.attribute.labels` |   
`AD-User-Resolved-Identities` | `sec_result.detection_fields`  
`principal.user.userid` |   
`AD-User-Resolved-Identities` |  |   
`AD-User-SamAccount-Name` | `principal.user.attribute.labels` |   
`Admin` | `principal.user.userid` |   
`AdminInterface` | `principal.user.attribute.labels` |   
`AdminIPAddress` | `principal.ip` |   
`AdminName` | `principal.user.userid` |   
`affected-dn` | `target.resource.name``target.resource.attribute.labels`  
`target.resource.resource_type` | `target.resource.resource_type` => `"USER"`  
`Airespace-Wlan-Id` | `additional.fields` |   
`allowEasyWiredSession` | `sec_result.detection_fields`  
`additional.fields` |   
`AMInstalled` | `security_result.detection_fields` |   
`assetDeviceType` | `principal.resource.name` |   
`assetIncidentScore` | `security_result.detection_fields` |   
`Audit_session_id` | `sec_result.detection_fields` |   
`AuditSessionId` | `sec_result.detection_fields` |   
`Authen-Reply-Status` | `security_result.detection_fields` |   
`AuthenticationIdentityStore` | `sec_result.detection_fields`  
`additional.fields` |   
`AuthenticationMethod` | `security_result.detection_fields` |   
`AuthenticationResult` | `security_result.action` |   
`AuthenticationStatus` | `security_result.action`  
`security_result.action_details` |   
`Author-Reply-Status` | `additional.fields` |   
`AuthorizationFailureReason` | `security_result.detection_fields` |   
`AuthorizationPolicyMatchedRule` | `security_result.rule_name` |   
`av-pair-severity` | `security_result.detection_fields` |   
`BYODRegistration` | `sec_result.detection_fields` |   
`CacheUpdateTime` | `security_result.detection_fields` |   
`Called-Station-ID` | `security_result.detection_fields`  
`target.ip`  
`target.mac` |   
`Calling-Station-ID` | `security_result.detection_fields`  
`principal.ip`  
`principal.mac` |   
`cdpCacheAddressType` | `security_result.detection_fields` |   
`cdpCacheVersion` | `security_result.detection_fields` |   
`cdpUndefined28` | `security_result.detection_fields` |   
`change-set` | `additional.fields` |   
`Chargeable-User-Identity` | `principal.user.attribute.labels` |   
`cisco-av-pair` | `additional.fields`  
`security_result.detection_fields` |   
`CiscoIOS` | `security_result.detection_fields` |   
`Class` | `sec_result.detection_fields` |   
`client_type` | `additional.fields` |   
`client-iif-id` | `security_result.detection_fields` |   
`ClientLatency` | `security_result.detection_fields`  
`additional.fields` |   
`CmdSet` | `target.process.command_line` |   
`coa-push` | `security_result.detection_fields` |   
`CoAClientInstanceDestinationIPAddress` | `target.ip`  
`target.asset.ip` |   
`coaReason` | `security_result.detection_fields` |   
`coaSourceComponent` | `security_result.detection_fields` |   
`coaType` | `security_result.detection_fields` |   
`Component` | `security_result.detection_fields` |   
`ConfigChangeData` | `security_result.detection_fields` |   
`ConfigVersionId` | `sec_result.detection_fields`  
`additional.fields` |   
`connect-progress` | `security_result.detection_fields` |   
`ConnectionStatus` | `sec_result.detection_fields` |   
`ConnectionStatus=Failed` | `security_result.action ="BLOCK"` |   
`Constructeurs` | `principal.asset.hardware.manufacturer` |   
`counters_kvp` | `event.idm.read_only_udm.target.asset.attribute.labels` |   
`CPMSessionID` | `security_result.detection_fields`  
`additional.fields`  
`network.session_id` |   
`CreateTime` | `event.idm.read_only_udm.principal.asset.attribute.creation_time` |   
`cts_security_group_tag` | `security_result.detection_fields` |   
`cts-pac-opaque` | `security_result.detection_fields` |   
`datetime` | `metadata.event_timestamp` |   
`days_to_expiry` | `security_result.detection_fields` |   
`DeltaRadiusRequestCount` | `security_result.detection_fields` |   
`DeltaTacacsRequestCount` | `security_result.detection_fields` |   
`Description` | `security_result.detection_fields` |   
`DestinationIPAddress` | `target.ip`  
`target.asset.ip` |   
`DestinationIPAddress` | `target.ip`  
`target.asset.ip` |   
`DestinationPort` | `target.port` |   
`DetailedInfo` | `sec_result.description` |   
`Device_IP_Address` | `principal.ip`  
`principal.asset.ip` |   
`device-mac` | `principal.mac` |   
`device-platform` | `principal.platform` |   
`device-platform-version` | `principal.platform_version` |   
`device-public-mac` | `principal.mac` |   
`device-type` | `principal.asset.hardware.model` |   
`device-uid` | `principal.resource.product_object_id` |   
`device-uid-global` | `principal.asset.product_object_id` |   
`DeviceIPAddress` | `principal.ip`  
`target.ip`  
`intermediary.ip` |   
`DevicePort` | `principal.port`  
`target.port`  
`intermediary.port` |   
`DeviceRegistrationStatus` | `sec_result.detection_fields` |   
`dhcp-class-identifier` | `security_result.detection_fields` |   
`dhcp-parameter-request-list` | `additional.fields` |   
`Domaines` | `additional.fields` |   
`DoReplicate` | `security_result.detection_fields` |   
`DTLSSupport` | `security_result.detection_fields` |   
`EAP-Key-Name` | `additional.fields` |   
`EapTunnel` | `additional.fields` |   
`EmailAddress` | `principal.user.email_addresses` |   
`EnableFlag` | `additional.fields` |   
`EnableSingleConnect` | `security_result.detection_fields` |   
`End-of-LLDPDU` | `security_result.detection_fields` |   
`endpoint_id` | `principal.mac`  
`principal.asset.mac` |   
`EndpointCertainityMetric` | `sec_result.detection_fields` |   
`EndpointIdentityGroup` | `principal.group.group_display_name` |   
`EndpointIPAddress` | `principal.asset.ip` |   
`EndPointMACAddress` | `principal.mac`  
`principal.asset.mac` |   
`EndPointMatchedProfile` | `security_result.about.labels`  
`additional.fields` |   
`EndpointNADAddress` | `sec_result.detection_fields` |   
`EndpointOUI` | `sec_result.detection_fields` |   
`EndpointPolicy` | `principal.asset.platform_software.platform_version`  
`security_result.detection_fields` |   
`EndPointPolicyID` | `security_result.detection_fields` |   
`EndPointProfilerServer` | `target.hostname` |   
`EndpointProperty` | `sec_result.detection_fields` |   
`EndPointSource` | `target.resource.attribute.labels` |   
`EndpointSourceEvent` | `sec_result.detection_fields` |   
`EndpointUserAgent` | `network.http.user_agent` |   
`EndPointVersion` | `security_result.detection_fields` |   
`epid` | `security_result.detection_fields` |   
`Error Message` | `additional.fields` |   
`event` | `additional.fields` |   
`extended_key_usage_oid` | `additional.fields` |   
`external_groups` | `additional.fields` |   
`FailureFlag` | `security_result.detection_fields` |   
`FailureReason` | `sec_result.detection_fields`  
`additional.fields` |   
`FeedService` | `security_result.detection_fields` |   
`FirstCollection` | `event.idm.read_only_udm.principal.asset.first_discover_time` |   
`foreign_ip` | `intermediary.ip` |   
`FQSubjectName` | `security_result.detection_fields` |   
`Framed-MTU` | `additional.fields` |   
`Framed-Protocol` | `sec_result.detection_fields` |   
`FramedIPAddress` | `security_result.detection_fields` |   
`group_name` | `principal.group.group_display_name` |   
`Header-Flags` | `security_result.detection_fields` |   
`HostIdentityGroup` | `additional.fields` |   
`IdentityAccessRestricted` | `security_result.detection_fields` |   
`IdentityGroup` | `principal.group.group_display_name` |   
`IdentityGroupID` | `principal.group.product_object_id` |   
`IdentityPolicyMatchedRule` | `sec_result.about.labels`  
`additional.fields` |   
`IdentitySelectionMatchedRule` | `sec_result.detection_fields` |   
`Idle-Timeout` | `security_result.detection_fields` |   
`idletime` | `security_result.detection_fields` |   
`IMEI` | `target.asset.product_object_id` |   
`inacl_rule` | `security_result.detection_fields` |   
`intermediary_hostname` | `intermediary.hostname` |   
`ionTimeStamp` | `security_result.detection_fields` |   
`ios-version` | `principal.asset.software.version` |   
`ip_inacl_rule` | `security_result.detection_fields` |   
`ip_source_ip` | `principal.ip`  
`principal.asset.ip` |   
`IpAddress` | `principal.ip`  
`principal.asset.ip` |   
`IPSEC` | `additional.fields` |   
`ise_port` | `principal.port`  
`intermediary.port` |   
`ISELocalAddress` | `intermediary.ip`  
`principal.ip` |   
`ISEModuleName` | `sec_result.detection_fields` |   
`ISEPolicySetName` | `target.resource.name` |   
`ISEServiceName` | `sec_result.detection_fields` |   
`IsMachineAuthentication` | `security_result.detection_fields` |   
`IsMachineIdentity` | `security_result.detection_fields` |   
`IsRegistered` | `security_result.detection_fields` |   
`Issuer` | `about.labels` |   
`IsThirdPartyDeviceFlow` | `sec_result.detection_fields`  
`additional.fields` |   
`key_usage` | `additional.fields` |   
`LastActivity` | `event.idm.read_only_udm.principal.asset.last_discover_time` |   
`LastNmapScanTime` | `sec_result.detection_fields` |   
`LicenseType` | `additional.fields` |   
`lldpManAddress` | `security_result.detection_fields` |   
`lldpPortDescription` | `security_result.detection_fields` |   
`lldpPortId` | `security_result.detection_fields` |   
`lldpSystemCapabilitiesMap` | `security_result.detection_fields` |   
`lldpSystemDescription` | `security_result.detection_fields` |   
`lldpTimeToLive` | `security_result.detection_fields` |   
`lldpUndefined127` | `security_result.detection_fields` |   
`localport` | `principal.port` |   
`Location` | `principal.location.country_or_region`  
`target.location.country_or_region`  
`security_result.detection_fields` |   
`log-id` | `metadata.product_log_id` |   
`logstash.ingest.host` | `intermediary.hostname` |   
`logstash.ingest.timestamp` | `metadata.ingested_timestamp` |   
`logstash.irm_environment` | `additional.fields` |   
`logstash.irm_region` | `additional.fields` |   
`logstash.irm_site` | `additional.fields` |   
`logstash.process.host` | `intermediary.hostname` |   
`logstash.process.timestamp` | `metadata.collected_timestamp` |   
`MAC` | `principal.mac` |   
`mac_UserName` | `principal.mac` |   
`MacAddress` | `principal.mac` |   
`MajorVersion` | `security_result.detection_fields` |   
`Manufacturer` | `target.asset.hardware.manufacturer` |   
`MatchedPolicy` | `security_result.detection_fields` |   
`MatchedPolicyID` | `security_result.rule_id` |   
`MDMFailureReason` | `sec_result.detection_fields` |   
`MDMServerName` | `metadata.product_name` |   
`mDNS` | `security_result.detection_fields` |   
`MESSAGE` | `security_result.description` |   
`MFCInfoEndpointType` | `principal.asset.asset_type`  
`principal.asset.attribute.labels` |   
`MinorVersion` | `security_result.detection_fields` |   
`MisconfiguredClientFixReason` | `security_result.detection_fields` |   
`Model` | `target.asset.hardware.model` |   
`Model_Name` | `principal.asset.attribute.labels` |   
`msg_class` | `metadata.description` |   
`msg_sev` | `security_result.severity`  
`sec_result.severity_details` |   
`msg_text` | `metadata.description`  
`security_result.severity`  
`sec_result.severity_details,security_result.action` |   
`msg_text` | `security_result.action` |   
`NAD Address` | `principal.ip` |   
`NADAddress` | `intermediary.ip` |   
`Name` | `principal.group.group_identifiers` |   
`nas_ip_address` | `principal.nat_ip` |   
`NAS-Identifier` | `principal.labels` |   
`NAS-IP-Address` | `principal.nat_ip`  
`principal.ip` |   
`NAS-Port` | `principal.port`  
`principal.labels` |   
`nas-update` | `security_result.detection_fields` |   
`NASIdentifier` | `security_result.detection_fields`  
`principal.labels` |   
`NASPort` | `principal.nat_port if valid else to security_result.detection_fields`  
`principal.labels` |   
`NASPortId` | `security_result.detection_fields`  
`principal.labels` |   
`NASPortType` | `security_result.detection_fields`  
`principal.labels` |   
`Network Device Name` | `target.hostname`  
`target.asset.hostname` |   
`network_adapter` | `target.resource.name` |   
`network_application_protocol_result` | `network.application_protocol` |   
`NetworkDeviceGroups` | `sec_result.detection_fields` |   
`NetworkDeviceGroups_IPSEC` | `additional.fields` |   
`NetworkDeviceProfileId` | `principal.asset.asset_id` |   
`NetworkDeviceProfileName` | `principal.asset.attribute.labels` |   
`NmapScanCount` | `security_result.detection_fields` |   
`ntp_server_1` | `target.ip`  
`target.asset.ip` |   
`ntp_server_2` | `target.ip`  
`target.asset.ip` |   
`ntp_server_3` | `target.ip`  
`target.asset.ip` |   
`ObjectInternalID` | `security_result.detection_fields` |   
`ObjectName` | `security_result.about.labels` |   
`ObjectType` | `security_result.labout.abels`  
`additional.fields` |   
`operating-system-result` | `target.asset.platform_software.platform_version` | `target.platform` = `WINDOWS`  
`OperatingSystem` | `target.asset.platform_software.platform_version` |   
`OperationMessageText` | `sec_result.detection_fields` |   
`OperationMessageText` | `about.labels` |   
`OUI` | `security_result.detection_fields` |   
`pad` | `security_result.detection_fields` |   
`PeerAddress` | `target.mac`  
`target.asset.mac` |   
`PeerName` | `target.hostname`  
`target.asset.hostname` |   
`PhoneNumber` | `principal.user.phone_numbers` |   
`platform-version` | `principal.platform_version` |   
`PolicyVersion` | `security_result.detection_fields` |   
`Port` | `principal.port`  
`target.port` |   
`Portal_Name` | `additional.fields` |   
`PortalName` | `target.url` |   
`PortalUser` | `principal.user.userid` |   
`PortalUser_GuestSponsor` | `principal.user.attribute.labels` |   
`PortalUser_GuestType` | `principal.user.attribute.labels` |   
`PostureApplicable` | `security_result.detection_fields` |   
`PostureAssessmentStatus` | `sec_result.detection_fields`  
`additional.fields` |   
`PostureExpiry` | `sec_result.detection_fields` |   
`PostureStatus` | `sec_result.detection_fields` |   
`principal_hostname` | `principal.hostname` |   
`principal_ip` | `principal.ip`  
`principal.asset.ip` |   
`profile-name` | `security_result.detection_fields` |   
`ProfilerServer` | `sec_result.detection_fields` |   
`Protocol` | `security_result.detection_fields` |   
`r_ip_or_host` | `observer.ip`  
`observer.hostname`  
`intermediary.hostname`  
`intermediary.ip` |   
`r_seg_num` | `metadata.product_log_id` |   
`RadiusFlowType` | `security_result.about.labels`  
`additional.fields` |   
`RadiusPacketType` | `security_result.detection_fields` |   
`received_b` | `network.received_bytes` |   
`RegisterStatus` | `security_result.rule_name` |   
`RegistrationTimeStamp` | `sec_result.detection_fields` |   
`RemoteAddress` | `principal.ip`  
`principal.asset.ip` |   
`RequestLatency` | `sec_result.detection_fields`  
`additional.fields` |   
`RequestResponseTypes` | `security_result.detection_fields` |   
`ResponseTime` | `sec_result.detection_fields` |   
`SelectedAccessService` | `sec_result.detection_fields`  
`additional.fields` |   
`SelectedAuthenticationIdentityStores` | `security_result.detection_fields` |   
`SelectedAuthorizationProfiles` | `sec_result.detection_fields`  
`additional.fields` |   
`SelectedShellProfile` | `additional.fields` |   
`sent_b` | `network.sent_bytes` |   
`sequence_num` | `metadata.product_log_id` |   
`Sequence-Number` | `security_result.detection_fields` |   
`serial_number` | `about.labels`  
`network.tls.server.certificate.serial` |   
`server_label` | `principal.asset.attribute.labels` |   
`Service-Type` | `sec_result.detection_fields`  
`additional.fields` |   
`session-id` | `network.session_id` |   
`Session-Timeout` | `network.session_duration` |   
`shell_role` | `principal.user.attribute.roles.name` |   
`ShutdownReason` | `security_result.detection_fields` |   
`SkipProfiling` | `security_result.detection_fields` |   
`software_version` | `principal.asset.platform_software.platform_version` |   
`Source` | `principal.ip`  
`principal.hostname` |   
`source_ip` | `src.ip` |   
`source_port` | `src.port` |   
`SSID` | `additional.fields` |   
`start_time` | `security_result.first_discovered_time` |   
`StaticAssignment` | `security_result.detection_fields` |   
`StaticGroupAssignment` | `sec_result.detection_fields` |   
`Step` | `additional.fields` |   
`StepData` | `about.hostname`  
`additional.fields` |   
`StepLatency` | `additional.fields` |   
`stop_time` | `security_result.last_discovered_time` |   
`Subject` | `about.labels` |   
`subject_alt_name` | `about.labels` |   
`subscriber_command` | `security_result.detection_fields` |   
`syslog_host` | `principal.ip`  
`principal.asset.ip` |   
`SysStatsCpuCount` | `target.asset.hardware.cpu_number_cores` |   
`SysStatsProcessMemoryMB` | `target.asset.hardware.ram` |   
`SysStatsUtilizationDiskIO` | `target.asset.attribute.labels` |   
`SysStatsUtilizationDiskSpace` | `target.asset.attribute.labels` |   
`SysStatsUtilizationLoadAvg` | `target.asset.attribute.labels` |   
`SystemDomain` | `principal.asset.network_domain` |   
`SystemName` | `principal.hostname`  
`principal.hostname` |   
`SystemUser` | `principal.user.userid` |   
`SystemUserDomain` | `principal.administrative_domain` |   
`target_email` | `target.user.email_addresses` |   
`target_group_identifiers` | `target.user.group_identifiers` |   
`target_hostname` | `target.hostname` |   
`target_ip` | `target.ip`  
`target.asset.ip` |   
`target_port` | `target.port` |   
`target_user` | `target.user.userid` |   
`target.resource.resource_type` |  | DEVICE  
`task_id` | `additional.fields` |   
`TaskId` | `security_result.detection_fields` |   
`Template_Name` | `additional.fields` |   
`Termination-Action` | `security_result.detection_fields` |   
`threshold_value` | `additional.fields` |   
`TimeToProfile` | `sec_result.detection_fields` |   
`TLSCipher` | `network.tls.cipher` |   
`TLSVersion` | `network.tls.version` |   
`total_certainty_factor` | `sec_result.detection_fields` |   
`TotalAuthenLatency` | `security_result.detection_fields`  
`additional.fields` |   
`TotalFailedTime` | `sec_result.detection_fields` |   
`Tunnel-Client-Endpoint` | `sec_result.detection_fields` |   
`Type` | `additional.fields` |   
`undefined-151` | `additional.fields` |   
`UniqueConnectionIdentifier` | `sec_result.detection_fields` |   
`UpdateTime` | `sec_result.detection_fields` |   
`url-redirect` | `target.url` |   
`url-redirect-acl` | `security_result.detection_fields` |   
`UseCase` | `sec_result.detection_fields` |   
`used_space_value` | `additional.fields` |   
`User` | `principal.user.userid` |   
`user` | `principal.user.userid` |   
`user_display_name` | `principal.user.user_display_name` |   
`User-AD-Last-Fetch-Time` | `principal.user.attribute.labels` |   
`User-Agent` | `network.http.user_agent`  
`network.http.parsed_user_agent` |   
`User-Fetch-Email` | `sec_result.detection_fields` |   
`User-Fetch-Last-Name` | `principal.user.last_name` |   
`User-Fetch-LocalityName` | `sec_result.detection_fields` |   
`User-Fetch-StateOrProvinceName` | `sec_result.detection_fields` |   
`User-Name` | `target.user.userid` |   
`UserAccountControl` | `principal.user.attribute.labels` |   
`UserAgreementStatus` | `security_result.detection_fields` |   
`UserName` | `target.user.userid` |   
`UserType` | `principal.user.attribute.labels` |   
`UseSingleConnect` | `security_result.detection_fields` |   
`vlan-id` | `security_result.detection_fields` |   
| `principal.resource.resource_type` | Statically mapped to `DEVICE`.  
  
## UDM mapping delta reference

On December 1, 2025, Google SecOps released a new version of the Cisco ISE parser, which includes significant changes to the mapping of Cisco ISE log fields to UDM fields and changes to the mapping of event types.

### Log-field mapping delta

Globally, the timestamp that the Cisco ISE parser displays now is the raw log field `Event-Timestamp`. Previously, the timestamp that the Cisco ISE parser displayed was from the header.

The following table lists the mapping delta for Cisco ISE log-to-UDM fields exposed prior to December 1, 2025 and subsequently (listed in the **Old mapping** and **Current mapping** columns respectively):

Log field | Old mapping | Current mapping  
---|---|---  
`Acct-Input-Gigawords` | `additional.fields` | `network.received_bytes`  
`Acct-Input-Packets` | `security_result.detection_fields` | `network.received_packets`  
`Acct-Output-Gigawords` | `additional.fields` | `network.sent_bytes`  
`Acct-Output-Packets` | `security_result.detection_fields` | `network.sent_packets`  
`Acct-Session-Id` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`AcsSessionID` | `security_result.detection_fields`  
`additional.fields` | `network.session_id`  
`security_result.detection_fields`  
`AD-Log-Id` | `security_result.detection_fields` | `metadata.product_log_id`  
`AD-User-SamAccount-Name` | `principal.user.attribute.labels` | `principal.user.user_display_name`  
`allowEasyWiredSession` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`AuthenticationIdentityStore` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`Calling-Station-ID` | `security_result.detection_fields`  
`additional.fields`  
`principal.ip` | `security_result.detection_fields`  
`ClientLatency` | `security_result.detection_fields`  
`additional.fields` | ``security_result.detection_fields`  
`ConfigVersionId` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`CPMSessionID` | `security_result.detection_fields`  
`additional.fields`  
`network.sesson_id` | `network.sesson_id`  
`DeviceIPAdresstarget.ip` | `target.ip` | `principal.ip`  
`EndPointMatchedProfile` | `security_result.about.labels`  
`additional.fields` | `security_result.about.resource.attribute.labels`  
`HostIdentityGroup` | `additional.fields` | `principal.group.group_display_name`  
`IdentityGroup` | `principal.group.group_display_name` | `principal.user.group_identifiers`  
`IdentityPolicyMatchedRule` | `security_result.about.labels`  
`additional.fields` | `security_result.rule_labels`  
`IsThirdPartyDeviceFlow` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`Issuer` | `about.labels` | `network.tls.server.certificate.issuer`  
`Location` | `principal.location.country_or_region`  
`target.location.country_or_region,security_result.detection_fields` | `principal.location.country_or_region,`  
`NAS Identifier` | `principal.labels` | `principal.asset.attribute.labels`  
`NAS-IP-Address` | `principal.nat_ip,principal.ip`  
`intermediary.ip` | `principal.nat_ip,principal.ip,`  
`NAS-Port` | `principal.labels` | `principal.resource.attribute.labels`  
`NAS-Port-Id` | `security_result.detection_fields`  
`principal.labels` | `security_result.detection_fields`  
`NAS-Port-Type` | `security_result.detection_fields`  
`principal.labels` | ``security_result.detection_fields`  
`NASIdentifier` | `principal.resource.attribute.labels,security_result.detection_fields` | `principal.resource.attribute.labels`  
`NASIdentifier` | `security_result.detection_fields`  
`principal.labels` | `security_result.detection_fields`  
`NetworkDeviceGroups_Location` | `intermediary.location.country_or_region` | `principal.location.country_or_region,`  
`Object Name` | `security_result.about.labels` | `security_result.about.resource.attribute.labels`  
`principal.mac` if it is a MAC  
`Object Type` | `security_result.about.labels`  
`additional.fields` | `security_result.about.resource.attribute.labels`  
`PostureAssessmentStatus` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`Privilege-Level` | `additional.fields` | `target.user.attribute.permissions.description`  
`ProfilerServer` | `principal.hostname`  
`security_result.detection_fields` | `principal.hostname`  
`RadiusFlowType` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`RequestLatency` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`r_msg_id` | `security_result.detection_fields` | `metadata.product_log_id`  
`r_seg_num` | `security_result.detection_fields`  
`additional.fields` | `additional.fields`  
`r_total_seg` | `security_result.detection_fields`  
`additional.fields` | `additional.fields`  
`SelectedAccessService` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`SelectedAuthorizationProfiles` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`Sequence-Number` | `metadata.product_log_id` | `security_result.detection_fields` if `AD-Log-Id` is not null  
`Server` | `principal.asset.attribute.labels` | `principal.hostname`  
`principal.asset.hostname`  
`Service-Type` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`serial_number` | `about.labels` | `about.resource.attribute.labels`  
`ShutdownReason` | `security_result.detection_fields` | `security_result.description`  
`Subject` | `about.labels` | `about.resource.attribute.labels`  
`subject_alt_name` | `about.labels` | `about.resource.attribute.labels`  
`subject_alt_name` | `about.labels` | `about.resource.attribute.labels`  
`TotalAuthenLatency` | `security_result.detection_fields`  
`additional.fields` | `security_result.detection_fields`  
`total_certainty_factor` | `security_result.detection_fields` | `security_result.confidence_score`  
`UniqueSubjectID` | `additional.fields` | `principal.user.userid.product_object_id`  
`Update Time` | `security_result.detection_fields` | `principal.asset.attribute.last_update_time`  
`User-Fetch-Email` | `security_result.detection_fields` | `principal.user.email_addresses`  
`User-Fetch-LocalityName` | `security_result.detection_fields` | `principal.location.name`  
`User-Fetch-StateOrProvinceName` | `security_result.detection_fields` | `principal.location.state`  
`User Name when [r_cat_name] =~ "CISE_Passed_Authentications"` | `principal.user.userid`  
`target.user.userid` | `principal.user.userid`  
`wlan-profile-name` | `security_result.detection_fields` | `principal.user.userid`  
  
### Event-type mapping delta

Multiple events that were classified generically are now properly classified with meaningful event types.

The following table lists the delta for the handling of Cisco ISE event types prior to December 1, 2025 and subsequently (listed in the **Old event_type** and **Current event-type** columns respectively):

Event ID from log and logic | Old event_type | Current event_type  
---|---|---  
(Based on event) `[has_resource] == "true"` | `GENERIC_EVENT` | `USER_RESOURCE_ACCESS`  
`[Action] == "Login"` | `NETWORK_CONNECTION` | `USER_LOGIN`  
`[PRAAction] =~ "logoff"` | `NETWORK_CONNECTION` | `USER_LOGOUT`  
`[message] =~ "Administrator-Login"` | `USER_UNCATEGORIZED` | `USER_LOGIN`  
`[message] =~ "Change password failed"` | `USER_LOGIN` | `USER_CHANGE_PASSWORD`  
`[msg_text] =~ "Login Success"` | `USER_UNCATEGORIZED` | `USER_LOGIN`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ise-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
