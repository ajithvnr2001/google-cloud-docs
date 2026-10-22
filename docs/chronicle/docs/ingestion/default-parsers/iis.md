---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iis/
title: Collect Microsoft IIS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:27.158950+00:00
---

# Collect Microsoft IIS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft IIS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Microsoft Internet Information Services (IIS) logs to Google Security Operations using the Bindplane agent.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows Server 2016 or later with IIS installed
  * Administrative access to the IIS server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements



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



## Configure IIS W3C Extended Logging

You must enable the correct W3C fields in IIS Manager so Google SecOps can parse your logs properly and detections work reliably.

### Open IIS Manager

  1. Click **Start**.
  2. Type `inetmgr` and press **Enter**.
  3. The **Internet Information Services (IIS) Manager** window opens.



**Alternative method:**

  1. Press **Windows Key + R**.
  2. Type `inetmgr` and press **Enter**.



### Navigate to Logging Configuration

  1. In the **Connections** pane (left side), expand your server name.
  2. To configure server-wide logging (recommended): 
     * Click the **server name** at the root level.
  3. To configure site-specific logging: 
     * Expand **Sites** > click the specific site (for example, **Default Web Site**).
  4. In the **Features View** (center pane), double-click **Logging**.



### Select W3C Extended Log Format

  1. On the **Logging** page, under **Log File** section: 
     * In the **Format** drop-down list, select **W3C**.
  2. Click **Select Fields** button.



### Configure W3C Logging Fields

**Important:** The Google SecOps IIS parser supports **8 field configurations**. You must enable **ALL fields** from **ONE** of the patterns. Enabling different fields or mixing patterns will cause parsing failures.

In the **W3C Logging Fields** dialog, select fields according to **ONE** of the following patterns:

#### Pattern 1: Full Site Context with Query String and Bytes

Enable these fields in this exact order:

  * **Date** (date)
  * **Time** (time)
  * **Service Name** (s-sitename)
  * **Server IP Address** (s-ip)
  * **Method** (cs-method)
  * **URI Stem** (cs-uri-stem)
  * **URI Query** (cs-uri-query)
  * **Server Port** (s-port)
  * **User Name** (cs-username)
  * **Client IP Address** (c-ip)
  * **User Agent** (cs(User-Agent))
  * **Referer** (cs(Referer))
  * **Protocol Status** (sc-status)
  * **Bytes Sent** (sc-bytes)
  * **Bytes Received** (cs-bytes)



**Use this pattern when:** Your downstream format includes site context + query string and you require sent/received bytes, and your pipeline expects the "username" and "referer" columns (even if values are `-`).

#### Pattern 2: Basic with Substatus, Win32 Status, and Performance (No Referer)

Enable these fields in this exact order:

  * **Date** (date)
  * **Time** (time)
  * **Server IP Address** (s-ip)
  * **Method** (cs-method)
  * **URI Stem** (cs-uri-stem)
  * **URI Query** (cs-uri-query)
  * **Server Port** (s-port)
  * **User Name** (cs-username)
  * **Client IP Address** (c-ip)
  * **User Agent** (cs(User-Agent))
  * **Protocol Status** (sc-status)
  * **Protocol Substatus** (sc-substatus)
  * **Win32 Status** (sc-win32-status)
  * **Time Taken** (time-taken)



**Use this pattern when:** Your pipeline does **not** include Referer, but you need detailed error codes and latency (`time-taken`).

#### Pattern 3: Basic with Substatus, Win32 Status, and Performance (with Referer)

Enable these fields in this exact order:

  * **Date** (date)
  * **Time** (time)
  * **Server IP Address** (s-ip)
  * **Method** (cs-method)
  * **URI Stem** (cs-uri-stem)
  * **URI Query** (cs-uri-query)
  * **Server Port** (s-port)
  * **User Name** (cs-username)
  * **Client IP Address** (c-ip)
  * **User Agent** (cs(User-Agent))
  * **Referer** (cs(Referer))
  * **Protocol Status** (sc-status)
  * **Protocol Substatus** (sc-substatus)
  * **Win32 Status** (sc-win32-status)
  * **Time Taken** (time-taken)



**Use this pattern when:** Same as Pattern 2, but your pipeline includes Referer as a dedicated column.

#### Pattern 4: TLS/Protocol-Version Aware with Referrer and Performance

