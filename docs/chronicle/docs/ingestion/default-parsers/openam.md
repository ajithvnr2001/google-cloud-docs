---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openam/
title: Collect ForgeRock OpenAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:24:33.724986+00:00
---

# Collect ForgeRock OpenAM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ForgeRock OpenAM logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ForgeRock OpenAM logs to Google Security Operations using the Bindplane agent.

ForgeRock OpenAM is an access management solution that generates syslog messages for authentication events, access control decisions, session activity, and configuration changes. The parser extracts fields from JSON-formatted audit logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the ForgeRock OpenAM server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrator access to the AM console (for example, `amAdmin`)



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
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/openam:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: OPENAM
                raw_log_field: body
        
        service:
            pipelines:
                logs/openam_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/openam
        




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
             




## Configure syslog handlers for ForgeRock OpenAM

  1. Sign in to the AM console as an administrator (for example, **amAdmin**).
  2. To create the event handler in the **global configuration** , go to **Configure > Global Services > Audit Logging**. 
     * To create the event handler in a **realm** , go to **Realms > Realm Name > Services > Audit Logging**.
  3. Click **Add a Secondary Configuration > Syslog**.
  4. Provide the following configuration details: 
     * **Name** : Enter a name for the event handler (for example, `Syslog Event Handler`).
     * **Server hostname** : Enter the Bindplane agent IP address.
     * **Server port** : Enter the Bindplane agent port number (for example, `514` for UDP).
     * **Transport Protocol** : Select **UDP**.
     * **Connection timeout** : Enter the number of seconds to connect (for example, `120`).
     * Optional: Enable the **Buffering** option.
  5. Click **Create**.
  6. On the **General Handler Configuration** tab, select **Enabled** to activate the event handler.
  7. Select the topics for audit logs: 
     * Access
     * Activity
     * Authentication
     * Configuration
  8. Click **Save**.
  9. On the **Syslog Configuration** tab, provide the following configuration details: 
     * **Server hostname** : Enter the Bindplane IP address.
     * **Server port** : Enter the Bindplane port number.
     * **Connection timeout** : Enter the number of seconds to connect (for example, `120`).
     * **Transport Protocol** : Select **UDP**.
     * **Facility** : Select **Local0**.
     * All topics set the severity to **INFORMATIONAL**.
  10. Click **Save**.
  11. On the **Buffering** tab, select **Buffering Enabled** to activate it.
  12. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`client.ip` | `principal.ip` | The IP address of the client making the request.  
`client.ip` | `principal.asset.ip` | The IP address of the client asset making the request.  
`client.port` | `principal.port` | The port used by the client making the request.  
`entries[0].info.authLevel` | `principal.resource.resource_subtype` | The authentication level associated with the event. Prefixed with "authLevel:".  
`entries[0].info.displayName` | `security_result.description` | A descriptive name for the node in the authentication tree.  
`entries[0].info.ipAddress` | `principal.asset.ip` | The IP address associated with the principal in the event.  
`entries[0].info.ipAddress` | `principal.ip` | The IP address associated with the principal in the event.  
`entries[0].info.nodeId` | `principal.resource.id` | The unique identifier of the node in the authentication tree. Prefixed with "nodeId:".  
`entries[0].info.nodeOutcome` | `principal.resource.attribute.labels.value` | The outcome of the node in the authentication tree.  
`entries[0].info.nodeType` | `principal.resource.type` | The type of the node in the authentication tree. Prefixed with "nodeType:".  
`entries[0].info.treeName` | `principal.resource.name` | The name of the authentication tree. Prefixed with "treeName:".  
`eventName` | `metadata.product_event_type` | The raw event name from the OpenAM logs.  
`http.request.headers.host[0]` | `target.asset.hostname` | The hostname of the target server, extracted from the `host` header.  
`http.request.headers.host[0]` | `target.hostname` | The hostname of the target server, extracted from the `host` header.  
`http.request.headers.user-agent[0]` | `network.http.user_agent` | The user-agent of the HTTP request.  
`http.request.method` | `network.http.method` | The HTTP method used in the request.  
`http.request.path` | `target.url` | The path of the HTTP request URL.  
`info.failureReason` | `security_result.summary` | The reason for an authentication failure. Hardcoded to "SSO". Determined by logic based on `eventName` and other fields. Can be `GENERIC_EVENT`, `USER_LOGIN`, `USER_LOGOUT`, `NETWORK_HTTP`, or `STATUS_UPDATE`. Hardcoded to "OPENAM". Hardcoded to "OpenAM". Hardcoded to "ForgeRock".  
`principal` | `target.user.userid` | The user ID involved in the event, extracted from either `userId`, `principal`, or `runAs` fields.  
`result` | `security_result.action_details` | The result of the event (e.g., "SUCCESSFUL", "FAILED").  
`response.detail.reason` | `security_result.summary` | The reason for a failure in an access outcome event.  
`response.status` | `security_result.action_details` | The status of the response in an access outcome event.  
`runAs` | `target.user.userid` | The user ID involved in the event, extracted from either `userId`, `principal`, or `runAs` fields.  
`security_result.action` | `security_result.action` | The action taken as a result of the security event (e.g., "ALLOW", "BLOCK").  
`server.ip` | `target.asset.ip` | The IP address of the target server.  
`server.ip` | `target.ip` | The IP address of the target server.  
`server.port` | `target.port` | The port of the target server.  
`timestamp` | `metadata.event_timestamp` | The timestamp of the event.  
`trackingIds` | `metadata.product_log_id` | The tracking ID associated with the event.  
`transactionId` | `metadata.product_deployment_id` | The transaction ID associated with the event.  
`userId` | `target.user.userid` | The user ID involved in the event, extracted from either `userId`, `principal`, or `runAs` fields.  
`userId` | `target.user.group_identifiers` | The group identifiers associated with the user.  
`am_group` | `target.user.group_identifiers` | The group identifiers associated with the user.  
`am_user` | `target.user.email_addresses` | The email address of the user, if present in the `am_user` field.  
`loginID[0]` | `target.user.userid` | The login ID used in the event.  
`loginID[0]` | `target.user.email_addresses` | The email address used for login, if present in the `loginID` field.  
`hostip` | `intermediary.hostname` | The hostname of an intermediary device.  
`hostip` | `intermediary.ip` | The IP address of an intermediary device.  
`src_ip` | `principal.asset.ip` | The source IP address.  
`src_ip` | `principal.ip` | The source IP address.  
`desc` | `metadata.description` | The description of the event.  
`payload` | `metadata.description` | The payload of the event.  
`http.request.headers.host.0` | `tatget.hostname` | Mapped from changelog  
`http.request.headers.user-agent.0` | `network.http.user_agent` | Mapped from changelog  
`extensions.auth.type` | `SSO` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
