---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail-filter/
title: Collect Proofpoint Email Filter logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:24:46.015417+00:00
---

# Collect Proofpoint Email Filter logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint Email Filter logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint Email Filter logs to Google Security Operations using the Bindplane agent.

Proofpoint Email Protection (PPS) is an email security gateway that provides spam filtering, threat detection, and email policy enforcement. It supports syslog forwarding and CEF log integration for exporting security events and mail transaction logs.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Proofpoint Protection Server (PPS)
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Proofpoint Protection Server (PPS) management console with administrator permissions



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
            chronicle/proofpoint_mail_filter:
                compression: gzip
                creds_file_path: '<CREDS_FILE_PATH>'
                customer_id: '<CUSTOMER_ID>'
                endpoint: <REGION_ENDPOINT>
                log_type: PROOFPOINT_MAIL_FILTER
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/proofpoint_mail_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/proofpoint_mail_filter
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: Receives syslog over TCP. Use `udplog` if you configure UDP transport in PPS.
    * `0.0.0.0:514`: Listens on all interfaces on port 514. Change the port if needed (for example, `1514` for non-root Linux).
  * **Exporter configuration:**

    * `<CREDS_FILE_PATH>`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<CUSTOMER_ID>`: Customer ID from the **Get Google SecOps customer ID** step.
    * `<REGION_ENDPOINT>`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list.



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
             




## Configure Proofpoint Email Protection syslog forwarding

### Option 1: Configure syslog forwarding in Proofpoint PPS

  1. Sign in to the **Proofpoint Protection Server (PPS)** management console.
  2. Navigate to **System > Logs and Reports > Log Settings**.
  3. In the **Remote Log Settings** section, configure the following: 
     * **Protocol** : Select **Syslog**.
     * **Syslog server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Transport** : Select **TCP** (must match the Bindplane agent receiver configuration). TLS is also supported for secure forwarding.
  4. In the **Local Log Options** section, configure the logging verbosity as needed.
  5. Click **Save Changes**.

**Note:** Proofpoint on Demand (PoD) cloud deployments require an additional "Remote Syslog Forwarding" license to send logs from the cloud to an on-premises syslog server via TLS.



### Option 2: Configure CEF log integration

  1. Sign in to the **Proofpoint Protection Server (PPS)** management console.
  2. Navigate to **Configuration > Integrations > Integrated SIEM**.
  3. Click the **SIEM Log Integration** tab.
  4. Select **Enable export to ArcSight format** to activate CEF log integration.
  5. Configure the syslog destination server: 
     * **Host** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
  6. Click **Save**.
  7. Verify that CEF-formatted logs are being received by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| about | Additional information about the event  
adultscore, attachments, hops, routes, notroutes, eid, querydepth, selector, spamscore, phishscore, mod, status, folder | additional.fields | Vendor-specific event data that cannot be adequately represented within the formal sections of the UDM model  
auth | extensions.auth.type | Authentication type used  
| intermediary | Information about intermediary devices involved in the event  
domain | intermediary.administrative_domain | Administrative domain of the intermediary  
hops-ip, lip, interm_ip | intermediary.ip | IP address of the intermediary  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
prod_event_type | metadata.product_event_type | Product-specific event type  
engine | metadata.product_version | Version of the product that generated the event  
proto, mailer | network.application_protocol | Application protocol used in the network connection  
hfrom, from | network.email.from | Email sender address  
m, msgid, net_mail_id, hdr_mid | network.email.mail_id | Unique identifier for the email message  
subject | network.email.subject | Subject line of the email  
to | network.email.to | Email recipient addresses  
received_byte | network.received_bytes | Number of bytes received in the network connection  
s | network.session_id | Unique identifier for the network session  
cipher | network.tls.cipher | TLS cipher suite used  
tls_version, version | network.tls.version | TLS version used  
domain | principal.administrative_domain | Administrative domain of the principal  
proc | principal.application | Application involved in the event  
device, host | principal.asset.hostname | Hostname of the asset associated with the principal  
ip, srcip | principal.asset.ip | IP address of the asset associated with the principal  
guid | principal.asset_id | Unique identifier for the asset  
device, host | principal.hostname | Hostname of the principal  
ip, srcip | principal.ip | IP address of the principal  
country | principal.location.country_or_region | Country or region of the principal's location  
cmd | principal.process.command_line | Command line used to launch the process  
file, name | principal.process.file.full_path | Full path of the file involved in the process  
sz, size | principal.process.file.size | Size of the file in bytes  
pid, process_id | principal.process.pid | Process ID  
action, security_action | security_result.action | Action taken by the security product  
classifier | security_result.category | Category of the security result  
class, internalId | security_result.detection_fields | Fields used for detection  
rule | security_result.rule_name | Name of the rule that triggered the security result  
security_desc | security_result.summary | Summary of the security result  
hostname | target.asset.hostname | Hostname of the asset associated with the target  
hostname | target.hostname | Hostname of the target  
| metadata.product_name | Name of the product that generated the event  
| metadata.vendor_name | Name of the vendor that produced the product  
`AppAccessContext.AADSessionId` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`ClientAppName` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`AppAccessContext.CorrelationId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AppAccessContext.UniqueTokenId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AppAccessContext.UserObjectId` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`Id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`Operation` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`RecordType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`UserKey` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`UserType` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`Version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Workload` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`ClientIP` | `event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`UserId` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`AuthenticationType` | `event.idm.read_only_udm.extensions.auth.auth_details` | Mapped from changelog  
`BrowserName` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`BrowserVersion` | `event.idm.read_only_udm.network.http.parsed_user_agent.browser_version` | Mapped from changelog  
`CorrelationId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`EventSource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`GeoLocation` | `event.idm.read_only_udm.principal.location.name` | Mapped from changelog  
`IsManagedDevice` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`ItemType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ListId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ListItemUniqueId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Platform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Site` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`UserAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`WebId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`HighPriorityMediaProcessing` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ListBaseType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ListServerTemplate` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SourceRelativeUrl` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`net_mail_id" and "hdr_mid` | `network.email.mail_id` | Mapped from changelog  
`delay` | `about.resource.attribute.labels` | Mapped from changelog  
`relay` | `intermediary.administrative_domain` | Mapped from changelog  
`device" from "intermediary.hostname` | `principal.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-mail-filter-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
