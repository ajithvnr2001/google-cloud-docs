---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hadoop/
title: Collect Apache Hadoop logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:24.171454+00:00
---

# Collect Apache Hadoop logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hadoop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Apache Hadoop logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Apache Hadoop logs to Google Security Operations using the Bindplane agent. The parser first extracts fields from raw Hadoop logs using Grok patterns based on common Hadoop log formats. Then, it maps the extracted fields to the corresponding fields in the Unified Data Model (UDM) schema, performs data type conversions, and enriches the data with additional context.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Apache Hadoop cluster configuration files



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

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

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
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'HADOOP'
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
     * Replace `<CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'HADOOP'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Apache Hadoop

Apache Hadoop uses **Log4j** for logging. Configure the appropriate **Syslog appender** based on your Log4j version so that Hadoop daemons (NameNode, DataNode, ResourceManager, NodeManager, etc.) forward logs directly to your syslog receiver (Bindplane host). Log4j is configured via files (no web UI).

### Option 1: Log4j 1.x configuration

  1. Locate the **log4j.properties** file (typically in `$HADOOP_CONF_DIR/log4j.properties`).
  2. Add the following **SyslogAppender** configuration to the file:
         
         # Syslog appender (UDP example)
         log4j.appender.SYSLOG=org.apache.log4j.net.SyslogAppender
         log4j.appender.SYSLOG.SyslogHost=<BINDPLANE_HOST_IP>:514
         log4j.appender.SYSLOG.Facility=LOCAL0
         log4j.appender.SYSLOG.FacilityPrinting=true
         log4j.appender.SYSLOG.layout=org.apache.log4j.PatternLayout
         log4j.appender.SYSLOG.layout.ConversionPattern=%d{ISO8601} level=%p logger=%c thread=%t msg=%m%n
         
         # Example: send NameNode logs to syslog
         log4j.logger.org.apache.hadoop.hdfs.server.namenode=INFO,SYSLOG
         log4j.additivity.org.apache.hadoop.hdfs.server.namenode=false
         
         # Or attach to root logger to send all Hadoop logs
         # log4j.rootLogger=INFO, SYSLOG
         

  3. Replace `<BINDPLANE_HOST_IP>` with the IP address of your Bindplane host.

  4. Save the file.

  5. **Restart Hadoop daemons** to apply the configuration changes.




### Option 2: Log4j 2.x configuration

  1. Locate the **log4j2.xml** file (typically in `$HADOOP_CONF_DIR/log4j2.xml`).
  2. Add the following **Syslog appender** configuration to the file:
         
         <Configuration status="WARN">
           <Appenders>
             <!-- UDP example; for TCP use protocol="TCP" -->
             <Syslog name="SYSLOG" format="RFC 5424"
                     host="<BINDPLANE_HOST_IP>"
                     port="514"
                     protocol="UDP"
                     facility="LOCAL0"
                     appName="hadoop"
                     enterpriseNumber="18060"
                     mdcId="mdc">
               <PatternLayout pattern="%d{ISO8601} level=%p logger=%c thread=%t msg=%m %X%n"/>
             </Syslog>
           </Appenders>
         
           <Loggers>
             <!-- Send NameNode logs to syslog -->
             <Logger name="org.apache.hadoop.hdfs.server.namenode" level="info" additivity="false">
               <AppenderRef ref="SYSLOG"/>
             </Logger>
         
             <!-- Or send all Hadoop logs -->
             <Root level="info">
               <AppenderRef ref="SYSLOG"/>
             </Root>
           </Loggers>
         </Configuration>
         

  3. Replace `<BINDPLANE_HOST_IP>` with the IP address of your Bindplane host.

  4. Save the file.

  5. **Restart Hadoop daemons** to apply the configuration changes.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
allowed | security_result.action | If "false", action is "BLOCK". If "true", action is "ALLOW".  
auth_type | additional.fields.key = "auth_type", additional.fields.value.string_value | Extracted from "ugi" field using grok pattern "%{DATA:suser}@.*auth:%{WORD:auth_type}". Parentheses and "auth:" are removed.  
call | additional.fields.key = "Call#", additional.fields.value.string_value | Directly mapped.  
call_context | additional.fields.key = "callerContext", additional.fields.value.string_value | Directly mapped.  
cliIP | principal.ip | Mapped only when "json_data" field exists and is successfully parsed as JSON.  
cmd | principal.process.command_line | Directly mapped.  
cluster_name | target.hostname | Used as target hostname if present.  
day | metadata.event_timestamp.seconds | Used with month, year, hours, minutes, and seconds to construct event_timestamp.  
description | metadata.description | Directly mapped.  
driver | additional.fields.key = "driver", additional.fields.value.string_value | Directly mapped.  
dst | target.ip OR target.hostname OR target.file.full_path | If successfully parsed as IP, mapped to target IP. If the value starts with "/user", mapped to target file path. Otherwise, mapped to target hostname.  
dstport | target.port | Directly mapped and converted to integer.  
enforcer | security_result.rule_name | Directly mapped.  
event_count | additional.fields.key = "event_count", additional.fields.value.string_value | Directly mapped and converted to string.  
fname | src.file.full_path | Directly mapped.  
hours | metadata.event_timestamp.seconds | Used with month, day, year, minutes, and seconds to construct event_timestamp.  
id | additional.fields.key = "id", additional.fields.value.string_value | Directly mapped.  
ip | principal.ip | Mapped to principal IP after removing any leading "/" character.  
json_data |  | Parsed as JSON. Extracted fields are mapped to corresponding UDM fields.  
logType | additional.fields.key = "logType", additional.fields.value.string_value | Directly mapped.  
message |  | Used for extracting various fields using grok patterns.  
method | network.http.method | Directly mapped.  
minutes | metadata.event_timestamp.seconds | Used with month, day, year, hours, and seconds to construct event_timestamp.  
month | metadata.event_timestamp.seconds | Used with day, year, hours, minutes, and seconds to construct event_timestamp.  
observer | observer.hostname OR observer.ip | If successfully parsed as IP, mapped to observer IP. Otherwise, mapped to observer hostname.  
perm | additional.fields.key = "perm", additional.fields.value.string_value | Directly mapped.  
policy | security_result.rule_id | Directly mapped and converted to string.  
product | metadata.product_name | Directly mapped.  
product_event | metadata.product_event_type | Directly mapped. If "rename", the "dst" field is mapped to "target.file.full_path".  
proto | network.application_protocol | Directly mapped and converted to uppercase if it's not "webhdfs".  
reason | security_result.summary | Directly mapped.  
repo | additional.fields.key = "repo", additional.fields.value.string_value | Directly mapped.  
resType | additional.fields.key = "resType", additional.fields.value.string_value | Directly mapped.  
result | additional.fields.key = "result", additional.fields.value.string_value | Directly mapped and converted to string.  
Retry | additional.fields.key = "Retry#", additional.fields.value.string_value | Directly mapped.  
seconds | metadata.event_timestamp.seconds | Used with month, day, year, hours, and minutes to construct event_timestamp.  
seq_num | additional.fields.key = "seq_num", additional.fields.value.string_value | Directly mapped and converted to string.  
severity | security_result.severity | Mapped to different severity levels based on the value: "INFO", "Info", "info" -> "INFORMATIONAL"; "Low", "low", "LOW" -> "LOW"; "error", "Error", "WARN", "Warn" -> "MEDIUM"; "High", "high", "HIGH" -> "HIGH"; "Critical", "critical", "CRITICAL" -> "CRITICAL".  
shost | principal.hostname | Used as principal hostname if different from "src".  
src | principal.ip OR principal.hostname OR observer.ip | If successfully parsed as IP, mapped to principal and observer IP. Otherwise, mapped to principal hostname.  
srcport | principal.port | Directly mapped and converted to integer.  
summary | security_result.summary | Directly mapped.  
suser | principal.user.userid | Directly mapped.  
tags | additional.fields.key = "tags", additional.fields.value.string_value | Directly mapped.  
thread | additional.fields.key = "thread", additional.fields.value.string_value | Directly mapped.  
tip | target.ip | Directly mapped.  
ugi | target.hostname | Used as target hostname if "log_data" field doesn't contain "·".  
url | target.url | Directly mapped.  
vendor | metadata.vendor_name | Directly mapped.  
version | metadata.product_version | Directly mapped.  
year | metadata.event_timestamp.seconds | Used with month, day, hours, minutes, and seconds to construct event_timestamp.  
N/A | metadata.event_type | Set to "NETWORK_CONNECTION" by default. Changed to "STATUS_UPDATE" if no target is identified.  
N/A | metadata.log_type | Set to "HADOOP".  
N/A | security_result.alert_state | Set to "ALERTING" if severity is "HIGH" or "CRITICAL".  
N/A | is_alert | Set to "true" if severity is "HIGH" or "CRITICAL".  
N/A | is_significant | Set to "true" if severity is "HIGH" or "CRITICAL".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hadoop-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
