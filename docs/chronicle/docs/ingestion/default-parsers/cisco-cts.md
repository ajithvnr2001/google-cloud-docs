---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cts/
title: Collect Cisco CTS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:40:40.267000+00:00
---

# Collect Cisco CTS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco CTS logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco CTS logs to Google Security Operations using Bindplane agent.

Cisco TelePresence System (CTS) refers to legacy video conferencing hardware endpoints including CTS 500, CTS 1000, CTS 1100, CTS 1300, CTS 3000, CTS 3200, and TX series systems. These immersive telepresence room systems provide high-definition video conferencing capabilities and are managed through Cisco Unified Communications Manager (CUCM). The systems generate syslog messages for system operations, call activities, and troubleshooting.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Cisco TelePresence System
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to Cisco Unified Communications Manager (CUCM)
  * Administrative access to the Cisco TelePresence System Administration interface
  * Network connectivity from CTS codec to Bindplane agent on UDP port 514 (or configured port)



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * Linux:
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
             udplog:
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/cisco_cts:
                 compression: gzip
                 creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                 customer_id: 'YOUR_CUSTOMER_ID'
                 endpoint: malachiteingestion-pa.googleapis.com
                 log_type: CISCO_CTS
                 raw_log_field: body
         
         service:
             pipelines:
                 logs/cts_to_chronicle:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/cisco_cts
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * The receiver uses `udplog` for UDP syslog (standard for CTS devices)
       * `listen_address` is set to `0.0.0.0:514` to listen on all interfaces on UDP port 514
       * For Linux systems running as non-root, change port to `1514` or higher
     * Exporter configuration:

       * `creds_file_path`: Full path to ingestion authentication file: 
         * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `customer_id`: Replace `YOUR_CUSTOMER_ID` with your `customer ID`. For details, see Get Google SecOps customer ID.
       * `endpoint`: Regional endpoint URL: 
         * **US** : `malachiteingestion-pa.googleapis.com`
         * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
         * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
         * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
       * `log_type`: Set to `CISCO_CTS` (exact match required)



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
           




## Configure Cisco CTS syslog forwarding

Cisco TelePresence System (CTS) syslog forwarding is configured through Cisco Unified Communications Manager (CUCM). The External Syslog Address must be configured in the Product Specific Configuration Layout for each CTS device.

### Configure external syslog address in CUCM

  1. Sign in to the **Cisco Unified Communications Manager Administration** interface using a web browser.
  2. Go to **Device > Phone**.
  3. Use the search function to locate your Cisco TelePresence System device.
  4. Click on the device name to open the **Phone Configuration** window.
  5. Scroll down to the **Product Specific Configuration Layout** section.
  6. Locate the **External SYSLOG Address** field.
  7. In the **External SYSLOG Address** field, enter the syslog server address in one of the following formats:

     * IP address only: `192.168.1.100` (uses default port 514)
     * IP address with port: `192.168.1.100:514`
     * Hostname only: `bindplane-server.example.com` (uses default port 514)
     * Hostname with port: `bindplane-server.example.com:1514`
**Note:** The IP address or hostname should point to the Bindplane agent host. The port must match the port configured in the Bindplane agent `config.yaml` file (default is 514). Maximum field length is 60 characters.
  8. Click **Save** at the bottom of the page to save the configuration.

  9. Click **Apply Config** to apply the changes to the device.

**Note:** The system will display a message indicating that the configuration is being applied. Wait for the process to complete.
  10. Click **Reset** or **Restart** to restart the CTS device and activate the syslog forwarding.

**Note:** During the restart, the CTS device will be unavailable for calls. Schedule this restart during a maintenance window.



### Verify syslog configuration on CTS device

  1. Open a web browser and navigate to the CTS Administration interface at `https://<CTS-IP-ADDRESS>`.
  2. Log in with the SSH admin username and password configured in CUCM.
  3. Go to **Configuration > Network Settings**.
  4. Verify that the **Syslog Address** field displays the IP address or hostname of your Bindplane agent.

**Note:** This field is read-only and reflects the value configured in CUCM.



### Configure syslog for multiple CTS devices

If you have multiple CTS devices, repeat the configuration steps for each device:

  1. In CUCM, go to **Device > Phone**.
  2. Search for and select each CTS device.
  3. Configure the **External SYSLOG Address** field in the **Product Specific Configuration Layout** section.
  4. Save and apply the configuration for each device.
  5. Restart each device to activate syslog forwarding.



### Verify syslog messages are being received

  1. Check the Bindplane agent logs to verify syslog messages are being received:

     * Linux:
           
           sudo journalctl -u observiq-otel-collector -f | grep -i cisco
           

     * Windows:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log" | findstr /i cisco
           

  2. Sign in to the Google SecOps console.

  3. Go to **Search** and run a search query for recent CTS logs:
         
         metadata.log_type = "CISCO_CTS"
         

  4. Verify that logs are appearing in the search results with recent timestamps.




### Syslog message format

Cisco TelePresence System sends syslog messages in RFC 3164 (BSD syslog) format. Messages include:

  * System operation (sysop) log messages for call activities, video/audio events, and system operations
  * Facility code: Varies by message type
  * Default port: UDP 514
  * Message storage: Up to 20 rotating log files on the CTS device



### Troubleshooting syslog forwarding

If syslog messages are not being received:

  1. Verify network connectivity from CTS codec to Bindplane agent:
         
         ping <BINDPLANE_AGENT_IP>
         

  2. Verify firewall rules allow UDP traffic on port 514 (or configured port) from CTS IP addresses to Bindplane agent.

  3. Check that the External SYSLOG Address is correctly configured in CUCM Product Specific Configuration Layout.

  4. Verify the CTS device has been restarted after applying the syslog configuration.

  5. Check CTS Administration interface logs at **Troubleshooting > Log Files** for any syslog-related errors.

  6. Verify the Bindplane agent is listening on the correct port:

     * Linux:
           
           sudo netstat -ulnp | grep 514
           

     * Windows:
           
           netstat -an | findstr :514
           




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
AuditDetails, data2 | security_result.description | Value from AuditDetails if not empty, else data2  
ClientAddress, LoginFrom | principal.ip | Value from ClientAddress if not empty and not an IP address, else LoginFrom  
EventType | metadata.product_event_type | Value copied directly  
logType | metadata.description | Value copied directly  
severity | security_result.severity | Set to INFORMATIONAL if severity in [6,7]; LOW if 5; MEDIUM if 4; ERROR if 3; HIGH if 2; else CRITICAL  
logType, EventStatus | security_result.action | Set to ALLOW if logType == AuthenticationSucceeded or EventStatus == Success  
EventType, logType | metadata.event_type | Set to USER_RESOURCE_ACCESS if EventType == UserAccess; USER_LOGIN if EventType == UserLogging or logType matches LOGIN; USER_RESOURCE_UPDATE_CONTENT if EventType in [UserRoleMembershipUpdate, GeneralConfigurationUpdate]; else GENERIC_EVENT  
AppID | principal.application | Value copied directly  
NodeID | target.hostname | Value copied directly  
process_id | principal.process.pid | Value copied directly  
ResourceAccessed | target.resource.name | Value copied directly  
UserID | principal.user.userid | Value copied directly  
| metadata.product_name | Set to "CISCO_CTS"  
| metadata.vendor_name | Set to "CISCO"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
