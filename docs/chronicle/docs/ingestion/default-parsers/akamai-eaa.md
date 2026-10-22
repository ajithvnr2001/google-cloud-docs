---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-eaa/
title: Collect Akamai Enterprise Application Access logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:28:53.919096+00:00
---

# Collect Akamai Enterprise Application Access logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-eaa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Akamai Enterprise Application Access logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Akamai Enterprise Application Access (EAA) logs to Google Security Operations using Akamai Unified Log Streamer (ULS) and Bindplane. Akamai EAA is a zero-trust network access solution that provides secure, identity-aware access to enterprise applications without a traditional VPN. EAA produces operational data in the form of access logs, admin audit logs, connector health metrics, device inventory, and directory health information. The parser extracts fields from the JSON logs, performs data transformations such as string conversions and IP address extraction, and maps these fields to the UDM, handling various event types including `NETWORK_HTTP` and `USER_UNCATEGORIZED` based on the presence of specific fields.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows Server 2016 or later, or Linux host with `systemd` to run the Bindplane agent.
  * Linux host with Python 3.9 or later, or a containerized environment (Docker or Kubernetes) to run Unified Log Streamer.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Akamai EAA tenant with administrative access.
  * Akamai API credentials:

    * For access and admin audit feeds: EAA Legacy API Key and Secret (created in Enterprise Center).
    * For connector health, device inventory, and directory health feeds: Akamai OPEN API credentials (EdgeGrid authentication) with READ-WRITE access to the Enterprise Application Access API.
**Note:** Unified Log Streamer does not support Windows as a deployment platform. Supported platforms include Linux, macOS, Docker, and Kubernetes. The Bindplane agent can run on Windows or Linux.



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



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest logs and send to Google SecOps

  1. Open the Bindplane agent configuration file in a text editor:

**Linux:**
         
         sudo nano /opt/observiq-otel-collector/config.yaml
         

**Windows:**
         
         notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
         

  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:5140"
         
         exporters:
           chronicle/akamai_eaa:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: 'AKAMAI_EAA'
             raw_log_field: body
             ingestion_labels:
               source: akamai_eaa
         
         service:
           pipelines:
             logs/akamai_eaa:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/akamai_eaa
         




Replace the following:

  * `/path/to/ingestion-authentication-file.json`: The full path to the service account JSON key file (Option 1). 
    * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * `<CUSTOMER_ID>`: The Google SecOps customer ID.
  * `0.0.0.0:5140`: The IP address and port for Bindplane to listen on. Adjust as needed for your environment.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/akamai_eaa:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'AKAMAI_EAA'
            raw_log_field: body
            ingestion_labels:
              source: akamai_eaa
        


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
         




## Create Akamai API credentials

Akamai EAA uses two types of API credentials depending on the feed type. Create the credentials that correspond to the feeds you want to collect.

