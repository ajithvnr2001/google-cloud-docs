---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-protect-telemetry-v2/
title: Collect Jamf Protect Telemetry V2 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:45.610710+00:00
---

# Collect Jamf Protect Telemetry V2 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-protect-telemetry-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Jamf Protect Telemetry V2 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to configure Jamf Protect to send telemetry V2 logs to Google Security Operations using webhooks or Amazon S3.

Jamf Protect's Mac Endpoint Telemetry collects system and user event log data from macOS computers using Apple's Endpoint Security API. Telemetry data provides detailed audit trails of endpoint activity including process execution, file operations, user authentication, and system changes, enabling security teams to detect threats, investigate incidents, and meet compliance requirements.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **Jamf Protect** macOS Security portal with administrator permissions
  * A Google Cloud project configured in your Google SecOps instance with the **Chronicle API** enabled
  * Privileged access to **Google Cloud Console** (for API key creation)
  * macOS computers enrolled in Jamf Protect with the Jamf Protect agent deployed



## Configure Jamf Protect telemetry

Create a telemetry configuration in Jamf Protect to define which macOS endpoint events to collect.

  1. Sign in to the **Jamf Protect** macOS Security portal.
  2. Click **Telemetry**.
  3. Click **Create Telemetry**.
  4. In the **Name** field, enter a name for the telemetry configuration (for example, `Google SecOps Telemetry`).
  5. In the **Description** field, enter a description (for example, `Telemetry configuration for Google Security Operations integration`).
  6. Select the event categories to include in the configuration. Available categories include process events, file events, user events, and system events.

**Note:** For comprehensive security monitoring, select all available event categories. You can refine the selection later based on your organization's requirements.
  7. (Optional) Select **File hashes** to enable computation and reporting of file hashes for process executable files.

  8. Click **Save**.




## Create webhook feed in Google SecOps

### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Jamf Protect Telemetry V2`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Jamf Telemetry v2** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n`
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.



**Important** : The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create Google Cloud API key

### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Jamf Protect Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API**.
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.



## Configure Jamf Protect action configuration for webhook

Create or update an action configuration in Jamf Protect to send telemetry data to the Google SecOps webhook feed.

  1. In **Jamf Protect** , click **Actions**.
  2. Click **Create Action** to create a new action configuration, or select an existing action configuration and click **Edit**.
  3. Enter a **Name** for the action configuration (for example, `Google SecOps Webhook`).
  4. Enter a **Description** (for example, `Sends telemetry data to Google Security Operations via webhook`).
  5. In **Data Endpoints** , click **\+ Add**.
  6. Select **HTTP**.
  7. In the **URL** field, enter the **Feed endpoint URL** from Google SecOps.
  8. Click **\+ Add HTTP Header** and enter the following headers: 
     * First header: 
       * **Name** : `API_KEY`
       * **Value** : The API key you created in the Google Cloud Console
     * Second header: 
       * **Name** : `SECRET`
       * **Value** : The secret key you generated from the Google SecOps feed
  9. From **Collect Alerts** , select the alert levels you want to collect.
  10. From **Collect Logs** , select **Telemetry** and any additional macOS security data types to collect.
  11. Click **Save**.



## Assign the action configuration to a plan

  1. In **Jamf Protect** , click **Plans**.
  2. Select an existing plan and click **Edit** , or click **Create Plan** to create a new plan.
  3. From the **Telemetry** pop-up menu, select the telemetry configuration you created (for example, `Google SecOps Telemetry`).
  4. From the **Action** pop-up menu, select the action configuration you created (for example, `Google SecOps Webhook`).
  5. Click **Save**.



Computers assigned to this plan will begin sending telemetry data to Google SecOps.

## (Alternative) Configure ingestion using Amazon S3

You can also send Jamf Protect telemetry data to Google SecOps using Amazon S3 data forwarding from the Jamf Protect Cloud.

### Configure Jamf Protect data forwarding to Amazon S3

  1. In **Jamf Protect** , click **Administrative > Data**.
  2. Use the **Amazon S3 Forwarding** switch to enable data forwarding.
  3. Select the **Encrypt Forwarded Data** checkbox to ensure all data forwarded from the Jamf Protect Cloud is encrypted.
  4. Enter the name of an **Amazon S3 bucket** to send data to.
  5. (Optional) Enter a **prefix name** to use for all forwarded Jamf Protect data objects.
  6. Enter the **IAM Role** that Jamf Protect will assume when it forwards data to your Amazon S3 bucket. This value must be in Amazon Resource Name (ARN) format.
         
         arn:aws:iam::123456789012:role/S3Access
         

  7. Click **Save**.

**Note:** Jamf Protect provides an **External ID** to use when configuring Amazon S3 Forwarding. The ExternalId value is unique to every tenant and is included in the request to assume the role used to write data to the S3 bucket.
  8. Make sure your action configurations include **Jamf Protect Cloud** as a data endpoint and that **Telemetry** is selected under **Collect Logs**.




### Configure a feed in Google SecOps to ingest logs from Amazon S3

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Jamf Protect Telemetry V2 S3`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **Jamf Telemetry v2** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Specify values for the following fields:

     * **S3 URI** : `s3://<your-bucket-name>/<prefix>/`
     * **Source deletion option** : Select the deletion option according to your preference
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Access Key ID** : User access key with access to the S3 bucket
     * **Secret Access Key** : User secret key with access to the S3 bucket
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
  9. Click **Next** and then click **Submit**.




## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
**Note:** Batches of data sent through webhook feeds may experience ingestion delays if the request size or QPS limits are set too low.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
