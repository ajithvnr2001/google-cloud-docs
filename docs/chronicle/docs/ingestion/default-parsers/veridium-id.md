---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veridium-id/
title: Collect Veridium ID logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:26.725222+00:00
---

# Collect Veridium ID logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/veridium-id/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Veridium ID logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Veridium ID logs to Google Security Operations using the Bindplane agent.

Veridium ID is a biometric authentication platform that generates syslog messages for authentication events, account management, device registration, and administrative actions. The parser extracts fields from syslog messages using grok patterns and key-value parsing, and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Veridium ID host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Veridium ID



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
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/veridium_id:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VERIDIUM_ID
            raw_log_field: body
        
        service:
          pipelines:
            logs/veridium_id_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/veridium_id
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
      * Veridium ID uses TCP (`@@` in rsyslog), so `tcplog` receiver is required
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
          chronicle/veridium_id:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VERIDIUM_ID
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
             




## Configure syslog for Veridium ID

  1. Sign in to the **Veridium ID** host using SSH or CLI.
  2. Edit the `/etc/rsyslog.conf` or `/etc/rsyslog.d/events.conf` file:
         
         vi /etc/rsyslog.conf
         

  3. Add the following configuration, replacing `<bindplane-ip>` and `<bindplane-port>` with the actual Bindplane agent details:
         
         module(load="imfile" PollingInterval="10")
         
         input(type="imfile"
           File="/var/log/veridiumid/websecadmin/events.log"
           Tag="ver-adminevents"
           reopenOnTruncate="on")
         
         input(type="imfile"
           File="/var/log/veridiumid/tomcat/events.log"
           Tag="ver-events"
           reopenOnTruncate="on")
         
         if $programname == 'ver-events' then @@<bindplane-ip>:<bindplane-port>
         if $programname == 'ver-adminevents' then @@<bindplane-ip>:<bindplane-port>
         

