---
url: https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance/
title: Create an instance that uses IPv6 addresses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:32.607528+00:00
---

# Create an instance that uses IPv6 addresses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an instance that uses IPv6 addresses Stay organized with collections  Save and categorize content based on your preferences. 

By default, Compute Engine instances are created with IPv4 addresses. You can optionally create compute instances that use IPv6 addresses. Compute instances that have both IPv4 and IPv6 configurations are called _dual-stack_ instances. The IPv6 address is in addition to any IPv4 addresses that are configured on the network interface.

You can configure IPv6 addresses on a Compute Engine instance if the subnet that the instance is connected to has an [IPv6 range configured](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6).

Any network interface on the compute instance can have IPv6 addresses configured. For more information about configuring multiple network interfaces, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

The stack type of an instance's network interface determines the type of [subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types) to which it can connect:

  * IPv4-only network interfaces can connect to dual-stack and IPv4-only subnets.
  * Dual-stack network interfaces can connect to dual-stack subnets.
  * IPv6-only network interfaces can connect to dual-stack and IPv6-only subnets.



Additionally, a subnet's IPv6 access type configuration determines whether the subnet has an internal or external IPv6 range. Connected instances inherit the IPv6 access type from the subnet.

You can create instances with IPv6 addresses automatically assigned by Google Cloud or with IPv6 addresses that you specify. You can specify a static IPv6 address or a custom ephemeral IPv6 address.

