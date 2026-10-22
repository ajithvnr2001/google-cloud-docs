---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-hub/
title: Set up NCC and create a hub \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:31.397705+00:00
---

# Set up NCC and create a hub  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Set up NCC and create a hub Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a Network Connectivity Center (NCC) hub using the hybrid inspection topology so that you can add NCC Gateway spokes and VPC spokes to the hub.

For an introduction to NCC Gateway, see the [NCC Gateway overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview).

## Before you begin

Before you get started, review the following sections.

### Create or select a project

To make it easier to configure NCC, start by identifying a valid project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. If you are using the Google Cloud CLI, set your project ID by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
         
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your unique project ID.

The gcloud CLI instructions on this page assume that you have set your project ID. 

  13. To confirm that you set the project ID correctly, use the [`gcloud config list` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/list).
         
         gcloud config list --format='text(core.project)'




### Enable the Network Connectivity API

Before you can perform _any_ tasks using NCC Gateway, you must enable the Network Connectivity API.

###  Console

To enable the Network Connectivity API, do the following:

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. Click **Enable**.




Alternatively, you can enable the API by using the [Google Cloud console API Library](https://console.cloud.google.com/apis/library?project=_), as described in [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

### Get access

To work with NCC and NCC Gateway, you need the permissions described in [Roles and permissions](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control).

### Identify resources

When you reference resources by using the gcloud CLI or the API, use the conventions described in the following table.

Convention | Supported for | Notes | Example  
---|---|---|---  
Full URI | All resources | Use one of these methods to reference Router appliance instances. | 
    
    
    "https://www.googleapis.com/compute/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
    
            
  
[Relative resource name](https://google.aip.dev/122) | All resources | 
    
    
    "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
    
          
  
Name | Regional and global resources | Use this method for hubs, spokes, VPN tunnels, and VLAN attachments. | 
    
    
     "HUB_NAME"
    
          
  
## Create an NCC hub

To create an NCC hub with the preset [hybrid inspection topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#hybrid-inspection-topology), follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click **Create hub**.

  4. Optional: choose the **Hub policy mode**.

  5. Complete the **Basic configuration** section of the form:

     1. Enter a **Hub name**.
     2. Optional: Enter a **Description**.
     3. Optional: To add a label, click **Add Item** , and then enter a **Key** and **Value**.
     4. Verify that the form displays the correct **Project ID**. If the project ID is incorrect, select a different project by using the menu at the top of the page.
  6. Optional: To enable Private Service Connect connection propagation, in the **Private Service Connect connection propagation** field, click **On**.

  7. Do one of the following:

     * If you want to create a spoke, click **Next step** and complete the spoke-creation section of the form. For instructions, see, [Create an NCC Gateway spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-spoke).
     * If you don't want to create a spoke right now, click **Create** to finish creating your new hub.



###  gcloud 

Use the [`gcloud network-connectivity hubs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create) and specify the hybrid inspection preset topology.
    
    
    gcloud beta network-connectivity hubs create HUB_NAME \
        --preset-topology=hybrid-inspection
    

Replace `HUB_NAME` with a name for the new hub.

###  API 

Use the [`projects.locations.global.hubs.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs/create).
    
    
    POST https://networkconnectivity.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/hubs
    {
      "name":"HUB_NAME",
      "description":"DESCRIPTION",
      "labels": {
        "KEY": "VALUE"
      },
      "presetTopology": "HYBRID_INSPECTION"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project that contains the new hub
  * `HUB_NAME`: the name of the new hub
  * `DESCRIPTION`: optional text that describes the hub
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text



## Connect VPC networks to the hub

The process for connecting VPC networks to a hub differs depending on whether the network and hub are in the same project.

### Connect VPC networks and hub from different projects

To connect VPC networks from different projects, use the following steps:

  * A VPC spoke administrator [proposes a VPC spoke in a different project](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke)
  * A hub administrator [reviews proposed VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes)



### Connect VPC networks and hub in the same project

If the VPC networks and hub are in the same project, do the following:

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.networks.use` on the VPC network being added to a spoke
  * `networkconnectivity.groups.use` on the hub that the spoke is being associated with
  * `networkconnectivity.spokes.create` in the project where the VPC network lives
  * `networkconnectivity.groups.create` on the hub to create a group
  * `networkconnectivity.groups.use` on the hub to create spokes associated with a group in a different project from the hub



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the VPC network being added to a spoke
  * Group User (`roles/networkconnectivity.groupUser`) on the hub that the spoke is being associated with
  * Spoke Admin (`roles/networkconnectivity.spokeAdmin`) in the project where the VPC network lives



To connect multiple VPC networks within a given project, connect a VPC network to a spoke, and connect it to a hub.

If you are creating a VPC to connect to a hub that is configured for star topology, you must get the project ID, the hub name or URI, and the group name from the hub administrator.

If you want to assign [exclude export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#exclude-export-ranges) or [include export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#include-export-ranges), use the appropriate options during spoke creation.

To create a VPC spoke, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. Click **Add spokes**.

  5. In the **Select hub** section, select the hub location as follows:

     * To attach the new spoke to a hub in the same project, select **In project` PROJECT_NAME`** and select the hub name from the list.
     * If you want to attach the new spoke to a hub in another project, select **In another project**. Enter the **Project ID** and the **Hub name** to which you want to attach your new spoke.

When you choose a hub in a different project, your spoke becomes active only when the hub administrator reviews and accepts your proposed spoke. For more details about creating spokes attached to a hub in a different project, see [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). If you are creating a VPC spoke in the same project as the hub, it is automatically accepted and activated.

  6. Enter a **Spoke name** and optionally, a **Description**.

  7. Based on the topology of the hub that you are connecting to, choose the **Spoke group** for your spoke. You can choose from the following values:

     * **Default** for a mesh topology hub
     * **Center** or **Edge** for a star topology hub. This field is required for spoke groups that use star topology
     * **Prod** , **Non-prod** , or **Services** for a hub that uses the hybrid inspection topology (only for NCC Gateway spokes)

For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).

  8. Select **VPC network** as the **Spoke type**.

  9. To add a VPC network to the spoke, select one from the **Associated VPC network** list.

  10. Optional: add a **VPC spoke filter** to customize how routes are advertised by specifying IP address ranges to [exclude or include export](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters) from the spoke to the hub. You can configure the spoke to export only subnet ranges that use private IPv4 addresses, only IPv6 subnet ranges (internal and external), or both subnet ranges that use private IPv4 addresses and internal and external IPv6 subnet ranges.

     1. **IPv4 ranges** : configure the export of IPv4 subnet ranges.

        * **Include export IPv4 subnet ranges from spoke to hub** : by default, this checkbox is selected and all subnet ranges that use private IPv4 addresses are exported.

If you don't want to export IPv4 subnet ranges, clear this checkbox.

If you only want to export specific IPv4 subnet ranges, select **Specify IPv4 ranges** and enter the address ranges that you want to export. The IPv4 subnet ranges that you specify must be private IPv4 address ranges, excluding privately used public IPv4 addresses. For more information, see [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

        * **Exclude export IPv4 subnet ranges from spoke to hub** : if the spoke exports subnet ranges and you want to exclude specific ranges from export, enter those ranges in this field.

     2. **IPv6 ranges** : configure the export of IPv6 subnet ranges (internal and external).

        * **Include export all IPv6 subnet ranges from spoke to hub** : to export all IPv6 subnet ranges to the hub, select the checkbox.

If you only want to export specific IPv6 subnet ranges, select **Specify IPv6 ranges** and enter the address ranges that you want to export.

        * **Exclude export IPv6 subnet ranges from spoke to hub** : if the spoke exports subnet ranges and you want to exclude specific ranges from export, enter those ranges in this field.

  11. Click **Done**.

  12. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a **Spoke name**.

  13. When you have finished adding spokes, click **Create**. The NCC page updates to show details about the spokes that you created.




###  gcloud 

To create a VPC spoke, use the [`gcloud network-connectivity spokes linked-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create).
    
    
    gcloud network-connectivity spokes linked-vpc-network create SPOKE_NAME \
        --hub=HUB \
        --description=DESCRIPTION \
        --vpc-network=VPC_URI \
        --include-export-ranges=[INCLUDE_EXPORT_RANGES] \
        --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES] \
        --global \
        --group=GROUP_NAME
    

Replace the following:

  * `SPOKE_NAME`: the name of the spoke that you are creating, such as `vpc-spoke1`
  * `HUB`: the hub for the spoke
  * `DESCRIPTION`: an optional description of the spoke
  * `VPC_URI`: the VPC network that this spoke points to
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. All [valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for subnet ranges, including privately used public IPv4 address ranges, are included. You can refine the list by using the `--exclude-export-ranges` flag.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which subnet IP address ranges are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `GROUP_NAME`: the group that this spoke belongs to. Supported values are:

    * `Default` for a mesh topology hub
    * `Center` or `edge` for a star topology hub. This field is required for spoke groups that use star topology
    * `Prod`, `non-prod`, or `services` for a hub that uses the hybrid inspection topology (only for NCC Gateway spokes)

For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




###  API 

To create a VPC spoke, use the [`projects.locations.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes/SPOKE_NAME
      {
        "hub":"HUB_NAME",
        "linkedVpcNetwork": {
           "uri": VPC_URI,
           "include_export_ranges": "[INCLUDE_EXPORT_RANGES]",
           "exclude_export_ranges": "[EXCLUDE_EXPORT_RANGES]",
           "group": "GROUP_NAME"
        },
      }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the new spoke.
  * `SPOKE_NAME`: the name of the new spoke.
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to.
  * `VPC_URI`: The VPC network that this spoke points to, such as `vpc_uri`.
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. All [valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for subnet ranges, including privately used public IPv4 address ranges, are included. You can refine the list by using the `--exclude-export-ranges` flag.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `include_export_ranges` for a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which subnet IP address ranges are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit `exclude_export_ranges`, NCC uses an empty list as the default exclude export ranges.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `GROUP_NAME`: the group that this spoke belongs to. Supported values are:

    * `Default` for a mesh topology hub
    * `Center` or `edge` for a star topology hub. This field is required for spoke groups that use star topology
    * `Prod`, `non-prod`, or `services` for a hub that uses the hybrid inspection topology (only for NCC Gateway spokes)

For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




[ Next Create an NCC Gateway spoke  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-spoke)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
