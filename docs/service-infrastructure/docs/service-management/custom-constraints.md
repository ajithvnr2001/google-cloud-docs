---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/custom-constraints/
title: Manage Service Management resources with custom constraints \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:26.579012+00:00
---

# Manage Service Management resources with custom constraints  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Manage Service Management resources with custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `servicemanagement.googleapis.com/Service`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

## Before you begin

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

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Service Management supported resources

The following table lists the Service Management resources that you can reference in custom constraints. 

Resource | Field  
---|---  
servicemanagement.googleapis.com/Service |  `resource.authentication.providers.audiences`  
`resource.authentication.providers.authorizationUrl`  
`resource.authentication.providers.issuer`  
`resource.authentication.providers.jwksUri`  
`resource.authentication.providers.jwtLocations.cookie`  
`resource.authentication.providers.jwtLocations.header`  
`resource.authentication.providers.jwtLocations.query`  
`resource.authentication.providers.jwtLocations.valuePrefix`  
`resource.authentication.rules.allowWithoutCredential`  
`resource.authentication.rules.oauth.canonicalScopes`  
`resource.authentication.rules.requirements.audiences`  
`resource.authentication.rules.requirements.providerId`  
`resource.authentication.rules.selector`  
`resource.backend.rules.address`  
`resource.backend.rules.deadline`  
`resource.backend.rules.disableAuth`  
`resource.backend.rules.jwtAudience`  
`resource.backend.rules.operationDeadline`  
`resource.backend.rules.pathTranslation`  
`resource.backend.rules.protocol`  
`resource.backend.rules.selector`  
`resource.billing.consumerDestinations.metrics`  
`resource.billing.consumerDestinations.monitoredResource`  
`resource.context.rules.allowedRequestExtensions`  
`resource.context.rules.allowedResponseExtensions`  
`resource.context.rules.provided`  
`resource.context.rules.requested`  
`resource.context.rules.selector`  
`resource.control.environment`  
`resource.control.methodPolicies.requestPolicies.resourcePermission`  
`resource.control.methodPolicies.requestPolicies.resourceType`  
`resource.control.methodPolicies.requestPolicies.selector`  
`resource.control.methodPolicies.selector`  
`resource.customError.rules.isErrorType`  
`resource.customError.rules.selector`  
`resource.customError.types`  
`resource.endpoints.aliases`  
`resource.endpoints.allowCors`  
`resource.endpoints.name`  
`resource.endpoints.target`  
`resource.logging.consumerDestinations.logs`  
`resource.logging.consumerDestinations.monitoredResource`  
`resource.logging.producerDestinations.logs`  
`resource.logging.producerDestinations.monitoredResource`  
`resource.logs.description`  
`resource.logs.displayName`  
`resource.logs.name`  
`resource.metrics.description`  
`resource.metrics.displayName`  
`resource.metrics.launchStage`  
`resource.metrics.metadata.ingestDelay`  
`resource.metrics.metadata.samplePeriod`  
`resource.metrics.metadata.timeSeriesResourceHierarchyLevel`  
`resource.metrics.metricKind`  
`resource.metrics.monitoredResourceTypes`  
`resource.metrics.name`  
`resource.metrics.type`  
`resource.metrics.unit`  
`resource.metrics.valueType`  
`resource.monitoredResources.description`  
`resource.monitoredResources.displayName`  
`resource.monitoredResources.launchStage`  
`resource.monitoredResources.name`  
`resource.monitoredResources.type`  
`resource.monitoring.consumerDestinations.metrics`  
`resource.monitoring.consumerDestinations.monitoredResource`  
`resource.monitoring.producerDestinations.metrics`  
`resource.monitoring.producerDestinations.monitoredResource`  
`resource.name`  
`resource.producerProjectId`  
`resource.publishing.apiShortName`  
`resource.publishing.codeownerGithubTeams`  
`resource.publishing.docTagPrefix`  
`resource.publishing.documentationUri`  
`resource.publishing.githubLabel`  
`resource.publishing.librarySettings.cppSettings.common.destinations`  
`resource.publishing.librarySettings.cppSettings.common.selectiveGapicGeneration.methods`  
`resource.publishing.librarySettings.dotnetSettings.common.destinations`  
`resource.publishing.librarySettings.dotnetSettings.common.selectiveGapicGeneration.methods`  
`resource.publishing.librarySettings.dotnetSettings.forcedNamespaceAliases`  
`resource.publishing.librarySettings.dotnetSettings.handwrittenSignatures`  
`resource.publishing.librarySettings.dotnetSettings.ignoredResources`  
`resource.publishing.librarySettings.dotnetSettings.renamedResources`  
`resource.publishing.librarySettings.dotnetSettings.renamedServices`  
`resource.publishing.librarySettings.goSettings.common.destinations`  
`resource.publishing.librarySettings.goSettings.common.selectiveGapicGeneration.methods`  
`resource.publishing.librarySettings.javaSettings.common.destinations`  
`resource.publishing.librarySettings.javaSettings.common.selectiveGapicGeneration.methods`  
`resource.publishing.librarySettings.javaSettings.libraryPackage`  
`resource.publishing.librarySettings.javaSettings.serviceClassNames`  
`resource.publishing.librarySettings.launchStage`  
`resource.publishing.librarySettings.nodeSettings.common.destinations`  
`resource.publishing.librarySettings.nodeSettings.common.selectiveGapicGeneration.methods`  
`resource.publishing.librarySettings.phpSettings.common.destinations`  
`resource.publishing.librarySettings.phpSettings.common.selectiveGapicGeneration.methods`  
`resource.publishing.librarySettings.pythonSettings.common.destinations`  
`resource.publishing.librarySettings.pythonSettings.common.selectiveGapicGeneration.methods`  
`resource.publishing.librarySettings.pythonSettings.experimentalFeatures.restAsyncIoEnabled`  
`resource.publishing.librarySettings.restNumericEnums`  
`resource.publishing.librarySettings.rubySettings.common.destinations`  
`resource.publishing.librarySettings.rubySettings.common.selectiveGapicGeneration.methods`  
`resource.publishing.librarySettings.version`  
`resource.publishing.methodSettings.autoPopulatedFields`  
`resource.publishing.methodSettings.longRunning.initialPollDelay`  
`resource.publishing.methodSettings.longRunning.maxPollDelay`  
`resource.publishing.methodSettings.longRunning.pollDelayMultiplier`  
`resource.publishing.methodSettings.longRunning.totalPollTimeout`  
`resource.publishing.methodSettings.selector`  
`resource.publishing.newIssueUri`  
`resource.publishing.organization`  
`resource.publishing.protoReferenceDocumentationUri`  
`resource.publishing.restReferenceDocumentationUri`  
`resource.quota.limits.defaultLimit`  
`resource.quota.limits.description`  
`resource.quota.limits.displayName`  
`resource.quota.limits.duration`  
`resource.quota.limits.freeTier`  
`resource.quota.limits.maxLimit`  
`resource.quota.limits.metric`  
`resource.quota.limits.name`  
`resource.quota.limits.unit`  
`resource.quota.limits.values`  
`resource.quota.metricRules.metricCosts`  
`resource.quota.metricRules.selector`  
`resource.systemParameters.rules.parameters.httpHeader`  
`resource.systemParameters.rules.parameters.name`  
`resource.systemParameters.rules.parameters.urlQueryParameter`  
`resource.systemParameters.rules.selector`  
`resource.title`  
`resource.usage.producerNotificationChannel`  
`resource.usage.requirements`  
`resource.usage.rules.allowUnregisteredCalls`  
`resource.usage.rules.selector`  
`resource.usage.rules.skipServiceControl`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.authorizationCheck`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

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
      - UPDATE 
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.authorizationCheck`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `servicemanagement.googleapis.com/Service`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `resource.name == \"test-service-name\"`. 

