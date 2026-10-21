---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arraynetworks-vpn/
title: Collect Array Networks SSL VPN logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:39:35.796917+00:00
---

# Collect Array Networks SSL VPN logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arraynetworks-vpn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Array Networks SSL VPN logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Array Networks SSL VPN logs to Google Security Operations using the Bindplane agent.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Array Networks SSL VPN management console or appliance (AG Series or vxAG)



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

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

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
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
             customer_id: <CUSTOMER_ID>
             endpoint: malachiteingestion-pa.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'ARRAYNETWORKS_VPN'
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
     * Replace `<CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.
     * The endpoint `malachiteingestion-pa.googleapis.com` is for the US region. If your Google SecOps instance is in a different region, use the region-appropriate ingestion endpoint provided in your tenant documentation.



## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Array Networks SSL VPN

  1. Sign in to the **Array Networks SSL VPN Management Console** (WebUI).
  2. In the left navigation menu, click **ADMIN TOOLS**.
  3. Click **Monitoring**.
  4. Click the **Logging** tab.
  5. Click the **Syslog Servers** sub-tab.
  6. In the **REMOTE SYSLOG SERVER CONFIGURATION** section, click **Add Server Entry**.
  7. Provide the following configuration details: 
     * **Host IP** : Enter the Bindplane agent IP address.
     * **Host Port** : Enter the Bindplane agent port number (for example, 514).
     * **Protocol** : Select **UDP** or **TCP** , depending on your Bindplane agent configuration.
     * **Source Port** : Leave default or specify if required by your network configuration.
     * **Level** : Select the minimum severity level to forward (for example, Informational, Warning, Error).
  8. Click **Add** or **Save** to apply the configuration.
  9. Click **Save Configuration** at the top of the page to persist the changes.

**Note:** The UI paths shown above are based on Array Networks AG Series and vxAG firmware. If your firmware version differs, the exact menu labels may vary slightly. Consult your Array Networks administration guide for firmware-specific instructions.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`clientip` | `principal.ip` | The client's IP address extracted from the `clientip` field in the raw log message.  
`column1` | `principal.ip` | IP address extracted from `column1` in the raw log.  
`column1` | `principal.asset.ip` | IP address extracted from `column1` in the raw log.  
`column3` | `network.received_bytes` | The number of received bytes, converted to an unsigned integer.  
`column4` | `network.http.method` | The HTTP method extracted from `column4` in the raw log.  
`column7` | `target.ip` | The target IP address extracted from `column7` in the raw log.  
`dport` | `target.port` | Destination port, converted to an integer.  
`dst` | `target.ip` | Destination IP address.  
`dst` | `target.asset.ip` | Destination IP address.  
`hostname` | `principal.hostname` | The hostname extracted from the `hostname` field in the raw log message.  
`hostname` | `principal.asset.hostname` | The hostname extracted from the `hostname` field in the raw log message.  
`http_method` | `network.http.method` | The HTTP method extracted from the raw log message.  
`id` | `principal.application` | The application ID from the raw log.  
`mac` | `principal.mac` | The MAC address extracted from the `mac` field in the raw log message.  
`msg` | `metadata.product_event_type` | The message field from the raw log, used as the product event type. Also used for `security_result.description` after removing backslashes and quotes.  
`product_name` | `metadata.product_name` | The product name extracted from the raw log message.  
`prxy_ip` | `intermediary.ip` | Proxy IP address.  
`prxy_port` | `intermediary.port` | Proxy port, converted to an integer.  
`response_code` | `network.http.response_code` | The HTTP response code, converted to an integer.  
`security_result.action` | `security_result.action` | Determined by the parser logic based on the value of `column2`. "BLOCK" if `column2` contains "TCP_MISS", "UNKNOWN_ACTION" otherwise.  
`security_result.description` | `security_result.description` | The message field from the raw log, after removing backslashes and quotes.  
`sport` | `principal.port` | Source port, converted to an integer.  
`src` | `principal.ip` | Source IP address.  
`src` | `principal.asset.ip` | Source IP address.  
`target_hostname` | `target.hostname` | The target hostname extracted from the raw log message.  
`timestamp` | `metadata.event_timestamp` | The timestamp extracted from the raw log message and parsed into a timestamp object.  
`uri` | `target.url` | Part of the target URL. Combined with `uri_param` to form the complete URL.  
`uri_param` | `target.url` | Part of the target URL. Combined with `uri` to form the complete URL.  
`user` | `target.user.userid` | The username extracted from the raw log message.  
`user_agent_string` | `network.http.user_agent` | The user agent string extracted from the raw log message.  
`vpn` | `target.user.group_identifiers` | The VPN name extracted from the raw log message.  
`metadata.event_type` | `metadata.event_type` | Determined by the parser logic based on a combination of fields like `has_principal`, `has_target`, `has_http_value`, and `user`. Can be "NETWORK_HTTP", "NETWORK_CONNECTION", "STATUS_UPDATE", "USER_UNCATEGORIZED", or "GENERIC_EVENT".  
`network.ip_protocol` | `network.ip_protocol` | Set to "TCP" if the message contains "TCP".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arraynetworks-vpn-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
