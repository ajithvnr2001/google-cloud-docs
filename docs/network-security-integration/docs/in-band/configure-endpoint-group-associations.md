---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-endpoint-group-associations/
title: Create and manage intercept endpoint group associations \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:00.019995+00:00
---

# Create and manage intercept endpoint group associations  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-endpoint-group-associations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage intercept endpoint group associations Stay organized with collections  Save and categorize content based on your preferences. 

An [intercept endpoint group association](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-group-overview) is a global resource that links a consumer's Virtual Private Cloud network to an [intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-endpoint-groups) for traffic inspection. For each VPC network that requires traffic inspection, you create an intercept endpoint group association. The VPC network is ready for traffic inspection after you configure the endpoint group, endpoint group association, and firewall rules to redirect the traffic.

After you configure the endpoint group and the endpoint group association, and configure the firewall rules to redirect the traffic to be inspected, the VPC network is ready for traffic inspection.

This page describes how to create and manage intercept endpoint group associations.

## Before you begin

  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [ Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your Google Cloud project.

  * [Enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your Google Cloud project.

  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).

  * Create a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and a [subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).

  * Create an [intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-endpoint-groups).




### Roles

To create, view, or delete intercept endpoint group associations, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview#iam-roles) on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the following Intercept Endpoint Admin (`roles/networksecurity.interceptEndpointAdmin`) roles and permissions:

  * `networksecurity.interceptEndpointGroupAssociations.create`
  * `networksecurity.interceptEndpointGroupAssociations.delete`
  * `networksecurity.interceptEndpointGroupAssociations.update`
  * `networksecurity.interceptEndpointGroupAssociations.get`
  * `networksecurity.interceptEndpointGroupAssociations.list`
  * `networksecurity.interceptEndpointGroups.use`
  * `compute.networks.use`



## Create an intercept endpoint group association

You can associate a VPC network with multiple intercept endpoint groups. You can also associate an intercept endpoint group with multiple VPC networks.

In the [create and manage intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-endpoint-groups) section, you created an intercept endpoint group to handle the intercepted traffic. However, you must also specify which VPCs' traffic can be inspected. To do this, you create a project-level intercept endpoint group association.

You must create the intercept endpoint group association in the same project as the VPC network.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptEndpointGroupAssociations.create`
  * `networksecurity.interceptEndpointGroups.use`
  * `compute.networks.use`



**Roles**

  * [Intercept Endpoint Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointAdmin) (`networksecurity.interceptEndpointAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the endpoint group.

  3. In the **Associations** section, click **Create**.

  4. In the Create associations pane, click **Add endpoint group association**.

  5. For **Project** and **Network** , select the project and the VPC network that hosts the intercept deployment group.

**Note:** Make sure that the VPC network you associate with the endpoint group is not the same as the deployment group network.
  6. Click **Done**.

  7. Click **Create**.




###  gcloud 

To create an intercept endpoint group association, use the [`gcloud network-security intercept-endpoint-group-associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/create):
    
    
    gcloud network-security intercept-endpoint-group-associations create ENDPOINT_GROUP_ASSOCIATION_ID \
        --location global \
        --network NETWORK \
        --no-async \
        --intercept-endpoint-group \
            projects/ENDPOINT_GROUP_PROJECT_ID/locations/global/interceptEndpointGroups/ENDPOINT_GROUP_ID
    

Replace the following:

  * `ENDPOINT_GROUP_ASSOCIATION_ID`: the ID of the intercept endpoint group association.
  * `NETWORK`: the name of the network.
  * `ENDPOINT_GROUP_PROJECT_ID`: the ID of the Google Cloud project where you created the intercept endpoint group.
  * `ENDPOINT_GROUP_ID`: the ID of the intercept endpoint group.



###  Terraform 

To create an intercept endpoint group association, you can use a [`google_network_security_intercept_endpoint_group_association` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_intercept_endpoint_group_association).
    
    
    resource "google_network_security_intercept_endpoint_group_association" "default" {
      intercept_endpoint_group_association_id = "intercept-endpoint-group-association"
      location                                = "global"
      network                                 = google_compute_network.consumer_network.id
      intercept_endpoint_group                = google_network_security_intercept_endpoint_group.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View details of an intercept endpoint association

You can view the details of an intercept endpoint group association, including its name, intercept endpoint group, location, and network.

You can also see the details of intercept endpoint group association from the **Endpoint groups** tab of the VPC network's details page.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptEndpointgroupAssociations.get`



**Roles**

  * [Intercept Endpoint Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointAdmin) (`networksecurity.interceptEndpointAdmin`) 
  * [Intercept Endpoint Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointViewer) (`networksecurity.interceptEndpointViewer`) 



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the intercept endpoint group. The **Associations** section lists the details of the intercept endpoint associations.




###  gcloud 

To view an intercept endpoint group association, use the [`gcloud network-security intercept-endpoint-group-associations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/describe):
    
    
    gcloud network-security intercept-endpoint-group-associations describe ENDPOINT_GROUP_ASSOCIATION_ID \
        --location global
    

Replace `ENDPOINT_GROUP_ASSOCIATION_ID` with the ID of the intercept endpoint group association.

In the output, the name of the intercept endpoint association is displayed in the `projects/PROJECT_ID/locations/global/interceptEndpointGroupAssociations/ENDPOINT_GROUP_ASSOCIATION_ID` format.

## List intercept endpoint group associations

You can list all interceptor endpoint group associations in a project, including their IDs.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptEndpointgroupAssociations.list`



**Roles**

  * [Intercept Endpoint Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointAdmin) (`networksecurity.interceptEndpointAdmin`) 
  * [Intercept Endpoint Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointViewer) (`networksecurity.interceptEndpointViewer`) 



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the intercept endpoint group. The **Associations** section lists all intercept endpoint associations of the intercept endpoint group.




###  gcloud 

To list all intercept endpoint group associations in a project, use the [`gcloud network-security intercept-endpoint-group-associations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/list):
    
    
    gcloud network-security intercept-endpoint-group-associations list
    

## Delete an intercept endpoint group association

You can delete an intercept endpoint group association of the intercept deployment group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptEndpointgroupAssociations.delete`



**Roles**

  * [Intercept Endpoint Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointAdmin) (`networksecurity.interceptEndpointAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the intercept endpoint group.

  3. In the **Associations** section, select the intercept endpoint association to delete.

  4. Click **Delete**.

  5. Click **Delete** again to confirm.




###  gcloud 

To delete an intercept endpoint group association, use the [`gcloud network-security intercept-endpoint-group-associations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-group-associations/delete):
    
    
    gcloud network-security intercept-endpoint-group-associations delete ENDPOINT_GROUP_ASSOCIATION_ID \
        --no-async \
        --location global
    

Replace `ENDPOINT_GROUP_ASSOCIATION_ID` with the ID of the intercept endpoint group association.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
