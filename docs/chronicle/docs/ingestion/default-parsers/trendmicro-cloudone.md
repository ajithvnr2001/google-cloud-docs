---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-cloudone/
title: Collect Trend Micro Cloud One logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:22.388982+00:00
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



## Install Bindplane Agent

  1. For **Windows installation** , run the following script: `msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet`.
  2. For **Linux installation** , run the following script: `sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh`.
  3. Additional installation options can be found in this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane Agent to ingest Syslog and send to Google SecOps

  1. Access the machine with Bindplane Agent.
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the below port <5514> and IP (0.0.0.0) with your specific values
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you saved in Step 1
             creds: '{ json file for creds }'
             # Replace <customer_id> below with your actual ID that you copied
             customer_id: <customer_id>
             endpoint: chronicle.googleapis.com
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
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<customer_id>` with the actual customer ID.
     * Update `{ json file for creds }` to the path where the service account key file (Option 1) was saved.
  3. Restart the Bindplane Agent to apply the changes using the following command: `sudo systemctl bindplane restart`




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you saved in Step 1
            creds: '{ json file for creds }'
            # Replace <customer_id> below with your actual ID that you copied
            customer_id: <customer_id>
            endpoint: malachiteingestion-pa.googleapis.com
            # You can apply ingestion labels below as preferred
            ingestion_labels:
            log_type: SYSLOG
            namespace:
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
