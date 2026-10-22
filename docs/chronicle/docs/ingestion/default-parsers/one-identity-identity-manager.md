---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/one-identity-identity-manager/
title: Collect One Identity Identity Manager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:55.470052+00:00
---

# Collect One Identity Identity Manager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/one-identity-identity-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect One Identity Identity Manager logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest One Identity Identity Manager logs to Google Security Operations using Bindplane.

One Identity Identity Manager is an identity governance and administration (IGA) platform for managing user identities, access rights, and compliance across hybrid environments. It provides automated provisioning, access requests, attestation, and policy enforcement with a built-in Universal SIEM Forwarder for event export.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the One Identity Identity Manager server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the One Identity Identity Manager administration console with administrator permissions
  * One Identity Identity Manager version 8.x or later with the Universal SIEM Forwarder module installed



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/one_identity_idm:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: ONE_IDENTITY_IDENTITY_MANAGER
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/one_identity_idm_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/one_identity_idm
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: Receives syslog over TCP. The Universal SIEM Forwarder supports TCP for reliable delivery.
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
          chronicle/one_identity_idm:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ONE_IDENTITY_IDENTITY_MANAGER
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
         




## Configure One Identity Identity Manager syslog forwarding

One Identity Identity Manager includes a **Universal SIEM Forwarder** that exports audit and identity lifecycle events via syslog in JSON, CEF, or JSON-CIM formats.

  1. Sign in to the **One Identity Manager Administration Console** (Manager or Designer tool).
  2. Navigate to **Base Data > General > Configuration Parameters**.
  3. Locate the **QER\Person\Siem** configuration section.
  4. Enable the Universal SIEM Forwarder by setting the **Enabled** parameter to `True`.
  5. Configure the syslog destination: 
     * **SyslogHost** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **SyslogPort** : Enter `514` (must match the Bindplane agent receiver port).
     * **SyslogProtocol** : Select **TCP**.
     * **SyslogFormat** : Select **JSON** (recommended for maximum parsing fidelity).
  6. Configure the event types to forward: 
     * **PersonEvents** : Set to `True` to forward identity lifecycle events (create, modify, delete).
     * **EntitlementEvents** : Set to `True` to forward access assignment and removal events.
     * **PolicyEvents** : Set to `True` to forward policy violation and attestation events.
     * **SystemEvents** : Set to `True` to forward provisioning and synchronization events.
  7. Click **Save** to save the configuration.
  8. Restart the **One Identity Manager Service** for changes to take effect.
  9. Verify that logs are being sent by checking the Bindplane agent logs.

**Note:** For detailed configuration of the Universal SIEM Forwarder, see the One Identity Identity Manager Administration Guide for your version.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
ImportCompleted, MembersCount, SchedulerTriggerId, JobThreadCount, JobMessage, JobExitCode, TriggerVetoed, TriggerMisfired, JobException, ErrorCount, IdentityProviderName, AuditLogUri, ApplianceId, AssetName, AssetPartitionName, TaskId, SystemId, SystemName, AssetPartitionId, DurationInMinutes, OfflineWorkflowMode, RequiredDate, WasCheckedOut, ApproverAccessRequestUri, ReviewerAccessRequestUri, _DB_HOST, Enabled, UID_ConfigParm, XOrigin, Ident_AERole, UID_Person | additional.fields | Merged as key-value pairs from various fields  
RequesterAccessRequestUri | extensions.auth.auth_details | Value copied directly  
user_login, user_logout | extensions.auth.type | Set to AUTHTYPE_UNSPECIFIED if user_login or user_logout true  
hostname | intermediary.hostname | Set if hostname is not IP  
hostname | intermediary.ip | Set if hostname is IP  
time | metadata.collected_timestamp | Converted from ISO8601 timestamp  
EventDescription | metadata.description | Value copied directly  
EventTimestamp, MessageDate, XDateUpdated, XDateInserted | metadata.event_timestamp | Converted from UNIX_MS, priority XDateInserted > XDateUpdated > MessageDate > EventTimestamp  
has_principal, has_target_resource, has_user, user_login, user_logout, has_target_user | metadata.event_type | Set to USER_LOGIN if has_principal and has_target_resource and has_user and user_login; else USER_LOGOUT if has_principal and has_target_resource and has_user and user_logout; else USER_UNCATEGORIZED if has_target_user or has_user; else STATUS_UPDATE if has_principal; else GENERIC_EVENT  
EventDisplayName, XUserInserted, UID_ConfigParm, XDateInserted, XOrigin | metadata.product_event_type | Value from EventDisplayName, overridden by "Configuration Changed" if XUserInserted and UID_ConfigParm not empty, overridden by "User added to group" if XDateInserted and XOrigin not empty  
IdentityProviderId | metadata.product_log_id | Value copied directly  
version | metadata.product_version | Value copied directly  
EventUserDomainName | principal.administrative_domain | Value copied directly  
app_name, ApplicationName | principal.application | Value from ApplicationName if not empty, else app_name  
HostName | principal.asset.hostname | Value copied directly  
AuthClientMachine | principal.asset.ip | Extracted IP from AuthClientMachine  
AssetId | principal.asset_id | Concatenated as "AssetId:%{AssetId}"  
HostName | principal.hostname | Value copied directly  
AuthClientMachine | principal.ip | Extracted IP from AuthClientMachine  
process_id | principal.process.pid | Value copied directly  
AccountDistinguishedName | principal.user.attribute.roles | Set to object with name = AccountDistinguishedName  
email | principal.user.email_addresses | Merged if matches ^.+@.+$  
RequestId, UserGroupName | principal.user.product_object_id | Value from UserGroupName if not empty, else RequestId  
EventUserDisplayName | principal.user.user_display_name | Value copied directly  
EventUserName, UserGroupId, User, XUserInserted, Assignor | principal.user.userid | Value from Assignor if not empty, else XUserInserted if not empty, else User if not empty, else UserGroupId if not empty, else EventUserName  
SuccessInfo | security_result.category_details | Value copied directly  
MessageString | security_result.description | Value copied directly  
UID_DialogJournal, ApplicationIntent, IsLogOff, AuthIdentity, AuthModule | security_result.detection_fields | Merged with labels from various fields  
AccountDomainName | target.administrative_domain | Value copied directly  
AccessRequestType | target.application | Value copied directly  
AssetNetworkAddress | target.asset.hostname | Value copied directly  
AssetPlatformType | target.asset.platform_software.platform | Set to WINDOWS if matches (?i)Windows  
AssetNetworkAddress, AssetId | target.asset_id | Concatenated as "AssetNetworkAddress:%{AssetId}"  
Fullpath | target.file.full_path | Value copied directly  
AssetNetworkAddress | target.hostname | Value copied directly  
_DB_NAME, databasename, _DB_DRIVER, _DB_PORT | target.resource.attribute.labels | Merged with db_name from _DB_NAME or databasename, db_driver from _DB_DRIVER, db_port from _DB_PORT  
EventUserId | target.user.product_object_id | Value copied directly  
AccountName, Receiver | target.user.user_display_name | Value from Receiver if not empty, else AccountName  
AccountId, XUserUpdated, CentralAccount | target.user.userid | Value from CentralAccount if not empty, else XUserUpdated if not empty, else AccountId  
| metadata.product_name | Set to "ONE_IDENTITY_IDENTITY_MANAGER"  
| metadata.vendor_name | Set to "ONE_IDENTITY"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/one-identity-identity-manager-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
