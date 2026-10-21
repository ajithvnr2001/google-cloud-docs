---
url: https://docs.cloud.google.com/workload-manager/docs/access-control/service-accounts/
title: Workload Manager service agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:15.907318+00:00
---

# Workload Manager service agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/access-control/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Workload Manager service agents Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the service agents that are relevant to Workload Manager.

## Service agents

Service agents are service accounts that are created and managed by Google. Service agents act as an identity for Google Cloud services to access resources within your project on your behalf. 

Service agents are created at some point after you enable and use a Google Cloud API. Upon creation, Google often grants a specific, predefined IAM role to the service agent on your project. These roles contain the minimum permissions required for the service agent to function correctly. For a full list of service agents that are granted roles, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents) in the IAM documentation. 

Workload Manager uses [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to control access and communication between resources and the associated projects. 

You can use the [Google Cloud console](https://console.cloud.google.com/) or the Workload Manager API to evaluate workloads. If you use the [Google Cloud console](https://console.cloud.google.com/), Workload Manager creates all required service agents automatically. If you use the Workload Manager API, you must manually create the service agents.

### Required roles

To get the permission that you need to create a service agent, ask your administrator to grant you the [Project Identity and Access Management (IAM) Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) IAM role on each target project in scope. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `resourcemanager.projects.setIamPolicy` permission, which is required to create a service agent. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create and grant roles to service agents

###  Google Cloud console 

If you use the [Google Cloud console](https://console.cloud.google.com/) to evaluate workloads, then Workload Manager creates service agents in the consumer projects automatically.

The email address for this service agent is `service-PROJECT_NUMBER@gcp-sa-workloadmanager.iam.gserviceaccount.com`, and it is called Workload Manager Service Account.

Workload Manager service agents require the following roles to run evaluations. If prompted, grant these roles to the service agents.

  * Workload Manager Service Agent (`roles/workloadmanager.serviceAgent`): required in the target projects.
  * Workload Manager Worker (`roles/workloadmanager.worker`): required in the consumer project only if you set a frequency for the evaluation.



###  Workload Manager API 

If you use the Workload Manager API to evaluate workloads, then you must manually create the Workload Manager service agent in the consumer projects before you create an evaluation. To create a service agent, use the [`gcloud beta services identity create`command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create):
    
    
      gcloud beta services identity create --service=workloadmanager.googleapis.com  \
          --project=PROJECT_NUMBER
    

Replace `PROJECT_NUMBER` with the numeric ID of the consumer project in which you want to create the service agent.

After creating the service agent, you must grant the following roles to the service agent:

  * Workload Manager Service Agent (`roles/workloadmanager.serviceAgent`): required in the target projects.
  * Workload Manager Worker (`roles/workloadmanager.worker`): required in the consumer project only if you set a frequency for the evaluation.



For more information, see [Grant a role to the service agent](https://docs.cloud.google.com/iam/docs/create-service-agents#grant-role).

**Tip:** A user who has the required permission to create service accounts on the target projects can create the first evaluation and create the service agents. For subsequent evaluations, Workload Manager uses the existing service agent. Other users don't require the permission to create service accounts. 

## What's next

  * To learn more about service accounts, see [Service account overview](https://docs.cloud.google.com/iam/docs/service-account-overview) in the IAM documentation. 
  * To learn more about service agents, see [Service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) in the IAM documentation. 
  * To learn how to use service accounts securely, see [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) in the IAM documentation. 
  * Learn about [Workload Manager IAM roles and permissions](https://docs.cloud.google.com/workload-manager/docs/access-control/roles-permissions).
  * Learn about [IAM roles in consumer and target projects for evaluations](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
