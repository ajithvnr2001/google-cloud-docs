---
url: https://docs.cloud.google.com/vpc/docs/move-ip-address-different-project/
title: Move an external IPv4 address to a different project \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:40.271849+00:00
---

# Move an external IPv4 address to a different project  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/move-ip-address-different-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Move an external IPv4 address to a different project

Static external IPv4 addresses are associated with a Google Cloud project and can be used only within that project. However, you can move a static external IPv4 address from one project to another. The projects can be in the same organization or different organizations.

## IAM roles and permissions

To move a regional IP address, you must have the following permissions:

  * `compute.addresses.delete` in the source project
  * `compute.addresses.create` in the destination project



To move a global IP address, you must have the following permissions:

  * `compute.globalAddresses.delete` in the source project
  * `compute.globalAddresses.create` in the destination project



Example roles that include these permissions:

  * [Compute Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.admin) (`roles/compute.admin`)
  * [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Public IP Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.publicIpAdmin) (`roles/compute.publicIpAdmin`)



## Before you begin

  * Verify that the system limits for your project let you move IP addresses. See the following per-project system limits: 
    * [Address move requests per minute](https://docs.cloud.google.com/vpc/docs/quota#global-address-move-quota)
    * [Address move requests per minute per region](https://docs.cloud.google.com/vpc/docs/quota#per-region-address-move-quota)
If the system limit values are `0`, you can't move IP addresses. If you need to move IP addresses, contact your Google Cloud sales team. 
  * Verify that the project that you want to move the IP address to exists. If not, [create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in the target project.
  * Verify that the target project has enough available capacity in the appropriate quotas for the IP addresses that you're moving: 
    * For regional external IP addresses, check the [static IP addresses quota](https://docs.cloud.google.com/vpc/docs/quota#static-ip-addresses-quota).
    * For global external IP addresses, check the [static IP addresses global quota](https://docs.cloud.google.com/vpc/docs/quota#static-ip-addresses-global-quota).
  * Verify that the IP address that you want to move has the following attributes: 
    * The access type is external.
    * The IP version is IPv4.
    * The IP address is reserved (static), not ephemeral. To reserve an IP address, see [Reserve a new static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static).
    * The IP address is not in use by any resource, for example, a VM instance or a forwarding rule. To unassign an IP address, see [Unassign a static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip).
    * The IP address was not reserved by Cloud Support as part of a contiguous IP address range. For more information, see Moving an external IPv4 address fails.



## Limitations

  * If you unassign an IP address, you must wait some time before you move it:

    * For global IP addresses, wait 10 minutes.
    * For regional IP addresses, wait 20 minutes.
  * You can't change the region of a regional IP address.

  * You can't convert a global IP address to regional or a regional IP address to global.

  * You can't move [BYOIP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip) between projects.

  * You can't move IPv6 addresses between projects.




## Move an external IPv4 address to a different project

You can move a regional or global external IPv4 address from one project to another. When you move the IP address, by default the IP address resource is assigned the same name and description. However, you can choose to assign a new name or description. After the external IPv4 address is moved to a new project, you can assign it to [eligible resources](https://docs.cloud.google.com/vpc/docs/ip-addresses#external) in that project.

###  Console 

  1. In the Google Cloud console, go to **IP addresses**.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. In the **More actions** menu (more_vert) of the IP address that you want to move, select **Move to another project**.

  3. Click **Select project** , and then select the project that you want to move the IP address to.

  4. Optional: Enter a new **Name** for the IP address.

  5. Optional: Enter a new **Description** for the IP address.

  6. Click **Move**.




###  gcloud 

The command options vary depending on whether you're moving a regional or global IP address, and whether you're keeping or replacing the address name or description. The following examples describe some of these combinations.

  * Move a regional external IPv4 address to a different project:
        
        gcloud compute addresses move ADDRESS_NAME \
            --target-project=TARGET_PROJECT \
            --region=REGION
        

  * Move a regional external IPv4 address to a different project and assign it a new name and description in the new project:
        
        gcloud compute addresses move ADDRESS_NAME \
            --target-project=TARGET_PROJECT \
            --new-name=NEW_NAME \
            --description=NEW_DESCRIPTION \
            --region=REGION
        

  * Move a global external IPv4 address to a different project:
        
        gcloud compute addresses move ADDRESS_NAME \
            --target-project=TARGET_PROJECT \
            --global
        




Replace the following:

  * `ADDRESS_NAME`: the name of the IP address resource that you want to move.
  * `TARGET_PROJECT`: the name or ID of the project that you want to move the IP address to.
  * `REGION`: the region of the IP address.
  * `NEW_NAME`: a new name for the IP address resource in the new project.
  * `NEW_DESCRIPTION`: a new name for the IP address resource in the new project. If omitted, the existing description, if any, is used for the resource.



For more information, see the [`gcloud compute addresses move`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/move) reference documentation.

###  API 

The request details vary depending on whether you're moving a regional or global IP address, and whether you're keeping or replacing the address name or description. The following examples describe some of these combinations.

  * Move a regional external IPv4 address to a different project:
        
        POST https://www.googleapis.com/compute/v1/projects/SOURCE_PROJECT/regions/REGION/addresses/ADDRESS_NAME/move
        {
          "destination_address": "projects/TARGET_PROJECT/global/addresses/ADDRESS_NAME",
        }
        

  * Move a regional external IPv4 address to a different project and assign it a new name and description in the new project:
        
        POST https://www.googleapis.com/compute/v1/projects/SOURCE_PROJECT/regions/REGION/addresses/ADDRESS_NAME/move
        {
          "destination_address": "projects/TARGET_PROJECT/global/addresses/NEW_NAME",
          "description": "NEW_DESCRIPTION",
        }
        

  * Move a global external IPv4 address to a different project:
        
        POST https://www.googleapis.com/compute/v1/projects/SOURCE_PROJECT/global/addresses/ADDRESS_NAME/move
        {
          "destination_address": "projects/TARGET_PROJECT/global/addresses/ADDRESS_NAME",
        }
        




Replace the following:

  * `ADDRESS_NAME`: the name of the IP address resource that you want to move.
  * `SOURCE_PROJECT`: the name or ID of the project that you want to move the IP address to.
  * `TARGET_PROJECT`: the name or ID of the project that you want to move the IP address to.
  * `REGION`: the region of the IP address.
  * `NEW_NAME`: a new name for the IP address resource in the new project.
  * `NEW_DESCRIPTION`: a new name for the IP address resource in the new project. If omitted, the existing description, if any, is used for the resource.



## Troubleshooting

### Moving an external IPv4 address fails

You might see the following error message when you try to move an external IPv4 address:

`Invalid resource usage: 'Cannot move address that belongs to a reserved address range. Address range must be disassembled first.'`

If you see this message, it means that the IP address was reserved by Cloud Support as part of a contiguous IP address range. To move an IP address of this type, contact [Cloud Support](https://console.cloud.google.com/support?referrer=PlatformBarHelp).

To check if an IP address is part of a range that was reserved by Cloud Support, do the following:

  1. [List static external IP addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#list_ip), and then find the IP address that you want to check.
  2. Check the name of the IP address. If the IP address was reserved by Cloud Support, its name is made up of a string followed by the four bytes of the IP address, separated by hyphens. For example, if an IP address is `198.51.100.2`, and it was reserved by Cloud Support, the name has the following form: `STRING-198-51-100-2`. Other IP addresses that were reserved as part of the same range share the same string, followed by their IP addresses.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