Enable these fields in this exact order:

  * **Date** (date)
  * **Time** (time)
  * **Server IP Address** (s-ip)
  * **Method** (cs-method)
  * **URI Stem** (cs-uri-stem)
  * **URI Query** (cs-uri-query)
  * **Client Port** (c-port)
  * **User Name** (cs-username)
  * **Client IP Address** (c-ip)
  * **Protocol Version** (cs-version)
  * **User Agent** (cs(User-Agent))
  * **Referer** (cs(Referer))
  * **Protocol Status** (sc-status)
  * **Protocol Substatus** (sc-substatus)
  * **Win32 Status** (sc-win32-status)
  * **Time Taken** (time-taken)



**Use this pattern when:** Your downstream format explicitly logs `cs-version` (e.g., `HTTP/1.1`) and includes timing, and you also have client port as a dedicated column.

#### Pattern 5: TLS/Protocol-Version Aware with Referrer (No Performance)

Enable these fields in this exact order:

  * **Date** (date)
  * **Time** (time)
  * **Server IP Address** (s-ip)
  * **Method** (cs-method)
  * **URI Stem** (cs-uri-stem)
  * **URI Query** (cs-uri-query)
  * **Client Port** (c-port)
  * **User Name** (cs-username)
  * **Client IP Address** (c-ip)
  * **Protocol Version** (cs-version)
  * **User Agent** (cs(User-Agent))
  * **Referer** (cs(Referer))
  * **Protocol Status** (sc-status)
  * **Protocol Substatus** (sc-substatus)
  * **Win32 Status** (sc-win32-status)



**Use this pattern when:** Same as Pattern 4, but your pipeline does not include `time-taken`.

#### Pattern 6: With Cookie and Referer (No Performance, No Bytes)

Enable these fields in this exact order:

  * **Date** (date)
  * **Time** (time)
  * **Server IP Address** (s-ip)
  * **Method** (cs-method)
  * **URI Stem** (cs-uri-stem)
  * **URI Query** (cs-uri-query)
  * **Client Port** (c-port)
  * **User Name** (cs-username)
  * **Client IP Address** (c-ip)
  * **User Agent** (cs(User-Agent))
  * **Cookie** (cs(Cookie))
  * **Referer** (cs(Referer))
  * **Protocol Status** (sc-status)
  * **Protocol Substatus** (sc-substatus)
  * **Win32 Status** (sc-win32-status)



**Use this pattern when:** Your downstream format expects both Cookie and Referer as dedicated columns.

#### Pattern 7: Minimal with Referer (No Cookie, No Performance, No Bytes)

Enable these fields in this exact order:

  * **Date** (date)
  * **Time** (time)
  * **Server IP Address** (s-ip)
  * **Method** (cs-method)
  * **URI Stem** (cs-uri-stem)
  * **URI Query** (cs-uri-query)
  * **Client Port** (c-port)
  * **User Name** (cs-username)
  * **Client IP Address** (c-ip)
  * **User Agent** (cs(User-Agent))
  * **Referer** (cs(Referer))
  * **Protocol Status** (sc-status)
  * **Protocol Substatus** (sc-substatus)
  * **Win32 Status** (sc-win32-status)



**Use this pattern when:** Your downstream format includes Referer but does not include Cookie/time/bytes.

#### Pattern 8: Minimal without Referer (No Cookie, No Performance, No Bytes)

Enable these fields in this exact order:

  * **Date** (date)
  * **Time** (time)
  * **Server IP Address** (s-ip)
  * **Method** (cs-method)
  * **URI Stem** (cs-uri-stem)
  * **URI Query** (cs-uri-query)
  * **Client Port** (c-port)
  * **User Name** (cs-username)
  * **Client IP Address** (c-ip)
  * **User Agent** (cs(User-Agent))
  * **Protocol Status** (sc-status)
  * **Protocol Substatus** (sc-substatus)
  * **Win32 Status** (sc-win32-status)



**Use this pattern when:** Your downstream format does not include Referer and you only need core request context plus status codes.

**Do NOT enable fields from multiple patterns.** The parser expects one of these exact configurations.

### Apply configuration

  1. Click **OK** to close the **W3C Logging Fields** dialog.
  2. Verify the **Directory** path where logs will be written. 
     * Default: `%SystemDrive%\inetpub\logs\LogFiles`
  3. Under **Log File Rollover** , select **Daily** (recommended for Google SecOps ingestion).
  4. Click **Apply** in the **Actions** pane (right side).



## Verify IIS Logging

