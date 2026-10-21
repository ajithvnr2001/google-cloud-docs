---
url: https://docs.cloud.google.com/network-tiers/docs/using-network-service-tiers/
title: Quickstart: Set the network tier \u00a0|\u00a0 Network Service Tiers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:08:36.837296+00:00
---

# Quickstart: Set the network tier  |  Network Service Tiers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-tiers/docs/using-network-service-tiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Service Tiers ](https://docs.cloud.google.com/network-tiers/docs)
  * [ Guides ](https://docs.cloud.google.com/network-tiers/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set the network tier

This page shows you how to specify a network tier for your workloads. Before manually setting a network tier, review the information in the [Network Service Tiers overview](https://docs.cloud.google.com/network-tiers/docs/overview).

## Specifications

Network Service Tiers is only supported by [eligible Google Cloud resources](https://docs.cloud.google.com/network-tiers/docs/overview#resources). Standard Tier and Premium Tier are available in every Google Cloud region.

### External IP address pools

Whether an external IP address is regional or global (and if regional, what its network tier is) determines the pool from which the IP address is chosen. IP addresses in one pool _cannot_ be moved to another.

In Standard Tier, the pool of regional external IP addresses is unique to its respective region, not to the type of eligible resource. For example, virtual machine (VM) instances and Google Cloud load balancers that use Standard Tier (external Application Load Balancers, external proxy Network Load Balancers, and regional external passthrough Network Load Balancers) all use IP addresses from the chosen region's Standard Tier pool. 

In Premium Tier, external Application Load Balancers and external proxy Network Load Balancers use global external IP addresses, while regional external passthrough Network Load Balancers and VM instances use regional external IP addresses. In each region, the pool of regional external IP addresses for Premium Tier is separate from the pool of global external IP addresses.

### Unassigned IP addresses

Unused regional external IP addresses in Standard Tier behave differently from unused IP addresses in Premium Tier. 

Standard Tier IP addresses are automatically _parked_ when they are not assigned to an eligible resource. When an IP address is parked, the load balancer answers certain requests to that IP address; for example, HTTP requests sent to a parked Standard Tier IP address are sent to a Google-hosted `HTTP 404` (Not Found) web page. Traffic sent to parked Standard Tier IP addresses is not simply dropped. In addition, Standard Tier IP addresses that are being processed for assignment to a resource can behave as if they are parked.

A Standard Tier external IP address assigned to a VM instance might be moved to a parked state during [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration) if the migration takes more than 20 minutes.

A Premium Tier external IP address assigned to a VM drops traffic during long live migrations.

## Setting the default network tier for a project

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `projects.setDefaultNetworkTier`, which requires `compute.projects.setDefaultNetworkTier` on the project.



**Roles**

  * `roles/compute.admin`



Follow these directions to define a default network tier for your project. This tier is used by newly created eligible resources in the project unless you specify a tier for the resources themselves. Changing the default network tier for a project does not change the tier for any existing resources, but it does change the network tier for any new resource if you don't specify a network tier when creating the new resource.

###  Console 

  1. In the Google Cloud console, go to the **Network Service Tiers** page.

[Go to the Network Service Tiers page](https://console.cloud.google.com/net-tier/tiers/details)

  2. Click **Change tier**.

  3. Select **Premium** or **Standard** , and then click **Change**.




###  gcloud 
    
    
    gcloud compute project-info update \
        --default-network-tier NETWORK_TIER
    

Replace `NETWORK_TIER` with `PREMIUM` or `STANDARD`. The default is `PREMIUM`.

###  API 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/setNetworkTier
    {
      "networkTier": "STANDARD"
    }
    

Replace `PROJECT_ID` with your project ID.

### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_default_network_tier) to set the network tier for a project. This example sets the tier to `STANDARD`.
    
    
    resource "google_compute_project_default_network_tier" "project-tier" {
      project      = var.project_id # Replace this with your project ID in quotes
      network_tier = "STANDARD"
    }

The network tier that you specify for a resource always takes precedence over the default network tier that you define for your project. For example, if your project's default network tier is Premium, you can still create an instance or a load balancer in Standard Tier.

[ ![Tier configuration level.](https://docs.cloud.google.com/static/network-tiers/images/tiers-resources-projects.svg)](https://docs.cloud.google.com/static/network-tiers/images/tiers-resources-projects.svg) Tier configuration level (click to enlarge).

## Creating static external IP addresses

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.addresses.insert`, which requires `compute.addresses.create` on the project and `compute.subnetworks.use` on the subnetwork.



**Roles**

  * `roles/compute.networkAdmin`



When creating a static regional external IP address, you can specify either `PREMIUM` or `STANDARD` for its network tier. If you don't specify a network tier, the address is created using the project default tier.

**Note:** Global external IP addresses and internal IP addresses are always Premium Tier.

To reserve a static regional external IP address that uses Standard Tier, do the following.

###  Console 

  1. In the Google Cloud console, go to the **External IP addresses** page.

[Go to the External IP addresses page](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve static address**.

  3. Under **Type** , select **Regional** , and then select [a region where Standard Tier is supported](https://docs.cloud.google.com/network-tiers/docs/overview#regions_supporting_standard_tier).

  4. Under **Network Service Tier** , select **Standard**.

  5. Populate [other fields](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static) as appropriate.

  6. Click **Reserve**.




###  gcloud 
    
    
    gcloud compute addresses create my-standard-tier-ip-address \
         --region REGION \
         --network-tier STANDARD
    

Replace `REGION` with the region where you are creating the regional IP address.

For other command-line flags, see [`gcloud compute` addresses](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses).

###  API 
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses
    {
      "name": "my-standard-tier-ip-address",
      "networkTier": "STANDARD"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region where you are creating the forwarding rule



### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_address) to set the network tier for a regional external IP address. This example sets the tier to `STANDARD`.
    
    
    resource "google_compute_address" "ip-address" {
      project      = var.project_id # Replace this with your project ID in quotes
      name         = "my-standard-tier-ip-address"
      region       = "us-central1"
      network_tier = "STANDARD"
    }

## Creating forwarding rules

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `forwardingRules.insert`, which requires `compute.addresses.use` if a static external IP address is to be used and `compute.*.use` on the target of the forwarding rule (instance, target pool, proxy).



**Roles**

  * `roles/compute.networkAdmin`



When creating a new forwarding rule, you can specify the network tier; the possible values are `PREMIUM` (default) and `STANDARD`. If you don't specify a network tier, the forwarding rule is created using the project default tier:

  * If you specify an external IP address with the `--address` flag, that IP address must be in the same tier that you specify for the forwarding rule.
  * If you create a forwarding rule and do not specify the `--address` flag, Google Cloud allocates an ephemeral IP address of the appropriate tier.



Standard Tier is only available for regional forwarding rules. Global forwarding rules always use Premium Tier.

A load balancer can use both Premium Tier and Standard Tier by having two different forwarding rules, one for each tier. This can be useful in scenarios where one application requires the lower latency that Premium Tier can provide, and another application, perhaps serving static content, works well with higher latency and can be in Standard Tier.

###  Console 

To create a Standard Tier forwarding rule in the Google Cloud console, you must create or update an existing load balancer. Load balancers that have backend services in more than one region cannot use Standard Tier. For instructions about choosing and creating a load balancer, see the [load balancing](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer) documentation.

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to the Load balancing page](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click the name of an existing load balancer, and then click **Edit** edit.

  3. Click **Frontend configuration**.

  4. Click **Add Frontend IP and port**.

  5. Under **Network Service Tier** , click **Standard**.

  6. Populate other fields as appropriate.

  7. Click **Done** , and then click **Update**.




###  gcloud 
    
    
    gcloud compute forwarding-rules create my-standard-tier-regional-rule \
         --load-balancing-scheme=SCHEME \
         --network-tier STANDARD \
         --address my-standard-tier-ip-address \
         --region REGION \
         --ports PORTS \
         [--target-http-proxy=TARGET_HTTP_PROXY \
         | --target-https-proxy=TARGET_HTTPS_PROXY \
         | --target-ssl-proxy=TARGET_SSL_PROXY \
         | --target-tcp-proxy=TARGET_TCP_PROXY \
         | --target-pool=TARGET_POOL \
         | --target-instance=TARGET_INSTANCE]
    

Replace the following:

  * `SCHEME`: the [load balancing scheme](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#protocol-specifications) of the load balancer
  * `REGION`: the region where you are creating the forwarding rule
  * `TARGET_HTTP_PROXY` or `TARGET_HTTPS_PROXY` or `TARGET_SSL_PROXY` or `TARGET_TCP_PROXY` or `TARGET_POOL` or `TARGET_INSTANCE`: the appropriate target for the rule, depending on which target flag you specified



For other command-line flags, see [`gcloud compute` forwarding-rules](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules).

###  API 
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules
    {
      "name": "my-standard-tier-regional-rule",
      "networkTier": "STANDARD",
        "IPAddress": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses/my-standard-tier-ip-address",
      "IPProtocol": "tcp",
        "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region where you are creating the forwarding rule
  * `TARGET_HTTP_PROXY` or `TARGET_HTTPS_PROXY` or `TARGET_SSL_PROXY` or `TARGET_TCP_PROXY` or `TARGET_POOL` or `TARGET_INSTANCE`: the appropriate target for the rule, depending on which target flag you specified



### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_forwarding_rule) to set the network tier for a forwarding rule. This example sets the tier to `STANDARD` for a forwarding rule that points to a target instance.
    
    
    resource "google_compute_forwarding_rule" "target-fr" {
      project      = var.project_id # Replace this with your project ID in quotes
      name         = "target-instance-forwarding-rule"
      region       = "us-east4"
      target       = google_compute_target_instance.target.id
      port_range   = "80"
      network_tier = "STANDARD"
    }

## VM instances

Use the procedures in the following sections to create VM instances in a given network service tier, add an access configuration to an instance, or update the network tier of an instance.

### Creating VM instances

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `instances.insert`, which requires `compute.instances.create` on the project, `compute.subnetworks.use` on the subnetwork, `compute.subnetworks.useExternalIp` on the subnetwork, and `compute.address.use` on a static external IP address, if specifying one. 



**Roles**

  * `roles/compute.instanceAdmin.v1`



When creating an instance that connects directly to the internet, you can specify the network tier. The possible values are `PREMIUM` (default) and `STANDARD`. If you don't specify a network tier, the address is created using the project default tier. The network tier is only relevant if the instance communicates directly with the internet with a regional IPv4 address. For response traffic sent by a load balancer, the forwarding rule's network tier applies.

If assigning a static external IP address by using a reserved IP address, the network tier of the IP address must match the network tier of the instance. If assigning an ephemeral external IP address, the network tier of the instance is used to assign an IP address from the corresponding pool.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Click **Management, security, disks, networking, sole tenancy**.

  4. Click the **Networking** tab.

  5. Under **Network interfaces** , on the default network interface, click **Edit** edit.

  6. Under **Network Service Tier** , select **Standard**.

  7. Populate [other fields](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) as appropriate.

  8. Click **Create**.




###  gcloud 
    
    
    gcloud compute instances create my-standard-tier-instance \
        --network-tier STANDARD
    

For other command-line flags, see [`gcloud compute` instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances).

###  API 
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "name": "my-standard-tier-instance",
      "networkInterfaces":[
       {
        "network": "global/networks/default",
        "name": "nic0",
        "accessConfigs": [
         {
         "name": "External NAT",
         "type":"ONE_TO_ONE_NAT",
         "networkTier":"STANDARD"
         }
        ]
       }
      ],
        "IPAddress": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses/my-standard-tier-ip-address",
      ... other parameters
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone where you are creating the instance
  * `REGION`: the region of the resource

For a list of other required and optional parameters, see [REST Resource: instances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances).




### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) to set the network tier for a Compute Engine VM. This example sets the tier to `STANDARD`.
    
    
    resource "google_compute_address" "ip-address" {
      project      = var.project_id # Replace this with your project ID in quotes
      name         = "my-standard-tier-ip-address"
      region       = "us-central1"
      network_tier = "STANDARD"
    }

### Adding an access configuration to an instance

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.instances.addAccessConfig`, which requires `compute.subNetworks.useExternalIp` on the subnetwork, and `compute.address.use` on a static external IP address, if specifying one. 



**Roles**

  * `roles/compute.instanceAdmin.v1`



When creating an access configuration for an instance (that is, assigning an ephemeral or static regional external IPv4 address to the network interface of an instance), you can specify a network tier for the network interface of the instance. Whether you specify an existing regional external IPv4 address or create a new address, the address and instance's network interface must use matching network service tiers. The possible values are `PREMIUM` and `STANDARD`. If you don't specify a network tier and don't specify an IP address, the instance's network interface and a new ephemeral regional external IPv4 address both use the project default tier. If you don't specify a network tier but do specify an IP address, Google Cloud returns an error if the network tier of the IP address does not match the project default tier.

###  gcloud 
    
    
    gcloud compute instances add-access-config INSTANCE_NAME \
        --network-interface INTERFACE_NAME; default="nic0" \
        --access-config-name=ACCESS_CONFIG_NAME; default="external-nat" \
        --address=IP_ADDRESS \
        --network-tier PREMIUM | STANDARD
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance
  * `INTERFACE_NAME`: the name of the interface; default is `nic0` (the name of the default interface on the instance)
  * `ACCESS_CONFIG_NAME`: the name of the access configuration for the interface
  * `IP_ADDRESS`: the URL of the IP address resource, if you are specifying an IP address

**Note:** If you do not specify a `network-tier`, the instance is created in the project default tier.

###  API 
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/addAccessConfig?networkInterface=nic0
    {
      "name": INSTANCE_NAME,
      "networkTier": "STANDARD",
      ... other parameters
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone of the instance
  * `INSTANCE_NAME`: the name of the instance



For a list of other required and optional parameters, see [REST Resource: instances](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances).

### Updating the network tier of an instance

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.instances.updateAccessConfig`, which requires `compute.subNetworks.useExternalIp` on the subnetwork, and `compute.address.use` on a static external IP address, if specifying one. 



**Roles**

  * `roles/compute.instanceAdmin.v1`



You can use the `update-access-config` command to change the network tier of the network interface of an instance. The possible values for the network tier are `PREMIUM` and `STANDARD`. If the instance is already assigned a regional external IPv4 address in the existing access config, you must first remove that external IP address before you change the interface's network tier. For more information about how the network tier of a regional external IPv4 address must match the network tier of the instance's network interface, see Adding an access configuration to an instance.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the name of an instance.

  3. Click **Edit** edit.

  4. Under **Network interfaces** , on the default network interface, click **Edit** edit.

  5. Under **Network Service Tier** , select **Standard**.

  6. Click **Save**.




###  gcloud 
    
    
    gcloud compute instances update-access-config INSTANCE_NAME \
        --network-interface nic0 \
        --network-tier STANDARD
    

Replace `INSTANCE_NAME` with the name of the instance.

###  API 
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateAccessConfig?networkInterface=nic0
    {
      "networkTier": "STANDARD",
      ... other parameters
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone of the instance
  * `INSTANCE_NAME`: the name of the instance



## Creating an instance template that uses Standard Tier

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `instanceTemplates.insert`, which requires `compute.instanceTemplates.create` on the project. 



**Roles**

  * `roles/compute.instanceAdmin.v1`



When you configure the network tier during instance template creation, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to the Instance templates page](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.

  3. Click **Management, security, disks, networking, sole tenancy**.

  4. Click the **Networking** tab.

  5. Under **Network Service Tier** , select **Standard**.

  6. Populate [other fields](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) as appropriate.

  7. Click **Create**.




###  gcloud 
    
    
    gcloud compute instance-templates create my-standard-tier-instance-template \
        --network-tier STANDARD
    

For other command-line flags, see [`gcloud compute` instance-templates](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates).

###  API 
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceTemplates
    {
      "name": "my-standard-tier-instance-template",
      "networkInterfaces[].accessConfigs[].networkTier": "STANDARD",
      ... other parameters
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone of the instance template



For a list of other required and optional parameters, see [REST Resource: instanceTemplates](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates).

### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template) to set the network tier for a Compute Engine instance template. This example sets the tier to `STANDARD`.
    
    
    resource "google_compute_instance_template" "template" {
      project      = var.project_id # Replace this with your project ID in quotes
      name         = "template"
      machine_type = "e2-medium"
      disk {
        source_image = "debian-cloud/debian-10"
        boot         = true
      }
      network_interface {
        network = "default"
        access_config {
          network_tier = "STANDARD"
        }
      }
    }

## Setting up NAT using IP addresses from a specific network tier

When you create a Cloud NAT gateway, Google Cloud lets you assign IP addresses from both Standard Tier and Premium Tier.

For more information, see [Create a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#create-nat-gateway).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
