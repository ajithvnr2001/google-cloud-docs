---
url: https://docs.cloud.google.com/monitoring/docs/custom-constraints/
title: Use custom organization policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:56.926636+00:00
---

# Use custom organization policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Use custom organization policies Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `monitoring.googleapis.com/AlertPolicy`
  * `monitoring.googleapis.com/NotificationChannel`
  * `monitoring.googleapis.com/Snooze`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#custom-organization-policies).

In Cloud Monitoring, custom constraints let you enforce organization-wide governance rules on alerting configurations. For example, you can require alerting policies to include documentation or backup notification channels, restrict notification channels to approved types such as email, or limit the maximum duration of a snooze. 

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#disallow_inheritance).

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

## Cloud Monitoring supported resources

The following table lists the Cloud Monitoring resources that you can reference in custom constraints. 

Resource | Field  
---|---  
monitoring.googleapis.com/AlertPolicy |  `resource.alertStrategy.autoClose`  
`resource.alertStrategy.notificationChannelStrategy.notificationChannelNames`  
`resource.alertStrategy.notificationChannelStrategy.renotifyInterval`  
`resource.alertStrategy.notificationRateLimit.period`  
`resource.combiner`  
`resource.conditions.conditionAbsent.aggregations.alignmentPeriod`  
`resource.conditions.conditionAbsent.aggregations.crossSeriesReducer`  
`resource.conditions.conditionAbsent.aggregations.groupByFields`  
`resource.conditions.conditionAbsent.aggregations.perSeriesAligner`  
`resource.conditions.conditionAbsent.duration`  
`resource.conditions.conditionAbsent.filter`  
`resource.conditions.conditionAbsent.trigger.count`  
`resource.conditions.conditionAbsent.trigger.percent`  
`resource.conditions.conditionMatchedLog.filter`  
`resource.conditions.conditionMatchedLog.labelExtractors`  
`resource.conditions.conditionMonitoringQueryLanguage.duration`  
`resource.conditions.conditionMonitoringQueryLanguage.evaluationMissingData`  
`resource.conditions.conditionMonitoringQueryLanguage.query`  
`resource.conditions.conditionMonitoringQueryLanguage.trigger.count`  
`resource.conditions.conditionMonitoringQueryLanguage.trigger.percent`  
`resource.conditions.conditionPrometheusQueryLanguage.alertRule`  
`resource.conditions.conditionPrometheusQueryLanguage.duration`  
`resource.conditions.conditionPrometheusQueryLanguage.evaluationInterval`  
`resource.conditions.conditionPrometheusQueryLanguage.labels`  
`resource.conditions.conditionPrometheusQueryLanguage.query`  
`resource.conditions.conditionPrometheusQueryLanguage.ruleGroup`  
`resource.conditions.conditionSql.booleanTest.column`  
`resource.conditions.conditionSql.daily.periodicity`  
`resource.conditions.conditionSql.hourly.minuteOffset`  
`resource.conditions.conditionSql.hourly.periodicity`  
`resource.conditions.conditionSql.minutes.periodicity`  
`resource.conditions.conditionSql.query`  
`resource.conditions.conditionSql.rowCountTest.comparison`  
`resource.conditions.conditionSql.rowCountTest.threshold`  
`resource.conditions.conditionThreshold.aggregations.alignmentPeriod`  
`resource.conditions.conditionThreshold.aggregations.crossSeriesReducer`  
`resource.conditions.conditionThreshold.aggregations.groupByFields`  
`resource.conditions.conditionThreshold.aggregations.perSeriesAligner`  
`resource.conditions.conditionThreshold.comparison`  
`resource.conditions.conditionThreshold.denominatorAggregations.alignmentPeriod`  
`resource.conditions.conditionThreshold.denominatorAggregations.crossSeriesReducer`  
`resource.conditions.conditionThreshold.denominatorAggregations.groupByFields`  
`resource.conditions.conditionThreshold.denominatorAggregations.perSeriesAligner`  
`resource.conditions.conditionThreshold.denominatorFilter`  
`resource.conditions.conditionThreshold.duration`  
`resource.conditions.conditionThreshold.evaluationMissingData`  
`resource.conditions.conditionThreshold.filter`  
`resource.conditions.conditionThreshold.forecastOptions.forecastHorizon`  
`resource.conditions.conditionThreshold.thresholdValue`  
`resource.conditions.conditionThreshold.trigger.count`  
`resource.conditions.conditionThreshold.trigger.percent`  
`resource.conditions.displayName`  
`resource.conditions.name`  
`resource.displayName`  
`resource.documentation.content`  
`resource.documentation.links.displayName`  
`resource.documentation.links.url`  
`resource.documentation.mimeType`  
`resource.documentation.subject`  
`resource.enabled`  
`resource.name`  
`resource.notificationChannels`  
`resource.severity`  
monitoring.googleapis.com/NotificationChannel |  `resource.description`  
`resource.displayName`  
`resource.enabled`  
`resource.type`  
monitoring.googleapis.com/Snooze |  `resource.criteria.policies`  
`resource.displayName`  
`resource.interval.endTime`  
`resource.interval.startTime`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `alertDocHasProject`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
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
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `alertDocHasProject`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `monitoring.googleapis.com/AlertPolicy`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `resource.documentation.content.contains('${resource.project}')`. 

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
  9. To finish and apply the organization policy, click **Set policy**. The policy requires up to 15 minutes to take effect. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name of the constraint that you want to enforce. For example, `alertDocHasProject`. 
  2. To enforce the organization policy containing the constraint, run the following command: 
    
    gcloud org-policies set-policy POLICY_PATH

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint and policy that checks whether the [documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables) of an alerting policy mentions the project name.

