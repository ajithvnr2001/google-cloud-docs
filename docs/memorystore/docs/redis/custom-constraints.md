---
url: https://docs.cloud.google.com/memorystore/docs/redis/custom-constraints/
title: Manage Memorystore for Redis resources with custom constraints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:03.707303+00:00
---

# Manage Memorystore for Redis resources with custom constraints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Manage Memorystore for Redis resources with custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Organization Policy gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin), you can define an organization policy, which is a set of restrictions called constraints that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides [predefined constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create custom organization policies.

By implementing a custom organization policy you enforce consistent configurations and restrictions. This ensures that your Memorystore for Redis instances adhere to security best practices and regulatory requirements.

## Benefits

You can use a custom organization policy to allow or deny specific Memorystore for Redis resources. For example, if a request to create or update a Redis instance fails to satisfy custom constraint validation as set by your organization policy, the request will fail and an error will be returned to the caller.

## Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#disallow_inheritance).

## Pricing

The Organization Policy Service, including predefined and custom organization policies, is offered at no charge.

## Limitations

Like all organization policy constraints, policy changes don't apply retroactively to existing instances.

  * A new policy doesn't impact existing instance configurations.
  * An existing instance configuration remains valid, unless you change the instance configuration from a compliance to non-compliance state using the Google Cloud console, Google Cloud CLI, or RPC.
  * A scheduled maintenance update doesn't cause a policy enforcement, because maintenance doesn't change the configuration of instances.



## Before you begin

  1. **Set up your project.**

     1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
     2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

     7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

     12. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). 



### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You also need to add required roles to create Memorystore for Redis to your user account. See [Configuring access to Memorystore for Redis resources](https://docs.cloud.google.com/memorystore/docs/redis/access-control). 

## Create a custom constraint

You can create a custom constraint by using a YAML file to define the resources, methods, conditions, and actions that are subject to the constraint. These are specific to the service on which you're enforcing the organization policy. Conditions for your custom constraints must be defined using Common Expression Language. See the GitHub page about [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language).

Use the following template to create a YAML file for a custom constraint:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - redis.googleapis.com/RESOURCE_NAME
    methodTypes:
    - CREATE
    - UPDATE
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `123456789`.

  * `CONSTRAINT_NAME`: the name you want for your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers, for example, `custom.restrictInstanceToOnereplica`. The maximum length of this field is 70 characters, not counting the prefix, for example, `organizations/123456789/customConstraints/custom.allowConstraint`.

  * `RESOURCE_NAME`: the name (not the URI) of the Memorystore for Redis resource containing the object and field you want to restrict. For example, `Instance`.

  * `CONDITION`: a [CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field has a maximum length of 1000 characters. See Supported resources for more information about the resources available to write conditions against. For example, `"resource.replicaCount >= 2"`.

  * `ACTION`: the action to take if the `condition` is met. This can be either `ALLOW` or `DENY`.

  * `DISPLAY_NAME`: a human-friendly name for the constraint. This field has a maximum length of 200 characters.

  * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2000 characters.




For more information about how to create a custom constraint, see [Creating and managing custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#defining_custom_constraints).

## Set up a custom constraint

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.restrictInstanceToOnereplica`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
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
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.restrictInstanceToOnereplica`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `redis.googleapis.com/Instance`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, ``"resource.replicaCount >= 2"``. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Can only be `ALLOW`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.restrictInstanceToOnereplica`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test a custom constraint

To test a custom constraint, run a gcloud command that attempts to create a Redis instance.

For example, assume that a constraint requires that Redis instances should not have more than one replica. You could test this constraint by running the `gcloud redis instances create` command with replica-count set to 2 as demonstrated in the following snippet:
    
    
    gcloud redis instances create redis-test-instance \
        --project=my-project \
        --tier=standard \
        --size=16 \
        --region=us-central1 \
        --redis-version=redis_7_0 \
        --network=projects/my-project/global/networks/default \
        --connect-mode=PRIVATE_SERVICE_ACCESS \
        --read-replicas-mode=READ_REPLICAS_ENABLED \
        --replica-count=2
    

The output is similar to the following:
    
    
    Operation denied by custom org policies: ["customConstraints/custom.restrictInstanceToOnereplica": "Prevent users from creating Redis instances with more than one replica"]
    

## Memorystore for Redis supported resources and operations

The following Memorystore for Redis custom constraint fields are available to use when you **create or update a Memorystore for Redis resource**.

  * [Memorystore for Redis Instance](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances)
    * `resource.alternativeLocationId`
    * `resource.authEnabled`
    * `resource.authorizedNetwork`
    * `resource.availableMaintenanceVersions`
    * `resource.connectMode`
    * `resource.customerManagedKey`
    * `resource.displayName`
    * `resource.locationId`
    * `resource.maintenancePolicy.description`
    * `resource.maintenancePolicy.weeklyMaintenanceWindow.day`
    * `resource.maintenanceVersion`
    * `resource.memorySizeGb`
    * `resource.name`
    * `resource.persistenceConfig.persistenceMode`
    * `resource.persistenceConfig.rdbSnapshotPeriod`
    * `resource.persistenceConfig.rdbSnapshotStartTime`
    * `resource.readReplicasMode`
    * `resource.redisConfigs`
    * `resource.redisVersion`
    * `resource.replicaCount`
    * `resource.reservedIpRange`
    * `resource.secondaryIpRange`
    * `resource.suspensionReasons`
    * `resource.tier`
    * `resource.transitEncryptionMode`



## Example custom constraints

The following table provides an example custom constraint that restricts Redis instance to one replica:

Description | Constraint syntax  
---|---  
Restrict Redis instances with one replicas | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictInstanceToOnereplica
        resourceTypes:
        - redis.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.replicaCount >= 2"
        actionType: DENY
        displayName: Restrict Redis instances to one replica
        description: Prevent users from creating Redis instances with more than one replica  
  
## What's next

  * See [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to learn more about organization policies.
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).
  * See the full list of predefined [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
