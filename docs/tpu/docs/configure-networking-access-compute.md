---
url: https://docs.cloud.google.com/tpu/docs/configure-networking-access-compute/
title: Configure networking and access to a TPU instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:13.790743+00:00
---

# Configure networking and access to a TPU instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/configure-networking-access-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure networking and access to a TPU instance

This page describes how to set up custom network and access configurations for a TPU instance, including:

  * Specifying a custom network and subnetwork
  * Specifying external and internal IP addresses
  * Enabling SSH access to TPUs
  * Attaching a custom service account to your TPU
  * Enabling custom SSH methods
  * Using VPC Service Controls



## Prerequisites

Before you run these procedures, you must install the Google Cloud CLI, create a Google Cloud project, and enable the Compute Engine API. For instructions, see [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).

## Specify a custom network and subnetwork

When creating a TPU VM instance or instance template, you can optionally specify the network and subnetwork to use for the TPU. If you don't specify a network, the TPU will be in the `default` network. The subnetwork needs to be in the same region as the zone where the TPU runs.

  1. Create a network and subnetwork by following the instructions to [create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  2. Create a TPU VM, specifying the custom network and subnetwork:

To specify the network and subnetwork, include the networking flags shown in the following example when you run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
         
         gcloud compute instances create TPU_NAME \
             --machine-type=MACHINE_TYPE \
             --image-family=IMAGE_FAMILY \
             --image-project=IMAGE_PROJECT \
             --zone=ZONE \
             --maintenance-policy=TERMINATE \
             --network=NETWORK_NAME \
             --subnet=SUBNET_NAME \
             --stack-type=STACK_TYPE \
             --private-network-ip=INTERNAL_IPV4_ADDRESS \
             --address=EXTERNAL_IPV4_ADDRESS
         

Replace the following placeholders:

     * TPU_NAME: A name for the TPU VM.
     * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
     * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
     * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).
     * NETWORK_NAME: Optional: name of the network. If you specify a network, you must specify a subnet and it must belong to the same network. If you don't specify a network, Compute Engine infers the network from the subnet specified.
     * SUBNET_NAME: Name of the subnet to use with the instance.

To view a list of subnets in the network, use the [`gcloud compute networks subnets list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list).

     * STACK_TYPE: Optional: the networking stack type for the network interface. `STACK_TYPE` must be one of: `IPV4_ONLY`, `IPV4_IPV6`, or `IPV6_ONLY` ([Preview](https://cloud.google.com/products#product-launch-stages)). The default value is `IPV4_ONLY`.

     * INTERNAL_IPV4_ADDRESS: Optional: the internal IPv4 address that you want the compute instance to use in the target subnet. Omit this flag if you don't need a specific IP address.

To specify an internal IPv6 address, use the flag `--internal-ipv6-address` instead.

     * EXTERNAL_IPV4_ADDRESS: Optional: the static external IPv4 address to use with the network interface. Replace EXTERNAL_IPV4_ADDRESS with one of the following:

       * A valid IPv4 address from the specified subnet. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address).
       * `''` (an empty string) to use an ephemeral external IP address.

If you don't want the VM to have an external IP address, replace the `--address` flag with the `--no-address` flag.

To specify an external IPv6 address, use the flag `--external-ipv6-address` instead.




## Understand external and internal IP addresses

When you create TPU VM instances, they always have internal IP addresses. If you create your TPU instances using the gcloud CLI, external IP addresses are generated by default. If you create them through the Compute Engine REST APIs (`compute.googleapis.com`), no external IP address is assigned by default. You can change the default behavior in both cases.

Here are a few reasons to restrict your TPU VMs to only use internal IP addresses:

  * **Enhanced security** : Internal IP addresses are only accessible to resources within the same VPC network, which can improve security by limiting external access to the TPU VMs. This is especially important when working with sensitive data or when you want to restrict access to the TPU VMs to specific users or systems within your network.
  * **Cost savings** : By using internal IP addresses, you can avoid the costs associated with external IP addresses, which can be significant for a large number of TPU VMs.
  * **Improved network performance** : Internal IP addresses can lead to better network performance because the traffic stays within Google's network, avoiding the overhead of routing through the public internet. This is particularly relevant for large-scale machine learning workloads that need high-bandwidth communication between TPU VMs.



### Create a TPU VM instance without an external IP address

If you want to create a TPU VM instance without an external IP address, use the `--no-address` flag when you run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
    
    
    gcloud compute instances create TPU_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --maintenance-policy=TERMINATE \
        --network=NETWORK_NAME \
        --subnet=SUBNET_NAME \
        --stack-type=STACK_TYPE \
        --private-network-ip=INTERNAL_IPV4_ADDRESS \
        --no-address
    

Replace the following placeholders:

  * TPU_NAME: A name for the TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).
  * NETWORK_NAME: Optional: name of the network. If you specify a network, you must specify a subnet and it must belong to the same network. If you don't specify a network, Compute Engine infers the network from the subnet specified.
  * SUBNET_NAME: Name of the subnet to use with the instance.

To view a list of subnets in the network, use the [`gcloud compute networks subnets list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list).

  * STACK_TYPE: Optional: the networking stack type for the network interface. `STACK_TYPE` must be one of: `IPV4_ONLY`, `IPV4_IPV6`, or `IPV6_ONLY` ([Preview](https://cloud.google.com/products#product-launch-stages)). The default value is `IPV4_ONLY`.

  * INTERNAL_IPV4_ADDRESS: Optional: the internal IPv4 address that you want the compute instance to use in the target subnet. Omit this flag if you don't need a specific IP address.

To specify an internal IPv6 address, use the flag `--internal-ipv6-address` instead.




### Create a TPU VM instance with an external IP address

When you create a TPU VM instance using gcloud CLI, the instance gets an ephemeral external IP address by default.

To create a TPU VM with an external IP address when using the REST API, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and include the `accessConfigs` field in the `networkInterfaces` array in the request body. If the request body doesn't specify the `accessConfigs` field, then the instance won't have external internet access.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
        "machineType":"zones/ZONE/machineTypes/MACHINE_TYPE",
        "name":"TPU_NAME",
        "disks":[
            {
                "initializeParams":{
                    "sourceImage":"projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
                },
                "boot":true
            }
        ],
        "networkInterfaces":[
            {
                "network":"global/networks/NETWORK_NAME",
                "subnetwork":"regions/REGION/subnetworks/SUBNET_NAME",
                "stackType":"STACK_TYPE",
                "accessConfigs":[
                    {
                        "name": "external-nat",
                        "type": "ONE_TO_ONE_NAT"
                    }
                ]
            }
        ],
        "scheduling": {
            "onHostMaintenance": "TERMINATE"
        }
    }
    

Replace the following placeholders:

  * PROJECT_ID: The ID of the project where you want to create the TPU VM.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * TPU_NAME: A name for the TPU VM.
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, replace the entire `"sourceImage"` value with the name of the image version in the following format: `projects/IMAGE_PROJECT/global/images/IMAGE_NAME`.

For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).

  * NETWORK_NAME: Optional: name of the network. If you specify a network, you must specify a subnet and it must belong to the same network. If you don't specify a network, Compute Engine infers the network from the subnet specified.

  * REGION: The region of the subnetwork.

  * SUBNET_NAME: Name of the subnet to use with the instance.

