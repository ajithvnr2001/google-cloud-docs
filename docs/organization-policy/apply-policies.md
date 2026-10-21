---
url: https://docs.cloud.google.com/organization-policy/apply-policies/
title: Apply organization policies \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:03.911995+00:00
---

# Apply organization policies  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/apply-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Apply organization policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view, create, and manage your organization policies using the Google Cloud console.

The Identity and Access Management role [`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy) enables an administrator to manage organization policies. Users must be organization policy administrators to change or override organization policies.

**Note:** If you're getting started with Google Cloud, you can apply recommended organization policies as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

## Before you begin

  * To set, change, or delete an organization policy, you must have the [Organization Policy Administrator](https://docs.cloud.google.com/organization-policy/create-organization-policies#delegate-admin) role.



To use this guide, you need to be familiar with the following concepts:

  * How [constraints](https://docs.cloud.google.com/organization-policy/overview#constraints) define the behavior of organization policies.

  * How organization policies are evaluated at different levels of the [resource hierarchy](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation).




## Viewing organization policies

To view organization policies:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project, folder, or organization for which you want to view organization policies.

  3. The **Organization policies** page displays a list of organization policy constraints that are available for this resource.

  4. To filter the list by constraint name, enter a constraint name into the **Filter** field.




For more details and step-by-step guides for using each constraint, see [Organization Policy Constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

## Creating and editing policies

Organization policies are defined by the values set for each constraint. They are either configured at the level of this resource, inherited from the parent resource, or set to the Google-managed default behavior.

**Note:** Enforcement of most organization policies is not retroactive. If a new organization policy sets a restriction on an action or state that a service is already in, the policy is considered to be in violation, but the service will not stop its original behavior. Organization policy constraints that are retroactive note this property in their description. For more details about organization policy violations, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview#violations).

### Updating policies with boolean rules

To update an organization policy with boolean rules:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project, folder, or organization for which you want to edit organization policies.

  3. The **Organization policies** page displays a filterable list of organization policy constraints that are available.

  4. Select a constraint from the list on the **Organization policies** page. The **Policy details** page that appears describes the constraint and provides information about how the constraint is applied.

  5. To update the organization policy for this resource, click **Manage policy**.

  6. On the **Edit policy** page, select **Override parent's policy**.

  7. Select **Add a rule**.

  8. Under **Enforcement** , select whether enforcement of this organization policy should be on or off.

  9. To enforce the policy, click **Set policy**.




Changes to organization policies can take up to 15 minutes to be fully enforced.

For Google Cloud CLI instructions, see [Use boolean rules in organization policy](https://docs.cloud.google.com/organization-policy/create-organization-policies#boolean-constraint).

### Updating policies with list rules

To update an organization policy with list rules:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project, folder, or organization for which you want to edit organization policies.

  3. The **Organization policies** page displays a filterable list of organization policy constraints that are available.

  4. Select a constraint from the list on the **Organization policies** page. The **Policy details** page that appears describes the constraint and provides information about how the constraint is applied.

  5. To update the organization policy for this resource, click **Manage policy**.

  6. On the **Edit policy** page, select **Override parent's policy**.

  7. Under **Policy enforcement** , select an enforcement option:

     * To merge and evaluate the organization policies together, select **Merge with parent**. For more information about inheritance and the resource hierarchy, see [Hierarchy evaluation](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation).

     * To override the inherited policies completely, select **Replace**.

  8. Select **Add a rule**.

  9. Under **Policy values** , select whether this organization policy allows all values, denies all values, or specifies a custom list.

     1. If you specify a custom list of values, then under **Policy type** , select whether the given values should be accepted or denied by the organization policy.

     2. Enter your allowed or denied value into the **Custom value** field. To add more values, click **Add value**. Specific values accepted by the policy depend on the service to which the policy applies. For a list of constraints and the values they accept, see [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

  10. To enforce the policy, click **Set policy**.




Changes to organization policies can take up to 15 minutes to be fully enforced.

Managed constraints can't have more than 100 individual parameter values.

Legacy managed constraints can't have more than 500 individual allowed or denied values. Organization policies with list rules can't be more than 32 KB. If an organization policy is created or updated to have more than the allowed number of values, or is greater than 32 KB in size, it can't save successfully, and the request will return an error. For Google Cloud CLI instructions, see [Use list rules in an organization policy](https://docs.cloud.google.com/organization-policy/create-organization-policies#list-constraint).

### Inheriting organization policy

You can set an organization policy to inherit the parent organization policy or to use the Google-managed default behavior. Either of these options will remove the configured organization policy. To change the behaviors that an organization policy inherits:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project, folder, or organization for which you want to edit organization policies.

  3. The **Organization policies** page displays a filterable list of organization policy constraints that are available.

  4. Select a constraint from the list on the **Organization policies** page. The **Policy details** page that appears describes the constraint and provides information about how the constraint is applied.

  5. To remove a configured organization policy on this resource, click **Manage policy** and then select an option to specify how the organization policy is evaluated:

     * To make this resource follow the same rules as the parent resource for this constraint, select **Inherit parent's policy**. This is the default behavior for resources.

     * To override the parent resource's organization policy with the default behavior set by Google for this constraint, select **Google-managed default**.




Changes to organization policies can take up to 15 minutes to be fully enforced.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
