---
url: https://docs.cloud.google.com/agent-registry/review-publishers/
title: Review skill publisher details \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:17.908787+00:00
---

# Review skill publisher details  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/review-publishers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Review skill publisher details Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In Agent Registry, publishers let you verify the authority behind registered standalone skills to help prevent unauthorized use of publisher names. Each [publisher](https://docs.cloud.google.com/agent-registry/skills-architecture#publishers) establishes the verified domain or ID prefix for [skill identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers), such as `cloud.google.com` for Google-managed skills or `private-` for manually registered skills.

Google controls publisher creation, updates, and deletions. Skills that you create are automatically assigned to the default `private` publisher, which uses the `private-` prefix. You can list and inspect publisher details in Agent Registry to verify the ownership of registered skills.

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) and [register a standalone skill](https://docs.cloud.google.com/agent-registry/register-skills).
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  3. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



### Required roles

To get the permissions that you need to review skill publisher details in Agent Registry, ask your administrator to grant you the [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) IAM role on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Other Agent Registry roles might also include the permissions required to view skill publisher details. For more information, see [Agent Registry roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

## Publisher tiers

Publishers are categorized into tiers that reflect their level of verification:

  * **Google-managed (`FIRST_PARTY`)**: verified publishers that Google manages, such as `cloud.google.com` and `discoveryengine.googleapis.com`.
  * **Private (`PRIVATE`)**: the default `private` publisher automatically assigned to the skills you or other users create within the project.



## List publishers

You can list all publishers configured in your location:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab. The page displays a list of all your [registered skills](https://docs.cloud.google.com/agent-registry/register-skills).
  3. In the **Publisher** column of all registered skills, you can browse all available verified publishers that you associated with each of your skills.



###  gcloud 

To list all verified publishers in a location, run the [`gcloud alpha agent-registry publishers list`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/publishers/list) command:
    
    
    gcloud alpha agent-registry publishers list \
        --project=PROJECT_ID \
        --location=LOCATION
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.



###  REST 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/publishers"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.



## View publisher details

You can inspect details for a specific publisher:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Click the name of a skill to open its details page.
  4. In the **Skill details** section, locate the [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) of the skill.

Use this skill identifier field to find a specific publisher's assets. For example, the format for Google-managed skills is `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`.




###  gcloud 

To view details for a specific publisher, run the [`gcloud alpha agent-registry publishers describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/publishers/describe) command:
    
    
    gcloud alpha agent-registry publishers describe PUBLISHER_ID \
        --project=PROJECT_ID \
        --location=LOCATION
    

Replace the following:

  * `PUBLISHER_ID`: the ID of the publisher you want to review.
  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.



###  REST 
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/publishers/PUBLISHER_ID"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the registry location.
  * `PUBLISHER_ID`: the ID of the publisher you want to review.



## What's next

  * Learn how to [register standalone skills](https://docs.cloud.google.com/agent-registry/register-skills).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
