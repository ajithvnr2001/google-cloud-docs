---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chromeos-xdr/
title: Collect ChromeOS XDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:41:56.154507+00:00
---

# Collect ChromeOS XDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chromeos-xdr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ChromeOS XDR logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ChromeOS XDR logs to Google Security Operations using Google Cloud Pub/Sub.

ChromeOS XDR forwards operating-system-level security telemetry from managed ChromeOS devices to a Google Cloud Pub/Sub topic that you own. This telemetry includes login and logout activity, device boot state, process execution, network flows, and sensitive file modifications. You point the ChromeOS XDR provider configuration in the Google Admin console at your Pub/Sub topic, and a Pub/Sub push subscription delivers the events to your Google SecOps feed endpoint.

**Note:** Chrome browser enterprise reporting events (such as malware transfers, unsafe site visits, password reuse, and extension installs) are a separate `CHROME_MANAGEMENT` log type and are covered by the [Chrome Enterprise (Chrome Management) integration guide](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management). This guide covers only ChromeOS device XDR telemetry.**Note:** The Google Admin console also offers a **ChromeOS XDR connector** provider configuration that asks for a **Token** and a **Host Name**. That provider configuration delivers to third-party endpoints, such as CrowdStrike Falcon and does not deliver to Google SecOps. To collect ChromeOS XDR telemetry in Google SecOps, use the **Google Cloud Pub/Sub XDR** provider configuration described in this guide.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Google Cloud project bound to your Google SecOps instance. The Pub/Sub topic and the push subscription must live in this project.
  * Privileged access to Identity and Access Management (IAM) and Pub/Sub in that Google Cloud project.
  * A Google Workspace Administrator account with Super Admin privileges.
  * Managed ChromeOS devices enrolled in your Google Workspace organization.
  * Target Organizational Units (OUs) that contain the ChromeOS devices you want to collect telemetry from
  * Access to the Google Cloud Pub/Sub XDR provider configuration in the Google Admin console.

**Note:** The Google Cloud Pub/Sub provider configuration is gated by an allowlist and is not available to every Google Workspace account. If it does not appear in the list of provider configurations, your account doesn't yet have access. To request access, contact your Google representative.

## Bind the Google Cloud project to your Google SecOps instance

Before you create a Pub/Sub Push feed, bind the Google Cloud project that hosts your topic to your Google SecOps instance. The binding is what lets the push subscription authenticate with a service account.

### Check whether the project is already bound

  1. In your Google SecOps instance, go to **SIEM Settings > Projects**.
  2. Check whether your Google Cloud project is listed.
  3. If it is listed, the project is already bound. Continue to the next section.



### Bind the project

  1. Go to **SIEM Settings > Projects**.
  2. Click **Add Project**.
  3. In the **Project ID** field, enter your Google Cloud project ID.
  4. Click **Add**.
  5. Wait for the binding to complete, then refresh the page and verify that the project appears with the status **Active**.

**Note:** Only Google SecOps administrators can bind projects. If you don't have permission, contact your Google SecOps administrator.

