---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-switch/
title: Collect Fortinet Switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:25:39.186379+00:00
---

# Collect Fortinet Switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet Switch logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how you can ingest Fortinet Switch logs to Google Security Operations using Bindplane agent.

Fortinet Switch is a line of secure, high-performance Ethernet switches designed for enterprise networks. FortiSwitch provides Layer 2 and Layer 3 switching capabilities, VLAN support, link aggregation, Power over Ethernet (PoE), and integrated security features. FortiSwitch units can operate in standalone mode or be managed by FortiGate firewalls via FortiLink.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with systemd.
  * Network connectivity between Bindplane agent and Fortinet Switch.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Fortinet Switch management console or FortiGate console (for managed switches).
  * Fortinet Switch running FortiSwitchOS 7.0 or later.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agent**.
  3. Click **Download** to download the **ingestion authentication file**.
  4. Save the file securely on the system where Bindplane agent will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install Bindplane agent

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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

**Linux:**
    
    
    sudo nano /etc/bindplane-agent/config.yaml
    

**Windows:**
    
    
    notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
    

### Edit the configuration file

Replace the entire contents of `config.yaml` with the following configuration:
    
    
    receivers:
        udplog:
        listen_address: "0.0.0.0:514"
    
    exporters:
        chronicle/fortiswitch:
        compression: gzip
        creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
        customer_id: 'YOUR_CUSTOMER_ID'
        endpoint: malachiteingestion-pa.googleapis.com
        log_type: FORTINET_SWITCH
        raw_log_field: body
        ingestion_labels:
            env: production
    
    service:
        pipelines:
        logs/fortiswitch_to_chronicle:
            receivers:
            - udplog
            exporters:
            - chronicle/fortiswitch
    

### Configuration parameters

Replace the following placeholders:

**Receiver configuration:**

  * The receiver is configured to listen on UDP port 514 for syslog messages from Fortinet Switch.
  * To listen on all interfaces, use `0.0.0.0:514`.
  * To use a non-privileged port on Linux, change to `0.0.0.0:1514` and configure Fortinet Switch to send to port 1514.



**Exporter configuration:**

  * `creds_file_path`: Full path to ingestion authentication file: 
    * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * `customer_id`: Customer ID from the previous step.
  * `endpoint`: Regional endpoint URL: 
    * **US** : `malachiteingestion-pa.googleapis.com`
    * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
    * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
    * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list.
  * `log_type`: Must be exactly `FORTINET_SWITCH`.
  * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`).



### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`.
  * **Windows** : Click **File > Save**.



## Restart Bindplane agent to apply the changes

  * Linux
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * Windows

Choose one of the following options: 

    * Using Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Using Services console:

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Fortinet Switch syslog forwarding

Configure Fortinet Switch to send logs to the Bindplane agent. The configuration steps differ depending on whether the switch is standalone or managed by FortiGate.

### For standalone FortiSwitch (GUI configuration)

  1. Sign in to the FortiSwitch web interface.
  2. Go to **Log > Config**.
  3. Under **Syslog** , select **Enable**.
  4. Select the severity of events to log (for example, **Information** or higher).
  5. In the **Server** field, enter the IP address or fully qualified domain name of the Bindplane agent host.
  6. In the **Port** field, enter `514` (or the port configured in the Bindplane agent).
  7. In the **Facility** dropdown, select **local7**.
  8. Click **Apply**.



### For standalone FortiSwitch (CLI configuration)

  1. Sign in to the FortiSwitch CLI via SSH or console.
  2. Enter the following commands:
         
         config log syslogd setting
             set status enable
             set server <BINDPLANE_AGENT_IP>
             set port 514
             set facility local7
         end
         
         config log syslogd filter
             set severity information
         end
         

Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.

  3. Verify the configuration:
         
         show log syslogd setting
         




### For FortiSwitch managed by FortiGate

When FortiSwitch is managed by FortiGate, configure syslog forwarding from the FortiGate CLI.

  1. Sign in to the FortiGate CLI via SSH or console.
  2. Enter the following commands to configure remote syslog for managed FortiSwitch:
         
         config switch-controller remote-log
             edit "chronicle-syslog"
                 set status enable
                 set server <BINDPLANE_AGENT_IP>
                 set port 514
                 set severity information
                 set facility local7
             next
         end
         

Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.

  3. Verify the configuration:
         
         show switch-controller remote-log
         

  4. Ensure that the FortiGate firewall policy allows syslog traffic from the FortiLink interface to the interface where the Bindplane agent is located. If needed, create a policy:
         
         config firewall policy
             edit 0
                 set srcintf <fortilink_interface>
                 set dstintf <bindplane_interface>
                 set srcaddr "all"
                 set dstaddr "all"
                 set action accept
                 set schedule "always"
                 set service "SYSLOG"
             next
         end
         

Replace `<fortilink_interface>` with the FortiLink interface name and `<bindplane_interface>` with the interface where the Bindplane agent is reachable.

**Note:** By default, FortiSwitch logs are sent to port 514 of the remote syslog server.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
| metadata.event_type | The type of event represented by this record.  
event | metadata.product_event_type | The event type as reported by the product.  
log_id | metadata.product_log_id | Unique identifier for the log entry as assigned by the product.  
device_id | principal.asset.asset_id | Unique identifier for the asset.  
devname | principal.asset.hostname | Hostname of the asset associated with the principal.  
devname | principal.hostname | Hostname associated with the principal.  
vd | principal.user.attribute.labels | List of labels associated with the user.  
oldrole | principal.user.attribute.roles | List of roles associated with the user.  
unit | principal.user.role_description | Description of the user's role.  
user | principal.user.userid | Unique identifier for the user.  
action | security_result.action_details | Details about the action taken.  
msg | security_result.description | Description of the security result.  
type, subtype, switch.physical-port, instanceid | security_result.detection_fields | List of fields that were used for detection.  
pri | security_result.priority_details | Details about the priority of the event.  
status | security_result.summary | Summary of the security result.  
newrole | target.user.attribute.roles | List of roles associated with the target user.  
| metadata.product_name | Name of the product that generated the event.  
| metadata.vendor_name | Name of the vendor that produced the product.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
