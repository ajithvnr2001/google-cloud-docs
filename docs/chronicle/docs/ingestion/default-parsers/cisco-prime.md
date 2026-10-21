---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-prime/
title: Collect Cisco Prime logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:32:24.752581+00:00
---

# Collect Cisco Prime logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-prime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Prime logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Prime logs to Google Security Operations using Bindplane. The parser utilizes Grok patterns to extract fields from various syslog message formats, mapping them to a Unified Data Model (UDM). It handles different log structures, including key-value pairs, and enriches the data with user, principal, target, and security information based on specific keywords and patterns found within the log messages.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Windows 2016 or later, or a Linux host with `systemd`
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to Cisco Prime



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             udplog:
                 # Replace the port and IP address as required
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/chronicle_w_labels:
                 compression: gzip
                 # Adjust the path to the credentials file you downloaded in Step 1
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 # Replace with your actual customer ID from Step 2
                 customer_id: <customer_id>
                 endpoint: malachiteingestion-pa.googleapis.com
                 # Add optional ingestion labels for better organization
                 log_type: 'CISCO_PRIME'
                 raw_log_field: body
                 ingestion_labels:
         
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<customer_id>` with the actual customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the path where the authentication file was saved in the [Get Google SecOps ingestion authentication file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-prime#get-auth-file) section.



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure change audit notifications and configure syslog receivers

  1. You can configure the system to send syslog notifications for change audits related to the following events:

     * Device inventory updates
     * Configuration modifications
     * Changes to configuration templates
     * Template-related operations
     * User activities such as logins, logouts, and account modifications
  2. Sign in to the Cisco Prime web UI.

  3. Go to **Administration > Settings > System Settings**.

  4. Select **Mail and Notification > Change Audit Notification**.

  5. Click **Enable Change Audit Notification** checkbox.

  6. Click the **+** button to specify a syslog server.

  7. Provide the following configuration details:

     * Enter the Bindplane agent IP address.
     * Select the **UDP** protocol.
     * Enter the Bindplane agent port number.
  8. Click **Save**.




## Configure forwarding system audit logs As syslog

  1. Sign in to the Cisco Prime web UI.
  2. Go to **Administration > Settings > Logging > Syslog Logging Options**.
  3. Click the **Enable Syslog** checkbox.
  4. Provide the following configuration details: 
     * Enter the Bindplane agent IP address.
     * Select the **UDP** protocol.
     * Enter the Bindplane agent port number.
     * Select one of the eight **Facilities** or `local0`.
  5. Click **Save**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
client_ip_address | principal.ip, principal.asset.ip | The value is taken from the `client_ip_address` field, which is extracted from the raw log using kv filter.  
date | metadata.event_timestamp | The value is taken from the `date` field, which is extracted from the raw log using grok patterns and then converted to a timestamp using the date filter.  
description | security_result.description | The value is taken from the `description` field, which is extracted from the raw log using grok patterns.  
dest_mac | target.mac | The value is taken from the `dest_mac` field, which is extracted from the raw log using grok patterns and converted to lowercase.  
device_id | principal.asset_id | The value is taken from the `device_id` field, which is extracted from the raw log using grok patterns. The final value is formatted as "Device ID:".  
device_ip | principal.ip, principal.asset.ip | The value is taken from the `device_ip` field, which is extracted from the raw log using kv filter. The value is then parsed as a JSON array and each IP address in the array is added to the UDM fields.  
device_type | target.resource.attribute.labels.value | The value is taken from the `device_type` field, which is extracted from the raw log using grok patterns.  
dst_user | target.user.userid | The value is taken from the `dst_user` field, which is extracted from the raw log using grok patterns.  
email | src.hostname | The value is taken from the `email` field, which is extracted from the raw log using grok patterns.  
file_path | principal.process.file.full_path | The value is taken from the `file_path` field, which is extracted from the raw log using grok patterns.  
hostname | target.resource.attribute.labels.value | The value is taken from the `hostname` field, which is extracted from the raw log using grok patterns.  
id | principal.asset_id | The value is taken from the `id` field, which is extracted from the raw log using grok patterns. The final value is formatted as "Entity ID:".  
ip_address | principal.ip, principal.asset.ip | The value is taken from the `ip_address` field, which is extracted from the raw log using grok patterns.  
log_level | security_result.severity | The value is taken from the `log_level` field, which is extracted from the raw log using grok patterns. It is used to determine the severity level if `severity` is not present.  
mac_address | principal.mac, source_mac | The value is taken from the `mac_address` field, which is extracted from the raw log using grok patterns and converted to lowercase. It is also used as the value for `source_mac` if `source_mac` is empty.  
oid | principal.asset.product_object_id | The value is taken from the `oid` field, which is extracted from the raw log using grok patterns.  
principal_ip | principal.ip, principal.asset.ip | The value is taken from the `principal_ip` field, which is extracted from the raw log using grok patterns.  
principal_port | principal.port | The value is taken from the `principal_port` field, which is extracted from the raw log using grok patterns and converted to an integer.  
process_name | principal.resource.name | The value is taken from the `process_name` field, which is extracted from the raw log using grok patterns.  
sec_description | security_result.description | The value is taken from the `sec_description` field, which is extracted from the raw log using grok patterns.  
session_id | network.session_id | The value is taken from the `session_id` field, which is extracted from the raw log using grok patterns.  
severity | security_result.severity | The value is taken from the `severity` field, which is extracted from the raw log using grok patterns. It is used to determine the severity level if present.  
source_mac | principal.mac | The value is taken from the `source_mac` field, which is extracted from the raw log using grok patterns and converted to lowercase. If empty, it takes the value of `mac_address`.  
summary | security_result.summary | The value is taken from the `summary` field, which is extracted from the raw log using grok patterns.  
target_ip | target.ip, target.asset.ip | The value is taken from the `target_ip` field, which is extracted from the raw log using grok patterns.  
thread_pool | metadata.product_event_type | The value is taken from the `thread_pool` field, which is extracted from the raw log using grok patterns.  
timestamp | metadata.event_timestamp | The value is taken from the `timestamp` field, which is extracted from the raw log using grok patterns and then converted to a timestamp using the date filter.  
Type | metadata.product_event_type | The value is taken from the `Type` field, which is extracted from the raw log using kv filter.  
user_name | principal.user.userid | The value is taken from the `user_name` field, which is extracted from the raw log using grok patterns or kv filter.  
metadata.event_type | metadata.event_type | The value is determined based on the presence of specific fields and patterns in the raw log. The logic includes:   
\- Default value: `GENERIC_EVENT`   
\- If `thread_pool` is 'EmailAlertHelper': `EMAIL_TRANSACTION`   
\- If `application_name` is 'aesSystem' and `desc` contains 'HealthMonitorHelper': `STATUS_HEARTBEAT`   
\- If `user_present` and `target_resource_present` are both true: `USER_RESOURCE_ACCESS`   
\- If `user_present` is true: `USER_UNCATEGORIZED`   
\- If `principal_present` and `target_present` are both true: `NETWORK_CONNECTION`   
\- If `principal_present` is true: `STATUS_UPDATE`   
\- If `dst_user` is present and `description` contains 'logout': `USER_LOGOUT`   
\- If `dst_user` is present and `description` does not contain 'logout': `USER_LOGIN`  
metadata.vendor_name | metadata.vendor_name | The value is set to "CISCO".  
metadata.product_name | metadata.product_name | The value is set to "CISCO_PRIME".  
metadata.log_type | metadata.log_type | The value is set to "CISCO_PRIME".  
network.session_id | network.session_id | The value is taken from the `session_id` field, which is extracted from the raw log using grok patterns.  
principal.application | principal.application | The value is taken from the `application_name` field, which is extracted from the raw log using grok patterns.  
principal.asset.ip | principal.asset.ip | The value can come from the following fields: `client_ip_address`, `device_ip`, `ip_address`, `principal_ip`, `target_ip`.  
principal.asset.product_object_id | principal.asset.product_object_id | The value is taken from the `oid` field, which is extracted from the raw log using grok patterns.  
principal.asset_id | principal.asset_id | The value can come from the following fields: `device_id`, `id`.  
principal.ip | principal.ip | The value can come from the following fields: `client_ip_address`, `device_ip`, `ip_address`, `principal_ip`.  
principal.mac | principal.mac | The value can come from the following fields: `mac_address`, `source_mac`.  
principal.port | principal.port | The value is taken from the `principal_port` field, which is extracted from the raw log using grok patterns and converted to an integer.  
principal.process.file.full_path | principal.process.file.full_path | The value is taken from the `file_path` field, which is extracted from the raw log using grok patterns.  
principal.resource.name | principal.resource.name | The value is taken from the `process_name` field, which is extracted from the raw log using grok patterns.  
principal.user.userid | principal.user.userid | The value is taken from the `user_name` field, which is extracted from the raw log using grok patterns or kv filter.  
security_result.action | security_result.action | The value is set to "BLOCK" if `description` contains "fail".  
security_result.description | security_result.description | The value can come from the following fields: `desc`, `description`, `sec_description`.  
security_result.severity | security_result.severity | The value can come from the following fields: `log_level`, `severity`.  
security_result.summary | security_result.summary | The value is taken from the `summary` field, which is extracted from the raw log using grok patterns.  
src.hostname | src.hostname | The value is taken from the `email` field, which is extracted from the raw log using grok patterns.  
target.asset.ip | target.asset.ip | The value is taken from the `target_ip` field, which is extracted from the raw log using grok patterns.  
target.ip | target.ip | The value is taken from the `target_ip` field, which is extracted from the raw log using grok patterns.  
target.mac | target.mac | The value is taken from the `dest_mac` field, which is extracted from the raw log using grok patterns and converted to lowercase.  
target.resource.attribute.labels.key | target.resource.attribute.labels.key | The value is set to "Device Type" or "Device Hostname" depending on the context.  
target.resource.attribute.labels.value | target.resource.attribute.labels.value | The value can come from the following fields: `device_type`, `hostname`.  
target.user.userid | target.user.userid | The value is taken from the `dst_user` field, which is extracted from the raw log using grok patterns.  
extensions.auth.mechanism | extensions.auth.mechanism | The value is set to "USERNAME_PASSWORD" if `dst_user` is present and `description` contains "password".  
extensions.auth.type | extensions.auth.type | The value is set to "MACHINE" if `dst_user` is present.  
`ts` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`principal_hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`target_hostname` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`target_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`device_hostname` | `target.resource.attribute.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-prime-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
