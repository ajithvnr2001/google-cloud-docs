---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/clearpass/
title: Collect Aruba ClearPass logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:40.326077+00:00
---

# Collect Aruba ClearPass logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/clearpass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Aruba ClearPass logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Aruba ClearPass logs to Google Security Operations using the Bindplane agent.

Aruba ClearPass Policy Manager generates syslog messages for RADIUS authentication, TACACS+, web authentication, endpoint posture, guest access, audit records, and system events. The parser maps extracted fields to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the ClearPass Policy Manager
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the ClearPass Policy Manager console



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
          chronicle/clearpass:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CLEARPASS
            raw_log_field: body
        
        service:
          pipelines:
            logs/clearpass_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/clearpass
        




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
          chronicle/clearpass:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CLEARPASS
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
             




## Configure Aruba ClearPass syslog server

  1. Sign in to the **ClearPass Policy Manager** console.
  2. Select **Administration > External servers > Syslog targets**.
  3. Click **Add**.
  4. In the **Add syslog target** window that appears, specify the following details: 
     * **Host address** : enter the Bindplane IP address.
     * **Server port** : enter the Bindplane port number.
     * **Protocol** : select **UDP** (you can also select **TCP** , depending on your Bindplane configuration).
  5. Click **Save**.



## Configure syslog export filters

  1. Go to **Administration > External servers > Syslog export filters**.
  2. Click **Add**.
  3. In the **Add Syslog Filters** window that appears, specify the following in the **General** tab: 
     * **Name** : enter the syslog export filter name based on the table in Export template items.
     * **Export template** : select the appropriate export template based on the table in Export template items.
     * **Export event format type** : select **Standard**.
     * **Syslog servers** : select the Bindplane IP address.
  4. In the **Export template** list, when you select the **Session** or **Insight** export templates, the **Filter and columns** tab is enabled. Complete the following steps: 
     * Click the **Filter and columns** tab.
     * **Data filter** : make sure the default value **All requests** is selected.
     * **Column selection** : select the predefined field group based on the table in Export template items.
     * **Selected columns** : verify that the automatically populated fields match the table in Export template items.
     * Click the **Summary** tab.
     * Click **Save**.
  5. In the **Export template** list, when you select the **System events** and **Audit records** export templates, the **Filter and columns** tab is not enabled. Proceed to the **Summary** tab and click **Save**.
  6. Repeat steps to add syslog export filters for all **Session** , **Insight** , **Audit records** and **System events** export templates based on the details from the table in Export template items.



## Export template items

The following table describes the items that you need to configure for each export template. The default fields that are listed in Selected Columns are supported for event parsing. Ensure all fields that are mentioned in the table under Selected columns (default) are present and in the same order. Make sure to create syslog export filter templates exactly as provided in table, including the case-sensitive name of the filter.

