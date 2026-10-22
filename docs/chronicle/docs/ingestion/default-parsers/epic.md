---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/epic/
title: Collect Epic Systems logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:17.369146+00:00
---

# Collect Epic Systems logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/epic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Epic Systems logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Epic Systems logs to Google Security Operations using the Bindplane agent.

Epic Systems is an Electronic Health Record (EHR) platform that generates CEF syslog messages for audit events, user login/logout, patient access, and file operations. The parser extracts key-value pairs and maps them to the Unified Data Model (UDM).

## Before you begin

  * Make sure you have the following prerequisites:

  * A Google SecOps instance

  * Windows Server 2016 or later, or Linux host with `systemd`

  * Network connectivity between the Bindplane agent and the Epic Systems server

  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements

  * Privileged access to Epic Systems




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
          chronicle/epic:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: EPIC
            raw_log_field: body
        
        service:
          pipelines:
            logs/epic_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/epic
        




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
          chronicle/epic:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: EPIC
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
             




## Configure the SendSIEMSyslogAudit service

  1. Sign in to the **Epic Systems** console.
  2. Go to **Start > Epic > Interconnect > `<your instance>` > Configuration editor**.
  3. Select the **Business services** form.
  4. On the **Service category** tab, select **SendSIEMSyslogAudit**.
  5. Click **Save**.



## Configure Epic Systems to export syslog

  1. Go to **Epic system definitions > Security > Auditing options > SIEM syslog settings**.
  2. Provide the following configuration details: 
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number.
     * **SIEM format** : Select **CEF (Common Event Format)**.
     * **Syslog ending character** : Select **New Line "\n"**.
  3. From the **SIEM syslog settings** menu, select **SIEM syslog**.
  4. Click **Enabled**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
