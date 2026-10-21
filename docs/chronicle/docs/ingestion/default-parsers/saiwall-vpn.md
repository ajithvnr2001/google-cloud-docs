---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saiwall-vpn/
title: Collect Saiwall VPN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:26:49.295446+00:00
---

# Collect Saiwall VPN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saiwall-vpn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Saiwall VPN logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Saiwall VPN logs to Google Security Operations using the Bindplane agent.

Saiwall Secure SD-WAN, developed by SAIMA Systems, is an enterprise network security platform that combines firewall, proxy, VPN encryption, and LDAP services into a centralized management solution. The VPN component uses SSL VPN protocol over TCP with 2048-bit security certificates and AES 256-bit symmetric encryption, providing secure connectivity between remote sites and the central office across distributed enterprise environments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Saiwall Secure SD-WAN management console (SAIWALL SD-WAN Orchestrator)



## Get a Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.



## Get a Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

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
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: '<customer_id>'
             endpoint: malachiteingestion-pa.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'SAIWALL_VPN'
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
     * Replace `<customer_id>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop observiq-otel-collector && net start observiq-otel-collector
        




## Configure Saiwall syslog forwarding

To configure the Saiwall Secure SD-WAN appliance to forward syslog messages to the Bindplane agent, follow these steps:

  1. Sign in to the **SAIWALL SD-WAN Orchestrator** web management console.
  2. Go to **Configuration** > **System** > **Logging**.
  3. In the **Syslog** section, click **Enable** to activate remote syslog forwarding.
  4. Provide the following configuration details: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or the port configured in the Bindplane agent).
     * **Protocol** : Select **UDP**.
     * **Facility** : Select **local0** or the appropriate facility for your environment.
  5. In the **Log Categories** section, enable the following log types for forwarding: 
     * VPN connection events (tunnel establishment and teardown)
     * Firewall traffic events (allow and deny)
     * Authentication events (user logins and logouts)
     * System events (configuration changes and alerts)
  6. Click **Save** to apply the syslog configuration.
  7. Click **Synchronize** to push the configuration to all connected SAIWALL SR devices.

**Note:** If you are using the SAIWALL SIEM Connector module, logs from all SAIWALL SR devices connected to the infrastructure are centralized and forwarded through a single configuration, without requiring individual device setup.



For more information, see the [SAIMA Systems documentation](https://saimasystems.com/en/products/saiwall-secure-sdwan).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`egressInterface_label` | `additional.fields` | Merged  
`flowEndMilliseconds_label` | `additional.fields` | Merged  
`flowEndReason_label` | `additional.fields` | Merged  
`flowStartMilliseconds_label` | `additional.fields` | Merged  
`format_label` | `additional.fields` | Merged  
`header_map_label` | `additional.fields` | Merged  
`ingressInterface_label` | `additional.fields` | Merged  
`ipClassOfService_label` | `additional.fields` | Merged  
`ipNextHopIPv4Address_label` | `additional.fields` | Merged  
`octetDeltaCount_label` | `additional.fields` | Merged  
`packetDeltaCount_label` | `additional.fields` | Merged  
`protocolIdentifier_label` | `additional.fields` | Merged  
`tcpControlBits_label` | `additional.fields` | Merged  
`inter_host` | `intermediary.hostname` | Directly mapped  
`record.nexthop` | `intermediary.ip` | Merged  
`port` | `intermediary.port` | Renamed/mapped  
`event_type` | `metadata.event_type` | Directly mapped  
`record.input` | `network.received_bytes` | Renamed/mapped  
`record.output` | `network.sent_bytes` | Renamed/mapped  
`record.srcaddr` | `principal.ip` | Merged  
`sourceIPv4Address` | `principal.ip` | Merged  
`record.srcport` | `principal.port` | Renamed/mapped  
`sourceTransportPort` | `principal.port` | Renamed/mapped  
`destinationIPv4Address` | `target.ip` | Merged  
`record.dstaddr` | `target.ip` | Merged  
`destinationTransportPort` | `target.port` | Renamed/mapped  
`record.dstport` | `target.port` | Renamed/mapped  
`record_map_label` | `target.resource.attribute.labels` | Merged  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/saiwall-vpn-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
