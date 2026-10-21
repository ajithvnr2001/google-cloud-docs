---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/quest-change-auditor-emc/
title: Collect Quest Change Auditor for EMC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:35:44.274200+00:00
---

# Collect Quest Change Auditor for EMC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/quest-change-auditor-emc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Quest Change Auditor for EMC logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Quest Change Auditor for EMC logs to Google Security Operations using the Bindplane agent.

Quest Change Auditor for EMC is a real-time change auditing and reporting solution for EMC storage environments. It captures detailed information about changes to files, folders, and permissions on EMC storage systems, providing comprehensive audit trails for compliance and security monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Quest Change Auditor coordinator server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Quest Change Auditor for EMC console with administrator permissions



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
            chronicle/quest_change_auditor_emc:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: QUEST_CHANGE_AUDITOR_EMC
                raw_log_field: body
        
        service:
            pipelines:
                logs/quest_emc_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/quest_change_auditor_emc
        




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
             




## Configure Quest Change Auditor for EMC syslog forwarding

Quest Change Auditor supports native SIEM integration including syslog forwarding through event subscriptions. Configure a syslog event subscription on the coordinator server to forward events to the Bindplane agent.

  1. Open **PowerShell** on the Change Auditor coordinator server with administrator privileges.
  2. Create a syslog event subscription using the following command:
         
         New-CASyslogEventSubscription -Name "Chronicle-Bindplane" -SyslogServer "<BINDPLANE_IP>" -Port 514 -Protocol TCP
         

     * Replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent host (for example, `192.168.1.100`).
  3. Select the event types and audited objects to forward:

     * File and folder changes on EMC storage
     * Permission changes
     * Share modifications
     * Administrative actions
  4. Verify the subscription is active:
         
         Get-CASyslogEventSubscription
         

  5. Verify logs are being received by checking the Bindplane agent logs.

**Note:** The `New-CASyslogEventSubscription` PowerShell cmdlet is part of the Quest Change Auditor management module. Ensure the Change Auditor PowerShell module is installed on the coordinator server before running these commands.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
facility, agentID, eventClassID, subsystemID, facilityID, valueTypeID, actionID, resultID, coordinatorId, parentDomainID, domainDn, siteDn, organizationalUnit, parentObjectID, objectID, objectClass, objectName, attributeName, objectDn, objectCanonical, sslTls, kerberos, adOriginatingObjectID, adUsnChangedPre, adUsnChangedPost, administrator, originAdSite, simpleBind, authPort, adStatusCode, eventId, id, Keywords, EventType, Task, ThreadID, Channel, Opcode | additional.fields | Merged as labels with keys matching field names  
description | metadata.description | Value copied directly  
EventTime | metadata.event_timestamp | Converted from epoch ms to timestamp  
event_data | metadata.event_type | Set based on conditional logic on event_data  
EventReceivedTime | metadata.ingested_timestamp | Converted from epoch ms to timestamp  
categoryBehavior, EventID | metadata.product_event_type | Value from categoryBehavior if not empty, else EventID  
RecordNumber | metadata.product_log_id | Value copied directly  
SourceModuleType | observer.application | Value copied directly  
SourceModuleName | observer.resource.attribute.labels | Merged as label  
Domain | principal.administrative_domain | Value copied directly  
SourceName | principal.application | Value copied directly  
origin, Hostname | principal.asset.hostname | Value from origin if not empty, else Hostname  
ipAddress, originIPv4 | principal.asset.ip | Value from ipAddress if not empty, else from originIPv4 if valid IP  
origin, Hostname | principal.hostname | Value from origin if not empty, else Hostname  
ipAddress, originIPv4 | principal.ip | Value from ipAddress if not empty, else from originIPv4 if valid IP  
osVersion | principal.platform | Set to "WINDOWS" if osVersion matches Windows  
osVersion | principal.platform_version | Value copied directly if Windows  
ProcessID | principal.process.pid | Value copied directly  
link | principal.url | Value copied directly  
AccountType | principal.user.attribute.roles.name | Value copied directly  
adUserMail, initiatorMail | principal.user.email_addresses | Merged from adUserMail if matches email pattern, and initiatorMail  
userDisplay, initiatorUserName | principal.user.user_display_name | Value from userDisplay if not empty, else initiatorUserName  
userSid, AccountName | principal.user.userid | Value from userSid if not empty, else AccountName  
UserID | principal.user.windows_sid | Value copied directly  
result | security_result.action | Set to "ALLOW" if result matches Success, "BLOCK" if matches failure  
result | security_result.action_details | Value copied directly  
start, end, timeDetected, timeZoneOffset, timeBatched, timeOfDay, siteID | security_result.detection_fields | Merged as labels  
description | security_result.description | Value copied directly  
SeverityValue | security_result.severity | Set to INFORMATIONAL if 1-3, ERROR if 4, CRITICAL if 5  
Severity | security_result.severity_details | Value copied directly  
Category | security_result.summary | Value copied directly  
file_path | src.file.full_path | Value copied directly  
file_path | src.process.file.full_path | Value copied directly  
initiatorMail | src.user.email_addresses | Value copied directly  
initiatorUserName | src.user.user_display_name | Value copied directly  
initiatorSid | src.user.userid | Value copied directly  
domainFqdn | target.administrative_domain | Value copied directly  
subsystem | target.application | Value copied directly  
serverFqdn, ip_or_host | target.asset.hostname | Value from serverFqdn if not empty, else ip_or_host if not IP  
ip_or_host | target.asset.ip | Extracted IP from ip_or_host  
domainID | target.asset_id | Set to "DOMAIN ID:" + domainID  
file_path, new_path | target.file.full_path | Value from file_path or new_path depending on EventID  
serverFqdn, ip_or_host | target.hostname | Value from serverFqdn if not empty, else ip_or_host if not IP  
site | target.location.name | Value copied directly  
file_path, new_path | target.process.file.full_path | Value from file_path or new_path depending on EventID  
filer_name | target.resource.attribute.labels | Merged as label  
computer | target.resource.name | Value copied directly  
serverDn | target.user.group_identifiers | Value copied directly  
| metadata.product_name | Set to "Quest Change Auditor EMC"  
| metadata.vendor_name | Set to "Quest"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/quest-change-auditor-emc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
