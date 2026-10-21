---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-waf/
title: Collect Akamai WAF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:15:41.298629+00:00
---

# Collect Akamai WAF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Akamai WAF logs

**Parser Version:** 32.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Akamai WAF logs to Google Security Operations using the Akamai CEF Connector and Bindplane. Akamai WAF is a cloud-based web application firewall that protects web applications and APIs against threats including SQL injection, cross-site scripting (XSS), and DDoS attacks. The Akamai CEF Connector pulls security events from the Akamai SIEM API in near real time and converts them from JSON to Common Event Format (CEF), which is then forwarded to Bindplane via syslog.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd for Bindplane agent installation.
  * A Linux server (CentOS, RHEL, or Ubuntu recommended) with at least 2 CPU cores, 6 GB RAM, and 2 GB free disk space for the Akamai CEF Connector.
  * Java 8 (JRE 1.8) or later installed on the CEF Connector host.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements, and that the proxy allowlists `*.cloudsecurity.akamaiapis.net` and `*.luna.akamaiapis.net`.
  * Privileged access to Akamai Control Center.
  * An Akamai security configuration with App & API Protector, Kona Site Defender, Web Application Protector, Bot Manager, or Account Protector enabled.



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
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Enable SIEM integration in Akamai Control Center

  1. Sign in to **Akamai Control Center**.
  2. Go to **WEB & DATA CENTER SECURITY** > **Security Configuration**.
  3. Open the security configuration and the appropriate version for which you want to collect SIEM data.
  4. Click **Advanced Settings** and expand **Data collection for SIEM Integrations**.
  5. Click **On** to enable SIEM.
  6. Choose the security policies for which you want to export data: 
     * **All Security policies** : Sends SIEM data for events that violate any security policy within the security configuration.
     * **Specific security policies** : Sends data for one or more specific security policies. Select the appropriate policies from the dropdown list.
  7. Copy the value in the **Web Security Configuration ID** field. Save this ID for later use.
  8. Click **Activate** to push your security configuration changes to the production network. Under **Network** , click **Production** , and then click **Activate**.

**Note:** If you want to enable SIEM integration for additional security configurations, repeat the preceding process for each configuration.



## Set up a user to manage SIEM in Akamai Control Center

  1. In **Akamai Control Center** , go to **ACCOUNT ADMIN** > **Identity & access**.
  2. On the **Users and API Clients** tab, find the user you want to assign the role to or click **Create user**.
  3. To assign the SIEM role to an existing user: 
     1. Open the user's account and click the **Edit roles** tab.
     2. Find the appropriate group, click the **Roles** dropdown, and select the **Manage SIEM** role.
     3. Click **Submit**.
  4. To assign the SIEM role to a new user:

     1. Click **Create user**.
     2. Enter basic information for the user and scroll down to the **Assign Roles** section.
     3. Find the appropriate group, click the **Roles** dropdown, and select the **Manage SIEM** role.
     4. Click **Save**.
**Note:** Only the Manage SIEM role has the proper permissions. Do not assign this user any other role.



