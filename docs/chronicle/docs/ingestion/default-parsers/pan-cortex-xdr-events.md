---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-cortex-xdr-events/
title: Collect Palo Alto Cortex XDR Events logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:42.565339+00:00
---

# Collect Palo Alto Cortex XDR Events logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-cortex-xdr-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Palo Alto Cortex XDR Events logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Palo Alto Cortex XDR Event logs to Google Security Operations using Google Cloud Storage. The parser extracts security event data from Palo Alto Networks Cortex XDR JSON logs. It normalizes the data into the Unified Data Model (UDM) by mapping fields, converting data types, and enriching events with metadata like vendor, product, and event types based on conditional logic tied to `event_type` and `event_sub_type` fields. It also handles network connections, file and registry operations, process information, and user activity.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Google Cloud Storage is set up and active in your Google Cloud environment
  * Privileged access to Google Cloud and appropriate permissions
  * Privileged access to Palo Alto Cortex XDR



## Create a Google Cloud Storage Bucket

  1. Sign in to the Google Cloud console.
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

  5. In the **Get started** section, do the following:

     1. Enter a unique name that meets the bucket name requirements (for example, **cortex-xdr-events-secops**).
     2. To enable hierarchical namespace, click the expander arrow to expand the **Optimize for file oriented and data-intensive workloads** section, and then select **Enable Hierarchical namespace on this bucket**.

**Note:** You can't enable hierarchical namespace in an existing bucket.
     3. To add a bucket label, click the expander arrow to expand the **Labels** section.

     4. Click **Add label** and specify a key and a value for your label.

  6. In the **Choose where to store your data** section, do the following:

     1. Select a **Location type**.
     2. Use the location type's menu to select a **Location** where object data within your bucket will be permanently stored.

**Note:** If you select the **dual-region** location type, you can also choose to enable **turbo replication** by selecting the relevant checkbox.
     3. To set up cross-bucket replication, expand the **Set up cross-bucket replication** section.

  7. In the **Choose a storage class for your data** section, either select a **default storage class** for the bucket, or select **Autoclass** for automatic storage class management of your bucket's data.

  8. In the **Choose how to control access to objects** section, select **not** to enforce **public access prevention** , and select an **access control model** for your bucket's objects.

**Note:** If public access prevention is already enforced by your project's organization policy, the **Prevent public access** checkbox is locked.
  9. In the **Choose how to protect object data** section, do the following:

     1. Select any of the options under **Data protection** that you want to set for your bucket.
     2. To choose how your object data will be encrypted, click the **Data encryption** expander arrow, and select a **Data encryption method**.
  10. Click **Create**.

**Important:** Make sure that the Google SecOps Service Account is granted **Read** or **Read & Write** permission for this bucket.
  11. Configure an **Object Lifecycle Management** rule on the newly created destination bucket to delete objects after 7 days:

     1. In the **Cloud Storage Buckets** list, click the name of your bucket.
     2. Select the **Lifecycle** tab, and then click **Add a rule**.
     3. In the **Select an action** section, select **Delete object**.
     4. In the **Select object conditions** section, select **Age** , and set the value to `7` days.
     5. Click **Save**.
**Note:** Configuring a 7-day retention rule ensures that the destination bucket lifecycle matches the PAN Cortex source bucket's 7-day retention policy, controlling storage costs without triggering continuous re-download loops.



## Configure Cortex XDR Event Forwarding

  1. Sign in to the **Cortex XDR** web UI.
  2. Go to **Settings > Configurations > Data Management > Event Forwarding**.
  3. Activate the licenses in the **Activation** section.
  4. Enable **GB Event Forwarding** to export parsed logs for Cortex XDR Pro per GB to an external SIEM for storage.
  5. Enable **Endpoints Event Forwarding** to export raw endpoint data for Cortex XDR Pro EP and Cloud Endpoints.
  6. **Save** the selection.
  7. **Copy** the storage path displayed.
  8. **Generate** and **download** the Service Account JSON WEB TOKEN, which contains the access key.
  9. **Save** it in a **secure location**.



## Configure Google Cloud Secret Manager

  1. Sign in to your **GCP**.
  2. Go to the **Secret Manager** page.
  3. If this your first time, you'll be prompted to **Enable** the **Secret Manager API**.
  4. Create a secret called **EVENT_FRWD_CRTX_KEY** and copy the contents of the JSON **xdr_sa_key.json** you downloaded as the value of the secret.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, **PANW Cortex XDR Event Logs**).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Palo Alto Cortex XDR Events** as the **Log type**.
  7. Click **Get Service Account** as the **Chronicle Service Account**.
  8. Click **Next**.
  9. Specify values for the following input parameters:

     * **Storage Bucket URI** : Google Cloud storage bucket URL (for example, `gs://cortex-xdr-events-secops`/). This URL must end with a trailing forward slash (/).
     * **Source deletion options** : Select **Do not delete transferred files**.

