---
url: https://docs.cloud.google.com/run/docs/configuring/tags/
title: Configure tags for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:34.145494+00:00
---

# Configure tags for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure tags for services Stay organized with collections  Save and categorize content based on your preferences. 

Tags are key-value pairs you can apply to your services for fine-grained access control. Tag administrators create tags for resources across Google Cloud at the organization or project level and manage them in [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing). Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag.

Tags _attached_ to Cloud Run services should not be confused with Cloud Run [traffic tags](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags) that allow you to route traffic to specific Cloud Run revisions.

**Note:** In contrast to tags, [labels](https://docs.cloud.google.com/run/docs/configuring/services/labels) are used to identify resources for billing-related reasons, filtering logs, and so forth.

## Required roles

To get the permissions that you need to attach or detach tags, ask your administrator to grant you the following IAM roles on the Cloud Run service: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)



To manage access on the tag value resource in Resource Manager, your account must also have the [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) role [granted for the tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#managing_access). The tag value is the resource that is attached to the Cloud Run service.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Attach tags to Cloud Run services

Note that attaching a tag to your service _does not_ result in the creation of a new revision.

You can attach or detach tags using the Google Cloud console or the Google Cloud CLI.

### Console

  1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Check the checkbox at the left of the service you are setting the tag on.

  3. Click **Tags** above the services list to display the tags pane.

![Cloud Run Google Cloud console showing the tags panel for attaching and detaching service tags.](https://docs.cloud.google.com/static/run/docs/images/tags.png)

  4. If your organization doesn't appear in the **Tags** panel, click **Select scope**. Select your organization and click **Open**.

  5. To attach a new tag to the service, click **Add Tag** and select one of the tag keys in the key dropdown menu, and select a value from the value dropdown menu.

  6. Click **Save** then confirm your changes if prompted.




###  gcloud 

You can update tags for a service using the command:
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAG_VALUE \
        --parent=//run.googleapis.com/projects/PROJECT_ID/locations/REGION/services/SERVICE \
        --location=REGION

To update more than one tag, supply a comma-delimited list of tag values.

Replace

  * TAG_VALUE with the value for the key: you can use these different types of identifiers: a permanent ID such as `tagValues/12345678901`, a namespaced value such as `123456789012/env/prod` or a short name such as `prod`
  * PROJECT_ID with project ID of your Google Cloud project
  * REGION with region your Cloud Run service is deployed to
  * SERVICE with name of your Cloud Run service



## Detach tags from Cloud Run services

You can use the console or the command line to detach tags from your service.

### Console

  1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Check the checkbox at the left of the service you are detaching the tag from.

  3. Click **Tags** above the services list to display the tags pane.

  4. Locate the tag you want to detach.

  5. Hold the pointer of your cursor to the right of the _Value_ drop-down menu for the tag to display the trash icon, and click the trash icon.

  6. Click **Save** and confirm your changes if prompted.




###  gcloud 

To detach a tag from a service:
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAG_VALUE \
        --parent=//run.googleapis.com/projects/PROJECT_ID/locations/REGION/services/SERVICE \
        --location=REGION

To detach more than one tag, supply a comma delimited list of tag values.

Replace

  * TAG_VALUE with the value for the key: you can use these different types of identifiers: a permanent ID such as `tagValues/12345678901`, a namespaced value such as `123456789012/env/prod` or a short name such as `prod`
  * PROJECT_ID with project ID of your Google Cloud project
  * REGION with region your Cloud Run service is deployed to
  * SERVICE with name of your Cloud Run service



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