### Create EAA Legacy API credentials (for access and admin feeds)

  1. Sign in to [Akamai Control Center](https://control.akamai.com).
  2. Select **Enterprise Center** from the main navigation menu on the left.
  3. Go to **General Settings > Settings**.
  4. Select the **API Keys** tab.
  5. Click **Generate new API Key** in the top right corner.
  6. Enter a name and a description for the API key.
  7. On the confirmation screen, copy the **Key** and the **Secret**.

**Note:** Store these credentials securely. The Secret is shown only once during creation.



### Create Akamai OPEN API credentials (for connector health, device inventory, and directory health feeds)

  1. Sign in to [Akamai Control Center](https://control.akamai.com).
  2. Go to **Account Admin > Identity and access**.
  3. Select the **API Users** tab.
  4. Click **Create API Client**.
  5. In the **Select APIs** section, search for **Enterprise Application Access** and set the access level to **READ-WRITE**.
  6. Complete the remaining settings and click **Create API client**.
  7. Click **Download** to download the credentials in `.edgerc` format, or click **Copy** to copy them to an existing `.edgerc` file.

**Note:** The credentials include `client_secret`, `host`, `access_token`, and `client_token`. Store these values securely.



## Configure the `.edgerc` credentials file

  1. Create the `.edgerc` credentials file on the system where ULS will run:
         
         touch ~/.edgerc
         

  2. Open the file in a text editor:
         
         nano ~/.edgerc
         

  3. Add your Akamai API credentials in the following format:
         
         [default]
         ; EAA Legacy API credentials (for access and admin feeds)
         eaa_api_host = manage.akamai-access.com
         eaa_api_key = <EAA_API_KEY>
         eaa_api_secret = <EAA_API_SECRET>
         
         ; Akamai OPEN API credentials (for conhealth, devinv, dirhealth feeds)
         host = <OPEN_API_HOST>
         client_token = <CLIENT_TOKEN>
         client_secret = <CLIENT_SECRET>
         access_token = <ACCESS_TOKEN>
         

  4. Secure the credentials file:
         
         chmod 600 ~/.edgerc
         




Replace the following:

  * `<EAA_API_KEY>`: The EAA Legacy API Key (for example, `XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`).
  * `<EAA_API_SECRET>`: The EAA Legacy API Secret.
  * `<OPEN_API_HOST>`: Your Akamai OPEN API hostname (for example, `akaa-xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx.luna.akamaiapis.net`).
  * `<CLIENT_TOKEN>`: Your Akamai OPEN API client token (for example, `akab-xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx`).
  * `<CLIENT_SECRET>`: Your Akamai OPEN API client secret.
  * `<ACCESS_TOKEN>`: Your Akamai OPEN API access token (for example, `akab-xxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxx`).

**Note:** If you only need access and admin feeds, you can omit the OPEN API fields. If you only need connector health feeds, you can omit the EAA Legacy API fields.



## Install Akamai Unified Log Streamer

Unified Log Streamer (ULS) pulls logs from Akamai EAA via the Akamai APIs and streams them to the Bindplane agent using TCP. ULS is a Python application that requires Python 3.9 or later.

### Linux installation (Python)

  1. Clone the ULS repository:
         
         git clone https://github.com/akamai/uls.git
         cd uls
         

  2. Install ULS Python requirements:
         
         pip3 install -r bin/requirements.txt
         

  3. Install the EAA CLI dependency:
         
         git clone --depth 1 --single-branch https://github.com/akamai/cli-eaa.git ext/cli-eaa
         pip3 install -r ext/cli-eaa/requirements.txt
         

  4. Verify the installation:
         
         python3 bin/uls.py --help
         




### Docker installation

  1. Pull the official ULS Docker image:
         
         docker pull akamai/uls:latest
         




## Configure ULS to stream EAA logs to Bindplane

### Command-line execution (testing)

  * Run ULS with TCP output to stream logs to the Bindplane agent:
        
        python3 bin/uls.py --input eaa \
            --feed access \
            --output tcp \
            --host <BINDPLANE_HOST> \
            --port 5140 \
            --edgerc ~/.edgerc \
            --section default
        




Replace the following:

  * `<BINDPLANE_HOST>`: The IP address or hostname of the server running the Bindplane agent.
  * `5140`: The port configured in the Bindplane `tcplog` receiver.

  * To stream multiple feed types, run separate ULS instances:
        
        # Access logs
        python3 bin/uls.py --input eaa --feed access --output tcp --host <BINDPLANE_HOST> --port 5140 --edgerc ~/.edgerc --section default
        
        # Admin audit logs
        python3 bin/uls.py --input eaa --feed admin --output tcp --host <BINDPLANE_HOST> --port 5140 --edgerc ~/.edgerc --section default
        
        # Connector health
        python3 bin/uls.py --input eaa --feed conhealth --output tcp --host <BINDPLANE_HOST> --port 5140 --edgerc ~/.edgerc --section default
        




### Systemd service (production)

For production deployments, configure ULS as a systemd service.

  1. Create a ULS configuration file:
         
         sudo mkdir -p /etc/uls
         sudo nano /etc/uls/eaa-access-tcp.conf
         

  2. Add the following configuration:
         
         ULS_INPUT=eaa
         ULS_FEED=access
         ULS_OUTPUT=tcp
         ULS_HOST=<BINDPLANE_HOST>
         ULS_PORT=5140
         ULS_EDGERC=/root/.edgerc
         ULS_SECTION=default
         

  3. Create a systemd service file:
         
         sudo nano /etc/systemd/system/uls-eaa-access.service
         

  4. Add the following content:
         
         [Unit]
         Description=Unified Log Streamer - EAA Access Logs to Bindplane
         After=network.target
         
         [Service]
         Type=simple
         EnvironmentFile=/etc/uls/eaa-access-tcp.conf
         ExecStart=/usr/bin/python3 /opt/uls/bin/uls.py --input ${ULS_INPUT} --feed ${ULS_FEED} --output ${ULS_OUTPUT} --host ${ULS_HOST} --port ${ULS_PORT} --edgerc ${ULS_EDGERC} --section ${ULS_SECTION}
         Restart=always
         RestartSec=10
         User=root
         
         [Install]
         WantedBy=multi-user.target
         

**Note:** Adjust the path `/opt/uls/bin/uls.py` to match the location where you cloned the ULS repository.
  5. Enable and start the service:
         
         sudo systemctl daemon-reload
         sudo systemctl enable uls-eaa-access.service
         sudo systemctl start uls-eaa-access.service
         

  6. Verify the service is running:
         
         sudo systemctl status uls-eaa-access.service
         

  7. View logs:
         
         sudo journalctl -u uls-eaa-access.service -f
         




Repeat steps 1-7 for each additional feed type (admin, conhealth) by creating separate configuration and service files with different names (for example, `uls-eaa-admin.service`, `uls-eaa-conhealth.service`).

### Docker Compose deployment

  1. Create a `docker-compose.yml` file:
         
         version: '3.8'
         
         services:
           uls-eaa-access:
             image: akamai/uls:latest
             container_name: uls-eaa-access
             restart: unless-stopped
             environment:
               - ULS_INPUT=eaa
               - ULS_FEED=access
               - ULS_OUTPUT=tcp
               - ULS_HOST=<BINDPLANE_HOST>
               - ULS_PORT=5140
             volumes:
               - ~/.edgerc:/root/.edgerc:ro
         
           uls-eaa-admin:
             image: akamai/uls:latest
             container_name: uls-eaa-admin
             restart: unless-stopped
             environment:
               - ULS_INPUT=eaa
               - ULS_FEED=admin
               - ULS_OUTPUT=tcp
               - ULS_HOST=<BINDPLANE_HOST>
               - ULS_PORT=5140
             volumes:
               - ~/.edgerc:/root/.edgerc:ro
         
           uls-eaa-conhealth:
             image: akamai/uls:latest
             container_name: uls-eaa-conhealth
             restart: unless-stopped
             environment:
               - ULS_INPUT=eaa
               - ULS_FEED=conhealth
               - ULS_OUTPUT=tcp
               - ULS_HOST=<BINDPLANE_HOST>
               - ULS_PORT=5140
             volumes:
               - ~/.edgerc:/root/.edgerc:ro
         




Replace `<BINDPLANE_HOST>` with the IP address or hostname of the Bindplane agent server.

  1. Start the containers:
         
         docker compose up -d
         

  2. View logs:
         
         docker compose logs -f
         




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`app` | `target.application` | The value after the colon in the `app` field.  
`apphost` | `target.hostname` | Directly mapped.  
`browser` | `network.http.user_agent` | Directly mapped.  
`bytes_in` | `network.recieved_bytes` | Directly mapped.  
`bytes_out` | `network.sent_bytes` | Directly mapped.  
`cc` | `principal.location.country_or_region` | Directly mapped.  
`client_id` | `additional.fields.key`: "Client Id", `additional.fields.value.string_value`: `client_id` | Conditionally mapped if `client_id` is present.  
`clientip` | `principal.ip` | Directly mapped.  
`cloud_zone` | `principal.cloud.availability_zone` | Directly mapped.  
`connector_resp_time` | `security_result.detection_fields.key`: "Connector response time", `security_result.detection_fields.value`: `connector_resp_time` | Conditionally mapped if `connector_resp_time` is not empty or "-".  
`content_type` | `additional.fields.key`: "Content type", `additional.fields.value.string_value`: `content_type` | Conditionally mapped if `content_type` is present.  
`datetime` | `metadata.event_timestamp` | Parsed from the `datetime` field using the RFC 3339 format.  
`deny_reason` | `security_result.summary` | Directly mapped.  
`device_type` | `principal.platform`, `principal.platform_version` | Mapped to `WINDOWS`, `LINUX`, or `MAC` based on regex matching. The raw value is mapped to `principal.platform_version`.  
`di` | `metadata.ingestion_labels.key`: "di", `metadata.ingestion_labels.value`: `di` | Directly mapped as an ingestion label.  
`error_code` | `additional.fields.key`: "Error code", `additional.fields.value.string_value`: `error_code` | Conditionally mapped if `error_code` is present.  
`event` | `metadata.description` | Directly mapped.  
`geo_city` | `principal.location.city` | Directly mapped.  
`geo_country` | `principal.location.country_or_region` | Directly mapped.  
`geo_state` | `principal.location.state` | Directly mapped.  
`groups` | `principal.user.group_identifiers` | Directly mapped.  
`http_method` | `network.http.method` | Directly mapped.  
`http_ver` | `network.application_protocol`, `network.application_protocol_version` | Parsed using grok to extract protocol and version.  
`idpinfo` | `additional.fields.key`: "IDP Info", `additional.fields.value.string_value`: `idpinfo` | Conditionally mapped if `idpinfo` is present.  
`internal_host` | `additional.fields.key`: "Internal host", `additional.fields.value.string_value`: `internal_host` | Conditionally mapped if `internal_host` is present.  
`metadata.log_type` | `metadata.log_type` | Hardcoded to "AKAMAI_EAA".  
`metadata.product_name` | `metadata.product_name` | Hardcoded to "AKAMAI_EAA".  
`metadata.vendor_name` | `metadata.vendor_name` | Hardcoded to "AKAMAI_EAA".  
`metadata.event_type` | `metadata.event_type` | Determined by logic: `USER_UNCATEGORIZED` if `uid` is present, `NETWORK_HTTP` if both `principal.ip` and `target` are set, or `GENERIC_EVENT` otherwise.  
`origin_host` | `additional.fields.key`: "Origin host", `additional.fields.value.string_value`: `origin_host` | Conditionally mapped if `origin_host` is present.  
`origin_resp_time` | `security_result.detection_fields.key`: "Origin response time", `security_result.detection_fields.value`: `origin_resp_time` | Conditionally mapped if `origin_resp_time` is not empty or "-".  
`os` | `principal.platform` | Mapped to `WINDOWS`, `MAC`, or `LINUX` based on regex matching.  
`port` | `target.port` | The value after the colon in the `app` field.  
`ral` | `metadata.description` | Concatenated values of the `ral` array, separated by commas.  
`referer` | `network.http.referral_url` | Directly mapped.  
`resource` | `principal.resource.attribute.labels.key`: "Resource", `principal.resource.attribute.labels.value`: `resource` | Conditionally mapped if `resource` is present.  
`resource_type` | `principal.resource.attribute.labels.key`: "Resource Type", `principal.resource.attribute.labels.value`: `resource_type` | Conditionally mapped if `resource_type` is present.  
`rscd` | `metadata.ingestion_labels.key`: "rscd", `metadata.ingestion_labels.value`: `rscd` | Directly mapped as an ingestion label.  
`session_id` | `network.session_id` | Directly mapped.  
`session_info` | `additional.fields.key`: "Session info", `additional.fields.value.string_value`: `session_info` | Conditionally mapped if `session_info` is present.  
`state` | `principal.location.state` | Directly mapped.  
`status_code` | `network.http.response_code` | Directly mapped.  
`total_resp_time` | `security_result.detection_fields.key`: "Total response time", `security_result.detection_fields.value`: `total_resp_time` | Conditionally mapped if `total_resp_time` is not empty or "-".  
`ts` | `metadata.event_timestamp` | Parsed from the `ts` field as UNIX milliseconds or seconds if present, otherwise from the `datetime` field.  
`uid` | `principal.user.userid` | Directly mapped.  
`uip` | `principal.ip` | Directly mapped.  
`url_path` | `target.url` | Directly mapped.  
`user_agent` | `network.http.user_agent`, `network.http.parsed_user_agent` | Directly mapped and parsed into a structured `parsed_user_agent` field.  
`username` | `principal.user.email_addresses` or `principal.user.userid` | Mapped to `email_addresses` if it looks like an email, otherwise to `userid`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-eaa-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
