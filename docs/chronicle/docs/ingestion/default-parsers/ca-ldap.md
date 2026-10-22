---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-ldap/
title: Collect CA LDAP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:28:59.743531+00:00
---

# Collect CA LDAP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-ldap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CA LDAP logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CA LDAP logs to Google Security Operations using Bindplane agent.

CA Directory (formerly Symantec Directory) is an LDAP v2/v3 compliant directory server based on X.500 standards. It provides enterprise-level directory services with comprehensive logging capabilities including alarm, trace, warn, query, summary, connection, diagnostic, update, and statistics logs for monitoring directory operations and security events.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and CA Directory server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the CA Directory server (root or administrator)
  * CA Directory installed and configured with logging enabled



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

**Note:** The `customer ID` is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

  * Windows installation

    1. Open **Command Prompt** or **PowerShell** as an administrator.
    2. Run the following command:
           
           msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
           

    3. Wait for the installation to complete.

    4. Verify the installation by running:
           
           sc query observiq-otel-collector
           

The service should show as **RUNNING**.

  * Linux installation

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

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/ca_directory:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
             customer_id: 'YOUR_CUSTOMER_ID'
             endpoint: chronicle.googleapis.com
             log_type: CA_LDAP
             raw_log_field: body
             ingestion_labels:
               env: production
               source: ca_directory
         
         service:
           pipelines:
             logs/ca_directory_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/ca_directory
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on UDP port 514

         * For Linux non-root installations, use port `1514` or higher
         * Ensure the port matches the port configured in rsyslog forwarding
     * Exporter configuration:

       * `creds_file_path`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `customer_id`: Replace `YOUR_CUSTOMER_ID` with your `customer ID`. For details, see Get Google SecOps customer ID.

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `log_type`: Set to `CA_LDAP` (Chronicle ingestion label for CA Directory)

       * `ingestion_labels`: Optional labels for filtering and organization




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/ca_directory:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CA_LDAP
            raw_log_field: body
            ingestion_labels:
              env: production
              source: ca_directory
        


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
           




## Configure CA LDAP syslog forwarding using rsyslog

This section describes how to configure rsyslog on the CA Directory server to forward logs to the Bindplane agent.

### Identify CA Directory log file locations

