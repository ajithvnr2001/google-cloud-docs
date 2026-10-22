---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-acs/
title: Collect Cisco Secure ACS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:56.851685+00:00
---

# Collect Cisco Secure ACS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-acs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Secure ACS logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Secure ACS logs to Google Security Operations using Bindplane.

The parser extracts fields from Cisco Secure ACS syslog and key-value formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco Secure ACS web interface



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
            log_type: 'CISCO_ACS'
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
      * `log_type`: Log type exactly as it appears in Chronicle (`CISCO_ACS`)



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'CISCO_ACS'
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
             




## Configure Syslog forwarding on Cisco Secure ACS

  1. Sign in to the **Cisco Secure ACS** web interface.
  2. Go to **System Administration > Configuration > Log Configuration > Remote Log Targets**.
  3. Click **Create** to add a new remote log target.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google-SecOps-Bindplane`).
     * **Description** : Enter a description (optional).
     * **IP Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Facility Code** : Select **LOCAL6** (or your preferred facility).
  5. Click **Submit**.
  6. Go to **System Administration > Configuration > Log Configuration > Logging Categories**.
  7. Select the log categories to forward: 
     * **AAA Audit**
     * **AAA Diagnostics**
     * **Administrative and Operational Audit**
     * **System Diagnostics**
  8. For each selected category, click the category name.
  9. Go to the **Remote Log Target** tab.
  10. Move the created remote log target (for example, `Google-SecOps-Bindplane`) from **Available** to **Selected**.
  11. Click **Save**.
  12. Verify syslog messages are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
Acct-Authentic | additional.fields[].value.string_value | Value is taken from the Acct-Authentic field.  
Acct-Delay-Time | additional.fields[].value.string_value | Value is taken from the Acct-Delay-Time field.  
Acct-Input-Octets | additional.fields[].value.string_value | Value is taken from the Acct-Input-Octets field.  
Acct-Input-Packets | additional.fields[].value.string_value | Value is taken from the Acct-Input-Packets field.  
Acct-Output-Octets | additional.fields[].value.string_value | Value is taken from the Acct-Output-Octets field.  
Acct-Output-Packets | additional.fields[].value.string_value | Value is taken from the Acct-Output-Packets field.  
Acct-Session-Id | additional.fields[].value.string_value | Value is taken from the Acct-Session-Id field.  
Acct-Session-Time | additional.fields[].value.string_value | Value is taken from the Acct-Session-Time field.  
Acct-Status-Type | additional.fields[].value.string_value | Value is taken from the Acct-Status-Type field.  
Acct-Terminate-Cause | additional.fields[].value.string_value | Value is taken from the Acct-Terminate-Cause field.  
ACSVersion | additional.fields[].value.string_value | Value is taken from the ACSVersion field.  
AD-Domain | principal.group.group_display_name | Value is taken from the AD-Domain field.  
AD-IP-Address | principal.ip | Value is taken from the AD-IP-Address field.  
Called-Station-ID | additional.fields[].value.string_value | Value is taken from the Called-Station-ID field.  
Calling-Station-ID | additional.fields[].value.string_value | Value is taken from the Calling-Station-ID field.  
Class | additional.fields[].value.string_value | Value is taken from the Class field.  
CmdSet | (not mapped) | Not mapped to the IDM object.  
ConfigVersionId | additional.fields[].value.number_value | Value is taken from the ConfigVersionId field and converted to a float.  
DestinationIPAddress | target.ip, intermediary.ip | Value is taken from the DestinationIPAddress field. intermediary.ip is derived from Device IP Address.  
DestinationPort | target.port | Value is taken from the DestinationPort field and converted to an integer.  
Device IP Address | intermediary.ip | Value is taken from the Device IP Address field.  
Device Port | intermediary.port | Value is taken from the Device Port field and converted to an integer.  
DetailedInfo | security_result.summary, security_result.description, security_result.action | If DetailedInfo is "Authentication succeed", security_result.summary is "successful login occurred" and security_result.action is ALLOW. If DetailedInfo contains "Invalid username or password specified", security_result.summary is "failed login occurred" and security_result.action is BLOCK. security_result.description is derived from log_header.  
Framed-IP-Address | principal.ip | Value is taken from the Framed-IP-Address field.  
Framed-Protocol | additional.fields[].value.string_value | Value is taken from the Framed-Protocol field.  
NAS-IP-Address | target.ip | Value is taken from the NAS-IP-Address field.  
NAS-Port | additional.fields[].value.string_value | Value is taken from the NAS-Port field.  
NAS-Port-Id | target.port | Value is taken from the NAS-Port-Id field and converted to an integer.  
NAS-Port-Type | additional.fields[].value.string_value | Value is taken from the NAS-Port-Type field.  
NetworkDeviceName | target.hostname | Value is taken from the NetworkDeviceName field.  
Protocol | additional.fields[].value.string_value | Value is taken from the Protocol field.  
RadiusPacketType | (not mapped) | Not mapped to the IDM object.  
Remote-Address | principal.ip, target.ip | Value is taken from the Remote-Address field and parsed as an IP address. It is mapped to principal.ip for authentication events and target.ip for accounting and diagnostic events.  
RequestLatency | additional.fields[].value.string_value | Value is taken from the RequestLatency field.  
Response | principal.user.userid | If Response contains "User-Name", the username is extracted and mapped to principal.user.userid.  
SelectedAccessService | additional.fields[].value.string_value | Value is taken from the SelectedAccessService field.  
SelectedAuthenticationIdentityStores | security_result.detection_fields[].value | Value is taken from the SelectedAuthenticationIdentityStores field.  
SelectedAuthorizationProfiles | security_result.detection_fields[].value | Value is taken from the SelectedAuthorizationProfiles field.  
Service-Type | additional.fields[].value.string_value | Value is taken from the Service-Type field.  
Tunnel-Client-Endpoint | additional.fields[].value.string_value | Value is taken from the Tunnel-Client-Endpoint field and parsed as an IP address.  
User | target.user.userid | Value is taken from the User field.  
UserName | target.user.userid, principal.mac | If UserName is a MAC address, it is parsed and mapped to principal.mac. Otherwise, it is mapped to target.user.userid.  
ac-user-agent | network.http.user_agent | Value is taken from the ac-user-agent field.  
cat | metadata.description | Value is taken from the cat field.  
device-mac | principal.mac | Value is taken from the device-mac field, colons are added, and the value is converted to lowercase. If device-mac is "00", it is replaced with "00:00:00:00:00:00".  
device-platform | principal.asset.platform_software.platform | If device-platform is "win", the value "WINDOWS" is assigned to principal.asset.platform_software.platform.  
device-platform-version | principal.asset.platform_software.platform_version | Value is taken from the device-platform-version field.  
device-public-mac | principal.mac | Value is taken from the device-public-mac field, hyphens are replaced with colons, and the value is converted to lowercase.  
device-type | principal.asset.hardware.model | Value is taken from the device-type field.  
device-uid | principal.asset.asset_id | Value is taken from the device-uid field and prepended with "ASSET ID: ".  
device-uid-global | principal.asset.product_object_id | Value is taken from the device-uid-global field.  
hostname | principal.hostname | Value is taken from the hostname field.  
ip:source-ip | principal.ip | Value is taken from the ip:source-ip field.  
kv.ADDomain | (not mapped) | Not mapped to the IDM object.  
kv.Airespace-Wlan-Id | (not mapped) | Not mapped to the IDM object.  
kv.AuthenticationIdentityStore | (not mapped) | Not mapped to the IDM object.  
kv.AVPair | (not mapped) | Not mapped to the IDM object.  
kv.CVPN3000/ASA/PIX7.x-DAP-Tunnel-Group-Name | (not mapped) | Not mapped to the IDM object.  
kv.CVPN3000/ASA/PIX7.x-Group-Based-Address-Pools | (not mapped) | Not mapped to the IDM object.  
kv.ExternalGroups | (not mapped) | Not mapped to the IDM object.  
kv.FailureReason | (not mapped) | Not mapped to the IDM object.  
kv.IdentityAccessRestricted | (not mapped) | Not mapped to the IDM object.  
kv.IdentityGroup | (not mapped) | Not mapped to the IDM object.  
kv.NAS-Identifier | (not mapped) | Not mapped to the IDM object.  
kv.SelectedShellProfile | (not mapped) | Not mapped to the IDM object.  
kv.ServiceSelectionMatchedRule | (not mapped) | Not mapped to the IDM object.  
kv.State | (not mapped) | Not mapped to the IDM object.  
kv.Step | (not mapped) | Not mapped to the IDM object.  
kv.Tunnel-Medium-Type | (not mapped) | Not mapped to the IDM object.  
kv.Tunnel-Private-Group-ID | (not mapped) | Not mapped to the IDM object.  
kv.Tunnel-Type | (not mapped) | Not mapped to the IDM object.  
kv.UseCase | (not mapped) | Not mapped to the IDM object.  
kv.UserIdentityGroup | (not mapped) | Not mapped to the IDM object.  
kv.VendorSpecific | (not mapped) | Not mapped to the IDM object.  
kv.attribute-131 | (not mapped) | Not mapped to the IDM object.  
kv.attribute-89 | (not mapped) | Not mapped to the IDM object.  
kv.cisco-av-pair | (not mapped) | Not mapped to the IDM object.  
kv.cisco-av-pair:CiscoSecure-Group-Id | (not mapped) | Not mapped to the IDM object.  
leef_version | (not mapped) | Not mapped to the IDM object.  
log_header | metadata.description | Value is taken from the log_header field.  
log_id | metadata.product_log_id | Value is taken from the log_id field.  
log_type | metadata.product_event_type | Value is taken from the log_type field.  
message_severity | (not mapped) | Not mapped to the IDM object.  
product | metadata.product_name | Value is taken from the product field.  
product_version | metadata.product_version | Value is taken from the product_version field.  
server_host | target.hostname | Value is taken from the server_host field.  
timestamp | metadata.event_timestamp | Value is taken from the timestamp field and the timezone field (after removing the colon). The combined value is parsed as a timestamp.  
url | network.dns.questions[].name | Value is taken from the url field.  
vendor | metadata.vendor_name | Value is taken from the vendor field. Set to "GENERIC_EVENT" initially, then potentially overwritten based on the log_type and parsed fields. Can be "USER_LOGIN", "USER_UNCATEGORIZED", "NETWORK_DNS", "NETWORK_CONNECTION", "STATUS_UPDATE", or "STATUS_UNCATEGORIZED". Set to "Cisco" initially, then potentially overwritten by the vendor field. Set to "ACS" initially, then potentially overwritten by the product field. Set to "CISCO_ACS". Set to "USERNAME_PASSWORD". Set to "TACACS". Set to "UDP" for RADIUS accounting and diagnostic events. Set to "DNS" for DNS events. Derived from the security_action field, which is set based on whether the login was successful or not. Set to "successful login occurred" for successful logins and "failed login occurred" for failed logins. May also be set to "passed" for certain identity store diagnostic events. Set to "LOW" for failed login attempts. Constructed by prepending "ASSET ID: " to the device-uid field.  
`hostname` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`kv.NAS-IP-Address` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`kv.source_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`kv.NetworkDeviceName` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`kv.Remote-Address` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`kv.DeviceIPAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`kv.AD-IP-Address` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`kv.Framed-IP-Address` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`kv.Caller-Id` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`kv.Group-Name` | `event.idm.read_only_udm.principal.group.group_display_name` | Mapped from changelog  
`kv.Session ID` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`kv.FailureReason` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`kv.IdentityPolicyMatchedRule` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`kv.ServiceSelectionMatchedRule` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`kv.cmd` | `event.idm.read_only_udm.principal.process.command_line` | Mapped from changelog  
`kv.Network Device Group` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Access Device` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Priv-lvl` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Network Access Profile Name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Authen-Failure-Code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Message-Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Privilege-Level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Authen-Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.NAS-Portname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.priv-lvl` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.task_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Acct-Flags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Acct-Method` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Acct-Type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.Acct-Service` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.timezone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.AAA Server` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.start_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`steps` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.NetworkDeviceGroups` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`kv.AuthenticationMethod` | `additional.fields` | Mapped from changelog  
`kv.SelectedAccessService` | `additional.fields` | Mapped from changelog  
`kv.SelectedAuthorizationProfiles` | `security_result.detection_fields` | Mapped from changelog  
`kv.SelectedAuthenticationIdentityStores` | `security_result.detection_fields` | Mapped from changelog  
`kv.device-uid-global` | `principal.asset.product_object_id` | Mapped from changelog  
`kv.device-uid` | `principal.asset.asset_id` | Mapped from changelog  
`metadata.event_type` | `USER_UNCATEGORIZED` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-acs-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
