---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hid-digitalpersona/
title: Collect HID DigitalPersona logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:10:01.185998+00:00
---

# Collect HID DigitalPersona logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hid-digitalpersona/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HID DigitalPersona logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HID DigitalPersona logs into Google Security Operations using the Bindplane agent.

HID DigitalPersona is a multi-factor authentication and identity management solution that provides passwordless authentication, credential management, and access control for Windows environments. DigitalPersona components write authentication, credential management, user management, and policy events to dedicated Windows Event Log channels when significant activities occur.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later with `systemd`
  * Network connectivity between the Bindplane agent and the internet
  * If running behind a proxy, ensure that firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Windows Server where DigitalPersona is installed
  * DigitalPersona AD or LDS version 4.2.0 or later installed and configured



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system by following these instructions.

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

## Configure Bindplane agent to ingest Windows Event Logs and send to Google SecOps

### Locate the configuration file

  1. Open **Command Prompt** as an administrator.
  2. Navigate to the Bindplane agent installation directory and open the configuration file:
         
         notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
         




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
             windowseventlog/digitalpersona_core:
                 channel: DigitalPersona-Altus-Core/Operational
                 raw: true
                 start_at: end
             windowseventlog/digitalpersona_logon:
                 channel: DigitalPersona-Altus-Logon/Operational
                 raw: true
                 start_at: end
             windowseventlog/digitalpersona_policies:
                 channel: DigitalPersona-Altus-Policies/Operational
                 raw: true
                 start_at: end
             windowseventlog/digitalpersona_radius:
                 channel: DigitalPersona-Altus-RADIUS/Operational
                 raw: true
                 start_at: end
             windowseventlog/digitalpersona_passwordmanager:
                 channel: DigitalPersona-Altus-PasswordManager/Operational
                 raw: true
                 start_at: end
             windowseventlog/digitalpersona_identityprovider:
                 channel: DigitalPersona-Altus-IdentityProvider/Operational
                 raw: true
                 start_at: end
             windowseventlog/digitalpersona_adfauthprovider:
                 channel: DigitalPersona-Altus-AdfAuthProvider/Operational
                 raw: true
                 start_at: end
         
         processors:
             batch:
         
         exporters:
             chronicle/digitalpersona:
                 compression: gzip
                 creds: '{
                     "type": "service_account",
                     "project_id": "YOUR_PROJECT_ID",
                     "private_key_id": "YOUR_PRIVATE_KEY_ID",
                     "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
                     "client_email": "YOUR_CLIENT_EMAIL",
                     "client_id": "YOUR_CLIENT_ID",
                     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                     "token_uri": "https://oauth2.googleapis.com/token",
                     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                     "client_x509_cert_url": "YOUR_CERT_URL"
                 }'
                 customer_id: 'YOUR_CUSTOMER_ID'
                 endpoint: malachiteingestion-pa.googleapis.com
                 log_type: 'HID_DIGITALPERSONA'
                 override_log_type: false
                 raw_log_field: body
         
         service:
             pipelines:
                 logs/digitalpersona:
                     receivers:
                         - windowseventlog/digitalpersona_core
                         - windowseventlog/digitalpersona_logon
                         - windowseventlog/digitalpersona_policies
                         - windowseventlog/digitalpersona_radius
                         - windowseventlog/digitalpersona_passwordmanager
                         - windowseventlog/digitalpersona_identityprovider
                         - windowseventlog/digitalpersona_adfauthprovider
                     processors:
                         - batch
                     exporters:
                         - chronicle/digitalpersona
         

  2. Replace the following placeholders:

     * Exporter configuration:

       * `YOUR_PROJECT_ID`: The project ID from your ingestion authentication file
       * `YOUR_PRIVATE_KEY_ID`: The private key ID from your ingestion authentication file
       * `YOUR_PRIVATE_KEY`: The private key from your ingestion authentication file (ensure proper escaping of newlines)
       * `YOUR_CLIENT_EMAIL`: The client email from your ingestion authentication file
       * `YOUR_CLIENT_ID`: The client ID from your ingestion authentication file
       * `YOUR_CERT_URL`: The client x509 certificate URL from your ingestion authentication file
       * `YOUR_CUSTOMER_ID`: Your Google SecOps customer ID from the previous step
     * Regional endpoint configuration:

       * For **US region** , use `malachiteingestion-pa.googleapis.com`
       * For **Europe region** , use `europe-malachiteingestion-pa.googleapis.com`
       * For **Asia Southeast region** , use `asia-southeast1-malachiteingestion-pa.googleapis.com`
       * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list