After configuring the W3C fields, verify that IIS is writing logs correctly:

  1. Generate test traffic to your IIS site by opening a web page in a browser.
  2. Navigate to the log directory: `C:\inetpub\logs\LogFiles\W3SVC1\`
     * Note: `W3SVC1` corresponds to the first site (Default Web Site). For other sites, the folder name will be `W3SVC2`, `W3SVC3`, etc.
  3. Open the most recent log file (for example, `u_ex251217.log`) in Notepad.
  4. Verify the `#Fields:` line contains all the fields you enabled in the exact order from your chosen pattern.



### Example for Pattern 3

  * If you configured **Pattern 3** (Basic with Substatus, Win32 Status, and Performance with Referer), the `#Fields:` line should be:
        
        #Fields: date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken
        

  * Example log entry:
        
        2025-12-17 14:23:15 192.168.1.10 GET /index.html - 80 - 203.0.113.45 Mozilla/5.0+(Windows+NT+10.0) https://example.com/previous.html 200 0 0 125
        




**Important notes:**

  * Empty fields are represented by a hyphen (`-`).
  * Field order must match the `#Fields:` header exactly.
  * The parser will fail if fields are missing, reordered, or from multiple patterns.



## Install the Bindplane agent

Install the Bindplane agent on your Windows server according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Additional installation resources

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest IIS logs and send to Google SecOps

### Edit the configuration file

  1. Locate the `config.yaml` file. 
     * Default path: `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`
  2. Open the file using a text editor (for example, Notepad, VS Code, or Notepad++) as Administrator.
  3. Replace the entire contents with the following configuration:
         
         receivers:
           iis:
             collection_interval: 60s
         
         processors:
           resourcedetection:
             detectors: ["system"]
             system:
               hostname_sources: ["os"]
           normalizesums:
           batch:
         
         exporters:
           chronicle/iis:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             endpoint: chronicle.googleapis.com
             creds: 'C:\SecOps\ingestion-auth.json'
             log_type: 'IIS'
             override_log_type: false
             raw_log_field: body
             customer_id: '<CUSTOMER_ID>'
         
         service:
           pipelines:
             logs/iis:
               receivers:
                 - iis
               processors:
                 - resourcedetection
                 - normalizesums
                 - batch
               exporters:
                 - chronicle/iis
         




### Update Configuration Values

Replace the following placeholders:

  * `creds:` \- Path to your service account JSON key file (Option 1) (for example, `C:\SecOps\ingestion-auth.json`).
  * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
  * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * `endpoint`: Keep set to `chronicle.googleapis.com`.
  * `customer_id:` \- Your actual Google SecOps customer ID from the Get Google SecOps customer ID section.

