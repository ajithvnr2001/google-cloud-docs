---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access/
title: Best practices for controlling SSH network access \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:13.162945+00:00
---

# Best practices for controlling SSH network access  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for controlling SSH network access Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for controlling SSH network access to Linux virtual machine (VM) instances.

To connect to a VM instance using SSH, a user needs network access to the VM instance and valid SSH credentials. By default, Compute Engine [uses a firewall rule](https://docs.cloud.google.com/firewall/docs/firewalls#more_rules_default_vpc) that doesn't restrict SSH network access, but allows anybody on the internet to connect to port `22` of VM instances. While convenient for developers to get started quickly without considering network or security controls, allowing users to connect from any device, network and location bears risks:

  * Users might connect from untrusted devices or networks.
  * Bad actors might launch brute force attacks and attempt to compromise your VM instances.
  * Bad actors with access to SSH credentials that were leaked or not revoked in time can use the credentials to access and sign in to a VM from any network.



The following sections describe how you can reduce risk by limiting the networks, locations, or devices from which users can establish SSH connection to your VMs:

  * Reduce network exposure
  * Use a bastion VM if you need session recording
  * Use firewall policies and to restrict SSH exposure
  * Disable serial console access



The document focuses on practices that are either specific to Google Cloud or of particular relevance when using SSH on Google Cloud. The document doesn't cover best practices for specific SSH client or server implementations.

## Reduce network exposure

Allowing users to establish SSH connections from anywhere means that you are completely reliant on SSH authentication and authorization mechanisms to protect your VMs. You can reduce risk and establish an additional layer of protection by reducing the network exposure of VMs.

There are multiple approaches to reducing the network exposure of your VMs. To identify the approach that's best suited to your environment, you must consider a number of factors as illustrated by the following flowchart:

![Reducing the network exposure](https://docs.cloud.google.com/static/compute/docs/connect/ssh-best-practices/flowchart.svg)

  * **External access** : The first factor to consider is whether the VM only needs to be accessible within the VPC network, or whether you need the VM to be accessible externally too.

If VPC-internal access is sufficient, then you don't need to assign an external IP address to the VM, but you must still decide how to manage access.

  * **Size of the internal network:** If VPC-internal access is sufficient, then the second factor to consider is the size of your internal network.

In smaller networks, it might be sufficient to use firewall rules that allow ingress to port `22` from internal addresses to help protect your VMs. In larger networks, relying on firewall rules alone might be too limiting: In such cases, you can benefit from using [Identity-Aware Proxy TCP-forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) to enforce context-aware access to VMs.

  * **VPC Service Controls perimeter design** : The next factor to consider is whether the VM instance is part of a VPC Service Controls perimeter.

If the VM is part of a service perimeter, then any API access originating from the VM is considered to originate from within the perimeter. When you grant a user that's situated outside the perimeter SSH access to a VM inside the perimeter, they can potentially copy data from the perimeter to their local workstation, or the other way round – this can put the confidentiality and integrity of your perimeter's data at risk.

Whenever you need to grant SSH access to a VM instance that's part of a VPC Service Controls perimeter, use [IAP TCP-forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding). IAP detects whether the user's workstation is part of the same VPC Service Controls perimeter and blocks access attempts from outside the service perimeter by default. To allow external access, use [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) and configure them to [enforce context-aware access](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access).

  * **Management of client devices:** The final factor to consider is how your client devices are managed, because that determines the ways in which you can control context-aware access.

Context-aware access is most effective when [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) has access to a rich set of signals about a user, their device, and their location and therefore works in conjunction with Chrome Enterprise Premium: If you use Chrome Enterprise Premium to manage your devices, then you can set up [access levels](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels) that control access based on device posture. You can then apply this access level to SSH access by using IAP TCP-forwarding in combination with [access bindings](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis#create_an_access_binding) or [IAM conditions](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto).

If you don't control the configuration of a client device, you must consider it unmanaged and potentially untrusted.

To allow access from unmanaged devices, you can also use IAP TCP-forwarding, but you can only manage access based on user's identity and the device's IP address. Because Access Context Manager doesn't have access to any device signals, you won't be able to restrict access based on device posture.




Based on the factors and by using the flow-chart, you can identify which approach to reduce network exposure is best suited to your environment. The following sections describe these approaches in more detail.

### IAP-based SSH access

The idea of this approach is to only allow SSH access through [IAP TCP-forwarding](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview), and to let IAP control access based on the user's identity.

We recommend this approach for VM instances for which the following applies:

  * The VM instance must be accessible externally or from a large internal network.
  * The VM isn't part of a VPC Service Controls perimeter.



By default, a VM instance with an external IP address allows SSH access because default firewalls allow connections from the public internet to port 22, but this is not a recommended approach. This approach can significantly increase the risk that the VM becomes subject to attacks such as the following:

  * Usage of unrevoked credentials: Former employees whose access hasn't been fully revoked might continue to access the VM.
  * Abuse of valid credentials: Bad actors in possession of stolen or leaked credentials might use these to sign in.
  * Denial of service: Bad actors might attempt to exhaust the VM's resources by flooding it with requests.

**Important:** We don't recommend exposing SSH directly over the public internet.

A more secure way to enable external SSH access to a VM instance is to use IAP TCP-forwarding. Similar to a bastion host or reverse proxy, IAP TCP-forwarding acts as an intermediary between the client device and the VM.

IAP TCP-forwarding performs the following four functions when a user attempts to establish an SSH connection:

  * **Authentication:** IAP verifies that the user possesses a valid Google credential.
  * **Authorization:** IAP checks IAM policies to verify that the user has been granted permission to connect to the VM through IAP.
  * **Context-aware access:** Optionally, IAP can verify that the user, their device and location satisfies certain access levels.
  * **Auditing:** When data access logs are enabled, IAP logs each successful and failed attempt to connect to a VM instance.



By acting as an intermediary and performing these functions, IAP removes the need to assign a external IP address to the VM and provides an additional layer of security.

### IAP-based context-aware SSH access

The idea of this approach is to only allow SSH access through IAP TCP forwarding, and to let IAP control access based on the user's identity and additional factors.

We recommend this approach for VM instances for which the following applies:

  * The VM instance must be accessible from outside the VPC and networks that are connected to the VPC.
  * The VM isn't part of a VPC Service Controls perimeter.
  * The VM only needs to be accessible from certain devices, networks, or locations.



When you grant a user SSH access to a VM instance – whether directly or through IAP – then, by default, they can access the VM instance from any device, network and location. While convenient for users, this level of access increases risks as users might be connecting from compromised devices or untrusted networks.

To reduce risk, configure IAP TCP-forwarding so that users can only access VM instances from certain devices or locations. You can configure such context-aware access in two ways:

  * **Access bindings** : You can [create an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) and assign it to a group by using an [access binding](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis#create_an_access_binding). Access bindings are a form or identity-based policy and they apply to all resources that a user attempts to access – this includes IAP, but also other APIs and the Google Cloud console.

Using access bindings works best if you want to ensure that context-aware access is uniformly enforced across resources.

  * **IAM conditions:** You can create an access level and assign it to individual IAM role bindings by using [IAM conditions](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto).

Using IAM role bindings is a form of resource-based policy and the approach works best if you want to apply different policies to different sets of VMs.




Basic access levels let you limit access by network or geo-location. As a Chrome Enterprise Premium subscriber, you can also limit access based on other attributes such as [credential strength](https://docs.cloud.google.com/access-context-manager/docs/create-credential-strength-policy), [the configuration of the browser](https://docs.cloud.google.com/access-context-manager/docs/browser-attributes) that's used for authentication, or [device posture](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level).

### VPC Service Controls-based SSH access

The idea of this approach is to only allow SSH access through IAP TCP forwarding, and to configure the service perimeter to allow IAP ingress for certain identities our sources.

We recommend this approach for VM instances that are part of a VPC Service Controls perimeter.

Granting users external SSH access to a VM that's part of a service perimeter can be risky because it might allow users to undermine your VPC Service Controls perimeter by exfiltrating data through SSH.

By only allowing SSH access through IAP TCP-forwarding, you can reduce this risk and ensure that all SSH access is subject to the configuration of your VPC Service Controls perimeter:

  * If a user attempts to connect from outside the service perimeter (as illustrated in the previous example), IAP TCP-forwarding not only checks if the user is granted IAM access to the VM, but also checks if the request satisfies any of the [perimeter's ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).
  * If a user attempts to connect from inside the service perimeter, IAP TCP-forwarding also checks if the user is granted IAM access to the VM, but ignores VPC Service Controls ingress rules.

IAP considers a connection to originate from inside a service perimeter if any of the following applies:

    * The source IP is the external IP address of a VM that's part of the service perimeter.
    * The connection is made through Private Google Access from a VM that's part of the service perimeter.
    * The connection is made through a Private Service Connect access endpoint that's part of the service perimeter.



### Firewall-controlled internal SSH access

The idea of this approach is to disallow all external access and to only allow VPC-internal SSH access.

You can use this approach for VM instances for which the following applies:

  * The VM instance doesn't need to be accessible externally.
  * The VM is connected to a small- to medium-sized internal network.
  * The VM isn't part of a VPC Service Controls perimeter.



To disallow all external access, you can do one of the following:

  * Deploy the VM instances without an external IP address.
  * [Configure firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) so that ingress SSH traffic from IP ranges outside the VPC isn't allowed.



## Disable serial console access

To troubleshoot malfunctioning VM instances, Compute Engine lets you [connect to an instance's serial port console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#connectserialconsole) through an SSH gateway, `ssh-serialport.googleapis.com`. This gateway is publicly accessible over the internet.

The SSH gateway accesses the VM through the underlying hypervisor instead of the VPC network. Access to the serial console is therefore controlled by IAM policies and not by firewall rules.

Allowing users to access a VM serial console can unintentionally leave the VM overexposed. To prevent this over-exposure, use the `compute.disableSerialPortAccess` organizational policy constraint [to disable serial console access](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#setting_the_organization_policy_at_the_project_level), and lift the constraint temporarily when you need emergency access to the VM's serial port.

## Use a bastion VM if you need session recording

By acting as an intermediary between client devices and VMs, IAP TCP-forwarding performs functions that are commonly performed by bastion hosts or jump servers. These functions include:

  * Enforcing access policies in a centralized way
  * Auditing access



Unlike some bastion hosts, IAP TCP-forwarding doesn't terminate SSH connections: When you establish an SSH connection to a VM through IAP TCP-forwarding, the SSH connection is end-to-end encrypted between your client and the VM. As a result of this end-to-end encryption, IAP TCP-forwarding can't inspect the contents of the SSH session, and doesn't provide session recording capabilities. The IAP audit logs contain connection metadata, but don't reveal any information about the contents of the session.

If you need session recording, use a bastion VM:

  * Configure the bastion VM so that it terminates SSH connections and records its contents. Make sure to restrict the use of SSH port forwarding as it might undermine the effectiveness of session recording.
  * Set up firewall rules of target VMs so that SSH connections are only allowed from the bastion VM.
  * Allow access to the bastion VM through IAP TCP-forwarding only

**Important:** Bastion VMs that terminate SSH sessions can be a particularly attractive target for bad actors, and you must secure the VM's configuration accordingly.

## Use firewall policies to restrict SSH exposure

After you determine which way to limit SSH exposure works best for your environment, you must ensure that all VMs and projects are configured accordingly. In particular, you must ensure that all projects use a consistent set of firewall rules that determine how SSH can be used.

To apply a set of firewall rules across multiple projects, use [hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies) and apply them to folders in your [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

For example, to help enforce that all SSH access is performed through IAP TCP-forwarding, apply a firewall policy that includes the following two custom rules (in order of priority):

  1. Allow ingress from `35.235.240.0/20` to port 22 of selected VMs. `35.235.240.0/20` is the IP range used by IAP TCP-forwarding.
  2. Deny ingress from `0.0.0.0/0` to port 22 of all VMs.



## What's next

  * Continue reading about [best practices for controlling SSH login access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/credentials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
