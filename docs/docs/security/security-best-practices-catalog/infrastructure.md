---
url: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure/
title: Infrastructure controls \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:38.176317+00:00
---

# Infrastructure controls  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Infrastructure controls Stay organized with collections  Save and categorize content based on your preferences. 

This document includes the best practices and guidelines for Google Cloud services such as Compute Engine, Google Kubernetes Engine (GKE), Pub/Sub, Dataflow, and Cloud Run functions when running workloads on Google Cloud.

## Compute controls

These controls apply to compute services.

### Define VM instances that can enable IP forwarding

Google control ID | VPC-CO-6.3  
---|---  
Implementation | Required  
Description | The `compute.vmCanIpForward` constraint defines the VM instances that can enable IP forwarding. By default, any VM can enable IP forwarding in any virtual network. Specify VM instances using one of the following formats: 

  * `under:organizations/ORGANIZATION_ID`
  * `under:folders/FOLDER_ID`
  * `under:projects/PROJECT_ID`
  * `projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME`.

This constraint isn't retroactive.  
Applicable products | 

  * Organization Policy Service
  * Virtual Private Cloud (VPC)
  * Compute Engine

  
Path | `constraints/compute.vmCanIpForward`  
Operator | =  
Value |  `Your list of VM instances that can enable IP forwarding.`  
Type | List  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Recommendations](https://docs.cloud.google.com/vpc-service-controls/docs/enable-internal-ip-access#recommendations)
  * [Enable IP forwarding for instances](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward)

  
  
### Disable VM-nested virtualization

Google control ID | VPC-CO-6.6  
---|---  
Implementation | Required  
Description | The `compute.disableNestedVirtualization` boolean constraint disables hardware-accelerated nested virtualization for Compute Engine VMs.  
Applicable products | 

  * Organization Policy Service
  * Virtual Private Cloud (VPC)
  * Compute Engine

  
Path | `constraints/compute.disableNestedVirtualization`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Manage the nested virtualization constraint](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint)

  
  
### Restrict external IP addresses on VMs

Google control ID | VPC-CO-6.2  
---|---  
Implementation | Required  
Description | Unless needed, prevent the creation of Compute Engine instances with public IP addresses. The `compute.vmExternalIpAccess` list constraint defines the set of Compute Engine VM instances that can have external IP addresses.Prevent Compute Engine instances from having external IP addresses to drastically reduce their exposure to the internet. Any instance with an external IP address is immediately discoverable and becomes a direct target for automated scans, brute-force attacks, and attempts to exploit vulnerabilities. Instead, require instances to use private IP addresses and manage access through controlled, authenticated, and logged pathways like the Identity-Aware Proxy (IAP) tunnel or a bastion host.Adopting this deny-by-default posture is a foundational security best practice that helps minimize your attack surface and enforces a zero-trust approach to your network. This constraint isn't retroactive.  
Applicable products | 

  * Organization Policy Service
  * Virtual Private Cloud (VPC)
  * Compute Engine

  
Path | `constraints/compute.vmExternalIpAccess`  
Operator | =  
Value |  `The list of VM instances in your organization that can have external IP addresses.`  
Type | List  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Restrict external IP addresses to specific instances](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip)
  * [View the network configuration for an instance](https://docs.cloud.google.com/compute/docs/instances/view-network-properties)

  
  
### Define permitted external IP addresses for VM instances

Google control ID | CBD-CO-6.3  
---|---  
Implementation | Required  
Description | The `compute.vmExternalIpAccess` list constraint lets you restrict external access to virtual machines by not assigning external IP addresses. Configure this list constraint to deny all external IP addresses to virtual machines.  
Applicable products | 

  * Organization Policy Service
  * Compute Engine

  
Path | `compute.vmExternalIpAccess`  
Operator | =  
Value |  `Deny All`  
Type | List  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.PT-3.1
  * PR-PT-4.1

  
Related information | 

  * [Restrict external IP addresses to specific instances](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip)

  
  
### Disable VM serial port access

Implementation | Required  
---|---  
Description | Turn off serial port access by setting the `compute.disableSerialPortAccess` organization policy constraint. Disable serial port access on your Compute Engine VMs to help eliminate an access channel that bypasses your firewall rules and other network security controls. The interactive serial console is primarily intended for emergency troubleshooting, but, when you leave it enabled, you can create a persistent backdoor that can be targeted by attackers.Disabling serial port access helps enforces a defense-in-depth security posture by forcing all administrative access through standard, audited pathways like SSH, which you can protect by enabling Identity and Access Management (IAM) and Identity-Aware Proxy (IAP).  
Applicable products |  Compute Engine  
Path | `constraints/compute.disableSerialPortAccess`  
Operator | =  
Value |  `True`  
Related NIST-800-53 controls | 

  * AC-3

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Disabling interactive serial console access through Organization Policy Service](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#disabling_interactive_serial_console_access_through_organization_policy)

  
  
### Require VPC connector for Cloud Run functions

Google control ID | CF-CO-4.4  
---|---  
Implementation | Required  
Description | The `cloudfunctions.requireVPCConnector` boolean constraint requires that administrators specify a Serverless VPC Access connector when they deploy a Cloud Run function. When enforced, functions must specify a connector.  
Applicable products | 

  * Organization Policy Service
  * Cloud Run functions

  
Path | `constraints/cloudfunctions.requireVPCConnector`  
Operator | =  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Connect to a VPC network](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access)

  
  
