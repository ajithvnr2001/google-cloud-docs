---
url: https://docs.cloud.google.com/vpc/docs/troubleshoot-multiple-interfaces/
title: Troubleshoot VMs with multiple network interfaces \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:15:55.886582+00:00
---

# Troubleshoot VMs with multiple network interfaces  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/troubleshoot-multiple-interfaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot VMs with multiple network interfaces

This page provides troubleshooting steps for common issues that you might encounter when creating and using VMs with multiple network interfaces.

## I can't create a VM with multiple interfaces

You may see one of the following error messages:

  * `Invalid value for field 'resource': ''. Too many network interfaces. The maximum number of network interfaces allowed for this machine type is.`

If you get this error message, you are trying to create more interfaces than the maximum interfaces supported by your instance machine type. See the [maximum number of interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces) table.

  * `Subnetwork CIDR ranges must be non-overlapping for NICs attached to a VM.`

If you get this message, the CIDR ranges associated with your VM's interfaces are overlapping. These CIDR ranges include all primary ranges of subnets associated with VM interfaces as well as secondary ranges used for [alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip). Each interface is attached to a subnet that must not overlap with subnets of other interfaces. For example, if you are trying to create your instance in region `REGION_A`, you can check subnet primary CIDR ranges using the following command or the [Google Cloud console](https://console.cloud.google.com/networking/networks/list).
        
        gcloud compute networks subnets list --regions REGION_A
        NAME                REGION      NETWORK          RANGE
        default             REGION_A  default          10.138.0.0/20
        overlapping-subnet  REGION_A  test-network     10.138.8.0/24
        