Before you begin, replace the following:

  * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  * PROJECT_ID: The identifier of the project.



### Create the constraint

  1. Save the following file as `constraint-alert-doc-has-project.yaml`:
         
         actionType: DENY
         condition: resource.documentation.content.contains('${resource.project}')
         description: Requires documentation to include the project name.
         displayName: Alerting policy documentation must include the project name.
         methodTypes:
           - CREATE
           - UPDATE
         name: organizations/ORGANIZATION_ID/customConstraints/custom.alertDocHasProject
         resourceTypes:
           - monitoring.googleapis.com/AlertPolicy
         

Replace ORGANIZATION_ID with your organization ID.

This constraint prevents an alerting policy from being created or updated if the name of the resource project is missing from the alerting policy documentation.

  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint ~/constraint-alert-doc-has-project.yaml
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output is similar to the following:
         
         CUSTOM_CONSTRAINT: custom.alertDocHasProject
         ACTION_TYPE: DENY
         METHOD_TYPES: CREATE,UPDATE
         RESOURCE_TYPES: monitoring.googleapis.com/AlertPolicy
         DISPLAY_NAME: Alerting policy documentation must include the project name.
         




### Create the policy

  1. Save the following file as `policy-alert-doc-has-project.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.alertDocHasProject
         spec:
           rules:
           - enforce: true
         

Replace PROJECT_ID with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy ~/policy-alert-doc-has-project.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT: custom.alertDocHasProject
         LIST_POLICY: -
         BOOLEAN_POLICY: SET
         ETAG: CKSx5LwGEPjBuKwD-
         




After you apply the policy, wait for about two minutes for Google Cloud to start enforcing the policy.

### Test the policy

Try to create an alerting policy with documentation that excludes the resource project name.
    
    
    gcloud monitoring policies create \
      --display-name="CPU Utilization - 5% Threshold" \
      --project=PROJECT_ID \
      --condition-display-name="Condition 1" \
      --condition-filter='resource.type="gce_instance" AND metric.type="compute.googleapis.com/instance/cpu/utilization"' \
      --duration='60s' \
      --if='>5' \
      --combiner='AND' \
      --documentation='The ${metric.display_name} of the ${resource.type} ${resource.label.instance_id} has exceeded 5% for over 60 seconds.'
    

Replace PROJECT_ID with your project ID.

The output is the following:
    
    
    Operation denied by custom org policies: ["customConstraints/alertDocHasProject": "Alerting policy documentation must include the project name."]
    

## Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints.

Description | Constraint syntax  
---|---  
Alerting policies must have only one condition | 
    
    
        actionType: DENY
        condition: "resource.conditions.size() > 1"
        description: Requires alerting policies to have only one condition.
        displayName: Alerting policies must have only one condition
        methodTypes:
          - CREATE
          - UPDATE
        name: organizations/ORGANIZATION_ID/customConstraints/custom.oneCondition
        resourceTypes:
          - monitoring.googleapis.com/AlertPolicy
          
  
Alerting policies must use at least two notification channels | 
    
    
        actionType: DENY
        condition: "resource.notificationChannels.size() < 2"
        description: Alerting policies must use at least two notification channels.
        displayName: Policies must have a backup notification channel
        methodTypes:
          - CREATE
          - UPDATE
        name: organizations/ORGANIZATION_ID/customConstraints/custom.alertOnTwoChannels
        resourceTypes:
          - monitoring.googleapis.com/AlertPolicy
          
  
Only allow email notification channels | 
    
    
        actionType: DENY
        condition: "resource.type != 'email'"
        description: Requires notification channels to use only the email channel
        type.
        displayName: Always use email for notification channels
        methodTypes:
          - CREATE
          - UPDATE
        name: organizations/ORGANIZATION_ID/customConstraints/custom.emailChannelsOnly
        resourceTypes:
          - monitoring.googleapis.com/NotificationChannel
          
  
Snoozes must be less than one hour | 
    
    
        actionType: DENY
        condition: "int(resource.interval.endTime) > int(resource.interval.startTime) + 3600"
        description: Requires snoozes to be under 1 hour.
        displayName: Snoozes must be less than 1 hour
        methodTypes:
        - CREATE
        - UPDATE
        name: organizations/ORGANIZATION_ID/customConstraints/custom.setMaxSnooze
        resourceTypes:
        - monitoring.googleapis.com/Snooze
          
  
## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
