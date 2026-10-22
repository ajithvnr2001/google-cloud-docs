---
url: https://docs.cloud.google.com/organization-policy/test-constraints-gca/
title: Test custom constraints with Gemini Cloud Assist \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:09.633786+00:00
---

# Test custom constraints with Gemini Cloud Assist  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/test-constraints-gca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Test custom constraints with Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides guidance for creating and testing custom organization policy constraints using [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview).

## Before you begin

  * For more information about what organization policies and constraints are and how they work, see the [Introduction to the Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).

  * For more information about custom organization policies, see [Create custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints).

  * To set up Gemini Cloud Assist to create and test custom constraints, see [Set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).




### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the following IAM roles on the organization: 

  * [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
  * To use Gemini Cloud Assist: [Gemini for Google Cloud User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`) 
  * To enable Google Cloud APIs: [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can delegate the administration of organization policies by adding [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to the Organization policy administrator role binding. To control the resources where a principal can manage organization policies, you can make the role binding conditional on a particular [tag](https://docs.cloud.google.com/iam/docs/tags-access-control). For more information, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#delegate-admin). 

## Custom constraints

A custom constraint is created in a YAML file, which specifies the resources, methods, conditions, and actions that are subject to the constraint. These are specific to the service on which you're enforcing the organization policy. The conditions for your custom constraint are defined using Common Expression Language (CEL).

### Set up a custom constraint

You can create a custom constraint and set it up for use in organization policies using Gemini Cloud Assist.

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker at the top of the page, select the project that you want to set the organization policy for.

  3. In the **Create custom organization constraints with Gemini** banner, click **Create constraint**.

  4. In the **Cloud Assist** pane, send a prompt describing the custom constraint you want to generate. For example:

"Restrict the boot disk size to 250 GB or less for all `compute.googleapis.com/Disk` resources."

  5. Review the response, which includes generated code for the constraint and additional details for how the constraint works, to verify that the constraint achieves your goal.

  6. Optional: If the constraint needs modification, send a prompt with the required changes. For example, "can you add asia-east1" instructs Gemini Cloud Assist to add the `asia-east1` locale to the relevant place in your constraint.

  7. Optional: You can use Gemini Cloud Assist to define test resources and simulate the constraint to verify it works as intended. For more information, see Test custom constraints with Gemini Cloud Assist.

  8. To create a custom organization policy using your new constraint, click **Insert to Create Constraint**. The **Create custom constraint** window appears, with the fields populated by the generated custom constraint. You can test or create the custom organization policy as normal.




### Test custom constraints with Gemini Cloud Assist

You can test custom constraints that you create using Gemini Cloud Assist. After you create your custom constraint, Gemini Cloud Assist can help create a set of resources to test that custom constraint, and then simulate the effect that the custom constraint will have on those resources.

  1. To create the custom constraint, use the Gemini Cloud Assist workflow to Set up a custom constraint.

  2. After the custom constraint is generated, click **Begin testing**. This generates a list of resource configurations, each of which is labeled compliant or not compliant with the custom constraint. The attributes column describes the unique attributes of each resource.

For each compliant or non-compliant resource, a list of gcloud CLI commands is generated that you can use to create the resources defined in the test cases.

  3. Create the test resources by entering the generated gcloud CLI commands in the shell or Google Cloud console. For more information and instructions on how to troubleshoot issues, see the documentation for the specific Google Cloud service related to your test resources.

  4. After resources are generated, allow at least 10 minutes for the resources to be ready for simulation.

  5. To simulate the effect that your custom organization policy will have on your resources, click **Begin simulation**.

  6. Review the details of the pending simulation, and then click **Confirm**. The simulation can take up to an hour to complete.

     1. To view simulation results, go to the **Simulation history** page. 

[Go to Simulation history](https://console.cloud.google.com/iam-admin/orgpolicies/reports)

     2. Select the simulation to view its details. If the simulation results are not visible, select your organization from the project picker at the top of the page.

On the **Simulation details** page, you can view the number of violations, the number of resources checked, the date of the simulation, and a list of all resources with non-compliant configurations.

You can also set the simulated organization policy in dry-run mode by clicking **Set dry-run policy**.

For more information, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).




## What's next

  * [Learn about constraints in-depth](https://docs.cloud.google.com/organization-policy/overview#constraints).
  * [Read about the additional options you can use to customize your policies](https://docs.cloud.google.com/organization-policy/apply-policies).
  * [Learn how to set organization policies based on Tags](https://docs.cloud.google.com/organization-policy/scope-policies).
  * [See the custom organization policy library on GitHub](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/custom-organization-policy-library).
  * [Learn about validating and monitoring organization policies with Config Validator](https://github.com/forseti-security/policy-library/blob/master/docs/user_guide.md).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
