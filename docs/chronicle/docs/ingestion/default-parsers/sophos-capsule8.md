---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-capsule8/
title: Collect Sophos Capsule8 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:50.278721+00:00
---

# Collect Sophos Capsule8 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-capsule8/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Sophos Capsule8 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Sophos Capsule8 (Linux Sensor) logs to Google Security Operations using the Bindplane agent. Sophos Linux Sensor (formerly Capsule8) provides runtime protection for Linux workloads, containers, and Kubernetes environments by detecting and responding to threats at the kernel level using eBPF technology. Alerts and telemetry data are sent to Sophos Central, where they can be exported to a SIEM using the Sophos Central SIEM Integration script.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * An additional Windows, Linux, or macOS machine capable of continuously running Python 3.7 or later
  * Network connectivity between the Bindplane agent and the machine running the Sophos SIEM integration script
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Sophos Central Admin console
  * Sophos Linux Sensor (Capsule8) deployed on your Linux systems
  * Sophos Linux Sensor version 5.5.2.22 or later
  * One of the following Sophos Central licenses: 
    * Intercept X Advanced for Server with XDR
    * Central Managed Detection and Response Essential Server
    * Central Managed Detection and Response Complete Server



## Configure Sophos Linux Sensor to export alerts to Sophos Central

Before configuring the SIEM integration, you must first configure Sophos Linux Sensor to send alert data to Sophos Central.

### Find your Sophos Central MCS URL

  1. Sign in to **Sophos Central**.
  2. Click your account name, and then click **Support settings**.
  3. Look for the line that starts with **This account is located in** to identify your geographical region.
  4. Use the following table to find your MCS URL based on your region:

Region | MCS URL  
---|---  
United States (Oregon) | `mcs2-cloudstation-us-west-2.prod.hydra.sophos.com`  
United States (Ohio) | `mcs2-cloudstation-us-east-2.prod.hydra.sophos.com`  
Ireland | `mcs2-cloudstation-eu-west-1.prod.hydra.sophos.com`  
Germany | `mcs2-cloudstation-eu-central-1.prod.hydra.sophos.com`  
Canada | `mcs2.stn100yul.ctr.sophos.com`  
Australia | `mcs2.stn100syd.ctr.sophos.com`  
Asia Pacific (Tokyo) | `mcs2.stn100hnd.ctr.sophos.com`  
South America (Sao Paulo) | `mcs2.stn100gru.ctr.sophos.com`  
**Note:** If your region is not listed, use `mcs2.stn100bom.ctr.sophos.com` as your MCS URL.



### Configure Sophos Linux Sensor alert output

  1. Open `/etc/sophos/runtimedetections.yaml` in a text editor on the Linux host where Sophos Linux Sensor is installed.
  2. Add or update the following configuration, replacing the placeholder values with your actual Sophos Central details:
         
         send_labs_telemetry: true
         endpoint_telemetry_enabled: true
         cloud_meta: auto
         
         # Set your Sophos Central tenant ID
         customer_id: "{TENANT_ID}"
         
         mcs:
           token: "{LINUX_REPO_API_KEY}"
           url: "{MCS_URL}"
           enabled: true
         

     * `{TENANT_ID}`: Your Sophos Central tenant ID.
     * `{LINUX_REPO_API_KEY}`: Your SLS package repository API token.
     * `{MCS_URL}`: The MCS URL for your region from the table above.
  3. Save the file and exit.

  4. Restart the Sophos Linux Sensor service:
         
         sudo systemctl restart sophoslinuxsensor
         




### Configure Sophos Linux Sensor to send metaevents to Data Lake (optional)

Starting in version 5.11.0, Sophos Linux Sensor supports sending event data to the Sophos Data Lake for additional telemetry.

  1. Open `/etc/sophos/runtimedetections.yaml` in a text editor.
  2. Add the following configuration:
         
         investigations:
           reporting_interval: 5s
           zeromq:
             topics:
             - process_events: running_processes_linux_events
               audit_user_msg: user_events_linux
           sinks:
           - backend: mcs
             name: "mcs"
             type: mcs
           flight_recorder:
             enabled: true
             tables:
             - name: "process_events"
               enabled: true
               rows: 1000
               filter:
               - match eventType == "PROCESS_EVENT_TYPE_EXEC"
               - match eventType == "BASELINE_TASK"
               - default ignore
             - name: "audit_user_msg"
               enabled: true
               rows: 1000
               filter:
               - ignore programName == "cron"
               - ignore processPid == 1
               - default match
         

  3. Save the file and exit.

  4. Restart the Sophos Linux Sensor service:
         
         sudo systemctl restart sophoslinuxsensor
         




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
          chronicle/sophos_capsule8:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id'
            endpoint: chronicle.googleapis.com
            log_type: SOPHOS_CAPSULE8
            raw_log_field: body
            ingestion_labels:
        
        service:
          pipelines:
            logs/sophos_capsule8_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/sophos_capsule8
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces. Port `514` is the standard syslog port.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Google SecOps Customer ID.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/sophos_capsule8:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SOPHOS_CAPSULE8
            raw_log_field: body
            ingestion_labels:
        


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
             