### Enable Shielded VM features

Implementation | Required  
---|---  
Description | Turn on the virtual trusted platform module (vTPM) and integrity monitoring attributes of Shielded VM for your instances. vTPM and integrity monitoring attributes are part of the default VM instance creation process. Use the vTPM and integrity monitoring attributes of Shielded VM to help ensure that your VMs boot only with trusted, unmodified code.The vTPM provides a secure, virtual cryptoprocessor that generates and stores cryptographic measurements of the entire boot sequence, from the UEFI firmware to the kernel drivers. Integrity monitoring then continuously compares these runtime measurements against a known-good baseline established when the VM was first created.These features provide a verifiable chain of trust and automatically alert you or take action if they detect any malicious modifications, like those from a bootkit or rootkit. Shielded VM features help to maintain your workload's integrity from the moment that the instance powers on.  
Applicable products |  Compute Engine  
Path | `compute.instances/shieldedInstanceConfig.enableVtpm`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SI-7

  
Related CRI profile controls | 

  * PR.DS-6.1

  
Related information | 

  * [Shielded VM overview](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)

  
  
### Enforce OS Login for VMs

Implementation | Required  
---|---  
Description | If you let developers access Compute Engine resources using SSH, configure OS Login with 2-step verification. Use OS Login to manage SSH keys with Identity and Access Management (IAM) policies by setting the `compute.requireOsLogin` organization policy constraint. OS Login centralizes VM access by tying SSH permissions to a user's Google identity and IAM roles, eliminating the need to manage individual SSH keys on each machine.Tying SSH permissions to a user's identity is crucial for security because removing a user's IAM role instantly revokes their access across all instances, protecting against unauthorized entry from stale accounts. The system simplifies key management to help prevent key sprawl and provides a clear, centralized audit trail for all login events in Cloud Audit Logs. OS Login also lets you enforce two-factor authentication, adding a critical layer of protection against stolen SSH keys and credentials. An attacker with compromised OAuth tokens but no password or security key is blocked by this feature. Remote Desktop Protocol (RDP) access to Windows instances on Compute Engine doesn't support the OS Login service, so 2-step verification can't be granularly enforced for RDP sessions. When using IAP Desktop or Google Chrome-based RDP plugins, set coarse-grained controls like session length for Google services and 2-step verification settings for the user's web sessions and disable the **Allow user to trust the device** setting under 2-step verification.  
Applicable products |  Compute Engine  
Path | `compute.projects/commonInstanceMetadata.items`  
Operator | Is  
Value |  `enable-oslogin=TRUE`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-2

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin)

  
  
### Configure trusted image policies

Implementation | Recommended  
---|---  
Description | The `compute.trustedImageProjects` list constraint lets you define which projects can store images and persistent disks. Ensure that only trusted and maintained images exist in those projects.  
Applicable products | 

  * Organization Policy Service
  * Compute Engine

  
Path | `compute.trustedImageProjects`  
Operator | =  
Type | List  
Related NIST-800-53 controls | 

  * CM-7
  * CM-2
  * SI-7
  * SA-10
  * AC-3

  
Related CRI profile controls | 

  * PR.IP-1.1
  * PR.IP-1.2
  * PR.DS-6.1
  * PR.PT-3.1
  * ID.SC-2.1

  
Related information | 

  * [Setting up trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access)

  
  
### Use Patch to upgrade VM instances

Implementation | Recommended  
---|---  
Description | If supported, use Patch to apply operating system patches to Compute Engine VM instances. Patch lets you apply regular security patches and kernel updates.To update a Windows Server OS, you can complete an in-place upgrade.  
Applicable products |  Compute Engine  
Related NIST-800-53 controls | 

  * SI-2
  * CM-3
  * CM-8
  * RA-5
  * MA-2

  
Related CRI profile controls | 

  * PR.IP-12.1
  * PR.IP-12.2
  * PR.MA-1.1
  * PR.MA-1.2
  * PR.IP-1.4
  * PR.IP-3.1

  
Related information | 

  * [About Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch)
  * [Performing an in-place upgrade of Windows Server](https://docs.cloud.google.com/compute/docs/tutorials/performing-in-place-upgrade-windows-server)

  
  
### Configure message storage policies

Google control ID | PS-CO-4.1  
---|---  
Implementation | Optional  
Description | If you publish messages to the global Pub/Sub endpoint, Pub/Sub automatically stores the messages in the nearest Google Cloud region. To control which regions your messages are stored in, configure a message storage policy on your topic. Use one of the following ways to configure message storage policies for topics: 

  * Set a message storage policy using the Resource Location Restriction (`gcp.resourceLocations`) organization policy constraint.
  * Configure a message storage policy when creating a topic. For example: `gcloud pubsub topics create TOPIC_ID \--message-storage-policy-allowed-regions=REGION1, REGION2`

  
Applicable products | 

  * Organization Policy Service
  * Pub/Sub

  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Configure message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction)

  
  
