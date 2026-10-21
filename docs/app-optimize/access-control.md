---
url: https://docs.cloud.google.com/app-optimize/access-control/
title: Access control with IAM \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:05:47.593154+00:00
---

# Access control with IAM  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Guides ](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

App Optimize API uses Identity and Access Management (IAM) to control access to its resources, such as reports and operations. IAM lets you grant granular access to specific App Optimize API resources and helps prevent unwanted access to other resources.

This document describes the IAM permissions and roles that apply to App Optimize API.

## Permissions overview

Permissions allow users to perform specific actions on App Optimize API resources. The following table lists the permissions for App Optimize API:

Permission | Description  
---|---  
`appoptimize.operations.cancel` | Cancel a long-running operation.  
`appoptimize.operations.delete` | Delete a long-running operation.  
`appoptimize.operations.get` | Get the status of a long-running operation.  
`appoptimize.operations.list` | List long-running operations.  
`appoptimize.reports.create` | Create an App Optimize API report resource.  
`appoptimize.reports.delete` | Delete an App Optimize API report resource.  
`appoptimize.reports.get` | Read an App Optimize API report resource's configuration metadata.   
This does not grant access to report data.  
`appoptimize.reports.getData` | Read the data contained within an App Optimize API report.  
`appoptimize.reports.list` | List App Optimize API report resources in a project.  
  
## Predefined roles

IAM provides predefined roles that grant a set of related permissions. The following roles are available for App Optimize API:

Role | Title | Description  
---|---|---  
`roles/appoptimize.admin` | App Optimize Admin | Full control over App Optimize API reports and operations.  
`roles/appoptimize.viewer` | App Optimize Viewer | Read access to App Optimize API report metadata, report data, and operations.  
  
### Grant an IAM role

You can grant an IAM role to a principal using the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click person_add **Grant Access**.

  3. In the **New principals** field, enter the email address of the principal to be granted the role.

  4. Click the **Select a role** drop-down menu.

  5. Filter for **App Optimize** roles and select the role to grant, such as App Optimize Admin or App Optimize Viewer.

  6. Click **Save**.




###  gcloud 

  1. If you haven't already done so, [install and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

  2. Use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command to grant the role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="PRINCIPAL" \
             --role="ROLE_NAME"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `PRINCIPAL`: the identifier for the principal, such as `user:my-user@example.com` or `group:my-group@example.com`. See [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).
     * `ROLE_NAME`: the role to grant, such as `roles/appoptimize.admin` or `roles/appoptimize.viewer`.



For example, to grant the App Optimize Admin role to the user `test-user@example.com` on the project `my-appoptimize-project`:
    
    
    gcloud projects add-iam-policy-binding my-appoptimize-project \
        --member="user:test-user@example.com" \
        --role="roles/appoptimize.admin"
    

For more information on granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### App Optimize Admin

App Optimize Admin grants full control over App Optimize API resources, and includes permissions granted to App Optimize Viewer.

Role name | Included permissions  
---|---  
`roles/appoptimize.admin` | 

  * `appoptimize.operations.*`
  * `appoptimize.reports.*`

  
  
### App Optimize Viewer

App Optimize Viewer grants permissions to read App Optimize API reports, their metadata, and operations.

Role name | Included permissions  
---|---  
`roles/appoptimize.viewer` | 

  * `appoptimize.operations.get`
  * `appoptimize.operations.list`
  * `appoptimize.reports.get`
  * `appoptimize.reports.getData`
  * `appoptimize.reports.list`

  
  
## Permissions to create reports

To create a report, a user, service account, or other principal must have:

  * The `appoptimize.reports.create` permission on the project where the report resource will be created. This permission is included in the App Optimize Admin (`roles/appoptimize.admin`) role.

  * The `billing.resourceCosts.get` permission on all the projects scoped in the report. This permission is provided by roles such as Cloud Hub Operator (`roles/cloudhub.operator`) or the basic Viewer (`roles/viewer`).

  * Permissions to access the data sources encompassed by the report's scope, dimensions, and metrics. App Optimize API checks these permissions when the report is created. The roles that grant this data source access include:

    * For CPU and memory utilization metrics: Monitoring Viewer (`roles/monitoring.viewer`) on the scoped resources.

    * For App Hub application scopes and dimensions: App Management Viewer (`roles/apphub.appManagementViewer`) on the applications' App Hub host project.

If you are generating a report on an App Hub application, which can be made up of multiple projects, you must have the required monitoring and billing permissions on all of the application's associated projects to create the report.




## Permissions to read report data

Once a report has been successfully created, a principal needs only the `appoptimize.reports.getData` permission to read the generated data. This permission can be on the project where the report was created, or on the report itself, and is included in both the App Optimize Admin and App Optimize Viewer roles.

## What's next

  * Learn more about IAM [roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview).
  * Learn how to [create a report](https://docs.cloud.google.com/app-optimize/create-report).
  * Review the [App Optimize API overview](https://docs.cloud.google.com/app-optimize/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
