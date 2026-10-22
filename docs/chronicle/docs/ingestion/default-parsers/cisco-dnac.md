---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-dnac/
title: Collect Cisco Catalyst Center (formerly DNA Center) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:17.871130+00:00
---

# Collect Cisco Catalyst Center (formerly DNA Center) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-dnac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Catalyst Center (formerly DNA Center) logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Catalyst Center (formerly known as DNA Center) logs to Google Security Operations using two different approaches. Choose the option that best fits your environment and requirements.

Cisco Catalyst Center is a centralized network management and automation platform for enterprise campus, branch, and IoT networks. It provides intent-based networking, policy management, device provisioning, assurance analytics, and AI-driven issue detection across wired and wireless infrastructure. Catalyst Center generates events related to network health, device status changes, security policy violations, and assurance issues.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Privileged access to the Cisco Catalyst Center management console.
  * For **Option 1** : Windows Server 2016 or later, or a Linux host with `systemd` for the Bindplane agent.
  * For **Option 2** : Network connectivity between Cisco Catalyst Center and the Google SecOps webhook endpoint.



## Option 1 - Syslog integration using the Bindplane agent

This option uses syslog forwarding from Cisco Catalyst Center to the Bindplane agent, which then forwards structured logs to Google SecOps.

### Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



#### Option 1: Create a service account for the Chronicle API (recommended)

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

#### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

### Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



### Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

#### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

#### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

#### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

### Configure the Bindplane agent to ingest syslog and send to Google SecOps

#### Locate the configuration file

  * Locate the configuration file on your operating system as follows:

    * **Linux:**
    
    sudo nano /opt/observiq-otel-collector/config.yaml
    

    * **Windows:**
    
    notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
    




#### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/cisco_catalyst_center:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: CISCO_DNAC
            raw_log_field: body
        
        service:
          pipelines:
            logs/cisco_catalyst_center_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cisco_catalyst_center
        




#### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces. Replace the port if needed (for example, `1514` for non-root Linux).
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `YOUR_CUSTOMER_ID`: Your Google SecOps customer ID.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



#### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cisco_catalyst_center:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_DNAC
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

#### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



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
         




### Configure syslog forwarding on Cisco Catalyst Center

  1. Sign in to the **Cisco Catalyst Center**.
  2. Go to **System > Settings > External Services > Destinations > Syslog**.
  3. Click the **Add** icon (**+**) to create a new syslog destination.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps-Bindplane`).
     * **Description** : Enter a brief description (for example, `Syslog forwarding to Google SecOps via Bindplane`).
     * **Hostname/IP Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514` (or the port configured in the Bindplane agent).
     * **Protocol** : Select **UDP** or **TCP** depending on your Bindplane configuration.
  5. Click **Save**.

**Note:** Verify that the syslog destination shows a green status indicator after saving. If it does not, check network connectivity between Cisco Catalyst Center and the Bindplane agent host.



## Option 2 - Webhook integration

This option uses Cisco Catalyst Center's native webhook capabilities to deliver structured JSON events directly to Google SecOps in real time.

### Create webhook feed in Google SecOps

#### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cisco Catalyst Center Webhook`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Cisco Catalyst Center** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter `\n` for newline-delimited events.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



#### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Note:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.



#### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. Save this URL for the next steps.
  4. Click **Done**.



### Create Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

#### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



#### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`).
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Chronicle API**.
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.



