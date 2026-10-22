---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/logonbox/
title: Collect LogonBox logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:56.018891+00:00
---

# Collect LogonBox logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/logonbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect LogonBox logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest LogonBox logs to Google Security Operations using Bindplane.

LogonBox is a self-service password management and identity verification platform. It generates audit logs for password resets, identity verification events, and admin actions. The parser maps LogonBox audit data to the Unified Data Model (UDM), capturing user identity, authentication events, resource modifications, and group management operations.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the LogonBox server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the LogonBox administration console



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
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/logonbox:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: LOGONBOX
            raw_log_field: body
        
        service:
          pipelines:
            logs/logonbox:
              receivers:
                - udplog
              exporters:
                - chronicle/logonbox
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * Adjust the `creds_file_path` to the path of your service account JSON key file (Option 1), depending on the platform: 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/logonbox:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: LOGONBOX
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
         




## Configure LogonBox syslog forwarding

  1. Sign in to the **LogonBox** administration console as an administrator.
  2. Navigate to **Reports > Audit Log**.
  3. Configure the syslog export settings: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane receiver port).
     * **Protocol** : Select **UDP** (must match the Bindplane receiver type).
  4. Select the event categories to forward (for example, password resets, identity verifications, user and group management).
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| additional.fields | Merged from attr_associatedPrincipals_label, sAMAccountName_label, attr_local_label, msDS-PrincipalName_label, attr_realmType_label, attr_selfCreated_label, attr_administrative_label based on conditions  
attr_principalDesc, desc | metadata.description | Value from attr_principalDesc if product_event_type matches changePassword|SessionService, else from attr_principalDesc if not empty, else from desc  
event_type | metadata.event_type | Value copied directly from event_type after conditional logic sets it based on product_event_type and presence flags  
product_event_type | metadata.product_event_type | Value copied directly  
| metadata.product_name | Set to "LogonBox"  
| metadata.vendor_name | Set to "LOGONBOX"  
| network.application_protocol | Set to "DNS" if product_event_type matches AnswerService and conditions met  
dns_answer | network.dns.answers | Merged from dns_answer  
dns_question | network.dns.questions | Merged from dns_question  
attr_userAgent, attr_userAgentVersion | network.http.parsed_user_agent | Concatenated from attr_userAgent and attr_userAgentVersion if both present, else from attr_userAgent, then converted to parseduseragent and renamed  
attr_userAgent, attr_userAgentVersion | network.http.user_agent | Concatenated from attr_userAgent and attr_userAgentVersion if both present, else from attr_userAgent  
hostname | principal.asset.hostname | Value copied directly  
attr_ipAddress | principal.asset.ip | Value copied directly  
hostname | principal.hostname | Value copied directly  
attr_ipAddress | principal.ip | Value copied directly  
attr_os | principal.platform | Uppercased and set if matches (?i)LINUX|MAC|WINDOWS  
attr_osVersion | principal.platform_version | Value copied directly if not matches (?i)unknown  
attr_principalRealm_label, attr_unassignedRoles_label, attr_assignedRoles_label, attr_oldResourceName_label, attr_roles_label, attr_resumedPrincipalName_label, attr_resumedPrincipalRealm_label, attr_resumedPrincipal_label, attr_module_label, reconcile_map_label, users_map_label, groups_map_label, createUser_map_label, user_map_label, mobile_map_label | principal.resource.attribute.labels | Merged from various labels created from attr_principalRealm, attr_unassignedRoles, attr_assignedRoles, attr_oldResourceName, attr_roles, attr_resumedPrincipalName, attr_resumedPrincipalRealm, attr_resumedPrincipal, attr_module, and maps from reconcile, users, groups, createUser, user, mobile based on conditions  
attr_resourceName | principal.resource.name | Value copied directly  
attr_resourceId | principal.resource.product_object_id | Value copied directly  
mail | principal.user.email_addresses | Merged if mail is valid email  
ImmutableID, attr_uuid | principal.user.product_object_id | Value from ImmutableID if product_event_type matches changePassword|userUpdated|userCreated|setPassword|answer|accountUnlockNoSuspension, else from attr_uuid  
attr_scheme | principal.user.role_name | Value copied directly  
attr_principalDesc | principal.user.user_display_name | Value copied directly if product_event_type matches changePassword|SessionService  
attr_principalName | principal.user.userid | Value copied directly  
authy_code_length_label, authy_window_length_label, authy_step_size_label, msauthenticator_code_length_label, msauthenticator_window_length_label, msauthenticator_step_size_label, googleUser_code_length_label, googleUser_window_length_label, googleUser_step_size_label | security_result.detection_fields | Merged from labels created from authy.code.length, authy.window.length, authy.step.size, msauthenticator.code.length, msauthenticator.window.length, msauthenticator.step.size, googleUser.code.length, googleUser.window.length, googleUser.step.size if present  
cn | target.resource.attribute.labels | Merged from full_name_label created from cn, and attr_disabledRealm_label from attr_disabledRealm  
attr_lastModified | target.resource.attribute.last_update_time | Date parsed from attr_lastModified using ISO8601 or d MMM yyyy HH:mm:ss  
attr_created | target.resource.attribute.creation_time | Date parsed from attr_created using ISO8601 or d MMM yyyy HH:mm:ss  
givenName | target.user.first_name | Value copied directly  
ou | target.user.group_identifiers | Merged from ou if product_event_type matches userUpdated|userCreated|changePassword|setPassword|answer|accountUnlockNoSuspension  
sn | target.user.last_name | Value copied directly  
attr_uuid, attr_disabledPrincipal | target.user.product_object_id | Value from attr_uuid if product_event_type matches userUpdated|userCreated|changePassword|setPassword|answer|accountUnlockNoSuspension or groupCreated|groupUpdated or attr_group or group, else from attr_disabledPrincipal if accountDisabled  
displayName, description | target.user.user_display_name | Value from displayName if not empty, else from description if product_event_type matches userUpdated|userCreated|changePassword|setPassword|answer|accountUnlockNoSuspension  
userPrincipalName, attr_user, attr_associatedPrincipals, attr_disabledPrincipalName | target.user.userid | Value from userPrincipalName if product_event_type matches userUpdated|userCreated|changePassword|setPassword|answer|accountUnlockNoSuspension, else attr_user if not set, else attr_associatedPrincipals if groupCreated|groupUpdated or attr_group, else attr_user if group, else attr_disabledPrincipalName if accountDisabled  
attr_group | target.group.group_display_name | Value copied directly if product_event_type matches groupCreated|groupUpdated or attr_group present  
attr_uuid | target.group.product_object_id | Value copied directly if product_event_type matches groupCreated|groupUpdated or attr_group present  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/logonbox-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