## Configure Sophos Central API credentials

  1. Sign in to **Sophos Central Admin**.
  2. Go to **Global Settings > API Credentials Management**.
  3. Click **Add Credential**.
  4. Enter a name and an optional description for the credential, and then click **Add**.
  5. Copy the **Client ID** and **Client Secret**. Store them securely.

**Note:** The client secret is only shown once. If you lose it, you must create a new credential.



## Install and configure the Sophos Central SIEM Integration script

### Install Python

  1. Download and install Python 3.7 or later from the [Python website](https://www.python.org).
  2. On Windows, check the box **Add Python to PATH** during installation.
  3. Verify the installation by running:
         
         python3 --version
         




### Download the Sophos Central SIEM Integration script

  1. Download the latest release from the [Sophos Central SIEM Integration GitHub Repository](https://github.com/sophos/Sophos-Central-SIEM-Integration/archive/v2.1.0.zip).
  2. Extract the ZIP file to a directory on the machine where the script will run.



### Configure the SIEM Integration script

  1. In the extracted directory, copy `config.ini.sample` to `config.ini`.
  2. Open `config.ini` in a text editor.
  3. Under the `[login]` section, enter the API credentials: 
     * `client_id`: Enter the Client ID from Sophos Central.
     * `client_secret`: Enter the Client Secret from Sophos Central.
  4. Set the output format: 
     * `format`: Enter `json`.
  5. Set the output destination to syslog: 
     * `filename`: Enter `syslog`.
  6. Set the endpoint type: 
     * `endpoint`: Enter `all` to collect both events and alerts.
  7. Configure the syslog properties: 
     * `address`: Enter the IP address and port of the Bindplane agent (for example, `192.168.1.100:514`).
     * `facility`: Enter `daemon`.
     * `socktype`: Enter `udp`.
  8. Save and close the file.

**Note:** For a complete list of configuration options, refer to the [Sophos Central SIEM Integration README](https://github.com/sophos/Sophos-Central-SIEM-Integration).



## Run the SIEM Integration script

  1. Open a terminal or command prompt and navigate to the script directory.
  2. Run the script:
         
         python3 siem.py
         

**Note:** The script fetches the last 12 hours of events on its initial run. A maximum of 24 hours of historical data can be retrieved. On subsequent runs, the script picks up from where it left off using a state file.



## Automate the SIEM Integration script

### Windows (Task Scheduler)

  1. Open **Task Scheduler** from the Start menu.
  2. Click **Create Task**.
  3. In the **General** tab: 
     * **Name** : Enter `Sophos Capsule8 SIEM Export`.
  4. In the **Triggers** tab: 
     1. Click **New**.
     2. Set the task to repeat every **5 minutes** for a duration of **Indefinitely**.
  5. In the **Actions** tab: 
     1. Click **New** and select **Start a program**.
     2. In the **Program/script** field, enter the path to `python.exe`.
     3. In the **Add arguments** field, enter the full path to `siem.py`.
     4. In the **Start in** field, enter the directory containing `siem.py`.
  6. Click **OK** to save the task.



### Linux or macOS (cron)

  1. Open a terminal and edit the crontab:
         
         crontab -e
         

  2. Add the following line to run the script every 5 minutes:
         
         */5 * * * * cd /path/to/Sophos-Central-SIEM-Integration && /usr/bin/python3 siem.py
         

**Note:** Replace `/path/to/Sophos-Central-SIEM-Integration` with the actual path to the extracted script directory.
  3. Save and exit the editor.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_network_interface_eth0_addr_0` | `principal.ip` | Merged  
`_label_container_id` | `principal.labels` | Merged  
`_label_container_name` | `principal.labels` | Merged  
`_label_image_id` | `principal.labels` | Merged  
`_label_image_name` | `principal.labels` | Merged  
`_label_kubernetes_namespace` | `principal.labels` | Merged  
`_label_kubernetes_pod` | `principal.labels` | Merged  
`_label_maintainer` | `principal.labels` | Merged  
`_process_labels` | `principal.labels` | Merged  
`metadata.network_interface_eth0_hardware_addr` | `principal.mac` | Merged  
`_security_result` | `security_result` | Merged  
N/A | `metadata.gcp_instance_zone` | Constant: `^.*?zones.(?P<_zone>.*)`  
N/A | `metadata.network_interface_eth0_addr_0` | Constant: `^(?P<_network_interface_eth0_addr_0>.*?)/`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
