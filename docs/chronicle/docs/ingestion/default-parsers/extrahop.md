---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop/
title: Collect ExtraHop Reveal(x) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:37:31.289729+00:00
---

# Collect ExtraHop Reveal(x) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/extrahop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ExtraHop Reveal(x) logs

**Parser Version:** 12.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ExtraHop Reveal(x) logs to Google Security Operations using Bindplane. ExtraHop Reveal(x) is a network detection and response (NDR) platform that provides real-time visibility into network traffic, enabling organizations to detect threats, investigate incidents, and respond to security events across cloud and on-premises environments.

## Before you begin

Make sure you have the following prerequisites:

  * A **Google SecOps instance**.
  * A **Windows Server 2016 or later** , or a **Linux host** with `systemd`.
  * If running behind a proxy, ensure **firewall ports** are open per the Bindplane agent requirements.
  * **Privileged access** to the ExtraHop Reveal(x) Administration settings.



## Get Google SecOps ingestion authentication file

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Collection Agents**.
  3. Download the **Ingestion Authentication File**. 
  4. Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)&quot; /quiet
         

  3. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with **root** or **sudo** privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:** `sudo systemctl status observiq-otel-collector`
  * **Windows:** `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`



### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/extrahop:
            compression: gzip
            creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
        <    custome>r_id: 'CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: EXTRAHOP
            raw_log_field: body
            ingestion_labels:
        
        service:
          pipelines:
            logs/extrahop_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/extrahop
        




### Configuration parameters

Replace the following placeholders:

  * **`<CUSTOMER_ID>`**: Your Google SecOps customer ID.
  * Update the **`creds_file_path`** to the path where the ingestion authentication file was saved: 
    * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * Update the **`endpoint`** value with your regional endpoint: 
    * **United States** : `malachiteingestion-pa.googleapis.com`
    * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
    * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`



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
         




## Configure ExtraHop Reveal(x) syslog forwarding

### Configure system notification syslog

  1. Sign in to the ExtraHop **Administration** settings (`https://<extrahop-hostname-or-IP-address>/admin`).
  2. In the **Network Settings** section, click **Notifications**.
  3. Click **Syslog**.
  4. Provide the following configuration details: 
     * **Destination** : Enter the IP address of the **Bindplane agent** host.
     * **Protocol** : Select **TCP**.
     * **Port** : Enter the port number configured in the Bindplane agent (for example, `514`).
  5. Click **Test Settings** and then **Save**.



### Configure audit log syslog forwarding

  1. In the ExtraHop **Administration** settings, go to the **Status and Diagnostics** section.
  2. Click **Audit Log > Configure Syslog Settings**.
  3. Provide the following configuration details: 
     * **Destination** : Enter the IP address of the **Bindplane agent** host.
     * **Protocol** : Select **TCP**.
     * **Port** : Enter `514`.
  4. Click **Test Settings** and then **Save**.



### Optional: Configure RFC-compliant syslog format

  1. In the ExtraHop **Administration** settings, click **Running Config > Edit Config**.
  2. Add the following entry under the `syslog_notification` section:
         
         "rfc_compliant_format": "rfc5424"
         

  3. Click **Save** and then **Apply Changes**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`act` | `security_result.action_details` | Raw log value mapping.  
