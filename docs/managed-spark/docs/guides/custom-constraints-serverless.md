---
url: https://docs.cloud.google.com/managed-spark/docs/guides/custom-constraints-serverless/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:29.984259+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/custom-constraints-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create custom constraints

Google Cloud Organization Policy gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin), you can define an organization policy, which is a set of restrictions called constraints that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides [predefined constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create custom constraints and use those custom constraints in an organization policy.

## Benefits

You can use a custom organization policy to allow or deny specific operations on Managed Service for Apache Spark batches, sessions, and session templates. For example, if a request to create a batch workload fails to satisfy custom constraint validation as set by your organization policy, the request will fail, and an error will be returned to the caller.

## Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#disallow_inheritance).

## Pricing

The Organization Policy Service, including predefined and custom constraints, is offered at no charge.

## Before you begin

  1. **Set up your project**

     1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
     2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     4. Enable the Managed Service for Apache Spark API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc-serverless&redirect=https%3A//console.cloud.google.com)

     5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

     8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     10. Enable the Managed Service for Apache Spark API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc-serverless&redirect=https%3A//console.cloud.google.com)

     11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

     14. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). 



### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

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

## Create a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions it is applied to. Managed Service for Apache Spark supports custom constraints that are applied to the `CREATE` method of the batch and session resources.

For more information about how to create a custom constraint, see [Creating and managing custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints).

### Create a custom constraint for a batch resource