### Turn off external IP addresses for Dataflow jobs

Google control ID | DF-CO-6.1  
---|---  
Implementation | Optional  
Description | Turn off external IP addresses for administrative and monitoring tasks that are related to Dataflow jobs. Instead, configure access to your Dataflow worker VMs using SSH.Enable Private Google Access and specify one of the following options in your Dataflow job:

  * `--usePublicIps=false` and `--network=NETWORK-NAME`
  * `--subnetwork=SUBNETWORK-NAME`

Where:

  * `NETWORK-NAME`: The name of your Compute Engine network.
  * `SUBNETWORK-NAME`: The name of your Compute Engine subnetwork.

  
Applicable products | 

  * Compute Engine
  * Dataflow

  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Choose an access method](https://docs.cloud.google.com/compute/docs/instances/access-overview)
  * [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access)

  
  
### Use network tags for firewall rules

Google control ID | DF-CO-6.2  
---|---  
Implementation | Optional  
Description | Network tags are text attributes that attach to Compute Engine VMs such as Dataflow worker VMs. Network tags let you make VPC network firewall rules and some custom static routes applicable to specific VM instances. Dataflow supports adding network tags to all worker VMs that run a particular Dataflow job.  
Applicable products | 

  * Compute Engine
  * Dataflow

  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Network tags for Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall#specifying_network_tags)

  
  
## Container controls

These controls apply to containers within GKE.

### Restrict control plane access

Google control ID | GKE-CO-1.1  
---|---  
Implementation | Required  
Description | By default, the Google Kubernetes Engine (GKE) cluster control plane and nodes have internet routable addresses that can be accessed from any IP address. Restrict network access to the control plane by using a DNS-based endpoint and by creating private clusters. The control plane is the management center for a Kubernetes cluster, and exposing it to the internet makes it a prime target for attackers. This configuration makes the control plane private and removes it from the internet.Restricting control plane access helps ensure that only trusted devices within your organization's private network can manage the cluster, drastically reducing the risk of an external attack.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * SC-7

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work)
  * [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)
  * [Creating a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/legacy/network-isolation)

  
  
### Use least-privilege firewall rules

Google control ID | GKE-CO-1.2  
---|---  
Implementation | Required  
Description | When you create firewall rules, use the principle of least privilege to provide access only for the required purpose. Ensure that your firewall rules don't conflict with the GKE default firewall rules when possible.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * AC-3
  * AC-4
  * AC-17
  * SC-7

  
Related information | 

  * [Automatically created firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules)

  
  
### Use Google Groups for RBAC

Google control ID | GKE-CO-1.3  
---|---  
Implementation | Required  
Description | Use Google Groups for role-based access control (RBAC), which also lets you integrate with your existing user account management practices, such as revoking access when someone leaves your organization. Google Groups for RBAC helps provide efficient management of cluster access using Identity and Access Management (IAM) and Google Groups, which is suitable for most organizations that use Google Groups.  
Applicable products |  Google Kubernetes Engine (GKE)  
Related NIST-800-53 controls | 

  * AC-2

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac)

  
  
### Enable Shielded GKE Nodes

Google control ID | GKE-CO-1.4  
---|---  
Implementation | Required  
Description | Enable Shielded GKE Nodes for cryptographic verification of the nodes in your cluster. Shielded GKE Nodes provide strong, verifiable node identity and integrity. Enable Shielded GKE Nodes when creating or updating clusters. Where possible, use Shielded GKE Nodes with secure boot to also authenticate the boot components of your node VMs during the boot process. Don't use secure boot if you need third-party unsigned kernel modules.Shielded GKE Nodes is enabled by default when you create a cluster.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * AC-3
  * AC-4
  * AC-17
  * SC-7

  
Related information | 

  * [Using Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes)

  
  
### Use Container-Optimized OS with containerd runtime

Google control ID | GKE-CO-1.5  
---|---  
Implementation | Required  
Description | Use Container-Optimized OS to implement a hardened and managed container OS. General-purpose operating systems include many extra programs that aren't needed to run containers and therefore create a larger, unnecessary target for attackers. Container-Optimized OS is a minimal, locked-down operating system that significantly reduces this attack surface by including only what is necessary. As a managed OS, Container-Optimized OS also has security patches that are automatically applied by Google, which help ensure critical vulnerabilities are fixed and reduces your operational workload.An image that includes Container-Optimized OS with containerd (cos_containerd) has containerd as the main container runtime directly integrated with Kubernetes. containerd is the core runtime component of Docker and is designed to deliver core container functionality for the Kubernetes Container Runtime Interface (CRI). It is significantly less complex than the full Docker daemon, and therefore has a smaller attack surface.  
Applicable products |  Container-Optimized OS  
Related NIST-800-53 controls | 

  * CM-7
  * SC-7
  * SC-38
  * SI-2
  * SI-7

  
Related CRI profile controls | 

  * PR.PT-3.1

  