### Verify that the Chronicle API is enabled

  1. Go to the [Google Cloud console APIs & Services library](https://console.cloud.google.com/apis/library).
  2. Select the bound project.
  3. In the search box, type **Chronicle**.
  4. Click **Chronicle API**.
  5. If the API is not enabled, click **Enable**.



## Create the Pub/Sub topic

Create the topic that receives ChromeOS XDR events. The topic belongs to you and is the value you enter in the Google Admin console later.

### Using the Google Cloud console

  1. Go to [Pub/Sub Topics](https://console.cloud.google.com/cloudpubsub/topic/list).
  2. Select the bound project.
  3. Click **Create topic**.
  4. Provide the following configuration details: 
     * **Topic ID** : Enter a descriptive name (for example, `chromeos-xdr-secops`)
     * **Add a default subscription** : Clear this checkbox
  5. Click **Create**.
  6. **Copy** the full topic path. The format is as follows:
         
         projects/<PROJECT_ID>/topics/<TOPIC_ID>
         




### Using the gcloud command-line tool

  * Use the following command:
        
        gcloud pubsub topics create chromeos-xdr-secops \
                --project=<PROJECT_ID>
        

    * Replace `<PROJECT_ID>` with the ID of the bound Google Cloud project.



## Grant publish access to the ChromeOS XDR publisher

ChromeOS XDR publishes events using a Google-managed service account. This service account does not have access to your topic until you grant access, and the Google Admin console **Test connection** check fails until you do.

### Using the Google Cloud console

  1. Go to [Pub/Sub Topics](https://console.cloud.google.com/cloudpubsub/topic/list).
  2. Click the topic you created.
  3. Open the **Permissions** tab, and then click **Add principal**.
  4. Provide the following configuration details: 
     * **New principals** : Enter `cloud-pub-sub-publisher@chromeos-xdr.iam.gserviceaccount.com`
     * **Role** : Select **Pub/Sub > Pub/Sub Publisher**
  5. Click **Save**.



### Using the gcloud command-line tool

  * Use the following command:
        
        gcloud pubsub topics add-iam-policy-binding chromeos-xdr-secops \
                --member="serviceAccount:cloud-pub-sub-publisher@chromeos-xdr.iam.gserviceaccount.com" \
                --role="roles/pubsub.publisher" \
                --project=<PROJECT_ID>
        

**Note:** This publisher service account is specific to ChromeOS XDR. Chrome browser enterprise reporting uses a different publisher account, so a topic already configured for Chrome browser reporting still needs this grant.



## Create the Pub/Sub push feed in Google SecOps

### Create the feed

  1. In your Google SecOps instance, go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ChromeOS XDR events`).
  5. Select **Google Cloud Pub/Sub Push** as the **Source type**.
  6. Select **ChromeOS XDR** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Leave this field empty. ChromeOS XDR publishes one event per Pub/Sub message.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The labels to be applied to the events from this feed
  9. Click **Next**.
  10. Review the feed configuration in the **Finalize screen** , and then click **Submit**.



### Get the push endpoint URL

  1. On the feed details page, verify that the feed status is **Active** and that the **Feed Enabled** toggle is on.
  2. In the **Endpoint Information** field, copy the push endpoint URL. The format is:
         
         https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs
         

  3. Save this URL for the push subscription.


**Note:** Pub/Sub Push feeds do not use API keys or secret keys. The push subscription authenticates with a service account OIDC token.

## Create the service account for Pub/Sub push

### Create the service account

  1. Go to the [Google Cloud console Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts).
  2. Select the bound project.
  3. Click **\+ Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a descriptive name (for example, `chromeos-xdr-push`)
     * **Service account description** : Enter `Pub/Sub Push to Google SecOps for ChromeOS XDR`
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, leave the **Role** field empty.
  7. Click **Continue > Done**.
  8. Copy the service account email. The format is:
         
         chromeos-xdr-push@<PROJECT_ID>.iam.gserviceaccount.com
         




### Using the gcloud command-line tool

  * Use the following command:
        
        gcloud iam service-accounts create chromeos-xdr-push \
                --display-name="ChromeOS XDR Push" \
                --description="Pub/Sub Push to Google SecOps for ChromeOS XDR" \
                --project=<PROJECT_ID>
        




### Service account permissions

No additional IAM role is required for this service account. The project binding you configured earlier enables service account authentication, and the push subscription authenticates to the Google SecOps feed endpoint using the service account's OIDC token. You select this service account when you enable authentication on the push subscription.

**Note:** There is no predefined `roles/chronicle.apiInvoker` role. Do not grant `roles/run.invoker`, which applies to Cloud Run and not to Google SecOps ingestion.

## Create the Pub/Sub push subscription

### Using the Google Cloud console

  1. Go to [Pub/Sub Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription/list).
  2. Click **Create subscription**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Subscription ID** | Enter a descriptive name (for example, `secops-chromeos-xdr`)  
**Select a Cloud Pub/Sub topic** | Select the topic you created  
**Delivery type** | **Push**  
**Endpoint URL** | Paste the push endpoint URL from the feed details page  
**Enable authentication** | Selected  
**Service account** | Select the service account you created  
**Audience** | Leave empty  
**Enable payload unwrapping** | Cleared  
**Write metadata** | Cleared  
**Acknowledgement deadline** | 600 seconds  
**Expiration period** | Never expire  
  4. Click **Create**.


**Note:** The Pub/Sub service agent `service-<PROJECT_NUMBER>@gcp-sa-pubsub.iam.gserviceaccount.com` must hold the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`) on the push service account, otherwise creating the authenticated subscription fails with a permission error. The Google Cloud console prompts you to grant it when you select **Enable authentication**.**Note:** Leave both **Enable payload unwrapping** and **Write metadata** cleared. The Google SecOps feed endpoint expects the full Pub/Sub message envelope and extracts the event payload itself. Enabling payload unwrapping strips that envelope before the message reaches the endpoint.

### Using the gcloud command-line tool

  * Use the following command:
        
        gcloud pubsub subscriptions create secops-chromeos-xdr \
                --topic=chromeos-xdr-secops \
                --push-endpoint=<PUSH_ENDPOINT_URL> \
                --push-auth-service-account=chromeos-xdr-push@<PROJECT_ID>.iam.gserviceaccount.com \
                --ack-deadline=600 \
                --expiration-period=never \
                --project=<PROJECT_ID>
        

Replace the following:

    * `<PUSH_ENDPOINT_URL>`: The push endpoint URL from the feed details page
    * `<PROJECT_ID>`: The ID of the bound Google Cloud project



### Verify that the subscription is created

  * Use the following command:
        
        gcloud pubsub subscriptions describe secops-chromeos-xdr \
                --project=<PROJECT_ID>
        

Verify that the output shows the following:

    * `pushConfig.pushEndpoint`: The feed endpoint URL
    * `pushConfig.oidcToken.serviceAccountEmail`: Your service account email
    * `ackDeadlineSeconds`: `600`



## Add the Google Cloud Pub/Sub XDR provider configuration

Point the ChromeOS XDR provider configuration at your Pub/Sub topic so that managed ChromeOS devices publish their telemetry to it.

  1. Sign in with a super administrator account to the [Google Admin console](https://admin.google.com).

If you aren't using a super administrator account, you can't complete these steps.

  2. Go to **Menu > Devices > Chrome > Connectors**.

  3. (Optional) If you're configuring Chrome Enterprise Connectors settings for the first time, follow the prompts to turn on **Chrome Enterprise Connectors**.

  4. At the top, click **\+ New provider configuration**.

  5. Find **Google Cloud Pub/Sub XDR** and click **Set up**.

The **Google Cloud Pub/Sub XDR configuration** dialog opens.

  6. Enter the following configuration details:

     * **Configuration name** : Enter a descriptive name. For example, `ChromeOS XDR to Google SecOps`.
     * **Topic full path** : Enter the full path of the topic you created, in the format `projects/<PROJECT_ID>/topics/<TOPIC_ID>`.
  7. Click **Test connection** to validate the configuration details.

If the validation fails, verify that:

     * The topic full path is correct and the topic exists in the bound Google Cloud project
     * `cloud-pub-sub-publisher@chromeos-xdr.iam.gserviceaccount.com` holds the **Pub/Sub Publisher** role on that topic
     * The Pub/Sub API is enabled in the project
**Note:** Google SecOps deduplicates identical batches, so if you run **Test connection** more than once, only the first test message appears in your instance.
  8. Under **Events this configuration is allowed to receive** , expand **XDR events** and select **Enable XDR events**.

  9. Click **Save configuration**.




The configuration is added for your entire organization. To enable it for the ChromeOS devices you want to monitor, select the organizational unit that contains those devices and select the checkbox next to your configuration.

## Enable ChromeOS XDR reporting

Enable ChromeOS XDR reporting in **Device settings** to start collecting operating-system-level security telemetry from your managed ChromeOS devices.

  1. In the [Google Admin console](https://admin.google.com), go to **Menu > Devices > Chrome > Settings > Device settings**.
  2. To apply the setting to all ChromeOS devices, leave the top organizational unit selected. Otherwise, select a child **organizational unit** that contains the devices you want to collect telemetry from.
  3. Go to **User and Device reporting**.
  4. Next to **Report extended detection and response (XDR) events** , select **Report information about extended detection and response (XDR) events**.
  5. Click **Save**.

Click **Override** for an organizational unit. To later restore the inherited value, click **Inherit**.

  6. Repeat these steps for any other organizational units that contain ChromeOS devices you want to collect telemetry from.




## Verify the data flow

To verify that ChromeOS XDR logs are being ingested into Google SecOps:

  1. Open your Google SecOps instance.
  2. Go to **Menu > Search**.
  3. Run the following search query to look for ChromeOS XDR events:
         
         metadata.log_type = "CHROMEOS_XDR"
         

  4. You should see events appearing within a few minutes of configuration. If no events appear:

     * In the Google Cloud console, open the topic and check the **Metrics** tab for published messages. No published messages means the Admin console side is not delivering.
     * In the Google Cloud console, open the subscription and check its metrics for push request counts and errors. Push errors mean the endpoint URL, the service account, or the project binding is wrong.
     * Verify that ChromeOS XDR reporting is enabled in the Google Admin console for the correct organizational units
     * Verify that the provider configuration is applied to the organizational units that contain your devices
     * Verify that the target ChromeOS devices are enrolled and managed in your organization
     * Verify that **Enable payload unwrapping** and **Write metadata** are cleared on the push subscription



## Supported log types

ChromeOS XDR reporting forwards the following ChromeOS device security telemetry to Google SecOps:

Event Category | Description  
---|---  
**Login and logout** | User login, logout, and authentication factor activity on the ChromeOS device  
**Device boot state** | Device boot state, firmware secure boot status, and kernel version reporting  
**Process execution** | Process and parent-process execution, including command line and image details  
**Network flow** | Network connections, including local and remote endpoints, ports, protocol, and bytes transferred  
**Sensitive file modification** | Creation and modification of sensitive files, including path and hash details  
  
## UDM mapping table

The following table shows how ChromeOS XDR log fields are mapped to Google SecOps Unified Data Model (UDM) fields:

Log Field | UDM Mapping | Logic  
---|---|---  
`application_protocol_label` | `additional.fields` | Merged  
`attributesBefore_canonicalGid_label` | `additional.fields` | Merged  
`attributesBefore_canonicalUid_label` | `additional.fields` | Merged  
`attributesBefore_mode_label` | `additional.fields` | Merged  
`authFactor_label` | `additional.fields` | Merged  
`bindAddr_label` | `additional.fields` | Merged  
`bindPort_label` | `additional.fields` | Merged  
`communityIdV1_label` | `additional.fields` | Merged  
`fileAfter_inodeDeviceId_label` | `additional.fields` | Merged  
`fileAfter_inode_label` | `additional.fields` | Merged  
`fileAfter_mntNs_label` | `additional.fields` | Merged  
`fileAfter_mode_label` | `additional.fields` | Merged  
`firmwareSecureBoot_label` | `additional.fields` | Merged  
`image_canonicalGid_label` | `additional.fields` | Merged  
`image_canonicalUid_label` | `additional.fields` | Merged  
`image_mode_label` | `additional.fields` | Merged  
`inodeDeviceId_label` | `additional.fields` | Merged  
`inode_label` | `additional.fields` | Merged  
`inode_process_label` | `additional.fields` | Merged  
`linuxKernelVersion_label` | `additional.fields` | Merged  
`local_timezone_label` | `additional.fields` | Merged  
`metaFirstAppearance_label` | `additional.fields` | Merged  
`modifyType_label` | `additional.fields` | Merged  
`networkFlow_direction_label` | `additional.fields` | Merged  
`process_image_canonicalGid_label` | `additional.fields` | Merged  
`process_image_canonicalUid_label` | `additional.fields` | Merged  
`process_image_mode_label` | `additional.fields` | Merged  
`process_inodeDeviceId_label` | `additional.fields` | Merged  
`process_metaFirstAppearance_label` | `additional.fields` | Merged  
`process_relStartTimeS_label` | `additional.fields` | Merged  
`rel_start_time_label` | `additional.fields` | Merged  
`sensitiveFileType_label` | `additional.fields` | Merged  
`socketType_label` | `additional.fields` | Merged  
`spawnProcess_canonicalUid_label` | `additional.fields` | Merged  
`spawnProcess_image_inodeDeviceId_label` | `additional.fields` | Merged  
`spawnProcess_image_inode_label` | `additional.fields` | Merged  
`spawnProcess_image_mode_label` | `additional.fields` | Merged  
`spawnProcess_metaFirstAppearance_label` | `additional.fields` | Merged  
`spawnProcess_relStartTimeS_label` | `additional.fields` | Merged  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`schemaVersion` | `metadata.product_version` | Directly mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Renamed/mapped  
`networkFlow.rxBytes` | `network.received_bytes` | Renamed/mapped  
`networkFlow.txBytes` | `network.sent_bytes` | Renamed/mapped  
`deviceName` | `principal.asset.asset_id` | Directly mapped  
`localIp` | `principal.asset.ip` | Merged  
`sensitiveModify.attributesBefore.pathname` | `principal.file.full_path` | Directly mapped  
`localIp` | `principal.ip` | Merged  
`networkFlow.localIp` | `principal.ip` | Merged  
`osVersion` | `principal.platform_version` | Directly mapped  
`networkFlow.localPort` | `principal.port` | Renamed/mapped  
`spawnProcess.commandline` | `principal.process.parent_process.command_line` | Directly mapped  
`spawnProcess.image.pathname` | `principal.process.parent_process.file.full_path` | Directly mapped  
`spawnProcess.image.sha256` | `principal.process.parent_process.file.sha256` | Directly mapped  
`spawnProcess.canonicalPid` | `principal.process.parent_process.pid` | Directly mapped  
`spawnProcess.processUuid` | `principal.process.product_specific_process_id` | Directly mapped  
`devicePermanentId` | `principal.resource.product_object_id` | Directly mapped  
`event_log` | `security_result.summary` | Directly mapped  
`sensitiveModify.fileAfter.pathname` | `target.file.full_path` | Directly mapped  
`sensitiveModify.fileAfter.sha256` | `target.file.sha256` | Directly mapped  
`networkFlow.remoteHostName` | `target.hostname` | Directly mapped  
`networkFlow.remoteIp` | `target.ip` | Merged  
`networkFlow.remotePort` | `target.port` | Renamed/mapped  
`process.image.pathname` | `target.process.file.full_path` | Directly mapped  
`process.image.sha256` | `target.process.file.sha256` | Directly mapped  
`parentProcess.commandline` | `target.process.parent_process.command_line` | Directly mapped  
`process.commandline` | `target.process.parent_process.command_line` | Directly mapped  
`parentProcess.image.pathname` | `target.process.parent_process.file.full_path` | Directly mapped  
`parentProcess.image.sha256` | `target.process.parent_process.file.sha256` | Directly mapped  
`parentProcess.canonicalPid` | `target.process.parent_process.pid` | Directly mapped  
`parentProcess.processUuid` | `target.process.parent_process.product_specific_process_id` | Directly mapped  
`process.canonicalPid` | `target.process.pid` | Directly mapped  
`process.processUuid` | `target.process.product_specific_process_id` | Directly mapped  
`deviceUser` | `target.user.email_addresses` | Merged  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `CHROMEOS XDR`  
N/A | `metadata.vendor_name` | Constant: `CHROMEOS XDR`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/chromeos-xdr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
