---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/secureauth-sso/
title: Collect SecureAuth Identity Platform logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:09:14.288875+00:00
---

# Collect SecureAuth Identity Platform logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/secureauth-sso/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SecureAuth Identity Platform logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SecureAuth Identity Platform logs to Google Security Operations using the Bindplane agent.

SecureAuth Identity Platform is a single sign-on and identity management solution that generates syslog messages for authentication events, session activity, access control decisions, and audit trails. The parser extracts fields from syslog and XML-formatted logs using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the SecureAuth Identity Platform
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to SecureAuth



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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

## Configure the syslog and send to Google SecOps

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
            chronicle/secureauth_sso:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: SECUREAUTH_SSO
                raw_log_field: body
        
        service:
            pipelines:
                logs/secureauth_sso_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/secureauth_sso
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Configure SecureAuth Identity Platform

  1. Sign in to the **SecureAuth Identity console** as an administrator.
  2. Select **Logs**.
  3. Provide the following configuration details in the **Log options** section: 
     * **Log instance ID** : Enter the log instance ID, the Application Name or the realm name (for example, `SecureAuth1`).
     * **Audit logs** : Select the **Syslog** checkbox.
     * **Error logs** : Select the **Syslog** checkbox.
     * **Syslog Server** : Enter the IP address of your Bindplane agent.
     * **Syslog Port** : Enter the Bindplane agent port number (for example, `514`).
     * **Syslog RFC spec** : Select **RFC 5424**.
  4. Click **Save**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
