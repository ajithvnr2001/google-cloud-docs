---
url: https://docs.cloud.google.com/monitoring/synthetic-monitors/broken-links/
title: Create a broken-link checker \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:26.530824+00:00
---

# Create a broken-link checker  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/synthetic-monitors/broken-links/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create a broken-link checker Stay organized with collections  Save and categorize content based on your preferences. 

A broken-link checker synthetic monitor lets you periodically test the links on a web page to detect unreachable URLs. You configure test options—such as the origin URI, link limit, and retry count—in a preconfigured Cloud Run function. To help you troubleshoot failures, each execution saves detailed results and screenshots of the responses seen by your users.

For information about synthetic monitors, see [About synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/create#overview).

## About broken-link checkers

Each broken-link checker tests the links serially, and there is an overall synthetic timeout, which is configurable.

By default, a broken-link checker does the following:

  * Searches the origin URI for HTML anchor elements with `href` attributes.
  * Tests the first 10 links found on the origin URI.
  * For each link, the checker issues a request and then waits at most 30 seconds for a response. When a response is received, the checker verifies that the HTTP response status is `200`, which indicates a successful response. The checker doesn't perform retries.



You specify the origin URI. You can configure which HTML elements the broken-link checker searches for, the maximum number of elements tested, the per-test timeout, and whether retries are performed. You can also configure broken-link checkers to wait for a selector to appear.

Broken-link checkers use the [`broken-links-ok`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/broken-links-ok) template. The configuration for a broken-link checker is specified by the `options` object of the `index.js` file. If you create your checker by using the Google Cloud console, you're prompted for each configuration option and the Cloud Run function is updated for you. However, if you use the Cloud Monitoring API or Terraform, then you must populate this object.

After you create a broken-link checker, to modify the configuration, update the `options` object and redeploy the Cloud Run function.

## Before you begin

Configure your project and your IAM roles, and select the interface that you plan to use. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

### Configure your project and roles

  1. To get the permissions that you need to view and modify synthetic monitors by using the Google Cloud console, ask your administrator to grant you the following IAM roles on your project: 

     * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`)
     * [Cloud Functions Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. Enable the Cloud Monitoring API, Artifact Registry API, Cloud Build API, Cloud Functions API, Cloud Logging API, Pub/Sub API, and Cloud Run Admin API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,cloudfunctions.googleapis.com,logging.googleapis.com,pubsub.googleapis.com,run.googleapis.com)

  3. Verify that your Google Cloud project contains the default Compute Engine service account. This service account is created when you enable the Compute Engine API and has a name similar to `12345-compute@developer.gserviceaccount.com`.

In the Google Cloud console, go to the **Service Accounts** page: 

[Go to **Service Accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

If the default Compute Engine service account doesn't exist, then click **Create service account** and complete the dialog.

  4. Ensure that the default Compute Engine service account, or the service account that you created, has been granted the role of Editor (`roles/editor`).

To view the roles granted to your service account, do the following:

     1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

     2. Select **Include Google-provided role grants**.
     3. If the service account used by your synthetic monitor isn't listed, or if it hasn't been granted a role that includes the permissions in the role of Cloud Trace Agent (`roles/cloudtrace.agent`), then grant this role to your service account.
  5. Configure the notification channels that you want to use to receive notifications. We recommend that you create multiple types of notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options) and [Create and manage notification channels by API](https://docs.cloud.google.com/monitoring/alerts/using-channels-api). 



### Select the interface you plan to use

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## Create a broken-link checker

###  Console 

When you create a synthetic monitor by using the Google Cloud console, a new Cloud Run function (2nd gen) is deployed and the monitor for that Cloud Run function is created. You can't create a synthetic monitor that monitors an existing Cloud Run function.

  1. Ensure that you've enabled the required APIs, that your project contains a default Compute Engine service account, and that this account has been granted the role of Editor (`roles/editor`). For more information, see Before you begin.

  2. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  3. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  4. Select **Create Synthetic Monitor**.
  5. For the template, select **Broken link checker**.
  6. Enter a name for the synthetic monitor.
  7. Optional: Update the **Response Timeout** and the **Check Frequency** , and add user-defined labels.

  8. Configure the URI and the elements to test:

**Note:**

The values in the **URI configuration** fields are copied to the `options` object in the `index.js` file when you click **Create Function**. After you click **Create Function** , to change the configuration, edit the `options` object.

For details, see [Edit a synthetic monitor or Cloud Run function](https://docs.cloud.google.com/monitoring/synthetic-monitors/manage#edit).
     1. Click **Origin URI** , and enter a URI that you want tested. The value that you enter must be an HTTP or HTTPS endpoint. For example, you might enter `https://mywebsite.example.com`.

     2. Optional: In the **Number of links to follow** , update the maximum number of links that are tested. The default value of this field is **10**.

     3. Optional: In the **HTML element selector** field, enter the HTML elements that you want matched, as a comma-separated list. The value that you enter is converted to a string and then passed to the [`Document: querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) method.

By default, this field is set to `a`, which matches anchors. You can enter values such as `a, img`, when you want to match both anchors and images.

     4. Optional: In the **HTML attributes to follow** field, enter the HTML attributes that you want matched. The comma-separated values that you enter are individually passed to the [`getAttribute()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttribute) method.

By default, this field is set to `href`, which specifies the URI for the link. You can enter multiple attributes; for example, you can enter `href, src`. In this example, the code searches for the attribute `href` and then searches for the attribute `src`.

     5. Optional: Configure wait for selector, per-URI timeout, retries, and expected status codes:

        1. Click **Show more options**.
        2. To configure the broken-link checker to wait for a specific selector to appear in the URI before any links are scraped, enter the [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) in the **Wait for element selector** field. The value that you enter is converted to a string and then passed to the [`page.waitForSelector()`](https://pptr.dev/api/puppeteer.page.waitforselector) method.

If the selector doesn't appear before the timeout expires, then the failure is recorded in the logs.

        3. Update the order in which links are selected for testing.

        4. Configure retries.

By default, one request is sent to each link. If the initial request fails for any reason—for example, the command times out or the HTTP status code isn't `200`—then the link is marked as failed.

This field specifies the number of times the broken-link checker can issue an HTTP request to a link before marking the link as failed.

        5. Configure a timeout that applies to each URI. By default, this value is set to 30 seconds.

        6. To specify the expected status code and timeout for a specific URI, click **Add per-link option** and complete the dialog.

  9. Optional: Configure whether screenshots of responses are collected and saved. If you use the default settings, then screenshots aren't saved. If you enable screenshot collection, then you can collect screenshots for all tests or only for failing tests. Cloud Monitoring uses the following convention to name the Cloud Storage bucket:
         
         gcm-PROJECT_ID-synthetics-LOCATION
         

In the previous expression:

     * PROJECT_ID: The ID of your Google Cloud project.
     * LOCATION: The location of your Cloud Storage bucket.

You have the option to use an existing Cloud Storage bucket.

  10. Review your configuration and ensure that it is correct and complete, and then create your Cloud Run function:

     1. Click **Create Function**.

The values in the **URI configuration** fields are copied to the `options` object in the `index.js` file when you click **Create Function**. After you click **Create Function** , to change the configuration, edit the `options` object.

     2. Enter a display name and select a region. Names must be unique within a region.

**Note:** Don't include an underscore in the name of your Cloud Run function.

     3. In the **Runtime, build, connections and security settings** section, do the following:

        * In the **Connections** tab, ensure that **Allow all traffic** is selected.

        * Review the default settings and update them when necessary.

**Note:** The default settings for the allocated memory, CPU, and security might not be sufficient. We recommend that the memory be set to at least 2 GiB.
        * In the **Runtime service account** field, select a service account.
     4. Click **Apply function**.

  11. Configure the [alerting policy](https://docs.cloud.google.com/monitoring/alerts):

     1. Optional: Update the alerting policy name and the duration of failure before notifications are sent.

     2. Add the notification channels.

  12. Click **Create**.

The Cloud Run function that you defined is built and deployed as 2nd gen, and the synthetic monitor is created.




###  Terraform 

The process of creating a broken-link checker by using Terraform is identical to the process of creating any other synthetic monitor. For information about using Terraform to create a synthetic monitor, see [Create a synthetic monitor](https://docs.cloud.google.com/monitoring/synthetic-monitors/create), and select the Terraform tab.

**Note:** Don't include an underscore in the name of your Cloud Run function.

Broken-link checkers use the [`broken-links-ok`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/broken-links-ok) template. The configuration for a broken-link checker is specified by the `options` object of the `index.js` file.

When the `options.screenshot_options` structure is defined, the broken-link checker collects screenshots and saves them to a Cloud Storage bucket. If the `screenshot_options.storage_location` field isn't defined or if the value is an empty string, then Monitoring creates a Cloud Storage bucket and screenshots are saved to that bucket. Monitoring uses the following convention to name the Cloud Storage bucket:
    
    
    gcm-PROJECT_ID-synthetics-LOCATION
    

In the previous expression:

  * PROJECT_ID: The ID of your Google Cloud project.
  * LOCATION: The location of your Cloud Storage bucket.



###  REST 

The process of creating a broken-link checker by using the Cloud Monitoring API is identical to the process of creating any other synthetic monitor. For information about using the Cloud Monitoring API to create a synthetic monitor, see [Create a synthetic monitor](https://docs.cloud.google.com/monitoring/synthetic-monitors/create), and select the **REST** tab.

**Note:** Don't include an underscore in the name of your Cloud Run function.

Broken-link checkers use the [`broken-links-ok`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/tree/main/samples/broken-links-ok) template. The configuration for a broken-link checker is specified by the `options` object of the `index.js` file.

When the `options.screenshot_options` structure is defined, the broken-link checker collects screenshots and saves them to a Cloud Storage bucket. If the `screenshot_options.storage_location` field isn't defined or if the value is an empty string, then Monitoring creates a Cloud Storage bucket and screenshots are saved to that bucket. Monitoring uses the following convention to name the Cloud Storage bucket:
    
    
    gcm-PROJECT_ID-synthetics-LOCATION
    

In the previous expression:

  * PROJECT_ID: The ID of your Google Cloud project.
  * LOCATION: The location of your Cloud Storage bucket.



## Explore results

For each execution, a broken-link checker does the following:

  * Generates a table, where each row provides information about the testing of a specific URI. The summary information includes the target URI, latency, status, and the HTML element identifier. For example, this column lists **a** when an HTML anchor element is tested. When the row corresponds to the origin URI, the value of the HTML element identifier is **-**.

  * Collects metrics, trace data, and log data.

  * Collects screenshots, when configured.




For more information about how to explore the collected data, see [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore).

## Troubleshoot

This section provides information that you can use to help you troubleshoot your broken-link checkers.

### Unable to edit the configuration of a broken-link checker

You created a broken-link checker by using the Google Cloud console, and you want to change the HTML elements that are tested, or you want to modify the URI timeout, retries, wait for selector, and per-link options. However, when you edit the broken-link checker, the Google Cloud console doesn't display the configuration fields.

To resolve this failure, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate the synthetic monitor that you want to edit, click _more_vert_ **More options** , and then select **Edit**.
  4. Click **Edit function**.
  5. Edit the `options` object in the `index.js` file, and then click **Apply function**.

For information about the fields and syntax for this object, see [`broken-links-ok/index.js`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/blob/main/samples/broken-links-ok/index.js).

  6. Click **Save**.




### Google Cloud console reports that saving screenshots failed

**Note:** A synthetic monitor that can't save screenshots continues to test the links contained in a URI.

You created a broken-link checker and configured it to save screenshots. However, the Google Cloud console is displaying one of the following warning messages along with more detailed information:

  * `InvalidStorageLocation`
  * `StorageValidationError`
  * `BucketCreationError`
  * `ScreenshotFileUploadError`



To resolve these failures, try the following:

  * If you see the `InvalidStorageLocation` message, then verify the existence of the Cloud Storage bucket specified in the field named `options.screenshot_options.storage_location`.

  * View the logs related to your Cloud Run function. For more information, see [Finding logs](https://docs.cloud.google.com/monitoring/uptime-checks/troubleshoot#trouble-find-logs).

  * Verify that the service account being used in the corresponding Cloud Run function has an Identity and Access Management role that lets it create, access, and write to Cloud Storage buckets.




## What's next

  * [Samples for synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/samples)
  * [Manage synthetic monitors](https://docs.cloud.google.com/monitoring/synthetic-monitors/manage)
  * [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