`cat` | `metadata.product_event_type` | Raw log value mapping.  
`deviceExternalId` | `metadata.product_log_id` | Raw log value mapping.  
`dhost` | `target.hostname` | Raw log value mapping.  
`dpt` | `target.port` | Raw log value mapping.  
`dst` | `target.ip` | Raw log value mapping.  
`duser` | `target.user.userid` | Raw log value mapping.  
`msg` | `metadata.description` | Raw log value mapping.  
`proto` | `network.ip_protocol` | Raw log value mapping.  
`severity` | `security_result.severity` | Mapped based on CEF severity value.  
`shost` | `principal.hostname` | Raw log value mapping.  
`spt` | `principal.port` | Raw log value mapping.  
`src` | `principal.ip` | Raw log value mapping.  
`suser` | `principal.user.userid` | Raw log value mapping.  
N/A | `metadata.log_type` | Set to `EXTRAHOP`.  
N/A | `metadata.product_name` | Set to `Reveal(x)`.  
N/A | `metadata.vendor_name` | Set to `ExtraHop`.  
`tar_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`tar_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`extrahop_detail` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert_value` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`jsonPayload.target.ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`jsonPayload.principal.mac` | `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`jsonPayload.target.mac` | `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` | Mapped from changelog  
`jsonPayload.principal.hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`jsonPayload.target.hostname` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`jsonPayload.vulnerability.cvss_vector` | `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_vector` | Mapped from changelog  
`suspicious_domain` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`reference` | `event.idm.read_only_udm.security_result.about.url` | Mapped from changelog  
`sid` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`start_time` | `event.idm.read_only_udm.metadata.event_timestamp` and `event.idm.read_only_udm.security_result.first_discovered_time` | Mapped from changelog  
`update_time` | `event.idm.read_only_udm.security_result.last_updated_time` | Mapped from changelog  
`end_time` | `event.idm.read_only_udm.security_result.last_discovered_time` | Mapped from changelog  
`title` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`risk_score` | `event.idm.read_only_udm.security_result.risk_score` | Mapped from changelog  
`categories` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`participant.endpoint` | `event.idm.read_only_udm.principal.asset.category` | Mapped from changelog  
`participant.object_id` | `event.idm.read_only_udm.principal.asset.product_object_id` | Mapped from changelog  
`participant.object_value` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`participant.hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`participant.username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`participant.endpoint` | `event.idm.read_only_udm.target.asset.category` | Mapped from changelog  
`participant.object_id` | `event.idm.read_only_udm.target.asset.product_object_id` | Mapped from changelog  
`participant.object_value` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`participant.hostname` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`participant.username` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`mitre_tactics.id` | `event.idm.read_only_udm.security_result.attack_details.tactics.id` | Mapped from changelog  
`mitre_tactics.name` | `event.idm.read_only_udm.security_result.attack_details.tactics.name` | Mapped from changelog  
`mitre_techniques.id` | `event.idm.read_only_udm.security_result.attack_details.techniques.id` | Mapped from changelog  
`mitre_techniques.name` | `event.idm.read_only_udm.security_result.attack_details.techniques.name` | Mapped from changelog  
`create_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`url` | `event.idm.read_only_udm.url_back_to_product` | Mapped from changelog  
`time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`security_result.severity` | `CRITICAL` | Mapped from changelog  
`security_result.severity` | `ERROR` | Mapped from changelog  
`security_result.severity` | `HIGH` | Mapped from changelog  
`security_result.severity` | `MEDIUM` | Mapped from changelog  
`security_result.severity` | `LOW` | Mapped from changelog  
`security_result.severity` | `INFORMATIONAL` | Mapped from changelog  
`jsonPayload.msg` | `metadata.description` | Mapped from changelog  
`jsonPayload.srcdata` | `principal.ip` | Mapped from changelog  
`jsonPayload.dstdata` | `target.ip` | Mapped from changelog  
`jsonPayload.dhost` | `target.hostname` | Mapped from changelog  
`jsonPayload.shost` | `principal.hostname` | Mapped from changelog  
`insertId` | `additional.fields` | Mapped from changelog  
`jsonPayload.cn2` | `security_result.risk_score` | Mapped from changelog  
`jsonPayload.name` | `security_result.summary` | Mapped from changelog  
`jsonPayload.rt` | `metadata.event_timestamp` | Mapped from changelog  
`jsonPayload.start", "jsonPayload.end" and "logName` | `additional.fields` | Mapped from changelog  
`resource.labels.method" and "resource.labels.service` | `target.resource.attribute.labels` | Mapped from changelog  
`jsonPayload.cat" and "jsonPayload.cs5` | `security_result.detection_fields` | Mapped from changelog  
`dst` | `target.asset.ip` | Mapped from changelog  
`url` | `principal.url` | Mapped from changelog  
`title", "id", "description_format", "victims.name", "victims.external", "offenders.name", "offenders.externaal", "victim_primary.name", victim_primary.external", "offender_primary.name", and "offender_primary.external` | `additional.fields` | Mapped from changelog  
`dst.type` | `target.resource_type` | Mapped from changelog  
`dst.hostname` | `target.hostname` | Mapped from changelog  
`dst.ipaddr` | `target.ip` | Mapped from changelog  
`dst.role` | `target_resource.attribute.roles` | Mapped from changelog  
`dst.device.macaddr` | `target.mac` | Mapped from changelog  
`src.type` | `principal.resource_type` | Mapped from changelog  
`src.hostname` | `principal.hostname` | Mapped from changelog  
`src.ipaddr` | `principal.ip` | Mapped from changelog  
`src.role` | `principal_resource.attribute.roles` | Mapped from changelog  
`src.device.macaddr` | `principal.mac` | Mapped from changelog  
`api.ip", "api.status", "api.id", "api.start_time", "api.mod_time", "api.categories", "api.update_time", and "api.ticket_id` | `security_result.detection_fields` | Mapped from changelog  
`victims.ipaddr` | `principal.ip` | Mapped from changelog  
`offenders.ipaddr` | `target.ip` | Mapped from changelog  
`victim_primary.ipaddr` | `principal.ip` | Mapped from changelog  
`offender_primary.ipaddr` | `target.ip` | Mapped from changelog  
`api.participants.role", "api.participants.object_id", "api.participants.object_type", and "api.participants.external` | `section_details.fields` | Mapped from changelog  
`risk_score" and "api.risk_score` | `security_result.risk_score` | Mapped from changelog  
`src.endpoint" and "src.device.oid` | `principal.resource.attribute.labels` | Mapped from changelog  
`dst.endpoint" and "dst.device.oid` | `target.resource.attribute.labels` | Mapped from changelog  
`dst.device.ipaddr` | `target.ip` | Mapped from changelog  
`src.device.ipaddr` | `principal.ip` | Mapped from changelog  
`categories_array" and "categories_id` | `additional.fields` | Mapped from changelog  
`src` | `principal.asset.ip` | Mapped from changelog  
`device_version` | `metadata.product_version` | Mapped from changelog  
`signature` | `security_result.summary` | Mapped from changelog  
`events.vulnerability.description` | `metadata.description` | Mapped from changelog  
`detectionID` | `security_result.rule_labels` | Mapped from changelog  
`event_type` | `STATUS_UPDATE` | Mapped from changelog  
`prin_url` | `principal.url` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extrahop-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
