---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lookout-mobile-endpoint-security/
title: Collect Lookout Mobile Endpoint Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:33.138953+00:00
---

# Collect Lookout Mobile Endpoint Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lookout-mobile-endpoint-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Lookout Mobile Endpoint Security logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Lookout Mobile Endpoint Security logs to Google Security Operations using Bindplane agent.

Lookout Mobile Endpoint Security (MES) is a comprehensive mobile security solution that protects iOS, Android, and ChromeOS devices from phishing, malware, network attacks, and device vulnerabilities. It leverages AI-driven threat intelligence to detect and prevent mobile threats while maintaining user privacy. Lookout MES supports forwarding security events in CEF (Common Event Format) over syslog to external SIEM systems.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Lookout MES SIEM Connector host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrator access to the Lookout MES Console
  * An Application Key generated in the Lookout MES Console for SIEM Connector authentication



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
          tcplog:
            listen_address: "0.0.0.0:6514"
        
        exporters:
          chronicle/lookout_mes:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: LOOKOUT_MOBILE_ENDPOINT_SECURITY
            raw_log_field: body
            ingestion_labels:
              log_type: LOOKOUT_MOBILE_ENDPOINT_SECURITY
        
        service:
          pipelines:
            logs/lookout_mes_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/lookout_mes
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` listens on all interfaces
      * Port `6514` is recommended for TLS-capable syslog; use `514` or `1514` if preferred
    * The `tcplog` receiver is recommended because Lookout SIEM Connector supports TCP syslog and TCP provides reliable delivery of CEF events
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Your Google SecOps customer ID
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/lookout_mes:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: LOOKOUT_MOBILE_ENDPOINT_SECURITY
            raw_log_field: body
            ingestion_labels:
              log_type: LOOKOUT_MOBILE_ENDPOINT_SECURITY
        


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
           
           ```cmd
            sc query observiq-otel-collector
            ```
           

    5. Check logs for errors:
           
           ```cmd
            type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
            ```
           




## Configure Lookout Mobile Endpoint Security syslog forwarding

Lookout MES uses the SIEM Connector App to export security events in CEF format over syslog. The SIEM Connector authenticates to the Lookout Mobile Risk API, retrieves threat events, and forwards them as CEF-formatted syslog messages to your Bindplane agent.

### Generate an Application Key for the SIEM Connector

  1. Sign in to the **Lookout MES Console** at `https://app.lookout.com`.

**Note:** If your organization uses Azure Active Directory integration, sign in at `https://aad.lookout.com`.
  2. In the left navigation bar, go to **System > Application Keys**.

**Note:** If you don't see the **Application Keys** option, contact Lookout Enterprise Support to enable this feature on your tenant.
  3. Click **Generate Key** in the upper-right corner.

  4. In the **Label** field, enter a descriptive name (for example, `Bindplane-Chronicle-CEF`).

  5. Click **Next**.

  6. Copy the generated application key by clicking **Click to Copy Application Key to Clipboard**.

**Important** : Copy and save the application key immediately. You cannot retrieve this key again after closing this dialog.

  7. Record your **Enterprise GUID** from the **System** settings. This is your unique Lookout tenant identifier.




