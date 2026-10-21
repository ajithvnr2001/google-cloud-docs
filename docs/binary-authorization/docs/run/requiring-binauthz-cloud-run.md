---
url: https://docs.cloud.google.com/binary-authorization/docs/run/requiring-binauthz-cloud-run/
title: Require Binary Authorization for Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:11.252183+00:00
---

# Require Binary Authorization for Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/run/requiring-binauthz-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Require Binary Authorization for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure an organization policy that requires Binary Authorization enforcement of container images that are deployed to Cloud Run. You can require enforcement for a project, folder, or an organization.

## Before you begin

You must have permission to modify [organization policies](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy) to set this constraint. For example, the [`orgpolicy.policyAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy) role has permission to set organization policy constraints. The [`resourcemanager.organizationAdmin`](https://docs.cloud.google.com/resource-manager/docs/access-control-org) role has permission to add a user as an Organization Policy Administrator. Read the [Using Constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin) page to learn more about managing policies at the organization level. You can [use a custom constraint](https://docs.cloud.google.com/run/docs/securing/custom-constraints#require-binary) to require that Binary Authorization is set to `default` at the project level.

## Set the organization policy

This section shows you how to set an organization policy to require Binary Authorization enforcement on images deployed to Cloud Run. You can set the policy using the Google Cloud console or the Google Cloud CLI.

**Warning:** Setting this policy can affect running services. If you have running services, we recommend you [enable dry-run mode in the policy](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run) and review [Cloud Audit Logs entries for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run) before updating the policy to be more restrictive.

###  Console 

To set the organization policy using Google Cloud console, do the following:

  1. In the Google Cloud console, go to the Organization policies page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the **Project Selector** at the top of the page, do the following:

     1. Select the organization for which you want to set the policy.

You can set the policy at the organization, folder or project level using the [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#configuring_access_to_folders) and [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects), respectively. To learn more, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).

     2. To complete the selection, click **Open**.

  3. In **Filter** , enter the following:
         
         Allowed Binary Authorization Policies (Cloud Run)
         

  4. To edit the policy details, in **Policy details** , click **Edit**.

  5. In **Applies to** , click **Customize**.

**Note:** You can inherit settings from a parent project or organization by clicking **Inherit parent's policy**.
  6. Make sure **Policy type** is set to `Allow`.




To set the default Binary Authorization policy that the organization policy requires, do the following:

  1. In **Custom values** , in the text field, type `default`.

The policy value must be set to `default`. Setting the value to `default` configures Binary Authorization to use the policy in the same project as your Cloud Run services.

  2. To save this organization policy, click **Save**.




### gcloud

To set the organization policy using `gcloud`, do the following:
    
    
    gcloud resource-manager org-policies allow run.allowedBinaryAuthorizationPolicies \
      default \
      --organization=ORGANIZATION_ID
    

Replace ORGANIZATION_ID with the numeric ID of the organization.

You can also apply the organization policy to a folder or a project with the `--folder` or the `--project` flags, and the [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#configuring_access_to_folders) and [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects), respectively.

**Note:** It can take up to a few minutes for the organization policy to update and require Binary Authorization enforcement for Cloud Run.

## View the organization policy

You can view the organization policy using the Google Cloud console or `gcloud`.

###  Console 

  1. In the Google Cloud console, go to the Organization policies page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the **Project Selector** , select the organization for which you want to view the policy.

  3. In **Filter** , enter the following:
         
         Allowed Binary Authorization Policies (Cloud Run)
         

  4. To complete the selection, click **Open**.

  5. You can view the `Allowed Binary Authorization Policies (Cloud Run)` policy configuration.




###  gcloud 

To view the organization policy that requires Binary Authorization for Cloud Run on an organization, enter the following command:
    
    
    gcloud resource-manager org-policies describe \
      run.allowedBinaryAuthorizationPolicies \
      --effective \
      --organization=ORGANIZATION_ID
    

Replace ORGANIZATION_ID with the numeric ID of the organization.

## Revert the policy

You can revert the policy so that Cloud Run no longer requires Binary Authorization enforcement using the Google Cloud console or `gcloud`.

###  Console 

To revert the policy using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the Organization policies page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the **Project Selector** , select the organization for which you want to revert the policy.

  3. In **Filter** , enter the following:
         
         Allowed Binary Authorization Policies (Cloud Run)
         

  4. To complete the selection, click **Open**.

  5. To edit the policy details, in **Policy details** , click **Edit**.

  6. In **Applies to** , select `Inherit parent's policy`.

  7. To save the organization policy, click **Save**.




###  gcloud 

To revert the policy using `gcloud`, do the following:
    
    
    gcloud resource-manager org-policies delete \
      run.allowedBinaryAuthorizationPolicies \
      --organization=ORGANIZATION_ID
    

Replace ORGANIZATION_ID with the numeric ID of the organization.

The command returns the following:
    
    
    Deleted [<Empty>]
    

Alternatively, you can view the org policy and note that the **Inheritance** is set to `Inherit`, instead of `custom` and there is no custom value set.

## What's next

  * [Enable Binary Authorization on a Cloud Run service](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run)
  * [Deploy a prebuilt Cloud Run service](https://docs.cloud.google.com/run/docs/quickstarts/deploy-container)
  * [Configure a Binary Authorization policy](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
