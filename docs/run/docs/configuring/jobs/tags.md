---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/tags/
title: Tag jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:55.805253+00:00
---

# Tag jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Tag jobs Stay organized with collections  Save and categorize content based on your preferences. 

Tags are key-value pairs you can apply to your jobs for fine-grained access control. Tag administrators create tags for resources across Google Cloud at the organization or project level and manage them in [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing). Tags provides a way to conditionally allow or deny policies based on whether a resource has a specific tag.

**Note:** In contrast to tags, [labels](https://docs.cloud.google.com/run/docs/configuring/jobs/labels) are used to identify resources for billing-related reasons, filtering logs, and so forth.

## Required roles

To get the permissions that you need to attach or detach tags, ask your administrator to grant you the following IAM roles on the Cloud Run job: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)



To manage access on the tag value resource in Resource Manager, your account must also have the [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) role [granted for the tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#managing_access). The tag value is the resource that is attached to the Cloud Run job.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Attaching tags

Attach tags using the Google Cloud CLI.

###  gcloud 

Update tags for a job using the command:
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAG_VALUE \
        --parent=//run.googleapis.com/projects/PROJECT_ID/locations/REGION/jobs/JOB \
        --location=REGION

To update more than one tag, supply a comma delimited list of key/value pairs.

Replace

  * TAG_VALUE with the value for the key. You can use these different types of identifiers: a permanent ID such as `tagValues/12345678901`, a namespaced value such as `123456789012/env/prod` or a short name such as `prod`
  * PROJECT_ID with project ID of your Google Cloud project
  * REGION with region your Cloud Run job is deployed to
  * JOB with name of your Cloud Run job



## Detaching a tag

Use the Google Cloud CLI to detach tags from your job.

###  gcloud 

To detach a tag from a job:
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAG_VALUE \
        --parent=//run.googleapis.com/projects/PROJECT_ID/locations/REGION/jobs/JOB \
        --location=REGION

To detach more than one tag, supply a comma delimited list of key/value pairs.

Replace

  * TAG_VALUE with the value for the key: you can use these different types of identifiers: a permanent ID such as `tagValues/12345678901`, a namespaced value such as `123456789012/env/prod` or a short name such as `prod`
  * PROJECT_ID with project ID of your Google Cloud project
  * REGION with region your Cloud Run job is deployed to
  * JOB with name of your Cloud Run job



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
