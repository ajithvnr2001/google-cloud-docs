---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke/
title: Propose a VPC spoke in a different project \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:11.548333+00:00
---

# Propose a VPC spoke in a different project  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Propose a VPC spoke in a different project Stay organized with collections  Save and categorize content based on your preferences. 

When you create a spoke, you must associate it with a hub. If your spoke is in a different project from the hub, the hub administrator must approve your proposed spoke before it can become active. To create a VPC spoke that you want to connect to a hub in a different project, follow these steps.

For information about how to work with spokes including creating, listing, updating, and deleting spokes, see [Work with spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#working-with-spokes).

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

Before you can perform _any_ tasks using Network Connectivity Center (NCC), you must enable the Network Connectivity API.

###  Console

To enable the Network Connectivity API:

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. Click **Enable**.




Alternatively, you can enable the API by using the [Google Cloud console API Library](https://console.cloud.google.com/apis/library?project=_), as described in [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.networks.use` on the appropriate network depending on the spoke type: 
    * For VPC spokes: on the VPC network being added to a spoke
    * For producer VPC spokes: on the peered consumer VPC network
  * `networkconnectivity.groups.use` on the hub that the spoke is being associated with
  * `networkconnectivity.spokes.create` in the appropriate project depending on the spoke type: 
    * For VPC spokes: in the project where the VPC network lives
    * For producer VPC spokes: in the project where the peered consumer VPC network lives
  * `networkconnectivity.spokes.use` for producer VPC spokes only, you must have this permission on the peered consumer VPC spoke



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the appropriate network depending on the spoke type: 
    * For VPC spokes: the VPC network being added to a spoke
    * For producer VPC spokes: the peered consumer VPC network
  * Group User (`roles/networkconnectivity.groupUser`) on the hub that the spoke is being associated with
  * Spoke Admin (`roles/networkconnectivity.spokeAdmin`) in the appropriate project depending on the spoke type: 
    * For VPC spokes: in the project where the VPC network lives
    * For producer VPC spokes: in the project where the peered consumer VPC network lives



## Propose a spoke

To create a VPC spoke in the same project as the hub or in a different project, follow these steps.

If you want to assign [exclude export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#exclude-export-ranges) or [include export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#include-export-ranges), use the appropriate options during spoke creation.

Note: A hub administrator can't accept a proposed producer VPC spoke on the hub until they accept the associated VPC spoke for the peered consumer network. 

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. Click **Add spokes**.

  5. In the **Select hub** section, to attach the new spoke to a hub in another project, select the hub location as **In another project**.

  6. Enter the **Project ID** and the **Hub name** to which you want to attach your new spoke.

  7. Enter a **Spoke name** and optionally, a **Description**.

  8. If the hub that you are connecting to is configured for star topology, select or enter the **Spoke group** name for your spoke. For information about star topology, see [Star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#star-topology). For information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).

  9. For **Spoke type** , the following options are available:

     * For a hub in a different project, the default **Spoke type** is **VPC spoke**.
     * For a hub in the same project, allowed spoke types are determined by pre-existing spoke types.
     * If there are no spokes, you can select any spoke type, although the preselected option is Cloud VPN tunnel.
  10. To add a VPC network to the spoke, select the **VPC network** from the list.

  11. Optional: in the **VPC spoke filter** field, you can add a filter to customize how routes are advertised by specifying IP address ranges to [exclude or include export](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters) from the spoke to the hub. You can configure the spoke to export only subnet ranges that use private IPv4 addresses, only IPv6 subnet ranges (internal and external), or both subnet ranges that use private IPv4 addresses and internal and external IPv6 subnet ranges.

     1. **IPv4 ranges** : configure the export of IPv4 subnet ranges.

        * **Include export IPv4 subnet ranges from spoke to hub** : by default, this checkbox is selected and all subnet ranges that use private IPv4 addresses are exported.

If you don't want to export IPv4 subnet ranges, clear this checkbox.

If you only want to export specific IPv4 subnet ranges, select **Specify IPv4 ranges** and enter the address ranges that you want to export. The IPv4 subnet ranges that you specify must be private IPv4 address ranges, excluding privately used public IPv4 addresses. For more information, see [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

        * **Exclude export subnet ranges from spoke to hub** : if the spoke exports all subnet ranges that use private IPv4 addresses and you want to exclude specific ranges from export, enter those ranges in this field.

     2. **IPv6 ranges** : Configure the export of IPv6 subnet ranges.

        * **Include export all IPv6 subnet ranges from spoke to hub** : to export all internal and external IPv6 subnet ranges to the hub, select the checkbox.
  12. Click **Done**.

  13. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a **Spoke name**.

  14. When you have finished adding spokes, click **Create**. The NCC page updates to show details about the spokes that you created.

The spoke status remains `Inactive` until the hub administrator reviews and accepts your proposed spoke.




###  gcloud 

To create a VPC spoke, use the [`gcloud network-connectivity spokes linked-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create).
    
    
    gcloud network-connectivity spokes linked-vpc-network create SPOKE_NAME \
        --hub=HUB_URI \
        --global \
        --vpc-network=VPC_NETWORK \
        --include-export-ranges=[INCLUDE_EXPORT_RANGES] \
        --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES] \
        --group=GROUP_NAME
    

Replace the following:

  * `SPOKE_NAME`: a name for the spoke that you are creating.
  * `HUB_URI`: the URI of a hub in a different project that you want to create the spoke in.
  * `VPC_NETWORK`: the VPC network that this spoke provides connectivity to. The VPC network must be in the same project as the spoke.
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, CIDRs, or a combination of keywords and CIDRs that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV6_RANGES` keyword adds all IPv6 subnet ranges to the include export range list.

    * The include export ranges list supports up to 16 unique, nonoverlapping IPv4 or IPv6 CIDR ranges. No CIDR in the list can match or contain another CIDR in the list. Every current and future subnet range in the VPC spoke network that overlaps with a CIDR in the include export ranges list must fulfill one of the following conditions:

      * Exactly match a CIDR in the include export ranges list.

      * Fit within a CIDR in the include export ranges list. In this situation, a subnet range has a larger subnet mask length than the CIDR in the include export ranges list. For example, if the VPC spoke network has the 10.1.2.0/24 subnet range, 10.1.0.0/16 is a valid CIDR for the include export ranges list, but 10.1.2.0/25 is not.

    * If you omit the `INCLUDE_EXPORT_RANGES` list, NCC operates as if the include export ranges list is `[ALL_PRIVATE_IPV4_RANGES]`.

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of CIDRs that define which subnet IP address ranges are never exported to the hub.

    * The exclude ranges list supports up to 16 unique, nonoverlapping CIDRs. No CIDR in the list can match or contain another CIDR in the list.

    * Every CIDR specified in the exclude ranges list must expand to IP addresses that are fully contained by the include export ranges list.

    * If you omit the `EXCLUDE_EXPORT_RANGES` list, NCC operates as if the exclude export ranges list is empty (`[]`).

  * `GROUP_NAME`: the group this spoke belongs to. The supported values are `default` for a mesh topology hub or `center` or `edge` for a star topology hub. This field is required for spoke groups that use star topology. For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




###  API 

To create a VPC spoke, use the [`networkconnectivity.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes
      {
        "name":"SPOKE_NAME",
        "hub":"HUB_URI",
        "linkedVpcNetwork": {
           "uri": VPC_URI,
           "include_export_ranges": "[INCLUDE_EXPORT_RANGES]",
           "exclude_export_ranges": "[EXCLUDE_EXPORT_RANGES]",
           "group": "GROUP_NAME"
        },
      }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project that contains the new spoke
  * `SPOKE_NAME`: a name for the spoke that you are creating
  * `HUB_URI`: the full hub URI including the project, since the hub is in a different project from the spoke—for example, `projects/hub-project-ID/locations/global/hubs/hub-name`
  * `VPC_URI`: The VPC network that this spoke points to, such as `vpc_uri`
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, CIDRs, or a combination of keywords and CIDRs that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV6_RANGES` keyword adds all IPv6 subnet ranges to the include export range list.

    * The include export ranges list supports up to 16 unique, nonoverlapping CIDRs. No CIDR in the list can match or contain another CIDR in the list. Every current and future subnet range in the VPC spoke network that overlaps with a CIDR in the include export ranges list must fulfill one of the following conditions:

      * Exactly match a CIDR in the include export ranges list.

      * Fit within a CIDR in the include export ranges list. In this situation, a subnet range has a larger subnet mask length than the CIDR in the include export ranges list. For example, if the VPC spoke network has the 10.1.2.0/24 subnet range, 10.1.0.0/16 is a valid CIDR for the include export ranges list, but 10.1.2.0/25 is not.

    * If you omit the `INCLUDE_EXPORT_RANGES` list, NCC operates as if the include export ranges list is `[ALL_PRIVATE_IPV4_RANGES]`.

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of CIDRs that define which subnet IP address ranges are never exported to the hub.

    * The exclude ranges list supports up to 16 unique, nonoverlapping CIDRs. No CIDR in the list can match or contain another CIDR in the list.

    * Every CIDR specified in the exclude ranges list must expand to IP addresses that are fully contained by the include export ranges list.

    * If you omit the `EXCLUDE_EXPORT_RANGES` list, NCC operates as if the exclude export ranges list is empty (`[]`).

  * `GROUP_NAME`: the group that this spoke belongs to—for example, `center` or `edge`. This field is required for spoke groups that use star topology. For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions to common issues, see [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
