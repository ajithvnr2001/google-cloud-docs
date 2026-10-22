---
url: https://docs.cloud.google.com/developer-device-platform/quickstart/
title: Quickstart: Prepare for Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:25.824139+00:00
---

# Quickstart: Prepare for Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Prepare for Developer Device Platform

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Get set up to use the Developer Device Platform, a next-generation, commercial-grade suite for remote device orchestration.

If you are migrating from [Firebase Test Lab](https://firebase.google.com/docs/test-lab) to Developer Device Platform, see our [migration guide](https://docs.cloud.google.com/developer-device-platform/device-run/migrate), [command and flag translation](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/flag-command-translation), and [migration skill](https://docs.cloud.google.com/developer-device-platform/device-run/migrate/migration-skill) for AI agents.

## Before you begin

The Developer Device Platform (DDP) works on any workstation with a terminal and internet access following the instructions on this page.

These documents assume you are a Google Cloud user with projects and accounts, as described in [Get started with Google Cloud](https://docs.cloud.google.com/docs/get-started) found in the _Overview_ tab of this site.

### Google Cloud configuration

**Note:** The Cloud Testing API is required by the Device Streaming API during Preview.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. Verify that you have the permissions required to complete this guide. 

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Device Run, Device Streaming, and Cloud Testing APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable devicerun.googleapis.com devicestreaming.googleapis.com testing.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Verify that you have the permissions required to complete this guide. 

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Device Run, Device Streaming, and Cloud Testing APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable devicerun.googleapis.com devicestreaming.googleapis.com testing.googleapis.com

  15. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




### Required roles

To get the permissions that you need to use Developer Device Platform, ask your administrator to grant you the following IAM roles on on your project: 

  * All: 
    * [Roles Viewer ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)
    * [Device Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.admin) (`roles/devicerun.admin`)
    * [Device Streaming Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.admin) (`roles/devicestreaming.admin`)
    * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Example commands

Now that you have the Device Run service, you can run the following commands to try out the catalog.

First, list all of the devices in your project:
    
    
    gcloud beta device-run devices list
    

Then filter for devices running a specific operating system:

### Android
    
    
    gcloud beta device-run devices list --filter="PLATFORM=ANDROID"
    

### iOS
    
    
    gcloud beta device-run devices list --filter="PLATFORM=iOS"
    

Finally, list all of the sessions in your project (likely none, try later):
    
    
    gcloud beta device-run sessions list
    

Now continue onto the feature instructions under What's next.

## Supporting documentation

  * [Google Cloud Skills README](https://github.com/google/skills/blob/main/README.md)
  * [Developer Device Platform Agent Skills repository](https://github.com/google/skills/tree/main/skills/cloud/developer-device-platform-basics)



## Contact us

Visit the [DDP Developer Forum](https://discuss.google.dev/c/google-cloud/developer-device-platform/248) to get help and offer suggestions.

To report bugs and file feature requests for the Developer Device Platform, [create an issue](https://issuetracker.google.com/issues/new?component=2214095&template=0).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

## What's next

  * [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog) \- Describe all of the device types in the Developer Device Platform lab and delve into each type.
  * [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run) \- Run tests on devices in the Developer Device Platform lab using both [Android](https://docs.cloud.google.com/developer-device-platform/device-run/android) and [iOS](https://docs.cloud.google.com/developer-device-platform/device-run/ios) devices.
  * [Share Storage](https://docs.cloud.google.com/developer-device-platform/device-run/share-storage) \- Grant the Developer Device Platform access to your existing Cloud Storage buckets.
  * [Find Logs](https://docs.cloud.google.com/developer-device-platform/device-run/find-logs) \- See your results at the command line and in the Google Cloud console.
  * [Device Streaming API](https://docs.cloud.google.com/device-streaming/docs) \- Connect to remote physical Android devices and interact with your app as if it is connected to your local machine.
  * [Agentic Development with Device Streaming](https://docs.cloud.google.com/developer-device-platform/agent-skill) \- Use the Developer Device Platform agent skill to find, reserve and connect to devices in Developer Device Platform.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
