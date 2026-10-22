---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/access-vm/
title: Access user VMs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:38.058142+00:00
---

# Access user VMs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/access-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Access user VMs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to access user VMs from a host with a VPN tunnel connection.

Hosts in the remote network with a VPN tunnel connection to a GDC organization can access the primary interface of organization user VMs, assuming egress and ingress traffic to the project containing the user VM is allowed.

## Before you begin

To configure ingress and egress traffic for a VPN tunnel, you must have the following:

  * An existing VPN tunnel. For more information, see [Create a VPN tunnel](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/configure-the-tunnel).
  * Have enabled egress and ingress traffic to the project containing the VM. For more information, see [Control ingress and egress traffic](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/vpn/egress-and-ingress).
  * The necessary identity and access roles:

    * VPN Admin: has read and write permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Admin (`vpn-admin`) role.
    * VPN Viewer: has read permissions on all VPN-related resources. Ask your Organization IAM Admin to grant you the VPN Viewer (`vpn-viewer`) role.
    * Project VirtualMachine Admin: manages VMs in the project namespace. Ask your Organization IAM Admin to grant you the Project VirtualMachine Admin (`project-vm-admin`) role.
    * For more information, see [Role definitions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-definitions).



## Access the user VM

Follow these steps to access the primary interface of the user VM:

  1. Get the interfaces of the user VM by viewing its respective `VirtualMachine` object in the org admin cluster:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER get -n PROJECT_NAME gvm VM_NAME -ojson | jq '.status.network.interfaces'
         

Replace the following:

     * `MANAGEMENT_API_SERVER`: the zonal API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `VM_NAME`: the name of the `VirtualMachine` object.

The output looks like the following example:
    
    [
        {
          "ipAddresses": [
            "172.16.19.189"
          ],
          "macAddress": "8a:fc:81:0b:41:dc",
          "name": "net1"
        }
      ]
      ```
    

  2. Hosts in the remote network with a VPN tunnel connection to a GDC organization can access user VMs through the primary `net1` interface:
         
         /home/ubuntu# ssh -i ~/vm-access user@172.16.19.189
         

Note, for SSH access details including retrieving a key for a VM, see [Connect to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