To create a YAML file for a Managed Service for Apache Spark custom constraint for a batch resource, use the following format:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - dataproc.googleapis.com/Batch
    methodTypes: 
    - CREATE
    condition: CONDITION
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `123456789`.

  * `CONSTRAINT_NAME`: the name you want for your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers, for example, `custom.batchMustHaveSpecifiedCategoryLabel`. The maximum length of this field is 70 characters, not counting the prefix, for example, `organizations/123456789/customConstraints/custom.`.

  * `CONDITION`: a [CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field has a maximum length of 1000 characters. For more information about the resources available to write conditions against, see Dataproc Serverless constraints on resources and operations. Sample condition: `("category" in resource.labels) && (resource.labels['category'] in ['retail', 'ads', 'service'])`.

  * `ACTION`: the action to take if the condition is met. This can be either `ALLOW` or `DENY`.

  * `DISPLAY_NAME`: a human-friendly name for the constraint. Sample display name: "Enforce batch 'category' label requirement". This field has a maximum length of 200 characters.

  * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2000 characters. Sample description: "Only allow Dataproc batch creation if it has a 'category' label with a 'retail', 'ads', or 'service' value".




### Create a custom constraint for a session resource

To create a YAML file for a Managed Service for Apache Spark custom constraint for a session resource, use the following format:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - dataproc.googleapis.com/Session
    methodTypes: 
    - CREATE
    condition: CONDITION
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `123456789`.

  * `CONSTRAINT_NAME`: the name you want for your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers, for example, `custom.SessionNameMustStartWithTeamName`. The maximum length of this field is 70 characters, not counting the prefix, for example, `organizations/123456789/customConstraints/custom.`.

  * `CONDITION`: a [CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field has a maximum length of 1000 characters. For more information about the resources available to write conditions against, see Dataproc Serverless constraints on resources and operations. Sample condition: `(resource.name.startsWith("dataproc")`.

  * `ACTION`: the action to take if the condition is met. This can be either `ALLOW` or `DENY`.

  * `DISPLAY_NAME`: a human-friendly name for the constraint. Sample display name: "Enforce session to have a ttl < 2 hours". This field has a maximum length of 200 characters.

  * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2000 characters. Sample description: "Only allow session creation if it sets an allowable TTL".


**Note:** When you set up custom policies for sessions, you must include a constraint on the `sessionTemplate` field. This constraint must ensure that either the template ID matches an entry in the approved template IDs allow list, or that the `sessionTemplate` is left empty. This is essential to maintain organization policy restrictions and prevent users from overriding them using session templates.

### Create a custom constraint for a session template resource

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To create a YAML file for a Managed Service for Apache Spark custom constraint for a session template resource, use the following format:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - dataproc.googleapis.com/SessionTemplate
    methodTypes: 
    - CREATE
    - UPDATE
    condition: CONDITION
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `123456789`.

  * `CONSTRAINT_NAME`: the name you want for your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers, for example, `custom.SessionTemplateNameMustStartWithTeamName`. The maximum length of this field is 70 characters, not counting the prefix, for example, `organizations/123456789/customConstraints/custom.`.

  * `CONDITION`: a [CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field has a maximum length of 1000 characters. For more information about the resources available to write conditions against, see Constraints on resources and operations. Sample condition: `(resource.name.startsWith("dataproc")`.

  * `ACTION`: the action to take if the condition is met. This can be either `ALLOW` or `DENY`.

  * `DISPLAY_NAME`: a human-friendly name for the constraint. Sample display name: "Enforce session template to have a ttl < 2 hours". This field has a maximum length of 200 characters.

  * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2000 characters. Sample description: "Only allow session template creation if it sets an allowable TTL".




## Set up a custom constraint

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example ``custom.batchMustHaveSpecifiedCategoryLabel``. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
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
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, ``custom.batchMustHaveSpecifiedCategoryLabel``. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `dataproc.googleapis.com/batch`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, ``("category" in resource.labels) && (resource.labels['category'] in ['retail', 'ads', 'service'])``. 

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




## Enforce a custom constraint

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, ``custom.batchMustHaveSpecifiedCategoryLabel``. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom constraint

This section describes how to test custom constraints for batch, session, and session template resources.

### Test the custom constraint for a batch resource

The following batch creation example assumes a custom constraint has been created and enforced on batch creation to require that the batch has a "category" label attached with a value of "retail", "ads" or "service: `("category" in resource.labels) && (resource.labels['category'] in ['retail', 'ads', 'service'])`.

**Note:** The "category" label in the example doesn't have one of the required values.
    
    
    gcloud dataproc batches submit spark \
      --region us-west1
      --jars file:///usr/lib/spark/examples/jars/spark-examples.jar \
      --class org.apache.spark.examples.SparkPi  \
      --network default \
      --labels category=foo \
      --100
    

Sample output:
    
    
    Operation denied by custom org policies: ["customConstraints/custom.batchMustHaveSpecifiedCategoryLabel": ""Only allow Dataproc batch creation if it has a 'category' label with
      a 'retail', 'ads', or 'service' value""]
    

### Test the custom constraint for a session resource

The following session creation example assumes a custom constraint has been created and enforced on session creation to require that the session has a `name` starting with `orgName`.

**Note:** The session `name` label in the example doesn't start with the string `orgName`.
    
    
    gcloud beta dataproc sessions create spark test-session
      --location us-central1
    

Sample output:
    
    
    Operation denied by custom org policy:
    ["customConstraints/custom.denySessionNameNotStartingWithOrgName": "Deny session
    creation if its name does not start with 'orgName'"]
    

### Test the custom constraint for a session template resource

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following session template creation example assumes a custom constraint has been created and enforced on session template creation and update to require that the session template has a `name` starting with `orgName`.

**Note:** The session template `name` label in the example doesn't start with the string `orgName`.
    
    
    gcloud beta dataproc session-templates import test-session-template
    --source=saved-template.yaml
    

Sample output:
    
    
    Operation denied by custom org policy:
    ["customConstraints/custom.denySessionTemplateNameNotStartingWithOrgName":
    "Deny session template creation or update if its name does not start with
    'orgName'"]
    

## Constraints on resources and operations

This section lists the available Managed Service for Apache Spark custom constraints for batch and session resources.

### Supported batch constraints

The following Managed Service for Apache Spark custom constraints are available to use when you create (submit) a batch workload:

**General**

  * `resource.labels`



**PySparkBatch**

  * `resource.pysparkBatch.mainPythonFileUri`
  * `resource.pysparkBatch.args`
  * `resource.pysparkBatch.pythonFileUris`
  * `resource.pysparkBatch.jarFileUris`
  * `resource.pysparkBatch.fileUris`
  * `resource.pysparkBatch.archiveUris`



**SparkBatch**

  * `resource.sparkBatch.mainJarFileUri`
  * `resource.sparkBatch.mainClass`
  * `resource.sparkBatch.args`
  * `resource.sparkBatch.jarFileUris`
  * `resource.sparkBatch.fileUris`
  * `resource.sparkBatch.archiveUris`



**SparRBatch**

  * `resource.sparkRBatch.mainRFileUri`
  * `resource.sparkRBatch.args`
  * `resource.sparkRBatch.fileUris`
  * `resource.sparkRBatch.archiveUris`



**SparkSqlBatch**

  * `resource.sparkSqlBatch.queryFileUri`
  * `resource.sparkSqlBatch.queryVariables`
  * `resource.sparkSqlBatch.jarFileUris`



**RuntimeConfig**

  * `resource.runtimeConfig.version`
  * `resource.runtimeConfig.containerImage`
  * `resource.runtimeConfig.properties`
  * `resource.runtimeConfig.repositoryConfig.pypiRepositoryConfig.pypiRepository`
  * `resource.runtimeConfig.autotuningConfig.scenarios`
  * `resource.runtimeConfig.cohort`



**ExecutionConfig**

  * `resource.environmentConfig.executionConfig.serviceAccount`
  * `resource.environmentConfig.executionConfig.networkUri`
  * `resource.environmentConfig.executionConfig.subnetworkUri`
  * `resource.environmentConfig.executionConfig.networkTags`
  * `resource.environmentConfig.executionConfig.kmsKey`
  * `resource.environmentConfig.executionConfig.idleTtl`
  * `resource.environmentConfig.executionConfig.ttl`
  * `resource.environmentConfig.executionConfig.stagingBucket`
  * `resource.environmentConfig.executionConfig.authenticationConfig.userWorkloadAuthenticationType`



**PeripheralsConfig**

  * `resource.environmentConfig.peripheralsConfig.metastoreService`
  * `resource.environmentConfig.peripheralsConfig.sparkHistoryServerConfig.dataprocCluster`



### Supported session constraints

The following session attributes are available to use when you create custom constraints on serverless sessions:

**General**

  * `resource.name`
  * `resource.sparkConnectSession`
  * `resource.user`
  * `resource.sessionTemplate`



**JupyterSession**

  * `resource.jupyterSession.kernel`
  * `resource.jupyterSession.displayName`



**RuntimeConfig**

  * `resource.runtimeConfig.version`
  * `resource.runtimeConfig.containerImage`
  * `resource.runtimeConfig.properties`
  * `resource.runtimeConfig.repositoryConfig.pypiRepositoryConfig.pypiRepository`
  * `resource.runtimeConfig.autotuningConfig.scenarios`
  * `resource.runtimeConfig.cohort`



**ExecutionConfig**

  * `resource.environmentConfig.executionConfig.serviceAccount`
  * `resource.environmentConfig.executionConfig.networkUri`
  * `resource.environmentConfig.executionConfig.subnetworkUri`
  * `resource.environmentConfig.executionConfig.networkTags`
  * `resource.environmentConfig.executionConfig.kmsKey`
  * `resource.environmentConfig.executionConfig.idleTtl`
  * `resource.environmentConfig.executionConfig.ttl`
  * `resource.environmentConfig.executionConfig.stagingBucket`
  * `resource.environmentConfig.executionConfig.authenticationConfig.userWorkloadAuthenticationType`



**PeripheralsConfig**

  * `resource.environmentConfig.peripheralsConfig.metastoreService`
  * `resource.environmentConfig.peripheralsConfig.sparkHistoryServerConfig.dataprocCluster`



### Supported session template constraints

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following session template attributes are available to use when you create custom constraints on serverless session templates:

**General**

  * `resource.name`
  * `resource.description`
  * `resource.sparkConnectSession`



**JupyterSession**

  * `resource.jupyterSession.kernel`
  * `resource.jupyterSession.displayName`



**RuntimeConfig**

  * `resource.runtimeConfig.version`
  * `resource.runtimeConfig.containerImage`
  * `resource.runtimeConfig.properties`
  * `resource.runtimeConfig.repositoryConfig.pypiRepositoryConfig.pypiRepository`
  * `resource.runtimeConfig.autotuningConfig.scenarios`
  * `resource.runtimeConfig.cohort`



**ExecutionConfig**

  * `resource.environmentConfig.executionConfig.serviceAccount`
  * `resource.environmentConfig.executionConfig.networkUri`
  * `resource.environmentConfig.executionConfig.subnetworkUri`
  * `resource.environmentConfig.executionConfig.networkTags`
  * `resource.environmentConfig.executionConfig.kmsKey`
  * `resource.environmentConfig.executionConfig.idleTtl`
  * `resource.environmentConfig.executionConfig.ttl`
  * `resource.environmentConfig.executionConfig.stagingBucket`
  * `resource.environmentConfig.executionConfig.authenticationConfig.userWorkloadAuthenticationType`



**PeripheralsConfig**

  * `resource.environmentConfig.peripheralsConfig.metastoreService`
  * `resource.environmentConfig.peripheralsConfig.sparkHistoryServerConfig.dataprocCluster`



## Example custom constraints for common use cases

This section includes example custom constraints for common uses cases for batch and session resources.

### Example custom constraints for a batch resource

The following table provides examples of Managed Service for Apache Spark batch custom constraints:

Description | Constraint syntax  
---|---  
Batch must attach a "category" label with allowed values. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchMustHaveSpecifiedCategoryLabel
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition: ("category" in resource.labels) && (resource.labels['category'] in ['retail', 'ads', 'service'])
        actionType: ALLOW
        displayName: Enforce batch "category" label requirement.
        description: Only allow batch creation if it attaches a "category" label with an allowable value.  
  
Batch must set an allowed runtime version. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchMustUseAllowedVersion
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition:  (has(resource.runtimeConfig.version)) && (resource.runtimeConfig.version in ["2.0.45", "2.0.48"])
        actionType: ALLOW
        displayName: Enforce batch runtime version.
        description: Only allow batch creation if it sets an allowable runtime version.  
  
Must use SparkSQL. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchMustUseSparkSQL
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition: (has(resource.sparkSqlBatch))
        actionType: ALLOW
        displayName: Enforce batch only use SparkSQL Batch.
        description: Only allow creation of SparkSQL Batch.  
  
Batch must set TTL less than 2 hours. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchMustSetLessThan2hTtl
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition:  (has(resource.environmentConfig.executionConfig.ttl)) && (resource.environmentConfig.executionConfig.ttl <= duration('2h'))
        actionType: ALLOW
        displayName: Enforce batch TTL.
        description: Only allow batch creation if it sets an allowable TTL.  
  
Batch can't set more than 20 Spark initial executors. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchInitialExecutorMax20
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition: (has(resource.runtimeConfig.properties)) && ('spark.executor.instances' in resource.runtimeConfig.properties)
         && (int(resource.runtimeConfig.properties['spark.executor.instances'])>20)
        actionType: DENY
        displayName: Enforce maximum number of batch Spark executor instances.
        description: Deny batch creation if it specifies more than 20 Spark executor instances.  
  
Batch can't set more than 20 Spark dynamic allocation initial executors. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchDynamicAllocationInitialExecutorMax20
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition: (has(resource.runtimeConfig.properties)) && ('spark.dynamicAllocation.initialExecutors' in resource.runtimeConfig.properties)
         && (int(resource.runtimeConfig.properties['spark.dynamicAllocation.initialExecutors'])>20)
        actionType: DENY
        displayName: Enforce maximum number of batch dynamic allocation initial executors.
        description: Deny batch creation if it specifies more than 20 Spark dynamic allocation initial executors.  
  
Batch must not allow more than 20 dynamic allocation executors. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchDynamicAllocationMaxExecutorMax20
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition: (resource.runtimeConfig.properties['spark.dynamicAllocation.enabled']=='false') || (('spark.dynamicAllocation.maxExecutors' in resource.runtimeConfig.properties) && (int(resource.runtimeConfig.properties['spark.dynamicAllocation.maxExecutors'])<=20))
        actionType: ALLOW
        displayName: Enforce batch maximum number of dynamic allocation executors.
        description:  Only allow batch creation if dynamic allocation is disabled or
        the maximum number of dynamic allocation executors is set to less than or equal to 20.  
  
Batch must set the KMS key to an allowed pattern. | 
    
    
        name: organizations/ORGANIZATION_ID/custom.batchKmsPattern
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition:  matches(resource.environmentConfig.executionConfig.kmsKey, '^keypattern[a-z]$')
        actionType: ALLOW
        displayName: Enforce batch KMS Key pattern.
        description: Only allow batch creation if it sets the KMS key to an allowable pattern.  
  
Batch must set the staging bucket prefix to an allowed value. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchStagingBucketPrefix
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition:  resource.environmentConfig.executionConfig.stagingBucket.startsWith(ALLOWED_PREFIX)
        actionType: ALLOW
        displayName: Enforce batch staging bucket prefix.
        description: Only allow batch creation if it sets the staging bucket prefix to ALLOWED_PREFIX.  
  
Batch executor memory setting must end with a suffix `m` and be less than 20000 m. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.batchExecutorMemoryMax
        resourceTypes:
        - dataproc.googleapis.com/Batch
        methodTypes:
        - CREATE
        condition:  ('spark.executor.memory' in resource.runtimeConfig.properties) && (resource.runtimeConfig.properties['spark.executor.memory'].endsWith('m')) && (int(resource.runtimeConfig.properties['spark.executor.memory'].split('m')[0])<20000)
        actionType: ALLOW
        displayName: Enforce batch executor maximum memory.
        description: Only allow batch creation if the executor memory setting ends with a suffix 'm' and is less than 20000 m.  
  
### Example custom constraints for a session resource

The following table provides examples of Managed Service for Apache Spark session custom constraints:

Description | Constraint syntax  
---|---  
Session must set `sessionTemplate` to empty string. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionTemplateMustBeEmpty
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition: resource.sessionTemplate == ""
        actionType: ALLOW
        displayName: Enforce empty session templates.
        description: Only allow session creation if session template is empty string.  
  
`sessionTemplate` must be equal to approved template IDs. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionTemplateIdMustBeApproved
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition:
        resource.sessionTemplate.startsWith("https://www.googleapis.com/compute/v1/projects/")
          &&
          resource.sessionTemplate.contains("/locations/") &&
          resource.sessionTemplate.contains("/sessionTemplates/") &&
           (
             resource.sessionTemplate.endsWith("/1") ||
             resource.sessionTemplate.endsWith("/2") ||
             resource.sessionTemplate.endsWith("/13")
           )
        actionType: ALLOW
        displayName: Enforce templateId must be 1, 2, or 13.
        description: Only allow session creation if session template ID is in the
        approved list, that is, 1, 2 and 13.  
  
Session must use end user credentials to authenticate the workload. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.AllowEUCSessions
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition:
        resource.environmentConfig.executionConfig.authenticationConfig.userWorkloadAuthenticationType=="END_USER_CREDENTIALS"
        actionType: ALLOW
        displayName: Require end user credential authenticated sessions.
        description: Allow session creation only if the workload is authenticated
        using end-user credentials.  
  
Session must set an allowed runtime version. | 
    
    
        name: organizations/ORGANIZATION_ID/custom.sessionMustUseAllowedVersion
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition: (has(resource.runtimeConfig.version)) &&
        (resource.runtimeConfig.version in ["2.0.45", "2.0.48"])
        actionType: ALLOW
        displayName: Enforce session runtime version.
        description: Only allow session creation if it sets an allowable runtime
        version.  
  
Session must set TTL less than 2 hours. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionMustSetLessThan2hTtl
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition: (has(resource.environmentConfig.executionConfig.ttl)) &&
        (resource.environmentConfig.executionConfig.ttl <= duration('2h'))
        actionType: ALLOW
        displayName: Enforce session TTL.
        description: Only allow session creation if it sets an allowable TTL.  
  
Session can't set more than 20 Spark initial executors. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionInitialExecutorMax20
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition: (has(resource.runtimeConfig.properties)) &&
        ('spark.executor.instances' in resource.runtimeConfig.properties) &&
        (int(resource.runtimeConfig.properties['spark.executor.instances'])>20)
        actionType: DENY
        displayName: Enforce maximum number of session Spark executor instances.
        description: Deny session creation if it specifies more than 20 Spark executor
        instances.  
  
Session can't set more than 20 Spark dynamic allocation initial executors. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionDynamicAllocationInitialExecutorMax20
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition: (has(resource.runtimeConfig.properties)) &&
        ('spark.dynamicAllocation.initialExecutors' in resource.runtimeConfig.properties)
        && (int(resource.runtimeConfig.properties['spark.dynamicAllocation.initialExecutors'])>20)
        actionType: DENY
        displayName: Enforce maximum number of session dynamic allocation initial executors.
        description: Deny session creation if it specifies more than 20 Spark dynamic
        allocation initial executors.  
  
Session must set the KMS key to an allowed pattern. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionKmsPattern
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition: matches(resource.environmentConfig.executionConfig.kmsKey, '^keypattern[a-z]$')
        actionType: ALLOW
        displayName: Enforce session KMS Key pattern.
        description: Only allow session creation if it sets the KMS key to an
        allowable pattern.  
  
Session must set the staging bucket prefix to an allowed value. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionStagingBucketPrefix
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition: resource.environmentConfig.executionConfig.stagingBucket.startsWith(ALLOWED_PREFIX)
        actionType: ALLOW
        displayName: Enforce session staging bucket prefix.
        description: Only allow session creation if it sets the staging bucket prefix
        to ALLOWED_PREFIX.  
  
Session executor memory setting must end with a suffix `m` and be less than 20000 m. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionExecutorMemoryMax
        resourceTypes:
        - dataproc.googleapis.com/Session
        methodTypes:
        - CREATE
        condition: ('spark.executor.memory' in resource.runtimeConfig.properties) &&
        (resource.runtimeConfig.properties['spark.executor.memory'].endsWith('m')) &&
        (int(resource.runtimeConfig.properties['spark.executor.memory'].split('m')[0])<20000)
        actionType: ALLOW
        displayName: Enforce session executor maximum memory.
        description: Only allow session creation if the executor memory setting ends
        with a suffix 'm' and is less than 20000 m.  
  
### Example custom constraints for a session template resource

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following table provides examples of Managed Service for Apache Spark session template custom constraints:

Description | Constraint syntax  
---|---  
Session template name must end with `org-name`. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.denySessionTemplateNameNotEndingWithOrgName
        resourceTypes:
        - dataproc.googleapis.com/SessionTemplate
        methodTypes:
        - CREATE
        - UPDATE
        condition: '!resource.name.endsWith(''org-name'')'
        actionType: DENY
        displayName: DenySessionTemplateNameNotEndingWithOrgName
        description: Deny session template creation/update if its name does not end with 'org-name'  
  
Session template must set an allowed runtime version. | 
    
    
        name: organizations/ORGANIZATION_ID/custom.sessionTemplateMustUseAllowedVersion
        resourceTypes:
        - dataproc.googleapis.com/SessionTemplate
        methodTypes:
        - CREATE
        - UPDATE
        condition: (has(resource.runtimeConfig.version)) &&
        (resource.runtimeConfig.version in ["2.0.45", "2.0.48"])
        actionType: ALLOW
        displayName: Enforce session template runtime version.
        description: Only allow session template creation or update if it sets an
        allowable runtime version.  
  
Session template must set TTL less than 2 hours. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionTemplateMustSetLessThan2hTtl
        resourceTypes:
        - dataproc.googleapis.com/SessionTemplate
        methodTypes:
        - CREATE
        - UPDATE
        condition: (has(resource.environmentConfig.executionConfig.ttl)) &&
        (resource.environmentConfig.executionConfig.ttl <= duration('2h'))
        actionType: ALLOW
        displayName: Enforce session template TTL.
        description: Only allow session template creation or update if it sets an
        allowable TTL.  
  
Session template can't set more than 20 Spark initial executors. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionTemplateInitialExecutorMax20
        resourceTypes:
        - dataproc.googleapis.com/SessionTemplate
        methodTypes:
        - CREATE
        - UPDATE
        condition: (has(resource.runtimeConfig.properties)) &&
        ('spark.executor.instances' in resource.runtimeConfig.properties) &&
        (int(resource.runtimeConfig.properties['spark.executor.instances'])>20)
        actionType: DENY
        displayName: Enforce maximum number of session Spark executor instances.
        description: Deny session template creation or update if it specifies more
        than 20 Spark executor instances.  
  
Session template can't set more than 20 Spark dynamic allocation initial executors. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionTemplateDynamicAllocationInitialExecutorMax20
        resourceTypes:
        - dataproc.googleapis.com/SessionTemplate
        methodTypes:
        - CREATE
        - UPDATE
        condition: (has(resource.runtimeConfig.properties)) &&
        ('spark.dynamicAllocation.initialExecutors' in resource.runtimeConfig.properties)
        && (int(resource.runtimeConfig.properties['spark.dynamicAllocation.initialExecutors'])>20)
        actionType: DENY
        displayName: Enforce maximum number of session dynamic allocation initial executors.
        description: Deny session template creation or update if it specifies more than 20
        Spark dynamic allocation initial executors.  
  
Session template must set the KMS key to an allowed pattern. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionTemplateKmsPattern
        resourceTypes:
        - dataproc.googleapis.com/SessionTemplate
        methodTypes:
        - CREATE
        - UPDATE
        condition: matches(resource.environmentConfig.executionConfig.kmsKey, '^keypattern[a-z]$')
        actionType: ALLOW
        displayName: Enforce session KMS Key pattern.
        description: Only allow session template creation or update if it sets the KMS key to an
        allowable pattern.  
  
Session template must set the staging bucket prefix to an allowed value. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionTemplateStagingBucketPrefix
        resourceTypes:
        - dataproc.googleapis.com/SessionTemplate
        methodTypes:
        - CREATE
        - UPDATE
        condition: resource.environmentConfig.executionConfig.stagingBucket.startsWith(ALLOWED_PREFIX)
        actionType: ALLOW
        displayName: Enforce session staging bucket prefix.
        description: Only allow session template creation or update if it sets the staging
        bucket prefix to ALLOWED_PREFIX.  
  
Session template executor memory setting must end with a suffix `m` and be less than 20000 m. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sessionTemplateExecutorMemoryMax
        resourceTypes:
        - dataproc.googleapis.com/SessionTemplate
        methodTypes:
        - CREATE
        - UPDATE
        condition: ('spark.executor.memory' in resource.runtimeConfig.properties) &&
        (resource.runtimeConfig.properties['spark.executor.memory'].endsWith('m')) &&
        (int(resource.runtimeConfig.properties['spark.executor.memory'].split('m')[0])<20000)
        actionType: ALLOW
        displayName: Enforce session executor maximum memory.
        description: Only allow session template creation or update if the executor memory setting ends
        with a suffix 'm' and is less than 20000 m.  
  
## What's next

  * For more information about organization policies, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).
  * See the full list of predefined [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
