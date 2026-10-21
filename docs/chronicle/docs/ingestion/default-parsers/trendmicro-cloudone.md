---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-cloudone/
title: Collect Trend Micro Cloud One logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:30:46.317974+00:00
---

# Collect Trend Micro Cloud One logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-cloudone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Cloud One logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser handles syslog and JSON formatted logs from Trend Micro Cloud One. It extracts key-value pairs from LEEF formatted messages, normalizes severity values, identifies principal and target entities (IP, hostname, user), and maps the data into the UDM schema. If the LEEF format is not detected, the parser attempts to process the input as JSON and extract relevant fields accordingly.

## Before you begin

  * Ensure that you have a Google SecOps instance.
  * Ensure that you have privileged access to Trend Micro Cloud One.
  * Ensure that you have a Windows 2012 SP2 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agents**.
  3. Download the **Ingestion Authentication File**.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install Bindplane Agent

  1. For **Windows installation** , run the following script: `msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet`.
  2. For **Linux installation** , run the following script: `sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh`.
  3. Additional installation options can be found in this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).



## Configure Bindplane Agent to ingest Syslog and send to Google SecOps

  1. Access the machine with Bindplane Agent.
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the below port <5514> and IP (0.0.0.0) with your specific values
             listen_address: "0.0.0.0:514" 
         
         exporters:
             chronicle/chronicle_w_labels:
                 compression: gzip
                 # Adjust the creds location below according the placement of the credentials file you downloaded
                 creds: '{ json file for creds }'
                 # Replace <customer_id> below with your actual ID that you copied
                 customer_id: <customer_id>
                 endpoint: malachiteingestion-pa.googleapis.com
                 # You can apply ingestion labels below as preferred
                 ingestion_labels:
                 log_type: SYSLOG
                 namespace: 
                 raw_log_field: body
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/chronicle_w_labels
         

  3. Restart the Bindplane Agent to apply the changes using the following command: `sudo systemctl bindplane restart`




## Configure Syslog from Trend Micro Cloud One

  1. Go to **Policies** > **Common Objects** > **Other** > **Syslog Configurations**.
  2. Click **New** > **New Configuration** > **General**
  3. Specify values for the following parameters: 
     * **Name** : Unique name that identifies the configuration (for example, **Google SecOps BindPlance server**).
     * **Server Name** : Enter the IP address of the Bindplane Agent.
     * **Server Port** : Enter the port of the Bindplane Agent (for example, **514**).
     * **Transport** : Select **UDP**.
     * **Event Format** : Select **Syslog**. 
     * **Include time zone in events** : Keep **unselected**.
     * **Facility** : Type of process with which events will be associated.
     * **Agents should forward logs** : Select **Syslog** server.
     * Click **Save**.



## Export system events in Trend Micro Cloud One

  1. Go to **Administration** > **System Settings** > **Event Forwarding**.
  2. **Forward System Events to a remote computer** (via Syslog) using configuration, select the configuration created in the previous step.
  3. Click **Save**.



## Export security events in Trend Micro Cloud One

  1. Go to **Policies**.
  2. Click the policy used by the computers.
  3. Go to **Settings** > **Event Forwarding**.
  4. **Event Forwarding Frequency (from the Agent/Appliance)** : choose **Period between sending of events** and select how often the security events will be forwarded.
  5. **Event Forwarding Configuration (from the Agent/Appliance)** : choose **Anti-Malware Syslog Configuration** and select the configuration created in the previous step.
  6. Click **Save**.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
act | `security_result.action` | If `act` is "deny" or "block" (case-insensitive), then `BLOCK`. If `act` is "pass" or "allow" (case-insensitive), then `ALLOW`. If `act` is "update" or "rename" (case-insensitive), then `ALLOW_WITH_MODIFICATION`. If `act` is "quarantine" (case-insensitive), then `QUARANTINE`. Otherwise, `UNKNOWN_ACTION`.  
act | `security_result.action_details` | Directly mapped.  
cat | `security_result.category_details` | Directly mapped.  
cn1 | `target.asset_id` | Prefixed with "Host Id:" if `cn1Label` is "Host ID".  
desc | `metadata.description` | Directly mapped.  
dvchost | `target.asset.hostname` | Directly mapped.  
dvchost | `target.hostname` | Directly mapped.  
log_type | `metadata.product_name` | Directly mapped.  
msg | `security_result.description` | Directly mapped.  
name | `security_result.summary` | Directly mapped.  
organization | `target.administrative_domain` | Directly mapped.  
proto | `additional.fields.key` | Set to "Protocol" if the `proto` field cannot be converted to an integer.  
proto | `additional.fields.value.string_value` | Directly mapped if the `proto` field cannot be converted to an integer.  
proto | `network.ip_protocol` | Mapped using the `parse_ip_protocol.include` logic, which converts the protocol number to its corresponding name (e.g., "6" becomes "TCP").  
product_version | `metadata.product_version` | Directly mapped.  
sev | `security_result.severity` | If `sev` is "0", "1", "2", "3" or "low" (case-insensitive), then `LOW`. If `sev` is "4", "5", "6" or "medium" (case-insensitive), then `MEDIUM`. If `sev` is "7", "8" or "high" (case-insensitive), then `HIGH`. If `sev` is "9", "10" or "very high" (case-insensitive), then `CRITICAL`.  
sev | `security_result.severity_details` | Directly mapped.  
src | `principal.asset.hostname` | Directly mapped if it's not a valid IP address.  
src | `principal.asset.ip` | Directly mapped if it's a valid IP address.  
src | `principal.hostname` | Directly mapped if it's not a valid IP address.  
src | `principal.ip` | Directly mapped if it's a valid IP address.  
TrendMicroDsTenant | `security_result.detection_fields.key` | Set to "TrendMicroDsTenant".  
TrendMicroDsTenant | `security_result.detection_fields.value` | Directly mapped.  
TrendMicroDsTenantId | `security_result.detection_fields.key` | Set to "TrendMicroDsTenantId".  
TrendMicroDsTenantId | `security_result.detection_fields.value` | Directly mapped.  
usrName | `principal.user.userid` | Directly mapped. If `has_principal` is true and `has_target` is true, then `NETWORK_CONNECTION`. Else if `has_principal` is true, then `STATUS_UPDATE`. Else if `has_target` is true and `has_principal` is false, then `USER_UNCATEGORIZED`. Otherwise, `GENERIC_EVENT`. Set to `AUTHTYPE_UNSPECIFIED` if `event_type` is `USER_UNCATEGORIZED`. Set to "true" if a principal IP, hostname, or MAC address is extracted. Otherwise, initialized to "false". Set to "true" if a target IP, hostname, or MAC address is extracted. Otherwise, initialized to "false". Same as the top-level event timestamp. Set to "Trend Micro".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-cloudone-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
