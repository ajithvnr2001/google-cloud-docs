---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/setup-custom-constraints/
title: Create and manage custom constraints \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:10.245985+00:00
---

# Create and manage custom constraints  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/setup-custom-constraints/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Create and manage custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to enable and use custom constraints within your GKE on AWS environment. Google Cloud's [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) helps you manage resource configurations and create guardrails in your cloud environment.

## Overview

With custom organization policies, you can create granular resource policies across GKE Multi-Cloud environments to meet your organization's specific security and compliance requirements. You can also create organization policies in dry-run mode to test new policies without affecting your production workloads.

To learn more about organization policies, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#custom-organization-policies).

## Before you begin

Before you start, make sure you understand the following topics.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on an organization, Google Cloud enforces the policy on all projects in the organization. To learn more about policy inheritance and how to change evaluation rules, see [Hierarchy evaluation rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#disallow_inheritance).

### Limitations

Before you create custom constraints, keep in mind the following limitations:

  * Custom constraints can only be enforced on the `CREATE` or `UPDATE` methods for GKE on AWS resources.
  * Newly enforced custom constraints don't automatically apply to existing resources. You must update existing resources to apply the constraint. To find existing resources that need to be updated, you can enforce a [dry-run organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy).
  * To create constraints and enforce organization policies, you need the [Organization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on your Google Cloud organization. For more information about the permissions required to manage organization policies with custom constraints, see [Required roles](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#required-roles).



### Pricing

Organizational policies and custom constraints are offered at no charge.

**Note:** This guide provides a general overview. Specific gcloud commands may vary based on your exact configuration and required policy enforcement.

## Create custom constraints

Custom constraints must be specified by using the fields in the [AwsCluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.awsClusters#AwsCluster) and [AwsNodepool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.awsClusters.awsNodePools#AwsNodePool) API resource specs, excluding fields that are described as "Output only". 

### Create a custom constraint

To create a new custom constraint, you define the constraint in a YAML file and apply the custom constraint in your organization using the Google Cloud CLI. This constraint must encapsulate the specific policy you want to enforce across your GKE on AWS resources.

Create a YAML file for defining a custom constraint on your cluster:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - gkemulticloud.googleapis.com/AwsCluster
    methodTypes:
    - CREATE
    condition: CONDITION
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

To define a custom constraint on your node pool, use the following YAML configuration:
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes:
    - gkemulticloud.googleapis.com/AwsNodePool
    methodTypes:
    - CREATE
    condition: CONDITION
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION
    

Replace the following:

  * `ORGANIZATION_ID` : your organization ID, such as `123456789`.

  * `CONSTRAINT_NAME` : the name of your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers. For example, `custom.allowClusterCreateIfAnnotationPresent`. The maximum length of this field is 70 characters, not counting the prefix, for example, `organizations/123456789/customConstraints/custom`.

  * `CONDITION` : a condition that is written against a representation of a Google Cloud resource. Conditions are written in [Common Expression Language (CEL)](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). This field has a maximum length of 1,000 characters. For example, condition: `"key" in resource.annotations && resource.annotations.key == "created-by"`.

  * `ACTION` : the action to take if the condition is met. This can be either `ALLOW` or `DENY`.

  * `DISPLAY_NAME` : a display name for the constraint. This field has a maximum length of 200 characters.

  * `DESCRIPTION` : a description of the constraint to display as an error message when the policy is violated, for example, `"Allow new clusters only when certain annotations are set."` This field has a maximum length of 2,000 characters.




For more information about how to create a custom constraint, see [Defining custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#defining_custom_constraints).

### Associate the constraint with your resources

After you have created the YAML file for a new custom constraint, you must set it up to make the constraint available for organization policies.

  1. To set up a custom constraint, use the `gcloud org-policies set-custom-constraint` command:
         
         gcloud org-policies set-custom-constraint PATH_TO_FILE
         

Replace `PATH_TO_FILE` with the path of your custom constraint YAML definition.

  2. To verify that the custom constraint is created, use the `gcloud org-policies list-custom-constraints` command:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output lists the created policies:
         
         CUSTOM_CONSTRAINT: custom.allowClusterCreateIfAnnotationPresent
         ACTION_TYPE: ALLOW
         METHOD_TYPES: CREATE
         RESOURCE_TYPES: gkemulticloud.googleapis.com/AwsCluster
         DISPLAY_NAME: Allow new clusters only when certain annotations are set.
         




## Enforce the custom constraint

To enforce the new custom constraint, create an organization policy that references the constraint, and then apply the organization policy.

  1. Create a YAML file for the organization policy:
         
         name: RESOURCE_HIERARCHY/policies/POLICY_NAME
         spec:
           rules:
           - enforce: true
         

Replace the following:

     * `RESOURCE_HIERARCHY`: the location of the new policy, which affects the scope of enforcement. Use the Google Cloud resource hierarchy as a guide. For example, if you want to enforce the policy in a specific project, use `projects/``PROJECT_ID`. To enforce the policy in a specific organization, use `organizations/``ORGANIZATION_ID`.

     * `POLICY_NAME`: the name of the new policy.

  2. Enforce the policy:
         
         gcloud org-policies set-policy PATH_TO_POLICY
         

Replace `PATH_TO_POLICY` with the path to your policy definition file.

  3. Verify that the policy exists:
         
         gcloud org-policies list --RESOURCE_FLAG=RESOURCE_ID
         

Replace the following:

     * `RESOURCE_FLAG`: the Google Cloud resource where you enforced the policy. For example, a project or organization.

     * `RESOURCE_ID`: the ID of the resource where you enforced the policy. For example, your project ID or organization ID.

The output is similar to the following:
    
    CONSTRAINT: custom.allowClusterCreateIfAnnotationPresent
    LIST_POLICY: -
    BOOLEAN_POLICY: SET
    ETAG: CPjb27wGEOijhL4B-
    




## Test the policy

Test the organization policy by creating a new AWS cluster in a restricted project. 

  1. Create an AWS cluster in a restricted project.
         
         gcloud container aws clusters create CLUSTER_NAME \
           --aws-region AWS_REGION \
           --location GOOGLE_CLOUD_LOCATION \
           --cluster-version CLUSTER_VERSION \
           --fleet-project FLEET_PROJECT \
           --vpc-id VPC_ID \
           --subnet-ids CONTROL_PLANE_SUBNET_1,CONTROL_PLANE_SUBNET_2,CONTROL_PLANE_SUBNET_3 \
           --pod-address-cidr-blocks POD_ADDRESS_CIDR_BLOCKS \
           --service-address-cidr-blocks SERVICE_ADDRESS_CIDR_BLOCKS \
           --role-arn API_ROLE_ARN \
           --database-encryption-kms-key-arn DB_KMS_KEY_ARN \
           --admin-users ADMIN_USERS_LIST \
           --config-encryption-kms-key-arn CONFIG_KMS_KEY_ARN \
           --iam-instance-profile CONTROL_PLANE_PROFILE \
           --tags "Name=CLUSTER_NAME-cp"
         

  2. The output is similar to the following:
         
         FAILED_PRECONDITION: Operation denied by org policy on resource 'projects/PROJECT_NUMBER/locations/GOOGLE_CLOUD_REGION': ["customConstraints/custom.allowClusterCreateIfAnnotationPresent": "Allow new clusters only when certain annotations are set."]
         
         '@type': type.googleapis.com/google.rpc.ErrorInfo
         domain: googleapis.com
         metadata:
           customConstraints: customConstraints/custom.allowClusterCreateIfAnnotationPresent
         service: gkemulticloud.googleapis.com
         reason: CUSTOM_ORG_POLICY_VIOLATION
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
