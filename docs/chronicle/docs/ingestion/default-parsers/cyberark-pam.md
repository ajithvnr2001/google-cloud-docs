---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pam/
title: Collect CyberArk PAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:13:42.334638+00:00
---

# Collect CyberArk PAM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-pam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CyberArk PAM logs

**Parser Version:** 11.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CyberArk PAM (Privileged Access Manager) logs to Google Security Operations using Bindplane. CyberArk PAM secures, manages, and monitors privileged credentials across on-premises and cloud environments. It provides a Digital Vault for storing privileged account credentials, session isolation and monitoring, automated password rotation, and detailed audit logs for all privileged access activities.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the CyberArk PAM Vault and PVWA (Password Vault Web Access) with administrative permissions.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agent**.
  3. Download the **Ingestion Authentication File**. 
     * Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

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

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             tcplog:
                 # Replace the port and IP address as required
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/chronicle_w_labels:
                 compression: gzip
                 # Adjust the path to the credentials file you downloaded in Step 1
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 # Replace with your actual customer ID from Step 2
                 customer_id: <PLACEHOLDER_CUSTOMER_ID>
                 endpoint: malachiteingestion-pa.googleapis.com
                 # Add optional ingestion labels for better organization
                 log_type: 'CYBERARK_PAM'
                 raw_log_field: body
                 ingestion_labels:
         
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - tcplog
                     exporters:
                         - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<PLACEHOLDER_CUSTOMER_ID>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in the **Get Google SecOps ingestion authentication file** section.



## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure CyberArk PAM syslog forwarding

CyberArk PAM sends audit data to a SIEM via the Vault's syslog integration configured in the `dbparm.ini` file.

### Configure the Vault server

  1. Sign in to the CyberArk Vault server with administrative privileges.
  2. Navigate to the Vault installation directory and open the `dbparm.ini` file:

     * **Default path (Windows)** : `C:\Program Files (x86)\PrivateArk\Server\Conf\dbparm.ini`
     * **Default path (Linux)** : `/opt/CARKaim/vault/Conf/dbparm.ini`
**Note:** The actual path may differ depending on your CyberArk PAM installation. Verify the path with your CyberArk administrator.
  3. Add or modify the following syslog configuration parameters in `dbparm.ini`:
         
         SyslogTranslatorFile=Syslog\CASP.xsl
         SyslogServerIP=<BINDPLANE_AGENT_IP>
         SyslogServerPort=514
         SyslogServerProtocol=TCP
         SyslogMessageCodeFilter=0-999
         UseSyslogFormat=Yes
         SyslogSendAuditAsJSON=Yes
         

  4. Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host (for example, `192.168.1.100`).




### Configuration parameter reference

Parameter | Value | Description  
---|---|---  
`SyslogTranslatorFile` | `Syslog\CASP.xsl` | XSL translation file for syslog format  
`SyslogServerIP` | Bindplane agent IP | IP address of the syslog receiver  
`SyslogServerPort` | `514` | Port number for syslog (match Bindplane config)  
`SyslogServerProtocol` | `TCP` | Transport protocol (TCP recommended for reliable delivery)  
`SyslogMessageCodeFilter` | `0-999` | Range of message codes to forward (0-999 = all)  
`UseSyslogFormat` | `Yes` | Send logs in standard syslog format  
`SyslogSendAuditAsJSON` | `Yes` | Send audit records in JSON format for better parsing  
  
### Restart the Vault service

  1. After modifying `dbparm.ini`, restart the CyberArk Vault service:

     * **Windows** : Open **Services** console, find **CyberArk Vault** , right-click, and select **Restart**.
     * **Linux** : Run the following command:
    
    sudo systemctl restart vault
    

  2. Verify logs are being received by checking the Bindplane agent logs:
         
         sudo journalctl -u observiq-otel-collector -f
         




### Configure PVWA audit logging (optional)

To forward PVWA (Password Vault Web Access) activity logs:

  1. Sign in to the **PVWA** web interface as an administrator.
  2. Go to **Administration > Options > Audit**.
  3. Verify that **Send syslog messages** is enabled.
  4. The PVWA uses the Vault's syslog configuration from `dbparm.ini`.