For more information about the resources available to write conditions against, see Supported resources. 

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.authorizationCheck`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint based on the attributes of the Service resource. These rules can be used to allow or deny certain `CreateServiceConfig` requests

Before you begin, you should know the following:

  * Your organization ID
  * A project ID



### Create the constraint

  1. Save the following file as `constraint-file-name.yaml`:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.authorizationCheck
             resourceTypes:
             -  servicemanagement.googleapis.com/Service
             methodTypes:
             -   CREATE
             -   UPDATE
             condition: resource.name == \"test-service-name\"
             actionType: ALLOW
             displayName: Check Configuration time policy enforcement
             description: Organization policies, defined with CEL and enforced via service manager APIs, allow admins to control service configurations through inheritable and granular rules.
         

This defines a constraint where the service name for every Service Management should be equal to `test-service-name`.

  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint ~/constraint-file-name.yaml
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output is similar to the following:
         
         CUSTOM_CONSTRAINT ACTION_TYPE METHOD_TYPES RESOURCE_TYPES DISPLAY_NAME
         custom.configTimeEnforcement ALLOW CREATE,UPDATE servicemanagement.googleapis.com/Service Configuration time policy enforcement
         




### Create the policy

  1. Save the following file as `policy-file-name.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.configTimeEnforcement
         spec:
           rules:
         - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy ~/policy-file-name.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT LIST_POLICY BOOLEAN_POLICY ETAG
         custom.configTimeEnforcement - SET COCsm5QGENiXi2E=
         




After you apply the policy, wait for about two minutes for Google Cloud to start enforcing the policy.

### Test the policy

Run the following command to create the service configuration to check the constraints.
    
    
      gcloud endpoints services deploy policy-file-name.yaml
    

The output is similar to the following:
    
    
      Operation denied by custom org policies: ["customConstraints/custom.authorizationCheck": "error Message"]
    

## What's next

  * To learn more about Service Management options, see the Service Management overview.
  * To help you solve common issues that you might encounter when using Service Management, see Troubleshooting.
  * See the predefined organization policy constraints for Service Management.
  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
