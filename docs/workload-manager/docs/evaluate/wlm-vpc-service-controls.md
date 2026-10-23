---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/wlm-vpc-service-controls/
title: Configure Workload Manager to use with VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:17.961979+00:00
---

# Configure Workload Manager to use with VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/wlm-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Configure Workload Manager to use with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure ingress and egress rules to run Workload Manager evaluations in projects that are protected with VPC Service Controls. 

When you run Workload Manager evaluations in projects that are protected by VPC Service Controls, you must configure ingress and egress rules to the service account attached to the Compute Engine instance that runs your Agent for Compute Workloads. These rules let the service account access the required APIs within the VPC Service Controls perimeter. If you don't configure these rules, the agent cannot send data to Workload Manager, and your evaluations fail.

For more information, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

Before setting up VPC Service Controls for your project, do the following:

  1. [Set up a VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).
  2. Identify the service account attached to the Compute Engine instance that runs your Agent for Compute Workloads. For example, `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`. You can find this on the **VM instance details** page in the Google Cloud console.
  3. Verify that the service account has the required roles. For example, see [Required roles for the agent and SAP workloads](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sap#grant-iam-roles).



### Required roles

To get the permissions that you need to configure Workload Manager for use within VPC Service Controls perimeters, ask your administrator to grant you the [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create ingress and egress rules for a service perimeter

To let the Agent for Compute Workloads communicate with required services, you must configure ingress and egress rules in your VPC Service Controls perimeter.

**Note:** Egress rules are required only if the _target project_ (where your workload runs) is different from the _consumer project_ (where you run evaluations). For more information about these project types, see [Workload Manager projects](https://docs.cloud.google.com/workload-manager/docs/evaluate/roles#wlm-projects). If your setup involves cross-project communication, you must configure egress rules to allow the required traffic.

For more information about how to create ingress rules, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

###  Console 

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to the VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. Select your project.

  3. Click the name of the service perimeter, and then click **Edit**.

  4. Click **Ingress policy** or **Egress policy**.

  5. Click **Add an ingress rule**.

  6. In the **From** section, specify the identity for the service agent:

     1. For **Identities** , select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address of the agent service account. For example, `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.
  7. In the **To** section, specify the allowed operations:

     1. For **Resources** , select **All projects**.
     2. For **Operations** , select **Select operations**.
     3. Click **Add operations** , and then add the following services with **All methods** selected: 
        * `compute.googleapis.com`
        * `workloadmanager.googleapis.com`
        * `secretmanager.googleapis.com`
  8. Click **Done** , and then click **Save**.




###  gcloud 

To add the ingress rule, create a YAML file that contains the ingress rule and use the [`gcloud access-context-manager perimeters update`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update) command with the `--set-ingress-policies` flag.

  1. Create an ingress policy YAML file named `ingress_policy.yaml` with the following contents:
         
         - ingressFrom:
             identities:
              - serviceAccount:SERVICE_ACCOUNT_EMAIL
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: workloadmanager.googleapis.com
               methodSelectors:
               - method: "*"
             - serviceName: secretmanager.googleapis.com
               methodSelectors:
               - method: "*"
             resources:
             - "*"
         

Replace `SERVICE_ACCOUNT_EMAIL` with the email address of the service account attached to the Compute Engine instance that runs the Agent for Compute Workloads.

  2. Add the ingress policy to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
              --set-ingress-policies=ingress_policy.yaml
         

Replace `PERIMETER_NAME` with the name of your service perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`.




## Troubleshoot VPC Service Controls violations

To view VPC Service Controls violations in your project and troubleshoot issues, use Logs Explorer.

For more information, see [Troubleshooting VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter).

## What's next

  * [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