CA Directory stores log files in the following locations:

  * **Linux** : `/opt/CA/Directory/dxserver/logs/`
  * **Windows** : `C:\Program Files\CA\Directory\dxserver\logs\`



The log files follow naming patterns based on the DSA name (for example, `democorp_alarm`, `democorp_warn`, `democorp_trace`).

### Available log types

CA Directory generates the following log types:

  * **Alarm log** : Critical events (always enabled)
  * **Warn log** : Errors and warnings
  * **Trace log** : Detailed operation tracing
  * **Query log** : Detailed operation information with timestamps
  * **Summary log** : Operation summaries
  * **Connection log** : Connection and disconnection events
  * **Diagnostic log** : Rejected operations
  * **Statistics log** : Per-minute operational statistics
  * **Update log** : Add, modify, rename, and delete operations
  * **Time log** : Operation timing information



### Configure rsyslog on Linux

  1. Sign in to the CA Directory server as root or with sudo privileges.

  2. Install rsyslog if not already installed:
         
         sudo yum install rsyslog
         

Or for Debian/Ubuntu:
         
         sudo apt-get install rsyslog
         

  3. Create a new rsyslog configuration file for CA Directory:
         
         sudo nano /etc/rsyslog.d/ca-directory.conf
         

  4. Add the following configuration to forward CA Directory logs:
         
         # Load the imfile module for file monitoring
         module(load="imfile" PollingInterval="10")
         
         # Monitor CA Directory alarm logs
         input(type="imfile"
             File="/opt/CA/Directory/dxserver/logs/*_alarm*"
             Tag="ca-directory-alarm"
             Severity="error"
             Facility="local0")
         
         # Monitor CA Directory warn logs
         input(type="imfile"
             File="/opt/CA/Directory/dxserver/logs/*_warn*"
             Tag="ca-directory-warn"
             Severity="warning"
             Facility="local0")
         
         # Monitor CA Directory trace logs
         input(type="imfile"
             File="/opt/CA/Directory/dxserver/logs/*_trace*"
             Tag="ca-directory-trace"
             Severity="info"
             Facility="local0")
         
         # Monitor CA Directory query logs
         input(type="imfile"
             File="/opt/CA/Directory/dxserver/logs/*_query*"
             Tag="ca-directory-query"
             Severity="info"
             Facility="local0")
         
         # Monitor CA Directory connection logs
         input(type="imfile"
             File="/opt/CA/Directory/dxserver/logs/*_connection*"
             Tag="ca-directory-connection"
             Severity="info"
             Facility="local0")
         
         # Monitor CA Directory update logs
         input(type="imfile"
             File="/opt/CA/Directory/dxserver/logs/*_update*"
             Tag="ca-directory-update"
             Severity="info"
             Facility="local0")
         
         # Forward all CA Directory logs to Bindplane agent
         if $syslogtag contains 'ca-directory' then @@BINDPLANE_AGENT_IP:514
         & stop
         

  5. Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host:

     * If Bindplane agent is on the same server: `127.0.0.1`
     * If Bindplane agent is on a different server: Enter the IP address (for example, `192.168.1.100`)
**Note:** The `@@` prefix indicates TCP forwarding. Use `@` for UDP forwarding (for example, `@BINDPLANE_AGENT_IP:514`).
  6. Save the configuration file:

Press `Ctrl+O`, then `Enter`, then `Ctrl+X`

  7. Verify the rsyslog configuration syntax:
         
         sudo rsyslogd -N1
         

  8. Restart the rsyslog service:
         
         sudo systemctl restart rsyslog
         

  9. Verify rsyslog is running:
         
         sudo systemctl status rsyslog
         

  10. Check rsyslog logs for errors:
         
         sudo tail -f /var/log/messages
         




### Configure rsyslog on Windows

  1. Download and install rsyslog for Windows from the [rsyslog website](https://www.rsyslog.com/windows-agent/).

  2. Open the rsyslog configuration file:
         
         notepad "C:\Program Files\rsyslog\rsyslog.conf"
         

  3. Add the following configuration:
         
         # Load the imfile module for file monitoring
         module(load="imfile" PollingInterval="10")
         
         # Monitor CA Directory alarm logs
         input(type="imfile"
             File="C:\\Program Files\\CA\\Directory\\dxserver\\logs\\*_alarm*"
             Tag="ca-directory-alarm"
             Severity="error"
             Facility="local0")
         
         # Monitor CA Directory warn logs
         input(type="imfile"
             File="C:\\Program Files\\CA\\Directory\\dxserver\\logs\\*_warn*"
             Tag="ca-directory-warn"
             Severity="warning"
             Facility="local0")
         
         # Monitor CA Directory trace logs
         input(type="imfile"
             File="C:\\Program Files\\CA\\Directory\\dxserver\\logs\\*_trace*"
             Tag="ca-directory-trace"
             Severity="info"
             Facility="local0")
         
         # Forward all CA Directory logs to Bindplane agent
         if $syslogtag contains 'ca-directory' then @@BINDPLANE_AGENT_IP:514
         & stop
         

  4. Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host.

  5. Save the configuration file.

  6. Restart the rsyslog service:
         
         net stop rsyslog
         net start rsyslog
         




### Enable CA Directory logging

Ensure that the required log types are enabled in CA Directory:

  1. Edit the DSA configuration file:

     * **Linux** : `/opt/CA/Directory/dxserver/config/servers/democorp.dxc`
     * **Windows** : `C:\Program Files\CA\Directory\dxserver\config\servers\democorp.dxc`
**Note:** Replace `democorp` with your DSA name.
  2. Verify or add the following logging settings:
         
         set alarm-log = true;
             set warn-log = true;
             set trace-log = true;
             set query-log = true;
             set connection-log = true;
             set update-log = true;
         

  3. Save the configuration file.

  4. Restart the CA Directory DSA:

     * **Linux** :
           
           dxserver stop democorp
           dxserver start democorp
           

     * **Windows** :
           
           net stop "CA Directory DSA - democorp"
           net start "CA Directory DSA - democorp"
           




### Verify log forwarding

  1. Generate test activity in CA Directory by performing LDAP queries or authentication attempts.

  2. Check the Bindplane agent logs to verify logs are being received:

     * **Linux** :
           
           sudo journalctl -u observiq-otel-collector -f
           

     * **Windows** :
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           

  3. Sign in to the Google SecOps console and verify that CA Directory logs are appearing in the log viewer.




For more information about CA Directory logging, see the [Broadcom CA Directory documentation](https://techdocs.broadcom.com/us/en/symantec-security-software/identity-security/directory/14-1/administrating/monitor-the-directory/monitoring-with-log-files.html).

For detailed rsyslog configuration examples, see the [Broadcom Knowledge Base article on centralized logging](https://knowledge.broadcom.com/external/article/208528/ca-directory-centralized-logging.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
agent.ephemeral_id, logstash.irm_region, logstash.irm_environment, logstash.irm_site, host.os.name | additional.fields | Merged as labels with keys "ephemeral_id", "irm_region", "irm_environment", "irm_site", "os_name" respectively  
host.architecture | hardware.cpu_platform | Value copied directly  
logstash.process.host | intermediary.hostname | Value copied directly  
logstash.collect.timestamp | metadata.collected_timestamp | Parsed as timestamp using date filter  
msg | metadata.description | Value copied directly  
| metadata.event_type | Set to "STATUS_UPDATE"  
agent.type, agent.version | observer.application | Concatenated as "%{agent.type} %{agent.version}" if both not empty, else "%{agent.type}"  
agent.type, agent.id | observer.asset_id | Concatenated as "%{agent.type}: %{agent.id}"  
agent.hostname | observer.hostname | Value copied directly  
host.id | principal.asset.asset_id | Concatenated as "CA_LDAP:%{host.id}"  
hardware | principal.asset.hardware | Merged from hardware object  
host.hostname | principal.hostname | Value copied directly  
host.ip | principal.ip | Merged from host.ip array  
host.mac | principal.mac | Merged from host.mac array  
host.os.family | principal.platform | Set to "LINUX" if matches "(rhel|redhat)"  
host.os.kernel | principal.platform_patch_level | Value copied directly  
host.os.version | principal.platform_version | Value copied directly  
log.file.path | principal.process.file.full_path | Value copied directly  
syslog_severity | security_result.severity | Set to "INFORMATIONAL" if matches "(?i)(DEFAULT|DEBUG|INFO|NOTICE)", "ERROR" if matches "(?i)ERROR", "MEDIUM" if matches "(?i)WARNING", "HIGH" if matches "(?i)(CRITICAL|ALERT|EMERGENCY)"  
syslog_severity | security_result.severity_details | Value copied directly  
| metadata.product_name | Set to "CA_LDAP"  
| metadata.vendor_name | Set to "CA_LDAP"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-ldap-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
