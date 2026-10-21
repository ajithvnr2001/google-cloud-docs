---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/clam-av/
title: Collect ClamAV logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:21:08.859283+00:00
---

# Collect ClamAV logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/clam-av/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ClamAV logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ClamAV logs into Google Security Operations using the Bindplane agent.

ClamAV is an open-source antivirus engine designed for detecting trojans, viruses, malware, and other malicious threats. It provides command-line scanning, automatic signature database updates, and supports multiple file formats, including archives, executables, and documents. ClamAV operates as a local daemon (clamd) or command-line scanner (clamscan) on Linux, Unix, and Windows systems.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent host and the ClamAV server
  * If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
  * ClamAV installed and running on Linux endpoints
  * Root or sudo access to the ClamAV server and Bindplane agent host



## Get the Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get the Google SecOps customer ID

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

## Configure Bindplane agent to ingest syslog and send logs to Google SecOps

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
             chronicle/clamav:
                 compression: gzip
                 creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                 customer_id: 'YOUR_CUSTOMER_ID'
                 endpoint: malachiteingestion-pa.googleapis.com
                 log_type: CLAM_AV
                 raw_log_field: body
                 ingestion_labels:
                     env: production
         
         service:
             pipelines:
                 logs/clamav_to_chronicle:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/clamav
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on UDP port 514. If port 514 requires root privileges on Linux, use `0.0.0.0:1514` and configure rsyslog to forward to port 1514.
     * Exporter configuration:

       * `creds_file_path`: Full path to the ingestion authentication file:

         * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `customer_id`: Replace `YOUR_CUSTOMER_ID` with the customer ID obtained previously

       * `endpoint`: Regional endpoint URL:

         * **US** : `malachiteingestion-pa.googleapis.com`
         * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
         * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
         * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for a complete list
       * `log_type`: Set to `CLAM_AV` (exact match for the Google SecOps parser)

       * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)




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
           

    3. Check the logs for errors:
           
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
           

    3. Check the logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




## Configure ClamAV syslog forwarding

### Enable syslog logging in ClamAV

  1. Sign in to the Linux system running ClamAV with root or sudo privileges.
  2. Open the ClamAV daemon configuration file:
         
         sudo nano /etc/clamav/clamd.conf
         

**Note:** The configuration file location may vary by distribution. Common locations include `/etc/clamav/clamd.conf`, `/etc/clamd.conf`, or `/usr/local/etc/clamd.conf`.
  3. Find the line that reads `#LogSyslog yes` or `#LogSyslog true`.

  4. Remove the `#` comment character to enable syslog logging:
         
         LogSyslog yes
         

  5. Optional: Configure the syslog facility. Find the line `#LogFacility LOG_LOCAL6` and uncomment it:
         
         LogFacility LOG_LOCAL6
         

**Note:** The default facility is `LOG_LOCAL6`. You can change this to another facility such as `LOG_LOCAL0` through `LOG_LOCAL7` if needed.
  6. Optional: Enable additional logging options for more detailed logs:
         
         LogTime yes
         LogVerbose yes
         ExtendedDetectionInfo yes
         

     * `LogTime`: Adds timestamps to log messages
     * `LogVerbose`: Enables verbose logging with additional details
     * `ExtendedDetectionInfo`: Includes file size and hash with virus detections
  7. Save the file and exit:

Press `Ctrl+O`, then `Enter`, then `Ctrl+X`

  8. Restart the ClamAV daemon to apply the changes:
         
         sudo systemctl restart clamav-daemon
         

**Note:** The service name may vary by distribution. Try `clamav-daemon`, `clamd`, or `clamd@scan` if the above command fails.
  9. Verify the ClamAV daemon is running:
         
         sudo systemctl status clamav-daemon
         




### Configure rsyslog to forward ClamAV logs

  1. Create a new rsyslog configuration file for ClamAV forwarding:
         
         sudo nano /etc/rsyslog.d/30-clamav-forward.conf
         

**Note:** The filename starts with `30-` to ensure it loads after the main rsyslog configuration but before default rules.
  2. Add the following configuration to forward ClamAV logs to the Bindplane agent:
         
         # Forward ClamAV logs (LOG_LOCAL6 facility) to Bindplane agent
         if $syslogfacility-text == 'local6' then {
             action(
                 type="omfwd"
                 protocol="udp"
                 target="BINDPLANE_AGENT_IP"
                 port="514"
                 queue.type="linkedList"
                 queue.size="10000"
                 action.resumeRetryCount="100"
             )
             stop
         }
         

  3. Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host:

     * If Bindplane is installed on the same host as ClamAV, use `127.0.0.1`
     * If Bindplane is on a different host, use the IP address of that host (for example, `192.168.1.100`)
  4. If you configured Bindplane to listen on a different port (for example, `1514`), update the `port` parameter accordingly.

  5. Save the file and exit:

Press `Ctrl+O`, then `Enter`, then `Ctrl+X`

  6. Validate the rsyslog configuration syntax:
         
         sudo rsyslogd -N1
         

**Note:** This command checks for syntax errors. If there are no errors, you will see `rsyslogd: version X, config validation run (level 1), master config /etc/rsyslog.conf`.
  7. Restart rsyslog to apply the changes:
         
         sudo systemctl restart rsyslog
         

  8. Verify rsyslog is running:
         
         sudo systemctl status rsyslog
         




### Test the configuration

  1. Generate a test virus detection using the EICAR test file:
         
         cd /tmp
         echo 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > eicar.com
         

  2. Scan the test file with ClamAV:
         
         sudo clamdscan /tmp/eicar.com
         

  3. Verify the detection appears in syslog:
         
         sudo tail -f /var/log/syslog | grep clamd
         

You should see a log entry similar to:
         
         Jan 15 10:30:45 hostname clamd[1234]: /tmp/eicar.com: Win.Test.EICAR_HDB-1(44d88612fea8a8f36de82e1278abb02f:68) FOUND
         

  4. Check the Bindplane agent logs to verify that logs are being forwarded:
         
         sudo journalctl -u observiq-otel-collector -f
         

  5. Verify that logs are appearing in Google SecOps:

     1. Sign in to the Google SecOps console.
     2. Go to **Search > UDM Search**.
     3. Run a search query for ClamAV logs:
            
            metadata.log_type = "CLAM_AV"
            

  6. Clean up the test file:
         
         sudo rm /tmp/eicar.com
         




### Alternative configuration: Forward all syslog messages to Bindplane

If you want to forward all syslog messages (not just ClamAV) to Bindplane, use this simpler configuration:

  1. Edit the rsyslog configuration:
         
         sudo nano /etc/rsyslog.d/30-forward-all.conf
         

  2. Add the following configuration:
         
         # Forward all logs to Bindplane agent
         *.* action(
             type="omfwd"
             protocol="udp"
             target="BINDPLANE_AGENT_IP"
             port="514"
             queue.type="linkedList"
             queue.size="10000"
             action.resumeRetryCount="100"
         )
         

  3. Replace `BINDPLANE_AGENT_IP` with the appropriate IP address.

  4. Save, validate, and restart rsyslog as described in the previous steps.

**Note:** This configuration forwards all syslog messages to Bindplane, not just ClamAV logs. You may need to configure additional Bindplane pipelines and Google SecOps parsers for other log sources.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
parsed_msg.resource.labels.instance_id | observer.resource.id | Value copied directly  
parsed_msg.labels.compute.googleapis.com/resource_name | observer.resource.name | Value copied directly  
parsed_msg.resource.type, parsed_msg.labels.container.googleapis.com/stream | observer.resource.type | Concatenated from parsed_msg.resource.type and parsed_msg.labels.container.googleapis.com/stream with "/" separator  
parsed_msg.resource.labels.project_id, parsed_msg.resource.labels.cluster_name, parsed_msg.resource.labels.container_name | observer.hostname | Concatenated from parsed_msg.resource.labels.project_id, parsed_msg.resource.labels.cluster_name, and parsed_msg.resource.labels.container_name with "/" separators  
parsed_msg.resource.labels.container_name | observer.application | Value copied directly  
parsed_msg.labels.container.googleapis.com/namespace_name | observer.namespace | Value copied directly  
parsed_msg.resource.labels.zone | observer.location.country_or_region | Value copied directly  
parsed_msg.resource.labels.pod_id | observer.labels | Merged as key "pod_id" with value from parsed_msg.resource.labels.pod_id  
parsed_msg.resource.labels.project_id, parsed_msg.resource.labels.cluster_name, parsed_msg.resource.labels.container_name | principal.hostname | Concatenated from parsed_msg.resource.labels.project_id, parsed_msg.resource.labels.cluster_name, and parsed_msg.resource.labels.container_name with "/" separators  
file, _file_path | target.file.full_path | Value from file if extracted from grok pattern, else from _file_path if extracted from alternative grok pattern  
threat | security_result.threat_name | Value copied directly  
total_files, _outcome, threat | security_result.summary | Set to "%{total_files} infected files found." if num_files extracted, else "File scanned. (%{_outcome})" if _outcome extracted, else "Threat %{threat} signature found." if threat not empty  
category | security_result.category | Value copied directly (set to "SOFTWARE_MALICIOUS" if threat not empty)  
action | security_result.action | Value copied directly (set to "BLOCK" if threat not empty, else "ALLOW" if _outcome extracted)  
parsed_msg.insertId | metadata.product_log_id | Value copied directly  
parsed_msg.logName | metadata.description | Value copied directly  
| metadata.event_type | Set to "SCAN_FILE" if threat found or file scanned, else "STATUS_UPDATE" if infected files count extracted  
| metadata.product_name | Set to "CLAMAV"  
| metadata.vendor_name | Set to "Cisco Systems"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
