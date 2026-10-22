---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nyansa-events/
title: Collect Nyansa Voyance / VMware Edge Network Intelligence logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:47.279211+00:00
---

# Collect Nyansa Voyance / VMware Edge Network Intelligence logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nyansa-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Nyansa Voyance / VMware Edge Network Intelligence logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Nyansa Voyance (VMware Edge Network Intelligence) logs to Google Security Operations using Bindplane.

Nyansa Voyance, now known as VMware Edge Network Intelligence (ENI), is a network analytics and IoT security platform that provides visibility into client access, network services, IoT devices, and enterprise applications. The platform collects data from wireless controllers, switches, and network devices to analyze user experience, application performance, and device behavior across wired and wireless networks.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and your Nyansa Voyance / VMware Edge Network Intelligence instance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Access to the VMware SD-WAN Orchestrator portal with Enterprise Admin privileges
  * Nyansa Voyance GraphQL API v2 access token
  * Java 1.8 or above installed on a Linux or macOS system to run the Nyansa SIEM syslog agent
  * At least 2GB of free memory for the Java Virtual Machine (JVM)



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:6514"
        
        exporters:
          chronicle/nyansa_events:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: NYANSA_EVENTS
            raw_log_field: body
            ingestion_labels:
              env: production
              source: nyansa
        
        service:
          pipelines:
            logs/nyansa_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/nyansa_events
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: Set to `0.0.0.0:6514` to listen on all interfaces on port 6514 (or use a different port if needed)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Replace `YOUR_CUSTOMER_ID` with your Chronicle customer ID from step 3
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Set to `NYANSA_EVENTS`
    * `ingestion_labels`: Optional labels in YAML format (customize as needed)



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/nyansa_events:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: NYANSA_EVENTS
            raw_log_field: body
            ingestion_labels:
              env: production
              source: nyansa
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

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
         




## Configure Nyansa Voyance API access

To enable the Nyansa SIEM syslog agent to retrieve events from Voyance, you need to create an API token with appropriate permissions.

### Create API token in VMware SD-WAN Orchestrator

  1. Sign in to the **VMware SD-WAN Orchestrator** portal as an Enterprise Admin user.
  2. Go to **Administration > Administrators**.
  3. Locate your administrator account in the list.
  4. Click **Actions > Modify** for your administrator account.
  5. Navigate to the **Developer API** tab.
  6. Click **Generate New Token** or **Create API Token**.
  7. Copy and save the generated API token securely.

**Note:** The API token is displayed only once. If you lose it, you will need to generate a new token.

### Record API endpoint URL

  * Your Voyance GraphQL API v2 URL follows this format:

    * **Legacy Nyansa customers** : `https://yourcompany.nyansa.com/api/v2/graphql`
    * **VMware Edge Network Intelligence** : `https://your-eni-domain/api/v2/graphql`

Replace `yourcompany` or `your-eni-domain` with your actual organization domain.




## Install and configure Nyansa SIEM syslog agent

The Nyansa SIEM syslog agent is a Java application that polls the Voyance GraphQL API and forwards events to syslog. This agent acts as a bridge between the Voyance API and your Bindplane agent.

### Download the Nyansa SIEM syslog agent

  1. Download the latest release from the official GitHub repository:
         
         wget https://github.com/Nyansa/voyance-siem-syslog-agent/archive/refs/tags/v0.9.4.tar.gz
         

  2. Extract the archive:
         
         tar xf v0.9.4.tar.gz
         cd voyance-siem-syslog-agent-0.9.4
         

  3. Build the package using Maven:
         
         mvn clean package
         

  4. Extract the generated package:
         
         tar xf target/VoyanceSiemSyslogAgent-0.9.4-package.tar.gz
         cd VoyanceSiemSyslogAgent-0.9.4
         


**Note:** If you prefer not to build from source, you can download pre-built packages from the GitHub releases page.

### Configure the agent properties

  1. Edit the `config/config.properties` file:
         
         nano config/config.properties
         

  2. Configure the following required parameters:
         
         # Voyance GraphQL API v2 URL
         voyance.dev.api.url = https://yourcompany.nyansa.com/api/v2/graphql
         
         # Voyance GraphQL API v2 Access Token
         voyance.dev.api.token = YOUR_API_TOKEN_HERE
         
         # HTTP Proxy (optional, leave blank if not needed)
         http.proxy = 
         
         # API Data Fetches Enabled
         # Available options: iotOutlierList_all, iotDeviceStatsList_last3h, iotDeviceStatsList_last24h,
         # iotDeviceStatsList_last7d, iotDeviceStatsList_last14d, iotGroupStatsList_last3h,
         # iotGroupStatsList_last24h, iotGroupStatsList_last7d, iotGroupStatsList_last14d,
         # deviceList_updated, applicationList_last3h, applicationList_last24h, deviceEventList_all
         api.fetches.enabled = iotOutlierList_all,iotDeviceStatsList_last24h,deviceEventList_all
         

     * `voyance.dev.api.url`: Enter your Voyance GraphQL API v2 URL
     * `voyance.dev.api.token`: Enter the API token created in the previous step
     * `http.proxy`: Enter proxy hostname and port if required (for example, `proxy.company.com:3128`), otherwise leave blank
     * `api.fetches.enabled`: Comma-separated list of API fetch IDs to enable (customize based on your needs)
  3. Save the file.