### Install and configure the Lookout SIEM Connector

  1. Download the **Lookout SIEM Connector App** from the Lookout Help Portal or contact Lookout Enterprise Support to obtain the latest distribution package.
  2. Install the SIEM Connector on a host that has network access to both the Lookout API endpoint (`https://api.lookout.com`) and the Bindplane agent.
  3. Open the SIEM Connector configuration file.
  4. Provide the following configuration details:

     * **Application Key** : The application key you generated from the Lookout MES Console
     * **Enterprise GUID** : Your Lookout tenant identifier
     * **API Base URL** : `https://api.lookout.com`
     * **Output Format** : Select **CEF**
     * **Transport Protocol** : Select **TCP**
     * **Syslog Server Host** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`)
     * **Syslog Server Port** : Enter the port number matching your Bindplane agent receiver configuration (for example, `6514`)
  5. Save the configuration file.

  6. Start the SIEM Connector service.

**Note:** The SIEM Connector periodically polls the Lookout Mobile Risk API for new events and forwards them as CEF-formatted syslog messages. Events include threat detections, audit actions, and device state changes.



### Verify syslog delivery

  1. Check the SIEM Connector logs to confirm that events are being retrieved from the Lookout Mobile Risk API and forwarded to the Bindplane agent.
  2. On the Bindplane agent host, check the agent logs to confirm CEF events are being received:

**Linux:**
         
         sudo journalctl -u observiq-otel-collector -f
         

**Windows:**
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         

  3. In the Google SecOps console, verify that Lookout Mobile Endpoint Security events appear in the search results.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
deviceNtDomain | about.administrative_domain | Value copied directly  
deviceExternalId | about.asset.asset_id | Concatenated from device_vendor, device_product, deviceExternalId  
filePath | about.file.full_path | Value from filePath, or from fileHash if not a hash  
fileHash | about.file.full_path |   
fname | about.file.names | Value copied directly  
_hash | about.file.sha256 | Value from _hash or fileHash  
fileHash | about.file.sha256 |   
fsize | about.file.size | Converted to uinteger  
dvchost | about.hostname | Value copied directly  
dvc | about.ip | Extracted IPs from dvc after splitting and validating  
dvcmac | about.mac | Value copied directly  
deviceTranslatedAddress | about.nat_ip | Value copied directly  
deviceProcessName | about.process.command_line | Value from deviceProcessName, or Subject, or Emne, or Path  
Subject | about.process.command_line |   
Emne | about.process.command_line |   
Path | about.process.command_line |   
dvcpid | about.process.pid | Value copied directly  
filePermission | about.resource.attribute.permissions | Value copied directly  
device_security_result | about.security_result | Value copied directly  
Received | metadata.collected_timestamp | Parsed from Received using date format yyyy-MM-ddTHH:mm:ss  
msg | metadata.description | Value copied directly  
file_full_path | metadata.event_type | Set to SCAN_UNCATEGORIZED if file_full_path set, STATUS_UPDATE if principal_hostname, principal_ip, principal_mac present, GENERIC_EVENT otherwise, USER_UNCATEGORIZED if has_principal_user, STATUS_UPDATE if has_principal_host  
principal_hostname | metadata.event_type |   
has_principal_user | metadata.event_type |   
principal_ip | metadata.event_type |   
principal_mac | metadata.event_type |   
device_event_class_id | metadata.product_event_type | Concatenated from device_event_class_id - event_name, or from type  
event_name | metadata.product_event_type |   
type | metadata.product_event_type |   
externalId | metadata.product_log_id | Value from externalId or target.id  
target.id | metadata.product_log_id |   
device_product | metadata.product_name | Value copied directly  
device_version | metadata.product_version | Value copied directly  
device_vendor | metadata.vendor_name | Value copied directly  
app_protocol_src | network.application_protocol | Mapped from app_protocol_src using predefined protocol rules  
deviceDirection | network.direction | Set to INBOUND if 0, OUTBOUND if 1  
requestMethod | network.http.method | Value copied directly  
requestClientApplication | network.http.user_agent | Value copied directly  
proto | network.ip_protocol | Mapped from protocol_number_src using IANA protocol numbers  
in | network.received_bytes | Converted to uinteger  
out | network.sent_bytes | Converted to uinteger  
sntdom | principal.administrative_domain | Value from sntdom, or Domain, or Domene  
Domain | principal.administrative_domain |   
Domene | principal.administrative_domain |   
sourceServiceName | principal.application | Value from sourceServiceName or details.applicationName  
details.applicationName | principal.application |   
aid | principal.asset.asset_id | Concatenated from metadata.vendor_name, metadata.product_name, aid  
_hardware | principal.asset.hardware | Value copied directly  
principal_hostname | principal.asset.hostname | Value from principal_hostname (from Device_name, Enhetsnavn, shost if not IP, entName)  
av | principal.asset.platform_software.platform_version | Value copied directly  
agentZoneURI_label | principal.asset.attribute.labels | Merged from various labels  
agentTimeZone_label | principal.asset.attribute.labels |   
agentType_label | principal.asset.attribute.labels |   
agentReceiptTime_label | principal.asset.attribute.labels |   
token_new | principal.asset.attribute.labels |   
details.path | principal.file.full_path | Value copied directly  
Group_name | principal.group.group_display_name | Value from Group_name or Gruppenavn  
Gruppenavn | principal.group.group_display_name |   
Device_name | principal.hostname | Value from Device_name, or Enhetsnavn, or shost if not IP, or entName  
Enhetsnavn | principal.hostname |   
shost | principal.hostname |   
entName | principal.hostname |   
src | principal.ip | Value from src if valid IP, or shost if IP, or agt  
shost | principal.ip |   
agt | principal.ip |   
smac | principal.mac | Value copied directly  
sourceTranslatedAddress | principal.nat_ip | Value copied directly  
sourceTranslatedPort | principal.nat_port | Converted to integer  
target.platform | principal.platform | Set to MAC if IOS, ANDROID if ANDROID  
target.osVersion | principal.platform_version | Value copied directly  
spt | principal.port | Converted to integer  
sproc | principal.process.command_line | Value from sproc or about.process.command_line  
about.process.command_line | principal.process.command_line |   
details.fileName | principal.process.file.full_path | Value copied directly  
spid | principal.process.pid | Value copied directly  
old_permissions | principal.resource.attribute.permissions | Value copied directly  
target.type | principal.resource.name | Value copied directly  
principal_role | principal.user.attribute.roles | Value copied directly  
suser | principal.user.user_display_name | Value from suser if not empty, or CustomerName  
CustomerName | principal.user.user_display_name |   
suid | principal.user.userid | Value from suid or target.emailAddress  
target.emailAddress | principal.user.userid |   
oldFilePath | src.file.full_path | Value copied directly  
oldFileSize | src.file.size | Converted to uinteger  
old_permissions | src.resource.attribute.permissions | Value copied directly  
dntdom | target.administrative_domain | Value copied directly  
destinationServiceName | target.application | Value copied directly  
target_hostname | target.asset.hostname | Value from target_hostname (from temp_dhost)  
token_new | target.asset.attribute.labels | Merged from token_new  
temp_dhost | target.hostname | Value copied directly  
dst_ip | target.ip | Value copied directly  
mac_address | target.mac | Value copied directly  
destination_translated_address | target.nat_ip | Value copied directly  
destinationTranslatedPort | target.nat_port | Converted to integer  
dpt | target.port | Converted to integer  
dproc | target.process.command_line | Value copied directly  
file_full_path | target.process.file.full_path | Value from file_full_path (from File_name, Object, Objekt, Infected_Resource)  
dpid | target.process.pid | Value copied directly  
request | target.url | Value from request or details.url  
details.url | target.url |   
target_role | target.user.attribute.roles | Value copied directly  
temp_duser | target.user.user_display_name | Value from temp_duser or CustomerName  
CustomerName | target.user.user_display_name |   
temp_duid | target.user.userid | Value from temp_duid, or User, or Bruker  
User | target.user.userid |   
Bruker | target.user.userid |   
_action | security_result.action | Set to ALLOW if act matches accept/notified/REDIRECTED_USER_MAY_PROCEED/Success, BLOCK if deny/blocked/BLOCKED/Failure/Failed, FAIL if Failure  
act | security_result.action_details | Value from act, or details.action, or Action_Taken  
details.action | security_result.action_details |   
Action_Taken | security_result.action_details |   
cat | security_result.category_details | Value from cat or sec_result_category_details  
sec_result_category_details | security_result.category_details |   
catdt_field | security_result.detection_fields | Merged from various labels  
categorySignificance_label | security_result.detection_fields |   
categoryBehavior_label | security_result.detection_fields |   
categoryDeviceGroup_label | security_result.detection_fields |   
categoryOutcome_label | security_result.detection_fields |   
categoryObject_label | security_result.detection_fields |   
operation_label | security_result.detection_fields |   
operasjon_label | security_result.detection_fields |   
permission_label | security_result.detection_fields |   
tillatelse_label | security_result.detection_fields |   
infection_channel_label | security_result.detection_fields |   
spyware_Grayware_Type_label | security_result.detection_fields |   
threat_probability_label | security_result.detection_fields |   
categoryOutcome_label | security_result.outcomes | Value copied directly  
mwProfile | security_result.rule_name | Value copied directly  
severity | security_result.severity | Mapped to LOW if 0-3/LOW, MEDIUM if 4-6/MEDIUM/INFO/SUBSTANTIAL, HIGH if 7-8/HIGH/SEVERE, CRITICAL if 9-10/CRITICAL/VERY-HIGH  
details.severity | security_result.severity |   
reason | security_result.summary | Value from reason, or appcategory, or Result  
appcategory | security_result.summary |   
Result | security_result.summary |   
Spyware | security_result.threat_name | Value from Spyware, or Virus_Malware_Name, or Unknown_Threat  
Virus_Malware_Name | security_result.threat_name |   
Unknown_Threat | security_result.threat_name |   
`actor.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actor_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`changeType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`id` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`CustomerName` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`details.type", "details.packageSha", "details.packageName", "details.assessments", "details.activationStatus", "details.securityStatus", and "details.protectionStatus` | `additional.fields` | Mapped from changelog  
`target.manufacturer` | `principal.asset.hardware.manufacturer` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lookout-mobile-endpoint-security-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
