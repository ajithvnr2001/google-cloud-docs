---
url: https://docs.cloud.google.com/logging/docs/setup/python/
title: Setting Up Cloud Logging for Python \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:02.929271+00:00
---

# Setting Up Cloud Logging for Python  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/setup/python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Setting Up Cloud Logging for Python Stay organized with collections  Save and categorize content based on your preferences. 

You can write logs to Cloud Logging from Python applications by using the standard Python logging handler, or by using the Cloud Logging API client library for Python directly. When you use the standard Python logging handler, you must attach a Cloud Logging handler to the Python root handler. This document illustrates that approach. 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Logging API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Logging API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com)

  8. Prepare your environment for Python development. 

[ Go to the Python setup guide ](https://docs.cloud.google.com/python/docs/setup)




## Install the library

To install the Cloud Logging library for Python, see [Install the client library for Python](https://docs.cloud.google.com/logging/docs/reference/libraries#client-libraries-install-python). This library lets you attach a Cloud Logging handler to the standard Python root handler. You can also use this library to send API requests to Cloud Logging.

For more information on installation, see the [documentation](https://docs.cloud.google.com/python/docs/reference/logging/latest) for the Cloud Logging library for Python. You can also report issues using the [issue tracker](https://github.com/googleapis/google-cloud-python/issues).

## Write logs with the standard Python logging handler

For information about how to use the standard logging handler, see [Advanced, code-based configuration](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-logging#advanced-code-based-configuration).

## Write logs with the Cloud Logging client library

For information on using the Cloud Logging client library for Python directly, see [Cloud Logging Client Libraries](https://docs.cloud.google.com/logging/docs/reference/libraries).

## Run on Google Cloud

For an application to write logs by using the Cloud Logging library for Python, the service account for the underlying resource must have the [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) [IAM](https://docs.cloud.google.com/iam/docs/understanding-roles) role. Most Google Cloud environments automatically configure the default service account to have this role.

### App Engine

Cloud Logging is automatically enabled for App Engine, and your app's [default service account](https://docs.cloud.google.com/appengine/docs/standard/python3/service-account) has the IAM permissions by default to write log entries.

For more information, see [Writing and viewing logs](https://docs.cloud.google.com/appengine/docs/standard/python3/writing-application-logs).

### Google Kubernetes Engine (GKE)

[GKE](https://docs.cloud.google.com/kubernetes-engine/docs) automatically grants the default service account the [Logs Writer (`roles/logging.logWriter`)](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) IAM role. If you use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) with this default service account to let workloads access specific Google Cloud APIs, then no additional configuration is required. However, if you use Workload Identity Federation for GKE with a custom IAM service account, then ensure that the custom service account has the role of Logs Writer (`roles/logging.logWriter`).

If needed, you can also use the following command to add the `logging.write` access scope when creating the cluster:
    
    
    gcloud container clusters create example-cluster-name \
        --scopes https://www.googleapis.com/auth/logging.write
    

### Compute Engine

**Note:** To use the Cloud Logging library for Python on a **Compute Engine** VM instance, you do not need to install the Cloud Logging agent.

When using [Compute Engine](https://docs.cloud.google.com/compute/docs) VM instances, add the `cloud-platform` access scope to each instance. When creating a new instance through the Google Cloud console, you can do this in the **Identity and API access** section of the **Create Instance** panel. Use the Compute Engine default service account or another service account of your choice, and select **Allow full access to all Cloud APIs** in the **Identity and API access** section. Whichever service account you select, ensure that it has been granted the [Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) in the **IAM & Admin** section of the Google Cloud console.

## Run locally and elsewhere

To use the Cloud Logging library for Python outside of Google Cloud, including running the library on your own workstation, on your data center's computers, or on the VM instances of another cloud provider, you must set up Application Default Credentials (ADC) in your local environment to authenticate to the Cloud Logging library for Python.

For more information, see [Set up ADC for on-premises or another cloud provider](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises).

## View the logs

In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

In the Logs Explorer, you must specify one or more resources, but the resource selection might not be obvious. Here are some tips to help you get started:

  * If you are deploying your application to App Engine or using the App Engine-specific libraries, set your resource to **GAE Application**.

  * If you are deploying your application on Compute Engine, set the resource to **GCE VM Instance**.

  * If you are deploying your application on Google Kubernetes Engine, your cluster's logging configuration determines the resource type of the log entries. For a detailed discussion on the Legacy Google Cloud Observability and the Google Cloud Observability Kubernetes Monitoring solutions, and how those options affect the resource type, see [Migrating to Google Cloud Observability Kubernetes Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/migration#stackdriver-options).

  * If your application is using the Cloud Logging API directly, the resource is dependent on the API and your configuration. For example, in your application, you can specify a resource or use a default resource.

  * If you don't see any logs in the Logs Explorer, to see all log entries, switch to the advanced query mode and use an empty query.

    1. To switch to the advanced query mode, click **menu** (▾) at the top of the Logs Explorer and then select **Convert to advanced filter**.
    2. Clear the content that appears in the filter box.
    3. Click **Submit Filter**.

You can examine the individual entries to identify your resources.




For additional information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
