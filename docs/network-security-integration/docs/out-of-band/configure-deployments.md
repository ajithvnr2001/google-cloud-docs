---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployments/
title: Create and manage mirroring deployments \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:29.618719+00:00
---

# Create and manage mirroring deployments  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage mirroring deployments Stay organized with collections  Save and categorize content based on your preferences. 

Mirroring deployment lets you expose a zonal set of load balanced appliances so that mirroring deployment can be used by the [mirroring endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview).

This page explains how to create and manage [mirroring deployment](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployments-overview).

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.
  * You have a [mirroring deployment group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups).
  * You have a forwarding rule to direct network traffic to an internal passthrough Network Load Balancer whose backends provide packet mirroring. For more information, see [Set up producer services](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-producer-service).



### Roles

To get the permissions that you need to create, view, or delete mirroring deployments, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployments-overview#iam-roles) on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the following [Mirroring Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.mirroringDeploymentAdmin) (`roles/networksecurity.mirroringDeploymentAdmin`) permissions:

  * `networksecurity.mirroringDeployments.create`
  * `networksecurity.mirroringDeployments.delete`
  * `networksecurity.mirroringDeployments.get`
  * `networksecurity.mirroringDeployments.list`



## Create a mirroring deployment

Create a mirroring deployment to represent the producer side within a zone and associate it with the mirroring deployment group. We recommend that you create the mirroring deployment in a project owned by your security administrator.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.mirroringDeployments.create`



**Roles**

  * Mirroring Deployment Admin (`roles/networksecurity.mirroringDeploymentAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click filter_list**Filter**.

  3. From the **Properties** list, select **Purpose** and then for **Value** , select **NSI out-of-band**.

  4. Click the deployment group where you want to add the mirroring deployment.

  5. Click **Create mirroring deployment**.

  6. For **Name** , enter a name of the mirroring deployment.

  7. For **Region** and **Zone** , select your region and zone.

  8. For **Load balancer** , select the internal passthrough Network Load Balancer.

  9. For **Forwarding rule** , select the UDP forwarding rule of the load balancer. If the load balancer has only one forwarding rule, it is selected by default and the field is disabled.

**Note:** The forwarding rule's VPC network must match the mirroring deployment group's network.
  10. Click **Create**.




###  gcloud 

To create a mirroring deployment, use the [`gcloud network-security mirroring-deployments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/create):
    
    
     gcloud network-security mirroring-deployments \
         create DEPLOYMENT \
         --location ZONE \
         --forwarding-rule FWD_RULE \
         --forwarding-rule-location REGION \
         --mirroring-deployment-group DEPLOYMENT_GROUP_ID \
         --no-async
    

Replace the following:

  * `DEPLOYMENT`: the name of the mirroring deployment; you can specify the name as a string or as a unique URL identifier.

  * `ZONE`: the zone of the mirroring deployment

  * `FWD_RULE`:the forwarding rule to direct network traffic to a load balance

  * `REGION`: the region of the forwarding rule

  * `DEPLOYMENT_GROUP_ID`: the ID of the mirroring deployment group




### Terraform

To create a mirroring deployment, you can use a [`google_network_security_mirroring_deployment` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_mirroring_deployment).
    
    
    resource "google_network_security_mirroring_deployment" "default" {
      mirroring_deployment_id    = "mirroring-deployment"
      location                   = "us-central1-a"
      forwarding_rule            = google_compute_forwarding_rule.default.id
      mirroring_deployment_group = google_network_security_mirroring_deployment_group.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View mirroring deployment

You can view the details of a specific mirroring deployment in a project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringDeployments.get`



**Roles**

  * Mirroring Deployment Admin (`roles/networksecurity.mirroringDeploymentAdmin`)
  * Mirroring Deployment Viewer (`roles/networksecurity.mirroringDeploymentViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the name of the deployment group.

  3. Click the name of the deployment.




###  gcloud 

To view details of a mirroring deployment, use the [`gcloud network-security mirroring-deployments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/describe):
    
    
    gcloud network-security mirroring-deployments \
        describe DEPLOYMENT \
        --location ZONE \
        --project PROJECT
    

Replace the following:

  * `DEPLOYMENT`: the name of the mirroring deployment

  * `ZONE`: the zone of the mirroring deployment

  * `PROJECT`: the project name of the mirroring deployment




## List mirroring deployments

You can list all the mirroring deployments in a project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.mirroringDeployments.list`



**Roles**

  * Mirroring Deployment Admin (`roles/networksecurity.mirroringDeploymentAdmin`)
  * Mirroring Deployment Viewer (`roles/networksecurity.mirroringDeploymentViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the name of the deployment group.




###  gcloud 

To list mirroring deployments, use the [`gcloud network-security mirroring-deployments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/list):
    
    
     gcloud network-security mirroring-deployments list \
         --location ZONE \
         --project PROJECT
    

Replace the following:

  * `ZONE`: the zone of the mirroring deployment

  * `PROJECT`: the name of your mirroring deployment project




## Delete a mirroring deployment

You can delete a mirroring deployment by specifying its name, location, and project. However, if a mirroring deployment is referenced by a mirroring deployment group, then it cannot be deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.mirroringDeployments.delete`



**Roles**

  * Mirroring Deployment Admin (`roles/networksecurity.mirroringDeploymentAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the name of the mirroring deployment group.

  3. Select the checkbox of the mirroring deployment and click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete a mirroring deployment, use the [`gcloud network-security mirroring-deployments delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployments/delete):
    
    
     gcloud network-security mirroring-deployments \
         delete DEPLOYMENT \
         --location ZONE \
         --project PROJECT \
         --no-async
    

Replace the following:

  * `DEPLOYMENT`: the name of the mirroring deployment

  * `ZONE`: the zone of the mirroring deployment

  * `PROJECT`: the project name of the mirroring deployment




## What's next

  * [Mirroring deployment groups overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview)
  * [Create and manage mirroring deployment groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
