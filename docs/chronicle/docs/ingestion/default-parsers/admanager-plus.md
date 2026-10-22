---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/admanager-plus/
title: Collect ManageEngine ADManager Plus logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:49.347167+00:00
---

# Collect ManageEngine ADManager Plus logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/admanager-plus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ManageEngine ADManager Plus logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ManageEngine ADManager Plus logs to Google Security Operations using the Bindplane agent.

ManageEngine ADManager Plus offers a web-based solution for simplified AD management, including user creation and modification, role-based security, and detailed reports. ADManager Plus' integration with Splunk and Syslog servers enables organizations to forward logs of all Active Directory, Microsoft 365, and Google Workspace management actions performed in ADManager Plus.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and ManageEngine ADManager Plus
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the ManageEngine ADManager Plus management console



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
         
         msiexec /i "https://github.com/observIQ/bindplane-otel-collector/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-otel-collector/releases/latest/download/install_unix.sh)" install_unix.sh
         

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

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/admanager_plus:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '<CREDS_FILE_PATH>'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: ADMANAGER_PLUS
             raw_log_field: body
             ingestion_labels:
               log_source: admanager_plus
         
         service:
           pipelines:
             logs/admanager_to_chronicle:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/admanager_plus
         

  2. Replace the following placeholders:

     * **Receiver configuration:**

       * The receiver uses `tcplog` to receive syslog data on TCP port 514.
       * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on port 514.
     * **Exporter configuration:**

       * `<CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1): 
         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\\Program Files\\observIQ OpenTelemetry Collector\\ingestion-auth.json`
       * `<CUSTOMER_ID>`: Customer ID from the previous step.
       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
       * `endpoint`: Keep set to `chronicle.googleapis.com`.
       * `log_type`: Set to `ADMANAGER_PLUS` exactly as it appears in Chronicle.
       * `ingestion_labels`: Optional labels in YAML format.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/admanager_plus:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ADMANAGER_PLUS
            raw_log_field: body
            ingestion_labels:
              log_source: admanager_plus
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

### Linux

  1. To restart the Bindplane agent in Linux, run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




### Windows

  1. To restart the Bindplane agent in Windows, choose one of the following options: 

     * Using Command Prompt or PowerShell as administrator:
           
           net stop observiq-otel-collector && net start observiq-otel-collector
           

     * Using Services console:

       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ Distro for OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure ManageEngine ADManager Plus syslog forwarding

  1. Log in to ADManager Plus.
  2. Navigate to the **Admin** tab.
  3. Under **System Settings** , click **Integrations**.
  4. Under **Log Forwarding** , click **Syslog**.

  5. Configure the following fields:

     * **Syslog Server** : Enter the syslog server name. Enter the IP address or hostname of the Bindplane agent host.
     * **Port** : Enter the port number. Enter `514`.
     * **Protocol** : Choose the appropriate protocol, TCP or UDP, for forwarding logs. Select **TCP**.
     * **Syslog Standard** : Select the desired syslog message format, RFC 3164, RFC 5424, or RawLog. Select **RFC 5424** (recommended).
     * **Data Format** : Enter the data format. Configure the data format as needed for your environment.
  6. Click **Save** to save the configuration.