**Note:** Instead of manually editing the `creds` field, you can save the ingestion authentication file to a secure location and reference it using `creds_file_path`:  
  
`exporters:`  
` chronicle/digitalpersona:`  
` compression: gzip`  
` creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'`  
` customer_id: 'YOUR_CUSTOMER_ID'`  
` endpoint: malachiteingestion-pa.googleapis.com`  
` log_type: 'HID_DIGITALPERSONA'`  
` override_log_type: false`  
` raw_log_field: body`



### DigitalPersona Event Channels

The configuration above collects events from the following DigitalPersona Windows Event Log channels:

Channel Name | Event Categories | Event ID Range  
---|---|---  
DigitalPersona-Altus-Core/Operational | Credential Management, User Management, Secret Management, Service Management, Credential Authentication, Deployment, OTP Management | 256-4352  
DigitalPersona-Altus-Logon/Operational | Windows Logon | 4864-4873  
DigitalPersona-Altus-Policies/Operational | Policy Management | 5376-5383  
DigitalPersona-Altus-RADIUS/Operational | RADIUS Authentication | 6400-6402  
DigitalPersona-Altus-PasswordManager/Operational | Password Manager | 1536-1557  
DigitalPersona-Altus-IdentityProvider/Operational | Identity Provider | 6656-6765  
DigitalPersona-Altus-AdfAuthProvider/Operational | ADFS Authentication Provider | 6401-6405  
  
### Save the configuration file

After editing, save the file:

  1. Click **File > Save**.
  2. Close Notepad.



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Windows, use one of the following options:

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Services console:

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
    1. Verify the service is running:
           
           sc query observiq-otel-collector
           

    2. Check logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




## Verify DigitalPersona event collection

### Verify Windows Event Log channels are active

  1. Press `Win+R`, type `eventvwr.msc`, and press Enter to open **Event Viewer**.
  2. Navigate to **Applications and Services Logs**.
  3. Expand the **DigitalPersona-Altus-Core** folder.
  4. Right-click **Operational** and select **Properties**.
  5. Verify that **Enable logging** is checked.
  6. Repeat steps 3-5 for the following channels:

     * DigitalPersona-Altus-Logon/Operational
     * DigitalPersona-Altus-Policies/Operational
     * DigitalPersona-Altus-RADIUS/Operational
     * DigitalPersona-Altus-PasswordManager/Operational
     * DigitalPersona-Altus-IdentityProvider/Operational
     * DigitalPersona-Altus-AdfAuthProvider/Operational



### Verify events are being collected

  1. In **Event Viewer** , navigate to one of the DigitalPersona channels (for example, **DigitalPersona-Altus-Core > Operational**).
  2. Verify that events are being logged.
  3. Perform a test authentication or credential management operation in DigitalPersona to generate new events.
  4. Refresh the Event Viewer to see the new events.



### Verify events are being sent to Google SecOps

  1. Wait for 5-10 minutes for events to be processed and ingested.
  2. Sign in to the Google SecOps console.
  3. Go to **Investigate > Enterprise Insights > Data Ingestion**.
  4. Search for **HID_DIGITALPERSONA** in the log type filter.
  5. Verify that events are being ingested with recent timestamps.



## Troubleshooting

### No events appearing in Google SecOps

  * Verify the Bindplane agent service is running:
        
        sc query observiq-otel-collector
        

  * Check the Bindplane agent logs for errors:
        
        type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
        

  * Verify the ingestion authentication credentials are correct in the `config.yaml` file.

  * Verify the customer ID is correct.

  * Verify network connectivity to the Google SecOps endpoint:
        
        ping malachiteingestion-pa.googleapis.com
        




### Events not being generated in Windows Event Log

  * Verify DigitalPersona services are running:

    1. Press `Win+R`, type `services.msc`, and press Enter.
    2. Verify the following services are running: 
       * DigitalPersona Authentication Service
       * DigitalPersona Server
  * Verify event logging is enabled in DigitalPersona Group Policy settings:

    1. Open **Group Policy Management Console**.
    2. Navigate to the DigitalPersona policy.
    3. Verify that **Level of detail in event logs** is set to **Details** or **Audit**.
  * Verify the Windows Event Log channels are enabled (see "Verify Windows Event Log channels are active" above).




### Bindplane agent service fails to start

  * Verify that the `config.yaml` file syntax is correct (use proper YAML indentation with spaces, not tabs).
  * Check for syntax errors in the configuration:
        
        "C:\Program Files\observIQ OpenTelemetry Collector\observiq-otel-collector.exe" --config "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml" validate
        

  * Review the Windows Event Log for service startup errors:

    1. Open **Event Viewer**.
    2. Navigate to **Windows Logs > Application**.
    3. Look for errors from source **observiq-otel-collector**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
