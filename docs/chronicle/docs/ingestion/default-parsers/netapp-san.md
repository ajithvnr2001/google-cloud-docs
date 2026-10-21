---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-san/
title: Collect NetApp ONTAP SAN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:09:04.103371+00:00
---

# Collect NetApp ONTAP SAN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-san/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect NetApp ONTAP SAN logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest NetApp ONTAP SAN logs to Google Security Operations using Bindplane. NetApp ONTAP is a data management software platform for storage systems that provides SAN (Storage Area Network) services including block-level storage using iSCSI, Fibre Channel, and NVMe over Fabrics protocols. ONTAP SAN logs capture events related to LUN operations, initiator group management, port status changes, and storage access activities.

For more information, see [Collect NetApp SAN logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netapp-san).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * Network connectivity: If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the NetApp ONTAP cluster management interface (ONTAP System Manager or CLI).
  * ONTAP 9.x or later running on the storage system.



## Get Google SecOps ingestion authentication file

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Collection Agent**.
  3. Download the **Ingestion Authentication File**. 
     * Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/netapp_san:
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<CUSTOMER_ID>'
             endpoint: malachiteingestion-pa.googleapis.com
             log_type: NETAPP_SAN
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/netapp_san_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/netapp_san
         



  * Replace the **port** and **IP address** as required in your infrastructure.
  * Replace **`<CUSTOMER_ID>`** with the actual customer ID.
  * Update **`/path/to/ingestion-authentication-file.json`** to the path where the authentication file was saved.



## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure syslog forwarding on NetApp ONTAP

### Configure syslog using ONTAP CLI

  1. Connect to the NetApp ONTAP cluster management LIF using **SSH**.
  2. Enter the following command to view the current event notification destinations:
         
         cluster1::> event notification destination show
         

  3. Create a syslog notification destination pointing to the Bindplane agent:
         
         cluster1::> event notification destination create -name bindplane-syslog -syslog <BINDPLANE_IP_ADDRESS> -syslog-port 514 -syslog-transport udp-unencrypted
         

     * Replace **`<BINDPLANE_IP_ADDRESS>`** with the IP address of the Bindplane agent host.
  4. Create an event notification to forward EMS events to the syslog destination:
         
         cluster1::> event notification create -filter-name default-trap-events -destinations bindplane-syslog
         

**Note:** The `default-trap-events` filter includes critical and important EMS events. You can create custom filters to include additional event severities.
  5. **(Optional)** Create a custom filter to include all events:
         
         cluster1::> event filter create -filter-name all-events
         cluster1::> event filter rule add -filter-name all-events -type include -message-name * -severity <=NOTICE
         cluster1::> event notification create -filter-name all-events -destinations bindplane-syslog
         

  6. Verify the configuration:
         
         cluster1::> event notification destination show
         cluster1::> event notification show
         




### Configure syslog using ONTAP System Manager

  1. Sign in to **ONTAP System Manager**.
  2. Go to **Events & Jobs** > **Events** > **EMS Event Notifications**.
  3. Click **Add** to create a notification destination.
  4. Provide the following configuration details: 
     * **Name** : Enter `bindplane-syslog`.
     * **Type** : Select **Syslog**.
     * **Syslog Server** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Transport Protocol** : Select **UDP**.
  5. Click **Save**.
  6. Create an event notification rule and associate it with the `bindplane-syslog` destination.
  7. Select the event filter (for example, `default-trap-events` or a custom filter).
  8. Click **Save**.



For more information, see [NetApp ONTAP EMS configuration documentation](https://docs.netapp.com/us-en/ontap/error-messages/configure-ems-notifications-sm-task.html).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`desc` | `metadata.description` | Directly mapped  
`datetime` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`ip` | `principal.ip` | Merged  
`port` | `principal.port` | Directly mapped  
`userid` | `principal.user.userid` | Directly mapped  
`sr` | `security_result` | Merged  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `metadata.product_name` | Constant: `Storage Area Network`  
N/A | `metadata.vendor_name` | Constant: `NetApp`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-san-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
