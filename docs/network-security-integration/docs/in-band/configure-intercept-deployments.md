---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployments/
title: Create and manage intercept deployments \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:22.246400+00:00
---

# Create and manage intercept deployments  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage intercept deployments Stay organized with collections  Save and categorize content based on your preferences. 

An [intercept deployment](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployments-overview) is a zonal resource that references the forwarding rule of an internal passthrough Network Load Balancer whose backends are packet inspection VMs. An intercept deployment represents the producer's inspection service offering for a zone.

This page describes how to create and manage intercept deployments.

## Before you begin

  * [Enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).
  * Create an [intercept deployment group](https://docs.cloud.google.com/network-security-integration/docs/configure-deployment-groups).
  * Make sure you have a forwarding rule that directs network traffic to the internal passthrough Network Load Balancer whose backends provide packet inspection. For more information, see [Set up producer services](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-producer-service).



### Roles

To create, view, or delete intercept deployments, your Identity and Access Management (IAM) principal must have the necessary [IAM roles](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployments-overview#iam-roles) on your project. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, your IAM principal must have the following [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`roles/networksecurity.interceptDeploymentAdmin`) permissions:

  * `networksecurity.interceptDeployments.create`
  * `networksecurity.interceptDeployments.delete`
  * `networksecurity.interceptDeployments.get`
  * `networksecurity.interceptDeployments.list`



## Create an intercept deployment

Create an intercept deployment to represent the producer's compute resources within a zone and associate it with an existing intercept deployment group.

You can create the intercept deployments in the same project that contains the parent intercept deployment group. We recommend that you create the intercept deployment in a project owned by your security administrator.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.interceptDeployments.create`



**Roles**

  * [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`networksecurity.interceptDeploymentAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the deployment group where you want to add the intercept deployment.

  3. Click **Create intercept deployment**.

  4. For **Name** , enter a name of the intercept deployment.

  5. For **Region** and **Zone** , select your region and zone.

  6. For **Internal load balancer** , select the internal passthrough Network Load Balancer.

  7. For **Forwarding rule** , select the UDP forwarding rule of the load balancer. If the load balancer has only one forwarding rule, it is selected by default and the field is disabled.

**Note:** The forwarding rule's VPC network must match the intercept deployment group's network.
  8. Click **Create**.




###  gcloud 

To create an intercept deployment, use the [`gcloud network-security intercept-deployments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/create):
    
    
    gcloud network-security intercept-deployments create DEPLOYMENT_ID \
        --location ZONE \
        --forwarding-rule FWD_RULE \
        --forwarding-rule-location REGION \
        --no-async \
        --intercept-deployment-group \
            projects/PROJECT_ID/locations/global/interceptDeploymentGroups/DEPLOYMENT_GROUP_ID
    

Replace the following:

  * `DEPLOYMENT_ID`: the ID of the intercept deployment.
  * `ZONE`: the zone where you want to create the intercept deployment.
  * `FWD_RULE`: the forwarding rule of an internal passthrough Network Load Balancer in the same region as the zone of the intercept deployment.
  * `REGION`: the region that contains the zone of the intercept deployment.
  * `PROJECT_ID`: the ID of the Google Cloud project.
  * `DEPLOYMENT_GROUP_ID`: the ID of the intercept deployment group.



###  Terraform 

To create an intercept deployment, you can use a [`google_network_security_intercept_deployment` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_intercept_deployment).
    
    
    resource "google_network_security_intercept_deployment" "default" {
      intercept_deployment_id    = "intercept-deployment"
      location                   = "us-central1-a"
      forwarding_rule            = google_compute_forwarding_rule.default.id
      intercept_deployment_group = google_network_security_intercept_deployment_group.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View details of an intercept deployment

You can view the details of an intercept deployment, including its name, its forwarding rule, and its location.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptDeployments.get`



**Roles**

  * [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`networksecurity.interceptDeploymentAdmin`) 
  * [Intercept Deployment Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentViewer) (`networksecurity.interceptDeploymentViewer`) 



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the name of the deployment group.

  3. Click the name of the deployment.




###  gcloud 

To view details of an intercept deployment, use the [`gcloud network-security intercept-deployments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/describe):
    
    
    gcloud network-security intercept-deployments describe DEPLOYMENT_ID \
        --location ZONE
    

Replace the following:

  * `DEPLOYMENT_ID`: the ID of the intercept deployment.
  * `ZONE`: the zone of the intercept deployment.



In the output, the name of the intercept deployment is displayed in the `projects/PROJECT_ID/locations/ZONE/interceptDeployments/DEPLOYMENT_ID` format.

## List intercept deployments

You can list all intercept deployments in a project, including their IDs and locations.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.interceptDeployments.list`



**Roles**

  * [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`networksecurity.interceptDeploymentAdmin`) 
  * [Intercept Deployment Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentViewer) (`networksecurity.interceptDeploymentViewer`) 



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the name of the deployment group.




###  gcloud 

To list intercept deployments, use the [`gcloud network-security intercept-deployments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/list):
    
    
    gcloud network-security intercept-deployments list \
        [--location ZONE]
    

To see intercept deployments in a specific zone, replace `ZONE` with the zone of the intercept deployments. This setting is optional.

## Delete an intercept deployment

You can delete an intercept deployment if it is not referenced by any intercept deployment group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.interceptDeployments.delete`



**Roles**

  * [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`networksecurity.interceptDeploymentAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the name of the intercept deployment group.

  3. Select the checkbox of the intercept deployment and click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete an intercept deployment, use the [`gcloud network-security intercept-deployments delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployments/delete):
    
    
    gcloud network-security intercept-deployments delete DEPLOYMENT_ID \
        --no-async \
        --location ZONE
    

Replace the following:

  * `DEPLOYMENT_ID`: the ID of the intercept deployment.
  * `ZONE`: the zone of the intercept deployment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