device_application | about.application | Value copied directly  
AgentLocation | about.asset.location.name | Value copied directly  
dhostname, device_hostname | about.hostname | Value from device_hostname if not empty, else dhostname  
dip | about.ip | Value copied directly  
System.Version, System.Channel, System.Keywords, System.Opcode, System.ThreadID, EventData.Credential, EventData.DataName, EventData.CredentialMask, content_version_field_value, dhostname, dip, device_application, device_subapplication, device_event_count, bootstraphosts, usessl, acknowledgementmode, contenttype, topic, compression.type, esmversion, schemaregistryhosts, truststoreloc, truststorepass, usesslauth, keystoreloc, keystorepass, keypass, desc, AddrBasedSysZonePopEvents, AddrBasedSysZonePopRows, AddrBasedUsrZonePopEvents, AddrBasedUsrZonePopRows, AddrBasedZonePopEvents, AddrBasedZonePopRows, AddrBasedZonePopRowsIPv6, AgentId, AgentName, CategorizerCount, CategorizerCountConsole, CategorizerCountCustom, Comment, Current Drop Count, DeviceLocation, Estimated Cache Size, First Global event Processed, First Post-Aggregation Event Processed, First Post-Filtering Event Processed, Global events Processed, HostNameResolutionEnabled, Last Global event Processed, Last Post-Aggregation Event Processed, Last Post-Filtering Event Processed, LastModified, M1CacheDropped, M1CacheSize, ModifiedBy, NGCustomAdditionalDataMapper0, NGCustomAdditionalDataMapper1, NameResolverIPv6Control, Post-Aggregation Event rate LTC, Post-Aggregation Events Processed, Post-Aggregation Events Processed(SLC), Post-Aggregation Events/Sec, Post-Aggregation Events/Sec(SLC), Post-Filtering Event rate LTC, Post-Filtering Events Processed, Post-Filtering Events Processed(SLC), Post-Filtering Events/Sec, Post-Filtering Events/Sec(SLC), RawEventCount, RawEventLen, RawEventPreAggregatedCount, Resolver.hAdded, Resolver.hEvicted, Resolver.hQBlocked, Resolver.hQRejected, Resolver.hQSize, Resolver.hSize, Resolver.iAdded, Resolver.iEvicted, Resolver.iQBlocked, Resolver.iQRejected, Resolver.iQSize, Resolver.iSize, StatusCode, TC.dropcount, TC.size, ZFiltered, aup[acp].version, aup[system-zone-mappings].version, aup[user-categorizations].version, aup[user-zone-mappings].version, hbstatus, queuesize, sent, sent(SLC), status, throughput, throughput LTC, throughput(SLC), C, ET, HT, N, S, T | additional.fields | Merged with token objects where each token.value.string_value is set from the corresponding source field  
| extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED" if System.EventId == "2054"  
System.Task, Comment | metadata.description | Value from Comment if not empty, else System.Task  
| metadata.event_type | Set to "GENERIC_EVENT", then "USER_UNCATEGORIZED" if System.EventId in ["260","262"] and conditions met, "USER_DELETION" if System.EventId == "533" and conditions met, "STATUS_UPDATE" if System.EventId in ["776","780"], "USER_LOGIN" if System.EventId == "2054"  
System.EventId | metadata.product_event_type | Value copied directly  
System.EventRecordID | metadata.product_log_id | Value copied directly  
System.ProviderName | principal.application | Value copied directly  
EventData.InitiatorDomain | principal.domain.name | Value copied directly  
System.Computer | principal.hostname | Value copied directly  
System.ProcessID | principal.process.pid | Value copied directly  
EventData.InitiatorName | principal.user.userid | Value copied directly  
EventData.Error | security_result.description | Value copied directly  
| security_result.severity | Set to "INFORMATIONAL" if System.Level == "Information" or level =~ "INFO", "LOW" if System.Level == "Warning", else "UNKNOWN_SEVERITY"  
System.Level, level | security_result.severity_details | Value from level if not empty, else System.Level  
EventData.UserDomain | target.domain.name | Value copied directly  
EventData.UserName | target.user.user_display_name | Value copied directly  
System.UserId | target.user.userid | Value copied directly  
| metadata.vendor_name | Set to "HID"  
| metadata.product_name | Set to "DigitalPersona"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hid-digitalpersona-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
