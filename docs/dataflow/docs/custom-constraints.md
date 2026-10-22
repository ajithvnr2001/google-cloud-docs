---
url: https://docs.cloud.google.com/dataflow/docs/custom-constraints/
title: Manage Dataflow resources using custom constraints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:19.258369+00:00
---

# Manage Dataflow resources using custom constraints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Manage Dataflow resources using custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

Custom constraints for Dataflow let you enforce granular governance over pipeline resources across your organization. As an [organization policy administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin), you can define policies that restrict specific resource fields throughout your [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce these policies at the organization, folder, or project level.

Organization Policy Service provides [predefined constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) for various Google Cloud services. When you need more customizable control over specific Dataflow fields, you can create custom organization policies to enforce your compliance and security requirements.

## Benefits

You can use a custom organization policy to allow or deny creation of Dataflow jobs with conditions based on supported resource attributes, such as job name, type, and service options.

## Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, see [Hierarchy evaluation rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#disallow_inheritance).

## Pricing

The Organization Policy Service, including predefined and custom organization policies, is offered at no charge.

## Limitations

  * Custom constraints for Dataflow `Job` resources can only be set up by using the Google Cloud console or Google Cloud CLI.

  * Custom constraints can only be enforced on the `CREATE` method for Dataflow `Job` resources.

  * Newly enforced custom constraints don't apply to existing resources.




## Before you begin

For more information about what organization policies and constraints are and how they work, see the [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

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

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language).

To create a YAML file for a custom constraint:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - dataflow.googleapis.com/RESOURCE_NAME
    methodTypes:
    - CREATE
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID, such as `123456789`.

  * `CONSTRAINT_NAME`: the name you want for your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers—for example, custom.denyPrimeJobs. The maximum length of this field is 70 characters, not counting the prefix—for example, `organizations/123456789/customConstraints/custom`.

  * `RESOURCE_NAME`: the name (not the URI) of the Dataflow API REST resource containing the object and field you want to restrict. For example, dataflow.googleapis.com/Job.

  * `CONDITION`: a [CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field has a maximum length of 1000 characters. See Supported resources for more information about the resources available to write conditions against. For example, "resource.environment.serviceOptions.exists(value, value=='enable_prime')".

  * `ACTION`: the action to take if the `condition` is met. Supported values are `ALLOW` and `DENY`.

  * `DISPLAY_NAME`: a human-friendly name for the constraint. This field has a maximum length of 200 characters.

  * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2000 characters.




For more information about how to create a custom constraint, see [Defining custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#defining_custom_constraints).

## Set up a custom constraint

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.denyPrimeJobs`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
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
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.denyPrimeJobs`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `dataflow.googleapis.com/Job`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.environment.serviceOptions.exists(value, value=='enable_prime')"`. 

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.denyPrimeJobs`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Example: Create a constraint to deny creation of a job with prime enabled

### gcloud

  1. Create a `denyPrimeJobs.yaml` constraint file with the following information. Replace `ORGANIZATION_ID` with your organization ID.
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.denyPrimeJobs
         resource_types: dataflow.googleapis.com/Job
         condition: "resource.environment.serviceOptions.exists(value, value=='enable_prime')"
         action_type: DENY
         method_types: CREATE
         display_name: Restrict creation of job with prime enabled
         description: Deny creation of jobs with prime enabled.

  2. Set the custom constraint.
         
         gcloud org-policies set-custom-constraint denyPrimeJobs.yaml
         

  3. Create an `enforce-policy-denyPrimeJobs.yaml` policy file with the following information. In this example, the constraint is enforced at the project level. You might also set this constraint at the organization or folder level. Replace `PROJECT_ID` with your project ID.
         
         name: projects/PROJECT_ID/policies/custom.denyPrimeJobs
               spec:
                 rules:
                 – enforce: true

  4. [Enforce the policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#enforcing_custom_constraints) by running the following command: 
         
         gcloud org-policies set-policy enforce-policy-denyPrimeJobs.yaml
         

  5. To test the constraint, try to create a Dataflow job with the `enable_prime` option. Follow the [Create a Dataflow pipeline using Java](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-java) quickstart to create a WordCount job.
         
         mvn -Pdataflow-runner compile \
         exec:java \
         -Dexec.mainClass=org.apache.beam.examples.WordCount \
         -Dexec.args="--project=PROJECT_ID \
         --gcpTempLocation=gs://BUCKET_NAME/temp/ \
         --output=gs://BUCKET_NAME/output \
         --runner=DataflowRunner \
         --region=us-central1 \
         --dataflowServiceOptions=enable_prime" \
         -Pdataflow-runner
         

The output is similar to the following example:
         
         "details" : [ {
           "@type" : "type.googleapis.com/google.rpc.ErrorInfo",
           "reason" : "CUSTOM_ORG_POLICY_VIOLATION"
         }]

The audit log should show violation details like the following: 
         
         policyViolationInfo: {
             orgPolicyViolationInfo: {
             violationInfo: [
             0: {
               constraint: "customConstraints/custom.denyPrimeJobs"
               errorMessage: "Restrict creation of job with prime enabled"
               policyType: "CUSTOM_CONSTRAINT"
             }]}}




## Expression fields for conditions

The following table contains the expression fields that you can use to create conditions. Conditions are written in [Common Expression Language (CEL)](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). The value of the expression fields is case-sensitive.

For descriptions of the following expression fields and which values you can specify, see the [Dataflow `Job` JSON representation](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job). 

**Expression field** | **Value type**  
---|---  
`name` | `string`  
`type` | `string`  
`transformNameMapping` | `map`  
`location` | `string`  
`environment` | `message`  
`environment.serviceOptions` | `list of string`  
`environment.serviceKmsKeyName` | `string`  
`environment.serviceAccountEmail` | `string`  
`environment.workerRegion` | `string`  
`environment.workerZone` | `string`  
`environment.streamingMode` | `string`  
`environment.debugOptions` | `message`  
`environment.debugOptions.enableHotKeyLogging` | `bool`  
  
## Example use cases

Some example use cases are listed in the following table. 

**Use Case** | **Action** | **Custom Constraint**  
---|---|---  
Disallow use of prime job | DENY | `resource.environment.serviceOptions.exists(value, value=='enable_prime')`  
Prevents VMs from accepting SSH keys that are stored in project metadata. | DENY | `!resource.environment.serviceOptions.exists(value, value=='block_project_ssh_keys')`  
Disallow jobs without setting the maximum number of seconds the job can run | DENY | `!resource.environment.serviceOptions.exists(value, value.contains('max_workflow_runtime_walltime_seconds=')`  
  
## What's next

  * See [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to learn more about organization policies.
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).
  * See the full list of predefined [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
