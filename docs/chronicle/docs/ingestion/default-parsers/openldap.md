---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openldap/
title: Collect OpenLDAP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:36:31.690737+00:00
---

# Collect OpenLDAP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/openldap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect OpenLDAP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest OpenLDAP logs to Google Security Operations using Bindplane.

OpenLDAP is an open-source LDAP directory server that generates access, audit, and replication logs. The parser extracts fields from OpenLDAP log entries and maps them to the Unified Data Model (UDM), capturing user identity, authentication events, LDAP operations, and security results.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the OpenLDAP server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the OpenLDAP server with root or administrative permissions



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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo systemctl status observiq-otel-collector
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/openldap:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: OPENLDAP
                raw_log_field: body
        
        service:
            pipelines:
                logs/openldap:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/openldap
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `malachiteingestion-pa.googleapis.com`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * Adjust the `creds_file_path` depending on the platform: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



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
         




## Configure OpenLDAP syslog forwarding

OpenLDAP (`slapd`) can be configured to log via syslog. Configure the syslog daemon to forward OpenLDAP logs to the Bindplane agent.

  1. Verify that OpenLDAP is configured to log to syslog. Check the `slapd.conf` or `cn=config` for the `loglevel` directive:
         
         loglevel stats conns
         

**Note:** Common log levels include `stats` (connection/operation statistics), `conns` (connection management), and `ACL` (access control processing). Adjust the log level to capture the events you need.
  2. OpenLDAP logs to the `local4` syslog facility by default. Configure rsyslog to forward these logs to the Bindplane agent. Create a configuration file:
         
         sudo nano /etc/rsyslog.d/openldap-forward.conf
         

  3. Add the following content:
         
         local4.* @BINDPLANE_AGENT_IP:514
         

**Note:** Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host. Use `@@` instead of `@` for TCP.
  4. Restart the rsyslog service:
         
         sudo systemctl restart rsyslog
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
op, fd, ou, cn, dc, dc1, base1, base2, base3, scope_data, valueData, method, filter, tag_data, err, attrData, ou_2, ou_1, syslog_message, immutable_user_id, resource | additional.fields | Merged with labels created from these fields  
| extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED"  
caller_ip, proxy1_ip, proxy2_ip | intermediary | Merged from intermediary, proxy_1, proxy_2  
msg1, inner_message | metadata.description | Value from msg1 or inner_message  
| metadata.event_type | Set to "GENERIC_EVENT" initially, then "STATUS_UPDATE" if principal IP present, "USER_UNCATEGORIZED" if user present, "USER_LOGIN" if timestamp or inner_ts present  
ldap_action | metadata.product_event_type | Value from ldap_action lowercased  
ldap_conn | metadata.product_log_id | Value from ldap_conn after removing "conn="  
user_agent | network.http.user_agent | Value copied directly  
session_id | network.session_id | Value copied directly  
principal_ip, prin_ip, caller_ip, r_ip_or_host, proxy_client_ip, src_ip, client_ip | principal.asset.ip | Merged from principal_ip (after replacing - with .), prin_ip, caller_ip, r_ip_or_host (if IP), proxy_client_ip, src_ip, client_ip  
r_ip_or_host, src_host | principal.hostname | Value from r_ip_or_host if hostname, else src_host  
principal_ip, prin_ip, caller_ip, r_ip_or_host, proxy_client_ip, src_ip, client_ip | principal.ip | Merged from principal_ip (after replacing - with .), prin_ip, caller_ip, r_ip_or_host (if IP), proxy_client_ip, src_ip, client_ip  
country | principal.location.country_or_region | Value copied directly  
prin_port, port, src_port | principal.port | Value from prin_port, port, or src_port, converted to integer  
syslog_process | principal.process.file.full_path | Value copied directly  
syslog_pid | principal.process.pid | Value copied directly  
org_name | principal.user.company_name | Value copied directly  
user, cn, uid | principal.user.userid | Value from user, cn, or uid  
security_result | security_result | Merged directly  
action, sec_action | security_result.action | Value from action (based on err codes) or sec_action (based on login_status)  
resource, immutable_user_id | security_result.detection_fields | Merged with labels from resource and immutable_user_id  
inner_descrption, security_description | security_result.description | Value from inner_descrption or security_description  
tuser, username, userid | target.user.userid | Value from tuser, username, or userid  
| metadata.product_name | Set to "OpenLDAP"  
| metadata.vendor_name | Set to "OpenLDAP"  
`eventType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`cn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sequenceId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dc_2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dc_3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dc` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dc_1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`path` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`ip1` | `principal.ip` | Mapped from changelog  
`base", "err", "attr", "tag", "scope", and "valueData` | `additional.fields` | Mapped from changelog  
`security_result.action` | `ALLOW` | Mapped from changelog  
`security_result.action` | `BLOCK` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openldap-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
