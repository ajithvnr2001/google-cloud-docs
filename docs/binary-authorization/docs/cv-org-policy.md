---
url: https://docs.cloud.google.com/binary-authorization/docs/cv-org-policy/
title: Require continuous validation check-based platform policies for all GKE clusters \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:13.033036+00:00
---

# Require continuous validation check-based platform policies for all GKE clusters  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/cv-org-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Require continuous validation check-based platform policies for all GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to use the Organization Policy Service to require that GKE clusters use one or more continuous validation (CV) check-based platform policies. You specify the required check-based platform policies in [custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints). You then enforce the custom constraints in your organization policy.

## Costs

This guide uses the following Google Cloud services:

  * Binary Authorization, but CV is available free of charge during the [Preview](https://cloud.google.com/products/#product-launch-stages) stage
  * Organization policies and constraints are offered at no charge.



## Before you begin

  1. Enable [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).
  2. Set up [CV with check-based platform policies](https://docs.cloud.google.com/binary-authorization/docs/enabling) and at least one [CV check-based platform policy](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#checks).



## Required roles

To get the permissions that you need to create constraints and enforce organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on your Google Cloud organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a CV custom constraint

### Console

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. On the **Organization policies** page, click add **Custom constraint**.

  3. If you're prompted to do so, click **Switch to parent organization**. To learn more about organizations, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)

  4. In **Constraint details** enter the following information in the fields:

     1. **Display name:** A display name for your constraint, such as `Require a Binary Authorization continuous validation policy for all GKE clusters`. You use the display name to look up the constraint after it is saved. The display name field has a maximum length of 200 characters 

     2. **Constraint ID** : a constraint ID for your constraint—for example, `RequireBinAuthzCVPolicy`.

     3. **Description** (Optional): a human-friendly description of the constraint to display as an error message when the policy is violated. The description field has a maximum length of 2000 characters. 

  5. In **Enforcement** , do the following:

     1. In **Resource types** , enter `container.googleaips.com/Cluster`.

     2. In **Enforcement method** , select **Enforce on create and update**.

     3. Enter an expression into the **Condition** field. This field has a maximum length of 1000 characters. The custom constraint is enforced when the condition evaluates to `true`. The condition is as expression in the [Common Expression Language (CEL) syntax](https://cel.dev). You can combine expressions with and (`&&`) and or (`||`) to create a complex condition. CEL is a C-like expression language. To learn more about the syntax and semantics of CEL, see <https://github.com/google/cel-spec>. To enter the condition, do the following:

        1. Click edit **Edit condition**.

        2. Enter an expression to check for the existence of a CV platform policy. The following condition requires that a CV platform policy binding exists and that the platform policy has a specific name:
               
               resource.binaryAuthorization.policyBindings.exists(policy, policy.name == "projects/PROJECT_ID/platforms/gke/policies/POLICY_ID")
               

Replace the following:

           * `PROJECT_ID`: the project ID of your platform policy. The project must be in the same organization.
           * `POLICY_ID`: the policy ID of your platform policy.

The following condition requires that two CV platform policy bindings exist and that each has a specific platform policy name.
    
    resource.binaryAuthorization.policyBindings.exists(policy, policy.name == "projects/PROJECT_ID1/platforms/gke/policies/POLICY_ID1") && resource.binaryAuthorization.policyBindings.exists(policy, policy.name == "projects/PROJECT_ID2/platforms/gke/policies/POLICY_ID2")
    

           * `PROJECT_ID1`: the project ID of your first platform policy. The project must be in the same organization.
           * `POLICY_ID1`: the policy ID of your first platform policy.
           * `PROJECT_ID2`: the project ID of your second platform policy.
           * `POLICY_ID2`: the policy ID of your second platform policy. 
           * Click **Save**.

     4. In **Action** , select **Allow**.

  6. To create your custom constraint, click **Create Constraint**.




### gcloud

  1. Create a YAML file for the custom constraint:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.CONSTRAINT_ID
         resource_types: container.googleapis.com/Cluster
         method_types:
           - CREATE
           - UPDATE
         condition: >-
           CONDITION
         action_type: ACTION
         display_name: DISPLAY_NAME
         description: DESCRIPTION
         

Replace the following:

     * `ORGANIZATION_ID`: your organization ID—for example, `123456789`.
     * `CONSTRAINT_ID`: a constraint ID—for example, `RequireBinAuthzCVPolicy`.
     * `CONDITION`: enter an expression to check for the existence of a CV platform policy. This field has a maximum length of 1000 characters. The custom constraint is enforced when the condition evaluates to `true`. The condition is as expression in the [Common Expression Language (CEL) syntax](https://cel.dev). You can combine expressions with and (`&&`) and or (`||`) to create a complex condition. CEL is a C-like expression language. To learn more about the syntax and semantics of CEL, see <https://github.com/google/cel-spec>. The following condition requires that a CV platform policy binding exists and that the platform policy has a specific name:
           
           resource.binaryAuthorization.policyBindings.exists(policy, policy.name == "projects/PROJECT_ID/platforms/gke/policies/POLICY_ID")
           

Replace the following:

       * `PROJECT_ID`: the project ID of your platform policy. The project must be in the same organization.
       * `POLICY_ID`: the policy ID of your platform policy.

The following condition requires that two CV platform policy bindings exist and that each has a specific platform policy name.
    
    resource.binaryAuthorization.policyBindings.exists(policy, policy.name == "projects/PROJECT_ID1/platforms/gke/policies/POLICY_ID1") && resource.binaryAuthorization.policyBindings.exists(policy, policy.name == "projects/PROJECT_ID2/platforms/gke/policies/POLICY_ID2")
    

       * `PROJECT_ID1`: the project ID of your first platform policy. The project must be in the same organization.
       * `POLICY_ID1`: the policy ID of your first platform policy.
       * `PROJECT_ID2`: the project ID of your second platform policy.
       * `POLICY_ID2`: the policy ID of your second platform policy. 
       * `ACTION`: the action to take if the `condition` is met. This can be either `ALLOW` or `DENY`.

       * `DISPLAY_NAME`: a human-friendly name for the constraint—for example, `Require a Binary Authorization continuous validation policy for all GKE clusters`. The display name field has a maximum length of 200 characters 

       * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. The description field has a maximum length of 2000 characters. 

     * Apply the custom constraint:
           
           gcloud org-policies set-custom-constraint CUSTOM_CONSTRAINT_PATH
           

Replace `CUSTOM_CONSTRAINT_PATH` with the path of your custom constraint definition.

     * Verify that the custom constraint exists:
           
           gcloud org-policies list-custom-constraints \
               --organization=ORGANIZATION_ID
           

The output is similar to the following:
           
           CUSTOM_CONSTRAINT: custom.RequireBinAuthzCVPolicy
           ACTION_TYPE: ALLOW
           METHOD_TYPES: CREATE,UPDATE
           RESOURCE_TYPES: container.googleapis.com/Cluster
           DISPLAY_NAME: This cluster requires the continuous validation policy: projects/my-project/platforms/gke/policies/my-policy
           




To enable enforcement of the custom constraint that you created, create an organization policy.

## Use an organization policy to enforce the custom constraint

To enforce the new custom constraint, create an organization policy that references the constraint, and then apply the organization policy.

### Console

To enforce the constraint, do the following:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Select the project picker select the organization.

  3. Search for and select your constraint from the list.

  4. In the **Policy details** page for that constraint, click **Manage policy**.

  5. On the **Edit policy** page, select **Override parent's policy**.

  6. Click **Add a rule**.

  7. In **Enforcement** , select **On**.

  8. Optional: Click **Test changes** to simulate the effect of this organization policy. For more information, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

  9. To finish and apply the organization policy, click **Set policy**.




### gcloud

  1. Create a YAML policy definition file:
         
         name: organizations/ORGANIZATION_ID/policies/custom.CONSTRAINT_ID
         spec:
           rules:
           - enforce: true
         

Replace the following:

     * `ORGANIZATION_ID`: the organization ID
     * `CONSTRAINT_ID`: the constraint ID
  2. Enforce the policy:
         
         gcloud org-policies set-policy ORG_POLICY_PATH
         

Replace `ORG_POLICY_PATH` with the path to your policy definition file.

  3. Verify that the policy exists:
         
         gcloud org-policies list \
             --organization=ORGANIZATION_ID
         

Replace `ORGANIZATION_ID` with the organization ID.

For a list of arguments, refer to [`gcloud org-policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list).

The output is similar to the following:
         
         CONSTRAINT: custom.RequireBinAuthzCVPolicy
         LIST_POLICY: -
         BOOLEAN_POLICY: SET
         ETAG: CN622LIGEIDXnpMB-
         




The policy can take up to 15 minutes to take effect.

To enforce multiple constraints on CV check-based platform policies, do the following:

  * Create one custom constraint per CV check-based policy.
  * Update the organization policy with each custom constraint as described in this section.



## Delete the custom constraint

You can delete a custom constraint using the Google Cloud console or the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Select the project picker at the top of the page.

  3. From the project picker, select your organization.

  4. Search for and select your constraint from the list.

  5. In **Constraint details** , click delete **Delete**.

  6. To confirm you want to delete the constraint, click **Delete**.




### gcloud

To delete a custom constraint, use the `org-policies delete-custom-constraint` gcloud CLI command:
    
    
    gcloud org-policies delete-custom-constraint custom.CONSTRAINT_ID \
      --organization=ORGANIZATION_ID
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `123456789`

  * `CONSTRAINT_NAME`: the name of your custom constraint




The output is similar to the following:
    
    
    Deleted custom constraint [organizations/123456789/customConstraints/CONSTRAINT_NAME]
    

After you delete a custom constraint, any policies that have been created using that constraint continue to exist, but are ignored. You can't create another custom constraint with the same name as a deleted custom constraint.

## What's next

  * Learn about [Organization Policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints).
  * [Use the image freshness check](https://docs.cloud.google.com/binary-authorization/docs/cv-freshness-check)
  * [Use the simple signing attestation check](https://docs.cloud.google.com/binary-authorization/docs/cv-attestation-check)
  * [Use the Sigstore signature check](https://docs.cloud.google.com/binary-authorization/docs/cv-sigstore-check)
  * [Use the SLSA check](https://docs.cloud.google.com/binary-authorization/docs/cv-slsa-check)
  * [Use the trusted directory check](https://docs.cloud.google.com/binary-authorization/docs/cv-trusted-directory-check)
  * [Use the vulnerability check](https://docs.cloud.google.com/binary-authorization/docs/cv-vulnerability-check)
  * [View CV logs](https://docs.cloud.google.com/binary-authorization/docs/cv-view-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
