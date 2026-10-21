---
url: https://docs.cloud.google.com/hub/docs/deployments/
title: View deployments \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:22:06.475715+00:00
---

# View deployments  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  View deployments Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Hub lets you monitor failed deployments from Application Design Center, review applications that have available updates, and view recent deployment details for Google Kubernetes Engine (GKE) and Cloud Run. Tracking deployment status helps you troubleshoot deployment issues and keep your applications up-to-date.

## Overview

You can view the following information on the Deployments page:

  * View failed application deployments, and their causes, from [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview). You can then investigate the failures in App Design Center by viewing the Cloud Build logs, or you can make updates to the application. App Design Center uses Cloud Build to deploy your applications.
  * View application deployments that have updated application templates. You can then review the changes and update the applications.
  * If you set up Developer Connect insights, you can view information for recent application deployments to Google Kubernetes Engine (GKE) and Cloud Run.



## Before you begin

Ensure that you have performed the following steps:

  1. [Set up App Hub for a folder](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder).

  2. [Set up App Design Center](https://docs.cloud.google.com/application-design-center/docs/setup).

  3. [Set up Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/set-up-insights).

  4. Create and deploy your applications. To learn more, see the [App Design Center overview](https://docs.cloud.google.com/application-design-center/docs/overview).


**Note:** Cloud Hub only supports applications in a folder configured for application management. It doesn't support applications in a [host project or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

### Required roles

To get the permissions that you need to view data in Cloud Hub, ask your administrator to grant you the [Cloud Hub Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) IAM role on the management project for a folder. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To make updates to application instances or templates in App Design Center, you must have additional permissions. See the App Design Center [access control documentation](https://docs.cloud.google.com/application-design-center/docs/access-control) for information about roles and permissions.

## View failed deployments

If your application deployment failed, you can view details and take a suggested action to resolve the issue.

  1. In the Google Cloud console, go to the **Deployments** page:

[Go to Deployments](https://console.cloud.google.com/cloud-hub/deployments)

  2. Select a folder configured for application management (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)) from the project picker at the top of the page.

The **Applications infrastructure deployment notifications** table displays the most recent failed deployments from App Design Center. The **Issue** column indicates the reason for the failure based on information in the Cloud Build logs. If there are no failed deployments in the selected folder, the table is empty.

  3. Investigate an application failure with one of the following options:

     * To investigate the identified issue for an application, click **View in ADC** in the table row to view the application in App Design Center.
     * To view details for an application in App Design Center, click the application name.
     * To view a list of all deployments, click **View all Application infrastructure deployments**.



## View applications with available updates

If your deployed applications are based on templates that have new revisions, you can view the latest revision and redeploy your application to include the latest changes.

  1. In the Google Cloud console, go to the **Deployments** page,

[Go to Deployments](https://console.cloud.google.com/cloud-hub/deployments)

  2. Select a folder configured for application management (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)) from the project picker at the top of the page.

The **Applications infrastructure updates available** section displays deployed applications with an updated application template. If there are no applications with an updated template in the selected folder, the table is empty.

  3. In the list of applications, you can view an application or template by clicking on its name. To review changes to a template and apply changes, click **Review and update application**. For details about applying a template revision, see [Apply template revisions](https://docs.cloud.google.com/application-design-center/docs/deploy-applications#apply-template-revisions).




## View recent deployment details

  1. In the Google Cloud console, go to the **Deployments** page,

[Go to Deployments](https://console.cloud.google.com/cloud-hub/deployments)

  2. Select a folder configured for application management (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)) from the project picker at the top of the page.

The **Application code deployment updates** section displays recent application deployments to GKE or Cloud Run.

  3. To view more information, you can do the following:

     * To view application details in App Hub, click an application name.
     * To view the deployment details in GKE or Cloud Run, click the resource name in the **Runtime resource** column.
     * To view the deployed artifact, click the artifact in the **Artifact** column.



## What's next

  * Learn more about [App Design Center](https://docs.cloud.google.com/application-design-center/docs/overview).
  * Learn about [using Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/use-insights).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