action_msg | read_only_udm.target.process.command_line | Value of `action_msg` field  
Appliance | read_only_udm.principal.domain.name | Value of `Appliance` field  
Appliance | read_only_udm.target.administrative_domain | Value of `Appliance` field  
BrowserSession | read_only_udm.network.session_id | Value of `BrowserSession` field  
cat | read_only_udm.metadata.product_event_type | Value of `cat` field  
Category | read_only_udm.metadata.product_event_type | Value of `Category` field  
cn1 | security_result.severity | Mapped based on the value of `cn1` when `cn1Label` is 'Priority': 1 - HIGH, 2 - MEDIUM, 3 or 4 - LOW  
Company | read_only_udm.additional.fields.value.string_value | Value of `Company` field  
cs1 | read_only_udm.network.session_id | Value of `cs1` field when `cs1Label` is 'BrowserSession'  
cs3 | read_only_udm.additional.fields.value.string_value | Value of `cs3` field when `cs3Label` is 'CompanyName'  
dst | read_only_udm.target.ip | Value of `dst` field  
domain | read_only_udm.principal.domain.name | Value of `domain` field  
dvc | read_only_udm.intermediary.ip | Value of `dvc` field  
EventID | read_only_udm.metadata.product_log_id | Value of `EventID` field  
HostName | read_only_udm.principal.hostname | Value of `HostName` field when grok fails to match IP address  
HostName | read_only_udm.principal.ip | Value of `HostName` field when grok matches IP address  
ip | read_only_udm.principal.ip | Value of `ip` field  
Message | read_only_udm.metadata.description | Value of `Message` field  
Message | security_result.description | Value of `Message` field  
nat_ip | read_only_udm.principal.nat_ip | Value of `nat_ip` field  
Priority | security_result.severity | Mapped based on the value of `Priority`: 1 - HIGH, 2 - MEDIUM, 3 or 4 - LOW  
SAMLConsumerURL | read_only_udm.target.url | Value of `SAMLConsumerURL` field  
sec_msg | security_result.description | Value of `sec_msg` field  
SecureAuthIdPAppliance | read_only_udm.target.administrative_domain | Value of `SecureAuthIdPAppliance` field  
SecureAuthIdPApplianceMachineName | read_only_udm.target.hostname | Value of `SecureAuthIdPApplianceMachineName` field  
SecureAuthIdPDestinationSiteUrl | read_only_udm.target.url | Value of `SecureAuthIdPDestinationSiteUrl` field  
SecureAuthIdPProductType | read_only_udm.additional.fields.value.string_value | Value of `SecureAuthIdPProductType` field  
session | read_only_udm.network.session_id | Value of `session` field  
spid | read_only_udm.target.process.pid | Value of `spid` field  
src | read_only_udm.principal.ip | Value of `src` field  
suser | read_only_udm.target.user.userid | Value of `suser` field  
UserAgent | read_only_udm.network.http.user_agent | Value of `UserAgent` field  
UserHostAddress | read_only_udm.principal.nat_ip | Value of `UserHostAddress` field  
UserHostAddress | read_only_udm.target.ip | Value of `UserHostAddress` field  
UserID | read_only_udm.principal.user.userid | Value of `UserID` field  
Version | read_only_udm.metadata.product_version | Value of `Version` field  
| read_only_udm.additional.fields.key | Hardcoded value - 'CompanyName'  
| read_only_udm.additional.fields.key | Hardcoded value - 'Company'  
| read_only_udm.additional.fields.key | Hardcoded value - 'SecureAuthIdPProductType'  
| read_only_udm.extensions.auth.type | Hardcoded value - 'SSO'  
| read_only_udm.metadata.event_type | 'USER_LOGIN' if `SecureAuthIdPAuthGuiMode` == `0` and `auth_result` == `Success`, 'USER_CHANGE_PERMISSIONS' if `SecureAuthIdPAuthGuiMode` == `0` and `auth_result` ==`WS-Trust success.`, 'USER_LOGOUT' if `SecureAuthIdPAuthGuiMode` == `0` and `auth_result` == `Session Aborted`, 'NETWORK_CONNECTION' if `UserHostAddress` != `and `HostName` !=`, 'STATUS_UPDATE' if `ip` != `or `HostName` !=`, 'USER_UNCATEGORIZED' if `UserHostAddress` != `and `HostName` ==` and `UserID` != ``, otherwise - 'GENERIC_EVENT'  
| read_only_udm.metadata.log_type | Hardcoded value - 'SECUREAUTH_SSO'  
| read_only_udm.metadata.product_name | Hardcoded value - 'SECUREAUTH_SSO'  
| read_only_udm.metadata.vendor_name | Hardcoded value - 'SECUREAUTH_SSO'  
| read_only_udm.target.user.email_addresses | Value of `user_email` field when `not_email` is false  
| security_result.severity | 'HIGH' if `cn1Label` == `Priority` and `cn1` == `1`, 'MEDIUM' if `cn1Label` == `Priority` and `cn1` == `2`, 'LOW' if `cn1Label` == `Priority` and `cn1` in [`3`, `4`], 'HIGH' if `Priority` == `1`, 'MEDIUM' if `Priority` == `2`, 'LOW' if `Priority` in [`3`, `4`]  
`_timestamp` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`i_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`i_port` | `event.idm.read_only_udm.intermediary.port` | Mapped from changelog  
`parsed.LogChannel` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`parsed.FormatVersion` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`parsed.EventID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`parsed.CompanyID` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`parsed.Realm` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`parsed.UserHostAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`parsed.UserHostAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`host.name` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`host.name` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`parsed.RequestID` | `event.idm.read_only_udm.metadata.id` | Mapped from changelog  
`meta.cloud.availability_zone` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`meta.cloud.region` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`host.id` | `event.idm.read_only_udm.principal.resource.id` | Mapped from changelog  
`LogstashPod` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`fields.ApplianceID` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`LogChannel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`FormatVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EventID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`parsed.UserAgent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`parsed.ApplianceID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`beat.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`beat.hostname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`beat.version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`fields.CompanyID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`derived.CompanyIndex` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`derived.EventType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`prospector.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`input.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`parsed_Message` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`meta.cloud.machine_type` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`ApplianceType` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`parsed.Version` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`host.architecture` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`host.os.platform` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`host.os.version` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`host.os.build` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`host.os.family` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`host.os.name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`meta.cloud.provider` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`derived.LogChannelIndex` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`document_id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`meta.cloud.instance_id` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`tags` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`Realm` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`CompanyID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PEN` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplianceID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ApplianceMachineName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RequestID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UseJava` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/secureauth-sso-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