For more information about IPv6 addresses, see [IPv6 overview](https://docs.cloud.google.com/vpc/docs/ipv6-support).

## Limitations

  * IPv6-only instances are supported with only Debian, Red Hat, and Ubuntu OS images.



## Before you begin

  * You must [create the network and subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) prior to creating the compute instance.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create an instance with IPv6 addresses, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
  * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
  * To specify a static IP address for the VM: `compute.addresses.use` on the project
  * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
  * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
  * To set tags for the VM: `compute.instances.setTags` on the VM
  * To set labels for the VM: `compute.instances.setLabels` on the VM
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
  * To create a new disk for the VM: `compute.disks.create` on the project
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk



## Create a dual-stack instance

To create an instance with an internal IPv4 address and an external IPv6 address, connect the compute instance to a [dual-stack subnet](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

If you're using Shared VPC, and want to create a dual-stack instance that is connected to a shared subnet, see [Create an instance](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#creating_an_instance_in_a_shared_subnet) in the Shared VPC documentation.

###  Console 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. If prompted, select your project and click **Continue**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  3. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Naming resources](https://docs.cloud.google.com/compute/docs/naming-resources).
     2. Optional: In the **Zone** field, select a zone for this instance. Choose a zone in a region that contains a subnet that has an IPv6 range configured. 
     3. Select the machine family for your instance. The Google Cloud console then displays the machine series that are available for your selected machine family. The following machine family options are available:

        * **General purpose**
        * **Compute optimized**
        * **Memory optimized**
        * **Storage optimized**
        * **Network optimized**
        * **GPUs**
        * **TPUs**
     4. In the **Series** column, select the machine series for your instance.

     5. In the **Machine type** section, select the machine type for your instance.

  4. In the navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. In the **Network interfaces** section, click the network interface to expand and edit it.

     2. For **Network** and **Subnetwork** , select the network and subnetwork that has an IPv6 range configured.

     3. For **IP stack type** , select **IPv4 and IPv6 (dual-stack)**.

     4. For **Primary internal IPv4 address** , select one of the following: 

        * To assign a new ephemeral IPv4 internal address, choose **Ephemeral**.
        * To assign an existing static external IP address, choose the name of a reserved IPv4 address from the list.
        * To create and assign a new static internal IPv4 address, choose **Reserve static internal IPv4 address**.
     5. Optional: For **External IPv4 address** , select one of the following: 

        * To assign an ephemeral external IPv4 address, choose **Ephemeral**.
        * To create an instance without an external IPv4 address, choose **None**.
        * To assign an existing static external IP address, choose the name of a reserved IPv4 address from the list.
        * To create and assign a new static external IPv4 address, choose **Reserve static external IPv4 address**.
     6. Optional: To configure an external IPv6 address, for **External IPv6 address** , select one of the following: 

        * To automatically assign a new ephemeral external IPv6 address, choose **Ephemeral (Automatic)**.
        * To manually specify a new ephemeral external IPv6 address, choose **Ephemeral (Custom)**.
        * To assign an existing static external IP address, choose the name of a reserved IPv6 address from the list.
        * To create and assign a new static external IPv6 address, choose **Reserve static external IPv6 address**.
     7. To finish modifying the network interface, click **Done**.

     8. Optional: To configure an additional network interface, click **Add a network interface** and repeat the previous steps for the **Networking** pane.

  5. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  6. To create and start the instance, click **Create**.




###  gcloud 

Create an instance by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). To specify custom IPv6 addresses, include the `internal-ipv6-address` and `external-ipv6-address` flags. If not specified, ephemeral IPv6 addresses are automatically assigned to the instance by Google Cloud.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --subnet=SUBNET_NAME \
        --zone=ZONE \
        --stack-type=IPV4_IPV6
    

Replace the following:

  * `INSTANCE_NAME`: the name for the instance
  * `SUBNET_NAME`: the subnet to connect the instance to; the subnet must have an IPv6 subnet range
  * `ZONE`: the zone to deploy the instance in



###  REST 

  1. Select an [image](https://docs.cloud.google.com/compute/docs/images). Make a note of the name of the image or image family and the name of the project containing the image.
  2. Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create an instance from an image family or from a specific version of an OS image. To specify custom IPv6 addresses, include the `networkInterfaces[].ipv6Address` and `networkInterfaces[].ipv6AccessConfigs[].externalIpv6` fields. If not specified, ephemeral IPv6 addresses are automatically assigned to the instance by Google Cloud.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: ID of the project to create the instance in.
     * `ZONE`: zone to create the instance in.
     * `MACHINE_TYPE_ZONE`: if using a custom machine type, then specify the zone containing the custom machine type to use for the new instance; otherwise, specify the zone to create the instance in.
     * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-types#predefined_machine_types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), for the new instance—for example, `n4-standard-2`
     * `INSTANCE_NAME`: a name for the new instance
     * `REGION`: the region that contains the subnet
     * `SUBNET`: a dual-stack subnet
     * `IMAGE_PROJECT`: Optional: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image
     * `IMAGE`: Optional: specify one of the following:

       * A specific version of the OS image—for example, `debian-12-bookworm-v20241009`
       * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates an instance using the latest version of the OS image in the Debian 12 image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices). 

HTTP method and URL: 
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances

Request JSON body: 
    
    {
        "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
        "name": "INSTANCE_NAME",
        "networkInterfaces": [
          {
            "subnetwork": "regions/REGION/subnetworks/SUBNET",
            "stackType": "IPV4_IPV6"
          }
        ],
        "disks": [
          {
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            },
            "boot": true
          }
        ],
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#operation",
      "id": "9216044482154695709",
      "name": "operation-1739207409646-62dccc7d7bc58-d1350b42-64fdb7f7",
      "zone": "https://www.googleapis.com/compute/{api_version}/projects/`PROJECT_ID`/zones/`ZONE`",
      "operationType": "insert",
      "targetLink": "https://www.googleapis.com/compute/{api_version}/projects/`PROJECT_ID`/zones/`ZONE`/instances/`INSTANCE_NAME`",
      "targetId": "2679381553616227357",
      "status": "RUNNING",
      "user": "USER_ID",
      "progress": 0,
      "insertTime": "2025-02-10T09:10:10.551-08:00",
      "startTime": "2025-02-10T09:10:10.551-08:00",
      "selfLink": "https://www.googleapis.com/compute/{api_version}/projects/`PROJECT_ID`/zones/`ZONE`/operations/operation-1565289606387-58f9f62f5989c-e582f586-6d22f38"
     "kind": "compute#operation"
    }
    




## Create an IPv6-only instance

**Note:** The Google Cloud console doesn't support selecting the IPv6 network tier. To explicitly set external IPv6 addresses to Standard Tier ([Preview](https://cloud.google.com/products#product-launch-stages)), use the gcloud CLI or the API.

