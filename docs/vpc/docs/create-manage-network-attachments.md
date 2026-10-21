---
url: https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments/
title: Create and manage network attachments \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:12.346373+00:00
---

# Create and manage network attachments  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage network attachments

This page describes how consumer network administrators can create and manage Private Service Connect network attachments. Network attachments let service producer VPC networks initiate connections to consumer VPC networks.

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.
  * If you want to manually specify which projects can connect to a network attachment, you need to know the IDs of the projects.



### Roles

To get the permissions that you need to create, view, and delete network attachments, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create a subnet

When you create a network attachment, you assign it a single [regular subnet](https://docs.cloud.google.com/vpc/docs/subnets#purpose). This subnet must be in the same region as the network attachment. One subnet can be shared across multiple network attachments. Subnets with the dual-stack or IPv6-only stack type must use internal IPv6 address ranges.

For more information about creating subnets, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

## Create network attachments

Network attachments are regional resources that represent the consumer side of a [Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) connection. A network attachment must be in the same region as the associated Private Service Connect interface's VM.

The network attachment's [authorization policy](https://docs.cloud.google.com/vpc/docs/about-network-attachments#connection-policies) determines whether a network attachment can accept a connection from a Private Service Connect interface.

You can update the subnet, accept list, reject list, and description of a network attachment.

### Create a network attachment that manually accepts connections

You can create a network attachment that manually accepts connections. Before you create an attachment of this type, make sure that you know either the project IDs or the service class IDs of the producers that you want to accept.

The accept and reject lists can contain either project IDs or service class IDs, but not a mix of both.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page:

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click **Network attachments**.

  3. Click **Create network attachment**.

  4. Enter a **Name**.

  5. Select a **Network**.

  6. Select a **Region**.

  7. Select a **Subnetwork**.

  8. Do one of the following:

     * To accept connections based on project ID: 
       1. Select **Accept connections for selected projects**.
       2. For each project that you want to accept, click **Add accepted project** , and then enter the project ID to accept.
       3. Optional: For each project that you want to explicitly reject, click **Add rejected project** , and then enter the project ID to reject.
     * To accept connections based on service class ID: 
       1. Select **Accept connections for selected service classes**.
       2. For each service class that you want to accept, click **Add accepted service class** , and then select the service class to accept.
       3. Optional: For each service class that you want to explicitly reject, click **Add rejected service class** , and then select the service class to reject.
  9. Click **Create network attachment**.




###  gcloud 

Use the [`network-attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create).
    
    
    gcloud compute network-attachments create ATTACHMENT_NAME \
        --region=REGION \
        --connection-preference=ACCEPT_MANUAL \
        --producer-accept-list=ACCEPTED_PRODUCERS \
        --producer-reject-list=REJECTED_PRODUCERS \
        --subnets=SUBNET_NAME
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the network attachment.
  * `REGION`: the region of the network attachment.
  * `ACCEPTED_PRODUCERS`: a comma-separated list of producers that are authorized to connect to this network attachment. You can specify producers in one of the following ways: 
    * By project ID: for example, `project-id-1,project-id-2`.
    * By service class ID: each ID must use the `serviceclasses/` prefix—for example, `serviceclasses/service-class1,serviceclasses/service-class2`.
  * `REJECTED_PRODUCERS`: a comma-separated list of project IDs or service class IDs that are explicitly rejected from connecting to this network attachment. Specify producers using the same format as the consumer accept list.
  * `SUBNET_NAME`: the name of the subnet to associate with this network attachment.



###  API 

Make a `POST` request to the [`networkAttachments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkAttachments/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkAttachments
    {
      "connectionPreference": "ACCEPT_MANUAL",
      "name": "ATTACHMENT_NAME",
      "producerAcceptLists": [
        "ACCEPTED_PRODUCERS"
      ],
      "producerRejectLists": [
        "REJECTED_PRODUCERS"
      ],
      "subnetworks": [
        "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project to create the network attachment in.
  * `REGION`: the region of the network attachment
  * `ATTACHMENT_NAME`: the name of the network attachment
  * `ACCEPTED_PRODUCERS`: a list of producers that are authorized to connect to this network attachment. You can specify producers in one of the following ways: 
    * By project ID: for example, `"project-id-1", "project-id-2"`.
    * By service class ID: each ID must use the `serviceclasses/` prefix—for example, `"serviceclasses/service-class1", "serviceclasses/service-class2"`.
  * `REJECTED_PRODUCERS`: a list of project IDs or service class IDs that are explicitly rejected from connecting to this network attachment. Specify producers using the same format as the consumer accept list.
  * `SUBNET_NAME`: the name of the subnet to associate with the network attachment.



### Create a network attachment that automatically accepts connections

You can create a network attachment that automatically accepts connections from any Private Service Connect interface that refers to the network attachment.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page:

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click **Network attachments**.

  3. Click **Create network attachment**.

  4. Enter a **Name**.

  5. Select a **Network**.

  6. Select a **Region**.

  7. Select a **Subnetwork**.

  8. Click **Automatically accept connections for all projects**.

  9. Click **Create network attachment**.




###  gcloud 

Use the [`network-attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create).
    
    
    gcloud compute network-attachments create ATTACHMENT_NAME \
        --region=REGION \
        --connection-preference=ACCEPT_AUTOMATIC \
        --subnets=SUBNET_NAME
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the network attachment.
  * `REGION`: the region of the network attachment.
  * `SUBNET_NAME`: the name of the subnet to associate with this network attachment.



###  API 

Make a `POST` request to the [`networkAttachments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkAttachments/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkAttachments
    {
      "connectionPreference": "ACCEPT_AUTOMATIC",
      "name": "ATTACHMENT_NAME",
      "subnetworks": [
        "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project to create the network attachment in.
  * `REGION`: the region of the network attachment
  * `ATTACHMENT_NAME`: the name of the network attachment
  * `SUBNET_NAME`: the name of the subnet to associate with the network attachment.



## List network attachments

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page:

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click **Network attachments**.




###  gcloud 

  * To list all network attachments in a project, use the [`network-attachments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/list).
        
        gcloud compute network-attachments list
        

  * To list network attachments in a given region or regions, use the [`network-attachments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/list), and specify the regions.
        
        gcloud compute network-attachments list
           --regions=REGIONS
        

Replace `REGIONS` with the region or regions to list network attachments in. You can include multiple regions in a comma-separated list.




###  API 

To list network attachments in a given region, make a `GET` request to the [`networkAttachments.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkAttachments/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkAttachments
    

Replace the following:

  * `PROJECT_ID`: the ID of the project.
  * `REGION`: the region of the network attachment.



## Describe network attachments

You can describe a network attachment to view its details, including the associated Private Service Connect interface connections. For each connection, you can see the Private Service Connect interface's assigned IP address.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page:

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click **Network attachments**.

  3. Select a network attachment to view its details and a list of connected projects.

  4. To view individual Private Service Connect interface connections for a project, click the name of the project.

The connection status of a project does not necessarily determine the status of Private Service Connect interface connections from that project. For example, if you add a project to the reject list after you've accepted a connection from that project, the project status is rejected, but the existing connection remains open. New connections from that project are rejected.




###  gcloud 

Use the [`network-attachments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/describe).
    
    
    gcloud compute network-attachments describe ATTACHMENT_NAME \
        --region=REGION
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the network attachment to describe.
  * `REGION`: the region of the network attachment



Connected Private Service Connect interfaces are displayed in the following format:
    
    
    connectionEndpoints:
    - ipAddress: 10.6.0.59
      projectIdOrNum: '123456789'
      status: ACCEPTED
      subnetwork: https://www.googleapis.com/compute/v1/projects/consumer-project-id/regions/us-central1/subnetworks/consumer-subnet
    - ipAddress: 10.6.0.11
      projectIdOrNum: '987654321'
      status: ACCEPTED
      subnetwork: https://www.googleapis.com/compute/v1/projects/consumer-project-id/regions/us-central1/subnetworks/consumer-subnet
      ```
    

###  API 

To describe a network attachment and view its details, make a `GET` request to the [`networkAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkAttachments/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project.
  * `REGION`: the region of the network attachment.
  * `ATTACHMENT_NAME`: the name of the network attachment.



Connected Private Service Connect interfaces are displayed in the following format:
    
    
    "connectionEndpoints": [
      {
        "status": "ACCEPTED",
        "projectIdOrNum": "123456789",
        "subnetwork": "https://www.googleapis.com/compute/v1/projects/consumer-project-id/regions/us-central1/subnetworks/consumer-subnet-1",
        "ipAddress": "10.6.0.11"
      },
      {
        "status": "ACCEPTED",
        "projectIdOrNum": "987654321",
        "subnetwork": "https://www.googleapis.com/compute/v1/projects/consumer-project-id/regions/us-central1/subnetworks/consumer-subnet-2",
        "ipAddress": "10.6.0.59"
      }
    ]
    

## Update network attachments

You can update a network attachment by replacing its subnet, description, or—for network attachments that were created to manually accept connections—the accept or reject lists. If you need to update other fields, delete the network attachment, and then create a new one.

If you replace a network attachment's subnet, existing connections are not affected. Connections that are created after the update use IP addresses from the new subnet.

If you update a network attachment's accept or reject list, existing connections are not affected. Connections that are created after the update are accepted or rejected according to the updated lists.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page:

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click **Network attachments**.

  3. Click the network attachment that you want to update, and then click **Edit**.

  4. To replace the network attachment's subnetwork, click **Subnetwork** , and then select the new subnetwork.

  5. To update the accept list, do the following:

     1. To add a producer, click **Add accepted project** or **Add accepted service class** , and then enter a project ID or select a service class.
     2. To remove a producer, hold the pointer over the producer, and then click delete **Delete accepted project** or **Delete accepted service class**.
  6. To update the reject list, do the following:

     1. To add a producer, click **Add rejected project** or **Add rejected service class** , and then enter a project ID or select a service class.
     2. To remove a producer, hold the pointer over the producer, and then click delete **Delete rejected project** or **Delete rejected service class**.
  7. Click **Update network attachment**.




###  gcloud 

Use the [`network-attachments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update). You can update one or more of the fields listed here, except for region, which is used to identify the network attachment. If you update a network attachment's accept or reject lists, you must replace the entire list in one update.
    
    
    gcloud compute network-attachments update ATTACHMENT_NAME \
        --region=REGION \
        --subnets=SUBNET \
        --producer-accept-list=ACCEPTED_PRODUCERS \
        --producer-reject-list=REJECTED_PRODUCERS \
        --description=DESCRIPTION
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the network attachment.
  * `REGION`: the region of the network attachment. This flag is used to identify the network attachment. You can't update the region of a network attachment.
  * `SUBNET`: the name of the subnet to associate with this network attachment.
  * `ACCEPTED_PRODUCERS`: a comma-separated list of producers that are authorized to connect to this network attachment. You can specify producers in one of the following ways: 
    * By project ID: for example, `project-id-1,project-id-2`.
    * By service class ID: each ID must use the `serviceclasses/` prefix—for example, `serviceclasses/service-class1,serviceclasses/service-class2`.
  * `REJECTED_PRODUCERS`: a comma-separated list of project IDs or service class IDs that are explicitly rejected from connecting to this network attachment. Specify producers using the same format as the consumer accept list.
  * `DESCRIPTION`: a description of the network attachment.



###  API 

  1. Send an API request to describe the network attachment that you want to update.
  2. Note the value for the `fingerprint` field of the network attachment.
  3. Make a `PATCH` request to the [`networkAttachments.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkAttachments/patch). Omit any fields from the request body that you don't want to replace, except for `fingerprint`. If you update a network attachment's accept or reject lists, you must replace the entire list in one update.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME
         {
           "fingerprint": "FINGERPRINT",
           "producerAcceptLists": [
             "ACCEPTED_PRODUCERS"
           ],
           "producerRejectLists": [
             "REJECTED_PRODUCERS"
           ],
           "subnetworks": [
             "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME"
           ],
           "description": "DESCRIPTION"
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project.
     * `REGION`: the region of the network attachment.
     * `ATTACHMENT_NAME`: the name of the network attachment.
     * `FINGERPRINT`: the value for the fingerprint field that you found in step 2.
     * `ACCEPTED_PRODUCERS`: a list of producers that are authorized to connect to this network attachment. You can specify producers in one of the following ways: 
       * By project ID: for example, `"project-id-1", "project-id-2"`.
       * By service class ID: each ID must use the `serviceclasses/` prefix—for example, `"serviceclasses/service-class1", "serviceclasses/service-class2"`.
     * `REJECTED_PRODUCERS`: a list of project IDs or service class IDs that are explicitly rejected from connecting to this network attachment. Specify producers using the same format as the consumer accept list.
     * `SUBNET_NAME`: the name of the new subnet to associate with the network attachment.
     * `DESCRIPTION`: an updated description for the network attachment.



## Delete network attachments

You can delete a network attachment if it does not have any connections. If you want to delete a network attachment that has connections, the producer must first delete the associated Private Service Connect interface.

If you delete a network attachment and then create a new one with the same name, Google Cloud treats the network attachments as two separate resources.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page:

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click **Network attachments**.

  3. Select a network attachment, and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

Use the [`network-attachments delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/delete).
    
    
    gcloud compute network-attachments delete ATTACHMENT_NAME \
        --region=REGION
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the network attachment to delete.
  * `REGION`: the region of the network attachment



###  API 

Make a `DELETE` request to the [`networkAttachments.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkAttachments/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/networkAttachments/ATTACHMENT_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project.
  * `REGION`: the region of the network attachment.
  * `ATTACHMENT_NAME`: the name of the network attachment.



## What's next?

  * [Create a Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/create-manage-private-service-connect-interfaces) that connects to a network attachment.
  * [Configure security](https://docs.cloud.google.com/vpc/docs/configure-security-private-service-connect-interfaces) for a network that has a network attachment.
  * [Manage destination overlap](https://docs.cloud.google.com/vpc/docs/manage-destination-overlap) in a network that has a Private Service Connect interface connection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