APIID | read_only_udm.additional.fields.api.value.string_value | Value is taken from APIID field in the raw log  
APPLICATIONID | read_only_udm.additional.fields.application_id.value.string_value | Value is taken from APPLICATIONID field in the raw log  
APP | read_only_udm.target.application | Value is taken from APP field in the raw log  
AUDIT SESSION | read_only_udm.network.session_id | Value is taken from AUDIT SESSION field in the raw log  
AUTH_SOURCE |  | This field is not mapped to the UDM  
BCAPCS | read_only_udm.target.application | Value is taken from BCAPCS field in the raw log  
BTGEXPLANATION | read_only_udm.security_result.description | Value is taken from BTGEXPLANATION field in the raw log  
BTGNOACCESSREAS | read_only_udm.security_result.summary | Value is taken from BTGNOACCESSREAS field in the raw log  
BTGREASON | read_only_udm.security_result.summary | Value is taken from BTGREASON field in the raw log  
CLIENTNAME | read_only_udm.principal.hostname | Value is taken from CLIENTNAME field in the raw log  
CSISESS_TOKEN | read_only_udm.network.session_id | Value is taken from CSISESS_TOKEN field in the raw log  
CTXT | read_only_udm.metadata.description | Value is taken from CTXT field in the raw log  
CVG | read_only_udm.additional.fields.cvg.value.string_value | Value is taken from CVG field in the raw log  
DAT |  | This field is not mapped to the UDM  
DEP | read_only_udm.principal.user.department | Value is taken from DEP field in the raw log. If both NEWDEPARTMENT and PREVDEPARTMENT fields exist in the raw log, the value will be `PREVDEPARTMENT:-{PREVDEPARTMENT}, NEWDEPARTMENT:-{NEWDEPARTMENT}`. If only NEWDEPARTMENT exists, the value will be `PREVDEPARTMENT:-NONE, NEWDEPARTMENT:{NEWDEPARTMENT}`. If only PREVDEPARTMENT exists, the value will be `PREVDEPARTMENT:{PREVDEPARTMENT}, NEWDEPARTMENT:-NONE`  
devTime | read_only_udm.metadata.event_timestamp | Value is taken from devTime field in the raw log and converted to seconds since epoch  
devTimeFormat |  | This field is not mapped to the UDM  
E3MID | read_only_udm.network.session_id | Value is taken from E3MID field in the raw log  
ENCRYPTED | read_only_udm.additional.fields.encrypt.value.string_value | Value is taken from ENCRYPTED field in the raw log  
ERRMSG | read_only_udm.security_result.summary | Value is taken from ERRMSG field in the raw log  
eventCnt |  | This field is not mapped to the UDM  
FILENAME | read_only_udm.target.file.full_path | Value is taken from FILENAME field in the raw log and all occurrences of `\\\\` are replaced with `\`  
flag | read_only_udm.security_result.description | Value is taken from flag field in the raw log and all leading and trailing `-` are removed  
HKUAPVER | read_only_udm.metadata.product_version | Value is taken from HKUAPVER field in the raw log  
HKUDVCID | read_only_udm.principal.asset_id | Value is taken from HKUDVCID field in the raw log and formatted as `Device ID:{HKUDVCID}`  
HKUOSNAM | read_only_udm.principal.platform | Value is taken from HKUOSNAM field in the raw log and mapped to `WINDOWS`, `MAC`, `LINUX`, or `UNKNOWN_PLATFORM` based on the value  
HKUOSVER | read_only_udm.principal.platform_version | Value is taken from HKUOSVER field in the raw log  
INSTANCEURN | read_only_udm.intermediary.hostname | Value is taken from INSTANCEURN field in the raw log  
IP | read_only_udm.target.ip | Value is taken from IP field in the raw log. If the value contains `/`, it is split into two IP addresses. If the value contains `,`, it is split into multiple IP addresses.  
LOGINERROR | read_only_udm.security_result.summary | Value is taken from LOGINERROR field in the raw log  
LOGIN_CONTEXT | read_only_udm.metadata.description | Value is taken from LOGIN_CONTEXT field in the raw log  
LOGIN_DEVICE | read_only_udm.additional.fields.login_device.value.string_value | Value is taken from LOGIN_DEVICE field in the raw log  
LOGIN_LDAP_ID | read_only_udm.principal.user.userid | Value is taken from LOGIN_LDAP_ID field in the raw log  
LOGIN_REASON | read_only_udm.security_result.summary | Value is taken from LOGIN_REASON field in the raw log  
LOGIN_REVAL | read_only_udm.additional.fields.login_reval.value.string_value | Value is taken from LOGIN_REVAL field in the raw log  
MASKMODE | read_only_udm.additional.fields.masked_mode.value.string_value | Value is taken from MASKMODE field in the raw log  
MYCACCT | read_only_udm.principal.user.userid | Value is taken from MYCACCT field in the raw log  
NEWDEPARTMENT | read_only_udm.principal.user.department | See logic for DEP field  
NEWUSER |  | This field is not mapped to the UDM  
NSC | read_only_udm.additional.fields.nsc.value.string_value | Value is taken from NSC field in the raw log  
OSUSR | read_only_udm.target.user.userid | Value is taken from OSUSR field in the raw log  
PATIENT | read_only_udm.target.user.userid | Value is taken from PATIENT field in the raw log  
PREVDEPARTMENT | read_only_udm.principal.user.department | See logic for DEP field  
PREVPROVIDER |  | This field is not mapped to the UDM  
PREVUSER | read_only_udm.principal.resource.attribute.labels.prev_user.value | Value is taken from PREVUSER field in the raw log  
PWREASON | read_only_udm.metadata.description | Value is taken from PWREASON field in the raw log  
ROLE | read_only_udm.principal.user.attribute.roles.name | Value is taken from ROLE field in the raw log  
resource | read_only_udm.target.hostname | Value is taken from resource field in the raw log  
SERVICEID | read_only_udm.additional.fields.service_id.value.string_value | Value is taken from SERVICEID field in the raw log  
SERVICECATEGORY | read_only_udm.additional.fields.service_category.value.string_value | Value is taken from SERVICECATEGORY field in the raw log  
SERVICEMSGID |  | This field is not mapped to the UDM  
SERVICENAME | read_only_udm.target.resource.name | Value is taken from SERVICENAME field in the raw log  
SERVICETYPE | read_only_udm.target.resource.type | Value is taken from SERVICETYPE field in the raw log. If event_id is `PHI_CLIENT_FILE`, the value is set to `FILE`  
SERVICE_USER | read_only_udm.target.user.userid | Value is taken from SERVICE_USER field in the raw log  
SERVICE_USERTYP | read_only_udm.additional.fields.service_user_type.value.string_value | Value is taken from SERVICE_USERTYP field in the raw log  
sev | read_only_udm.security_result.severity | Value is taken from sev field in the raw log and mapped to `LOW`, `HIGH`, or `CRITICAL` based on the value  
shost | read_only_udm.target.resource.attribute.labels.workstation_type.value | Value is taken from shost field in the raw log  
SOURCE | read_only_udm.additional.fields.login_source.value.string_value | Value is taken from SOURCE field in the raw log  
SUCCESS | read_only_udm.additional.fields.success_yes_no.value.string_value | Value is taken from SUCCESS field in the raw log  
TIMEOUT | read_only_udm.additional.fields.time_out.value.string_value | Value is taken from TIMEOUT field in the raw log  
UID | read_only_udm.principal.user.userid | Value is taken from UID field in the raw log  
USERJOB |  | This field is not mapped to the UDM  
usrName | read_only_udm.principal.user.userid, read_only_udm.principal.user.user_display_name | If UID or LOGIN_LDAP_ID fields exist in the raw log, usrName is used for read_only_udm.principal.user.user_display_name and the other field is used for read_only_udm.principal.user.userid. Otherwise, usrName is used for read_only_udm.principal.user.userid  
WEBLGAPP | read_only_udm.target.application | Value is taken from WEBLGAPP field in the raw log  
| read_only_udm.extensions.auth.type | Value is set to `SSO` if LOGIN_LDAP_ID is not empty. Otherwise, the value is set to `AUTHTYPE_UNSPECIFIED`.  
| read_only_udm.intermediary.ip | Value is set to the IP address of the log source.  
| read_only_udm.metadata.event_type | Value is set to `RESOURCE_READ` if event_id is one of `IC_SERVICE_AUDIT`, `AC_BREAK_THE_GLASS_FAILED_ACCESS`, `AC_BREAK_THE_GLASS_INAPPROPRIATE_ATTEMPT`, `AC_BREAK_THE_GLASS_ACCESS`, or `MCMEMEDISA` and either target_ip_set is `true` or resource is not empty. Value is set to `USER_LOGIN` if event_id is one of `FAILEDLOGIN`, `LOGIN`, `ROVER_FAILED_LOGIN`, `SWITCHUSER`, `AUTHENTICATION`, `EW_LOGIN`, `ROVER_LOGIN`, `CTO_FAILED_LOGIN`, `CTO_LOGIN`, `HKU_FAILED_LOGIN`, `HKU_LOGIN`, `WPSEC_SEC_AUTH_OPT_OUT`, `WPSEC_SEC_AUTH_OPT_IN`, `BCA_LOGIN_FAILURE`, `BCA_LOGIN_SUCCESS`, `BCA_USER_LOCKED`, `WPSEC_LOGIN_FAIL`, or `WPSEC_LOGIN_SUCCESS` and at least one of target_ip_set, resource, SERVICENAME, SERVICETYPE, or shost is not empty. Value is set to `USER_CHANGE_PASSWORD` if event_id is one of `E_ADMINPASSWORDCHANGE`, `E_FAILEDPASSWORDCHANGE`, `E_SELFPASSWORDCHANGE`, `WPSEC_USER_PASSWORD_CHANGE_FAIL`, or `WPSEC_USER_PASSWORD_CHANGE`. Value is set to `USER_UNCATEGORIZED` if event_id is `CONTEXTCHANGE`. Value is set to `USER_RESOURCE_ACCESS` if event_id is one of `SECURE`, `UNSECURE`, `MASKED_DATA_DISPLAY`, or `MASKED_DATA_PRINTING`. Value is set to `USER_RESOURCE_UPDATE_CONTENT` if event_id is `PHI_CLIENT_FILE`. Value is set to `STATUS_UPDATE` if CLIENTNAME is not empty. Value is set to `USER_UNCATEGORIZED` if prin_usr_id is not empty. Otherwise, the value is set to `GENERIC_EVENT`.  
| read_only_udm.metadata.log_type | Value is set to `EPIC`.  
| read_only_udm.metadata.product_name | Value is set to `Epic Systems`.  
| read_only_udm.metadata.vendor_name | Value is set to `EPIC`.  
| read_only_udm.network.ip_protocol | Value is derived from the proto field in the raw log and mapped to the corresponding IP protocol name.  
| read_only_udm.principal.resource.attribute.labels.workstation_type.key | Value is set to `Workstation ID/Type`.  
| read_only_udm.principal.resource.attribute.labels.prev_user.key | Value is set to `Prev User`.  
| read_only_udm.security_result.action | Value is set to `BLOCK` if either ERRMSG or LOGINERROR fields exist in the raw log.  
`REMOTEIP` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CLIENTTYPE` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`INTERNETAREA` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LOGINCLIENTID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LOGINCONTEXT` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PERIMAUTHST` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HYPACCESSID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UNRECDEVICE` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/epic-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