To create an IPv6-only instance, follow the steps in this section.

For a Compute Engine instance with a single network interface, the instance can have either an internal or external IPv6 address, depending on the access type of the network to which its interface is connected. You must create a custom mode Virtual Private Cloud (VPC) network with a subnet that has an IPv6 address range.

Before you can create a multi-NIC VM instance that uses both internal and external IPv6 addresses, you must create the following:

  * **The internal network and subnet** : A custom mode VPC network with IPv6 ULA enabled, a subnet with an IPv6 address range, and the access type set to `internal`.
  * **The external network and subnet** : A second custom mode VPC network, a second subnet with an IPv6 address range, and the access type set to `external`.



When you create the instance, you configure two network interfaces, one that connects to the subnet with the internal IPv6 address range and one that connects to the subnet with the external address range.

If you're using Shared VPC, and want to create an IPv6-only instance that is connected to a shared subnet, see [Create an instance](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#creating_an_instance_in_a_shared_subnet) in the Shared VPC documentation.

###  Console 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. If prompted, select your project and click **Continue**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  3. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Naming resources](https://docs.cloud.google.com/compute/docs/naming-resources).
     2. Optional: In the **Zone** field, select a zone for this instance. Choose a zone in a region that contains a subnet that has an IPv6 range configured. 
     3. Select the machine family for your instance. The Google Cloud console then displays the machine series that are available for your selected machine family. The following machine family options are available:

        * **General purpose**
        * **Compute optimized**
        * **Memory optimized**
        * **Storage optimized**
        * **Network optimized**
        * **GPUs**
        * **TPUs**
     4. In the **Series** column, select the machine series for your instance.

     5. In the **Machine type** section, select the machine type for your instance.

  4. In the navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. In the **Network interfaces** section, click the network interface to expand and edit it.

     2. For **Network** and **Subnetwork** , select the network and subnetwork that has an IPv6 range configured.

The IPv6 access type of the subnet determines whether the instance receives an internal IPv6 address or an external IPv6 address. To assign an internal IPv6 address, you must select a network that was created with the **Configure a ULA internal IPv6 range for this VPC Network** option. Otherwise, you can configure only external IPv6 addresses.

     3. For **IP stack type** , select **IPv6 (single stack)**.

     4. If you selected a subnet with an access type of `Internal`, then for **Primary internal IPv6 address** , select one of the following:

        * To automatically assign a new ephemeral internal IPv6 address, choose **Ephemeral (Automatic)**.
        * To manually specify a new ephemeral internal IPv6 address, choose **Ephemeral (Custom)**.
        * To assign an existing static internal IP address, choose the name of a reserved IPv6 address from the list.
        * To create and assign a new static internal IPv6 address, choose **Reserve static internal IPv6 address**.
     5. If you selected a subnet with an access type of `External`, then for **External IPv6 address** , select one of the following:

        * To automatically assign a new ephemeral external IPv6 address, choose **Ephemeral (Automatic)**.
        * To manually specify a new ephemeral external IPv6 address, choose **Ephemeral (Custom)**.
        * To assign an existing static external IP address, choose the name of a reserved IPv6 address from the list.
        * To create and assign a new static external IPv6 address, choose **Reserve static external IPv6 address**.
     6. To finish modifying the network interface, click **Done**.

     7. Optional: To add an additional IPv6 address, do the following:

        1. Select **Add a network interface**.
        2. Repeat the previous steps in this task for the **Networking** pane.
  5. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  6. To create and start the instance, click **Create**.




###  gcloud 

Create an instance by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). To assign both internal and external IPv6 addresses, you must create the instance with at least two network interfaces. To specify custom IPv6 addresses, include the `internal-ipv6-address` and `external-ipv6-address` flags. If not specified, ephemeral IPv6 addresses are automatically assigned to the instance by Google Cloud.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone ZONE \
        --machine-type=MACHINE_TYPE \
        --create-disk=boot=yes,image='projects/IMAGE_PROJECT/global/images/IMAGE',size=SIZE \
        --network-interface=subnet=SUBNET_INTERNAL_NAME,stack-type=IPV6_ONLY \
        --network-interface=subnet=SUBNET_EXTERNAL_NAME,stack-type=IPV6_ONLY,ipv6-network-tier=IPV6_NETWORK_TIER
    