**Note:** For the complete list of regional endpoints, see [Regional Endpoints documentation](https://cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint).

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/iis:
            compression: gzip
            endpoint: malachiteingestion-pa.googleapis.com
            creds: 'C:\SecOps\ingestion-auth.json'
            log_type: 'IIS'
            override_log_type: false
            raw_log_field: body
            customer_id: '<CUSTOMER_ID>'
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop observiq-otel-collector && net start observiq-otel-collector
        




## UDM mapping table

Log field | UDM mapping  
---|---  
`@timestamp` | `metadata.event_timestamp`  
`__AntiXsrfToken` | `additional.fields`  
`__type` | `additional.fields`  
`_raw` | `security_result.description`  
`_ResourceId` | `target.resource.product_object_id`  
`_time` | `metadata.event_timestamp`  
`_timestamp` | `metadata.event_timestamp`  
`_version` | `metadata.product_version`  
`AccountName` | `additional.fields`  
`AccountType` | `principal.user.attribute.roles.name`  
`Action` | `security_result.action_details`  
`addr` | `additional.fields`  
`admin_domain` | `principal.administrative_domain`  
`agent.ephemeral_id` | `additional.fields`  
`agent.hostname` | `observer.hostname`  
`agent.name` | `observer.hostname`  
`agent.type` | `observer.application`,  
`observer.asset.asset_id`  
`agent.version` | `additional.fields`  
`AgentDevice` | `additional.fields`  
`AgentLogFile` | `additional.fields`  
`AgentLogFormat` | `additional.fields`  
`AgentLogProtocol` | `additional.fields`  
`apparmor` | `security_result.action`  
`ASP.NET_SessionId` | `network.session_id`  
`auid` | `additional.fields`  
`AUID` | `additional.fields`  
`AuthenticationPackageName` | `additional.fields`  
`AzureDeploymentID` | `additional.fields`  
`beanFactory.0` | `additional.fields`  
`beanFactory.1.shareableResources.0` | `additional.fields`  
`BU` | `additional.fields`  
`c-ip` | `observer.ip`,  
`intermediary.ip`  
`c_ip` | `observer.ip`,  
`intermediary.ip`  
`CalloutKey` | `security_result.about.resource.attribute.labels`  
`CalloutName` | `security_result.about.resource.attribute.labels`  
`capability` | `security_result.detection_fields`  
`capname` | `security_result.detection_fields`  
`Category` | `security_result.category_details`  
`change_type` | `additional.fields`  
`ChangeType` | `security_result.about.resource.attribute.labels`  
`Channel` | `security_result.about.resource.attribute.labels`  
`ChannelID` | `security_result.about.resource.attribute.labels`  
`chronicle_tag` | `additional.fields`  
`class` | `security_result.detection_fields`  
`cloud_ray_id` | `additional.fields`  
`comm` | `principal.application`  
`Computer` | `target.hostname`,  
`target.asset.hostname`  
`computername` | `target.hostname`,  
`target.asset.hostname`  
`Conditions` | `security_result.about.resource.attribute.labels`  
`ConfigPath` | `additional.fields`  
`Configuration` | `additional.fields`  
`Connection_IP` | `target.ip`,  
`target.asset.ip`  
`content_type` | `additional.fields`  
`cookie` | `additional.fields`  
`count` | `additional.fields`  
`cribl_breaker` | `additional.fields`  
`cribl_host` | `observer.hostname`  
`cribl_pipe` (array element) | `additional.fields`  
`cs`(`Referer`) | `network.http.referral_url`  
`cs`(`User-Agent`) | `network.http.user_agent`,  
`network.http.parsed_user_agent`  
`cs-bytes` | `network.received_bytes`  
`cs-host` | `additional.fields`  
`cs-method` | `network.http.method`  
`cs-uri-query` | `target.url`  
`cs-uri-stem` | `target.url`  
`cs-uri-stem` | `target.url`  
`cs-username` (domain part) | `principal.administrative_domain`  
`cs-username` (user part) | `principal.user.userid`  
`cs-version` | `network.application_protocol_version`  
`cs_bytes` | `network.received_bytes`  
`cs_host` | `additional.fields`  
`cs_method` | `network.http.method`  
`cs_referer` | `network.http.referral_url`  
`cs_username` | `principal.user.userid`  
`csbyte` | `network.received_bytes`  
`csBytes` | `network.received_bytes`  
`cshost` | `additional.fields`  
`csip` | `principal.ip`,  
`principal.asset.ip`  
`csMethod` | `network.http.method`  
`csmethod` | `network.http.method`  
`csReferer` | `network.http.referral_url`  
`csreferer` | `network.http.referral_url`  
`csUriStem` | `target.url`  
`csUser-Agent` | `network.http.user_agent`,  
`network.http.parsed_user_agent`  
`csUserAgent` | `network.http.user_agent`,  
`network.http.parsed_user_agent`  
`csuseragent` | `network.http.user_agent`,  
`network.http.parsed_user_agent`  
`csusername` | `principal.user.userid`  
`csversion` | `network.application_protocol_version`  
`date` | `metadata.event_timestamp`  
`DC` | `additional.fields`  
`desc` | `metadata.description`  
`description` | `security_result.description`  
`Domain` | `principal.administrative_domain`  
`dst_ip` | `target.ip`,  
`target.asset.ip`  
`dst_ip2` | `target.ip`,  
`target.asset.ip`  
`dst_port` | `target.port`  
`duration` | `network.session_duration`,  
`additional.fields`  
`duration` | `network.session_duration.nanos` (if [`duration`] < 1000)  
`duration` | `network.session_duration.seconds` (if [`duration`] > 1000)  
`ecs.version` | `additional.fields`  
`EnabledFieldsFlags` | `additional.fields`  
`error_message` | `security_result.description`  
`event.dataset` | `additional.fields`  
`event.module` | `additional.fields`  
`event_data.dataset` | `additional.fields`  
`event_data.module` | `additional.fields`  
`EventEnqueuedUtcTime` | `additional.fields`  
`EventID` | `metadata.product_log_id`  
`EventProcessedUtcTime` | `additional.fields`  
`EventReceivedTime` | `metadata.collected_timestamp`  
`EventRecordID` | `principal.asset.product_object_id`  
`EventTime` | `metadata.event_timestamp`  
`EventType` | `metadata.product_event_type`  
`exe` | `principal.file.full_path`  
`ExecutionProcessID` | `principal.process.pid`  
`ExecutionThreadID` | `principal.process.product_specific_process_id`  
`facility` | `additional.fields`  
`FileOffset` | `additional.fields`  
`fileset.name` | `additional.fields`  
`FileUri` | `observer.file.full_path`  
`filter_action` | `security_result.action`  
`filter_type` | `additional.fields`  
`FilterId` | `security_result.about.resource.attribute.labels`  
`FilterKey` | `security_result.about.resource.attribute.labels`  
`FilterName` | `security_result.about.resource.attribute.labels`  
`FilterType` | `security_result.about.resource.attribute.labels`  
`first_seen` | `additional.fields`  
`Flags` | `additional.fields`  
`For login events` | `extensions.auth.type` (= "MACHINE")  
`ftp_command` | `network.ftp.command`  
`host` | `target.hostname`,  
`target.asset.hostname`  
`host.architecture` | `target.asset.hardware.cpu_platform`  
`host.geo.name` | `additional.fields`  
`host.id` | `target.asset.asset_id`  
`host.ip` | `target.ip`,  
`target.asset.ip`  
`host.mac` | `target.mac`,  
`target.asset.mac`  
`host.os.build` | `target.platform_patch_level`  
`host.os.family` | `additional.fields`  
`host.os.kernel` | `additional.fields`  
`host.os.name` | `target.platform_version`  
`host.os.platform` | `target.platform`  
`host.os.type` | `additional.fields`  
`host.os.version` | `target.platform_version`  
`host_hostname` | `target.hostname`,  
`target.asset.hostname`  
`host_name` | `target.hostname`,  
`target.asset.hostname`  
`Hostname` | `target.hostname`,  
`target.asset.hostname`  
`hostname` | `target.hostname`,  
`target.asset.hostname`  
`HTTP` | `network.application_protocol`  
`http_method` | `network.http.method`  
`http_response` | `network.http.response_code`  
`http_status_code` | `network.http.response_code`  
`HTTPS` | `network.application_protocol`  
`IIS_source` | `principal.resource.attribute.labels`  
`ImpersonationLevel` | `additional.fields`  
`input.type` | `additional.fields`  
`instance` | `additional.fields`  
`Internet Information Server` | `metadata.product_name`  
`IpAddress` | `principal.ip`,  
`principal.asset.ip`,  
`observer.ip`  
`IpPort` | `principal.port`  
`jndi_java_class` | `additional.fields`  
`jndi_payload` | `additional.fields`  
`jndiName` | `additional.fields`  
`KeyLength` | `additional.fields`  
`Keywords` | `additional.fields`  
`last_seen` | `additional.fields`  
`LayerId` | `security_result.about.resource.attribute.labels`  
`LayerKey` | `security_result.about.resource.attribute.labels`  
`LayerName` | `security_result.about.resource.attribute.labels`  
`Level` | `security_result.severity` (INFORMATIONAL, ERROR, MEDIUM, LOW)  
`LevelValue` | `security_result.about.resource.attribute.labels`  
`LmPackageName` | `additional.fields`  
`log.file.path` | `observer.file.full_path`  
`log.offset` | `metadata.product_log_id`  
`loginTimeout` | `additional.fields`  
`LogonGuid` | `security_result.about.resource.attribute.labels`  
`LogonProcessName` | `additional.fields`  
`LogonType` | `extensions.auth.auth_details`  
`logstash.collect.host` | `observer.hostname`  
`logstash.collect.timestamp` | `metadata.collected_timestamp`  
`logstash.ingest.timestamp` | `additional.fields`  
`logstash.irm_environment` | `additional.fields`  
`logstash.irm_region` | `additional.fields`  
`logstash.irm_site` | `additional.fields`  
`logstash.process.host` | `intermediary.hostname`  
`logstash.process.timestamp` | `additional.fields`  
`ManagementGroupName` | `additional.fields`  
`message_data` | `security_result.description`  
`MethodName` | `additional.fields`  
`MG` | `additional.fields`  
`Microsoft` | `metadata.vendor_name`  
`ministry` | `additional.fields`  
`misc` | `security_result.summary`  
`msg` | `security_result.description`  
`network_direction` | `network.direction` (OUTBOUND or INBOUND)  
`NewValue` | `additional.fields`  
`node` | `principal.hostname`,  
`principal.asset.hostname`  
`ObjectInstance.__type` | `additional.fields`  
`ObjectInstance.StartInfo.__type` | `additional.fields`  
`ObjectInstance.StartInfo.Arguments` | `additional.fields`  
`ObjectInstance.StartInfo.FileName` | `additional.fields`  
`obs_app` | `observer.application`  
`obs_host` | `observer.ip`  
`obs_pid` | `observer.process.pid`  
`OldValue` | `additional.fields`  
`Opcode` | `additional.fields`  
`OpcodeValue` | `additional.fields`  
`operation` | `security_result.detection_fields`  
`OS_Platform` | `additional.fields`  
`OS_Release` | `additional.fields`  
`OS_Timezone` | `additional.fields`  
`OS_type` | `target.platform`  
`OS_Version_ID` | `additional.fields`  
`OutlookSession` | `additional.fields`  
`PartitionId` | `additional.fields`  
`PhysicalPath` | `target.file.full_path`  
`pid` | `principal.process.pid`  
`PluginVersion` | `additional.fields`  
`prin_ip` | `observer.ip`  
`prin_ip` | `principal.ip`,  
`principal.asset.ip`  
`principal_ip` (conditionally) | `intermediary.ip`  
`principal_ip` (conditionally) | `observer.ip`  
`principal_or_intermediary_ip` | `intermediary.ip`  
`priority` | `additional.fields`  
`process_file` | `target.process.file.full_path`  
`process_id` | `additional.fields`  
`ProcessID` | `principal.process.pid`  
`ProcessName` | `principal.process.file.full_path`  
`profile` | `security_result.detection_fields`  
`propertyPath` | `additional.fields`  
`ProviderGuid` | `security_result.about.resource.attribute.labels`  
`ProviderKey` | `security_result.about.resource.attribute.labels`  
`ProviderName` | `security_result.about.resource.attribute.labels`  
`RecordNumber` | `additional.fields`  
`request_url` | `target.url`  
`res` | `security_result.action`  
`res` | `security_result.action` (ALLOW if "success")  
`response_content` | `additional.fields`  
`Role` | `additional.fields`  
`RoleInstance` | `additional.fields`  
`s-computername` | `target.hostname`,  
`target.asset.hostname`  
`s-ip` | `target.ip`,  
`target.asset.ip`  
`s-port` | `target.port`  
`s-sitename` | `target.application`  
`s_sitename` | `target.application`  
`sComputerName` | `target.hostname`,  
`target.asset.hostname`  
`scope_id` | `additional.fields`  
`sc-bytes` | `network.sent_bytes`  
`sc-status` | `network.http.response_code`  
`sc-substatus` | `additional.fields`  
`sc-win32-status` | `additional.fields`  
`sc_bytes` | `network.sent_bytes`  
`sc_substatus` | `additional.fields`  
`sc_win32_status` | `additional.fields`  
`scbyte` | `network.sent_bytes`  
`scBytes` | `network.sent_bytes`  
`scStatus` | `network.http.response_code`  
`scstatus` | `network.http.response_code`  
`sec_desc` | `security_result.description`  
`service.type` | `additional.fields`  
`ses` | `network.session_id`  
`Severity` | `security_result.severity` (INFORMATIONAL, ERROR, MEDIUM, LOW)  
`severity` | `security_result.severity` (INFORMATIONAL, ERROR, MEDIUM, LOW)  
`SeverityValue` | `security_result.about.resource.attribute.labels`  
`site` | `additional.fields`  
`sitename` | `target.application`  
`source` | `observer.file.full_path`  
`SourceModuleName` | `observer.resource.name`  
`SourceModuleType` | `observer.application`  
`SourceName` | `additional.fields`  
`SourceSystem` | `observer.application`  
`src_host` (if `Hostname`) | `principal.hostname`,  
`principal.asset.hostname`  
`src_ip` | `observer.ip`,  
`intermediary.ip`  
`src_port` | `principal.port`  
`sSiteName` | `target.application`  
`StorageAccount` | `additional.fields`  
`streamid` | `additional.fields`  
`SubFleetName` | `additional.fields`  
`subj` | `principal.resource.attribute.labels`  
`SubjectDomainName` | `principal.administrative_domain`  
`SubjectLogonId` | `principal.resource.attribute.labels`  
`SubjectUserName` | `principal.user.userid`  
`SubjectUserSid` | `principal.user.windows_sid`  
`syslog_facility` | `security_result.detection_fields`  
`syslog_facility_code` | `security_result.detection_fields`  
`syslog_pri` | `security_result.priority_details`  
`syslog_severity` | `security_result.severity_details`  
`syslog_severity_code` | `security_result.detection_fields`  
`SyslogFacility` | `security_result.about.resource.attribute.labels`  
`SyslogFacilityValue` | `security_result.about.resource.attribute.labels`  
`SyslogSeverity` | `security_result.about.resource.attribute.labels`  
`SyslogSeverityValue` | `security_result.about.resource.attribute.labels`  
`system` | `target.platform`  
`tags` (array elements) | `additional.fields`  
`target_host` | `target.hostname`,  
`target.asset.hostname`  
`targetBeanName` | `additional.fields`  
`TargetDomainName` | `target.administrative_domain`  
`TargetLogonId` | `target.resource.attribute.labels`  
`TargetUserName` | `target.user.userid`  
`TargetUserSid` | `target.user.windows_sid`  
`task` | `additional.fields`  
`TaskValue` | `additional.fields`  
`TenantId` | `additional.fields`  
`ThreadID` | `additional.fields`  
`time` | `metadata.event_timestamp`  
`time-taken` | `additional.fields`  
`time-taken` | `network.session_duration`  
`time_taken` | `additional.fields`  
`time_taken` | `network.session_duration`  
`TimeGenerated` | `security_result.about.resource.attribute.labels`  
`timestamp` | `metadata.event_timestamp`  
`total_CPU` | `target_hardware.cpu_number_cores`  
`total_memory` | `additional.fields`  
`transletBytecodes.0` | `additional.fields`  
`transletName` | `additional.fields`  
`TransmittedServices` | `additional.fields`  
`Type` | `additional.fields`  
`type` | `metadata.product_event_type`  
`UID` | `principal.user.user_display_name`  
`uid` | `principal.user.userid`  
`unit` | `target.application`  
`uristem` | `target.url`  
`user_agent` | `network.http.user_agent`,  
`network.http.parsed_user_agent`  
`user_agent` (if JSON parse fails) | `additional.fields`  
`UserID` | `principal.user.windows_sid`  
`UserName` | `target.user.userid`  
`UserSid` | `principal.user.windows_sid`  
`Version` | `metadata.product_version`  
`version` | `metadata.product_version`  
`Weight` | `security_result.about.resource.attribute.labels`  
`WorkstationName` | `additional.fields`  
`X-BackEndCookie` | `additional.fields`  
`xff_ip` | `principal.ip`,  
`principal.asset.ip`  
`xforwardedfor` | `principal.ip`,  
`principal.asset.ip` (for the first IP address),  
`intermediary.ip` (for the rest of theIP addresses)  
  
## UDM mapping delta reference

On July 16, 2026, Google SecOps released a new version of the Microsoft Internet Information Services (IIS) parser, which includes significant changes to the mapping of Microsoft Internet Information Services log fields to UDM fields.

The following table lists the mapping delta for Microsoft Internet Information Services log-to-UDM fields exposed prior to July 16, 2026 and subsequently (listed in the **Old mapping** and **Current mapping** columns respectively):

Log field | Old mapping | Current mapping  
---|---|---  
`AccountType` | `principal.user.role_name` | `principal.user.attribute.roles[].name`  
`Action` | `security_result.about.resource.attribute.labels` | `securtiy_result.action_details`  
`agent.type` | `principal.application` | `observer.application`  
`agent.type + host_id` | `observer.asset_id` | `target.asset.asset_id => host_id: %{host_id}`,  
`observer.asset.asset_id => agent.type + agent.id` ,  
(In the old mapping, the log fields `agent.type` and `host_id` merged and mapped to `observer.assetid`. In the current mapping, `host_id` maps to `target.asset.asset_id` and `agent.type` maps to `observer.asset.asset_id`.)  
`app_name` | `principal.application` | `target.hostname`  
`c_ip` | `principal.ip`,  
`principal.asset.ip` | If xff_ip is present: `intermediary.ip`  
`comm` | `target.process.command_line` | `principal.application`  
`cookie` |  | `additional.fields`  
`cribl_breaker` | `target.resource.attribute.labels` | `additional.fields`  
`cs`(`User-Agent`) | `network.http.user_agent` | The parser now includes a conditional check to avoid mapping of "-" values, which removes `network.http.user_agent` mapping when `cs`(`User-Agent`) has just "-".  
`cs-uri-query` | Data fields were extracted from it and mapped individually. | Concatenated with `cs-uri-stem` and mapped to `target.url`. Removed individually extracted mappings to conserve the whole meaning of the URL data.  
`cs-version` | `network.tls.version` | `network.application_protocol`,  
`network.application_protocol_version`  
`cs_version` | `network.tls.version` | `network.application_protocol`,  
`network.application_protocol_version`  
`csversion` | `network.tls.version` | `network.application_protocol`,  
`network.application_protocol_version`  
`Domain` | `principal.user.userid` | `principal.administrative_domain`  
`ecs.version` | `principal.asset.attribute.labels` | `additional.fields`  
`ftp_command` | `principal.application` | `network.ftp.command`  
`host` | `principal.hostname`,  
`principal.asset.hostname` | `target.hostname`,  
`target.asset.hostname`,  
`observer.hostname` (The target web server in the absence of a computer-name related field. Otherwise, the field acts as an identifier of the observer machine.)  
`host.architecture` | `principal.asset.hardware.cpu_platform` | `target.asset.hardware.cpu_platform`  
`host.mac` | `principal.mac` | `target.mac`  
`host.os.build` | `additional.fields` | `target.platform_patch_level`  
`host.os.kernel` | `principal.platform_patch_level` | `additional.fields`  
`host.os.platform` | `principal.platform` | `target.platform`  
`intermediary_device_name` | `intermediary.hostname`,  
`observer.hostname`  
(In the old mapping, the parser took the server-related data as two fields. The parser now takes a single field and maps server-related data to the relevant target details.) | `target.hostname`  
`log.file.path` | `target.file.full_path` | `observer.file.full_path`  
`LogonType` | `additional.fields` | `extensions.auth.auth_details`  
`name` | `target.resource.name`,  
`additional.fields`  
(In the old mapping, `name` was extracted from a pattern and improperly mapped.) | `target.application`  
`observer_devicename` | `intermediary.hostname`,  
`observer.hostname`  
(In the old mapping, the parser extracted `observer_devicename` from a pattern and improperly mapped the server-related data as two fields. The parser now takes a single field and maps server-related data to the relevant target details.) | `target.hostname`  
`OS_type` | `principal.asset.platform_software.platform` | `target.platform`  
`s-sitename` | `target.resource.name`,  
`additional.fields` | `target.application`  
`s_port` (extracted from updated patterns) | `principal.port` | `target.port`  
`s_sitename` | `target.resource.name`,  
`additional.fields` | `target.application`  
`sitename` | `target.resource.name`,  
`additional.fields` | `target.application`  
`source` | `principal.resource.attribute.labels` | `observer.file.full_path`  
`SourceName` | `security_result.about.resource.attribute.labels` | `additional.fields`  
`SourceSystem` | `security_result.detection_fields` | `observer.application`  
`sSiteName` | `target.resource.name`,  
`additional.fields` | `target.application`  
`SubjectUserName` | `principal.user.userid`,  
`principal.hostname` | `principal.user.userid`  
`tags` | `security_result.rule_name` | `additional.fields`  
`UID` | `target.user.userid` | `principal.user.user_display_name`  
`UserSid` | `target.user.windows_sid` | `principal.user.windows_sid`  
`xforwardedfor` | `principal.ip`,  
`target.ip`,  
`intermediary.ip`  
(In different cases) | `principal.ip` (the first IP address),  
`intermediary.ip` (all the rest of the IP addresses)  
IIS log details encapsulated in `_raw` or `message` | `security_result.description` | Removed if the format is parsed by the internal filter.  
Web server request-response log lines from IIS that detail the HTTP transaction, that is, a GET request resulting in a redirect, not an authentication outcome. | `metadata.event_type = USER_LOGIN` | `metadata.event_type = NETWORK_HTTP`  
N/A | `network.http.parsed_user_agent`  
(In the old mapping, the parser improperly mapped a log field to the user agent. In the current mapping, the parser properly maps a suitable field to `network.http.parsed_user_agent`.) |   
N/A | `principal.port` | `network.http.response_code` (In the old mapping, the mapping was improper. In the current mapping, the parser properly maps a suitable field to `network.http.response_code`.)  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/iis-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
