---
url: https://docs.cloud.google.com/organization-policy/scope-policies/
title: Scope organization policies with tags \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:14.748065+00:00
---

# Scope organization policies with tags  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/scope-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Scope organization policies with tags Stay organized with collections  Save and categorize content based on your preferences. 

Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag. You can use tags and conditional enforcement of organization policies to provide centralized control of the resources in your hierarchy.

**Note:** You can only conditionally enforce organization policies using tags that are attached to [supported resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services#supported_service_resources).

## Before you begin

For more information about what tags are and how they work, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

For detailed instructions about how to use tags, see [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can delegate the administration of organization policies by adding [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to the Organization policy administrator role binding. To control the resources where a principal can manage organization policies, you can make the role binding conditional on a particular [tag](https://docs.cloud.google.com/iam/docs/tags-access-control). For more information, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#delegate-admin). 

## Constraint support for tags

You can conditionally enforce organization policies with any type of constraint by using tags that are attached to organization, folder, and project resources. Tags that are attached directly to supported service resources, such as Compute Engine instances, can be used in conditions for managed or custom constraints. For more information, see [Services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services#supported_service_resources).

The following legacy managed constraints support conditions involving tags attached to service resources:

  * `constraints/sql.restrictNoncompliantDiagnosticDataAccess`
  * `constraints/gcp.restrictCmekCryptoKeyProjects`
  * `constraints/sql.restrictAuthorizedNetworks`
  * `constraints/gcp.resourceLocations`
  * `constraints/gcp.restrictNonCmekServices`
  * `constraints/sql.restrictNoncompliantResourceCreation`
  * `constraints/sql.restrictPublicIp`



Legacy managed constraints not on this list don't support conditions involving tags attached to service resources.

## Setting an organization policy with tags

To use tags to determine where an organization policy should take effect, you must specify a condition in the organization policy YAML file. You can set the condition to match a particular tag key-value pair, requiring that a particular tag value is set for the organization policy to be enforced.

You can also set the condition to match a tag key. This lets you enable or disable enforcement against all resources with that tag key, regardless of what tag value is attached.

Most organization policies are evaluated and enforced when a resource is created or updated. [Mandatory tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#enforcing_mandatory_tags) can be used to govern resources as they are created.

### List rule example

The following example demonstrates how to set an organization policy that enforces the `gcp.resourceLocations` legacy managed constraint. This organization policy uses both conditional and unconditional values, set within the same policy file.

###  Console 

To set the organization policy, do the following:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project for which you want to set the organization policy.

  3. On the **Organization policies** page, select a constraint from the list. The **Policy details** page for that constraint appears.

  4. To update the organization policy for this resource, click **Manage policy**.

  5. On the **Edit policy** page, select **Override parent's policy**.

  6. Under **Policy enforcement** , select an enforcement option:

     * To merge and evaluate your organization policies together, select **Merge with parent**. For more information about inheritance and the resource hierarchy, see [Hierarchy evaluation](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation).

     * To override policies inherited from a parent resource, select **Replace**.

  7. Click **Add rule**.

  8. Under **Policy values** , select whether this organization policy should allow all values, deny all values, or specify a custom set of values.

     * Specific values accepted by the policy depend on the service to which the policy applies. For a list of constraints and the values they accept, see [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).
  9. Optionally, to make the organization policy conditional on a tag, click **Add condition**.

     1. In the **Title** field, enter a name for the condition.

     2. In the **Description** field, give your condition a description. The description provides context on the tags that are required and how they impact resources.

     3. You can use the **Condition builder** to create a condition that requires a particular tag for the constraint to take effect.

        1. In the **Condition type** box, select **Tag**.

        2. Select the **Operator** for your condition.

           * To match an entire tag, use the **has value** operator with the namespaced name of the tag, or use the **has value ID** operator with the key and value IDs of the tag.

           * To match the tag key only, use the **has key** operator with the namespaced name of the tag key, or use the **has key ID** operator with the tag key ID.

        3. You can create multiple conditions by clicking **Add**. If you add another condition, you can set the conditional logic to require all of them by toggling **And**. You can set the conditional logic to require only one of the conditions to be true by toggling **Or**.

        4. You can delete an expression by clicking the large **X** to the right of the condition fields.

        5. When you have finished editing your conditions, click **Save**.

     4. The **Condition editor** can be used to create a conditional expression programmatically. It will also display a programmatic rendering of your current set of conditions.

The conditional expression must include 1 to 10 subexpressions, joined by the `||` or `&&` operators. Each subexpression must be one of the following functions:

        * `"resource.matchTag('KEY_NAME', 'VALUE_SHORT_NAME')"`

Replace the following:

          * `KEY_NAME` with the namespaced name of the tag key. For example, `123456789012/env`.

          * `VALUE_SHORT_NAME` with the short name of the tag value. For example, `prod`.

For example: `resource.matchTag('123456789012/environment, 'prod')`

        * `"resource.matchTagId('KEY_ID', 'VALUE_ID')"`

Replace the following:

          * `KEY_ID` with the permanent ID of the tag key. For example, `tagKeys/123456789012`.

          * `VALUE_ID` with the permanent ID of the tag value. For example, `tagValues/567890123456`.

For example: `resource.matchTagId('tagKeys/123456789012', 'tagValues/567890123456')`

        * `"resource.hasTagKey('KEY_NAME')"`

Replace `KEY_NAME` with the namespaced name of the tag key. For example, `123456789012/env`.

For example: `resource.matchTag('123456789012/environment, 'prod')`

        * `"resource.hasTagKeyId('KEY_ID')"`

Replace `KEY_ID` with the permanent ID of the tag key. For example, `tagKeys/123456789012`.

For example: `resource.hasTagKeyId('tagKeys/123456789012')`

        1. You can use the **Condition editor** to apply the `!` logical operator. For example, the query `!resource.matchTag('ORGANIZATION_ID/location', 'us-west1')` would apply the organization policy constraint to any resource that does not have the `us-west1` tag.
**Warning:** If you create a query that includes the `!` logical operator in the **Condition editor** , the **Condition builder** displays an error message and can't render the query. The query functions, but you must use the **Condition editor** to make any further changes to the query.
  10. To enforce the policy, click **Set policy**.




###  gcloud 

To set the organization policy, create a YAML file to store the organization policy:
    
    
    name: RESOURCE_TYPE/RESOURCE_ID/policies/gcp.resourceLocations
    spec:
      rules:
      # As there is no condition specified, this allowedValue is enforced unconditionally.
      - values:
          allowedValues:
          - us-east1-locations
      # This condition applies to the values block.
      - condition:
          expression: "resource.matchTag('ORGANIZATION_ID/location', 'us-west1')"
        values:
          allowedValues:
          - us-west1-locations
    

You can match an entire tag with the condition using the `resource.matchTag` operator with the namespaced name of the tag.

To match the tag key only, use the `resource.hasTagKey` operator with the namespaced name of the tag key. To match any tag value for a given tag key, use the `resource.hasTagKeyID` operator with the tag key ID.

Run the `set-policy` command:
    
    
    gcloud org-policies set-policy POLICY_PATH
    

Replace the following:

  * `POLICY_PATH`: the full path to your organization policy YAML file

  * `RESOURCE_TYPE`: `organizations`, `folders` or `projects`

  * `RESOURCE_ID`: your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`

  * `ORGANIZATION_ID`: the parent organization of your tag key




For this organization policy, the resource and all of its child resources have the `gcp.resourceLocations` legacy managed constraint enforced against them, with `allowedValues` of `us-east1-locations` only. Any of these resources that have the tag `location: us-west1` will have the `gcp.resourceLocations` legacy managed constraint enforced against it, with `allowedValues` of `us-east1-locations` and `us-west1-locations`.

In this way, both conditional and unconditional sets of values can be enforced for a constraint in a single organization policy.

### Boolean rule example

The following example demonstrates how to set an organization policy that enforces the `compute.disableSerialPortAccess` legacy managed constraint. This organization policy specifies that all serial ports are accessible to resources, but uses a condition to only restrict serial port access to resources that have the matching tag.

###  Console 

To set the organization policy, do the following:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project for which you want to set the organization policy.

  3. Select a constraint from the list on the **Organization policies** page. The **Policy details** page for that constraint should appear.

  4. To update the organization policy for this resource, click **Manage policy**.

  5. On the **Edit policy** page, select **Override parent's policy**.

  6. Click **Add rule**.

  7. Under **Enforcement** , select whether enforcement of this organization policy should be on or off.

  8. Optionally, to make the organization policy conditional on a tag, click **Add condition**. Note that, if you add a conditional rule to an organization policy, you must add only one unconditional rule or the policy cannot be saved.

     1. In the **Title** field, enter a name for the condition.

     2. In the **Description** field, give your condition a description. The description provides context on the tags that are required and how they impact resources.

     3. You can use the **Condition builder** to create a condition that requires a particular tag for the constraint to take effect.

        1. In the **Condition type** box, select **Tag**.

        2. Select the **Operator** for your condition.

           * To match an entire tag, use the **has value** operator with the namespaced name of the tag, or use the **has value ID** operator with the key and value IDs of the tag.

           * To match the tag key only, use the **has key** operator with the namespaced name of the tag key, or use the **has key ID** operator with the tag key ID.

        3. You can create multiple conditions by clicking **Add**. If you add another condition, you can set the conditional logic to require all of them by toggling **And**. You can set the conditional logic to require only one of the conditions to be true by toggling **Or**.

        4. You can delete an expression by clicking the large **X** to the right of the condition fields.

        5. When you have finished editing your conditions, click **Save**.

        6. An organization policy with a condition enforced must have only one unconditional rule. Click **Add rule** , and set whether enforcement of this organization policy should default to on or off.

     4. The **Condition editor** can be used to create a conditional expression programmatically. It will also display a programmatic rendering of your current set of conditions.

The conditional expression must include from 1 to 10 subexpressions, joined by the `||` or `&&` operators. Each subexpression must be one of the following forms:

        * `"resource.matchTag('KEY_NAME', 'VALUE_SHORT_NAME')"`

Replace the following:

          * `KEY_NAME` with the namespaced name of the tag key. For example, `123456789012/env`.

          * `VALUE_SHORT_NAME` with the short name of the tag value. For example, `prod`.

        * `"resource.matchTagId('KEY_ID', 'VALUE_ID')"`

Replace the following:

          * `KEY_ID` with the permanent ID of the tag key. For example, `tagKeys/123456789012`.

          * `VALUE_ID` with the permanent ID of the tag value. For example, `tagValues/567890123456`.

        1. You can use the **Condition editor** to apply the `!` logical operator. For example, the query `!resource.matchTag('ORGANIZATION_ID/location', 'us-west1')` would apply the organization policy constraint to any resource that does not have the `us-west1` tag.
**Warning:** If you create a query that includes the `!` logical operator in the **Condition editor** , the **Condition builder** displays an error message and is not able to render the query. The query will function, but you must use the **Condition editor** to make any further changes to the query.
  9. To finish and apply the organization policy, click **Save**.




###  gcloud 

To set the organization policy, create a YAML file to store the organization policy:
    
    
    name: RESOURCE_TYPE/RESOURCE_ID/policies/gcp.disableSerialPortAccess
    spec:
      rules:
      - condition:
          expression: "resource.matchTag('ORGANIZATION_ID/disableSerialAccess', 'yes')"
        enforce: true
      - enforce: false
    

You can match an entire tag with the condition using the `resource.matchTag` operator with the namespaced name of the tag.

To match the tag key only, use the `resource.hasTagKey` operator with the namespaced name of the tag key. To match any tag value for a given tag key, use the `resource.hasTagKeyID` operator with the tag key ID.

Run the `set-policy` command:
    
    
    gcloud org-policies set-policy POLICY_PATH
    

Replace the following:

  * `POLICY_PATH`: the full path to your organization policy YAML file

  * `RESOURCE_TYPE`: `organizations`, `folders` or `projects`

  * `RESOURCE_ID`: your organization ID, folder ID, project ID, or project number

  * `ORGANIZATION_ID`: the parent organization of your tag key




For this organization policy, the resource and all of its child resources have the `gcp.disableSerialPortAccess` legacy managed constraint enforced against them. Any resources that have the tag `disableSerialAccess: yes` are denied by the organization policy. Any resource that does not have the tag `disableSerialAccess: yes` doesn't have the legacy managed constraint enforced against them.

## Conditionally add rules to organization policy

You can use tags to conditionally add constraint rules to resources based on the tags they have attached. You can add multiple conditions within the same organization policy, which gives you fine-grained control of the resources to which you want the organization policy to apply.

Common Expression Language, or CEL, is the expression language used to specify conditional expressions. A conditional expression consists of one or more statements that are joined using logical operators (`&&`, `||`, or `!`). For more information, see the [CEL spec](https://github.com/google/cel-spec) and its [language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md).

Consider an organization policy to restrict the locations in which resources could be created based on the tags applied to those resources. To do this, create an organization policy that enforces the `gcp.resourceLocations` legacy managed constraint, and use conditions to narrow enforcement to only certain resources.

Start by creating a temporary file, `/tmp/policy.yaml`, to contain your organization policy:
    
    
    name: organizations/ORGANIZATION_ID/policies/gcp.resourceLocations
    spec:
      rules:
      - condition:
          expression: "resource.matchTag('ORGANIZATION_ID/location', 'us-east')"
        values:
          allowedValues:
          - in:us-east1-locations
      - condition:
          expression: "resource.matchTag('ORGANIZATION_ID/location', 'us-west')"
        values:
          allowedValues:
          - in:us-west1-locations
      - values:
          deniedValues:
          - in:asia-south1-locations
    

Replace `ORGANIZATION_ID` with the parent organization of your tag key.

In this example, any resource that has the `location: us-east` tag attached will be restricted to locations within the `us-east1-locations` value group. Any resource that has the `location: us-west` tag attached will be restricted to locations within the `us-west1-locations` value group. All resources in the organization will be blocked from locations within the `asia-south1-locations` value group.

Then, set the policy using the `set-policy` command:
    
    
    gcloud org-policies set-policy /tmp/policy.yaml
    

### Restricting untagged resources

You can use tags and conditional organization policies to restrict any resources that are not using a particular tag. If you set an organization policy on a resource that restricts services and make it conditional on the presence of a tag, no child resources descended from that resource can be used unless they have been tagged. In this way, resources must be set up in accordance with your governance plan before they can be used.

To restrict untagged organization, folder, or project resources, you can use the `!` logical operator in a conditional query when creating your organization policy.

For example, to allow the usage of `sqladmin.googleapis.com` only in projects that have the tag `sqladmin=enabled`, you can create an organization policy that denies `sqladmin.googleapis.com` on projects that do not have the tag `sqladmin=enabled`.

  1. [Create a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) that identifies whether the resources have had proper governance applied. For example, you could create a tag with the key `sqlAdmin` and the value `enabled`, to designate that this resource should allow the usage of the Cloud SQL Admin API. For example:

![Creating a tag key and value](https://docs.cloud.google.com/static/organization-policy/images/sqladmin_tag.png)

  2. Click on the name of the newly created tag. You need the namespaced name of the tag key, listed under **Tag key path** , in the next steps to create a condition.

  3. Create a **Restrict Resource Service Usage** organization policy at the level of your organization resource to deny access to the Cloud SQL Admin API. For example:

![Creating an organization policy for restricting resources](https://docs.cloud.google.com/static/organization-policy/images/sqladmin_policy.png)

  4. Add a condition to the above organization policy, specifying that the policy is enforced if the governance tag is not present. The logical NOT operator is not supported by the condition builder, so this condition must be built in the condition editor. For example:

![Building a conditional organization policy](https://docs.cloud.google.com/static/organization-policy/images/sqladmin_condition.png)

`!resource.matchTag("012345678901/sqlAdmin", "enabled")`




Now, the `sqlAdmin=enabled` tag must be attached to or inherited by a project, before your developers can use the Cloud SQL Admin API with that project.

### Enforcing mandatory tags on resources

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enforce mandatory tags on resources by using a custom organization policy. When you enforce mandatory tags, you can only create resources that comply with your organization's tagging policies; that is, resources are bound with the tag values for the mandatory tag keys specified in the policy. For more information, see [Set up a custom constraint to enforce tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#create_custom_constraint_tags). 

## Organization policy inheritance

Constraints with list rules that are enabled using tags merge with the existing organization policy, per normal rules of [inheritance](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation). These conditional rules only apply if the condition is true.

Constraints with boolean rules that are enabled using tags override the existing organization policy. In addition, since boolean rules only have two states, true or false, then all conditional statements must be the opposite of the non-condition statement to prevent multiple tags from conflicting with each other.

For example, consider an organization policy that enforces the `disableSerialPortAccess` legacy managed constraint. The unconditional value, which is the value that is used if no conditions override it, is true. Therefore, any other conditional statements for this policy must be set to false to not conflict.

## What's next

For more information about how to use tags, read the [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) page.

For more information about how to create and manage organization policy constraints, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
