---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/enforce-confidential-vm-use/
title: Enforce Confidential VM use \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:43.531979+00:00
---

# Enforce Confidential VM use  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/enforce-confidential-vm-use/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Enforce Confidential VM use Stay organized with collections  Save and categorize content based on your preferences. 

To make sure all VM instances created in your organization are Confidential VM instances, you can use an [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

## Required roles

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

## Enable the constraint

To enable the constraint on VM instances, complete the following instructions:

### Console

  1. In the Google Cloud console, go to the **Organization policies** page:

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. Click the switcher box at the top of the page, and choose the organization to apply the constraint to. To apply the constraint to a project, select a project instead.

  3. In the filter box, enter `restrict non-confidential computing`, and then click the **Restrict Non-Confidential Computing** policy.

  4. On the **Policy details** page for **Restrict Non-Confidential Computing** , click edit **Manage policy**.

**Note:** If edit **Manage policy** is disabled, you don't have permission to set organization policy.
  5. In the **Applies to** section, click **Customize**.

  6. In the **Policy enforcement** section, choose one of the following options:

     * **Merge with parent.** Merge your new policy setting with that of a parent organization.

     * **Replace.** Replace the current policy setting and ignore that of the parent organization.

  7. In the **Rules** section, click **Add a rule**.

  8. In the **Policy values** box, select **Custom** , and set the **Policy type** to **Deny**.

  9. In the **Custom values** box, enter `compute.googleapis.com` as the [API service name](https://docs.cloud.google.com/apis/design/glossary#api_service_name) you want to enforce the policy on.

  10. Click **Done**.

  11. Click **Set policy**.




### gcloud
    
    
    gcloud resource-manager org-policies deny \
        constraints/compute.restrictNonConfidentialComputing compute.googleapis.com \
        --organization=ORGANIZATION_ID
    

Provide the following value:

  * `ORGANIZATION_ID`: The ID of the organization to add the constraint to.

How to find a Google Cloud organization ID

### Console

To find a Google Cloud organization ID, complete the following steps:

    1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

    2. Click the **switcher** box in the menu bar.
    3. Click the **Select from** box, and then select your organization.
    4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve a Google Cloud organization ID with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"




To apply the constraint at the project level instead of the organization level, use `--project=PROJECT_ID` instead of `--organization=ORGANIZATION_ID`.

Alternatively, you can set policies with a policy file using [`set-policy` commands](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy).

## Verify the constraint

To verify the constraint:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the project selector at the top of the page, and choose a project to create a VM in.

  3. Click **Create instance**.

  4. In the **Confidential VM service** section, verify that your policy is enforced.


**Note:** Organization policies can take a moment to propagate. If you don't see the change, wait a few moments, and then try again.

## Disable the constraint

To disable the constraint, complete the following instructions:

### Console

  1. In the Google Cloud console, go to the **Organization policies** page:

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. Click the switcher box at the top of the page, and choose the organization to apply the constraint to. To apply the constraint to a project, select a project instead.

  3. In the filter box, enter `restrict non-confidential computing`, and then click the **Restrict Non-Confidential Computing** policy.

  4. On the **Policy details** page for **Restrict Non-Confidential Computing** , click edit **Manage policy**.

**Note:** If edit **Manage policy** is disabled, you don't have permission to set organization policy.
  5. Click the rule to expand it.

  6. In the **Policy values** box, select **Allow all** , and then click **Done**.

  7. Click **Set policy**.




### gcloud
    
    
    gcloud resource-manager org-policies delete \
        constraints/compute.restrictNonConfidentialComputing \
        --organization=ORGANIZATION_ID
    

Provide the following value:

  * `ORGANIZATION_ID`: The ID of the organization to delete the constraint from.

How to find a Google Cloud organization ID

### Console

To find a Google Cloud organization ID, complete the following steps:

    1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

    2. Click the **switcher** box in the menu bar.
    3. Click the **Select from** box, and then select your organization.
    4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve a Google Cloud organization ID with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"




To delete the constraint at the project level instead of the organization level, use `--project=PROJECT_ID` instead of `--organization=ORGANIZATION_ID`.

Alternatively, you can set policies with a policy file using [`set-policy` commands](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy).

## What's next

To learn more about the core concepts of organization policy:

  * Read the [overview of organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

  * Read about [what constraints are](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints).

  * Read about [the available organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

  * Read how to [use constraints to create organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