## Provision SIEM API credentials in Akamai Control Center

  1. Visit the [Create authentication credentials](https://techdocs.akamai.com/developer/docs/set-up-authentication-credentials) page in Akamai documentation.
  2. Follow the steps to provision the SIEM API for the user you assigned to manage SIEM.
  3. Copy and save the following credentials securely:

     * **Access Token**
     * **Client Token**
     * **Client Secret**
     * **Base URL** (host)
**Note:** You will need these credentials to configure the Akamai CEF Connector.



## Install the Akamai CEF Connector

  1. On your Linux server, download the latest CEF Connector distribution package from the [Akamai SIEM Integration Connector Packages](https://github.com/akamai/siem-integration-connector-packages) GitHub repository.
  2. Transfer the package to your server if needed.
  3. Verify the SHA256 hash of the downloaded file to ensure integrity.
  4. Unzip the distribution package:
         
         unzip CEFConnector-<version>.zip
         

  5. Navigate to the extracted directory:
         
         cd CEFConnector-<version>
         

  6. Create a symbolic link to the startup script to install the service:
         
         sudo ln -s /path/to/CEFConnector-<version>/bin/AkamaiCEFConnector.sh /etc/init.d/AkamaiCEFConnector
         




## Configure the Akamai CEF Connector

  1. Navigate to the `config` directory within the CEF Connector installation:
         
         cd /path/to/CEFConnector-<version>/config
         

  2. Open the `CEFConnector.properties` file using a text editor:
         
         sudo nano CEFConnector.properties
         

  3. Configure the following required parameters:
         
         # Pull rate from Akamai source (in seconds, positive integer)
         connector.pull.interval=60
         
         # Security Configuration IDs (semicolon-separated for multiple)
         akamai.data.configs=<YOUR_SECURITY_CONFIG_ID>
         
         # API Credentials
         akamai.data.accesstoken=<YOUR_ACCESS_TOKEN>
         akamai.data.clienttoken=<YOUR_CLIENT_TOKEN>
         akamai.data.clientsecret=<YOUR_CLIENT_SECRET>
         akamai.data.baseurl=<YOUR_BASE_URL>
         
         # Offset-based mode (recommended for continuous collection)
         akamai.data.timebased=false
         
         # Maximum number of events per API call
         akamai.data.limit=200000
         
         # Proxy Configuration (leave blank if no proxy)
         # connector.proxy.host=
         # connector.proxy.port=
         

  4. Replace the following placeholders with your actual values:

     * `<YOUR_SECURITY_CONFIG_ID>`: The Web Security Configuration ID you copied in the Enable SIEM section. For multiple configurations, separate IDs with semicolons (for example, `12345;67890`).
     * `<YOUR_ACCESS_TOKEN>`: The access token from Akamai API credentials.
     * `<YOUR_CLIENT_TOKEN>`: The client token from Akamai API credentials.
     * `<YOUR_CLIENT_SECRET>`: The client secret from Akamai API credentials.
     * `<YOUR_BASE_URL>`: The base URL (host) from Akamai API credentials (for example, `akab-xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx.luna.akamaiapis.net`).
  5. Save and close the file.




## Configure CEF Connector logging to forward syslog to Bindplane

  1. Navigate to the `config` directory within the CEF Connector installation.
  2. Open the `log4j2.xml` file using a text editor:
         
         sudo nano /path/to/CEFConnector-<version>/config/log4j2.xml
         

  3. In the Properties section near the top of the file, set the remote syslog server parameters to point to the Bindplane agent:
         
         <!-- Syslog Appender Configuration -->
         <Syslog name="SyslogAppender" 
                 host="<BINDPLANE_IP_ADDRESS>" 
                 port="<BINDPLANE_PORT>" 
                 protocol="<PROTOCOL>" 
                 facility="LOCAL0"
                 format="RFC 5424">
             <PatternLayout pattern="%m%n"/>
         </Syslog>
         

  4. Replace the following placeholders:

     * `<BINDPLANE_IP_ADDRESS>`: The IP address of the server where the Bindplane agent is installed (for example, `192.168.1.100`).
     * `<BINDPLANE_PORT>`: The port number where the Bindplane agent listens (for example, `514` for UDP or `601` for TCP).
     * Set `CEFProtocol` to `UDP` or `TCP` to match your Bindplane receiver configuration.
  5. Save and close the file.




## Start the Akamai CEF Connector

  1. Start the CEF Connector service:
         
         sudo /etc/init.d/AkamaiCEFConnector start
         

  2. Verify the service is running:
         
         sudo /etc/init.d/AkamaiCEFConnector status
         

  3. Monitor the logs to ensure the connector is pulling events from Akamai and forwarding them:
         
         tail -f /path/to/CEFConnector-<version>/bin/logs/cefconnector.log
         




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

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in the Get ingestion authentication file section
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from the Get customer ID section
             customer_id: <PLACEHOLDER_CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'AKAMAI_WAF'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<PLACEHOLDER_CUSTOMER_ID>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in the Get ingestion authentication file section
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from the Get customer ID section
            customer_id: <PLACEHOLDER_CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'AKAMAI_WAF'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`src` (attackData.clientIP) | `principal.ip` | Source IP address of the client making the request  
`c6a2` (ipv6src) | `principal.ip` | Source IPv6 address if attackData.clientIP is in IPv6 format  
`dhost` (httpMessage.host) | `target.hostname` | Hostname from the HTTP HOST header  
`dpt` (httpMessage.port) | `target.port` | Port number used by the incoming request  
`requestMethod` (httpMessage.method) | `network.http.method` | HTTP method of the incoming request (GET, POST, etc.)  
`request` (requestURL) | `target.url` | Calculated full URL from httpMessage fields  
`cs1` (attackData.rules) | `security_result.rule_id` | Rule IDs of rules that triggered for this request  
`cs2` (attackData.ruleMessages) | `security_result.rule_name` | Messages of rules that triggered  
`act` (appliedAction) | `security_result.action` | Action taken (alert, deny, abort, etc.)  
`severity` | `security_result.severity` | Calculated severity (5 for detect, 10 for mitigate)  
`cs5` (attackData.clientReputation) | `security_result.threat_name` | Client IP scores for Client Reputation  
`cs6` (attackData.apiId) | `security_result.detection_fields` | API ID for API Protection  
`start` (httpMessage.start) | `metadata.event_timestamp` | Time when the Edge Server initiated the connection (epoch format)  
`devicePayloadId` (httpMessage.requestId) | `metadata.product_log_id` | Globally unique ID of the message  
`flexString1` (attackData.configId) | `security_result.detection_fields` | ID of the Security Configuration applied to this request  
`flexString2` (attackData.policyId) | `security_result.detection_fields` | ID of the Firewall Policy applied to this request  
`AkamaiSiemJA4` (identity.ja4) | `network.tls.client.ja3` | JA4 client TLS fingerprint  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-waf-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
