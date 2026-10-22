---
url: https://docs.cloud.google.com/healthcare-api/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:45.738502+00:00
---

# Troubleshooting  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Support ](https://docs.cloud.google.com/healthcare-api/docs/support)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

Learn about troubleshooting steps that you might find helpful if you run into problems using the Cloud Healthcare API.

## Cannot enable the Cloud Healthcare API

When enabling the Cloud Healthcare API for the first time in your Google Cloud project, you might encounter a permissions error indicating that you don't have permission to enable Google Cloud APIs for your project.

See [Enabling and disabling APIs](https://docs.cloud.google.com/apis/docs/enable-disable-apis) for information on how to enable Google Cloud APIs, including the Cloud Healthcare API.

## Cannot authenticate to the Cloud Healthcare API

When calling the Cloud Healthcare API, you might receive an error message indicating that your "Application Default Credentials" are unavailable.

See [Authenticating to the API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/authentication) for information on how to configure Application Default Credentials or how to pass in authentication credentials manually to an application or command.

## Missing the Cloud Healthcare API service account or Healthcare Service Agent role

The **Cloud Healthcare Service Agent** service account is automatically created when you enable the Cloud Healthcare API and [create your first dataset](https://docs.cloud.google.com/healthcare-api/docs/datasets). This is a [Google-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed_service_accounts). You cannot delete the service account entirely, but under certain circumstances it might not appear in the [Identity and Access Management page](https://console.cloud.google.com/iam-admin/iam) and you might encounter issues with the Cloud Healthcare API.

For the Cloud Healthcare API to function correctly and complete tasks like publishing and receiving messages from Pub/Sub or writing metrics to Cloud Logging, the **Cloud Healthcare Service Agent** service account must exist and must have the **Healthcare Service Agent** IAM role.

You can recreate the **Cloud Healthcare Service Agent** service account or grant it the **Healthcare Service Agent** IAM role if you encounter any of the following issues:

  * You cannot find the **Cloud Healthcare Service Agent** service account in the [Identity and Access Management page](https://console.cloud.google.com/iam-admin/iam).
  * You can find the **Cloud Healthcare Service Agent** service account, but it does not contain the **Healthcare Service Agent** role.



Use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) to add the `healthcare.serviceAgent` role to the **Cloud Healthcare Service Agent** service account using the service account's identifier, which uses the format `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com`.

To recreate the service account or grant it the **Healthcare Service Agent** IAM role, run the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command. To find the PROJECT_ID and PROJECT_NUMBER, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com \
        --role=roles/healthcare.serviceAgent

If the request is successful, the command prompt displays a message similar to the following sample:
    
    
    Updated IAM policy for project [PROJECT_ID].
    bindings:
    ...
    - members:
      - serviceAccount:service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com
      role: roles/healthcare.serviceAgent
    ...
    etag: VALUE
    version: VALUE
    

Return to the [Identity and Access Management page](https://console.cloud.google.com/iam-admin/iam) again and verify the following:

  * The **Member** column contains a service account identifier in the format `service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount`.
  * In the same row as the **Member** column, the **Name** column contains **Cloud Healthcare Service Agent**.
  * In the same row as the **Member** column, the **Role** column contains **Healthcare Service Agent**.



## FHIR transactional bundle aborted due to cumulative heavy load

When executing a FHIR transactional bundle, you might receive an error message indicating that the request is "aborted due to cumulative heavy load for executing transactional bundle".

When you execute transactional bundles there is no bound on how much lock contention you can create. For example, if you construct a set of bundles where each bundle updates a single common Patient resource and also creates some other resources that are not common, and execute these in parallel, the time they take will rapidly increase as every bundle has to hold the lock on that common Patient for the entire transaction. As a result, they will start to time out. When the Cloud Healthcare API detects transactional bundles timing out, it temporarily rejects all transactional bundles with this error message to try to let the contention clear up.

To avoid this issue, you can try one of the following:

  * Use batch bundles if you do not need transaction semantics. Batch bundles avoid this problem entirely because they are not atomic. However, this reduces referential integrity enforcement.
  * If you can identify what resource is being updated in parallel, determine if those updates can be factored out or avoided. In FHIR, this happens if you are creating a new resource such as Observation and also updating the associated Patient (or Organization, Location, Device, etc.) that already exists and isn't changing.
  * Rate limiting on the client side; if your transactional bundles are taking a long time to execute, reduce the ingestion rate before the requests start timing out.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
