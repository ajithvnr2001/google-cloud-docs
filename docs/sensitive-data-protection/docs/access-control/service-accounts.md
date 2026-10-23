---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/service-accounts/
title: Sensitive Data Protection service agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:43.917751+00:00
---

# Sensitive Data Protection service agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/service-accounts/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Sensitive Data Protection service agents Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the service agents that are relevant to Sensitive Data Protection.

## Service agents

Service agents are service accounts that are created and managed by Google. Service agents act as an identity for Google Cloud services to access resources within your project on your behalf. 

Service agents are created at some point after you enable and use a Google Cloud API. Upon creation, Google often grants a specific, predefined IAM role to the service agent on your project. These roles contain the minimum permissions required for the service agent to function correctly. For a full list of service agents that are granted roles, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents) in the IAM documentation. 

To access both Google Cloud resources and make calls to Sensitive Data Protection, Sensitive Data Protection uses the credentials of the Cloud Data Loss Prevention Service Agent to authenticate to other APIs. A service agent is a special type of service account that runs internal Google processes on your behalf. The service agent is identifiable by the following email: 
    
    
    service-PROJECT_NUMBER@dlp-api.iam.gserviceaccount.com
    

The Cloud Data Loss Prevention Service Agent is created when it is first needed. You can create it in advance by calling [`InspectContent`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect):
    
    
    curl --request POST \
      "https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/us-central1/content:inspect" \
      --header "X-Goog-User-Project: PROJECT_ID" \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      --header 'Accept: application/json' \
      --header 'Content-Type: application/json' \
      --data '{"item":{"value":"google@google.com"}}' \
      --compressed

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

The Cloud Data Loss Prevention Service Agent is automatically granted common permissions on the project that are needed for inspecting resources and is listed in the Identity and Access Management section of the Google Cloud console. The service agent exists for the life of the project and is deleted only when the project is deleted. Sensitive Data Protection relies on this service agent, so do not remove it.

**Note:** If you use Sensitive Data Protection to scan critical resources, such as those protected by additional custom Identity and Access Management roles, assign those additional IAM roles to the Cloud Data Loss Prevention Service Agent. For example, if you want to use Sensitive Data Protection to inspect files in Google Cloud that are restricted to only a subset of individuals, grant the appropriate role to the Cloud Data Loss Prevention Service Agent.**Warning:** If you remove the Cloud Data Loss Prevention Service Agent or revoke its roles, all [jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs), [job triggers](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers), and [discovery operations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) that use it fail.

For more information about the Cloud Data Loss Prevention Service Agent in discovery operations, see [Service agent container and service agent](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container). 

## What's next

  * To learn more about service accounts, see [Service account overview](https://docs.cloud.google.com/iam/docs/service-account-overview) in the IAM documentation. 
  * To learn more about service agents, see [Service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) in the IAM documentation. 
  * To learn how to use service accounts securely, see [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) in the IAM documentation. 
  * Learn more about how the sensitive data discovery service uses [service agent containers and service agents](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container) to profile your data resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