To check secondary subnet CIDR ranges, use the following command or the [Google Cloud console](https://console.cloud.google.com/networking/networks/list).
        
        gcloud compute networks subnets describe overlapping-subnet --region REGION_A
        
        
        ...
        ipCidrRange: 10.128.8.0/24
        ...
        secondaryIpRanges:
        - ipCidrRange: 10.138.8.0/24
          rangeName: conflicting-range
        

**Note:** secondary ranges present in a subnet associated with VM interface but not used by the VM interface are not checked for overlap.
  * `Multiple network interfaces are not supported on legacy networks.`

If you get this message, you are trying to create your instance in a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy). Instances with multiple interfaces are not supported with legacy networks. You can check if a network is a legacy network by using one of the following methods:

    * In the Google Cloud console, go to the [**VPC Networks** page](https://console.cloud.google.com/networking/networks/list) and check the **Mode** column.
    * Run the `gcloud compute networks list` command and check the `SUBNET_MODE` field.
  * `Required 'compute.instances.create' permission for 'projects/PROJECT_ID/zones/ZONE/instances/test-inst'`

If you get this message, the account you are logged in with doesn't have the IAM permissions that are necessary for creating an instance. For more information about the roles required for creating instances, see [Permissions, IAM, and instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces#perms-iam-instances). You can check if the IAM policy associated with your project grants you any of the following roles: `OWNER`, `EDITOR` or `compute.instanceAdmin.v1`. For creating instances in Shared VPC you would additionally need the `compute.networkUser` role. In the following example, the account `email2@gmail.com` doesn't have sufficient IAM permissions to create an instance. For more detailed instructions see the [Granting, Changing, and Revoking Access to Resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant_access) IAM guide.
        
        gcloud projects get-iam-policy PROJECT_ID
        bindings:
        - members:
          - user:email1@gmail.com
            role: roles/owner
        - members:
          - serviceAccount:our-project-123@appspot.gserviceaccount.com
          - serviceAccount:123456789012-compute@developer.gserviceaccount.com
            role: roles/editor
        - members:
          - user:email2@gmail.com
            role: roles/viewer
        etag: BwUjMhXbSPU=
        version: 1
        

You can ask your project owner or editor to either grant you a role of `OWNER`, `EDITOR`, or `compute.instanceAdmin.v1`. You would need `compute.networkUser` role as well if you are associating any interface with a subnet belonging to Shared VPC.
        
        gcloud projects set-iam_policy --member user:email2@gmail.com --role roles/editor
        




## I can't connect to a secondary interface's internal IP address

  * Check firewall rules to see that they allow connectivity to the VM secondary interface. You can check by looking at the firewall rules for the network that is attached to the secondary interface by either visiting [Google Cloud console](https://console.cloud.google.com/networking/networks/list) and clicking the appropriate VPC network or by using the following `gcloud` command.
        
        gcloud compute firewall-rules list --filter='network:NETWORK_NAME'
        

  * Check if you are trying to connect to a secondary interface from an Internet address or from outside of the secondary interface's network. You can only connect to an interface's internal IP from within its network. If you need to reach that interface from outside the network, you can assign an external IP address to your secondary interface.

  * Check if you are trying to connect to the secondary interface's internal IP from outside the subnet the secondary interface is attached to, either from another subnet of the same network or from a [peered network](https://docs.cloud.google.com/vpc/docs/vpc-peering). [Multiple Network Interfaces per instance](https://docs.cloud.google.com/vpc/docs/vpc-peering#multiple_network_interfaces_per_instance) explains the interplay between VPC Peering and VM instances with multiple interfaces. In order to reach secondary interfaces from outside the interface's subnet, you might have to configure routes on the VM. See [Specifications](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#specifications) for details on how DHCP programs default routes in the VM.

  * If you're trying to access an IPv6 address, also see I can't connect to a secondary interface's IPv6 address.




## I can't connect to a secondary interface using an external IP address

The DHCP server programs a default route only on the primary network interface of the VM. If you want to connect to the secondary interface using an external IP, there are two options. If you only need to connect outside the network on the secondary network interface, you can set a default route on that network interface. Otherwise, you can use the approach described in the tutorial, [Configure routing for an additional interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface), to configure a separate routing table using source-based policy routing in your VM.

If you're trying to access an IPv6 address, also see I can't connect to a secondary interface's IPv6 address.

## I can't connect to a secondary interface's IPv6 address

If you're trying to access an IPv6 address, check that the VM has `google-guest-agent` version [20220603.00](https://github.com/GoogleCloudPlatform/guest-agent/releases/tag/20220603.00) or later installed. For more information about managing `google-guest-agent` versions, see [Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment).

If you have an earlier version of the `google-guest-agent`, the secondary interfaces do not receive an IPv6 subnet route. We recommend that you update the guest agent so that the routes are configured correctly.

However, as a workaround, you can instead create a startup script to make the following configuration change for each secondary interface.
    
    
    sudo sysctl -w net.ipv6.conf.INTERFACE_NAME.accept_ra_rt_info_max_plen=128
    

Replace `INTERFACE_NAME` with the name of the interface—for example, `eth1` or `ens5`.

## I am having connectivity issues when using a netmask that is not /32

For information about configuring network interfaces with netmasks other than `/32`, see [Compute instance netmasks](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks).

## I can't resolve the internal hostname of a VM with multiple network interfaces

When a DNS query is executed with an internal hostname, it resolves to the primary network interface (`nic0`) of the instance.

If `nic0` is attached to a VPC network that is different from the VPC network of the instance issuing the DNS query, then the DNS query fails. Internal DNS is resolved only within a given VPC network. For more information, see [Compute Engine internal DNS](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#internal-dns).

## I get an error when deleting a Dynamic NIC by updating instance properties

In rare cases, if you delete a Dynamic Network Interface (NIC) when [updating the properties of an instance](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties), the update might fail. After failure, the instance reverts to its original state. In very rare cases, it's possible that the Dynamic NIC might remain deleted.

If you experience this issue, do the following:

  * **To resolve the issue** : use the same command or request to update instance properties again. Re-running the operation ensures that the instance reaches the state that you specified in your original request.

  * **To prevent the issue from happening again** : don't delete Dynamic NICs from an instance by updating instance properties. Instead, delete Dynamic NICs directly as described in [Delete Dynamic NICs](https://docs.cloud.google.com/vpc/docs/delete-dynamic-nics).




## I get an error when deleting a Dynamic NIC by updating MIG configurations

In rare cases, if you delete a Dynamic NIC when [updating instance configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs), the update might fail. After failure, the instances revert to their original state.

Compute Engine resolves this issue automatically by retrying the update operation until it succeeds. You can periodically [check the status of the managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances) until the last attempt error is resolved.

## Troubleshooting using the serial console

It is often a good idea to enable the serial console on a VM to debug configuration-related issues. You can enable the serial console for interactive debugging by following the steps in [Troubleshooting using the serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
