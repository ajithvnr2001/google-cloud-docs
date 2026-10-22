---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/spaces-roles-permissions/
title: Apigee Spaces roles and permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:22.077703+00:00
---

# Apigee Spaces roles and permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/spaces-roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Spaces roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page lists the [Identity and Access Management](https://docs.cloud.google.com/iam/docs) roles and permissions required to use and manage Apigee Spaces and Space resources.

When using Spaces, it is important to note that IAM roles and permissions are primarily granted at the Space level and enable Apigee users to view and manage only the subset of API resources assigned to the Space. This is a change in behavior from Apigee contexts where Spaces are not used, and the roles and permissions granted to Apigee users for the management of API resources typically enable access to all resources of that type.

To learn more about the default roles and permissions required when using Spaces, see the following sections: 

  * Roles and permissions to create and manage Apigee Spaces
  * View Space resources in Google Cloud console
  * View and assign roles using IAM in the Google Cloud console



## Roles and permissions to create and manage Apigee Spaces

New roles and permissions have been added to IAM to make using Apigee Spaces in Apigee organizations easier for common use cases, as shown in the following sections. 

### Predefined roles for Apigee Spaces

Role | Description | Scope  
---|---|---  
`apigee.spaceContentEditor` | Provides full access to resources that can be associated with a Space. This role should be granted at the Space level. | Apigee Space  
`apigee.spaceContentViewer` | Provides read-only access to resources that can be associated with a Space. This role should be granted at the Space level. | Apigee Space  
`apigee.spaceConsoleUser` | Provides the minimum permissions required to manage resources in a Space using the Google Cloud console. Granted at the Google Cloud project level to users with access to resources in that Space. | Google Cloud project  
  
To allow Space members to manage resources in that Space, use the `setIamPolicy` method on a Space resource to grant the `apigee.spaceContentEditor` role to the member. For more information, see [ Add an organization member to a Space](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces#members-roles).

To allow Space members to use the Apigee UI to manage Space resources, grant the members the `apigee.spaceConsoleUser` role on the Google Cloud project. For more information, see View Space resources in Google Cloud console.

**Note:** The roles described in this section do not give Space members the ability to deploy or undeploy API proxies or shared flows. To allow Space members to manage deployments, set an IAM policy at the Apigee environment or Google Cloud project level granting the `apigee.environment.admin` role to the Space member.

If you have a more complex scenario, or would like to understand how usage of Spaces changes the IAM permission hierarchy, see [ IAM permission hierarchy in Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/iam-permission-hierarchy-spaces).

### Permissions required to create and manage Apigee Spaces

New permissions have been added to IAM to enable the creation and management of Spaces, as described in the following table. Apigee users assigned the `apigee.admin` role will have the required permissions to create and manage a Space in an Apigee organization.

Operation | Permission required  
---|---  
**Create a Space** | `apigee.spaces.create`  
**Update a Space** | `apigee.spaces.update`  
**Delete a Space** | `apigee.spaces.delete`  
**Get details of a Space** | `apigee.spaces.get`  
**List all Spaces in an Apigee organization** | `apigee.spaces.list`  
**Get the IAM policy associated with a Space** | `apigee.spaces.getIamPolicy`  
**Set the IAM policy associated with a Space** | `apigee.spaces.setIamPolicy`  
  
## View Space resources in Google Cloud console

To view API resources associated with Spaces using the Apigee UI, users must be granted a custom role: `apigee.spaceConsoleUser`.

**Note** : This role should be granted to users at the Google Cloud project level using IAM and _not_ at the Space level.

For more information on using the UI to view and manage API resources in Spaces, see [Manage API resources in Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/manage-space-resources). 

Check to ensure that this custom role is granted to any user who wants to use Apigee UI to view and manage Space resources. If the `apigee.spaceConsoleUser` role is not already available in IAM for your users, ask your organization administrator to add the role for the organization's Google Cloud project.

The administrator can create the role using the following command: 
    
    
    gcloud iam roles create apigee.spaceConsoleUser \
      --project="PROJECT_ID" \
      --title="Apigee Space Console User" \
      --description="Apigee Space Console User"\
      --permissions="apigee.entitlements.get,apigee.organizations.get,apigee.organizations.list,apigee.projectorganizations.get,resourcemanager.projects.get,apigee.spaces.list,apigee.spaces.get,apigee.deployments.list,apigee.environments.list,apigee.environments.get,apigee.envgroups.list,apigee.envgroupattachments.list,apigee.instances.list,apigee.apps.list" \
      --stage=GA

Replace PROJECT_ID with the name of the Google Cloud project where the Apigee organization was created.

## View and assign roles using IAM in the Google Cloud console

You can confirm the role assignments and permissions granted to Space members and organization administrators at the Google Cloud project level using IAM in the Google Cloud console. 

#### To check for the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### To grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. In the **Select a role** list, select a role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



To check for the IAM policies applied at the Space level, see [ Manage members and roles in a Space](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces#members-roles).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
