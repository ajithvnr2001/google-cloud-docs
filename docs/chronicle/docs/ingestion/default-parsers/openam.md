---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openam/
title: Collect ForgeRock OpenAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:26.156917+00:00
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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/openam:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
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

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/openam:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: OPENAM
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
