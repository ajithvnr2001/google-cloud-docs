---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-winlogbeat/
title: Collect Elastic Windows Event Log Beats logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:16.031003+00:00
---

# Collect Elastic Windows Event Log Beats logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/elastic-winlogbeat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Elastic Windows Event Log Beats logs

**Parser Version:** 19.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Elastic Windows Event Log Beats logs into Google Security Operations using the Bindplane agent.

Winlogbeat is Elastic's Windows-specific event log shipping agent that collects Windows Event Logs and forwards them to various destinations. It runs as a Windows service on Windows systems and can collect events from Application, Security, System, and other Windows event log channels.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or a Linux host with `systemd` for running the Bindplane agent
  * Network connectivity between the Bindplane agent and the Logstash server
  * Network connectivity between Logstash and the Bindplane agent
  * If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
  * Windows systems where Winlogbeat will be installed to collect event logs
  * Administrator access to Windows systems for Winlogbeat installation
  * Logstash server (version 7.x or 8.x) for intermediary processing



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
         

The service status should be **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service status should be **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:1514"
         
         exporters:
           chronicle/winlogbeat:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '<CREDS_FILE_PATH>'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: ELASTIC_WINLOGBEAT
             raw_log_field: body
             ingestion_labels:
               env: production
               source: winlogbeat
         
         service:
           pipelines:
             logs/winlogbeat_to_chronicle:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/winlogbeat
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * `listen_address`: Set to `0.0.0.0:1514` to listen on all interfaces on port 1514 (TCP). You can change the port number if needed, but ensure that it matches the Logstash syslog output configuration.
     * Exporter configuration:

       * `<CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `<CUSTOMER_ID>`: Customer ID from the previous step

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.




### Example configuration:
    
    
    receivers:
      tcplog:
        listen_address: "0.0.0.0:1514"
    
    exporters:
      chronicle/winlogbeat:
        protocol: https
        # Region of your instance, for example us, europe, asia-southeast1
        location: <LOCATION>
        # Project number of the Google Cloud project linked to the instance
        project: '<PROJECT_NUMBER>'
        compression: gzip
        creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
        customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
        endpoint: chronicle.googleapis.com
        log_type: ELASTIC_WINLOGBEAT
        raw_log_field: body
        ingestion_labels:
          env: production
          source: winlogbeat
    
    service:
      pipelines:
        logs/winlogbeat_to_chronicle:
          receivers:
            - tcplog
          exporters:
            - chronicle/winlogbeat
    

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/winlogbeat:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ELASTIC_WINLOGBEAT
            raw_log_field: body
            ingestion_labels:
              env: production
              source: winlogbeat
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux:

    1. Run the following command:
           
           sudo systemctl restart observiq-otel-collector
           

    2. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    3. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows:

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
           




## Install and configure Logstash

Logstash is required as an intermediary to receive events from Winlogbeat and forward them to the Bindplane agent via syslog. Winlogbeat does not have native syslog output capability.

### Install Logstash

  1. Download Logstash from the [Elastic downloads page](https://www.elastic.co/downloads/logstash).
  2. Install Logstash on a Windows or Linux server:


  * **Linux (Debian/Ubuntu):**
        
        wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
        sudo apt-get install apt-transport-https
        echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-8.x.list
        sudo apt-get update && sudo apt-get install logstash
        

  * **Linux (RHEL/CentOS):**
        
        sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
        sudo tee /etc/yum.repos.d/logstash.repo <<EOF
        [logstash-8.x]
        name=Elastic repository for 8.x packages
        baseurl=https://artifacts.elastic.co/packages/8.x/yum
        gpgcheck=1
        gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
        enabled=1
        autorefresh=1
        type=rpm-md
        EOF
        sudo yum install logstash
        

  * **Windows:**

    1. Download the ZIP file from the Elastic downloads page.
    2. Extract to `C:\logstash`.



### Configure Logstash pipeline

  1. Create a new pipeline configuration file:

     * **Linux:**
           
           sudo nano /etc/logstash/conf.d/winlogbeat-to-syslog.conf
           

     * **Windows:**
           
           notepad "C:\logstash\config\winlogbeat-to-syslog.conf"
           

  2. Add the following configuration:
         
         input {
             beats {
                 port => 5044
             }
         }
         
         output {
             syslog {
                 host => "<BINDPLANE_AGENT_IP>"
                 port => 1514
                 protocol => "tcp"
                 rfc => "rfc5424"
                 appname => "winlogbeat"
                 facility => "user-level"
                 severity => "informational"
             }
         }
         

  3. Replace `<BINDPLANE_AGENT_IP>` with the IP address of the server running the Bindplane agent.




### Example Logstash configuration
    
    
    input {
        beats {
            port => 5044
        }
    }
    
    output {
        syslog {
            host => "192.168.1.100"
            port => 1514
            protocol => "tcp"
            rfc => "rfc5424"
            appname => "winlogbeat"
            facility => "user-level"
            severity => "informational"
        }
    }
    

### Start Logstash

  * **Linux:**

    1. Start Logstash:
           
           sudo systemctl start logstash
           sudo systemctl enable logstash
           

    2. Verify Logstash is running:
           
           sudo systemctl status logstash
           

    3. Check Logstash logs:
           
           sudo tail -f /var/log/logstash/logstash-plain.log
           

  * **Windows:**
        
        cd C:\logstash\bin
        logstash.bat -f C:\logstash\config\winlogbeat-to-syslog.conf
        

For production use, install Logstash as a Windows service using NSSM or similar tools.




## Install Winlogbeat on Windows systems

### Download Winlogbeat

  1. Download Winlogbeat from the [Elastic downloads page](https://www.elastic.co/downloads/beats/winlogbeat).
  2. Choose the ZIP or MSI installer for Windows.



### Install Winlogbeat

  * **Using MSI installer:**

    1. Run the MSI installer.
    2. Follow the installation wizard.
    3. Install to the default location: `C:\Program Files\Winlogbeat`.
  * **Using ZIP file:**

    1. Extract the ZIP file to `C:\Program Files\Winlogbeat`.
    2. Open **PowerShell** as an administrator.
    3. Navigate to the Winlogbeat directory:
           
           cd 'C:\Program Files\Winlogbeat'
           

    4. Run the installation script:
           
           .\install-service-winlogbeat.ps1
           




## Configure Winlogbeat to send logs to Logstash

  1. Open the Winlogbeat configuration file:
         
         notepad "C:\Program Files\Winlogbeat\winlogbeat.yml"
         

  2. Configure the event logs to collect. Locate the `winlogbeat.event_logs` section and configure as follows:
         
         winlogbeat.event_logs:
           - name: Application
             ignore_older: 72h
           - name: System
           - name: Security
           - name: Microsoft-Windows-Sysmon/Operational
             ignore_older: 72h
           - name: Windows PowerShell
             event_id: 400, 403, 600, 800
           - name: Microsoft-Windows-PowerShell/Operational
             event_id: 4103, 4104, 4105, 4106
           - name: ForwardedEvents
             tags: [forwarded]
         

  3. Comment out the Elasticsearch output section by adding `#` at the beginning of each line:
         
         #output.elasticsearch:
         #  hosts: ["localhost:9200"]
         

  4. Uncomment and configure the Logstash output section:
         
         output.logstash:
           hosts: ["<LOGSTASH_SERVER_IP>:5044"]
         

  5. Replace `<LOGSTASH_SERVER_IP>` with the IP address of your Logstash server.