**Warning:** Don't select `Delete transferred files` or `Delete transferred files and empty directories`. Selecting a deletion option causes the scheduled `gcloud storage rsync` job to continuously re-download the 7-day backlog from the source bucket, resulting in an infinite ingestion loop and quota exhaustion.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.

  10. Click **Next**.

  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.

  12. After the Feed is created, find it on the **Feeds** list and click the three action dots to the right side of the line.

  13. Select **Disable Feed**.




## Configure Secret JSON Access to Cloud Storage

  1. Sign in to your **GCP**.
  2. Go to the **Secret Manager** page.
  3. Select the secret **EVENT_FRWD_CRTX_KEY**.
  4. Go to **Permissions** tab.
  5. Provide the **Storage Object Admin** and **Storage Legacy Bucket Reader** access to the bucket **cortex-xdr-events-secops** created previously.



## Configure Google SecOps Permissions for Cloud Storage

  1. Go to **IAM & Admin > IAM**.
  2. Locate the **Chronicle Service Account**.
  3. Grant the **Storage Object Viewer** (roles/storage.objectViewer) access to the bucket **cortex-xdr-events-secops** created previously.



## Configure PANW Cortex XDR Events logs ingestion to Project Cloud Storage

  1. In Google Cloud, go to **APIs & Services > Library**.
  2. Enable the **Cloud Run** and **Artifact Registry** APIs.
  3. Open **Cloud Shell** by clicking the icon in the top navigation bar.
  4. Download a custom code using the following command:
         
         git clone https://github.com/PaloAltoNetworks/google-cloud-cortex-chronicle.git
         

  5. Go to the directory by running the following command:
         
         cd google-cloud-cortex-chronicle/
         

  6. Open the file `env.properties` with an editor like `vi`.

  7. Provide the following configuration details:
         
         REGION=us-central1 # Update according to your project region
         REPO_NAME=panw-chronicle
         IMAGE_NAME=sync_cortex_bucket
         GCP_PROJECT_ID=chrxxxxxxxxx # Update according to your project ID
         JOB_NAME=cloud-run-job-cortex-data-sync # The Cloud Job name 
         ROJECT_NUMBER=80xxxxx9 # Update according to your project number
         # JOB ENV VARIABLES
         SRC_BUCKET=xdr-us-xxxxx-event-forwarding # Update with the Cortex XDR GCS bucket name
         DEST_BUCKET=cortex-xdr-events-secops # Update with the GCS name of the bucket you created
         SECRET_NAME=EVENT_FRWD_CRTX_KEY # Need to match the secret you created
         JOB_SCHEDULE_MINS=30
         

  8. Provide necessary permissions to the `deploy.sh` script:
         
         chmod 744 deploy.sh
         

  9. Run the `deploy.sh` script:
         
         ./deploy.sh
         

  10. Identify the used Cloud Job service account from the script output.

  11. Grant the **Cloud Job** service account **Secret Manager Secret Ancestor** permission to access the Secret you created before (as in our example, **EVENT_FRWD_CRTX_KEY**).

  12. Go to **Secret Manager > EVENT_FRWD_CRTX_KEY (secret) > Permissions**.

  13. In the Google SecOps platform, go to **SIEM Settings > Feeds > XDR Events Feed Name > Enable Feed**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action_file_path` | `target.file.full_path` | Directly mapped  
`action_file_size` | `target.file.size` | Directly mapped and converted to unsigned integer  
`action_local_ip` | `principal.ip` | Directly mapped and merged with other IP addresses  
`action_local_port` | `principal.port` | Directly mapped and converted to integer  
`action_module_path` | `target.process.file.full_path` | Directly mapped  
`action_network_connection_id` | `network.session_id` | Directly mapped  
`action_network_protocol` | `network.ip_protocol` | Renamed to `protocol_number_src`, parsed using `parse_ip_protocol.include`, and mapped to `network.ip_protocol`  
`action_process_image_command_line` | `target.process.command_line` | Directly mapped  
`action_process_image_md5` | `target.process.file.md5` | Directly mapped  
`action_process_image_path` | `target.process.file.full_path` | Directly mapped  
`action_process_image_sha256` | `target.process.file.sha256` | Directly mapped  
`action_process_os_pid` | `target.process.pid` | Directly mapped and converted to string  
`action_process_user_sid` | `target.user.windows_sid` | Directly mapped  
`action_process_username` | `target.user.userid`, `target.administrative_domain` | Lowercased, parsed for domain and user, and mapped accordingly  
`action_registry_data` | `target.registry.registry_value_data` | Directly mapped  
`action_registry_key_name` | `target.registry.registry_key` | Directly mapped  
`action_registry_value_name` | `target.registry.registry_value_name` | Directly mapped  
`action_remote_ip` | `target.ip` | Directly mapped and merged with other IP addresses  
`action_remote_port` | `target.port` | Directly mapped and converted to integer  
`action_total_download` | `network.received_bytes` | Directly mapped and converted to unsigned integer  
`action_total_upload` | `network.sent_bytes` | Directly mapped and converted to unsigned integer  
`agent_hostname` | `principal.hostname`, `observer.hostname` | Lowercased and mapped  
`agent_ip_addresses` | `observer.ip` | Parsed as JSON, split into individual IPs, and merged  
`agent_os_sub_type` | `target.platform_version` | Directly mapped  
`event_id` | `metadata.product_log_id` | Directly mapped  
`event_sub_type` | `metadata.product_event_type` | Converted to string and used for conditional mapping of `metadata.event_type` and `metadata.product_event_type`  
`event_timestamp` | `metadata.event_timestamp`, `timestamp` | Converted to string, parsed as UNIX_MS timestamp, and mapped  
`event_type` | `metadata.event_type` | Converted to string and used for conditional mapping of `metadata.event_type` and `metadata.product_event_type`  
`os_actor_process_command_line` | `principal.process.command_line` | Directly mapped  
`os_actor_process_image_md5` | `principal.process.file.md5` | Directly mapped  
`os_actor_process_image_path` | `principal.process.file.full_path` | Directly mapped  
`os_actor_process_image_sha256` | `principal.process.file.sha256` | Directly mapped  
`os_actor_process_instance_id` | `principal.process.product_specific_process_id` | Prefixed with "PAN:" and mapped  
`os_actor_process_os_pid` | `principal.process.pid` | Converted to string and mapped  
`os_actor_primary_user_sid` | `principal.user.windows_sid` | Mapped if it starts with "S-" or "s-"  
`os_actor_primary_username` | `principal.user.userid`, `principal.administrative_domain` | Lowercased, parsed for domain and user, and mapped accordingly  
`_action` | `security_result.action` | Merged into `_security_result` and then mapped  
`metadata.log_type` | `metadata.log_type` | Hardcoded to "PAN_CORTEX_XDR_EVENTS"  
`metadata.product_name` | `metadata.product_name` | Hardcoded to "Cortex XDR"  
`metadata.vendor_name` | `metadata.vendor_name` | Hardcoded to "PAN"  
`target.platform` | `target.platform` | Set to "WINDOWS" if `agent_os_sub_type` contains "Windows"  
`action_user_session_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`action_username` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`agent_ip_addresses` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`agent_os_sub_type` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`agent_id` | `event.idm.read_only_udm.principal.asset.asset_id` and `event.idm.read_only_udm.principal.asset_id` | Mapped from changelog  
`agent_os_type` | `event.idm.read_only_udm.principal.platform` | Mapped from changelog  
`action_process_token` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_process_fds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_process_termination_date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_process_termination_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_network_stats_is_last` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_user_is_local_session` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_user_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`action_file_previous_file_path` | `event.idm.read_only_udm.principal.file.full_path` | Mapped from changelog  
`agent_interface_map.ipv4` | `event.idm.read_only_udm.observer.ip` | Mapped from changelog  
`agent_interface_map.mac` | `event.idm.read_only_udm.observer.mac` | Mapped from changelog  
`action_file_last_writer_actor` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_file_device_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_file_previous_file_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_file_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`agent_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`agent_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`agent_os_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`os_actor_thread_thread_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_file_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_file_prev_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`os_actor_process_signature_status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`os_actor_process_logon_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`agent_content_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action_module_image_size` | `event.idm.read_only_udm.target.file.size` | Mapped from changelog  
`action_file_md5` | `event.idm.read_only_udm.target.file.md5` | Mapped from changelog  
`action_file_sha256` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`action_module_md5` | `target.process.file.md5` | Mapped from changelog  
`action_module_sha256` | `target.process.file.sha256` | Mapped from changelog  
`metadata.event_type` | `GENERIC_EVENT.` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-cortex-xdr-events-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
