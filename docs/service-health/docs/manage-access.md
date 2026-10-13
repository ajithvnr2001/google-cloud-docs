---
url: https://docs.cloud.google.com/service-health/docs/manage-access/
title: Manage Personalized Service Health access \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:23.582421+00:00
---

# Manage Personalized Service Health access  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/manage-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Manage Personalized Service Health access Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses how to set permissions and enable access so you can:

  * View service health events using the Service Health dashboard.
  * Pull service health information using the Service Health API.
  * Configure alerts relevant to your projects.



## Before you begin

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

## Access the Service Health API and dashboard

Personalized Service Health provides a predefined `servicehealth.viewer` role that you can use to provide access to project members. Use this role to access the Service Health API and dashboard.

Role name  | Description  | Personalized Service Health permissions   
---|---|---  
`roles/servicehealth.viewer` Personalized Service Health viewer  | Read-only access to service health events.  | `servicehealth.location.list` `servicehealth.location.get` `servicehealth.events.list` `servicehealth.events.get` `servicehealth.organizationEvents.list` `servicehealth.organizationEvents.get` `servicehealth.organizationImpacts.list` `servicehealth.organizationImpacts.get`  
**Tip:** To gain the permissions to access Personalized Service Health while following the principle of least privilege, ask your administrator to grant you the `roles/servicehealth.viewer` (Personalized Service Health Viewer) role. If you are already granted one of the Basic Roles (Viewer, Editor or Owner roles), you already have the permissions needed to access Personalized Service Health. 

You can use the roles and permissions directly through the gcloud CLI to set up proper access controls. For example, you can grant the role directly with the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member {USER|GROUP|SERVICE_ACCOUNT} \
      --role roles/servicehealth.viewer
    

You can view the Identity and Access Management (IAM) policy for the given project with the following command:
    
    
    gcloud projects get-iam-policy PROJECT_ID
    

Alternatively, you can add the permissions directly to an existing role:
    
    
    gcloud iam roles update ROLE_ID --project=PROJECT_ID \
      --add-permissions=servicehealth.events.list
    gcloud iam roles update ROLE_ID --project=PROJECT_ID \
      --add-permissions=servicehealth.events.get
    gcloud iam roles update ROLE_ID --project=PROJECT_ID \
      --add-permissions=servicehealth.locations.list
    gcloud iam roles update ROLE_ID --project=PROJECT_ID \
      --add-permissions=servicehealth.locations.get
    

## Use APIs and services in your projects

  1. [Enable the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#enable-service-health-api-single-project) for the project.
  2. Grant the [Service Usage Consumer](https://docs.cloud.google.com/service-usage/docs/access-control#predefined_roles) role (`roles/serviceusage.serviceUsageConsumer`).



## Access logs and configure log alerts

Do the following:

  1. [Enable the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#enable-service-health-api-single-project) for the project.
  2. Get [permissions for log-based alerts](https://docs.cloud.google.com/logging/docs/access-control#lba-permissions).



If you don't want to grant the [Monitoring NotificationChannel Editor](https://docs.cloud.google.com/monitoring/access-control#notification_channels_2) role (`roles/monitoring.notificationChannelEditor`), you can grant the [Monitoring NotificationChannel Viewer](https://docs.cloud.google.com/monitoring/access-control#notif_roles_desc) role (`roles/monitoring.notificationChannelViewer`) instead to allow you to link to a notification channel to an alerting policy.

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Enable Service Health API for a single project

Setting up alerts and pulling service health information require enabling the Service Health API. You can enable the API through the Google Cloud console or Google Cloud CLI.

### Console

  1. In the APIs and Services library, go to the Service Health API.

[Go to the Service Health API](https://console.cloud.google.com/apis/library/servicehealth.googleapis.com)

Alternatively, you can go to the [API Library](https://console.cloud.google.com/apis/library) and search "Service Health API".

  2. Select the project.

  3. Select the **Enable** button.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Make sure that the most recent version of Google Cloud CLI is installed. Run the following command from the Cloud Shell:
         
         gcloud components update

  3. Create or select a new project, `PROJECT_ID`.

     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

     * Select the Google Cloud project that you created:
           
           gcloud projects config set project PROJECT_ID

  4. Enable the Service Health API in the project that you just created.
         
         gcloud services enable servicehealth.googleapis.com \
          --project PROJECT_ID
         




### Script

You can use a [script](https://docs.cloud.google.com/service-health/docs/script-enable-api) to enable the Service Health API for projects in your organization or folder.

For background information, see [Enabling an API in your Google Cloud project](https://cloud.google.com/endpoints/docs/openapi/enable-api).

The Service Health API and alerts will recognize new events a few hours after API enablement.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
