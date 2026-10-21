---
url: https://docs.cloud.google.com/livestream/docs/how-to/vpc/configure-private-services-access/
title: Configure private services access \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:37.585487+00:00
---

# Configure private services access  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/vpc/configure-private-services-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Configure private services access Stay organized with collections  Save and categorize content based on your preferences. 

Private services access is a secure, private connection between your Google Cloud virtual private cloud (VPC) network and Google-managed or third-party services. It enables VM instances in your VPC network to communicate with these services using internal IP addresses, without exposing traffic to the public internet.

## Before you begin

To establish a private connection, complete the following prerequisites:

  * You must have an [existing VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) that you can use to connect to the service producer's network. VM instances must use this VPC network to connect to services over a private connection.
  * Follow the steps on the Live Stream API [Before you begin](https://docs.cloud.google.com/livestream/docs/how-to/before-you-begin) page to create a properly-configured Google Cloud project (or choose an existing project).



## Enable private services access for the Live Stream API

The general process for configuring private services access is provided in the [Virtual Private Cloud documentation](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). This page adapts the process to the Live Stream API.

  1. [Install and configure the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed the Google Cloud CLI previously, make sure you have the latest version by running `gcloud components update`.
  2. Enable the Service Networking API.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud services enable servicenetworking.googleapis.com

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud services enable servicenetworking.googleapis.com

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud services enable servicenetworking.googleapis.com

  3. To get the permissions that you need to set up a private connection, ask your administrator to grant you the [Compute Engine Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the Google Cloud project in which the VPC network resides. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

The required permissions are also available through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

  4. In the VPC network, allocate a named IP range using the `addresses create` command as shown in the following examples.

To specify an address range and a prefix length, which is also the subnet mask, use the `addresses` and `prefix-length` flags. For example, to allocate the CIDR block 192.168.0.0/17, specify `192.168.0.0` for the address and `17` for the prefix length.

Before using any of the command data below, make the following replacements: 

     * `RESERVED_RANGE_NAME`: a name for the allocated range, such as `my-allocated-range`
     * `DESCRIPTION`: a description for the range, such as `allocated for my-service`
     * `VPC_NETWORK`: the name of your VPC network, such as `my-vpc-network`

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute addresses create RESERVED_RANGE_NAME \
        --global \
        --purpose=VPC_PEERING \
        --addresses=192.168.0.0 \
        --prefix-length=13 \
        --description="DESCRIPTION" \
        --network=VPC_NETWORK

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute addresses create RESERVED_RANGE_NAME `
        --global `
        --purpose=VPC_PEERING `
        --addresses=192.168.0.0 `
        --prefix-length=13 `
        --description="DESCRIPTION" `
        --network=VPC_NETWORK

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute addresses create RESERVED_RANGE_NAME ^
        --global ^
        --purpose=VPC_PEERING ^
        --addresses=192.168.0.0 ^
        --prefix-length=13 ^
        --description="DESCRIPTION" ^
        --network=VPC_NETWORK

You should receive a response similar to the following:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses/RESERVED_RANGE_NAME].

To only specify a prefix length, use the `prefix-length` flag. When you omit the address range, Google Cloud automatically selects an unused address range in your VPC network. The following example selects an unused IP address range with a 17-bit prefix length.

Before using any of the command data below, make the following replacements: 

     * `RESERVED_RANGE_NAME`: a name for the allocated range, such as `my-allocated-range`
     * `DESCRIPTION`: a description for the range, such as `allocated for my-service`
     * `VPC_NETWORK`: the name of your VPC network, such as `my-vpc-network`

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute addresses create RESERVED_RANGE_NAME \
        --global \
        --purpose=VPC_PEERING \
        --prefix-length=13 \
        --description="DESCRIPTION" \
        --network=VPC_NETWORK

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute addresses create RESERVED_RANGE_NAME `
        --global `
        --purpose=VPC_PEERING `
        --prefix-length=13 `
        --description="DESCRIPTION" `
        --network=VPC_NETWORK

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud compute addresses create RESERVED_RANGE_NAME ^
        --global ^
        --purpose=VPC_PEERING ^
        --prefix-length=13 ^
        --description="DESCRIPTION" ^
        --network=VPC_NETWORK

You should receive a response similar to the following:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses/RESERVED_RANGE_NAME].

The preceding example creates a private connection to Google so that the VM instances in the provided VPC network (for example, `my-vpc-network`) can use private services access to reach Google services that support it.

The Live Stream API requires the allocation of a CIDR/17 block per region. If you are planning to use the Live Stream API in multiple regions, allocate a larger block. The following table describes the recommended block size to allocate depending on the number of regions:

Number of regions| value for the `prefix-length` flag  
---|---  
1| 17  
2| 16  
3-4| 15  
5-8| 14  
9-16| 13  
  5. Create a private connection between the service producer network and your VPC network:

     1. Create a private connection.

Before using any of the command data below, make the following replacements: 

        * `RESERVED_RANGE_NAME`: the name of the allocated range you created in the previous step
        * `VPC_NETWORK`: the name of your VPC network
        * `PROJECT_ID`: the Google Cloud project ID of the project that contains your VPC network

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings connect \
        --service=servicenetworking.googleapis.com \
        --ranges=RESERVED_RANGE_NAME \
        --network=VPC_NETWORK \
        --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings connect `
        --service=servicenetworking.googleapis.com `
        --ranges=RESERVED_RANGE_NAME `
        --network=VPC_NETWORK `
        --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings connect ^
        --service=servicenetworking.googleapis.com ^
        --ranges=RESERVED_RANGE_NAME ^
        --network=VPC_NETWORK ^
        --project=PROJECT_ID

You should receive a response similar to the following:
    
    Operation "operations/OPERATION_ID" finished successfully.

This command creates a long-running operation (LRO).

     2. If the command succeeds, skip to the next step. Otherwise, check the operation status.

Before using any of the command data below, make the following replacements: 

        * `OPERATION_ID`: the ID of the operation returned in the previous step

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings operations describe \
      --name=operations/OPERATION_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings operations describe `
      --name=operations/OPERATION_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings operations describe ^
      --name=operations/OPERATION_ID

You should receive a response similar to the following:
    
    Operation "operations/OPERATION_ID" finished successfully.

**Note:** You can specify more than one allocated range when you create a private connection. For example, if a range has been exhausted, you can assign additional allocated ranges. The service will use IP addresses from all of the provided ranges in the order that you specified.
  6. (Optional) If you are using VPC Service Controls, you need to enable VPC-SC for the private connection you just created.

Before using any of the command data below, make the following replacements: 

     * `VPC_NETWORK`: the name of your VPC network

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings enable-vpc-service-controls \
        --service=servicenetworking.googleapis.com \
        --network=VPC_NETWORK

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings enable-vpc-service-controls `
        --service=servicenetworking.googleapis.com `
        --network=VPC_NETWORK

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud services vpc-peerings enable-vpc-service-controls ^
        --service=servicenetworking.googleapis.com ^
        --network=VPC_NETWORK

You should receive a response similar to the following:
    
    Operation "operations/OPERATION_ID" finished successfully.

  7. (Optional) To enable on-premises access to the service producer, add the SRT / RTMP IP Address as a custom route advertisement on your Cloud Router. Then, update the Service Networking VPC peering to export custom routes, extending connectivity from your local network through the peering connection. For more information, see [on-premises host troubleshooting](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#on-prem).




[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/livestream/docs/how-to/vpc/secure-pipeline)

[ Next Configure a private pool  arrow_forward  ](https://docs.cloud.google.com/livestream/docs/how-to/vpc/configure-private-pool)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
