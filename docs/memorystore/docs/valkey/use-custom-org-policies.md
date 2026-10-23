---
url: https://docs.cloud.google.com/memorystore/docs/valkey/use-custom-org-policies/
title: Enforce consistent configurations and restrictions for your instances by using custom organization policy constraints \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:42.461944+00:00
---

# Enforce consistent configurations and restrictions for your instances by using custom organization policy constraints  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/use-custom-org-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Enforce consistent configurations and restrictions for your instances by using custom organization policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create, set up, and manage custom organization policy constraints for Memorystore for Valkey instances. For an overview of custom organization policies, see [custom organization policies](https://docs.cloud.google.com/memorystore/docs/valkey/about-org-policies#custom-org-policies).

The Google Cloud Organization Policy Service service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/organization-policy/create-organization-policies#required-roles), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation). You can enforce organization policies at the organization, folder, or project level.

The Organization Policy service provides [predefined constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services, including Memorystore for Valkey. However, if you want more granular, customizable control over specific fields that your organization policies restrict, then you can create custom constraints and use these constraints in organization policies.

By implementing custom organization policy constraints, you enforce consistent configurations and restrictions. This verifies that your instances adhere to security best practices and regulatory requirements.

You can use custom organization policies to allow or deny Memorystore for Valkey resources. For example, if you attempt to create or update an instance while a custom constraint is enforced, and the instance is non-compliant with the constraint, then Memorystore for Valkey doesn't create or update the instance. Also, any project that's added to an organization or folder which uses a custom organization policy inherits the constraints of that policy.

## Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, then Google Cloud enforces the policy on all projects in the folder. For more information about this behavior and how to change it, see [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#hierarchy_evaluation_rules).

## Before you begin

Before you begin to use custom organization policies, complete the prerequisites in this section.

### Use the Google Cloud console, Google Cloud CLI, and APIs

To use the Google Cloud console, gcloud CLI, and APIs, do the following:

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

[Go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI (gcloud CLI).

If you installed the gcloud CLI, then make sure you have the latest version by running `gcloud components update`. To access the Memorystore for Valkey gcloud CLI commands, you need at least gcloud CLI version `489.0.0`.

  4. Enable the Memorystore for Valkey API.   
[Memorystore for Valkey API](https://console.cloud.google.com/apis/library/memorystore.googleapis.com)
  5. If you're using an external identity provider (IdP), then you must first [sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 
  6. Make sure that you know your organization's [ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Assign roles

To use custom organization policies for your instances, you must have one of these [IAM roles](https://docs.cloud.google.com/memorystore/docs/valkey/access-control) in your Google Cloud project:

  * `roles/memorystore.admin` (the Memorystore Admin role)
  * `roles/owner` (the Owner role)
  * `roles/editor` (the Editor role)



In addition, you must grant the [`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (Organization Policy Administrator) role and the [`memorystore.instances.create`](https://docs.cloud.google.com/memorystore/docs/valkey/access-control#permissions_and_their_roles) permission to your user or service account. For more information about granting roles and permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

## Create and set up a custom constraint

You create a custom constraint to define the resources, methods, conditions, and actions that are subject to the constraint. These are specific to the service on which you're enforcing the organization policy.

You define conditions for the custom constraint by using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints by using CEL, see the CEL section of [Create and manage custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

After creating the custom constraint, you set it up to make it available for organization policies in your organization. You can do this by using either the Google Cloud console or the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Click the menu in the Google Cloud console menu bar, and then select the project, folder, or organization for which you're creating and setting up a custom constraint.
  3. On the **Organization policies** page, click **Custom constraint**.
  4. In the **Display name** field of the **Create custom constraint** page, enter a human-readable name for the constraint. This name is used in error messages, and you can also use it for identification and debugging purposes. This field can contain up to 200 characters.

  5. In the **Constraint ID** field, enter the ID of the custom constraint. This constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers (for example, `custom.restrictFiveShardInstances`). The maximum length of this value is 70 characters, not counting the prefix. For example: `organizations/123456789/customConstraints/custom.allowConstraint`. 

  6. In the **Description** field, enter a human-readable description of the constraint. This description is used as an error message when the organization policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. This field can contain up to 2,000 characters.

**Important** : Don't include personally identifiable information (PII) or sensitive data in the display name, constraint ID, or description because this information can be exposed in error messages.
  7. From the **Resource type** menu, select the name (not the URI) of the Memorystore for Valkey resource, containing the object and field that you want to restrict. For example: `memorystore.googleapis.com/Instance`. 
  8. From the **Enforcement method** menu, make one of the following selections: 
     * **Enforce on create** : the constraint is enforced only when you create Memorystore for Valkey instances.
     * **Enforce on create and update** : the constraint is enforced when you create and update instances.
  9. To define a CEL condition that's written against a representation of a supported service resource, do the following:

     1. In the **Condition** field, click **Edit**.
     2. In the **Add condition** dialog, enter the CEL condition. For example: `resource.shardCount == 5`.

This condition can have a maximum length of 1,000 characters. For more information about the resources available to write conditions against, see  Supported custom constraints and operations.

     3. Click **Save**.
  10. In the **Action** section, make one of the following selections that represents the action to take if the condition is met: 
     * **Allow** : if the condition evaluates to true, then the operation to create or update the instance is permitted. Every other case except those explicitly listed in the condition is blocked. 
     * **Deny** : if the condition evaluates to true, then the operation to create or update the instance is blocked.
  11. In the **YAML configuration** section, verify that the YAML configuration for the custom constraint is correct.
  12. Click **Create constraint**.



### gcloud

  1. To create a custom constraint, create a YAML file, using the following format:
         
         name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
           resourceTypes:
           - memorystore.googleapis.com/RESOURCE_NAME
           methodTypes:
           - CREATE
           - UPDATE
           condition: "CONDITION"
           actionType: ACTION
           displayName: DISPLAY_NAME
           description: DESCRIPTION

Make the following replacements:

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`.
     * `CONSTRAINT_NAME`: the name of the custom constraint. This constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers (for example, `custom.restrictFiveShardInstances`). The maximum length of this value is 70 characters, not counting the prefix. For example: `organizations/123456789/customConstraints/custom.allowConstraint`. 
     * `RESOURCE_NAME`: the name (not the URI) of the Memorystore for Valkey resource, containing the object and field that you want to restrict. For example: `memorystore.googleapis.com/Instance`.
     * `CONDITION`: a CEL condition that's written against a representation of a supported service resource. For example: `"resource.shardCount == 5"`.

This field has a maximum length of 1,000 characters. For more information about the resources available to write conditions against, see Supported custom constraints and operations.

     * `ACTION`: the action to take if the condition is met. This action can be one of the following values: 
       * `ALLOW`: if the condition evaluates to true, then the operation to create or update the instance is permitted. Every other case except those explicitly listed in the condition is blocked.
       * `DENY`: if the condition evaluates to true, then the operation to create or update the instance is blocked.
     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages, and you can also use it for identification and debugging purposes. This field can contain up to 200 characters.
     * `DESCRIPTION`: a human-readable description of the constraint. This description is used as an error message when the organization policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. This field can contain up to 2,000 characters. 
**Important** : Don't include personally identifiable information (PII) or sensitive data for the `CONSTRAINT_NAME`, `DISPLAY_NAME`, or `DESCRIPTION` because this information can be exposed in error messages.
  2. To set up a custom constraint, use the [`gcloud org-policies set-custom-constraint` ](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command:
         
         gcloud org-policies set-custom-constraint CONSTRAINT_PATH
         

Replace CONSTRAINT_PATH with the full path to the custom constraint file (for example, `/home/user/customconstraint.yaml`). 

After you set up the custom constraint, it's available as an organization policy in the list of Google Cloud organization policies.

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         




## Enforce a custom organization policy

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.restrictFiveShardInstances`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test a custom constraint

To test a custom organization policy constraint for Memorystore for Valkey, try to create or update an instance that doesn't comply with the enforced policy.

For example, suppose a constraint restricts you from [creating an instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances) if the instance has five shards. You can test this constraint by trying to create the instance and setting the shard count to five. Because the instance is non-compliant with the constraint, Memorystore for Valkey doesn't create the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type. For more information about these node types, see [Choose a node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type).

## Supported custom constraints and operations

The following Memorystore for Valkey custom constraint fields are available to use when you **create or update an instance** :

  * [Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances)
    * `resource.name`
    * `resource.replicaCount`
    * `resource.shardCount`
    * `resource.nodeType`
    * `resource.engineVersion`
    * `resource.mode`
    * `resource.kmsKey`
    * `resource.simulateMaintenanceEvent`
    * `resource.engineConfigs`
    * `resource.persistenceConfig.mode`
    * `resource.persistenceConfig.rdbConfig.rdbSnapshotPeriod`
    * `resource.persistenceConfig.rdbConfig.rdbSnapshotStartTime`
    * `resource.persistenceConfig.aofConfig.appendFsync`
    * `resource.deletionProtectionEnabled`
    * `resource.maintenancePolicy.weeklyMaintenanceWindow.day`
    * `resource.maintenancePolicy.weeklyMaintenanceWindow.startTime`
    * `resource.automatedBackupConfig.automatedBackupMode`
    * `resource.automatedBackupConfig.fixedFrequencySchedule`
    * `resource.automatedBackupConfig.retention`
    * `resource.crossInstanceReplicationConfig.instanceRole`
    * `resource.crossInstanceReplicationConfig.primaryInstance`
    * `resource.crossInstanceReplicationConfig.secondaryInstances`
    * `resource.crossInstanceReplicationConfig.primaryInstance.instance`
    * `resource.crossInstanceReplicationConfig.secondaryInstances.instance`
    * `resource.zoneDistributionConfig.zone`
    * `resource.zoneDistributionConfig.mode`
    * `resource.transitEncryptionMode`
    * `resource.authorizationMode`
    * `resource.serverCaMode`
    * `resource.managedBackupSource.backup`
    * `resource.serverCaPool`



## Sample custom constraint

The following table provides an example of a custom constraint that prevents users from creating or updating Memorystore for Valkey instances if the instances have five shards:

Description | Constraint syntax  
---|---  
Restrict creating or updating instances that have five shards | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictFiveShardInstances
        resourceTypes:
        - memorystore.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.shardCount == 5"
        actionType: DENY
        displayName: Restrict five-shard Memorystore for Valkey instances
        description: Prevent users from creating or updating instances that have
        five shards.  
  
## What's next

  * Learn more about [organization policies](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about [creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints).
  * Learn more about [creating and managing organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