For more information about CyberArk PAM syslog integration, see the [CyberArk PAM documentation](https://docs.cyberark.com/pam).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Vendor` | `metadata.vendor_name` | Set to "CyberArk".  
`Product` | `metadata.product_name` | Set to "PAM" or "Vault".  
`Version` | `metadata.product_version` | The CyberArk PAM version.  
`MessageID` | `metadata.product_event_type` | The audit action code.  
`Message` | `metadata.description` | The human-readable audit message.  
`Severity` | `security_result.severity` | Mapped from CyberArk severity level.  
`Issuer` | `principal.user.userid` | The user who performed the action.  
`Station` | `principal.ip` | The source IP address of the session.  
`SourceUser` | `principal.user.userid` | The source user initiating the action.  
`TargetUser` | `target.user.userid` | The target privileged account.  
`SafeName` | `target.resource.name` | The CyberArk Safe containing the credential.  
`AccountName` | `target.resource.attribute.labels` | The privileged account name.  
`Address` | `target.hostname` | The target system hostname or address.  
`PolicyID` | `security_result.rule_name` | The platform policy ID.  
`Reason` | `security_result.description` | The reason provided for the action.  
`RequestID` | `network.session_id` | The dual-control request ID.  
`GatewayStation` | `intermediary.ip` | The PSM gateway IP address.  
`Timestamp` | `metadata.event_timestamp` | The event timestamp.  
`Command` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`User` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`syslog.audit_record.TargetUser` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`syslog.audit_record.TargetUser` | `event.idm.read_only_udm.target.user.attribute.labels` | Mapped from changelog  
`SrcHost` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`DstHost` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`ProcessName` | `event.idm.read_only_udm.target.process.file.names` | Mapped from changelog  
`SessionID` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`Protocol` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`syslog.audit_record.Issuer` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`syslog.audit_record.SourceUser` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`syslog.audit_record.SourceUser` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`syslog.audit_record.Action` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`syslog.audit_record.Version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`syslog.audit_record.Severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`syslog.audit_record.Severity` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`syslog.audit_record.Location` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`syslog.audit_record.Message` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`syslog.audit_record.CAProperties.CAProperty` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`format` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog.audit_record.Rfc5424` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog.audit_record.Timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog.audit_record.IsoTimestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog.audit_record.Hostname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog.audit_record.Vendor` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog.audit_record.Product` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog.audit_record.RequestId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PSMID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs2` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`event_data.created` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`host` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`dvc` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`dvc` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`PSMID` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`PSMID` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`GatewayStation` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`GatewayStation` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`reason` | `event.idm.read_only_udm.target.process.file.full_path` | Mapped from changelog  
`ApplicationType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`RDPOffset` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`VIDOffset` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ConnectionComponentId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ProcessId` | `event.idm.read_only_udm.target.process.pid` | Mapped from changelog  
`leef_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`leef_event_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`inter_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`EventMessage` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`src` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`usrName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`Reason` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`Category` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`sev` | `event.idm.read_only_udm.security_result.severity` and `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`address` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`Safe` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`username` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`logondomain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`devicetype` | `event.idm.read_only_udm.principal.resource.resource_subtype` | Mapped from changelog  
`header_host` | `event.idm.read_only_udm.src.hostname` | Mapped from changelog  
`Ticket_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Ticketing_System` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Ticketing_Audit_Safe` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Action` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`name` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`policyid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`actionType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`auditType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.app_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.end_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.is_internal_application` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.scopes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.start_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.token_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.user_guid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`identityType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tenantId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`component` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`serviceName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.DPA.ephemeral_user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.DPA.access_method` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.DPA.assigned_domain_groups` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.DPA.assigned_groups` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.DPA.authentication_methods` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.DPA.connection_string` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.DPA.maximum_session_duration` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.deny_by_user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.mfa_reason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.factors` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.auth_method` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.entity_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customData.mfa_initiator` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`safe` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cloudAssets` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cloudIdentities` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cloudResources` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`applicationCode` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`auditCode` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`userId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`username` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`cloudProvider` | `event.idm.read_only_udm.principal.cloud.environment` | Mapped from changelog  
`customData.client` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`uuid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`source` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`source` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`accessMethod` | `event.idm.read_only_udm.extensions.auth.auth_details` | Mapped from changelog  
`accountId` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`sessionId` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`target` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`target` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`targetPlatform` | `event.idm.read_only_udm.target.labels` | Mapped from changelog  
`customData.DPA.source_hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`customData.DPA.source_hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`customData.DPA.source_user` | `event.idm.read_only_udm.principal.user.attributes.labels` | Mapped from changelog  
`customData.DPA.target_machine` | `event.idm.read_only_udm.target.labels` | Mapped from changelog  
`customData.entity_name` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`customData.entity_name` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`customData.geoip_latitude` | `event.idm.read_only_udm.principal.location.region_latitude` | Mapped from changelog  
`customData.geoip_longitude` | `event.idm.read_only_udm.principal.location.region_longitude` | Mapped from changelog  
`customData.geoip_city_name` | `event.idm.read_only_udm.principal.location.city` | Mapped from changelog  
`customData.mfa_result` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`customData.geoip_country_name` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`customData.request_device_os` | `event.idm.read_only_udm.principal.asset.platform_software.platform` | Mapped from changelog  
`customData.request_broswer_name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`customData.geoip_country_code` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`accountName` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`targetAccount` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`customData.PAM.new_target` | `event.idm.read_only_udm.target.user.attribute.labels` | Mapped from changelog  
`customData.PAM.target` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`customData.directory_service_id` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`customData.user_id` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`customData.user_name` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`customData.mfa_initiator` | `event.idm.read_only_udm.extensions.auth.type` | Mapped from changelog  
`signature_id` | `metadata.product_event_type` | Mapped from changelog  
`app` | `target.application` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-pam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
