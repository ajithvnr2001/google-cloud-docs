---
url: https://docs.cloud.google.com/datastream/docs/manage-private-connectivity-configurations/
title: Manage private connectivity configurations \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:31.858043+00:00
---

# Manage private connectivity configurations  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/manage-private-connectivity-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Manage private connectivity configurations Stay organized with collections  Save and categorize content based on your preferences. 

In this page, you learn how to use the Datastream API to create, retrieve information about, and delete private connectivity configurations.

Private connectivity configurations contain information that Datastream uses to communicate with a data source over a private network (internally within Google Cloud, or with external sources connected over VPN or Interconnect). This communication happens through a Private Service Connect interface or a Virtual Private Cloud (VPC) peering connection.

To use a private connection, any streams and connection profiles that use a private connectivity configuration must be in the same region.

Recommended: Run the source database in a subnet in the same region as the private connectivity configuration. Otherwise, you'll have to manually add a firewall rule that enables communication between the regions.

## Create a private connectivity configuration using VPC peering

Before creating a private connectivity configuration, make sure that you:

  * Have a VPC network to peer to Datastream's private network. For more information about creating a VPC network, see [Using VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering).
  * Have an available IP range (with a CIDR block of /29 at minimum) on the VPC network. Datastream uses this IP range to create VPC peering with the provided VPC, so the range can't overlap with subnets within that VPC. As a result, Datastream can communicate with the source.



There are two parameters associated with creating a private connectivity configuration:

  * `vpcName:` Specify the name and path of the VPC network.
  * `subnet:` Provide an available IP range on the VPC network.



