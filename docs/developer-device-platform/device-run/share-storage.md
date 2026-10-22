---
url: https://docs.cloud.google.com/developer-device-platform/device-run/share-storage/
title: Share your Cloud Storage Buckets with Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:28.700076+00:00
---

# Share your Cloud Storage Buckets with Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/device-run/share-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Share your Cloud Storage Buckets with Developer Device Platform Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Like many Google Cloud services, Developer Device Platform has a dedicated [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents). This page explains how the DDP service agent works, what it can do, and how you can share resources with it.

## Permissions

When DDP is used for a project the first time, the system creates a service agent-type service account named: _service-PROJECT_ID@gcp-sa-devicerun.iam.gserviceaccount.com_

When you enable the [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run) API ([devicerun.googleapis.com](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest)), Google Cloud automatically provisions the service agent and assigns it the [roles/devicerun.serviceAgent](https://docs.cloud.google.com/iam/docs/service-agents#device-run-service-agent) role at the project level.

This service agent is granted permission to the Google Cloud project in which the Developer Device Platform is launched. The service agent uses its own credentials rather than yours to:

  * Read and write to Cloud Storage buckets and objects
  * Download Cloud Storage input files to the internal system
  * Upload files from the internal system to the Cloud Storage output bucket



This means it is possible you have access to a Cloud Storage bucket and file, but that bucket is owned by a different Google Cloud project than the one used in DDP. You could also have additional access controls on individual buckets.

Therefore, the Developer Device Platform service agent may not have access to these resources. Follow the instructions here to share access to specific buckets with the DDP service agent.

## Sharing access

See [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run) for how to include files with your tests in the DDP-supported project. If your Cloud Storage bucket resides in a different Google Cloud project from your DDP project and you want Device Run to be able to _read_ these files, you must grant [roles/storage.objectViewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) to the service agent of the project where the DDP request is initiated as described here.

_Grant Storage Object Viewer to the service agent_ : Ensure the DDP Service Agent has the `Storage Object Viewer` (`roles/storage.objectViewer`) role on the Cloud Storage bucket containing the files:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
      --member="serviceAccount:service-PROJECT_ID@gcp-sa-devicerun.iam.gserviceaccount.com" \  --role="roles/storage.objectViewer"
    

**Caution:** You may also grant the [roles/storage.objectUser](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) role to the DDP service agent to _upload_ to Google Cloud; but we recommend against placing output files into buckets outside of the project where DDP was triggered.

## Validation

Now return to your workflow and ensure [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run) has access to the requisite files. If the service agent does not have access to the specified files, the test fails to start.

## Supporting documentation

  * [Types of service accounts: service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) \- Learn how service agents operate within Google Cloud
  * [Service Agents](https://docs.cloud.google.com/iam/docs/service-agents) \- See every Google Cloud service agent
  * [Cloud Storage roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/storage) \- Find all Cloud Storage-related roles and permissions



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
