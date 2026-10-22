---
url: https://docs.cloud.google.com/integration-connectors/docs/service-account/
title: Service account \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:59.049627+00:00
---

# Service account  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Service account

A service account is a special type of Google account used by applications or compute workloads, rather than individual users, to make authorized API calls. Each service account is uniquely identified by an email address. Applications can authenticate as the service account itself, gaining access to all resources the service account has permissions for. A common method is to attach a service account to a resource like a Compute Engine instance. 

There are several types of service accounts in Google Cloud, including user-managed service accounts that you create, default service accounts created automatically by certain services, and service agents managed by Google Cloud to act on your behalf. Applications can obtain short-lived credentials or, less securely, use service account keys to authenticate. 

Service accounts function as both principals and resources within IAM. As principals, you can grant them roles to access Google Cloud resources. As resources, you can grant other principals permissions to interact with the service account, such as allowing a user to impersonate it. 

It's recommended to create the service account in the same project as the connector. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

**Note:** When you're using a service account from a different Google Cloud project than the one where your connection is configured, you might encounter a `PERMISSION_DENIED` error with the message "Permission `iam.serviceAccounts.getAccessToken` denied". This error occurs because the default permissions granted to the Integration Connectors service agent (P4SA) don't extend across project boundaries. To resolve this, in the project that contains the service account, grant the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`) to the Integration Connectors service agent. For more information, see [Service account](https://docs.cloud.google.com/iam/docs/service-account-overview). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
