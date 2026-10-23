---
url: https://docs.cloud.google.com/source-repositories/docs/configure-access-control/
title: Access control with IAM \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:41.791301+00:00
---

# Access control with IAM  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/configure-access-control/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Access control in Google Cloud is controlled using [Identity and Access Management](https://docs.cloud.google.com/iam) (IAM). IAM allows you to set permissions specifying **who** has **what** kind of access to **which** resources in your project.

Cloud Source Repositories uses IAM for access control. You can use IAM to add team members to your project and to grant them permissions to create, view, and update repositories.

This page describes the IAM permissions and roles that apply to Cloud Source Repositories.

## Permissions

With IAM, every action on a repository in Cloud Source Repositories requires that the account initiating the action has the appropriate permissions. You don't grant specific permissions to an account. Instead, you grant a role that contains the appropriate set of permissions.

The following table describes the permissions available in Cloud Source Repositories.

Permission | Description  
---|---  
`source.repos.list` | List repositories within a project.  
`source.repos.create` | Create a repository within a project.  
`source.repos.get` | Clone, fetch, and browse repositories.  
`source.repos.update` | Push changes to a repository.  
`source.repos.updateRepoConfig` | Change a repository configuration.  
`source.repos.delete` | Delete a repository.  
`source.repos.getIamPolicy` | Read/view the IAM policy of a repository.  
`source.repos.setIamPolicy` | Change the IAM policy of a repository.  
`source.repos.getProjectConfig` | Read/view the Google Cloud project configuration.  
`source.repos.updateProjectConfig` | Change the Google Cloud project configuration.  
  
## Roles

You assign permissions to accounts through the use of roles. The following table lists the roles available for Cloud Source Repositories.

Role | Role Title  
---|---  
`roles/source.reader` | Source Repository Reader  
`roles/source.writer` | Source Repository Writer  
`roles/source.admin` | Source Repository Administrator  
  
## Roles and permissions matrix

Use the table below to select the appropriate role for an account based on the types of actions you want that account to perform.

Capability | `reader` | `writer` | `admin`  
---|---|---|---  
List repositories |  |  |   
Clone, fetch, and browse repositories |  |  |   
Update repositories |  |  |   
Create repositories |  |  |   
Update repository configurations |  |  |   
Delete repositories |  |  |   
View IAM policies |  |  |   
Set IAM policies |  |  |   
View Google Cloud project configurations |  |  |   
Update Google Cloud project configurations |  |  |   
  
## Custom roles

In addition to the predefined roles, Cloud Source Repositories also supports custom roles. For more information, see [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) in the IAM documentation.

**Note:** The `source.repos.update` permission cannot be granted to a custom role.

## Granting principals access

In IAM, you grant access to **principals**. There are multiple types of principals. For a complete list, see [Principal types](https://docs.cloud.google.com/iam/docs/principals-overview#principal-types).

For specific steps on granting member access, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You can't make a Google Cloud repository public. As a result, Cloud Source Repositories doesn't support the following member types:

  * allAuthenticatedUsers
  * allUsers



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