### Configure webhook destination in Cisco Catalyst Center

  1. Sign in to the **Cisco Catalyst Center**.
  2. Go to **System > Settings > External Services > Destinations > Webhook**.
  3. Click the **Add** icon (**+**) to create a new webhook destination.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps-Webhook`).
     * **Description** : Enter a brief description (for example, `Webhook to Google SecOps`).
     * **URL** : Paste the Google SecOps webhook endpoint URL.
     * **Method** : Select **POST**.
     * **Authentication** : Select **No Authentication**.
     * **Trust Certificate** : Select **Yes**.
     * **Headers** : Click **Add Header** and add the following headers: 
       * **Name** : `Content-Type`, **Value** : `application/json`
       * **Name** : `X-goog-api-key`, **Value** : Your Google Cloud API key
       * **Name** : `X-Webhook-Access-Key`, **Value** : Your Google SecOps feed secret key
  5. Click **Save**.



### Subscribe events to webhook notifications

  1. In Cisco Catalyst Center, go to **Platform > Developer Toolkit > Event Notifications**.
  2. In the **Notifications** tab, click **Create New Notification**.
  3. In **Step 1 (Select Site and Events)** , select the sites and events you want to monitor: 
     * **Network Events** : Device unreachable, interface down, configuration changes.
     * **Security Events** : Security policy violations, authentication failures.
     * **System Events** : Platform events, software updates, maintenance.
     * **Assurance Events** : Performance degradation, connectivity issues.
  4. Click **Next**.
  5. In **Step 2 (Select Channels)** , select **REST** as the notification channel.
  6. In the **Endpoint** dropdown, select the webhook destination created in the previous section (for example, `Google SecOps-Webhook`).
  7. Click **Next**.
  8. In **Step 3 (Summary)** , review the notification configuration.
  9. Enter a **Name** for the subscription (for example, `Google SecOps Events`).
  10. Click **Finish**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`category` | `security_result.severity_details` | The value of `category` from the raw log is mapped to the `security_result.severity_details` field.  
`ciscoDnaEventLink` | `target.url` | The value of `ciscoDnaEventLink` from the raw log is mapped to the `target.url` field.  
`date_time` | `metadata.event_timestamp` | Extracted from the raw log message using grok pattern and converted to timestamp format.  
`details.Assurance_Issue_Category` | `security_result.about.resource.attribute.labels[].value` | The value of `details.Assurance_Issue_Category` from the raw log is mapped with the key "Assurance_Issue_Category".  
`details.Assurance_Issue_Details` | `security_result.summary` | The value of `details.Assurance_Issue_Details` from the raw log is mapped to the `security_result.summary` field.  
`details.Assurance_Issue_Name` | `security_result.about.resource.attribute.labels[].value` | The value of `details.Assurance_Issue_Name` from the raw log is mapped with the key "Assurance_Issue_Name".  
`details.Assurance_Issue_Priority` | `security_result.about.resource.attribute.labels[].value` | The value of `details.Assurance_Issue_Priority` from the raw log is mapped with the key "Assurance_Issue_Priority".  
`details.Assurance_Issue_Status` | `security_result.about.resource.attribute.labels[].value` | The value of `details.Assurance_Issue_Status` from the raw log is mapped with the key "Assurance_Issue_Status".  
`details.Device` | `target.ip`, `target.hostname` | If the value is an IP address, it is mapped to `target.ip`, otherwise to `target.hostname`.  
`dnacIp` | `target.ip` | The value of `dnacIp` from the raw log is mapped to `target.ip` if it is a valid IP address.  
`domain` | `additional.fields[].value.string_value` | The value of `domain` from the raw log is added as a key-value pair to `additional.fields` with the key "domain".  
`eventId` | `metadata.product_event_type` | The value of `eventId` from the raw log is mapped to the `metadata.product_event_type` field.  
`instanceId` | `target.resource.product_object_id` | The value of `instanceId` from the raw log is mapped to the `target.resource.product_object_id` field.  
`name` | `target.resource.attribute.labels[].value` | The value of `name` from the raw log is mapped with the key "name".  
`namespace` | `target.namespace` | The value of `namespace` from the raw log is mapped to the `target.namespace` field.  
`network.deviceId` | `target.asset.asset_id` | The value of `network.deviceId` from the raw log is prefixed with "deviceId: " and mapped to `target.asset.asset_id`.  
`note` | `additional.fields[].value.string_value` | The value of `note` from the raw log is added as a key-value pair to `additional.fields` with the key "note".  
`severity` | `security_result.severity` | Used to determine the value of `security_result.severity`, `is_alert`, and `is_significant`.  
`source` | `target.resource.attribute.labels[].value` | The value of `source` from the raw log is mapped with the key "source".  
`src_ip` | `principal.ip` | Extracted from the raw log message using grok pattern and mapped to `principal.ip`.  
`subDomain` | `additional.fields[].value.string_value` | The value of `subDomain` from the raw log is added as a key-value pair to `additional.fields` with the key "subDomain".  
`tntId` | `target.resource.attribute.labels[].value` | The value of `tntId` from the raw log is mapped with the key "tntId".  
`type` | `target.resource.attribute.labels[].value` | The value of `type` from the raw log is mapped with the key "type".  
`userId` | `target.user.userid` | The value of `userId` from the raw log is mapped to the `target.user.userid` field.  
`version` | `metadata.product_version` | The value of `version` from the raw log is mapped to the `metadata.product_version` field.  
N/A | `metadata.event_type` | Set based on the presence and values of `has_principal`, `has_target`, and `userId` fields. Possible values: NETWORK_CONNECTION, USER_UNCATEGORIZED, STATUS_UPDATE, GENERIC_EVENT.  
N/A | `is_alert` | Set to true if severity is 0 or 1, false otherwise.  
N/A | `is_significant` | Set to true if severity is 0 or 1, false otherwise.  
`correlationId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`isSimulated` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`startTime` | `event.idm.read_only_udm.extensions.vulns.vulnerabilities.scan_start_time` | Mapped from changelog  
`details.wlcIp` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`details.detectingApName` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`details.detectingApLocation` | `event.idm.read_only_udm.observer.location.name` | Mapped from changelog  
`details.detectingApMacAddress` | `event.idm.read_only_udm.observer.mac` | Mapped from changelog  
`network.siteId` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`details` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`details.threatType` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`tenantId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-dnac-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