Replace the following:

  * `INSTANCE_NAME`: a name for the instance
  * `ZONE`: the zone where the instance is created, such as `europe-west1-b`. The instance's region is inferred from the zone.
  * `MACHINE_TYPE`: Optional: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-types#predefined_machine_types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), for the new instance. For example, `n4-standard-2`.
  * `IMAGE_PROJECT`: Optional: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image
  * `IMAGE`: Optional: specify one of the following: 
    * A specific version of the OS image—for example, `debian-12-bookworm-v202410095`.
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates an instance using the latest version of the OS image in the Debian 12 image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * `SIZE`: Optional: the size of the new disk. The value must be a whole number. The default unit of measurement is GiB.
  * `SUBNET_INTERNAL_NAME`: name of the subnet that is configured for internal IP addresses to use with the instance.
  * `SUBNET_EXTERNAL_NAME`: name of the subnet that is configured for external IP addresses to use with the instance.
  * `IPV6_NETWORK_TIER`: the subnet's new network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`.



###  REST 

  1. Select an [image](https://docs.cloud.google.com/compute/docs/images). Make a note of the name of the image or image family and the name of the project containing the image.
  2. Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create an instance from an image family or from a specific version of an OS image. To specify custom IPv6 addresses, include the `networkInterfaces[].ipv6Address` and `networkInterfaces[].ipv6AccessConfigs[].externalIpv6` fields. If not specified, ephemeral IPv6 addresses are automatically assigned to the instance by Google Cloud.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: ID of the project to create the instance in.
     * `ZONE`: zone to create the instance in.
     * `MACHINE_TYPE_ZONE`: if using a custom machine type, then specify the zone containing the custom machine type to use for the new instance; otherwise,specify the zone to create the instance in.
     * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-types#predefined_machine_types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), for the new instance—for example, `n4-standard-2`.
     * `INSTANCE_NAME`: a name for the new instance
     * `REGION`: the region that contains the subnet
     * `SUBNET_INTERNAL`: an IPv6-only subnet. The network for this subnet must have an access type of `INTERNAL` and have IPv6 ULA enabled.
     * `SUBNET_EXTERNAL`: an IPv6-only subnet. The network for this subnet must have an access type of `INTERNAL`.
     * `IMAGE_PROJECT`: Optional: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image
     * `IMAGE`: Optional: specify one of the following:

       * A specific version of the OS image—for example, `debian-12-bookworm-v20241009`
       * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates an instance using the latest version of the OS image in the Debian 12 image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices). 

HTTP method and URL: 
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances

Request JSON body: 
    
    {
        "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
        "name": "INSTANCE_NAME",
        "networkInterfaces": [
          {
            "subnetwork": "regions/REGION/subnetworks/SUBNET_INTERNAL",
            "stackType": "IPV6_ONLY"
          },
          {
            "subnetwork": "regions/REGION/subnetworks/SUBNET_EXTERNAL",
            "stackType": "IPV6_ONLY"
          }
        ],
        "disks": [
          {
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
    
            },
            "boot": true
          }
        ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#operation",
      "id": "9216044482154695709",
      "name": "operation-1739207409646-62dccc7d7bc58-d1350b42-64fdb7f7",
      "zone": "https://www.googleapis.com/compute/v1/projects/`PROJECT_ID`/zones/`ZONE`",
      "operationType": "insert",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/`PROJECT_ID`/zones/`ZONE`/instances/`INSTANCE_NAME`",
      "targetId": "2679381553616227357",
      "status": "RUNNING",
      "user": "USER_ID",
      "progress": 0,
      "insertTime": "2025-02-10T09:10:10.551-08:00",
      "startTime": "2025-02-10T09:10:10.551-08:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/`PROJECT_ID`/zones/`ZONE`/operations/operation-1565289606387-58f9f62f5989c-e582f586-6d22f38"
     "kind": "compute#operation"
    }
    




## What's next

  * [Configure IPv6 addresses for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address)
  * [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
