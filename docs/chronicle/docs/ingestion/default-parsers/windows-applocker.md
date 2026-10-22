---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-applocker/
title: Collect Windows AppLocker logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:04.004534+00:00
---

# Collect Windows AppLocker logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-applocker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Windows AppLocker logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Windows AppLocker logs to Google Security Operations using the Bindplane agent.

Windows AppLocker is an application control feature built into Windows that generates policy enforcement, audit, and application execution events. AppLocker writes these events to four Windows Event Log channels under **Applications and Services Logs > Microsoft > Windows > AppLocker**: **EXE and DLL** , **MSI and Script** , **Packaged app-Deployment** , and **Packaged app-Execution**.

You can configure ingestion using one of two supported methods:

  * **Method 1: NXLog forwarding to Bindplane agent (recommended)**. NXLog reads the AppLocker channels on each endpoint and forwards the events as syslog with a JSON payload to a Bindplane agent, which sends them to Google SecOps under the `WINDOWS_APPLOCKER` log type. This is the format the `WINDOWS_APPLOCKER` parser expects, and it preserves the AppLocker rule and file fields.
  * **Method 2: Bindplane agent direct channel read**. The Bindplane agent on each endpoint reads the AppLocker channels natively and sends the raw Windows event XML to Google SecOps under the `WINEVTLOG` log type. No file export or additional agent is needed, but the events are parsed by the generic Windows Event Log parser.

**Note:** Don't send the raw event XML produced by the Bindplane agent to the `WINDOWS_APPLOCKER` log type. The `WINDOWS_APPLOCKER` parser accepts the NXLog syslog formats (JSON, key-value, or NXLog XML) and drops the raw Windows event XML as malformed. Use Method 1 for the `WINDOWS_APPLOCKER` log type, or Method 2 with the `WINEVTLOG` log type.



## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Windows 10 or later, with AppLocker policies configured
  * Administrator access to the Windows endpoints
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * For Method 1: a Windows or Linux host for the Bindplane agent that the endpoints can reach on TCP port 514



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

## Get the Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent according to the following instructions. For Method 1, install it on the host that receives syslog from NXLog. For Method 2, install it on every endpoint whose AppLocker events you want to collect.

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
         




### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Method 1: NXLog forwarding to Bindplane agent

### Configure the Bindplane agent to receive syslog and send to Google SecOps

  1. Open the configuration file on the Bindplane agent host:

**Windows:**
         
         notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
         

**Linux:**
         
         sudo nano /opt/observiq-otel-collector/config.yaml
         

  2. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           tcplog/applocker:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/windows_applocker:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-auth.json'
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: WINDOWS_APPLOCKER
             raw_log_field: body
             ingestion_labels:
               env: production
         
         service:
           pipelines:
             logs/applocker_to_chronicle:
               receivers:
                 - tcplog/applocker
               exporters:
                 - chronicle/windows_applocker
         

  3. Replace the following placeholders:

     * `listen_address`: The IP address and port the agent listens on. `0.0.0.0:514` accepts syslog on every interface on TCP port 514. Use a port higher than 1024 on Linux if the agent does not run as root, and open the port in the host firewall.
     * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
       * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
     * `<customer_id>`: Customer ID from the Get Google SecOps customer ID section
     * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
     * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * `endpoint`: Keep set to `chronicle.googleapis.com`.
     * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  4. Save the file.

  5. Restart the Bindplane agent:

**Windows:**
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         

**Linux:**
         
         sudo systemctl restart observiq-otel-collector
         




#### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/windows_applocker:
            compression: gzip
            creds_file_path: '/path/to/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: WINDOWS_APPLOCKER
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Install NXLog on the Windows endpoints

  1. Download NXLog Agent (formerly NXLog Enterprise Edition) for Windows from the [NXLog website](https://nxlog.co/downloads).
  2. Run the installer on each endpoint whose AppLocker events you want to collect, and accept the default installation directory (`C:\Program Files\nxlog`).

**Note:** Use NXLog Agent. NXLog Community Edition does not deliver the `UserData` part of AppLocker events, which holds the rule name, policy name, path, file hash and target user. Events forwarded by Community Edition are parsed, but without those fields.



### Configure NXLog to forward AppLocker events

  1. Open **File Explorer** and navigate to `C:\Program Files\nxlog\conf`.
  2. Open the `nxlog.conf` file in **Notepad** or a text editor with administrator privileges.
  3. Replace the entire contents with the following configuration:
         
         define ROOT C:\Program Files\nxlog
         define LOGDIR %ROOT%\data
         define LOGFILE %LOGDIR%\nxlog.log
         
         Moduledir %ROOT%\modules
         CacheDir %ROOT%\data
         Pidfile %ROOT%\data\nxlog.pid
         SpoolDir %ROOT%\data
         LogFile %LOGFILE%
         
         <Extension json>
             Module      xm_json
         </Extension>
         
         <Extension xml>
             Module      xm_xml
         </Extension>
         
         <Extension syslog>
             Module      xm_syslog
         </Extension>
         
         <Input applocker_events>
             Module      im_msvistalog
             <QueryXML>
                 <QueryList>
                     <Query Id="0">
                         <Select Path="Microsoft-Windows-AppLocker/EXE and DLL">*</Select>
                         <Select Path="Microsoft-Windows-AppLocker/MSI and Script">*</Select>
                         <Select Path="Microsoft-Windows-AppLocker/Packaged app-Deployment">*</Select>
                         <Select Path="Microsoft-Windows-AppLocker/Packaged app-Execution">*</Select>
                     </Query>
                 </QueryList>
             </QueryXML>
             <Exec>
                 # AppLocker keeps the rule and file details in the UserData part of the
                 # event. parse_xml() turns them into RuleAndFileData.* fields, which
                 # the parser expects.
                 if $UserData parse_xml($UserData);
                 $Message = to_json();
                 to_syslog_bsd();
             </Exec>
         </Input>
         
         <Output bindplane_syslog>
             Module      om_tcp
             Host        <BINDPLANE_AGENT_IP>
             Port        514
         </Output>
         
         <Route applocker_to_bindplane>
             Path        applocker_events => bindplane_syslog
         </Route>
         

  4. Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host, and `514` with the port from `listen_address` if you changed it.

  5. Save the `nxlog.conf` file.

**Note:** The **EXE and DLL** channel is very verbose when DLL rules are enforced. To collect only blocked and audited executions, replace the `*` selectors with `*[System[(EventID=8003 or EventID=8004 or EventID=8006 or EventID=8007 or EventID=8021 or EventID=8022 or EventID=8024 or EventID=8025)]]`.



### Restart the NXLog service

  1. Open **Services** by pressing `Win+R`, typing `services.msc`, and pressing Enter.
  2. Locate **nxlog** in the services list.
  3. Right-click **nxlog** and select **Restart**.
  4. Verify the service status shows **Running**.


  * Alternatively, you can restart NXLog from the Command Prompt as administrator:
        
        net stop nxlog && net start nxlog
        




### Verify AppLocker events are being forwarded

  1. Open **Event Viewer** on the Windows endpoint.
  2. Go to **Applications and Services Logs > Microsoft > Windows > AppLocker > EXE and DLL**.
  3. Verify that AppLocker events (for example, Event IDs 8002, 8003, or 8004) are present. If the log is empty, confirm that an AppLocker policy is applied and the **Application Identity** service is running.
  4. Check the NXLog log file at `C:\Program Files\nxlog\data\nxlog.log` for errors or warnings.
  5. On the Bindplane agent host, check the agent log for errors:

**Windows:**
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         

**Linux:**
         
         sudo tail -f /opt/observiq-otel-collector/log/collector.log
         




## Method 2: Bindplane agent direct channel read

Use this method when you don't want to deploy NXLog. The Bindplane agent installed on each endpoint reads the AppLocker channels directly from the Windows Event Log and sends the raw event XML to Google SecOps under the `WINEVTLOG` log type.

**Note:** The `WINEVTLOG` parser maps the common Windows event fields of every AppLocker event and has specific handling for the allowed (8002) and blocked (8004) EXE and DLL events. The AppLocker rule, policy, and file hash fields of the other event IDs are not extracted. If you need those fields, use Method 1.

### Configure the Bindplane agent to read the AppLocker channels

  1. On the Windows endpoint, open the configuration file:
         
         notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
         

  2. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           windowseventlog/applocker_exe_dll:
             channel: Microsoft-Windows-AppLocker/EXE and DLL
             raw: true
             max_reads: 100
             poll_interval: 5s
             start_at: end
         
           windowseventlog/applocker_msi_script:
             channel: Microsoft-Windows-AppLocker/MSI and Script
             raw: true
             max_reads: 100
             poll_interval: 5s
             start_at: end
         
           windowseventlog/applocker_packaged_deployment:
             channel: Microsoft-Windows-AppLocker/Packaged app-Deployment
             raw: true
             max_reads: 100
             poll_interval: 5s
             start_at: end
         
           windowseventlog/applocker_packaged_execution:
             channel: Microsoft-Windows-AppLocker/Packaged app-Execution
             raw: true
             max_reads: 100
             poll_interval: 5s
             start_at: end
         
         exporters:
           chronicle/winevtlog:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: WINEVTLOG
             raw_log_field: body
             ingestion_labels:
               env: production
         
         service:
           pipelines:
             logs/applocker_to_chronicle:
               receivers:
                 - windowseventlog/applocker_exe_dll
                 - windowseventlog/applocker_msi_script
                 - windowseventlog/applocker_packaged_deployment
                 - windowseventlog/applocker_packaged_execution
               exporters:
                 - chronicle/winevtlog
         

  3. Replace the following placeholders:

     * `<customer_id>`: Customer ID from the Get Google SecOps customer ID section
     * `endpoint`: Regional endpoint URL, as listed in Method 1
     * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
     * `start_at`: Set to `end` to collect new events only, or `beginning` to also collect the events already in the channels
  4. Save the file.

  5. Restart the Bindplane agent:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         

  6. Verify the service is running and check the agent log for errors:
         
         sc query observiq-otel-collector
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




#### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/winevtlog:
            compression: gzip
            creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: WINEVTLOG
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`syslog_ts` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss Z`  
`event_type` | `metadata.event_type` | Directly mapped  
`EventID` | `metadata.product_event_type` | Directly mapped  
`sourceName` | `metadata.product_name` | Directly mapped  
`SourceModuleType` | `observer.application` | Renamed/mapped  
`Domain` | `principal.administrative_domain` | Renamed/mapped  
`Hostname` | `principal.hostname` | Renamed/mapped  
`principal_ip1` | `principal.ip` | Merged  
`roles` | `principal.user.attribute.roles` | Merged  
`AccountName` | `principal.user.userid` | Renamed/mapped  
`EventID` | `security_result.about.labels` | Mapped: `8002,8005, 8006, 8020` → `ssdl`  
`ssdl` | `security_result.about.labels` | Merged  
`message1` | `security_result.action` | Mapped: `allowed to run` → `security_action`  
`security_action` | `security_result.action` | Merged  
`message1` | `security_result.description` | Directly mapped  
`RuleAndFileData.RuleId` | `security_result.rule_id` | Renamed/mapped  
`EventID` | `security_result.rule_name` | Directly mapped  
`RuleAndFileData.RuleName` | `security_result.rule_name` | Renamed/mapped  
`EventType` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`, `WARNING` → `LOW`  
`RuleAndFileData.PolicyName` | `security_result.summary` | Renamed/mapped  
`ThreadID` | `security_result.threat_id` | Renamed/mapped  
`RuleAndFileData.FullFilePath` | `target.process.file.full_path` | Renamed/mapped  
`filePath` | `target.process.file.full_path` | Renamed/mapped  
`ProcessID` | `target.process.pid` | Directly mapped  
`RuleAndFileData.TargetProcessId` | `target.process.pid` | Renamed/mapped  
`ProviderGuid` | `target.resource.product_object_id` | Renamed/mapped  
`UserID` | `target.user.userid` | Renamed/mapped  
N/A | `metadata.vendor_name` | Constant: `Microsoft`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-applocker-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
