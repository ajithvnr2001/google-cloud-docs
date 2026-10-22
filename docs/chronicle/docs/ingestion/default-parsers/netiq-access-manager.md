---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netiq-access-manager/
title: Collect OpenText Access Manager (formerly NetIQ Access Manager) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:53.931431+00:00
---

# Collect OpenText Access Manager (formerly NetIQ Access Manager) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netiq-access-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect OpenText Access Manager (formerly NetIQ Access Manager) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest OpenText Access Manager (formerly known as NetIQ Access Manager) logs to Google Security Operations using Bindplane.

OpenText Access Manager is an on-premises identity and access management solution that provides single sign-on (SSO), multi-factor authentication, federation, and policy-based access control for web applications and services. It acts as a secure gateway between users and protected resources, enforcing authentication and authorization policies across enterprise environments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A host running Windows 2016 or later or a Linux host with `systemd`.
  * Network connectivity: If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the OpenText Access Manager Administration Console.



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

  1. Sign in to the **Google SecOps console**.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows Installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         




### Linux Installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional Installation Resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane Agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: NETIQ_ACCESS_MANAGER
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the **port** and **IP address** as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace **`<customer_id>`** with the actual Customer ID.
  * Update **`/path/to/ingestion-authentication-file.json`** to the file path where the service account key file (Option 1) was saved in the previous steps.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: NETIQ_ACCESS_MANAGER
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure OpenText Access Manager syslog forwarding

  1. Sign in to the **OpenText Access Manager Administration Console**.
  2. Go to **Auditing** > **Syslog**.
  3. Select the **Enable Syslog** checkbox.
  4. Provide the following configuration details: 
     * **Syslog Server Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Facility** : Select the appropriate syslog facility (for example, **LOCAL0**).
  5. In the **Audit Events** section, select the event categories to forward: 
     * **Authentication events**
     * **Authorization events**
     * **Administration events**
     * **System events**
  6. Click **Apply** to save the syslog configuration.

**Note:** Verify that the **OpenText Access Manager** appliance can reach the **Bindplane agent** host on TCP port 514. Check the Bindplane agent logs to confirm that syslog messages are being received.

* * *

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`version` | `about.resource.attribute.labels` | Merged  
`_field` | `additional.fields` | Merged  
`I` | `extensions.auth.type` | Mapped: `"002E0505","002E001E","002E0046"` → `AUTHTYPE_UNSPECIFIED`, `"002E0007","002E000C"`...  
`host_name` | `intermediary.hostname` | Directly mapped  
`D` | `metadata.description` | Directly mapped  
`stringValue3` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`I` | `metadata.event_type` | Mapped: `"002E0505","002E001E","002E0046"` → `USER_LOGIN`, `002E0525` → `NETWORK_UNCATEGORIZ...  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`id_sub_event` | `metadata.product_event_type` | Directly mapped  
`I` | `metadata.product_log_id` | Directly mapped  
`eventId` | `metadata.product_log_id` | Directly mapped  
`event_id` | `metadata.product_log_id` | Directly mapped  
`product` | `metadata.product_name` | Directly mapped  
`product_version` | `metadata.product_version` | Directly mapped  
`vendor` | `metadata.vendor_name` | Directly mapped  
`T` | `network.http.user_agent` | Directly mapped  
`L` | `network.session_id` | Directly mapped  
`subTarget` | `network.session_id` | Directly mapped  
`F` | `principal.application` | Directly mapped  
`appName` | `principal.application` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`host_name` | `principal.asset.hostname` | Directly mapped  
`originator` | `principal.asset.hostname` | Directly mapped  
`src_ip` | `principal.asset.ip` | Merged  
`host` | `principal.hostname` | Directly mapped  
`host_name` | `principal.hostname` | Directly mapped  
`originator` | `principal.hostname` | Directly mapped  
`src_ip` | `principal.ip` | Merged  
`stringValue1` | `principal.user.userid` | Directly mapped  
`I` | `security_result.action` | Mapped: `"002E0505","002E001E","002E0046"` → `security_action`, `002E0525` → `security_actio...  
`security_action` | `security_result.action` | Merged  
`name` | `security_result.action_details` | Directly mapped  
`g_label` | `security_result.detection_fields` | Merged  
`h_label` | `security_result.detection_fields` | Merged  
`impersonatee_session_id_label` | `security_result.detection_fields` | Merged  
`m_label` | `security_result.detection_fields` | Merged  
`v_label` | `security_result.detection_fields` | Merged  
`priority` | `security_result.priority_details` | Directly mapped  
`A` | `security_result.rule_id` | Directly mapped  
`severity` | `security_result.severity_details` | Mapped values (5 total, e.g. `1` → `TRACE`, `2` → `DEBUG`, `4` → `INFO`)  
`result` | `security_result.summary` | Directly mapped  
`process_name` | `target.application` | Directly mapped  
`dst_ip` | `target.asset.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`B` | `target.resource.id` | Directly mapped  
`O` | `target.resource.name` | Directly mapped  
`Y` | `target.url` | Directly mapped  
`_group_identifier` | `target.user.group_identifiers` | Merged  
`U` | `target.user.userid` | Directly mapped  
`device_name` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `Netiq_Access_Manager`  
N/A | `metadata.vendor_name` | Constant: `Netiq`  
N/A | `security_result.severity_details` | Constant: `TRACE`  
`"2"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"3"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"host_name"` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`stringValue2` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`eventId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`subTarget` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`stringValue1` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`stringValue3` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`originator` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`originator` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`G","H","M" and "V` | `security_result.detection_fields` | Mapped from changelog  
`L` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`T` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netiq-access-manager-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