**Note:** You can add more fields from Available Columns but these fields are not supported for event parsing and available in raw logs.Syslog export filter name (case sensitive) | Export template | Predefined field groups | Selected columns (default)  
---|---|---|---  
`ACPPM_radauth` | Insight Logs | Radius Authentications | Auth.Username, Auth.Host-MAC-Address, Auth.Protocol, Auth.NAS-IP-Address, CppmNode.CPPM-Node, Auth.Login-Status, Auth.Service, Auth.Source, Auth.Roles, Auth.Enforcement-Profiles  
`ACPPM_radfailedauth` | Insight Logs | Radius Failed Authentications | Auth.Username, Auth.Host-MAC-Address, Auth.NAS-IP-Address, CppmNode.CPPM-Node, Auth.Service, CppmErrorCode.Error-Code-Details, CppmAlert.Alerts  
`ACPPM_radacct` | Insight Logs | RADIUS Accounting | Radius.Username, Radius.Calling-Station-Id, Radius.Framed-IP-Address, Radius.NAS-IP-Address, Radius.Start-Time, Radius.End-Time, Radius.Duration, Radius.Input-bytes, Radius.Output-bytes  
`ACPPM_tacauth` | Insight Logs | tacacs Authentication | tacacs.Username, tacacs.Remote-Address, tacacs.Request-Type, tacacs.NAS-IP-Address, tacacs.Service, tacacs.Auth-Source, tacacs.Roles, tacacs.Enforcement-Profiles, tacacs.Privilege-Level  
`ACPPM_tacfailedauth` | Insight Logs | tacacs Failed Authentication | tacacs.Username, tacacs.Remote-Address, tacacs.Request-Type, tacacs.NAS-IP-Address, tacacs.Service, CppmErrorCode.Error-Code-Details, CppmAlert.Alerts  
`ACPPM_webauth` | Insight Logs | WEBAUTH | Auth.Username, Auth.Host-MAC-Address, Auth.Host-IP-Address, Auth.Protocol, Auth.System-Posture-Token, CppmNode.CPPM-Node, Auth.Login-Status, Auth.Service, Auth.Source, Auth.Roles, Auth.Enforcement-Profiles  
`ACPPM_webfailedauth` | Insight Logs | WEBAUTH Failed Authentications | Auth.Username, Auth.Host-MAC-Address, Auth.Host-IP-Address, Auth.Protocol, Auth.System-Posture-Token, CppmNode.CPPM-Node, Auth.Login-Status, Auth.Service, CppmErrorCode.Error-Code-Details, CppmAlert.Alerts  
`ACPPM_appauth` | Insight Logs | Application Authentication | Auth.Username, Auth.Host-IP-Address, Auth.Protocol, CppmNode.CPPM-Node, Auth.Login-Status, Auth.Service, Auth.Source, Auth.Roles, Auth.Enforcement-Profiles  
`ACPPM_failedappauth` | Insight Logs | Failed Application Authentication | Auth.Username, Auth.Host-IP-Address, Auth.Protocol, CppmNode.CPPM-Node, Auth.Login-Status, Auth.Service, CppmErrorCode.Error-Code-Details, CppmAlert.Alerts  
`ACPPM_endpoints` | Insight Logs | Endpoints | Endpoint.MAC-Address, Endpoint.MAC-Vendor, Endpoint.IP-Address, Endpoint.Username, Endpoint.Device-Category, Endpoint.Device-Family, Endpoint.Device-Name, Endpoint.Conflict, Endpoint.Status, Endpoint.Added-At, Endpoint.Updated-At  
`ACPPM_cpguest` | Insight Logs | Clearpass Guest | Guest.Username, Guest.MAC-Address, Guest.Visitor-Name, Guest.Visitor-Company, Guest.Role-Name, Guest.Enabled, Guest.Created-At, Guest.Starts-At, Guest.Expires-At  
`ACPPM_onbenroll` | Insight Logs | Onboard Enrollment | OnboardEnrollment.Username, OnboardEnrollment.Device-Name, OnboardEnrollment.MAC-Address, OnboardEnrollment.Device-Product, OnboardEnrollment.Device-Version, OnboardEnrollment.Added-At, OnboardEnrollment.Updated-At  
`ACPPM_onbcert` | Insight Logs | Onboard Certificate | OnboardCert.Username, OnboardCert.Mac-Address, OnboardCert.Subject, OnboardCert.Issuer, OnboardCert.Valid-From, OnboardCert.Valid-To, OnboardCert.Revoked-At  
`ACPPM_onboscp` | Insight Logs | Onboard OCSP | OnboardOCSP.Remote-Address, OnboardOCSP.Response-Status-Name, OnboardOCSP.Timestamp  
`ACPPM_cpsysevent` | Insight Logs | Clearpass System Events | CppmNode.CPPM-Node, CppmSystemEvent.Source, CppmSystemEvent.Level, CppmSystemEvent.Category, CppmSystemEvent.Action, CppmSystemEvent.Timestamp  
`ACPPM_cpconfaudit` | Insight Logs | Clearpass Configuration Audit | CppmConfigAudit.Name, CppmConfigAudit.Action, CppmConfigAudit.Category, CppmConfigAudit.Updated-By, CppmConfigAudit.Updated-At  
`ACPPM_possummary` | Insight Logs | Posture Summary | Endpoint.MAC-Address, Endpoint.IP-Address, Endpoint.Hostname, Endpoint.Usermame, Endpoint.System-Agent-Type, Endpoint.System-Agent-Version, Endpoint.System-Client-OS, Endpoint.System-Posture-Token, Endpoint.Posture-Healthy, Endpoint.Posture-Unhealthy  
`ACPPM_posfwsummary` | Insight Logs | Posture Firewall Summary | Endpoint.MAC-Address, Endpoint.IP-Address, Endpoint.Hostname, Endpoint.Usermame, Endpoint.System-Agent-Type, Endpoint.System-Agent-Version, Endpoint.System-Client-OS, Endpoint.System-Posture-Token, Endpoint.Firewall-APT, Endpoint.Firewall-Input, Endpoint.Firewall-Output  
`ACPPM_poavsummary` | Insight Logs | Posture Antivirus Summary | Endpoint.MAC-Address, Endpoint.IP-Address, Endpoint.Hostname, Endpoint.Usermame, Endpoint.System-Agent-Type, Endpoint.System-Agent-Version, Endpoint.System-Client-OS, Endpoint.System-Posture-Token, Endpoint.Antivirus-APT, Endpoint.Antivirus-Input, Endpoint.Antivirus-Output  
`ACPPM_posassummary` | Insight Logs | Posture Antispyware Summary | Endpoint.MAC-Address, Endpoint.IP-Address, Endpoint.Hostname, Endpoint.Usermame, Endpoint.System-Agent-Type, Endpoint.System-Agent-Version, Endpoint.System-Client-OS, Endpoint.System-Posture-Token, Endpoint.Antispyware-APT, Endpoint.Antispyware-Input, Endpoint.Antispyware-Output  
`ACPPM_posdskencrpsummary` | Insight Logs | Posture DiskEncryption Summary | Endpoint.MAC-Address, Endpoint.IP-Address, Endpoint.Hostname, Endpoint.Usermame, Endpoint.System-Agent-Type, Endpoint.System-Agent-Version, Endpoint.System-Client-OS, Endpoint.System-Posture-Token, Endpoint.DiskEncryption-APT, Endpoint.DiskEncryption-Input, Endpoint.DiskEncryption-Output  
`ACPPM_loggedusers` | Session Logs | Logged in Users | Common.Username, Common.Service, Common.Roles, Common.Host-MAC-Address, RADIUS.Acct-Framed-IP-Address, Common.NAS-IP-Address, Common.Request-Timestamp  
`ACPPM_failedauth` | Session Logs | Failed Authentications | Common.Username, Common.Service, Common.Roles, RADIUS.Auth-Source, RADIUS.Auth-Method, Common.System-Posture-Token, Common.Enforcement-Profiles, Common.Host-MAC-Address, Common.NAS-IP-Address, Common.Error-Code, Common.Alerts, Common.Request-Timestamp  
`ACPPM_radacctsession` | Session Logs | RADIUS Accounting | RADIUS.Acct-Username, RADIUS.Acct-NAS-IP-Address, RADIUS.Acct-NAS-Port, RADIUS.Acct-NAS-Port-Type, RADIUS.Acct-Calling-Station-Id, RADIUS.Acct-Framed-IP-Address, RADIUS.Acct-Session-Id, RADIUS.Acct-Session-Time, RADIUS.Acct-Output-Pkts, RADIUS.Acct-Input-Pkts, RADIUS.Acct-Output-Octets, RADIUS.Acct-Input.Octets, RADIUS.Acct-Service-Name, RADIUS.Acct-Timestamp  
`ACPPM_tacadmin` | Session Logs | tacacs+ Administration | Common.Username, Common.Service, tacacs.Remote-Address, tacacs.Privilege.Level, Common.Request-Timestamp  
`ACPPM_tacacct` | Session Logs | tacacs+ Accounting | Common.Username, Common.Service, tacacs.Remote-Address, tacacs.Acct-Flags, tacacs.Privilege.Level, Common.Request-Timestamp  
`ACPPM_webauthsession` | Session Logs | Web Authentication | Common.Username, Common.Host-MAC-Address, WEBAUTH.Host-IP-Address, Common.Roles, Common.System-Posture-Token, Common.Enforcement-Profiles, Common.Request-Timestamp  
`ACPPM_guestacc` | Session Logs | Guest Access | Common.Username, RADIUS.Auth-Method, Common.Host-MAC-Address, Common.Roles, Common.System-Posture-Token, Common.Enforcement-Profiles, Common.Request-Timestamp  
`ACPPM_auditrecords` | Audit Records | Not Applicable | Not Applicable  
`ACPPM_systemevents` | System Events | Not Applicable | Not Applicable  
  
## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`Action` | `security_result.action` | Value is mapped from 'Action' field if its value is 'ALLOW' or 'BLOCK'  
`Auth.Enforcement-Profiles` | `security_result.detection_fields.value` | Value is mapped from 'Auth.Enforcement-Profiles' field  
`Auth.Host-MAC-Address` | `principal.mac` | Value is mapped from 'Auth.Host-MAC-Address' field after converting it to colon-separated MAC address format  
`Auth.Login-Status` | `security_result.detection_fields.value` | Value is mapped from 'Auth.Login-Status' field  
`Auth.NAS-IP-Address` | `target.ip` | Value is mapped from 'Auth.NAS-IP-Address' field  
`Auth.Protocol` | `intermediary.application` | Value is mapped from 'Auth.Protocol' field  
`Auth.Service` | `security_result.detection_fields.value` | Value is mapped from 'Auth.Service' field  
`Auth.Source` | `principal.hostname` | Value is mapped from 'Auth.Source' field after removing any leading alphanumeric characters and spaces  
`Auth.Username` | `principal.user.user_display_name` | Value is mapped from 'Auth.Username' field  
`Category` | `metadata.event_type` | If value is 'Logged in', UDM field is set to 'USER_LOGIN'. If value is 'Logged out', UDM field is set to 'USER_LOGOUT'  
`Common.Alerts` | `security_result.description` | Value is mapped from 'Common.Alerts' field  
`Common.Enforcement-Profiles` | `security_result.detection_fields.value` | Value is mapped from 'Common.Enforcement-Profiles' field  
`Common.Login-Status` | `security_result.detection_fields.value` | Value is mapped from 'Common.Login-Status' field  
`Common.NAS-IP-Address` | `target.ip` | Value is mapped from 'Common.NAS-IP-Address' field  
`Common.Roles` | `principal.user.group_identifiers` | Value is mapped from 'Common.Roles' field  
`Common.Service` | `security_result.detection_fields.value` | Value is mapped from 'Common.Service' field  
`Common.Username` | `principal.user.userid` | Value is mapped from 'Common.Username' field  
`Component` | `intermediary.application` | Value is mapped from 'Component' field  
`Description` | `metadata.description` | Value is mapped from 'Description' field after replacing newline characters with pipe symbol. If 'Description' field contains 'User', 'Address', and 'Role', then it is parsed as key-value pairs and mapped to corresponding UDM fields. If 'Description' field contains 'Unable connection with', then the target hostname is extracted and mapped to 'target.hostname'  
`EntityName` | `principal.hostname` | Value is mapped from 'EntityName' field  
`InterIP` | `target.ip` | Value is mapped from 'InterIP' field  
`Level` | `security_result.severity` | If value is 'ERROR' or 'FATAL', UDM field is set to 'HIGH'. If value is 'WARN', UDM field is set to 'MEDIUM'. If value is 'INFO' or 'DEBUG', UDM field is set to 'LOW'  
`LogNumber` | `metadata.product_log_id` | Value is mapped from 'LogNumber' field  
`RADIUS.Acct-Framed-IP-Address` | `principal.ip` | Value is mapped from 'RADIUS.Acct-Framed-IP-Address' field  
`Timestamp` | `metadata.event_timestamp` | Value is mapped from 'Timestamp' field after converting it to UTC and parsing it as a timestamp  
`User` | `principal.user.userid` | Value is mapped from 'User' field  
`agent_ip` | `principal.ip,`, `principal.asset.ip` | Value is mapped from 'agent_ip' field  
`community` | `additional.fields.value.string_value` | Value is mapped from 'community' field  
`descr` | `metadata.description` | Value is mapped from 'descr' field  
`enterprise` | `additional.fields.value.string_value` | Value is mapped from 'enterprise' field  
`eventDescription` | `metadata.description` | Value is mapped from 'eventDescription' field after removing quotes  
`generic_num` | `additional.fields.value.string_value` | Value is mapped from 'generic_num' field  
`prin_mac` | `principal.mac` | Value is mapped from 'prin_mac' field after converting it to colon-separated MAC address format  
`prin_port` | `principal.port` | Value is mapped from 'prin_port' field and converted to integer  
`specificTrap_name` | `additional.fields.value.string_value` | Value is mapped from 'specificTrap_name' field  
`specificTrap_num` | `additional.fields.value.string_value` | Value is mapped from 'specificTrap_num' field  
`uptime` | `additional.fields.value.string_value` | Value is mapped from 'uptime' field  
`version` | `metadata.product_version` | Value is mapped from 'version' field  
| `extensions.auth.type` | Value is set to 'SSO'  
| `metadata.event_type` | Value is determined based on various log fields and parser logic. See parser code for details  
| `metadata.log_type` | Value is set to 'CLEARPASS'  
| `metadata.product_name` | Value is set to 'ClearPass'  
| `metadata.vendor_name` | Value is set to 'ArubaNetworks'  
`deviceProcessName` | `event.idm.read_only_udm.intermediary.application` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`NAD` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`nas_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`service_name` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`roles` | `event.idm.read_only_udm.principal.user.attribute.roles` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`rt` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`rt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs4` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs5` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs6` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cribl_pipe` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`organization.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`my_timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`VAR_TOPIC_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_pri` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_vendor` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_product_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_signature_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`dvc` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`syslog_host_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`cs1` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`cef_name` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`organization.name` | `event.idm.read_only_udm.principal.group.group_display_name` | Mapped from changelog  
`cat` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`kafkaTopic` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`evnt.created` | `event.idm.read_only_udm.security_result.first_discovered_time` | Mapped from changelog  
`cef_severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`dpriv` | `event.idm.read_only_udm.target.user.attribute.roles` | Mapped from changelog  
`duser` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`ts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`monitor_mode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`audit_apt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`spt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`end_host_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cpu_usage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`res_mem_usage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`virt_mem_usage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`roles` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`enf_profiles` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`auth_source` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`process_id` | `event.idm.read_only_udm.principal.process.product_specific_process_id` | Mapped from changelog  
`service_name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`LogNumber` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`nas_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`nas_port_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`seq_num` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`acct_authentic` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`acct_sessionId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`acct_status_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`called_station_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`calling_station_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`acct_delaytimestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`acct_delay_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Auth.Username` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`Auth.Host-MAC-Address` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`Auth.Roles` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`Auth.Protocol` | `event.idm.read_only_udm.intermediary.application` | Mapped from changelog  
`Auth.NAS-IP-Address` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`Auth.NAS-IP-Address` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`Auth.Service` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Auth.Login-Status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Common.Connection-Status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`source_ip1` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`identifier` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`log_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`val1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`val2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`swap_memory_avail` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`system_memory_avail` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cpu_raw_user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cpu_raw_system` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cpu_raw_idle` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cpu_raw_nice` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mgmt_inf_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data_inf_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`swap_size_used` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`slash_size_used` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ingest_timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`source_ip2` | `event.idm.read_only_udm.observer.ip` | Mapped from changelog  
`vd` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Mapped from changelog  
`ui` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`ui` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`ExporterName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Category` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`Action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`Remote_IP_Address` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`Remote_IP_Address` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`InterIP` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`InterIP` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`sdescription` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`code` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`server` | `event.idm.read_only_udm_principal.application` | Mapped from changelog  
`swVersion` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`enterpriseId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`software` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`CppmNode.CPPM-Node` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`CppmNode.CPPM-Node` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`messagedetail` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`Thread_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`servicename` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Req_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Internalserviceid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`InternalChallengeID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Entityid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`handlervalue` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`instanceid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`threadrequestinfo` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`Acct-NAS-IP-Address` | `principal.ip` | Mapped from changelog  
`Acct-Username` | `principal.user.userid` | Mapped from changelog  
`Acct-Calling-Station-Id` | `principal.user.product_object_id` | Mapped from changelog  
`descr" and "eventDescription` | `metadata.description` | Mapped from changelog  
`specificTrap_name", "uptime", "enterprise", "generic_num", "specificTrap_num", and "community` | `additional.fields` | Mapped from changelog  
`Common.Service", "Common.Enforcement-Profiles", and "Common.Login-Status` | `security_result.detection_fields` | Mapped from changelog  
`metadata.event_type` | `STATUS_UPDATE` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/clearpass-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
