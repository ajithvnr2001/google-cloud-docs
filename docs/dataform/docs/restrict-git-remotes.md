---
url: https://docs.cloud.google.com/dataform/docs/restrict-git-remotes/
title: Restrict remote repositories \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:36.130106+00:00
---

# Restrict remote repositories  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/restrict-git-remotes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Restrict remote repositories Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use the [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to restrict the pool of third-party remote Git repositories that Dataform repositories can connect to.

## Before you begin

Before you set or edit the `dataform.restrictGitRemotes` Organization Policy, find full URLs of the remote Git repositories that you want to add to the allowlist.

To find the full URL of a remote Git repository that is already connected to a Dataform repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository, and then click **Settings**.

Keep in mind that URLs of remote repositories displayed on the **Dataform** page are shortened and cannot be used in the `dataform.restrictGitRemotes` policy.

  3. On the **Settings** page, under **Git connection settings** , copy the **Repository source** value.

The **Repository source** value is the full URL of the remote repository. You can use this URL in the `dataform.restrictGitRemotes` policy.




### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage organization policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policies:

  * `orgpolicy.constraints.list`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## About restricting remote Git repositories

You can [connect a Dataform repository](https://docs.cloud.google.com/dataform/docs/connect-repository) to a GitHub or a GitLab repository.

You might want to restrict the pool of remote repositories that Dataform repositories can connect to in order to prevent malicious actors from accessing your Dataform codebase and access tokens through unprotected copies of your repository.

You can create an Organization Policy that restricts which Git repository URLs Dataform can connect to.

The constraint for restricting remote Git repositories in Dataform is:

`constraints/dataform.restrictGitRemotes`

To use the constraint, you create an Organization Policy with an `allowedValues` list of URLs of remote Git repositories that can connect to a Dataform repository. Remote Git repositories are identified by their full URL address.

The `dataform.restrictGitRemotes` policy has a retroactive effect, which means that the constraint impacts pre-existing Dataform repositories.

**Caution:** Setting the `dataform.restrictGitRemotes` policy can block communication and version control actions between pre-existing Dataform repositories and their remote Git repositories that are not included in the `allowedValues` list.

When the Organization Policy is in place, Dataform repository can connect to only the remote Git repositories that are listed in the `allowedValues` list. Remote Git repositories that are not explicitly defined in the Organization Policy are prohibited from connecting to a Dataform repository.

**Important:** To create a Dataform repository connected to a remote Git repository that is not allowed in the `dataform.restrictGitRemotes` policy, first add the remote Git repository to the `allowedValues` list in the Organization Policy, and then [create a new Dataform repository](https://docs.cloud.google.com/dataform/docs/create-repository) and [connect it to the remote repository](https://docs.cloud.google.com/dataform/docs/connect-repository).

If you don't set the `dataform.restrictGitRemotes` policy, communication between Dataform repositories and remote Git repositories are not restricted.

You can use the `dataform.restrictGitRemotes` policy in the following ways:

`Allow all`
    Dataform repositories are allowed to connect to all remote repository URLs. Select this option if your organization does not want to block any communication with remote repositories. Alternatively, to allow all remote repository URLs, you can leave the Organization Policy unset.
`allowedValues` list of URLs
    Dataform repositories are allowed to connect to only the allow-listed remote repositories. Select this option to prevent data exfiltration.
`Deny all`
    Dataform repositories are not allowed to connect to any remote URLs. Select this option if your organization wants to block all communication and use Dataform repositories.

## Specifications for allow-listing remote Git repositories

  * You can apply this [list constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#list_policies) only to GitHub and GitLab repositories.

  * The Organization Policy is applied retroactively and affects existing Dataform repositories.

  * This constraint accepts `allowedValues`, blocking connection to all other remote Git repositories, or `Deny all`. The default is `Allow all` \- an unset Organization Policy allows communication with all remote Git repositories. We recommend setting the Organization Policy to `allowedValues`.

  * It is up to you or an administrator with the required permissions to manage and maintain the policy. Ensure communication about the policy administrator within your organization.




## Set the Organization Policy constraint at the organization level

###  Console 

  1. Go to the **Organization Policies** page.

[Go to Organization Policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. If necessary, select the required organization from the project drop-down menu.

  3. Click **Restrict git remotes for repositories in Dataform**.

  4. Click **Manage policy**. If you can't click the **Manage policy** button, you don't have the correct permissions.

  5. Select **Customize** to set the Organization Policy for specific remote Git repositories.

![Customize option on the edit Organization Policy page.](https://docs.cloud.google.com/static/compute/images/org-policy-ui-customize.png)

  6. Select the required **Policy enforcement** and **Policy type**.

  7. For **Policy values** , select **Custom**.

  8. Enter the full URL of a remote Git repository.

  9. Click **New policy value** and enter full URLs of remote Git repositories as needed.

  10. Click **Save** to apply the constraint.




###  gcloud 

To set a constraint for remote Git repositories, you first need your organization ID. You can find the organization ID by running the [`organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list) and looking for the numeric ID in the response:
    
    
    gcloud organizations list
    

The gcloud CLI returns a list of organizations in the following format:
    
    
    DISPLAY_NAME               ID
    example-organization1      29252605212
    example-organization2      1234567890
    

Use the [`gcloud resource-manager org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) to set the Organization Policy. You need to provide your policy as a JSON or YAML file. Create a JSON file in the following format:
    
    
    {
      "name": "organizations/ORGANIZATION_ID/policies/dataform.restrictGitRemotes",
      "spec": {
        "rules": [
          {
            "values": {
              "allowedValues": ["https://github.com/example/allowed-repository.git"]
            }
          }
        ]
      }
    }
    

Replace `ORGANIZATION_ID` with the numeric ID of the organization.

If you don't want Dataform repositories to be able to connect to any remote Git repositories, you can set an Organization Policy with `denyAll` set to `true`:
    
    
    {
      "name": "organizations/ORGANIZATION_ID/policies/dataform.restrictGitRemotes",
      "spec": {
        "rules": [
          {
            "denyAll": true
          }
        ]
      }
    }
    

Replace `ORGANIZATION_ID` with the numeric ID of the organization.

###  API 

Use the [`setOrgPolicy()` API](https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest) to define your constraint. Dataform is allowed to connect to the remote Git repository URLs in the `allowedValues` list you specify.

For example, the following is a request to apply the `dataform.restrictGitRemotes` constraint to an organization where selected remote Git repositories that Dataform repositories can connect to:
    
    
    POST https://orgpolicy.googleapis.com/v2/organizations/ORGANIZATION_ID/policies
    

where `ORGANIZATION_ID` is the numeric ID of the organization.

Now, in your request body, provide the selected Organization Policy for this constraint:
    
    
    {
      "name": "organizations/ORGANIZATION_ID/policies/dataform.restrictGitRemotes",
      "spec": {
        "rules": [
          {
            "values": {
              "allowedValues": ["https://github.com/example/allowed-repository.git"]
            }
          }
        ]
      }
    }
    
    
    
    Replace <code><var>ORGANIZATION_ID</var></code> with the numeric ID
    of the organization.
    

If you don't want Dataform repositories to be able to connect to any remote Git repositories, you can set an Organization Policy with `denyAll` set to `true`:
    
    
    {
      "name": "organizations/ORGANIZATION_ID/policies/dataform.restrictGitRemotes",
      "spec": {
        "rules": [
          {
            "denyAll": true
          }
        ]
      }
    }
     
    
    
    Replace <code><var>ORGANIZATION_ID</var></code> with the numeric ID
    of the organization.
    

If the Organization Policy is already set, you need to execute the following request with the Organization Policy definition as request body:
    
    
    PATCH https://orgpolicy.googleapis.com/v2/organizations/ORGANIZATION_ID/policies/dataform.restrictGitRemotes
    

## Set the Organization Policy at the project level

Setting an Organization Policy at the project level overrides or merges with the Organization Policy at the organization level. In case of a merge, `denyAll` takes precedence over `allowedValues`. For example, if the Organization Policy at the organization level is set to `denyAll`, and the merged policy at the project level lists a remote repository URL on the `allowedValues` list, Dataform is not allowed to connect to the remote repository. In such a case, the Organization Policy at the project level must override the policy at the organization level, so that Dataform can connect to the remote repository. To learn more about Organization Policy hierarchy, see [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

###  Console 

Follow the same process documented under Set the Organization Policy constraint at the organization level but choose your selected project from the project selector instead of the organization.

![Project selector.](https://docs.cloud.google.com/static/compute/images/project-selector.png)

###  gcloud 

Use the [`gcloud resource-manager org-policies set-policy` command](https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest) to set the Organization Policy. You need to provide your policy as a JSON or YAML file.

Create a JSON file in the following format:
    
    
    {
      "name": "projects/PROJECT_ID_OR_NUMBER/policies/dataform.restrictGitRemotes",
      "spec": {
        "rules": [
          {
            "values": {
              "allowedValues": ["https://github.com/example/allowed-repository.git"]
            }
          }
        ]
      }
    }
    

Replace `PROJECT_ID_OR_NUMBER` with the project ID or project number for this Organization Policy.

Then, pass in the file with your request:
    
    
    gcloud resource-manager org-policies set-policy MY_POLICY.JSON --project=PROJECT_ID
    

###  API 

Use the [`setOrgPolicy()` API](https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest) to define your constraint. Dataform is allowed to connect to the remote Git repository URLs in the `allowedValues` list you specify.

For example, the following is a request to apply the `dataform.restrictGitRemotes` constraint to an organization where Dataform repositories can connect only to the selected remote Git repositories, and the `constraints/dataform.restrictGitRemotes` policy is not set yet:
    
    
    POST https://orgpolicy.googleapis.com/v2/projects/PROJECT_ID_OR_NUMBER/policies
    

The request body contains the selected Organization Policy for this constraint:
    
    
    {
      "name": "projects/PROJECT_ID_OR_NUMBER/policies/dataform.restrictGitRemotes",
      "spec": {
        "rules": [
          {
            "values": {
              "allowedValues": ["https://github.com/example/allowed-repository.git"]
            }
          }
        ]
      }
    }
    

Replace `PROJECT_ID_OR_NUMBER` with the project ID or project number for this request.

The following is a request to apply the `dataform.restrictGitRemotes` constraint to an organization where Dataform repositories can connect to only the selected remote Git repositories, and the `constraints/dataform.restrictGitRemotes` policy is already set:
    
    
    PATCH https://orgpolicy.googleapis.com/v2/projects/PROJECT_ID_OR_NUMBER/policies/dataform.restrictGitRemotes
    

The request body contains the selected Organization Policy for this constraint:
    
    
    {
      "name": "projects/PROJECT_ID_OR_NUMBER/policies/dataform.restrictGitRemotes",
      "spec": {
        "rules": [
          {
            "values": {
              "allowedValues": ["https://github.com/example/allowed-repository.git"]
            }
          }
        ]
      }
    }
    

Replace `PROJECT_ID_OR_NUMBER` with the project ID or project number for this request.

## Best practices for allow-listing Git remotes

  * To mitigate data exfiltration risk, explicitly set the `dataform.restrictGitRemotes` constraint to allow-list a selection of trusted remote Git repositories.

  * If you only use Dataform repositories that are not connected to remote Git repositories, set the `dataform.restrictGitRemotes` constraint to `Deny All`.

  * Avoid using the `deniedValues` list with this constraint. If you define values in the `deniedValues` list, it means that only the remote Git repositories in the `deniedValues` list are restricted from connection. This could be a security concern if you want control over exactly which remote Git repositories Dataform can connect to. If you want to remove certain remote Git repositories from the `allowedValues` list, update the existing Organization Policy to remove them from the `allowedValues` list rather than putting the remote into the `deniedValues` list at a lower hierarchy.

  * If you want to set an Organization Policy over a large part of the resource hierarchy but exempt certain projects, restore the default Organization Policy by using the `setOrgPolicy` method by specifying the [`restoreDefault`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#RestoreDefault) object to allow all Dataform repositories in the projects to be connected to remote Git repositories. The policies in place for projects are not affected by the default setting.

  * Use Organization Policy together with [IAM roles](https://docs.cloud.google.com/dataform/docs/access-control) to better control access to your Dataform codebase.

  * Any Dataform repositories within the organization or project with the Organization Policy enabled are subject to this policy. If this is an issue, we recommend that you set up other services and products in a different project that does not have the Organization Policy applied, and use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), if needed.

  * Before setting the `dataform.restrictGitRemotes` policy, ensure communication about the Organization Policy and its administrator within your organization. It is up to you or an administrator with the required permissions to manage and maintain the policy.




## What's next

  * To learn more about the Organization Policy, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * To learn more about Organization Policy constraints, see [Organization Policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).
  * To learn how to manage Google Cloud resources with Resource Manager, see [Manage your Google Cloud resources](https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