The following code shows a request to create a private connectivity configuration, and specifies the connectivity method as using VPC peering (`vpcPeeringConfig`).

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/privateConnections?privateConnectionId=PRIVATE_CONNECTIVITY_CONFIGURATION_ID
    {
      "displayName": "DISPLAY_NAME",
      "vpcPeeringConfig": {
          "vpcName": "VPC_NAME",
          "subnet": "SUBNET"
      }
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/privateConnections?privateConnectionId=myPrivateConnection
    {
      "displayName": "my-private-connection",
      "vpcPeeringConfig": {
        "vpcName": "projects/my-project/global/networks/my-vpc",
        "subnet": "10.11.12.13/29"
      }
    }
    

As part of creating a private connectivity configuration, multiple Google Cloud resources are also being created to achieve the connectivity. Therefore, it may take a few minutes for the private connectivity configuration to be created.

After the private connectivity configuration is created, you can view information about it by calling the `privateConnections/get` method. Your output appears, similar to the following:
    
    
    {
      "name": "projects/projectId/location/us-central1/privateConnections/myPrivateConnection",
      "createTime": "2019-12-22T16:17:37.159786963Z",
      "updateTime": "2019-12-22T16:17:37.159786963Z",
      "displayName": "my-private-connection",
      "state": "CREATED",
      "vpcPeeringConfig": {
        "vpcName": "projects/my-project/global/networks/my-vpc",
        "subnet": "10.11.12.13/29"
      }  
    }
    

There are three states of a private connectivity configuration:

  * `CREATING:` The private connectivity configuration is in the process of being created.
  * `CREATED:` The private connectivity configuration is ready to be used by connection profiles.
  * `FAILED:` A problem occurred while the private connectivity configuration was in the process of being created. If this happens, then a user-friendly error message appears, detailing why the error occurred and what to do to rectify the problem.



### gcloud
    
    
    gcloud datastream private-connections create PRIVATE_CONNECTION_NAME --location=LOCATION --display-name=DISPLAY_NAME --vpc=VPC_NAME --subnet=SUBNET

For example:
    
    
    gcloud datastream private-connections create my-privateConnection --location=us-central1 --display-name=my-private-connection --vpc=my-vpc --subnet=10.11.12.13/29
    

## Create a private connectivity configuration using a Private Service Connect interface

Before creating a private connectivity configuration, make sure that you:

  * Have a VPC network to connect to the Datastream private network. For more information about creating a VPC network, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  * Create a [network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments#create-manual-accept) in your VPC project.

  * Verify that Google Cloud and the on-premises firewall allow traffic from the network attachment IP address range to the source database from which you want to stream data.




The following code shows a request to create a private connectivity configuration using Private Service Connect interfaces. You first need to run a command to create a private connectivity configuration with the `validateOnly` flag (`--validate-only` for Google Cloud CLI):

### REST
    
    
    POST "https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/privateConnections?privateConnectionId=PRIVATE_CONNECTIVITY_CONFIGURATION_ID&validateOnly=true"

### gcloud
    
    
    gcloud datastream private-connections create PRIVATE_CONNECTION_NAME --location=LOCATION --display-name=DISPLAY_NAME --network-attachment=NETWORK_ATTACHMENT_NAME --validate-only

In the response, you get the name of the producer project to approve. You need to add it to your network attachment allowed projects list:

  1. Use the `describe` method to get the current `producer-accept-list` for your network attachment. For more information, see the Compute Engine [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/describe).
  2. Add the producer project to this list using the `update` method. For more information, see the Compute Engine [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/update).



Once you add the producer project to the allowed projects list, run the command to create the private connectivity configuration again, this time without the `validateOnly` flag:

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/privateConnections?privateConnectionId=PRIVATE_CONNECTIVITY_CONFIGURATION_ID
    {
      "displayName": "DISPLAY_NAME",
      "pscInterfaceConfig": {
          "networkAttachment": "NETWORK_ATTACHMENT_NAME"
      }
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/privateConnections?privateConnectionId=myPrivateConnection
    {
      "displayName": "my-private-connection",
      "pscInterfaceConfig": {
        "networkAttachment": "projects/my-project/regions/us-central1/networkAttachments/my-na"
      }
    }
    

### gcloud
    
    
    gcloud datastream private-connections create PRIVATE_CONNECTION_NAME --location=LOCATION --display-name=DISPLAY_NAME --network-attachment=NETWORK_ATTACHMENT_NAME

For example:
    
    
    gcloud datastream private-connections create my-private-connection --location=us-central1 --display-name=my-private-connection --network-attachment=my-network-attachment
    

Don't change the subnetwork associated with your Private Service Connect network attachment after you create the private connectivity configuration. If you do, the streams using the configuration fail. If you need to change the subnetwork, recreate the private connectivity configuration.

## Get information about a private connectivity configuration

The following code shows a request to retrieve information about a private connectivity configuration that has been created.

### REST
    
    
    GET https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/privateConnections/PRIVATE_CONNECTIVITY_CONFIGURATION_ID

For example:
    
    
    GET https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/privateConnections/myPrivateConnection
         

### gcloud

For more information about using `gcloud` to retrieve information about your private connectivity configuration, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/private-connections/describe).

## List private connectivity configurations

The following code shows a request to retrieve information about all of your private connectivity configurations.

### REST
    
    
    GET https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/privateConnections

### gcloud

For more information about using `gcloud` to retrieve information about all of your private connectivity configurations, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/private-connections/list).

## Delete a private connectivity configuration

The following code shows a request to delete a private connectivity configuration. After the configuration is deleted, any connection profiles using the configuration won't work. In addition, any streams using these connection profiles won't be operable.

To resolve this issue, assign a different private connectivity configuration to each connection profile. For more information, see [Update a connection profile](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles#update_a_connection_profile).

### REST
    
    
    DELETE https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/privateConnections/[private-connectivity-configuration-id] {"force": true} 

For example:
    
    
    DELETE https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/privateConnections/myPrivateConnection {"force": true} 
    

You must add the `{"force": true}` piece of code to ensure that the private connectivity configuration is deleted properly.

### gcloud

For more information about using `gcloud` to delete your private connectivity configuration, see the [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/private-connections/delete).

## What's next

  * Learn more about [private connectivity](https://docs.cloud.google.com/datastream/docs/private-connectivity).
  * Learn about other [network connectivity options](https://docs.cloud.google.com/datastream/docs/network-connectivity-options) you can use with Datastream.
  * Learn how to [use the Datastream API to manage connection profiles](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles).
  * Learn how to [use the Datastream API to manage streams](https://docs.cloud.google.com/datastream/docs/manage-streams).
  * For more information about using the Datastream API, see the [reference documentation](https://docs.cloud.google.com/datastream/docs/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
