---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jenkins/
title: Collect Jenkins logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:48.853789+00:00
---

# Collect Jenkins logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jenkins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Jenkins logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This parser extracts key information such as timestamps, user IDs, source IPs, actions, and object IDs from JSON and SYSLOG formatted logs. It uses grok patterns to match various log message formats, handling variations in structure, and populates a unified data model (UDM) with the extracted fields. The parser also categorizes events based on the presence of user or IP information.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Privileged access to Google Cloud IAM.
  * Privileged access to Google Cloud Storage.
  * Privileged access to Jenkins.



## Create a Google Cloud Storage Bucket

  1. Go to **Cloud Storage**.
  2. Create a new bucket. Choose a unique name and appropriate region. 
  3. Ensure the bucket has proper access controls (for example, only authorized service accounts can write to it).



## Create a Google Cloud Service account

  1. Go to **IAM & Admin** > **Service Accounts**.
  2. Create a new service account. Give it a descriptive name (for example, **jenkins-logs**).
  3. Grant the service account the **Storage Object Creator** role on the GCS bucket you created in the previous step.
  4. Create an SSH key for your service account: [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).
  5. Download a JSON key file for the service account.

**Note:** Keep this file secure. You will need it for the **Google OAuth Credentials** plugin to create credentials.



## Install Google Cloud Storage plugin in Jenkins

  1. Go to **Manage Jenkins** > **Plugins**. 
  2. Select **Available plugins**.
  3. Search for the **Google Cloud Storage** plugin.
  4. Install the plugin and restart Jenkins if required.



## Install Google OAuth Credentials Plugin in Jenkins

  1. Go to **Manage Jenkins** > **Plugins**.
  2. Select **Available plugins**
  3. Search for the **Google OAuth Credentials** plugin.
  4. Install the plugin and restart Jenkins if required.



## Configure Jenkins to authenticate with Google Cloud

  1. Go to **Manage Jenkins** > **Credentials** > **System**.

**Note:** You can use **Global Credentials** or add a new domain (recommended).
  2. Click  add  **Add Credentials**.

  3. **Kind** : select **Google Service Account from private key**.

  4. **Project name** : set a name for the credentials.

  5. Upload the JSON key file you obtained during the Google Cloud Service account creation.

  6. Click **Create**.




## Configure Jenkins logs to upload Google SecOps

  1. In the Jenkins job configuration, add **Google Storage Build Log Upload** in post-build actions, with the following parameters: 
     * **Google Credentials** : The name of your Google credentials you created in the previous step.
     * **Log Name** : The name of the file to store the Jenkins build log, under the specified storage path.
     * **Storage Location** : The name of the bucket where you want to upload your logs. The bucket must be accessible to the service account you created.
  2. Test the log upload.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**. 
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Jenkins Logs**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Jenkins** as the **Log type**.
  7. Click **Get Service Account** as the **Chronicle Service Account**.
  8. Specify values for the following input parameters:

     * **Storage Bucket URI** : Google Cloud storage bucket URL in **`gs://my-bucket/<value>/`** format. This URL must end with a trailing forward slash (/).
     * **Source deletion options** : select deletion option according to your preference.
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account. * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.
  9. Click **Create Feed**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
**act** | **security_result.action_details** | Extracted from **msg1** or **msg2** fields. Represents the action performed. Leading whitespace is removed.  
**data** | **principal.user.userid** OR **principal.ip** OR **metadata.description** | If **data** matches an IP address pattern, it maps to **principal.ip**. If it matches a username pattern, it maps to **principal.user.userid**. Otherwise, it maps to **metadata.description**.  
**msg1** | **target.asset.product_object_id** OR **security_result.action_details** | Used to extract **object** and **act**. If a `/` is present, it is split into **object** and **act**. If `»` is present, it is split into **object** and **act**. Otherwise, it is treated as **act** and potentially further parsed.  
**msg2** | **metadata.description** OR **security_result.action_details** | If present, initially mapped to **metadata.description**. If it contains "completed:", the value after is extracted and mapped to **security_result.action_details**.  
**object** | **target.asset.product_object_id** | Extracted from **msg1**. Represents the object acted upon.  
**object_id** | **target.resource.attribute.labels.value** | Extracted from **object** if a `/` is present. Represents a more specific object identifier. The key is hardcoded as "Plugin Name".  
**src_ip** | **principal.ip** | Extracted from **message** or **data**. Represents the source IP address.  
**user** | **principal.user.userid** | Extracted from **message** or **data**. Represents the user associated with the event.  
| **metadata.event_timestamp** | Copied from the calculated **@timestamp** field.  
| **metadata.event_type** | Determined by parser logic. Set to **USER_UNCATEGORIZED** if **user** is present, **STATUS_UNCATEGORIZED** if **src_ip** is present, and **GENERIC_EVENT** otherwise.  
| **metadata.product_name** | Hardcoded as **Jenkins**.  
| **metadata.product_version** | Hardcoded as **Jenkins**.  
| **metadata.vendor_name** | Hardcoded as **JENKINS**.  
| **metadata.event_timestamp** | Constructed from **year** , **month** , **day** , **time** , and **ampm** fields.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jenkins-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
