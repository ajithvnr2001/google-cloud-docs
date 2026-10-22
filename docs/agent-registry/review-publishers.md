---
url: https://docs.cloud.google.com/agent-registry/review-publishers/
title: Review skill publisher details \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:19.627393+00:00
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

In Agent Registry, a [publisher](https://docs.cloud.google.com/agent-registry/concepts#publisher) represents a verified authority that publishes agent [skills](https://docs.cloud.google.com/agent-registry/concepts#skill). Publishers dictate the prefixes that skills can use to prevent name squatting and enforce identity verification. For example, the `google-` prefix is reserved for verified Google skills.

This document explains how to review and inspect verified publisher details for your registered skills.

Creating, updating, or deleting publishers, and managing verified prefix allocations, is restricted to Google-internal administrators. The skills that you or other users create are automatically assigned to the default `private` publisher, so the published ID of a particular skill is prefixed with `private-`. You can't register custom publisher resources.

## Before you begin

Before you start, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) and [register a standalone skill](https://docs.cloud.google.com/agent-registry/register-skills). You need [the project ID](https://support.google.com/googleapi/answer/7014113) to perform these tasks.

To use the Google Cloud CLI commands in this document, make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

### Required roles

To get the permissions that you need to review skill publisher details in Agent Registry, ask your administrator to grant you the [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Other Agent Registry roles might also include the permissions required to view skill publisher details. For more information, see [Agent Registry roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

## Publisher tiers

Publishers are categorized into tiers that reflect their level of verification:

  * **First-party (`FIRST_PARTY`):** Verified Google-curated global publishers. For example, `publishers/cloud.google.com` and `publishers/discoveryengine.googleapis.com`.
  * **Private (`PRIVATE`):** The default `private` publisher automatically assigned to the skills you or other users create within the project.



## List publishers

You can list all publishers configured in your location:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab. The page displays a list of all your [registered skills](https://docs.cloud.google.com/agent-registry/register-skills).
  3. In the **Publisher** column of all registered skills, you can browse all available verified publishers that you associated with each of your skills.



###  gcloud 
    
    
    gcloud alpha agent-registry publishers list \
      --project=PROJECT_ID \
      --location=LOCATION
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.



###  REST 
    
    
    curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/publishers"
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.



## View publisher details

You can inspect details for a specific publisher:

###  Console 

  1. In the Google Cloud console, go to the **Agent Registry** page: 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. Select the **Skills** tab.
  3. Click the name of a skill to open its details page.
  4. In the **Skill details** section, locate the Uniform Resource Name (URN) of the skill.

Use this skill URN field to find a specific publisher's assets. For example, the format for Google-created skills is `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`




###  gcloud 
    
    
    gcloud alpha agent-registry publishers describe PUBLISHER_ID \
      --project=PROJECT_ID \
      --location=LOCATION
    

Replace the following:

  * `PUBLISHER_ID`: The ID of the publisher you want to review.
  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.



###  REST 
    
    
    curl -X GET \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          "https://agentregistry.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/publishers/PUBLISHER_ID"
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `LOCATION`: The registry location.
  * `PUBLISHER_ID`: The ID of the publisher you want to review.



## What's next

  * Learn how to [register standalone skills](https://docs.cloud.google.com/agent-registry/register-skills).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
