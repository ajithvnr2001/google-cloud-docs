---
url: https://docs.cloud.google.com/deploy/docs/securing/iam/
title: Use IAM to restrict Cloud Deploy access \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:06.433046+00:00
---

# Use IAM to restrict Cloud Deploy access  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/securing/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Use IAM to restrict Cloud Deploy access Stay organized with collections  Save and categorize content based on your preferences. 

As with all Google Cloud products, Identity and Access Management protects Cloud Deploy by controlling which authenticated users and service accounts can perform which actions.

This document describes some of the features of IAM, and provides instructions for protecting your application deliveries that are managed using Cloud Deploy. Here are some of the specific ways you can restrict access to actions and resources in Cloud Deploy:

  * Grant access to a specific delivery pipeline

  * Grant access to configure a specific target

  * Grant permissions to promote a release to a specific target

  * Grant permissions to approve rollouts to a specific target

  * Grant permissions to promote a release during a specific time window

  * Grant permissions to approve rollouts during a specific time window




## Before you begin

  * Understand the [basic concepts of IAM](https://docs.cloud.google.com/iam/docs/overview).

  * Learn about [Cloud Deploy roles and permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions).




## About IAM advanced features

Besides [roles and permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access), Cloud Deploy uses the following features of IAM to provide those controls:

### About IAM policies

An IAM policy is a collection of bindings and metadata. The role binding grants a single role to one or more principals (users, groups, or service accounts), plus any context-specific conditions that control whether the binding takes effect.

For more information about IAM policies, see [Understanding policies](https://docs.cloud.google.com/iam/docs/policies).

### About IAM conditions

With [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview), you can control. access to Cloud Deploy resources and actions based on conditions computed at runtime. For example, you can restrict promotion to a given target such that it's only allowed during a specified time window.

### About API attributes

When you construct IAM conditions, you can reference [API attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#api) to get runtime information about a request. For example, you can use an API attribute to get the name of the resource that the request is for. Then you can compare it to the resource or resources the principal has access to.

## Grant fine-grained access using advanced IAM features

These advanced IAM features allow you to control access to specific resources and to resource types under specific conditions.

The procedures in this section grant access to specific resources (targets, delivery pipelines). You can also grant access at the project level, which affects all delivery pipelines or all targets in that project. To set an IAM policy for a project, use the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command:
    
    
    gcloud projects set-iam-policy PROJECT_ID POLICY_FILE
    

### Grant access to a specific delivery pipeline

You can grant permissions for a principal to create, modify, and delete all delivery pipelines, by just granting an appropriate [role](https://docs.cloud.google.com/deploy/docs/iam-roles/permissions#predefined_roles). But sometimes you might want to grant a principal this access for one or more _specific_ pipelines.

To do so, use [role bindings](https://docs.cloud.google.com/iam/docs/policies#structure) to bind the `roles/clouddeploy.developer` role with that principal, then when you apply the policy (with `setIamPolicy`) you specify which delivery pipeline the access is granted for.

**Note:** You can grant access to pipelines using the `roles/clouddeploy.operator` role also. Or you can do it by directly adding the applicable [permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#permissions) (`clouddeploy.deliveryPipelines.*`).

To grant access to a specific delivery pipeline:

  1. [Create a policy file](https://docs.cloud.google.com/iam/docs/policies#structure) with the following binding:
         
         bindings:
         - role: roles/clouddeploy.developer
           members:
           - user:fatima@example.com
         

The above example grants the role to a user, but you can also grant the role to a group or to a service account.

  2. Call the following command to apply the policy file to a specific delivery pipeline:
         
         gcloud deploy delivery-pipelines set-iam-policy --delivery-pipeline=PIPELINE_NAME --region=REGION POLICY_FILE
         




### Grant access to configure a specific target

To grant a principal access to a specific target, you can use [role bindings](https://docs.cloud.google.com/iam/docs/policies#structure). To do so, bind the `roles/clouddeploy.operator` role with that principal, then when you apply the policy (with `setIamPolicy`) you specify which target the access is granted for.

Access to the specific target gives the principal the ability to update and to delete that target.

  1. [Create a policy file](https://docs.cloud.google.com/iam/docs/policies#structure) with the following binding:
         
         bindings:
         - role: roles/clouddeploy.operator
           members:
           - group:cd_operators@example.com
         

The above example grants the role to a group, but you can also grant the role to a user or to a service account.

  2. Call the following command to apply the policy file to a specific target:
         
         gcloud deploy targets set-iam-policy TARGET --region=REGION POLICY_FILE
         




### Grant permissions to promote a release to a specific target

This procedure assumes there is already a policy in place that binds the role to the principal. Here, we add a condition that specifies the target:

  1. Create a policy file with the following binding:
         
         bindings:
         - role: roles/clouddeploy.operator
           members:
           - serviceAccount:prod_operator@project-12345.iam.gserviceaccount.com
           condition:
             expression: api.getAttribute("clouddeploy.googleapis.com/rolloutTarget", "") == "prod"
             title: Deploy to prod
         

In this role binding, `condition` takes a key:value pair, where the key is `expression` and the value is a [CEL expression](https://opensource.google/projects/cel). This expression references a set of contextual [attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference) about the request and evaluates to a boolean.

In this case, the expression is evaluated, when the principal tries to promote the release, to confirm that the promotion target matches the target in the expression.

The expression uses the API attribute `clouddeploy.googleapis.com/rolloutTarget`, which is the target the principal is trying to promote to. The expression compares it to the target for which the principal is being given promotion access.

  2. Set the binding for a specific delivery pipeline:
         
         gcloud deploy delivery-pipelines set-iam-policy PIPELINE_NAME --region=REGION POLICY_FILE
         

If you want to set this binding for all delivery pipelines, you can set it at the project level:
         
         gcloud projects set-iam-policy PROJECT POLICY_FILE
         




### Grant permissions to approve rollouts to a specific target

The binding in this section grants a principal permission to approve rollouts for a pipeline, and includes a condition that applies the permission for the `prod` target.

  1. Create a policy file with the following binding:
         
         bindings:
         - role: roles/clouddeploy.approver
           members:
           - serviceAccount:prod_operator@project-12345.iam.gserviceaccount.com
           condition:
             expression: api.getAttribute("clouddeploy.googleapis.com/rolloutTarget", "") == "prod"
             title: Deploy to prod
         

In this role binding, `condition` takes a key:value pair, where the key is `expression` and the value is a [CEL expression](https://opensource.google/projects/cel). The expression references a set of contextual [attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference) about the request and evaluates to a boolean.

In this case, the expression is evaluated, when the principal tries to approve the rollout, to confirm that the target matches the target in the expression.

The expression uses the API attribute `clouddeploy.googleapis.com/rolloutTarget`, which is the target of the rollout, and compares it to the target for which the principal is being given approval access. The `clouddeploy.googleapis.com/rolloutTarget` attribute is the only API attribute Cloud Deploy supports.

  2. Set the binding for a specific delivery pipeline:
         
         gcloud deploy delivery-pipelines set-iam-policy PIPELINE_NAME --region=REGION POLICY_FILE
         

If you want to set this binding for all delivery pipelines, you can set it at the project level:
         
         gcloud projects set-iam-policy PROJECT POLICY_FILE
         




### Grant permissions to promote a release during a specific time window

The binding in this section grants a principal permission to promote releases for a pipeline, and includes a condition that that [specifies the time window](https://cloud.google.com/iam/docs/conditions-attribute-reference#date-time) during which the binding is in effect.

**Note:** If the principal otherwise has access to promote a release (for example, via membership in a group), this binding does not revoke that access outside of the time window.

  1. Create a policy file with the following binding:
         
         bindings:
         - role: roles/clouddeploy.operator
           members:
           - serviceAccount:prod_operator@project-12345.iam.gserviceaccount.com
           condition:
             expression: request.time.getDayOfWeek("America/Los_Angeles") > 0 && request.time.getDayOfWeek("America/Los_Angeles") < 6
             title: Promote during safe window
         

In this role binding, `condition` takes a key:value pair, where the key is `expression` and the value is a [CEL expression](https://opensource.google/projects/cel). The expression references a set of contextual [attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference) about the request and evaluates to a boolean. This expression checks that the request time occurs Monday through Friday.

In this case, the expression is evaluated, when the principal tries to promote the release, to confirm that the promotion target matches the target in the expression.

  2. Set the binding for a specific delivery pipeline:
         
         gcloud deploy delivery-pipelines set-iam-policy PIPELINE_NAME --region=REGION POLICY_FILE
         

If you want to set this binding for all delivery pipelines, you can set it at the project level:
         
         gcloud projects set-iam-policy PROJECT POLICY_FILE
         




### Grant permissions to approve rollouts during a specific time window

The binding in this section grants a principal permission to approve rollouts, and includes a condition that [specifies the time window](https://cloud.google.com/iam/docs/conditions-attribute-reference#date-time) during which the binding is in effect

**Note:** If the principal otherwise has access to approve rollouts (for example, via membership in a group), this binding does not revoke that access outside of the time window.

  1. Create a policy file with the following binding:
         
         bindings:
         - role: roles/clouddeploy.approver
           members:
           - serviceAccount:prod_operator@project-12345.iam.gserviceaccount.com
           condition:
             expression: request.time.getDayOfWeek("America/Los_Angeles") > 0 && request.time.getDayOfWeek("America/Los_Angeles") < 6
             title: Approve during safe window
         

In this role binding, `condition` takes a key:value pair, where the key is `expression` and the value is a [CEL expression](https://opensource.google/projects/cel) that references a set of contextual [attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference) about the request and evaluates to a boolean. This expression checks that the request time occurs Monday through Friday.

In this case, the expression is evaluated, when the principal tries to approve the rollout, to confirm that the rollout target matches the target in the expression.

  2. Set the binding for a specific delivery pipeline:
         
         gcloud deploy delivery-pipelines set-iam-policy PIPELINE_NAME --region=REGION POLICY_FILE
         

If you want to set this binding for all delivery pipelines, you can set it at the project level:
         
         gcloud projects set-iam-policy PROJECT POLICY_FILE
         




### Grant permissions to retry a job, based on job type

The binding in this section grants a principal permission to retry a Cloud Deploy job, based on the type of job

  1. Create a policy file with the following binding:
         
         bindings:
         - role: roles/clouddeploy.operator
           members:
           - serviceAccount:prod_operator@project-12345.iam.gserviceaccount.com
           condition:
             expression: api.getAttribute("clouddeploy.googleapis.com/jobType", "") == "deploy"
             title: Retry deploy job
         

In this role binding, `condition` takes a key:value pair, where the key is `expression` and the value is a [CEL expression](https://opensource.google/projects/cel). The expression references a set of contextual [attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference) about the request and evaluates to a boolean.

In this case, the expression is evaluated, when the principal tries to retry the job, to confirm that the job types matches the job type in the expression.

The expression uses the API attribute `clouddeploy.googleapis.com/jobType`, which can be either `deploy` or `verify`.

  2. Set the binding for a specific delivery pipeline:
         
         gcloud deploy delivery-pipelines set-iam-policy PIPELINE_NAME --region=REGION POLICY_FILE
         

If you want to set this binding for all delivery pipelines, you can set it at the project level:
         
         gcloud projects set-iam-policy PROJECT POLICY_FILE
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