### Configure syslog destination

  1. Edit the `config/log4j2.xml` file:
         
         nano config/log4j2.xml
         

  2. Locate the `<Properties>` section and configure the syslog settings:
         
         <Properties>
             <!-- SIEM Syslog Properties -->
             <Property name="SiemSyslogHost">BINDPLANE_AGENT_IP</Property>
             <Property name="SiemSyslogPort">6514</Property>
             <Property name="SiemSyslogProtocol">UDP</Property>
         </Properties>
         

     * `SiemSyslogHost`: Enter the IP address or hostname of the Bindplane agent host
     * `SiemSyslogPort`: Enter `6514` (or the port configured in your Bindplane agent)
     * `SiemSyslogProtocol`: Enter `UDP` or `TCP` (must match Bindplane receiver configuration)
  3. Save the file.




### Start the Nyansa SIEM syslog agent

  1. Start the agent using the provided script:
         
         ./VoyanceSiemSyslogAgent.sh start
         

  2. Verify the agent is running:
         
         ./VoyanceSiemSyslogAgent.sh status
         

  3. Monitor the agent logs for errors:
         
         tail -f logs/voyance-agent.log
         


**Note:** The agent automatically tracks API fetch progress and ensures only new data is sent between pulls. Progress is stored in a local database file `voyance-agent.mv.db`.

### Common agent commands

  * **Start the agent** :
        
        ./VoyanceSiemSyslogAgent.sh start
        

  * **Stop the agent** :
        
        ./VoyanceSiemSyslogAgent.sh stop
        

  * **Restart the agent** :
        
        ./VoyanceSiemSyslogAgent.sh restart
        

  * **Check agent status** :
        
        ./VoyanceSiemSyslogAgent.sh status
        

  * **Reset database and API fetch progress** :
        
        ./VoyanceSiemSyslogAgent.sh db_reset
        

  * **Validate configuration** :
        
        ./VoyanceSiemSyslogAgent.sh validate
        

  * **Show available API fetch IDs** :
        
        ./VoyanceSiemSyslogAgent.sh show_apis
        




## Verify log ingestion

  1. Wait a few minutes for the Nyansa SIEM syslog agent to poll the Voyance API and forward events to the Bindplane agent.
  2. Check the Bindplane agent logs to verify syslog messages are being received:

**Linux:**
         
         sudo journalctl -u observiq-otel-collector -f | grep -i nyansa
         

**Windows:**
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log" | findstr /i nyansa
         

  3. Sign in to the Google SecOps console.

  4. Go to **SIEM Settings > Feeds** and verify the feed status shows as **Active**.

  5. Search for Nyansa events in the Google SecOps search interface using the ingestion label `NYANSA_EVENTS`.




## Troubleshooting

### Nyansa SIEM syslog agent errors

  * **Missing API URL or token** : Verify `voyance.dev.api.url` and `voyance.dev.api.token` are correctly configured in `config/config.properties`.
  * **API authentication failures** : Verify the API token is valid and has not expired. Generate a new token if needed.
  * **Network connectivity issues** : Verify the agent can reach the Voyance API URL. Check firewall rules and proxy settings.
  * **Syslog connection failures** : Verify the Bindplane agent IP address and port are correct in `config/log4j2.xml`. Ensure the Bindplane agent is running and listening on the configured port.



### Bindplane agent errors

  * **Configuration syntax errors** : Validate YAML syntax in `config.yaml`. Ensure proper indentation (2 spaces, not tabs).
  * **Authentication failures** : Verify the ingestion authentication file path is correct and the file is readable.
  * **Network connectivity issues** : Verify the Bindplane agent can reach the Chronicle regional endpoint. Check firewall rules for outbound HTTPS (TCP 443) to the endpoint.
  * **No logs received** : Verify the Nyansa SIEM syslog agent is running and configured to send to the correct Bindplane agent IP and port.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
auth_method | extensions.auth.type | Type of authentication (e.g., USER, MACHINE)  
host | intermediary.hostname | Hostname of the intermediary device  
host | intermediary.ip | IP address of the intermediary device  
collected_timestamp | metadata.collected_timestamp | Timestamp when the event was collected  
timestamp | metadata.event_timestamp | Timestamp when the event occurred  
user_name | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
nas_ip | metadata.event_type |   
event_type | metadata.product_event_type | Product-specific event type  
session_id | network.session_id | Unique identifier for the network session  
service_name | principal.application | Application name associated with the principal  
nas_ip | principal.ip | IP address of the principal  
end_host_id | principal.mac | MAC address of the principal  
nas_port | principal.port | Port number of the principal  
user_name | principal.user.userid | User ID of the principal  
auth_method | security_result.detection_fields | Additional detection fields from security analysis  
auth_source | security_result.detection_fields |   
error_code | security_result.detection_fields |   
request_status | security_result.detection_fields |   
request_id | security_result.detection_fields |   
additional.label | security_result.detection_fields |   
additional.value | security_result.detection_fields |   
metadata.product_name | metadata.product_name | Product name  
metadata.vendor_name | metadata.vendor_name | Vendor name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nyansa-events-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
