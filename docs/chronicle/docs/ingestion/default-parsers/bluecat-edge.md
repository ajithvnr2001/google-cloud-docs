---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-edge/
title: Collect BlueCat Edge DNS Resolver logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:18.424740+00:00
---

# Collect BlueCat Edge DNS Resolver logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-edge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect BlueCat Edge DNS Resolver logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest BlueCat Edge DNS Resolver logs to Google Security Operations using the Bindplane agent.

BlueCat Edge DNS Resolver is a DNS security and management solution that generates logs for DNS queries, responses, and threat detection events. The parser normalizes fields and maps them to the Unified Data Model (UDM), handling both JSON and non-JSON log formats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the BlueCat BDDS server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the BlueCat BDDS web UI



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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/bluecat_edge:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: BLUECAT_EDGE
            raw_log_field: body
        
        service:
          pipelines:
            logs/bluecat_edge_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/bluecat_edge
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
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
          chronicle/bluecat_edge:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BLUECAT_EDGE
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
             




## Configure syslog on BlueCat Edge DNS Resolver

  1. Sign in to the **BDDS** web UI.
  2. Go to **Configuration > Servers tab**.
  3. Select the **name** of a **BDDS** to open the **Details tab** for the server.
  4. Click the **server name menu > Service Configuration**.
  5. Click **Service Type > Syslog**.
  6. Provide the following configuration details: 
     * Select the **ISO 8601 Timestamp** checkbox to use the ISO 8601 timestamp format for locally logged messages.
     * **Server** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number.
     * **Level** : Select **Informational**.
     * Select the **Use RFC 5424 Syslog Protocol** checkbox to use the RFC 5424 syslog protocol for syslog messages.
     * Select the **ISO 8601 Timestamp** checkbox to use the ISO 8601 timestamp format for syslog messages redirected to a remote syslog server.
     * Under **Service Type** , select **DNS** , **DHCP** , and **All Other Services**.
     * **Transport** : Select **UDP**.
     * Click **Add**.
  7. Click **Update**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
answer.domainName | network.dns.answers.name | The domain name from the `answer` section of the DNS response. The trailing `.` is removed.  
answer.recordTypeId | network.dns.answers.type | The record type ID from the `answer` section of the DNS response, converted to an unsigned integer.  
answer.ttl | network.dns.answers.ttl | The Time to Live (TTL) value from the `answer` section of the DNS response, converted to an unsigned integer.  
customerId | target.user.userid | The customer ID from the log, representing the user who initiated the DNS request.  
domain.domainName | network.dns.authority.data | The domain name from the `authority` or `additional` sections of the DNS response. The trailing `.` is removed.  
hostname | principal.hostname | The hostname extracted from the `Host` header in the raw log, only if the log is not in JSON format.  
method | network.http.method | The HTTP method extracted from the raw log, only if the log is not in JSON format.  
parentDomain | principal.administrative_domain | The parent domain of the queried DNS name. The trailing `.` is removed.  
port | principal.port | The port number extracted from the `Host` header in the raw log, only if the log is not in JSON format, converted to an integer.  
question.domainName | network.dns.questions.name | The domain name from the `question` section of the DNS request. The trailing `.` is removed.  
question.questionTypeId | network.dns.questions.type | The question type ID from the `question` section of the DNS request, converted to an unsigned integer.  
responseData.header.aa | network.dns.authoritative | Whether the DNS response is authoritative, extracted from the `responseData` section.  
responseData.header.id | network.dns.id | The DNS message ID, extracted from the `responseData` section, converted to an unsigned integer.  
responseData.header.opcode | network.dns.opcode | The DNS message opcode, extracted from the `responseData` section, converted to an unsigned integer.  
responseData.header.ra | network.dns.recursion_available | Whether recursion is available, extracted from the `responseData` section.  
responseData.header.rcode | network.dns.response_code | The DNS response code, extracted from the `responseData` section, converted to an unsigned integer.  
responseData.header.rd | network.dns.recursion_desired | Whether recursion is selected, extracted from the `responseData` section.  
responseData.header.tc | network.dns.truncated | Whether the DNS message is truncated, extracted from the `responseData` section.  
servicePointId | additional.fields.value.string_value | The service point ID from the log.  
siteId | additional.fields.value.string_value | The site ID from the log.  
socketProtocol | network.ip_protocol | The network protocol used for the DNS request (TCP or UDP).  
sourceAddress | principal.ip | The IP address of the DNS client.  
sourcePort | principal.port | The port number of the DNS client, converted to an integer.  
threat.indicators | security_result.category_details | The indicators associated with a detected threat.  
threat.type | security_result.threat_name | The type of detected threat.  
time | metadata.event_timestamp.seconds | The timestamp of the DNS event, extracted from the `time` field and converted from milliseconds to seconds.  
User-Agent | network.http.user_agent | The user agent string extracted from the raw log, only if the log is not in JSON format.  
| additional.fields.key | `servicePointId` or `siteId` or `Content-Type` or `Content-Length`, depending on the content of the raw log.  
| metadata.event_type | The event type, set to `NETWORK_DNS` if a DNS question is present, otherwise set to `GENERIC_EVENT`.  
| metadata.log_type | The log type, always set to `BLUECAT_EDGE`.  
| network.application_protocol | The application protocol, set to `DNS` if a DNS question is present, otherwise set to `HTTP` if an HTTP method is extracted, or left empty.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
