---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/adva-fsp/
title: Collect Adtran (formerly ADVA Fiber Service Platform) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:07.731997+00:00
---

# Collect Adtran (formerly ADVA Fiber Service Platform) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/adva-fsp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Adtran (formerly ADVA Fiber Service Platform) logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Adtran (formerly known as ADVA Fiber Service Platform) logs to Google Security Operations using Bindplane.

Adtran is a family of optical networking and Ethernet access devices used for transport, aggregation, and demarcation in carrier and enterprise networks. The FSP product line includes the FSP 3000 open optical transport platform, the FSP 150 Ethernet access family, and associated management systems such as the FSP Network Manager and Network Element Director (NED). These devices generate syslog messages for alarms, configuration changes, performance events, and security audit trails.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the ADVA FSP Network Element Director (NED) or Element Manager.



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

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi&quot; /quiet
         

  3. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * **Linux** : `/observiq-otel-collector/config.yaml`
     * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`
  2. Edit the `config.yaml` file. Following are two receiver options; choose the one that matches how your ADVA FSP device sends logs.



  * Option A - UDP syslog receiver
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/adva_fsp:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            <location>: LOCATION
            # Project number of the Google Cloud project linked to the instance
            <project: '>PROJECT_NUMBER'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.js<on'
           > customer_id: 'CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: ADVA_FSP
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/adva_fsp:
              receivers:
                - udplog
              exporters:
                - chronicle/adva_fsp
        

  * Option B - TCP syslog receiver
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/adva_fsp:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            <location>: LOCATION
            # Project number of the Google Cloud project linked to the instance
            <project: '>PROJECT_NUMBER'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.js<on'
           > customer_id: 'CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: ADVA_FSP
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/adva_fsp:
              receivers:
                - tcplog
              exporters:
                - chronicle/adva_fsp
        

  * Replace `<CUSTOMER_ID>` with the actual customer ID.

  * Update `/opt/observiq-otel-collector/ingestion-auth.json` to the path where the service account key file (Option 1) was saved. Note: For Windows, use a path such as `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`.

  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/adva_fsp:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            custom<er_id: '>;CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ADVA_FSP
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

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
         




## Configure syslog forwarding on ADVA FSP

Configure the ADVA FSP device to forward syslog messages to the Bindplane agent. The configuration is performed through the Network Element Director (NED) or Element Manager web interface.

  1. Sign in to the **ADVA FSP Network Element Director** (NED) or **Element Manager**.
  2. Go to **Node** > **General** > **Controls**.
  3. In the **Remote Syslog Servers** section, click **Add** to create a new syslog server entry.
  4. Provide the following configuration details: 
     * **IP Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter the port number that matches your Bindplane agent receiver configuration (for example, `514`).
     * **Transport** : Select **UDP** or **TCP** to match the Bindplane agent receiver type (`udplog` for UDP, `tcplog` for TCP).
     * **Syslog Events** : Select **Enable** to activate syslog forwarding for this server.
  5. Click **Apply** to save the configuration.
  6. Verify that syslog messages are being received by checking the Bindplane agent logs:

     * **Linux** :
    
    sudo journalctl -u observiq-otel-collector -f
    

     * **Windows** :
    
    type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
    

**Note:** ADVA FSP devices use BSD-style syslog (RFC 3164) format by default. If your deployment requires RFC 5424, consult the ADVA FSP 3000R7 Element Manager User Manual for the specific configuration steps.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`ACCESSORDER` | `additional.fields.value.string_value` | The value is taken from the ACCESSORDER field in the raw log.  
`ADDRESS` | `principal.ip` | The value is taken from the ADDRESS field in the raw log and parsed as an IP address.  
`ADMINSTATE` | `additional.fields.value.string_value` | The value is taken from the ADMINSTATE field in the raw log.  
`AISCLIENTMDLEVEL` | `additional.fields.value.string_value` | The value is taken from the AISCLIENTMDLEVEL field in the raw log.  
`AISGENENABLED` | `additional.fields.value.string_value` | The value is taken from the AISGENENABLED field in the raw log.  
`AISPRIORITY` | `additional.fields.value.string_value` | The value is taken from the AISPRIORITY field in the raw log.  
`AISTXPERIOD` | `additional.fields.value.string_value` | The value is taken from the AISTXPERIOD field in the raw log.  
`AISTRIGGERTYPES` | `additional.fields.value.string_value` | The value is taken from the AISTRIGGERTYPES field in the raw log.  
`BUFFERSIZE` | `additional.fields.value.string_value` | The value is taken from the BUFFERSIZE field in the raw log.  
`CCIENABLED` | `additional.fields.value.string_value` | The value is taken from the CCIENABLED field in the raw log.  
`CCMINTERFACESTATUSTLVCONTROL` | `additional.fields.value.string_value` | The value is taken from the CCMINTERFACESTATUSTLVCONTROL field in the raw log.  
`CCMLTMPRIORITY` | `additional.fields.value.string_value` | The value is taken from the CCMLTMPRIORITY field in the raw log.  
`CFMTAGETHERTYPE` | `additional.fields.value.string_value` | The value is taken from the CFMTAGETHERTYPE field in the raw log.  
`CIR` | `additional.fields.value.string_value` | The value is taken from the CIR field in the raw log.  
`COS` | `additional.fields.value.string_value` | The value is taken from the COS field in the raw log.  
`CT` | `metadata.description` | The value is taken from the CT field in the raw log.  
`DESTBMAC` | `target.mac` | The value is taken from the DESTBMAC field in the raw log and parsed as a MAC address.  
`DHCPCIDENABLED` | `additional.fields.value.string_value` | The value is taken from the DHCPCIDENABLED field in the raw log.  
`DHCPENABLED` | `additional.fields.value.string_value` | The value is taken from the DHCPENABLED field in the raw log.  
`DHCPHOSTNAME` | `network.dhcp.client_hostname` | The value is taken from the DHCPHOSTNAME field in the raw log.  
`DHCPHOSTNAMEENABLED` | `additional.fields.value.string_value` | The value is taken from the DHCPHOSTNAMEENABLED field in the raw log.  
`DHCPHOSTNAMETYPE` | `additional.fields.value.string_value` | The value is taken from the DHCPHOSTNAMETYPE field in the raw log.  
`DHCPLOGSERVERENABLED` | `additional.fields.value.string_value` | The value is taken from the DHCPLOGSERVERENABLED field in the raw log.  
`DHCPNTPSERVERENABLED` | `additional.fields.value.string_value` | The value is taken from the DHCPNTPSERVERENABLED field in the raw log.  
`DHCPV6CIDENABLED` | `additional.fields.value.string_value` | The value is taken from the DHCPV6CIDENABLED field in the raw log.  
`DHCPV6ENABLED` | `additional.fields.value.string_value` | The value is taken from the DHCPV6ENABLED field in the raw log.  
`DHCPV6ROLE` | `additional.fields.value.string_value` | The value is taken from the DHCPV6ROLE field in the raw log.  
`DHCPVENDORINFOTYPE` | `additional.fields.value.string_value` | The value is taken from the DHCPVENDORINFOTYPE field in the raw log.  
`DIR` | `additional.fields.value.string_value` | The value is taken from the DIR field in the raw log.  
`DIRECTION` | `network.direction` | The value is set to "OUTBOUND" if the DIRECTION field in the raw log is "UP" (case-insensitive), "INBOUND" if it is "DOWN", and is left empty otherwise.  
`ENCAPSULATIONTYPE` | `additional.fields.value.string_value` | The value is taken from the ENCAPSULATIONTYPE field in the raw log.  
`GUARANTEEDA2NBW` | `additional.fields.value.string_value` | The value is taken from the GUARANTEEDA2NBW field in the raw log.  
`HCOSMGMTENABLED` | `additional.fields.value.string_value` | The value is taken from the HCOSMGMTENABLED field in the raw log.  
`INT` | `additional.fields.value.string_value` | The value is taken from the INT field in the raw log.  
`IPMODE` | `additional.fields.value.string_value` | The value is taken from the IPMODE field in the raw log.  
`IPV6ADDR` | `principal.ip` | The value is taken from the IPV6ADDR field in the raw log and parsed as an IP address.  
`IPV6ADDRPREFIXLENGTH` | `additional.fields.value.string_value` | The value is taken from the IPV6ADDRPREFIXLENGTH field in the raw log.  
`IPV6MTU` | `additional.fields.value.string_value` | The value is taken from the IPV6MTU field in the raw log.  
`ITAG` | `additional.fields.value.string_value` | The value is taken from the ITAG field in the raw log.  
`ITAGENABLED` | `additional.fields.value.string_value` | The value is taken from the ITAGENABLED field in the raw log.  
`LBMTXDESTTYPE` | `additional.fields.value.string_value` | The value is taken from the LBMTXDESTTYPE field in the raw log.  
`LBMTXNUMMSGS` | `additional.fields.value.string_value` | The value is taken from the LBMTXNUMMSGS field in the raw log.  
`LBMTXVLANDROPENABLE` | `additional.fields.value.string_value` | The value is taken from the LBMTXVLANDROPENABLE field in the raw log.  
`LBMTXVLANPRIORITY` | `additional.fields.value.string_value` | The value is taken from the LBMTXVLANPRIORITY field in the raw log.  
`LLRESPONDERENABLED` | `additional.fields.value.string_value` | The value is taken from the LLRESPONDERENABLED field in the raw log.  
`LLVIDLIST` | `additional.fields.value.string_value` | The value is taken from the LLVIDLIST field in the raw log.  
`LMDUALENDEDCOUNTALLPRIOS` | `additional.fields.value.string_value` | The value is taken from the LMDUALENDEDCOUNTALLPRIOS field in the raw log.  
`LMINPROFILEONLY` | `additional.fields.value.string_value` | The value is taken from the LMINPROFILEONLY field in the raw log.  
`LMRXCOUNTALLPRIOS` | `additional.fields.value.string_value` | The value is taken from the LMRXCOUNTALLPRIOS field in the raw log.  
`LMTXCOUNTALLPRIOS` | `additional.fields.value.string_value` | The value is taken from the LMTXCOUNTALLPRIOS field in the raw log.  
`LOC` | `additional.fields.value.string_value` | The value is taken from the LOC field in the raw log.  
`LOCN` | `additional.fields.value.string_value` | The value is taken from the LOCN field in the raw log.  
`LOGINTIMEOUT` | `additional.fields.value.string_value` | The value is taken from the LOGINTIMEOUT field in the raw log.  
`LOOPBACKBLOCKINGENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKBLOCKINGENABLED field in the raw log.  
`LOOPBACKCONFIG` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKCONFIG field in the raw log.  
`LOOPBACKDESTMAC` | `target.mac` | The value is taken from the LOOPBACKDESTMAC field in the raw log and parsed as a MAC address.  
`LOOPBACKDESTMACCONTROL` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKDESTMACCONTROL field in the raw log.  
`LOOPBACKINNERVLAN1` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKINNERVLAN1 field in the raw log.  
`LOOPBACKINNERVLAN1ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKINNERVLAN1ENABLED field in the raw log.  
`LOOPBACKINNERVLAN2` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKINNERVLAN2 field in the raw log.  
`LOOPBACKINNERVLAN2ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKINNERVLAN2ENABLED field in the raw log.  
`LOOPBACKINNERVLAN3` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKINNERVLAN3 field in the raw log.  
`LOOPBACKINNERVLAN3ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKINNERVLAN3ENABLED field in the raw log.  
`LOOPBACKOUTERITAG1` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERITAG1 field in the raw log.  
`LOOPBACKOUTERITAG1ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERITAG1ENABLED field in the raw log.  
`LOOPBACKOUTERITAG2` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERITAG2 field in the raw log.  
`LOOPBACKOUTERITAG2ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERITAG2ENABLED field in the raw log.  
`LOOPBACKOUTERITAG3` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERITAG3 field in the raw log.  
`LOOPBACKOUTERITAG3ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERITAG3ENABLED field in the raw log.  
`LOOPBACKOUTERVLAN1` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERVLAN1 field in the raw log.  
`LOOPBACKOUTERVLAN1ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERVLAN1ENABLED field in the raw log.  
`LOOPBACKOUTERVLAN2` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERVLAN2 field in the raw log.  
`LOOPBACKOUTERVLAN2ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERVLAN2ENABLED field in the raw log.  
`LOOPBACKOUTERVLAN3` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERVLAN3 field in the raw log.  
`LOOPBACKOUTERVLAN3ENABLED` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKOUTERVLAN3ENABLED field in the raw log.  
`LOOPBACKSOURCEMAC` | `principal.mac` | The value is taken from the LOOPBACKSOURCEMAC field in the raw log and parsed as a MAC address.  
`LOOPBACKSWAPSADA` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKSWAPSADA field in the raw log.  
`LOOPBACKTIMER` | `additional.fields.value.string_value` | The value is taken from the LOOPBACKTIMER field in the raw log.  
`LOWESTPRIODEFECT` | `additional.fields.value.string_value` | The value is taken from the LOWESTPRIODEFECT field in the raw log.  
`LTMTXDESTTYPE` | `additional.fields.value.string_value` | The value is taken from the LTMTXDESTTYPE field in the raw log.  
`LTMTXEGRESSID` | `metadata.product_log_id` | The value is taken from the LTMTXEGRESSID field in the raw log.  
`LTMTXFLAGS` | `additional.fields.value.string_value` | The value is taken from the LTMTXFLAGS field in the raw log.  
`LTMTXTTL` | `additional.fields.value.string_value` | The value is taken from the LTMTXTTL field in the raw log.  
`MT` | `additional.fields.value.string_value` | The value is taken from the MT field in the raw log.  
`MAXIMUMA2NBW` | `additional.fields.value.string_value` | The value is taken from the MAXIMUMA2NBW field in the raw log.  
`MVAL` | `additional.fields.value.string_value` | The value is taken from the MVAL field in the raw log.  
`NAME` | `additional.fields.value.string_value` | The value is taken from the NAME field in the raw log.  
`NC` | `additional.fields.value.string_value` | The value is taken from the NC field in the raw log.  
`PORTEID` | `additional.fields.value.string_value` | The value is taken from the PORTEID field in the raw log.  
`PORTLLENABLED` | `additional.fields.value.string_value` | The value is taken from the PORTLLENABLED field in the raw log.  
`PRIMARYSERVER` | `target.ip` | The value is taken from the PRIMARYSERVER field in the raw log and parsed as an IP address.  
`PRIMARYVID` | `additional.fields.value.string_value` | The value is taken from the PRIMARYVID field in the raw log.  
`QUEUEPROFILEID` | `additional.fields.value.string_value` | The value is taken from the QUEUEPROFILEID field in the raw log.  
`RXSHAPEREID` | `additional.fields.value.string_value` | The value is taken from the RXSHAPEREID field in the raw log.  
`SATRESPONDENABLED` | `additional.fields.value.string_value` | The value is taken from the SATRESPONDENABLED field in the raw log.  
`SE` | `additional.fields.value.string_value` | The value is taken from the SE field in the raw log.  
`SHAREDVIM` | `additional.fields.value.string_value` | The value is taken from the SHAREDVIM field in the raw log.  
`SVLANENABLED` | `additional.fields.value.string_value` | The value is taken from the SVLANENABLED field in the raw log.  
`SVLANID` | `additional.fields.value.string_value` | The value is taken from the SVLANID field in the raw log.  
`SYSLOCATION` | `principal.location.country_or_region` | The value is taken from the SYSLOCATION field in the raw log.  
`THVAL` | `additional.fields.value.string_value` | The value is taken from the THVAL field in the raw log.  
`TYPE` | `additional.fields.value.string_value` | The value is taken from the TYPE field in the raw log.  
`USERACCESSTYPE` | `additional.fields.value.string_value` | The value is taken from the USERACCESSTYPE field in the raw log.  
`USERAUTHKEY` | `additional.fields.value.string_value` | The value is taken from the USERAUTHKEY field in the raw log.  
`USERAUTHKEYLOCAL` | `additional.fields.value.string_value` | The value is taken from the USERAUTHKEYLOCAL field in the raw log.  
`USERAUTHPROTOCOL` | `additional.fields.value.string_value` | The value is taken from the USERAUTHPROTOCOL field in the raw log.  
`USERENGINEID` | `additional.fields.value.string_value` | The value is taken from the USERENGINEID field in the raw log.  
`USERKEYSLOCAL` | `additional.fields.value.string_value` | The value is taken from the USERKEYSLOCAL field in the raw log.  
`USERNAME` | `principal.user.userid` | The value is taken from the USERNAME field in the raw log.  
`USERPRIVKEY` | `additional.fields.value.string_value` | The value is taken from the USERPRIVKEY field in the raw log.  
`USERPRIVKEYLOCAL` | `additional.fields.value.string_value` | The value is taken from the USERPRIVKEYLOCAL field in the raw log.  
`USERPRIVPROTOCOL` | `additional.fields.value.string_value` | The value is taken from the USERPRIVPROTOCOL field in the raw log.  
`USERSECURITYLEVEL` | `additional.fields.value.string_value` | The value is taken from the USERSECURITYLEVEL field in the raw log.  
`USERSECURITYNAME` | `principal.user.user_display_name` | The value is taken from the USERSECURITYNAME field in the raw log.  
`application` | `principal.application` | The value is taken from the application field extracted by the grok parser.  
`description` | `security_result.description` | The value is taken from the description field extracted by the grok parser.  
| `metadata.description` | The value is set to "Backup NTP Server Failed" if the CT field in the raw log is "Backup NTP Server Failed".  
| `metadata.event_timestamp.seconds` | The value is taken from the timestamp field extracted by the grok parser and converted to epoch seconds.  
| `metadata.event_type` | The value is set based on the following logic: NETWORK_DHCP if network_dhcp_present is true and either principal_present or target_present is true. NETWORK_CONNECTION if target_present and principal_present are both true. USER_RESOURCE_ACCESS if user_present is true. STATUS_UPDATE if principal_present is true. GENERIC_EVENT otherwise.  
| `metadata.product_log_id` | The value is taken from the LTMTXEGRESSID field in the raw log.  
| `metadata.product_name` | The value is set to "ADVA_FSP".  
| `metadata.vendor_name` | The value is set to "ADVA_FSP".  
| `network.application_protocol` | The value is set to "DHCP" if network_dhcp_present is true and either principal_present or target_present is true.  
| `principal.hostname` | The value is taken from the principal_hostname field extracted by the grok parser, with underscores removed.  
| `principal.ip` | The value is taken from the IPADDR field in the raw log and parsed as an IP address.  
| `timestamp.seconds` | The value is taken from the timestamp field extracted by the grok parser and converted to epoch seconds.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/adva-fsp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
