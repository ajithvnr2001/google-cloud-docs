---
url: https://docs.cloud.google.com/organization-policy/create-organization-policies/
title: Create organization policies \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:05:01.395325+00:00
---

# Create organization policies  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/create-organization-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Create organization policies Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to create an organization policy with managed and legacy managed constraints. If you want greater control over your organization policies, you can create [custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints).

For more information on constraints and the problems they solve, review the [list of all Organization Policy Service constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

## Before you begin

  * Read the [Organization Policy Service overview](https://docs.cloud.google.com/organization-policy/overview) page to learn how organization policy works.

  * Read the [Hierarchy evaluation](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation) page to learn about policy inheritance.




### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Delegate organization policy administration

To delegate the administration of organization policies to another principal, add [a condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to the role binding:
    
    
    "bindings": [
      {
        "role": "roles/orgpolicy.policyAdmin",
        "members": [
          "PRINCIPAL_1",
          "PRINCIPAL_2"
        ],
        "condition": {
          "title": "TITLE",
          "description": "DESCRIPTION",
          "expression": "resource.matchTag('TAG_KEY', 'TAG_VALUE')"
        }
      }
    ]

Replace the following:

  * `PRINCIPAL_1,PRINCIPAL_2`: a list of principals to which you want to delegate the Organization policy administrator role.

  * `TITLE`: the title of your conditional expression&emdash;for example, "Organization policy administrator for development environments".

  * `DESCRIPTION`: an optional description for your expression.

  * `TAG_KEY`: The namespaced name of the tag key&emdash;for example, `123456789012/environment`.

  * `TAG_VALUE`: The name of the tag value. The role is only granted on resources on which this tag is attached&emdash;for example, `development`.




For more information about using conditions in allow policies, see [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).

## Use list rules in an organization policy

You can set an organization policy on your organization resource that uses list rules to deny access to a particular service. The following process describes how to set an organization policy using the Google Cloud CLI. For instructions on how to view and set organization policies using the Google Cloud console, see [Apply organization policies](https://docs.cloud.google.com/organization-policy/apply-policies).

Organization policies using list rules cannot have more than 500 individual allowed or denied values, and cannot be more than 32 KB. If an organization policy is created or updated to have more than 500 values, or be greater than 32 KB in size, it can't save successfully, and the request will return an error.

### Set up enforcement on the organization resource

To set up enforcement on an organization using gcloud CLI, follow these steps:

  1. Get the current policy on the organization resource using the `describe` command. This command returns the policy directly applied to this resource:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --organization=ORGANIZATION_ID
         

Replace the following:

     * `ORGANIZATION_ID`: a unique identifier for the organization resource. [Organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) is formatted as decimal numbers, and cannot have leading zeros.

     * `CONSTRAINT_NAME`: the constraint for the service that you want to enforce. For example, the `gcp.restrictNonCmekServices` constraint restricts which services can create resources without customer-managed encryption keys (CMEK).

You can also apply the organization policy to a folder or a project with the `--folder` or the `--project` flags, and the [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#folder-permissions) and [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects), respectively.

The response returns the current organization policy, if one exists. For example:
    
    name: projects/841166443394/policies/gcp.resourceLocations
    spec:
      etag: BwW5P5cEOGs=
      inheritFromParent: true
      rules:
      - condition:
          expression: resource.matchTagId("tagKeys/1111", "tagValues/2222")
        values:
          allowedValues:
          - in:us-east1-locations
      - condition:
          expression: resource.matchTag("123/env", "prod")
        values:
          allowedValues:
          - in:us-west1-locations
      - values:
          deniedValues:
          - in:asia-south1-locations
      updateTime: '2021-01-19T12:00:51.095Z'
    

If a policy isn't set, this will return a `NOT_FOUND` error:
    
    ERROR: (gcloud.org-policies.describe) NOT_FOUND: Requested entity was not found.
    

  2. Set the policy on the organization using the `set-policy` command. This overwrites any policy attached to the resource.

     1. Create a temporary file `/tmp/policy.yaml` to store the policy:
            
            name: organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME
            spec:
              rules:
              - values:
                  deniedValues:
                  - VALUE_A
            

     2. Run the `set-policy` command:
            
            gcloud org-policies set-policy /tmp/policy.yaml
            

  3. View the current effective policy using `describe --effective`. This returns the organization policy as it is evaluated at this point in the resource hierarchy with inheritance included.
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --organization=ORGANIZATION_ID
         

The output of the command will be:
         
         name: organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME
         spec:
           etag: BwVJi0OOESU=
           rules:
           - values:
               deniedValues:
               - VALUE_A
         

Because this organization policy was set at the organization level, it will be [inherited](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation) by all child resources that allow inheritance.




Changes to organization policies can take up to 15 minutes to be fully enforced.

### Set up enforcement against a hierarchy subtree

Constraints with list rules take explicitly defined values to determine which resources should be allowed or denied. Some constraints can also accept values that use the prefix `under:`, which specifies a subtree with that resource as the root. Using the `under:` prefix on an allowed or denied value causes the organization policy to act on that resource and all of its children. For information about the constraints that allow using the `under:` prefix, see the [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) page.

A value that uses the `under:` prefix is called a hierarchy subtree string. A hierarchy subtree string specifies the type of resource it applies to. For example, using a subtree string of `projects/PROJECT_ID` when setting the `constraints/compute.storageResourceUseRestrictions` constraint will allow or deny the use of Compute Engine storage for `PROJECT_ID` and all of its children.

  1. Get the current policy on the organization resource using the `describe` command:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME \
           --organization=ORGANIZATION_ID
         

Replace the following:

     * [`ORGANIZATION_ID`](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) is a unique identifier for the organization resource.

     * `CONSTRAINT_NAME` is the constraint for the service that you want to enforce.

You can also apply the organization policy to a folder or a project with the `--folder` or the `--project` flags, and the [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#configuring_access_to_folders) and [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects), respectively.

If a policy isn't set, this will return a `NOT_FOUND` error:
    
    ERROR: (gcloud.org-policies.describe) NOT_FOUND: Requested entity was not found.
    

  2. Set the policy on the project using the `set-policy` command. The `under:` prefix sets the constraint to deny the named resource and all of its child resources.

     1. Create a temporary file `/tmp/policy.yaml` to store the policy:
            
            name: organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME
            spec:
              rules:
              - values:
                  deniedValues:
                  - under:folders/VALUE_A
            

     2. Run the `set-policy` command:
            
            gcloud org-policies set-policy /tmp/policy.yaml
            

Where:

     * `under:` is a prefix that signifies what follows is a subtree string.

     * `folders/VALUE_A` is the [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#configuring_access_to_folders) of the root resource you want to deny. This resource and all of its children in the resource hierarchy will be denied.

You can also apply the `under:` prefix to organizations and projects, as in the following examples:

     * `under:organizations/VALUE_X`

     * `under:projects/VALUE_Y`

  3. View the current effective policy using `describe --effective`.
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --organization=ORGANIZATION_ID
         

The output of the command will be:
         
         name: organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - values:
               deniedValues:
               - under:folders/VALUE_A
         

The policy now evaluates to deny the folder VALUE_A and all of its child resources.




Changes to organization policies can take up to 15 minutes to be fully enforced.

### Merge the organization policy on a project

You can set an organization policy on a resource, which will merge with any policy inherited from its parent resource. This merged policy will then be evaluated to create a new effective policy based on the rules of [inheritance](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation).

  1. Get the current policy on the resource using the `describe` command:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME \
           --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the [unique identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

     * `CONSTRAINT_NAME`: the constraint for the service that you want to enforce.

If a policy isn't set, this will return a `NOT_FOUND` error:
    
    ERROR: (gcloud.org-policies.describe) NOT_FOUND: Requested entity was not found.
    

  2. Display the current effective policy using the `describe --effective` command:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --project=PROJECT_ID
         

The output of the command will include a denied value that it inherits from the organization resource:
         
         name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - values:
               deniedValues:
               - VALUE_A
         

  3. Set the policy on the project using the `set-policy` command.

     1. Create a temporary file `/tmp/policy.yaml` to store the policy:
            
            name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
            spec:
              inheritFromParent: true
              rules:
              - values:
                  deniedValues:
                  - VALUE_B
                  - VALUE_C
            

     2. Run the `set-policy` command:
            
            gcloud org-policies set-policy /tmp/policy.yaml
            

  4. Use the `describe --effective` command again to display the updated policy:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --project=PROJECT_ID
         

The output of the command will include the effective result of merging the policy from the resource and from the parent:
         
         name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - values:
               deniedValues:
                 - VALUE_A
                 - VALUE_B
                 - VALUE_C
         




Changes to organization policies can take up to 15 minutes to be fully enforced.

### Restore default constraint behavior

You can use the `reset` command to reset the policy to use the constraint's default behavior. For a list of all available constraints and their default values, see [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints). The following example assumes that the default constraint behavior is to allow all values.

  1. Get the effective policy on the project to show the current merged policy:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --project=PROJECT_ID
         

Replace PROJECT_ID with the [unique identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project. The output of the command will be:
         
         name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - values:
               deniedValues:
               - VALUE_A
               - VALUE_B
               - VALUE_C
         

  2. Reset the organization policy using the `reset` command.
         
         gcloud org-policies reset CONSTRAINT_NAME \
             --project=PROJECT_ID
         

  3. Get the effective policy to verify the default behavior:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --project=PROJECT_ID
         

The output of the command will allow all values:
         
         name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - allowAll: true
         




Changes to organization policies can take up to 15 minutes to be fully enforced.

### Delete an organization policy

You can delete an organization policy from a resource. A resource without an organization policy set will inherit any policy of its parent resource. If you delete the organization policy on the organization resource, the effective policy will be the constraint's default behavior.

The following steps describe how to delete an organization policy on an organization.

  1. Delete the policy on the organization resource using the `delete` command:
         
         gcloud org-policies delete \
           CONSTRAINT_NAME \
           --organization=ORGANIZATION_ID
         

Replace [ORGANIZATION_ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) with the unique identifier for the organization resource. The output of the command will be:
         
         Deleted policy
         [organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME].
         {}
         

  2. Get the effective policy on the organization to verify it's not enforced:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --organization=ORGANIZATION_ID
         

The output of the command will be:
         
         name: organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - allowAll: true
         




The following steps describe how to delete an organization policy on a project:

  1. Delete the policy on a project using the `delete` command:
         
         gcloud org-policies delete \
           CONSTRAINT_NAME \
           --project=PROJECT_ID
         

Where `PROJECT_ID` is the [unique identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project. The output of the command will be:
         
         Deleted policy
         [projects/PROJECT_ID/policies/CONSTRAINT_NAME].
         {}
         

  2. Get the effective policy on the project to verify it's not enforced:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --project=PROJECT_ID
         

The output of the command will be:
         
         name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - allowAll: true
         




Changes to organization policies can take up to 15 minutes to be fully enforced.

## Use boolean rules in organization policy

### Set up enforcement on the organization resource

The following process describes how to set an organization policy with boolean rules using the Google Cloud CLI. For instructions on how to view and set organization policies using the Google Cloud console, see [Apply organization policies](https://docs.cloud.google.com/organization-policy/apply-policies).

  1. Get the current policy on the organization resource by using the `describe` command:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME \
           --organization=ORGANIZATION_ID
         

Replace [`ORGANIZATION_ID`](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) with the unique identifier for the organization resource. You can also apply the organization policy to a folder or a project with the `--folder` or the `--project` flags, and the [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#configuring_access_to_folders) and [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects), respectively.

If a policy isn't set, this will return a `NOT_FOUND` error:
         
         ERROR: (gcloud.org-policies.describe) NOT_FOUND: Requested entity was not found.
         

  2. Set the policy on the project using the `set-policy` command.

     1. Create a temporary file `/tmp/policy.yaml` to store the policy:
            
            name: organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME
            spec:
              rules:
              - enforce: true
            

     2. Run the `set-policy` command:
            
            gcloud org-policies set-policy /tmp/policy.yaml
            

  3. View the current effective policy using `describe --effective`:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --organization=ORGANIZATION_ID
         

The output of the command will be:
         
         name: organizations/ORGANIZATION_ID/policies/BOOLEAN_CONSTRAINT
         spec:
           rules:
           - enforce: true
         




Changes to organization policies can take up to 15 minutes to be fully enforced.

### Override the organization policy for a project

To override the organization policy for a project, set a policy that disables enforcement of the constraint to all resources in the hierarchy below the project.

  1. Get the current policy on the resource to show it's empty.
         
         gcloud org-policies describe \
           CONSTRAINT_NAME \
           --project=PROJECT_ID
         

Where `PROJECT_ID` is the [unique identifier](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

If a policy isn't set, this will return a `NOT_FOUND` error:
         
         ERROR: (gcloud.org-policies.describe) NOT_FOUND: Requested entity was not found.
         

  2. Get the effective policy on the project, which confirms that the constraint is being enforced at this project.
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --project=PROJECT_ID
         

The output of the command will be:
         
         name: projects/PROJECT_ID/policies/BOOLEAN_CONSTRAINT
         spec:
           rules:
           - enforce: true
         

  3. Set the policy on the project using the `set-policy` command.

     1. Create a temporary file `/tmp/policy.yaml` to store the policy:
            
            name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
            spec:
              rules:
              - enforce: false
            

     2. Run the `set-policy` command:
            
            gcloud org-policies set-policy /tmp/policy.yaml
            

  4. Get the effective policy to show that it is no longer enforced on the project.
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --project=PROJECT_ID
         

The output of the command will be:
         
         name: organizations/ORGANIZATION_ID/policies/BOOLEAN_CONSTRAINT
         spec:
           rules:
           - enforce: false
         




Changes to organization policies can take up to 15 minutes to be fully enforced.

### Delete an organization policy

You can delete an organization policy from a resource. A resource without an organization policy set will inherit any policy of its parent resource. If you delete the organization policy on the organization resource, the effective policy will be the constraints' default behavior.

The following steps describe how to delete an organization policy on an organization and a project.

  1. Delete the policy from the organization resource using the `delete` command:
         
         gcloud org-policies delete \
           CONSTRAINT_NAME \
           --organization=ORGANIZATION_ID
         

Replace [`ORGANIZATION_ID`](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) with a unique identifier for the organization resource. The output of the command will be:
         
         Deleted policy
         [organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME].
         {}
         

  2. Get the effective policy on the organization to verify it's not enforced:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --organization=ORGANIZATION_ID
         

If a policy isn't set, this will return a `NOT_FOUND` error:
         
         ERROR: (gcloud.org-policies.describe) NOT_FOUND: Requested entity was not found.
         

  3. Delete the organization policy from the project using the `delete` command:
         
         gcloud org-policies delete \
           CONSTRAINT_NAME \
           --project=PROJECT_ID
         

The output of the command will be:
         
         Deleted policy
         [organizations/ORGANIZATION_ID/policies/CONSTRAINT_NAME].
         {}
         

  4. Get the effective policy on the project to verify it's not enforced:
         
         gcloud org-policies describe \
           CONSTRAINT_NAME --effective \
           --project=PROJECT_ID
         

Replace [`PROJECT_ID`](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) with the unique identifier of your project.

If a policy isn't set, this will return a `NOT_FOUND` error:
         
         ERROR: (gcloud.org-policies.describe) NOT_FOUND: Requested entity was not found.
         




Changes to organization policies can take up to 15 minutes to be fully enforced.

## Using managed constraints in an organization policy

Managed constraints are built on the [custom organization policy](https://docs.cloud.google.com/organization-policy/overview#custom-constraints) platform. They can use Policy Simulator for Organization Policy Service and dry-run organization policies to more safely deploy policy changes.

### View and identify managed constraints

To see the available managed constraints for your organization, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project, folder, or organization for which you want to view organization policies. The **Organization policies** page that appears displays a list of organization policy constraints that are available for this resource.

  3. You can filter or sort the list of organization policies by constraint type to find managed constraints. Select the managed constraint you want to view details for from the list. On the **Policy details** page that appears, you can see the source of this organization policy, the effective policy evaluation on this resource, the current configuration of the organization policy on this resource, details about the constraint, and the default parameters of constraints that use them.




###  gcloud 

To list the managed and custom constraints enforced in organization policies on an organization, use the [`org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command.
    
    
    gcloud org-policies list-custom-constraints \
      --organization=ORGANIZATION_ID
    

Replace ORGANIZATION_ID with the ID of your organization.

To get details on a particular managed constraint for a resource, use the [`org-policies describe-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe-custom-constraint) command.
    
    
    gcloud org-policies describe-custom-constraint CONSTRAINT_NAME \
        --organization=ORGANIZATION_ID
    

Replace the following:

  * `CONSTRAINT_NAME`: the name of the managed constraint you want to get details on. For example, `iam.managed.disableServiceAccountKeyUpload`.

  * `ORGANIZATION_ID`: the ID of your organization.




###  REST 

To list the managed and custom constraints set in organization policies on an organization, use the [`organizations.customConstraints.list`](https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest/v2/organizations.customConstraints/list) method.
    
    
      GET https://orgpolicy.googleapis.com/v2/{parent=organizations/ORGANIZATION_ID}/customConstraints
    

Replace ORGANIZATION_ID with the ID of your organization.

### Creating and updating managed constraints

Organization policies are defined by the configuration of the constraint. They can be set on a resource, inherited from a parent resource, or reset to the Google-managed default behavior.

**Note:** Managed constraints that are inherited from a parent resource aren't merged to evaluate the effective policy on a given resource. A resource that inherits a managed constraint enforces the constraint as it was set on the parent resource or overrides the constraint with its own policy. 

To create or update an organization policy based on a managed constraint, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.



[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  1. From the project picker, select the project, folder, or organization for which you want to edit the organization policy. The **Organization policies** page that appears displays a filterable list of organization policy constraints that are available for this resource.

  2. Select the managed constraint for which you want to update the organization policy from the list.

  3. To update the organization policy for this resource, click **Manage policy**.

  4. On the **Edit policy** page, select **Override parent's policy**.

  5. Select **Add a rule**.

  6. Under **Enforcement** , select whether enforcement of this organization policy should be on or off.

  7. Optionally, to make the organization policy conditional on a tag, click **Add condition**. If you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more details, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

  8. If this constraint supports parameters, they appear under **Parameters** with the configured values displayed. If the parameters have not been configured, the Google-managed default values appear instead.

To change a parameter, select edit **Edit**.

     1. Under **Values** , select **Default** to reset this constraint to use and display the Google-managed default values.

Select **User-defined** to configure the parameter.

     1. For parameters that accept a list of values, enter a value to allow or deny into the field. Select add **Add a value** to add more fields.

The Common Expression Language (CEL) expression used to validate the parameter values is described under **Valid values expression**. All user-defined values must satisfy that expression.

     1. For parameters that are boolean, determine whether the parameter should be applied or not by selecting **True** or **False**.

     2. Click **Save**.

  9. Optionally, to preview the impact of your organization policy change before it is enforced, click **Test changes**. For more information about testing organization policy changes, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies).

  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**.




###  gcloud 

  1. Create a YAML file to define the organization policy. If this constraint doesn't support parameters, omit the `parameters` block under `rules`.
         
         name: RESOURCE_TYPE/RESOURCE_ID/policies/CONSTRAINT_NAME
         spec:
         rules:
             - enforce: ENFORCEMENT_STATE
               parameters:
                 LIST_PARAMETER:
                    - LIST_VALUE_1
                    - LIST_VALUE_2
                 BOOLEAN_PARAMETER: BOOLEAN_VALUE
         
         dryRunSpec:
           rules:
           - enforce: ENFORCEMENT_STATE
             parameters:
               LIST_PARAMETER:
                  - LIST_VALUE_1
                  - LIST_VALUE_2
               BOOLEAN_PARAMETER: BOOLEAN_VALUE
         

Replace the following:

     * `RESOURCE_TYPE` with `organizations`, `folders`, or `projects`.

     * `RESOURCE_ID` with your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.

     * `CONSTRAINT_NAME` with the name of the constraint you want to set.

     * `ENFORCEMENT_STATE` with `true` to enforce this organization policy when set, or `false` to disable it when set.

     * `LIST_PARAMETER` with the name of the list parameter to configure. See the constraint description for a list of available parameters.

     * `LIST_VALUE_1`, `LIST_VALUE_2`, and other list values with a list of values to allow or deny, based on the configuration of this parameter. See the constraint description for details on acceptable values.

     * `BOOLEAN_PARAMETER` with the name of the boolean parameter to configure. See the constraint description for a list of available parameters.

     * `BOOLEAN_VALUE` with `True` or `False`.

Optionally, to make the organization policy conditional on a tag, add a `condition` block to the `rules`. If you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more details, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

  2. Run the [`org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) command with the `dryRunSpec` flag to set the organization policy in dry-run mode:
         
         gcloud org-policies set-policy POLICY_PATH \
            --update-mask=dryRunSpec
         

Replace `POLICY_PATH` with the full path to your organization policy YAML file.

For more information about dry-run organization policies, see [Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies).

  3. Use the [`policy-intelligence simulate orgpolicy`](https://docs.cloud.google.com/sdk/gcloud/reference/policy-intelligence/simulate/orgpolicy) command to preview the impact of your organization policy change before it is enforced:
         
         gcloud policy-intelligence simulate orgpolicy \
           --organization=ORGANIZATION_ID \
           --policies=POLICY_PATH
         

Replace the following:

     * `ORGANIZATION_ID` with your organization ID, such as `1234567890123`. Simulating changes over multiple organizations is not supported.

     * `POLICY_PATH` with the full path to your organization policy YAML file.

For more information about testing organization policy changes, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

  4. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag:
         
         gcloud org-policies set-policy POLICY_PATH \
           --update-mask=spec
         

Replace `POLICY_PATH` with the full path to your organization policy YAML file.




###  REST 

To set the organization policy, use the [`organizations.policies.create`](https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest/v2/organizations.policies/create) method.
    
    
    POST https://orgpolicy.googleapis.com/v2/{parent=organizations/ORGANIZATION_ID}/policies
    

The request JSON body contains the definition of an organization policy. If this constraint doesn't support parameters, omit the `parameters` block under `rules`.
    
    
    {
      "name": "RESOURCE_TYPE/RESOURCE_ID/policies/CONSTRAINT_NAME",
      "spec": {
        "rules": [
          {
            "enforce": ["ENFORCEMENT_STATE"],
            "parameters": {
              "LIST_PARAMETER": [
                "LIST_VALUE_1",
                "LIST_VALUE_2"
              ],
              BOOLEAN_PARAMETER: BOOLEAN_VALUE
            }
          }
        ]
      }
      "dryRunSpec": {
        "rules": [
          {
            "enforce": ["ENFORCEMENT_STATE"],
            "parameters": {
              "LIST_PARAMETER": [
                "LIST_VALUE_1",
                "LIST_VALUE_2"
              ],
              BOOLEAN_PARAMETER: BOOLEAN_VALUE
            }
          }
        ]
      }
    }
    

Replace the following:

  * `RESOURCE_TYPE` with `organizations`, `folders`, or `projects`.

  * `RESOURCE_ID` with your organization ID, folder ID, project ID, or project number, depending on the type of resource specified in `RESOURCE_TYPE`.

  * `CONSTRAINT_NAME` with the name of the constraint you want to set.

  * `ENFORCEMENT_STATE` with `true` to enforce this organization policy when set, or `false` to disable it when set.

  * `LIST_PARAMETER` with the name of the list parameter to configure. See the constraint description for a list of available parameters.

  * `LIST_VALUE_1`, `LIST_VALUE_2`, and other list values with a list of values to allow or deny, based on the configuration of this parameter. See the constraint description for details on acceptable values.

  * `BOOLEAN_PARAMETER` with the name of the boolean parameter to configure. See the constraint description for a list of available parameters.

  * `BOOLEAN_VALUE` with `True` or `False`.




Optionally, to make the organization policy conditional on a tag, add a `condition` block to the `rules`. If you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more details, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

For more information about dry-run organization policies, see [Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies).

Changes to organization policies can take up to 15 minutes to be fully enforced.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