Related information | 

  * [Container-Optimized OS overview](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits)

  
  
### Use Workload Identity Federation for GKE

Google control ID | GKE-CO-1.6  
---|---  
Implementation | Required  
Description | Use Workload Identity Federation for GKE to securely authenticate to Google Cloud APIs from Google Kubernetes Engine (GKE) workloads. Workload Identity Federation for GKE provides a simpler and safer alternative to using service account keys.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * IA-2

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

  
  
### Enable GKE Sandbox

Google control ID | GKE-CO-1.7  
---|---  
Implementation | Required  
Description | Use GKE Sandbox to provide an extra layer of security to help prevent untrusted code from affecting the host kernel on your Google Kubernetes Engine (GKE) cluster nodes. GKE Sandbox enhances workload isolation for untrusted or sensitive workloads, providing an additional layer of protection against container escape attacks.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * SC-39

  
Related CRI profile controls | 

  * PR.DS-1.1

  
Related information | 

  * [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)

  
  
### Disable the kubelet read-only port

Google control ID | GKE-CO-1.9  
---|---  
Implementation | Required  
Description | Disable kubelet read-only port 10255 and use the more secure port 10250 instead. Kubernetes doesn't perform any authentication or authorization checks on this port. The kubelet serves the same endpoints on the more secure, authenticated port 10250.You can only disable the insecure kubelet read-only port in GKE version 1.26.4-gke.500 or later.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * AC-3
  * SC-7

  
Related information | 

  * [Disable the kubelet read-only port in GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port)

  
  
### Use namespace and RBAC to restrict access to cluster resources

Google control ID | GKE-CO-1.10  
---|---  
Implementation | Required  
Description | Create separate namespaces or clusters for each team and environment to implement least-privilege access to Kubernetes. Assign cost centers and appropriate labels to each namespace for accountability and chargeback. Only give developers the level of access to their namespace that they need to deploy and manage their application, especially in production. Map out the tasks that your users need to undertake against the cluster and define the permissions that they require to do each task.Assign the appropriate Identity and Access Management (IAM) roles for Google Kubernetes Engine (GKE) to groups and users to provide permissions at the project level and use RBAC to grant permissions on a cluster and namespace level.  
Applicable products | 

  * GKE
  * IAM

  
Related NIST-800-53 controls | 

  * AC-3
  * AC-4
  * AC-6

  
Related information | 

  * [Create IAM allow policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam)

  
  
### Restrict traffic among pods

Google control ID | GKE-CO-1.11  
---|---  
Implementation | Required  
Description | By default, all pods in a cluster can communicate with each other. Control pod-to-pod communication as needed for your workloads. Restricting network access to services makes it much more difficult for attackers to move laterally within your cluster, and also offers services some protection against accidental or deliberate denial of service.There are two ways to control traffic:

  * Use Cloud Service Mesh or Istio for load balancing, service authorization, throttling, quota, metrics and more.
  * Use Kubernetes network policies. Choose this option if you're looking for the basic access control functionality that's exposed by Kubernetes.

  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * AC-3
  * AC-4
  * SC-7

  