### Example Winlogbeat configuration
    
    
    winlogbeat.event_logs:
      - name: Application
        ignore_older: 72h
      - name: System
      - name: Security
      - name: Microsoft-Windows-Sysmon/Operational
        ignore_older: 72h
    
    output.logstash:
      hosts: ["192.168.1.50:5044"]
    

### Save the configuration file

Save and close the file.

## Start Winlogbeat service

  1. Open **PowerShell** as an administrator.
  2. Start the Winlogbeat service:
         
         Start-Service winlogbeat
         

  3. Verify the service is running:
         
         Get-Service winlogbeat
         

The status should show as **Running**.

  4. Check Winlogbeat logs for errors:
         
         Get-Content "C:\ProgramData\winlogbeat\Logs\winlogbeat" -Tail 50
         




## Verify log flow

### Verify Winlogbeat to Logstash connection

  1. On the Logstash server, check the Logstash logs:

     * **Linux:**
           
           sudo tail -f /var/log/logstash/logstash-plain.log
           

     * **Windows:**
           
           type C:\logstash\logs\logstash-plain.log
           

  2. Look for messages indicating Beats connections:
         
         [INFO ][logstash.inputs.beats] Beats inputs: Starting input listener {:address=>"0.0.0.0:5044"}
         




### Verify Logstash to Bindplane agent connection

  1. On the Bindplane agent server, check the agent logs:

     * **Linux:**
           
           sudo journalctl -u observiq-otel-collector -f
           

     * **Windows:**
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           

  2. Look for messages indicating successful log ingestion.




