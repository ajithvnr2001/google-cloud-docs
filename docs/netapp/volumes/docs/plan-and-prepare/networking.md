---
url: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking/
title: Configure networking \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:15.225778+00:00
---

# Configure networking  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Configure networking Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure networking for Google Cloud NetApp Volumes. NetApp Volumes uses [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) to create a high throughput and low-latency data path private connection.

## Considerations

Consider the following before you begin to configure networking:

  * **VPC private connections require a one-time setup** : you must set up the private connection once per VPC. You don't need to repeat private connection setup for multiple service projects or regions.

  * **Shared VPCs** : when connecting NetApp Volumes to a Shared VPC, you must perform private services access peering in the host project that owns the Shared VPC. Contact your network administrator to set up the peering to the Shared VPC by using the instructions in Configure private services access.

  * **Assign a CIDR range** : Classless Inter-Domain Routing (CIDR) ranges let you represent IP addresses and their corresponding networks for the service to use. The service uses IP addresses from the assigned CIDR range to assign volumes to the correct protocol type, such as Network File System (NFS) or Server Message Block (SMB).

  * **Set up the private services access peering before creating your first storage pool** : if peering isn't already configured, the storage pool creation process in the Google Cloud console detects this and prompts you to set up peering using a Google Cloud console based workflow. If a peering connection to the specified VPC already exists, the Google Cloud console workflow uses it. For both manual and Google Cloud console based peering, you can either manually specify a CIDR or have Google networking pick one for you automatically.

  * **Choose a CIDR range that doesn't collide with on-premises network CIDR ranges** : if you plan to use NetApp Volumes from on-premises networks through a VPN or Cloud Interconnect, we recommend that you choose a CIDR range that doesn't collide with the CIDR ranges used in your on-premises network. If you fail to do so, it can cause IP collisions and routing issues.

  * **NetApp Volumes traffic remains within the connected VPC** : access to NetApp Volumes uses private services access, which relies on VPC peering. Because traffic can't traverse two consecutive VPC peering connections, traffic from clients to a volume or from NetApp Volumes to Active Directory servers can't leave your attached VPC. To enable network connectivity, you can [connect additional networks](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/connect-additional-networks).

  * **CIDR range modification** : when you configure private services access, you assign CIDR ranges for NetApp Volumes. After the first volume is provisioned, you can't change those CIDR ranges. You can only add additional CIDR ranges to provide more IP addresses.

To modify an existing CIDR range, complete the following steps:

    1. Delete all existing volumes.

    2. Remove the peering connection.

    3. Wait a minimum of six hours for network cleanup.

    4. Create a new peering connection using the updated CIDR range.

  * **IP address assigned to a volume can't be modified** : NetApp Volumes assigns an IP address from the delegated private service access CIDR range to volumes. You can't control which IP address a volume receives or change the IP address of an existing volume.




## Configure private services access

You can choose to set up private services access later using the UI during [storage pool creation](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/create-storage-pool) or do it manually as described in the following instructions. To learn more about private services access, see [configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

  1. **Choose a CIDR range** : NetApp Volumes uses [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) or privately used public IP (PUPI) address ranges. The Standard, Premium, Extreme, and Flex File service levels support PUPI for NFS or SMB volumes and NFS or SMB clients that access the volumes. The Flex File service level doesn't support the `6.0.0.0/8` and `7.0.0.0/8` PUPI address ranges. When you use PUPI addresses, use the Google Cloud CLI commands instead of the Google Cloud console to set up networking. For more information about why the Flex Unified service level isn't supported, see [Known limitations](https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/known-limitations#non-rfc_1918_pupi_client_ip_address_support_issues_with_flex_unified_service_level).

You can choose to have private services access automatically select an unused CIDR range or specify it manually. Manual selection lets you choose a specific address range.

Pick a CIDR range that is large enough to accommodate your volumes and pools. The minimum CIDR range you can use is `/24`. NetApp Volumes consumes subranges from the assigned CIDR range based on the service level and the following rules:

     * **Standard, Premium, and Extreme service levels** :

       * Volumes can share a single IP address, even across different storage pools, which lets multiple volumes and pools share a single `/28` subrange. Depending on the storage pool parameters such as CMEK, LDAP, and Active Directory policy, volumes might consume additional IP addresses.

       * Large capacity volumes use a `/27` subrange to support multiple storage endpoints.

       * Intercluster communication, volume migration, external replication, and FlexCache use a `/27` subrange.

       * The service assigns IP addresses to volumes from consumed subranges. If a subrange runs out of IP addresses, the service might use additional subranges, even within the same project, VPC, or region.

     * **Flex Unified service level** :

       * Each regular storage pool uses a `/28` subrange, which is shared among all of its volumes.

       * Each large capacity storage pool uses a `/26` subrange, which is shared among all of its volumes.

     * **Flex File service level** :

       * Creating the first Flex File storage pool consumes a `/28` subrange. Each pool uses one IP address for volume access and one IP address for Active Directory access.

       * Additional pools share the same `/28` subrange until 12 IP addresses are used. After this limit is reached, creating additional pools consumes a new `/28` subrange.

Different service levels can't share the same subrange allocation, with the exception of the Standard, Premium, and Extreme service levels, which can share a single subrange allocation. Volumes and pools in different regions require separate subrange allocations. The required subrange size depends on the type of pool or volume. Each service project in a Shared VPC requires its own subnet ranges for volumes or pools.

  2. **Enable the Service Networking API** : make sure that you enable the `servicenetworking.googleapis.com` API.

[Enable the API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com)

  3. **Set up private services access** : use the following instructions to set up private services access using [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud):

     1. Reserve a static internal IP address range for your CIDR:
            
            gcloud compute addresses create netapp-addresses-production-vpc1 \
             --project=PROJECT_ID \
             --global \
             --purpose=VPC_PEERING \
             --prefix-length=24 \
             --network=VPC \
             --no-user-output-enabled

Replace `PROJECT_ID` with the name of the project you intend to set up private services access in.

This command chooses the base address for the CIDR automatically. If you want to specify a specific base address, include the following line:
            
            --addresses=192.168.0.0 \

Replace `192.168.0.0` with the base address you intend to set up private services access for.

     2. Run the following command to peer the networks:
            
            gcloud services vpc-peerings connect \
               --project=PROJECT_ID \
               --service=netapp.servicenetworking.goog \
               --ranges=netapp-addresses-production-vpc1,ADDITIONAL_IP_RANGES \
               --network=VPC

Replace `PROJECT_ID` with the name of the project you intend to set up private services access in.

You can specify multiple compute address ranges as a comma-separated list for the `--ranges` flag. NetApp Volumes uses subranges from the compute address ranges in an undefined order.

Replace `ADDITIONAL_IP_RANGES` with a comma-separated list of additional address ranges to peer, or leave it empty to peer the networks only with the address range created in the previous step.

**Important:** If peering fails and you receive a `Constraint constraints/compute.restrictVpcPeering violated for project` error, it means your Google Cloud organization policies restrict peering. To resolve this, work with your organization administrator to get an exception.
     3. Enable custom route propagation. Note that NetApp Volumes creates a `sn-netapp-prod` peering when the private connection is set up.
            
            gcloud compute networks peerings update sn-netapp-prod \
                --project=PROJECT_ID \
                --network=VPC  \
                --import-custom-routes \
                --export-custom-routes

Replace `PROJECT_ID` with the name of the project you intend to set up private services access in. If you use PUPI, use the `import-subnet-routes-with-public-ip` and `export-subnet-routes-with-public-ip` parameters instead.




## What's next

Set up [IAM permissions](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