Related information | 

  * [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview)
  * [Istio](https://istio.io/)
  * [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

  
  
### Use admission controllers to enforce policies

Google control ID | GKE-CO-1.12  
---|---  
Implementation | Required  
Description | Admission controllers are plugins that govern and enforce how the cluster is used. Enable them to use some of the more advanced security features of Kubernetes because they are an important part of the defense in depth approach to hardening your cluster. By default, pods in Kubernetes can operate with capabilities beyond what they require. Use admission controls to restrict the pod's capabilities to only those that are required for that workload.GKE supports numerous controls for restricting your pods to execute with capabilities that are explicitly granted. For example, Policy Controller is available for clusters in fleets. Kubernetes also has the built-in PodSecurity admission controller that lets you enforce the Pod Security Standards in individual clusters. Policy Controller is a feature of GKE that lets you enforce and validate security on GKE clusters at scale by using declarative policies.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * CM-2
  * CM-3
  * CM-6
  * CM-7

  
Related information | 

  * [A Guide to Kubernetes Admission Controllers](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/)
  * [Policy Controller overview](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)
  * [Apply predefined Pod-level security policies using PodSecurity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission)

  
  
### Restrict the ability for workloads to self-modify

Google control ID | GKE-CO-1.13  
---|---  
Implementation | Required  
Description | Certain Kubernetes workloads, especially system workloads, have permission to self-modify. For example, some workloads vertically autoscale themselves. While convenient, self-modification can allow an attacker who has already compromised a node to escalate further in the cluster. For example, an attacker could have a workload on the node change itself to run as a more privileged service account that exists in the same namespace.Don't grant workloads the permission to modify themselves by default. When self-modification is necessary, limit permissions by applying Gatekeeper or Policy Controller constraints, such as NoUpdateServiceAccount from the open source Gatekeeper library, which provides several useful security policies.When you deploy policies, allow the controllers that manage the cluster lifecycle to bypass the policies. Controllers must make changes to the cluster, such as applying cluster upgrades. For example, if you deploy the NoUpdateServiceAccount policy on GKE, you must set the following parameters in the constraint:`parameters:`` allowedGroups:`` - system:masters`` allowedUsers:`` - system:addon-manager`  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * AC-3
  * CM-3
  * SI-7

  
Related information | 

  * [Policy Controller overview](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)
  * [NoUpdateServiceAccount](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library#noupdateserviceaccount)

  
  
### Monitor your cluster configurations

Google control ID | GKE-CO-1.14  
---|---  
Implementation | Required  
Description | Audit your cluster configurations for deviations from your defined settings. Settings covered in these best practices, as well as other common misconfigurations, can be automatically checked using Security Command Center.  
Applicable products | 

  * GKE
  * Security Command Center

  
Related NIST-800-53 controls | 

  * SI-4
  * SI-5
  * RA-5

  
Related information | 

  * [Security Command Center overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)
  * [CIS GKE 1.7](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#cis-gke-1-7)

  
  
### Enforce Binary Authorization

Google control ID | BIN-CO-1.1  
---|---  
Implementation | Required  
Description | Use Binary Authorization to make sure trusted images are deployed to Google Kubernetes Engine (GKE) and Cloud Run. Binary Authorization helps ensure that only verified and trusted container images can be deployed in your clusters, strengthening software supply chain security.  
Applicable products | 

  * GKE
  * Binary Authorization
  * Cloud Run

  
Path | `constraints/binaryauthorization.requireBinauthz`  
Operator | ==  
Value |  `True`  
Related NIST-800-53 controls | 

  * SI-7

  
Related CRI profile controls | 

  * PR.DS-6.1

  
Related information | 

  * [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview)

  
  
### Use GKE Autopilot

Implementation | Required  
---|---  
Description | Use Google Kubernetes Engine (GKE) Autopilot clusters. Autopilot clusters offer robust security measures, with many security best practices for container or GKE enabled by default.  
Applicable products |  GKE  
Path | `container.clusters/autopilot.enabled`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * CM-2

  
Related CRI profile controls | 

  * PR.IP-1.1

  
Related information | 

  * [GKE Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

  
  
### Use least privilege accounts for GKE clusters and nodes

Implementation | Required  
---|---  
Description | Use least-privilege Identity and Access Management (IAM) service accounts for Google Kubernetes Engine (GKE) clusters and nodes. Access to the GKE control plane is restricted to a single DNS-based endpoint. Implementing least privilege significantly reduces the attack surface without the need for additional firewall rules or bastion hosts.  
Applicable products |  GKE  
Path | `container.clusters/nodeConfig.serviceAccount`  
Operator | !=  
Value |  `default`  
Type | String  
Related NIST-800-53 controls | 

  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1

  
Related information | 

  * [Harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)

  
  
### Use private GKE nodes

Implementation | Required  
---|---  
Description | Create private nodes to reduce internet exposure. Private Google Kubernetes Engine (GKE) nodes help reduce internet exposure by ensuring GKE nodes don't have a public IP address.  
Applicable products |  GKE  
Path | `container.clusters/networkConfig.defaultEnablePrivateNodes`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SC-7

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)

  
  
### Use Confidential Google Kubernetes Engine Nodes

Implementation | Required  
---|---  
Description | Use Confidential GKE Nodes to enforce encryption of data in-use in your nodes and workloads. Confidential GKE Nodes help secure highly sensitive workloads by encrypting data in use through confidential computing.  
Applicable products |  Google Kubernetes Engine (GKE)  
Path | `container.clusters/confidentialNodes.enabled`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SC-28

  
Related CRI profile controls | 

  * PR.DS-1.1

  
Related information | 

  * [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)

  
  
### Run a custom certificate authority in GKE

Implementation | Required  
---|---  
Description | Run your own certificate authorities to manage keys within Google Kubernetes Engine (GKE). Using your own certificate authorities offers greater control over cryptographic operations. To request access to this feature, contact your Google Cloud account team.  
Applicable products |  GKE  
Path | `container.clusters/userManagedKeysConfig.clusterCa`  
Operator | Is set  
Type | String  
Related NIST-800-53 controls | 

  * SC-12

  
Related CRI profile controls | 

  * PR.DS-1.1

  
Related information | 

  * [Run your own certificate authorities and keys in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys)

  
  
### Encrypt Kubernetes Secrets using Cloud KMS

Implementation | Required  
---|---  
Description | Encrypt Kubernetes Secrets at rest using Cloud Key Management Service (Cloud KMS) managed keys. Cloud KMS provides an additional layer of security for etcd data by letting you encrypt Kubernetes Secrets with a key that you own and manage.  
Applicable products | 

  * GKE
  * Cloud KMS

  
Path | `container.clusters/databaseEncryption.keyName`  
Operator | Is set  
Type | String  
Related NIST-800-53 controls | 

  * SC-28

  
Related CRI profile controls | 

  * PR.DS-1.1

  
Related information | 

  * [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets)

  
  
### Use CMEK for node boot disks

Implementation | Required  
---|---  
Description | Use customer-managed encryption keys (CMEK) for node boot disk encryption. CMEK lets you encrypt a Kubernetes node's boot disk with a key that you own and manage.  
Applicable products | 

  * Cloud Key Management Service
  * GKE

  
Path | `container.clusters/nodeConfig.bootDiskKmsKey`  
Operator | Is set  
Type | String  
Related NIST-800-53 controls | 

  * SC-28

  
Related CRI profile controls | 

  * PR.DS-1.1

  
Related information | 

  * [Use CMEK-protected node boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek#boot-disks)

  
  
### Keep GKE clusters up to date

Implementation | Required  
---|---  
Description | Use node auto-upgrades and maintenance windows to get the latest fixes for your Google Kubernetes Engine (GKE) nodes. Auto-upgrades provide an automatic way to keep your nodes up to date. Maintenance windows permit upgrades to occur during a repeating window of time.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * SI-2
  * SI-2(1)
  * CM-7

  
Related CRI profile controls | 

  * PR.IP-12.4
  * PR.PT-3.1
  * PR.IP-1.4

  
Related information | 

  * [Auto-upgrading nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades)
  * [Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)

  
  
### Use base images

Implementation | Recommended  
---|---  
Description | In Google Kubernetes Engine (GKE), ensure that your containers use base images, which are regularly updated with security patches.Also, consider distroless container images that include only your application and its runtime dependencies.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * SC-28

  
Related CRI profile controls | 

  * PR.DS-1.1

  
Related information | 

  * [Base images](https://docs.cloud.google.com/software-supply-chain-security/docs/base-images)
  * [Distroless container images](https://github.com/GoogleContainerTools/distroless)

  
  
### Scan containers for vulnerabilities

Implementation | Recommended  
---|---  
Description | Use Artifact Analysis to check for vulnerabilities in the container images that you store in Artifact Registry or Container Registry.  
Applicable products |  GKE  
Related NIST-800-53 controls | 

  * RA-5
  * SI-2
  * SA-11
  * SI-7
  * CA-7

  
Related CRI profile controls | 

  * DE.CM-8.1
  * DE.CM-8.2
  * ID.RA-1.1
  * ID.RA-3.1
  * PR.IP-12.1
  * PR.IP-12.2

  
Related information | 

  * [Container scanning overview](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview)

  
  
## VMware Engine controls

### Limit Admin role assignments for VMware Engine

Google control ID | GCVE-CO-3.1  
---|---  
Implementation | Required  
Description | Only grant Admin roles to the service accounts that deploy and configure Google Cloud VMware Engine private clouds and to a limited number of administrators. Typically, the manual addition or deletion of clusters and nodes is an action that doesn't happen frequently and might have a high impact on billing or the availability of the cluster.Make sure to regularly audit who has been assigned the VMware Engine Service Admin role, either directly on the project that's used for VMware Engine or on one of the parent levels of the resource hierarchy. This audit should include other roles, like the basic Editor and Owner roles that include critical permissions related to VMware Engine. You can use services like the IAM roles recommender to help identify overly privileged roles.  
Applicable products | 

  * VMware Engine
  * IAM

  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1

  
Related information | 

  * [VMware Engine IAM roles and permissions](https://docs.cloud.google.com/vmware-engine/docs/iam#vmware-engine-roles)
  * [Restrict and actively audit administrator access](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#restrict-and-audit-admin-access)

  
  
### Use the VMware Engine Service Viewer role for least privilege

Google control ID | GCVE-CO-3.3  
---|---  
Implementation | Required  
Description | Grant the VMware Engine Service Viewer role to users by default, and only if necessary. The VMware Engine Service Viewer role provides read-only access to Google Cloud VMware Engine on Google Cloud and is designed to be sufficient for most tasks.  
Applicable products | 

  * VMware Engine
  * IAM

  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1
  * PR.AC-4.3
  * PR.AC-6.1

  
Related information | 

  * [VMware Engine IAM roles and permissions](https://docs.cloud.google.com/vmware-engine/docs/iam#vmware-engine-roles)

  
  
### Use RBAC and least privilege for vCenter Server Appliance roles

Google control ID | GCVE-CO-3.4  
---|---  
Implementation | Required  
Description | When granting VMware-level roles in vCenter Server Appliance, use role-based access controls (RBAC) and the principle of least privilege.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1

  
Related information | 

  * [Private cloud VMware components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components)

  
  
### Use identity federation for VMware users

Google control ID | GCVE-CO-3.5  
---|---  
Implementation | Required  
Description | Maintain a single identity solution where you can provision and manage user accounts. This recommended practice lets you centralize activities such as identity lifecycle management, group management and password management. Avoid creating a fractured identity strategy.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-6.1

  
Related information | 

  * [Configure an LDAP or Active Directory identity source](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#configure-ldap-active-directory-identity-source)

  
  
### Grant roles to groups instead of individuals for vCenter Server Appliance

Google control ID | GCVE-CO-3.6  
---|---  
Implementation | Required  
Description | When granting VMware-level roles in vCenter Server Appliance, grant roles to the groups that you create in your identity provider. Don't create a fractured identity strategy.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-6

  
Related CRI profile controls | 

  * PR.AC-1.3
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-6.1

  
Related information | 

  * [Using vCenter Server Roles to Assign Privileges](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vsphere-security/vsphere-permissions-and-user-management-tasks/using-roles-to-assign-privileges.html)

  
  
### Don't assign the Cloud-Owner-Role to user groups in vSphere

Google control ID | GCVE-CO-3.7  
---|---  
Implementation | Required  
Description | When creating user groups in vSphere, don't assign the Cloud-Owner-Role. This role grants administrative control over your private cloud's vCenter environment while restricting certain underlying global infrastructure permissions. User groups with permissions higher than Cloud-Owner-Role are automatically reset to Cloud-Owner-Role.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1

  
Related information | 

  * [Managing vSphere permissions](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-permissions-model)

  
  
### Avoid using default vCenter and NSX-T service accounts

Google control ID | GCVE-CO-3.8  
---|---  
Implementation | Required  
Description | Except for the initial configuration process and in emergency procedures, don't use the default vCenter service account (CloudOwner@gve.local) and the default NSX-T service account administrator (admin). These default service accounts include powerful permissions such as Cloud-Owner-Role and Enterprise Admin. Save the credentials for these service accounts in Secret Manager.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-2
  * IA-2
  * SC-28

  
Related CRI profile controls | 

  * PR.AC-1.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1

  
Related information | 

  * [Managing vSphere permissions](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-permissions-model)
  * [Sign-in credentials for Private Cloud management appliances](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client)

  
  
### Rotate passwords for default vCenter and NSX-T service accounts every 90 days

Google control ID | GCVE-CO-3.9  
---|---  
Implementation | Required  
Description | To prevent and mitigate the unauthorized disclosure of the credentials for the default vCenter service account (CloudOwner@gve.local) and the default NSX-T service account administrator (admin), rotate their passwords every 90 days.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-2

  
Related CRI profile controls | 

  * PR.AC-1.2

  
Related information | 

  * [Rotate the passwords of built-in service accounts](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#rotate-passwords-of-built-in-service-accounts)

  
  
### Use the NSX Gateway Firewall to segment north-south traffic

Google control ID | GCVE-CO-1.2  
---|---  
Implementation | Required  
Description | Control the north-south network traffic entering and exiting your private clouds using the NSX Gateway Firewall. NSX Gateway Firewalls are north-south firewalls that help protect the perimeters.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-4
  * SC-7

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.PT-4.1

  
Related information | 

  * [Well-Architected Design: Gateway Firewalls Use Cases and Scope](https://www.vmware.com/docs/well-architected-design-gateway-firewalls-use-cases-and-scope#introduction)
  * [Separate north-south and east-west firewall rules on gateway and distributed firewall in VMware Engine NSX](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#separate-north-south-east-west-firewall-rules)

  
  
### Use the NSX Distributed Firewall to segment east-west traffic

Google control ID | GCVE-CO-1.3  
---|---  
Implementation | Required  
Description | Control the east-west network traffic within your private cloud using the NSX Distributed Firewall (DFW). By default, all subnets can communicate with each other. Use DFW to define permitted traffic between applications and services inside your application.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-4
  * SC-7

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.PT-4.1

  
Related information | 

  * [Well-Architected Design: Gateway Firewalls Use Cases and Scope](https://www.vmware.com/docs/well-architected-design-gateway-firewalls-use-cases-and-scope#introduction)
  * [Separate north-south and east-west firewall rules on gateway and distributed firewall in VMware Engine NSX](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#separate-north-south-east-west-firewall-rules)

  
  
### Create separate subnets for workloads with different security requirements

Google control ID | GCVE-CO-1.4  
---|---  
Implementation | Required  
Description | If you run workloads that have different security requirements or data classifications, create workload subnets to separate them. Subnets let you reduce the potential blast radius by not mixing workloads of varying security requirements and postures.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AC-4
  * AC-20
  * SC-7

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.PT-4.1

  
Related information | 

  * [Configure and manage subnets](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-manage-subnets)

  
  
### Create a log sink to store VMware Engine audit logs

Google control ID | GCVE-CO-4.1  
---|---  
Implementation | Required  
Description | Use a log sink to store Google Cloud VMware Engine API audit logs. You can route audit logs to different destinations as required.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-6
  * AU-7

  
Related CRI profile controls | 

  * PR.IP-1.4
  * DM.ED-7.1

  
Related information | 

  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Google Cloud VMware Engine audit logging](https://docs.cloud.google.com/vmware-engine/docs/audit-logging)

  
  
### Collect VMware-level platform logs

Google control ID | GCVE-CO-4.2  
---|---  
Implementation | Required  
Description | To collect VMware-level platform logs (for example, vCenter and NSX-T syslog messages), configure Google Cloud VMware Engine private clouds to forward syslog logs to a centralized log aggregator. These logs aren't collected in VMware Engine audit logs and must be collected separately.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-6
  * AU-7

  
Related CRI profile controls | 

  * PR.IP-1.4
  * DM.ED-7.1

  
Related information | 

  * [Forwarding syslog messages to a remote server](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-forward-syslog)
  * [VMware Engine operator audit logging information](https://docs.cloud.google.com/vmware-engine/docs/operator-audit-logging)
  * [VMware Engine system audit logging information](https://docs.cloud.google.com/vmware-engine/docs/system-audit-logging)

  
  
### Monitor applications using Logging and Monitoring

Google control ID | GCVE-CO-4.3  
---|---  
Implementation | Required  
Description | Install the standalone agent to enable Cloud Logging and Cloud Monitoring from the VMware vSphere platform. The standalone agent lets you collect workload-level logs and send them to Logging and Monitoring for analysis and storage.  
Applicable products | 

  * VMware Engine
  * Logging
  * Cloud Monitoring

  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-6
  * AU-7

  
Related CRI profile controls | 

  * PR.IP-1.4
  * DM.ED-7.1

  
Related information | 

  * [Set up Cloud Monitoring with a standalone agent](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone)
  * [Google Cloud VMware Engine audit logging](https://docs.cloud.google.com/vmware-engine/docs/audit-logging)

  
  
### Create private clouds in regions that match your data-residency requirements

Google control ID | GCVE-CO-2.1  
---|---  
Implementation | Required  
Description | Create Google Cloud VMware Engine private clouds in regions that match your organization's data-residency requirements. Private clouds are long-lived provisioned resources that are non-trivial to deploy and relocate.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * CP-2
  * SC-7
  * SC-32

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Creating a VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud)
  * [Availability and redundancy](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware)

  
  
### Implement a backup and disaster recovery strategy

Google control ID | GCVE-CO-5.1  
---|---  
Implementation | Required  
Description | Implement Backup and DR Service or a third-party backup solution for workloads. By default, Google Cloud VMware Engine only automatically backs up vCenter and NSX config. Backup and DR makes VM backup and recovery easier.  
Applicable products | 

  * VMware Engine
  * Backup and DR

  
Related NIST-800-53 controls | 

  * CP-2
  * CP-6
  * CP-9
  * CP-10

  
Related CRI profile controls | 

  * PR.IP-4.1
  * PR.IP-4.2

  
Related information | 

  * [Backup and DR for VMware Engine on a backup/recovery appliance](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-vmware-vms)
  * [Configure Google Cloud VMware Engine for Backup and DR on a backup/recovery appliance](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)

  
  
### Implement application-level encryption for VMware workloads

Google control ID | GCVE-CO-1.1  
---|---  
Implementation | Required  
Description | Ensure applications that run on Google Cloud VMware Engine encrypt their traffic. VMware Engine doesn't encrypt workload traffic in transit.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * SC-8
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Encrypt the communication between your on-premises environment and Google Cloud](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#encrypt-communication-between-on-prem-and-google-cloud)

  
  
### Enable data-in-transit encryption on VMware vSAN clusters

Google control ID | GCVE-CO-2.3  
---|---  
Implementation | Required  
Description | Enable data-in-transit encryption on VMware vSAN clusters to encrypt data, metadata, and file service traffic.  
Applicable products |  VMware Engine  
Related NIST-800-53 controls | 

  * SC-8

  
Related CRI profile controls | 

  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [vSAN Data-In-Transit Encryption](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/using-encryption-in-a-vsan-cluster-1/vsan-data-in-transit-encryption.html)

  
  
### Configure vSAN data-at-rest encryption to use CMEK

Google control ID | GCVE-CO-2.2  
---|---  
Implementation | Required  
Description | If required by your regulatory environment, configure vSAN data-at-rest encryption to use customer-managed encryption keys (CMEKs).  
Applicable products | 

  * VMware Engine
  * Cloud KMS

  
Related NIST-800-53 controls | 

  * SC-12
  * SC-28

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-5.1

  
Related information | 

  * [How vSAN Data-At-Rest Encryption Works](https://techdocs.broadcom.com/us/en/vmware-cis/vsan/vsan/8-0/vsan-administration/using-encryption-in-a-vsan-cluster-1/vsan-data-at-rest-encryption/how-vsan-data-at-rest-encryption-works.html)
  * [Use a Google-owned and managed key provider enabled for vSAN encryption at rest](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#use-google-managed-key-provider-for-vsan-encryption)

  
  
### Rotate the keys used for vSAN data-at-rest encryption

Google control ID | GCVE-CO-2.4  
---|---  
Implementation | Required  
Description | Manage the lifecycle of the key encryption keys (KEKs) that you use for vSan data-at-rest encryption. Implement a key rotation procedure that aligns with your organization's requirements.  
Applicable products | 

  * VMware Engine
  * Cloud KMS

  
Related NIST-800-53 controls | 

  * SC-12

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-5.1

  
Related information | 

  * [Key rotation](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption#key_rotation)
  * [Automate the rotation of encryption keys according to your organization's standard](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#automate-rotation-of-encryption-keys-according-to-organization-standards)

  
  
## What's next

  * Review [data management controls](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/data-management).

  * See more [Google Cloud security best practices and guidelines](https://docs.cloud.google.com/docs/security/security-best-practices-catalog).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