### Verify logs in Google SecOps

  1. Sign in to the Google SecOps console.
  2. Go to **Search**.
  3. Run a search query to verify Winlogbeat logs are being ingested:
         
         metadata.log_type = "ELASTIC_WINLOGBEAT"
         

  4. Verify that Windows event logs appear in the search results.




## Troubleshooting

### Winlogbeat not connecting to Logstash

  * Verify network connectivity between Winlogbeat and Logstash:
        
        Test-NetConnection -ComputerName <LOGSTASH_IP> -Port 5044
        

  * Check Windows Firewall rules allow outbound connections on port 5044.

  * Verify Logstash is listening on port 5044:

    * **Linux:**
          
          sudo netstat -tulpn | grep 5044
          

    * **Windows:**
          
          netstat -an | findstr 5044
          




### Logstash not forwarding to Bindplane agent

  * Verify network connectivity between Logstash and Bindplane agent:

    * **Linux:**
          
          telnet <BINDPLANE_IP> 1514
          

    * **Windows:**
          
          Test-NetConnection -ComputerName <BINDPLANE_IP> -Port 1514
          

  * Check firewall rules allow TCP connections on port 1514.

  * Verify Bindplane agent is listening on port 1514:

    * **Linux:**
          
          sudo netstat -tulpn | grep 1514
          

    * **Windows:**
          
          netstat -an | findstr 1514
          




### Logs not appearing in Google SecOps

  * Verify the customer ID and ingestion authentication file are correct.
  * Check the Bindplane agent logs for authentication errors.
  * Verify the regional endpoint matches your Google SecOps instance region.
  * Ensure the `log_type` is set to `ELASTIC_WINLOGBEAT` exactly as shown.



## UDM mapping table

