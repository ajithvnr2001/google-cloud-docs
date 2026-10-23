---
url: https://docs.cloud.google.com/organization-policy/create-custom-constraints/
title: Create custom constraints \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:17.630389+00:00
---

# Create custom constraints  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/create-custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Create custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can view, create, and manage custom organization policies as an administrator. With custom organization policies, you can customize control over the specific fields restricted by your organization policies.

## Before you begin

  * For more information about what organization policies and constraints are and how they work, see the [Introduction to the Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).



### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the following IAM roles on the organization: 

  * [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
  * To enable Google Cloud APIs: [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can delegate the administration of organization policies by adding [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to the Organization policy administrator role binding. To control the resources where a principal can manage organization policies, you can make the role binding conditional on a particular [tag](https://docs.cloud.google.com/iam/docs/tags-access-control). For more information, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#delegate-admin). 

## Custom constraints

A custom constraint is defined in a YAML file, which specifies the resources, methods, conditions, and actions that are subject to the constraint. Custom constraint behavior and supported parameters are specific to each service. Conditions for custom constraints are defined using Common Expression Language (CEL).

### Set up a custom constraint

You can create a custom constraint and set it up for use in organization policies using the Google Cloud console or Google Cloud CLI.

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.disableGkeAutoUpgrade`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. This constraint can only be enforced on the REST `CREATE` method. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.disableGkeAutoUpgrade`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.management.autoUpgrade == false"`. 
     * `ACTION`: the action to take if the `condition` is met. Possible values are `ALLOW` and `DENY`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

The deny action means that if the condition evaluates to true, the operation to create or update the resource is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




### Update a custom constraint

You can update a custom constraint by editing the constraint in the Google Cloud console, or by creating a new YAML file and using the `set-custom-constraint` gcloud CLI command again. There is no versioning of custom constraints, so this overwrites the existing custom constraint. If the custom constraint is already enforced, the updated custom constraint takes effect immediately.

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Select the project picker at the top of the page.

  3. From the project picker, select the resource that you want to update the organization policy for.

  4. Select the constraint that you want to edit from the list on the **Organization policies** page to open the **Policy details** page for that constraint.

  5. Click edit **Edit constraint**.

  6. Make changes to the display name, description, enforcement method, condition, and action. You can't change the constraint ID or resource type after the constraint is created.

  7. Click **Save changes**.




### gcloud

  1. Get the current custom constraint using the [`gcloud org-policies describe-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe-custom-constraint) command.
         
         gcloud org-policies describe-custom-constraint CONSTRAINT_NAME \
           --organization=ORGANIZATION_ID \
           --format=FORMAT > PATH
         

Replace the following:

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`.

     * `CONSTRAINT_NAME`: the name of your custom constraint, for example `custom.disableGkeAutoUpgrade`.

     * `FORMAT`: the format for the allow policy. Use `json` or `yaml`.

     * `PATH`: the path to a new output file for the custom constraint.

  2. Modify the local copy of the custom constraint to reflect the changes that you want to make to the display name, description, enforcement method, condition, and action. You can't change the constraint ID or resource type after the constraint is created.

  3. After you have updated the YAML file for your custom constraint, set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [`gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command:
         
         gcloud org-policies set-custom-constraint CONSTRAINT_PATH
         

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file.




After the update is complete, the updated custom constraint is available for your organization policies. If the original constraint is already enforced, the updated constraint takes effect immediately.

### Delete a custom constraint

You can delete a custom constraint using the Google Cloud console or the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Select the project picker at the top of the page.

  3. From the project picker, select the resource that you want to delete the organization policy for.

  4. Select the constraint that you want to delete from the list on the **Organization policies** page to open the **Policy details** page for that constraint.

  5. Click delete **Delete**.

  6. To confirm that you want to delete the constraint, click **Delete**.




### gcloud

To delete a custom constraint, use the `org-policies delete-custom-constraint` gcloud CLI command:
    
    
    gcloud org-policies delete-custom-constraint custom.CONSTRAINT_NAME \
      --organization=ORGANIZATION_ID
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `123456789`.

  * `CONSTRAINT_NAME`: the name of your custom constraint. For example, `custom.disableGkeAutoUpgrade`.




The output is similar to the following:
    
    
    Deleted custom constraint [organizations/123456789/customConstraints/custom.disableGkeAutoUpgrade]
    

If you delete a custom constraint, any policies that have been created using that constraint are deleted. The name of the deleted custom constraint is available to use within a few minutes.

### Test and analyze organization policy changes

We recommend that you test and dry-run all changes to your organization policies to understand how changes affect your environment.

Policy Simulator for Organization Policy helps you understand the effect of a constraint and organization policy on your current environment. Using this tool, you can review all resource configurations to see where violations occur, before the policy is enforced on your production environment. For detailed instructions, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

When you understand the current effect, you can create an organization policy in dry-run mode to understand the impact and potential violations of a policy over the next 30 days. An organization policy in dry-run mode is a type of organization policy where violations of the policy are audit-logged, but the violating actions aren't denied. You can create an organization policy in dry-run mode from a custom constraint using the Google Cloud console or Google Cloud CLI. For detailed instructions, see [Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies#create_dry_run_boolean_policy).

### Enforce a custom organization policy

After a custom constraint is set up, it operates identically to predefined boolean constraints. Google Cloud checks custom constraints first when evaluating if a user request is allowed. If any of the custom organization policies deny the request, the request is rejected. Then, Google Cloud checks for predefined organization policies enforced on that resource.

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.disableGkeAutoUpgrade`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




### Example constraint

You can define custom constraints similar to the predefined constraints provided by Google. A typical custom constraint YAML file looks similar to the following:
    
    
    name: organizations/1234567890123/customConstraints/custom.disableGkeAutoUpgrade
    resourceTypes: container.googleapis.com/NodePool
    methodTypes:
      - CREATE
      - UPDATE
    condition: "resource.management.autoUpgrade == false"
    actionType: ALLOW
    displayName: Disable GKE auto upgrade
    description: Only allow GKE NodePool resource to be created or updated if
    AutoUpgrade is not enabled where this custom constraint is enforced.
    

## Common Expression Language

Organization Policy Service uses [Common Expression Language (CEL)](https://opensource.google/projects/cel) to evaluate conditions on custom constraints. CEL is an open-source non-Turing complete language that implements common semantics for expression evaluation.

Each service that supports custom constraints makes a particular set of their resources and the fields of these resources available. The available fields are strongly typed, and can be directly referenced by custom constraints.

You can construct CEL conditions that refer to service resource fields based on the type of the field. Organization Policy Service supports a subset of CEL data types, expressions, and macros. The following sections list the available data types and common expressions and macros that work with them.

  * Integer
  * String
  * Boolean
  * List
  * Map



For details on which expressions and macros are available for each service, see [Custom constraint supported services](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services).

The following JSON example shows each of the potential field types you can reference using custom constraints:
    
    
    {
      "integerValue": 1,
      "stringValue": "A text string",
      "booleanValue": true,
      "nestedValue": {
        "nestedStringValue": "Another text string"
      },
      "listValue": ["foo", "bar"],
      "mapValue": {
        "costCenter": "123"
      }
    }
    

For every CEL expression, the custom constraint is enforced when the condition evaluates to `true`. You can combine expressions with and (`&&`) and or (`||`) to create a complex query. When creating the YAML or JSON file for your custom constraint, enclose the full query in double quotes (`"`).

### Integer

Integer fields, such as `integerValue` in the previous example, allow comparison operators to be used in conditions. For example:
    
    
    resource.integerValue == 1
    resource.integerValue > 5
    resource.integerValue < 10
    

### String

String fields, such as `stringValue` in the previous example, can be evaluated using a string literal, a regular expression, or a CEL expression. For example:
    
    
    resource.stringValue == "abc"
    // stringValue is exactly "abc".
    
    resource.stringValue.matches("dev$")
    // stringValue matches a regular expression, which specifies the string ends
    // with the word "dev".
    
    resource.stringValue.startsWith("startValue")
    // stringValue starts with "startValue".
    
    resource.stringValue.endsWith("endValue")
    // stringValue ends with "endValue".
    
    resource.stringValue.contains("fooBar")
    // stringValue contains "fooBar".
    

Nested fields, such as `nestedStringValue` in the previous example, must be referenced with the full path. For example:
    
    
    resource.nestedValue.nestedStringValue == "foo"
    // nestedValue contains the object nestedStringValue, which has a value of "foo".
    

### Boolean

Boolean fields, such as `booleanValue` in the previous example, contain a boolean value, which is either `true` or `false`.

### List

List fields, such as `listValue` in the previous example, can be evaluated by the size of the list, the contents of the list, and whether a particular element exists anywhere within the list.

For example:
    
    
    resource.listValue.size() >= 1 && resource.listValue[0] == "bar"
    // listValue has size greater than or equal to one, and the first element is "bar".
    
    resource.listValue.exists(value, value == "foo")
    // listValue has at least one element that is exactly "foo".
    
    resource.listValue.all(value, value.contains("foo"))
    // listValue is a list of values that are all exactly "foo".
    

**Warning:** Querying a list value that does not exist returns a `BAD_CONDITION` error. This error blocks all creation of the specified resource where the custom organization policy is enforced. To avoid this error, use `all()`, `any()`, or `exists()` methods. If you want to query a particular index, first check that the index exists using the `size()` method. For example, `listValue.size() >= 1 && resource.listValue[0] == "bar"`.

### Map

Map fields, such as `mapValue` in the previous example, are key-value pairs that can be evaluated based on the existence and value of particular elements.

For example:
    
    
    has(resource.mapValue.foo) && resource.mapValue.foo == "bar"
    // mapValue contains the key "foo", and that key has the value "bar".
    

**Warning:** Querying a map value that does not exist returns a `BAD_CONDITION` error. This error blocks all creation of the specified resource where the custom organization policy is enforced. To avoid this error, always check that the value exists first using the `has()` method. For example, `has(map.key) && map.key == "value"`.

## Troubleshooting custom constraints

The following sections describe common issues related to creating custom constraints and introduce workarounds for these issues.

### Method type errors

Custom constraints are created with a list of methods to enforce, typically either `CREATE` or both `CREATE` and `UPDATE`. If you specify a method type that's not supported by a resource, such as the `UPDATE` method for Compute Engine image resources, you can't save the custom constraint.

### Tags not evaluated

Tags on organization, folder, or project resources are supported by custom constraints. For more information about what services support tags, see the [service-specific documentation](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services).

### Cross-service restrictions

Some services, such as Compute Engine, involve a large number of related resources. The error message for a custom organization policy violation is displayed when the violation occurs, even if the custom constraint is for a different service.

For example, a Managed Service for Apache Spark action might be blocked by a custom constraint on Compute Engine resources.

## Troubleshooting CEL errors

Organization Policy Service compiles and validates conditions that you create, returning an error if the condition is not syntactically correct. If you can't create or save a custom constraint, then likely an invalid CEL syntax error occurred, which you must address first.

In the Google Cloud console, invalid CEL syntax errors will be flagged with an error **Error** icon. Highlighting this icon displays a tooltip containing more information about the syntax error.

Certain conditions might compile but cause an error to occur when Google Cloud attempts to enforce the constraints. For example, if you set up a constraint with a condition that tries to access a list index or map key that doesn't exist, the constraint fails and returns an error at the time of enforcement, **and blocks any attempt to create the resource**.

The following sections describe common CEL errors and potential workarounds for these errors.

### Invalid expression or type mismatch

A condition that is created with invalid expressions or type mismatches returns an error when you attempt to set up the custom constraint. For example, given the following invalid custom constraint, which compares a string with an integer:
    
    
    name: organizations/1234567890123/customConstraints/custom.badConfig
    resourceTypes: dataproc.googleapis.com/Cluster
    methodTypes:
      - CREATE
      - UPDATE
    condition: "resource.config.masterConfig.numInstances == 'mismatch'"
    actionType: ALLOW
    displayName: Number of instances is a string
    description: Demonstrate that type mismatches cause an error.
    

An error is produced if you try to set up that constraint using the Google Cloud CLI:
    
    
    ERROR: (gcloud.org-policies.set-custom-constraint) INVALID_ARGUMENT: Custom constraint condition [resource.config.masterConfig.numInstances == "mismatch"] is invalid. Error: ERROR: <input>:1:15: found no matching overload for '_==_' applied to '(int, string)' (candidates: (%A0, %A0))
     | resource.config.masterConfig.numInstances == "mismatch"
     | ..........................................^.
    

In the Google Cloud console, invalid CEL syntax errors will be flagged with an error **Error** icon. Highlighting this icon displays a tooltip containing more information about the syntax error.

Organization Policy Service compiles and validates conditions that you create, returning an error if the condition isn't syntactically correct. However, certain conditions might compile but return an error when Google Cloud attempts to enforce the constraints. For example, if you set up a constraint with a condition that tries to access a list index or map key that does not exist, the constraint fails and returns an error at the time of enforcement, **and blocks any attempt to create the resource**.

When creating conditions that depend on list or map elements, we recommend starting the condition with a check that ensures the condition is valid in all cases. For example, check `list.size()` before referencing a particular list element or use `has()` before referencing a map element.

## Supported services

Each service defines the set of custom constraint fields that can be used to enforce organization policies on their service resources. For a list of services that support custom constraints, see [Custom constraint supported services](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services).

For more information about setting up an organization policy scanner, see [Organization Policy vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#org-findings).

## Enforcing mandatory tags on resources

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enforce mandatory tags on resources by using a custom organization policy. When you enforce mandatory tags, you can only create resources that comply with your organization's tagging policies; that is, resources are bound with the tag values for the mandatory tag keys specified in the policy. For more information, see [Set up a custom constraint to enforce tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#create_custom_constraint_tags). 

## What's next

  * [Learn about constraints in-depth](https://docs.cloud.google.com/organization-policy/overview#constraints).
  * [Read about the additional options you can use to customize your policies](https://docs.cloud.google.com/organization-policy/apply-policies).
  * [Learn how to set organization policies based on Tags](https://docs.cloud.google.com/organization-policy/scope-policies).
  * [See the custom organization policy library on GitHub](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/custom-organization-policy-library).
  * [Learn about validating and monitoring organization policies with Config Validator](https://github.com/forseti-security/policy-library/blob/master/docs/user_guide.md).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
