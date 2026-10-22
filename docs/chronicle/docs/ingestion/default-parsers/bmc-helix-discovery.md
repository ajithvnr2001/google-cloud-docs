---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-helix-discovery/
title: Collect BMC Helix Discovery logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:11.306398+00:00
---

# Collect BMC Helix Discovery logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bmc-helix-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect BMC Helix Discovery logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts fields from BMC Helix Discovery syslog messages using grok patterns. It focuses on login/logout events and status updates. It maps extracted fields like timestamps, usernames, source IPs, and descriptions to the UDM. Events are categorized based on the extracted `product_event_type` and log details.

## Before you begin

  * Ensure that you have a Google Security Operations instance.
  * Ensure that you are using Windows 2016 or later, or a Linux host with systemd.
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open.
  * Ensure that you have privileged access to the BeyondTrust instance.



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



## Install Bindplane Agent

  1. For **Windows installation** , run the following script:  
`msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet`
  2. For **Linux installation** , run the following script:  
`sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh`
  3. Additional installation options can be found in this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane Agent to ingest Syslog and send to Google SecOps

  1. Access the machine where Bindplane is installed.
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             # Replace the below port <54525> and IP <0.0.0.0> with your specific values
             listen_address: "0.0.0.0:54525"
         
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
             namespace: BMC_HELIX_DISCOVERY
             raw_log_field: body
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<customer_id>` with the actual customer ID.
     * Update `{ json file for creds }` to the path where the service account key file (Option 1) was saved.
  3. Restart the Bindplane Agent to apply the changes:
         
         sudo systemctl restart bindplane
         




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
            namespace: BMC_HELIX_DISCOVERY
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Export Syslog from BMC Helix Discovery

  1. Access the BMC Discovery instance as a **root user**.
  2. Edit the **syslog configuration** file: `etc/rsyslog.conf`
  3. Add the following entry at the top: `# Send everything to the remote syslog server`.
  4. Replace the IP address with that of your syslog server:
         
         # Send everything to the remote syslog server
         
         *.* @192.168.1.100
         

  5. Restart the syslog service on the appliance:
         
         sudo /usr/bin/systemctl restart rsyslog.service
         

  6. Test the forwarding configuration.

  7. Use the logger utility to send a syslog message:
         
         logger this is a test of remote logging
         

  8. Verify this has been logged:
         
         su -
         Password:
         
         tail -n5 /var/log/messages
         Jan 17 11:42:10 localhost seclab: this is a test of remote logging
         

  9. Sign in to Google SecOps and check that the same messages appear.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`data` | metadata.description | The description of the event, extracted from the log message.  
`data` | metadata.product_event_type | The raw event type, extracted from the log message.  
`data` | principal.ip | The source IP address, extracted from the description field in the log message.  
`data` | security_result.summary | A summary of the event, extracted from the log message.  
`data` | target.user.userid | The username, extracted from the log message. An empty object is created by the parser. Copied from the top-level `timestamp` field in the raw log. Determined by the parser based on `product_event_type` and `desc` fields. If `product_event_type` is "logon" or `desc` contains "logged on", it's set to "USER_LOGIN". If `product_event_type` is "logoff" or `desc` contains "logged off", it's set to "USER_LOGOUT". Otherwise, if `src_ip` is present, it's set to "STATUS_UPDATE". Defaults to "GENERIC_EVENT". Hardcoded to "BMC_HELIX_DISCOVERY". Hardcoded to "BMC_HELIX_DISCOVERY". Hardcoded to "BMC_HELIX_DISCOVERY".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bmc-helix-discovery-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