| `winlog.event_data.powershell.HostApplication` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog | | `winlog.event_data.powershell.ScriptName` | `event.idm.read_only_udm.target.process.file.full_path` | Mapped from changelog | | `winlog.event_data.powershell.UserId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog | | `host.mac` | `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog | | `_event.created` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog | | `agent.name` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog | | `host.domain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog | | `winlog.event_data.powershell.CommandName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.CommandLine` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.HostVersion` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.DetailSequence` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.DetailTotal` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.HostId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.HostName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.PipelineId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.RunspaceId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.SequenceNumber` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.keywords` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.powershell.EngineVersion` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.TaskName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog | | `winlog.event_data.ClientProcessId` | `event.idm.read_only_udm.target.process.pid` | Mapped from changelog | | `winlog.event_data.ParentProcessId` | `event.idm.read_only_udm.target.process.parent_process.pid` | Mapped from changelog | | `winlog.event_data.ClientProcessStartKey` | `event.idm.read_only_udm.target.process.product_specific_process_id` | Mapped from changelog | | `TimeTriggerStartBoundary` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `EventVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `winlog.version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `RegistrationInfoSecurityDescriptor` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `winlog.event_data.RpcCallClientLocality` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `winlog.provider_guid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog | | `winlog.event_data.param1` | `event.idm.read_only_udm.target.application` | Mapped from changelog | | `DestinationIp` | `target.ip` | Mapped from changelog | | `source_network_address` | `src.ip` | Mapped from changelog | | `source_port` | `src.port` | Mapped from changelog | | `winlog.event_data.TaskContent` | `additional.fields` | Mapped from changelog | | `principal_user_id` | `principal.user.userid` | Mapped from changelog | | `principal_command_line` | `principal.process.command_line` | Mapped from changelog | | `run_level", "arguments", "RegistrationInfoURI", "WnfStateChangeTriggerEnabled", "WnfStateChangeTriggerStateName", "WnfStateChangeTriggerData", "WnfStateChangeTriggerDataOffset", "IdleSettingsRestartOnIdle", "IdleSettingsStopOnIdleEnd", "IdleSettingsWaitTimeout", "IdleSettingsDuration", "Priority", "ExecutionTimeLimit", "RunOnlyIfIdle", "DisallowStartOnRemoteAppSession", "UseUnifiedSchedulingEngine", "DisallowStartIfOnBatteries", "MultipleInstancesPolicy", "StopIfGoingOnBatteries", "AllowHardTerminate", "StartWhenAvailable", "RunOnlyIfNetworkAvailable", "AllowStartOnDemand", "Enabled", "Hidden", and "WakeToRun` | `additional.fields` | Mapped from changelog | | `winlog.event_data.ObjectServer` | `target.resource.attribute.labels` | Mapped from changelog | | `process.executable` | `principal.process.file.full_path` | Mapped from changelog | | `process.parent.executable` | `principal.process.parent_process.file.full_path` | Mapped from changelog | | `process.name` | `principal.process.file.names` | Mapped from changelog | | `process.parent.name` | `principal.process.parent_process.file.names` | Mapped from changelog | | `process.entity_id` | `target.process.product_specific_process_id` | Mapped from changelog | | `process.pid` | `principal.resource.attribute.labels` | Mapped from changelog | | `winlog.logon.failure.sub_status", "winlog.logon.failure.reason" and "winlog.logon.failure.status` | `security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.GroupMembership` | `principal.user.group_identifiers` | Mapped from changelog | | `client_ip` | `principal.asset.ip` | Mapped from changelog | | `ip` | `principal.asset.ip` | Mapped from changelog | | `winlog.event_data.SourceIp` | `principal.asset.ip` | Mapped from changelog | | `destination.ip` | `target.asset.ip` | Mapped from changelog | | `winlog.event_data.DestinationIp` | `target.asset.ip` | Mapped from changelog | | `agent.hostname` | `target.asset.hostname` | Mapped from changelog | | `winlog.event_data.IpAddress` | `principal.asset.ip` | Mapped from changelog | | `source.ip` | `principal.asset.ip` | Mapped from changelog | | `winlog.event_data.Binary", "winlog.event_data.process.thread.id", "winlog.event_data.param1", "winlog.event_data.param2", "winlog.event_data.param3", "winlog.event_data.param4", "winlog.event_data.param5", "winlog.event_data.param6", "winlog.event_data.param7", "winlog.event_data.param8", "winlog.event_data.param9", "winlog.event_data.param10", "winlog.event_data.param11", "winlog.event_data.param12", "winlog.event_data.param13", "winlog.channel", "winlog.opcode` | `security_result.detection_fields` | Mapped from changelog | | `host.ip` | `principal.ip` | Mapped from changelog | | `winlog.process.pid` | `principal.process.pid` | Mapped from changelog | | `message` | `metadata.description` | Mapped from changelog | | `message` | `security_result.detection_fields` | Mapped from changelog | | `metadata.event_type` | `SERVICE_STOP` | Mapped from changelog | | `metadata.event_type` | `SERVICE_START` | Mapped from changelog | | `winlog.event_data.HandleId` | `resource_ancestors.product_object_id` | Mapped from changelog | | `winlog.event_data.ObjectType` | `target.resource.resource_subtype` | Mapped from changelog | | `winlog.event_data.OperationType` | `security_result.summary` | Mapped from changelog | | `object_server` | `resource_ancestors.name` | Mapped from changelog | | `Accesses` | `target.resource.attribute.labels` | Mapped from changelog | | `Properties` | `security_result.detection_fields` | Mapped from changelog | | `event_data.param1` | `target.application` | Mapped from changelog | | `event_data.param2` | `security_result.action` | Mapped from changelog | | `event_data.param1` | `target.resource.attribute.permissions` | Mapped from changelog | | `event_data.param5` | `target.resource.product_object_id` | Mapped from changelog | | `event_data.param6` | `target.user.userid` | Mapped from changelog | | `event_data.param7` | `target.administrative_domain` | Mapped from changelog | | `event_data.param8` | `target.user.windows_sid` | Mapped from changelog | | `event_data.param10` | `target.application` | Mapped from changelog | | `event_data.param1` | `target.user.userid` | Mapped from changelog | | `client_ip` | `principal.ip` | Mapped from changelog | | `database_name` | `target.hostname` | Mapped from changelog | | `summary` | `security_result.summary` | Mapped from changelog | | `event_id` | `metadata.product_event_type` | Mapped from changelog | | `computer_name` | `principal.hostname` | Mapped from changelog | | `type` | `observer.application` | Mapped from changelog | | `task` | `target.resource.attribute.labels` | Mapped from changelog | | `source_name` | `security_result.about.labels` | Mapped from changelog | | `process_id` | `principal.process.pid` | Mapped from changelog | | `provider_guid` | `additional.fields` | Mapped from changelog | | `level` | `security_result.severity` | Mapped from changelog | | `thread_id` | `security_result.about.resource.attribute.labels` | Mapped from changelog | | `beat.version` | `principal.platform_version` | Mapped from changelog | | `message` | `security_result.description` | Mapped from changelog | | `winlog.event_data.LmPackageName` | `target.resource.attribute.labels` | Mapped from changelog | | `winlog.event_data.AuthenticationPackageName` | `target.resource.attribute.labels` | Mapped from changelog | | `winlog.event_data.LogonProcessName` | `target.resource.attribute.labels` | Mapped from changelog | | `winlog.event_data.WorkstationName` | `target.resource.attribute.labels` | Mapped from changelog | | `winlog.event_data.TargetOutboundUserName` | `target.resource.attribute.labels` | Mapped from changelog | | `CN" from "winlog.event_data.MemberName` | `target.user.userid` | Mapped from changelog | | `metadata.event_type` | `GROUP_MODIFICATION` | Mapped from changelog | | `winlog.event_data.Image` | `target.process.file.full_path` | Mapped from changelog | | `winlog.event_data.ProcessGuid` | `target.process.product_specific_process_id` | Mapped from changelog | | `winlog.event_data.ProcessId` | `target.process.pid` | Mapped from changelog | | `winlog.event_data.TargetObject` | `target.registry.registry_value_name` | Mapped from changelog | | `winlog.event_data.EventType` | `metadata.product_event_type` | Mapped from changelog | | `winlog.event_data.Subject` | `security_result.detection_fields` | Mapped from changelog | | `winlog.event_data.Requester` | `principal.user.userid` | Mapped from changelog | | `winlog.event_data.LogonType` | `extensions.auth.auth_details` | Mapped from changelog | | `winlog.event_data.ParentProcessId` | `principal.process.pid` | Mapped from changelog | | `winlog.event_data.ParentProcessGuid` | `principal.process.product_specific_process_id` | Mapped from changelog | | `winlog.event_data.ParentCommandLine` | `principal.process.command_line` | Mapped from changelog | | `winlog.event_data.ParentUser` | `principal.user.userid` | Mapped from changelog | | `winlog.event_data.CommandLine` | `target.process.command_line` | Mapped from changelog | | `winlog.event_data.User` | `target.user.userid` | Mapped from changelog | | `winlog.event_data.LogonGuid` | `target.resource.product_object_id` | Mapped from changelog | | `winlog.event_data.Hashes.SHA1` | `target.process.file.sha1` | Mapped from changelog | | `winlog.event_data.Hashes.SHA256` | `target.process.file.sha256` | Mapped from changelog | | `winlog.event_data.Hashes.MD5` | `target.process.file.md5` | Mapped from changelog | | `host.mac` | `principal.mac` | Mapped from changelog | | `winlog.event_data.ImageLoaded` | `target.process.file.full_path` | Mapped from changelog | | `winlog.opcode` | `security_result.description` | Mapped from changelog | | `winlog.event_data.MemberName` | `target.user.userid` | Mapped from changelog | | `winlog.event_data.MemberSid` | `target.user.windows_sid` | Mapped from changelog | | `winlog.event_data.TargetUserName` | `target.user.userid` | Mapped from changelog | | `winlog.event_data.TicketOptions", "winlog.event_data.TicketEncryptionType", "winlog.event_data.TicketEncryptionTypeDescription", "winlog.event_data.TransmittedServices", "winlog.event_data.TicketOptionsDescription` | `security_result.about.resource.attribute.labels` | Mapped from changelog | | `winlog.event_data.ServiceSid` | `target.user.windows_sid` | Mapped from changelog | | `winlog.event_data.TargetDomainName` | `target.administrative_domain` | Mapped from changelog | | `winlog.event_data.ServiceName` | `target.application` | Mapped from changelog | | `Failure Code" and "TicketOptions` | `security_result.about.labels` | Mapped from changelog | | `winlog.event_data.Status` | `security_result.action_details` | Mapped from changelog | | `winlog.event_data.Status" and "winlog.event_data.StatusDescription` | `metadata.description` | Mapped from changelog | | `winlog.event_data.RelativeTargetName` | `target.process.file.full_path` | Mapped from changelog | | `event.original` | `security_result.detection_fields` | Mapped from changelog | | `ip` | `principal.ip` | Mapped from changelog | | `mac` | `principal.mac` | Mapped from changelog | | `Account Domain` | `principal.administrative-domain` | Mapped from changelog | | `metadata.event_type` | `USER_CHANGE_PASSWORD` | Mapped from changelog | | `event.outcome` | `security_result.outcomes` | Mapped from changelog | | `event.action and event.outcome` | `security_result.summary` | Mapped from changelog | | `log.level` | `security_result.severity_details` | Mapped from changelog | | `User Account control` | `security_result.description` | Mapped from changelog | | `winlog.event_data.ObjectValueName` | `target.registry.registry_value_name` | Mapped from changelog | | `Operation Type` | `security_result.summary` | Mapped from changelog | | `metadata.event_type` | `REGISTRY_MODIFICATION` | Mapped from changelog | | `winlog.event_data.ProcessName` | `target.process.file.full_path` | Mapped from changelog | | `winlog.event_data.ObjectName` | `target.resource.name` | Mapped from changelog | | `winlog.event_data.OldValue` | `target.resource.attribute.labels` | Mapped from changelog | | `winlog.event_data.NewValue` | `target.resource.attribute.labels` | Mapped from changelog | | `winlog.computer_name` | `target.hostname` | Mapped from changelog | | `winlog.provider_name` | `metadata.product_name` | Mapped from changelog | | `winlog.event_data.OpCorrelationID` | `network.session_id` | Mapped from changelog | | `winlog.api","winlog.event_data.AttributeValue","winlog.provider_guid","winlog.event_data.ObjectDN","winlog.event_data.SubjectLogonId","event_data.AttributeSyntaxOID` | `additional.fields` | Mapped from changelog | | `winlog.record_id` | `metadata.product_log_id` | Mapped from changelog | | `winlog.event_data.AttributeLDAPDisplayName` | `target.resource.type` | Mapped from changelog | | `winlog.event_data.ObjectGUID` | `target.group.product_object_id` | Mapped from changelog | | `winlog.channel","winlog.process.thread.id","winlog.event_data.DSType","winlog.event_data.ObjectClass` | `security_result.about.resource.attribute.labels` | Mapped from changelog | | `winlog.event_data.DSName` | `target.hostname` | Mapped from changelog | | `winlog.event_id` | `metadata.product_event_type` | Mapped from changelog | | `source.ip` | `principal.ip` | Mapped from changelog | | `source.port` | `principal.port` | Mapped from changelog | | `user.name` | `principal.user.user_display_name` | Mapped from changelog | | `related.user` | `principal.user.group_identifiers` | Mapped from changelog |

Field mapping information is not available for this parser.

## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-winlogbeat-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