After configuration, ADManager Plus will begin forwarding logs of management actions to the Bindplane agent, which will then send them to Google SecOps.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
ipPhone | event.idm.read_only_udm.additional.fields | Merged as label with key "ipPhone" and value from ipPhone if ipPhone != ""  
l | event.idm.read_only_udm.additional.fields | Merged as label with key "l" and value from l if l != ""  
lockoutTime | event.idm.read_only_udm.additional.fields | Merged as label with key "lockoutTime" and value from lockoutTime if lockoutTime != ""  
Move From | event.idm.read_only_udm.additional.fields | Merged as label with key "Move From" and value from Move_From if Move_From != ""  
Move To | event.idm.read_only_udm.additional.fields | Merged as label with key "Move To" and value from Move_To if Move_To != ""  
msg | event.idm.read_only_udm.additional.fields | Merged as label with key "member" and value from msg if msg != ""  
sn | event.idm.read_only_udm.additional.fields | Merged as label with key "sn" and value from sn if sn != ""  
st | event.idm.read_only_udm.additional.fields | Merged as label with key "st" and value from st if st != ""  
Template Name | event.idm.read_only_udm.additional.fields | Merged as label with key "Template Name" and value from Template_Name if Template_Name != ""  
Status | event.idm.read_only_udm.metadata.description | Value taken from Status if Status != ""  
time | event.idm.read_only_udm.metadata.event_timestamp | Converted from time to timestamp format if time != ""  
| event.idm.read_only_udm.metadata.event_type | Derived: if has_principal_user == "true" then "USER_UNCATEGORIZED"; else if has_principal == "true" then "STATUS_UPDATE"; else "GENERIC_EVENT"  
TechnicianName | event.idm.read_only_udm.metadata.product_event_type | Value taken from TechnicianName if TechnicianName != ""  
| event.idm.read_only_udm.metadata.product_name | Set to "ADMANAGER_PLUS"  
| event.idm.read_only_udm.metadata.vendor_name | Set to "ADMANAGER_PLUS"  
Domain Name | event.idm.read_only_udm.principal.administrative_domain | Value taken from Domain_Name if Domain_Name != ""  
hostname | event.idm.read_only_udm.principal.asset.hostname | Value taken from hostname if hostname != ""  
mail | event.idm.read_only_udm.principal.email | Value taken from mail if mail != ""  
hostname | event.idm.read_only_udm.principal.hostname | Value taken from hostname if hostname != ""  
co | event.idm.read_only_udm.principal.location.city | Value taken from co if co != ""  
Task | event.idm.read_only_udm.principal.resource.name | Value taken from Task if Task != ""  
wWWHomePage | event.idm.read_only_udm.principal.url | Value taken from wWWHomePage if wWWHomePage != ""  
Password Type | event.idm.read_only_udm.principal.user.attribute.labels | Merged as label with key "Password Type" and value from Password_Type if Password_Type != ""  
countryCode | event.idm.read_only_udm.principal.user.attribute.labels | Merged as label with key "countryCode" and value from countryCode if countryCode != ""  
password | event.idm.read_only_udm.principal.user.attribute.labels | Merged as label with key "password" and value from password if password != ""  
postalCode | event.idm.read_only_udm.principal.user.attribute.labels | Merged as label with key "postalCode" and value from postalCode if postalCode != ""  
primaryGroupID | event.idm.read_only_udm.principal.user.attribute.labels | Merged as label with key "primaryGroupID" and value from primaryGroupID if primaryGroupID != ""  
userAccountControl | event.idm.read_only_udm.principal.user.attribute.labels | Merged as label with key "userAccountControl" and value from userAccountControl if userAccountControl != ""  
userPrincipalName | event.idm.read_only_udm.principal.user.attribute.labels | Merged as label with key "userPrincipalName" and value from userPrincipalName if userPrincipalName != ""  
company | event.idm.read_only_udm.principal.user.company_name | Value taken from company if company != ""  
department | event.idm.read_only_udm.principal.user.department | Merged with department if department != ""  
givenName | event.idm.read_only_udm.principal.user.first_name | Value taken from givenName if givenName != ""  
physicalDeliveryOfficeName | event.idm.read_only_udm.principal.user.office_address.name | Value taken from physicalDeliveryOfficeName if physicalDeliveryOfficeName != ""  
streetAddress | event.idm.read_only_udm.principal.user.personal_address.name | Value taken from streetAddress if streetAddress != ""  
homePhone | event.idm.read_only_udm.principal.user.phone_numbers | Merged with homePhone if homePhone != ""  
User Name | event.idm.read_only_udm.principal.user.user_display_name | Value taken from User_Name if User_Name != ""; else from Object_Name if Object_Name != ""  
sAMAccountName | event.idm.read_only_udm.principal.user.userid | Value taken from sAMAccountName if sAMAccountName != ""  
ACTION | event.idm.read_only_udm.security_result.action_details | Value taken from ACTION if ACTION != ""  
description | event.idm.read_only_udm.security_result.description | Value taken from description if description != ""  
Container Name | event.idm.read_only_udm.security_result.detection_fields | Derived from container_Name grok: merged as label with key "Container_Name_DC_value1" and value from dc_label_1 if dc_label_1 != ""  
Container Name | event.idm.read_only_udm.security_result.detection_fields | Derived from container_Name grok: merged as label with key "Container_Name_DC_value2" and value from dc_label_2 if dc_label_2 != ""  
Container Name | event.idm.read_only_udm.security_result.detection_fields | Derived from container_Name grok: merged as label with key "Container_Name_OU_value1" and value from ou_label_1 if ou_label_1 != ""  
Container Name | event.idm.read_only_udm.security_result.detection_fields | Derived from container_Name grok: merged as label with key "Container_Name_OU_value2" and value from ou_label_2 if ou_label_2 != ""  
Container Name | event.idm.read_only_udm.security_result.detection_fields | Derived from container_Name grok: merged as label with key "Container_Name_OU_value3" and value from ou_label_3 if ou_label_3 != ""  
Primary Group | event.idm.read_only_udm.security_result.detection_fields | Derived from Primary_Group grok: merged as label with key "Primary_Group_CN_value1" and value from cn_label_1 if cn_label_1 != ""  
Primary Group | event.idm.read_only_udm.security_result.detection_fields | Derived from Primary_Group grok: merged as label with key "Primary_Group_CN_value2" and value from cn_label_2 if cn_label_2 != ""  
Primary Group | event.idm.read_only_udm.security_result.detection_fields | Derived from Primary_Group grok: merged as label with key "Primary_Group_DC_value1" and value from primary_dc_label_1 if primary_dc_label_1 != ""  
Primary Group | event.idm.read_only_udm.security_result.detection_fields | Derived from Primary_Group grok: merged as label with key "Primary_Group_DC_value2" and value from primary_dc_label_2 if primary_dc_label_2 != ""  
accountExpires | event.idm.read_only_udm.security_result.detection_fields | Merged as label with key "accountExpires" and value from accountExpires if accountExpires != ""  
manager | event.idm.read_only_udm.security_result.detection_fields | Derived from manager grok: merged as label with key "manager_cn_value1" and value from manager_cn_value1 if manager_cn_value1 != ""  
manager | event.idm.read_only_udm.security_result.detection_fields | Derived from manager grok: merged as label with key "manager_dc_value1" and value from manager_dc_value1 if manager_dc_value1 != ""  
manager | event.idm.read_only_udm.security_result.detection_fields | Derived from manager grok: merged as label with key "manager_dc_value2" and value from manager_dc_value2 if manager_dc_value2 != ""  
manager | event.idm.read_only_udm.security_result.detection_fields | Derived from manager grok: merged as label with key "manager_ou_value1" and value from manager_ou_value1 if manager_ou_value1 != ""  
manager | event.idm.read_only_udm.security_result.detection_fields | Derived from manager grok: merged as label with key "manager_ou_value2" and value from manager_ou_value2 if manager_ou_value2 != ""  
manager | event.idm.read_only_udm.security_result.detection_fields | Derived from manager grok: merged as label with key "manager_ou_value3" and value from manager_ou_value3 if manager_ou_value3 != ""  
pwdLastSet | event.idm.read_only_udm.security_result.detection_fields | Merged as label with key "pwdLastSet" and value from pwdLastSet if pwdLastSet != ""  
ModuleName | event.idm.read_only_udm.target.resource.name | Value taken from ModuleName if ModuleName != ""  
`Object_Name` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`syslog_priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`product_app_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`User_Name` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`User_Name` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`streetAddress` | `event.idm.ready_only_udm.principal.user.personal_address.name` | Mapped from changelog  
`physicalDeliveryOfficeName` | `event.idm.ready_only_udm.principal.user.office_address.name` | Mapped from changelog  
`postalCode` | `event.idm.ready_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`countryCode` | `event.idm.ready_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`company` | `event.idm.ready_only_udm.principal.user.company_name` | Mapped from changelog  
`department` | `event.idm.ready_only_udm.principal.user.department` | Mapped from changelog  
`accountExpires` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`ou_label_1` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`ou_label_2` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`ou_label_3` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`dc_label_1` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`dc_label_2` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`cn_label_1` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`cn_label_2` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`primary_dc_label_1` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`primary_dc_label_2` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`manager_cn_value1` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`,` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`and` | `event.idm.ready_only_udm.security_result.detection_fields` | Mapped from changelog  
`givenName` | `event.idm.ready_only_udm.user.first_name` | Mapped from changelog  
`sn` | `event.idm.ready_only_udm.additional.fields` | Mapped from changelog  
`st` | `event.idm.ready_only_udm.additional.fields` | Mapped from changelog  
`l` | `event.idm.ready_only_udm.additional.fields` | Mapped from changelog  
`wWWHomePage` | `event.idm.ready_only_udm.principal.url` | Mapped from changelog  
`homePhone` | `event.idm.ready_only_udm.principal.user.phone_numbers` | Mapped from changelog  
`co` | `event.idm.ready_only_udm.principal.location.city` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/admanager-plus-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