To view a list of subnets in the network, use the [`gcloud compute networks subnets list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list).

  * STACK_TYPE: Optional: the stack type for the network interface. `STACK_TYPE` must be one of: `IPV4_ONLY`, `IPV4_IPV6`, or `IPV6_ONLY` ([Preview](https://cloud.google.com/products#product-launch-stages)). The default value is `IPV4_ONLY`.




If you've already reserved a static external IP address, you can assign it to the instance at creation time using the [`--address` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--address) with the static IP address or the [`--network-interface` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--network-interface) for setting detailed network configuration. For more information, see [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address).

## Enable SSH access to a TPU VM instance

To enable SSH access to a TPU VM instance:

  * The TPU instance must be reachable through an external IP address or Private Google Access. 
    * If you create the TPU instance using the gcloud CLI, the instance gets an ephemeral external IP address by default. If you create the TPU instance using the REST API, you must specify that the instance should have an external IP address. For more information, see Create a TPU VM instance with an external IP address.
    * If your TPU instances don't have external IP addresses, you can configure Private Google Access. For more information, see Enable Private Google Access.
  * The network that the TPU instance uses must allow SSH traffic. The default network automatically allows SSH traffic. If you're using a custom network or you change the default network settings, you must explicitly enable SSH on the network.



### Enable Private Google Access

TPUs that don't have external IP addresses can use Private Google Access to access Google APIs and services. For more information about enabling Private Google Access, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

After you configure Private Google Access, [connect to the VM using SSH](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

### Enable SSH traffic on the network

The default network allows SSH access to all TPU VMs. If you use a custom network or change the default network settings, you need to explicitly enable SSH access by adding a firewall rule:
    
    
    gcloud compute firewall-rules create \
        --network=NETWORK allow-ssh \
        --allow=tcp:22

## Attach a custom service account

Each TPU VM has an associated service account it uses to make API requests on your behalf. TPU VMs use this service account to call Compute Engine APIs and access Cloud Storage and other services. By default, your TPU VM uses the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

For more information about service accounts, see [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts#serviceaccount).

To specify a custom service account when creating a TPU VM instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and provide the service account email and the `cloud-platform` access scope to the VM instance:
    
    
    gcloud compute instances create TPU_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --maintenance-policy=TERMINATE \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --scopes=https://www.googleapis.com/auth/cloud-platform
    

Replace the following:

  * TPU_NAME: A name for the TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).
  * SERVICE_ACCOUNT_EMAIL: The email address for the service account that you created. For example: `my-sa-123@my-project-123.iam.gserviceaccount.com`. To view the email address, see [Listing service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit#listing).



To use a service account in a different project from where you create the TPU VM, follow the instructions from [Use a cross-project service account](https://docs.cloud.google.com/tpu/docs/cross-project-sa-compute).

## Integrate with VPC Service Controls

Use VPC Service Controls to define security perimeters around your TPU resources and control the movement of data across the perimeter boundary. To learn more, see [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview). To learn about the limitations in using TPUs with VPC Service Controls, see [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