**Note:** This should be configured on each webapp. The `@@` prefix indicates TCP transport.
  4. Save the file and exit.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_caller.accountId` | `principal.user.userid` | Directly mapped from the `_caller.accountId` field.  
`_caller.accountEmailAddressInfo` | `principal.user.email_addresses` | Directly mapped from the `_caller.accountEmailAddressInfo` field.  
`_caller.accountExternalId` | `principal.user.email_addresses` | Directly mapped from the `_caller.accountExternalId` field.  
`_caller.accountStatus` | `principal.user.attribute.labels[account_status].value` | Directly mapped from the `_caller.accountStatus` field.  
`_caller.deviceId` | `principal.asset.asset_id` | Prefixed with "VERIDIUM_ID:" and mapped from the `_caller.deviceId` field.  
`_caller.deviceDescription` | `principal.asset.attribute.labels[device_description].value` | Directly mapped from the `_caller.deviceDescription` field.  
`_caller.deviceManufacturer` | `principal.asset.attribute.labels[device_manufacturer].value` | Directly mapped from the `_caller.deviceManufacturer` field.  
`_caller.deviceName` | `principal.asset.attribute.labels[device_name].value` | Directly mapped from the `_caller.deviceName` field.  
`_caller.deviceOs` | `principal.asset.platform_software.platform` | Mapped from the `_caller.deviceOs` field. If the value is "iOS", it is mapped to "IOS". If the value is "Android", it is mapped to "ANDROID". If the value is "WIN" or "Windows", it is mapped to "WINDOWS".  
`_caller.deviceStatus` | `principal.asset.attribute.labels[device_status].value` | Directly mapped from the `_caller.deviceStatus` field.  
`_caller.deviceType` | `principal.asset.attribute.labels[device_type].value` | Directly mapped from the `_caller.deviceType` field.  
`actionDate` | `additional.fields[action_date].value.string_value` | Directly mapped from the `actionDate` field.  
`actionName` | `metadata.product_event_type` | Directly mapped from the `actionName` field.  
`accountEmail` | `principal.user.email_addresses` | Directly mapped from the `accountEmail` field.  
`accountExternalId` | `principal.user.email_addresses` | Directly mapped from the `accountExternalId` field.  
`accountId` | `principal.user.userid` | Directly mapped from the `accountId` field.  
`authenticatorDeviceContext.deviceMake` | `intermediary.asset.hardware.manufacturer` | Directly mapped from the `authenticatorDeviceContext.deviceMake` field.  
`authenticatorDeviceContext.ip` | `intermediary.ip` | Directly mapped from the `authenticatorDeviceContext.ip` field.  
`authenticatorDeviceContext.location.city` | `intermediary.asset.location.city` | Directly mapped from the `authenticatorDeviceContext.location.coordinates.latitude` field.  
`authenticatorDeviceContext.location.coordinates.latitude` | `intermediary.asset.location.region_latitude` | Directly mapped from the `authenticatorDeviceContext.location.coordinates.latitude` field.  
`authenticatorDeviceContext.location.coordinates.longitude` | `intermediary.asset.location.region_longitude` | Directly mapped from the `authenticatorDeviceContext.location.coordinates.longitude` field.  
`authenticatorDeviceContext.location.countryName` | `intermediary.asset.location.country_or_region` | Directly mapped from the `authenticatorDeviceContext.location.countryName` field.  
`authenticatorDeviceContext.location.ip` | `intermediary.ip` | Directly mapped from the `authenticatorDeviceContext.location.ip` field.  
`authenticationDeviceDescription` | `intermediary.asset.attribute.labels[authentication_device_description].value` | Directly mapped from the `authenticationDeviceDescription` field.  
`authenticationDeviceName` | `intermediary.asset.asset_id` | Prefixed with "VERIDIUM_ID:" and mapped from the `authenticationDeviceName` field.  
`authenticationDeviceOs` | `intermediary.asset.platform_software.platform` | Mapped from the `authenticationDeviceOs` field. If the value is "iOS", it is mapped to "IOS". If the value is "Android", it is mapped to "ANDROID". If the value is "WIN" or "Windows", it is mapped to "WINDOWS".  
`authenticationDeviceOsVersion` | `intermediary.asset.platform_software.platform_version` | Directly mapped from the `authenticationDeviceOsVersion` field.  
`authenticationDevicePhone` | `intermediary.asset.attribute.labels[authentication_device_phone].value` | Directly mapped from the `authenticationDevicePhone` field.  
`authenticationDevicePhoneModel` | `intermediary.asset.attribute.labels[authentication_device_phone_model].value` | Directly mapped from the `authenticationDevicePhoneModel` field.  
`authenticationDeviceRegistrationTime` | `intermediary.asset.attribute.labels[authentication_device_registeration_time].value` | Directly mapped from the `authenticationDeviceRegistrationTime` field.  
`authenticationDeviceType` | `intermediary.asset.attribute.labels[authentication_device_type].value` | Directly mapped from the `authenticationDeviceType` field.  
`authenticationResult` | `extensions.auth.auth_details` | Directly mapped from the `authenticationResult` field.  
`context.deviceMake` | `principal.asset.hardware.manufacturer` | Directly mapped from the `context.deviceMake` field.  
`context.ip` | `principal.ip` | Directly mapped from the `context.ip` field.  
`context.location.countryName` | `principal.location.country_or_region` | Directly mapped from the `context.location.countryName` field.  
`context.location.ip` | `principal.ip` | Directly mapped from the `context.location.ip` field.  
`context.osVersion` | `principal.asset.platform_software.platform_version` | Directly mapped from the `context.osVersion` field.  
`context.userAgentRaw` | `network.http.user_agent` | Directly mapped from the `context.userAgentRaw` field.  
`exploiterDeviceContext.deviceMake` | `src.asset.hardware.manufacturer` | Directly mapped from the `exploiterDeviceContext.deviceMake` field.  
`exploiterDeviceContext.ip` | `src.ip` | Directly mapped from the `exploiterDeviceContext.ip` field.  
`exploiterDeviceContext.location.city` | `src.asset.location.city` | Directly mapped from the `exploiterDeviceContext.location.city` field.  
`exploiterDeviceContext.location.coordinates.latitude` | `src.asset.location.region_latitude` | Directly mapped from the `exploiterDeviceContext.location.coordinates.latitude` field.  
`exploiterDeviceContext.location.coordinates.longitude` | `src.asset.location.region_longitude` | Directly mapped from the `exploiterDeviceContext.location.coordinates.longitude` field.  
`exploiterDeviceContext.location.countryName` | `src.asset.location.country_or_region` | Directly mapped from the `exploiterDeviceContext.location.countryName` field.  
`exploiterDeviceContext.location.ip` | `src.ip` | Directly mapped from the `exploiterDeviceContext.location.ip` field.  
`exploiterDeviceContext.osName` | `src.asset.platform_software.platform` | Mapped from the `exploiterDeviceContext.osName` field. If the value is "WIN" or "Windows", it is mapped to "WINDOWS". If the value is "iOS", it is mapped to "IOS". If the value is "Android", it is mapped to "ANDROID".  
`exploiterDeviceContext.osVersion` | `src.asset.platform_software.platform_version` | Directly mapped from the `exploiterDeviceContext.osVersion` field.  
`exploiterDeviceName` | `src.asset.attribute.labels[exploiter_device_name].value` | Directly mapped from the `exploiterDeviceName` field.  
`hostname` | `principal.hostname` | Directly mapped from the `hostname` field.  
`ipAddress` | `principal.ip` | Directly mapped from the `ipAddress` field.  
`location` | `principal.location.city` | Directly mapped from the `location` field.  
`location.city` | `about.location.city` | Directly mapped from the `location.city` field.  
`location.coordinates.latitude` | `about.location.region_latitude` | Directly mapped from the `location.coordinates.latitude` field.  
`location.coordinates.longitude` | `about.location.region_longitude` | Directly mapped from the `location.coordinates.longitude` field.  
`location.countryName` | `about.location.country_or_region` | Directly mapped from the `location.countryName` field.  
`location.ip` | `about.ip` | Directly mapped from the `location.ip` field.  
`metadata.collected_timestamp` | `metadata.collected_timestamp` | Directly mapped from the `collected_time` field.  
`metadata.event_timestamp` | `metadata.event_timestamp` | Directly mapped from the `event_time` field.  
`metadata.event_type` | `metadata.event_type` | Set to "USER_UNCATEGORIZED".  
`metadata.product_event_type` | `metadata.product_event_type` | Directly mapped from the `actionName` field.  
`metadata.product_name` | `metadata.product_name` | Set to "VERIDIUM_ID".  
`namespace` | `principal.namespace` | Directly mapped from the `namespace` field.  
`pid` | `principal.process.pid` | Directly mapped from the `pid` field.  
`request.context.userAgentRaw` | `network.http.user_agent` | Directly mapped from the `request.context.userAgentRaw` field.  
`request.sessionId` | `network.session_id` | Directly mapped from the `request.sessionId` field.  
`requestMethod` | `network.http.method` | Directly mapped from the `requestMethod` field.  
`requestURI` | `network.http.referral_url` | Directly mapped from the `requestURI` field.  
`security_result.severity` | `security_result.severity` | Mapped from the `severity` field. If the value is "INFO", it is mapped to "INFORMATIONAL".  
| `principal.application` | Directly mapped from the `application` field.  
| `principal.asset.hostname` | Directly mapped from the `hostname` field.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/veridium-id-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
