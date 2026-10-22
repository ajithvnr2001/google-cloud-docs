---
url: https://docs.cloud.google.com/docs/security/gcmvsp/infrastructure/
title: Infrastructure guidelines \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:51.044482+00:00
---

# Infrastructure guidelines  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/gcmvsp/infrastructure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Infrastructure guidelines Stay organized with collections  Save and categorize content based on your preferences. 

The following guidelines for the minimum viable security platform align with the infrastructure pillar.

## Basic level guidelines

Implement the following infrastructure guidelines first.

Item | 

### Disable VM serial port access  
  
---|---  
Description | Turn off serial port access by setting the `compute.disableSerialPortAccess` organization policy constraint. Disable serial port access on your Compute Engine VMs to help eliminate an access channel that bypasses your firewall rules and other network security controls. The interactive serial console is primarily intended for emergency troubleshooting, but, when you leave it enabled, you can create a persistent backdoor that can be targeted by attackers.Disabling serial port access helps enforces a defense-in-depth security posture by forcing all administrative access through standard, audited pathways like SSH, which you can protect by enabling Identity and Access Management (IAM) and Identity-Aware Proxy (IAP).  
Related information | 

  * [Disabling interactive serial console access through Organization Policy Service](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#disabling_interactive_serial_console_access_through_organization_policy)

  
Item ID | MVSP-CO-1.24  
Mapping |  Related NIST-800-53 controls:

  * AC-3

Related CRI profile controls:

  * PR.AC-3.1

  
Item | 

### Disable IPv6 unless required  
  
---|---  
Description | Disable IPv6 external subnet creation unless specifically required. To reduce your attack surface, consider disabling IPv6 on systems and networks where it's not actively managed or required. Many organizations have mature security controls and monitoring for IPv4, but their tools and policies might not fully extend to IPv6, which can create a significant blind spot for threats. Running a dual-stack network also introduces operational complexity, requiring specific configurations and expertise to manage and troubleshoot effectively. Therefore, if you don't have a clear business driver for IPv6, disabling it can simplify your environment and ensure all traffic is consistently filtered through your established IPv4 security posture.  
Related information | 

  * [IPv6 support in Google Cloud](https://docs.cloud.google.com/vpc/docs/ipv6-support)

  
Item ID | MVSP-CO-1.25  
Mapping |  Related NIST-800-53 controls:

  * CM-7

Related CRI profile controls:

  * PR.PT-3.1

Compliance Manager control:

  * [Configure the Disable VPC External IPv6 Usage Organization Policy](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-external-ipv6-addresses-org-policy)

  
Item | 

### Enable Shielded VM features  
  
---|---  
Description | Turn on the virtual trusted platform module (vTPM) and integrity monitoring attributes of Shielded VM for your instances. vTPM and integrity monitoring attributes are part of the default VM instance creation process. Use the vTPM and integrity monitoring attributes of Shielded VM to help ensure that your VMs boot only with trusted, unmodified code.The vTPM provides a secure, virtual cryptoprocessor that generates and stores cryptographic measurements of the entire boot sequence, from the UEFI firmware to the kernel drivers. Integrity monitoring then continuously compares these runtime measurements against a known-good baseline established when the VM was first created.These features provide a verifiable chain of trust and automatically alert you or take action if they detect any malicious modifications, like those from a bootkit or rootkit. Shielded VM features help to maintain your workload's integrity from the moment that the instance powers on.  
Related information | 

  * [Shielded VM overview](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)

  
Item ID | MVSP-CO-1.28  
Mapping |  Related NIST-800-53 controls:

  * SI-7

Related CRI profile controls:

  * PR.DS-6.1

Compliance Manager control:

  * [Enable Shielded VM for Compute Engine Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-shielded-vm-compute-instances)

  
Item | 

### Use GKE Autopilot  
  
---|---  
Description | Use Google Kubernetes Engine (GKE) Autopilot clusters. Autopilot clusters offer robust security measures, with many security best practices for container or GKE enabled by default.  
Related information | 

  * [GKE Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

  
Item ID | MVSP-CO-1.29  
Mapping |  Related NIST-800-53 controls:

  * CM-2

Related CRI profile controls:

  * PR.IP-1.1

  
Item | 

### Use least privilege accounts for GKE clusters and nodes  
  
---|---  
Description | Use least-privilege Identity and Access Management (IAM) service accounts for Google Kubernetes Engine (GKE) clusters and nodes. Access to the GKE control plane is restricted to a single DNS-based endpoint. Implementing least privilege significantly reduces the attack surface without the need for additional firewall rules or bastion hosts.  
Related information | 

  * [Harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)

  
Item ID | MVSP-CO-1.30  
Mapping |  Related NIST-800-53 controls:

  * AC-6

Related CRI profile controls:

  * PR.AC-4.1

Compliance Manager control:

  * [Use Least Privilege Service Accounts for GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#use-least-privileges-service-accounts-gke)

  
Item | 

### Restrict control plane access  
  
---|---  
Description | By default, the Google Kubernetes Engine (GKE) cluster control plane and nodes have internet routable addresses that can be accessed from any IP address. Restrict network access to the control plane by using a DNS-based endpoint and by creating private clusters. The control plane is the management center for a Kubernetes cluster, and exposing it to the internet makes it a prime target for attackers. This configuration makes the control plane private and removes it from the internet.Restricting control plane access helps ensure that only trusted devices within your organization's private network can manage the cluster, drastically reducing the risk of an external attack.  
Related information | 

  * [How authorized networks work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#how_authorized_networks_work)
  * [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)
  * [Creating a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/legacy/network-isolation)

  
Item ID | MVSP-CO-1.31  
Mapping |  Related NIST-800-53 controls:

  * SC-7

Related CRI profile controls:

  * PR.AC-3.1

  
Item | 

### Use Container-Optimized OS with containerd runtime  
  
---|---  
Description | Use Container-Optimized OS to implement a hardened and managed container OS. General-purpose operating systems include many extra programs that aren't needed to run containers and therefore create a larger, unnecessary target for attackers. Container-Optimized OS is a minimal, locked-down operating system that significantly reduces this attack surface by including only what is necessary. As a managed OS, Container-Optimized OS also has security patches that are automatically applied by Google, which help ensure critical vulnerabilities are fixed and reduces your operational workload.An image that includes Container-Optimized OS with containerd (cos_containerd) has containerd as the main container runtime directly integrated with Kubernetes. containerd is the core runtime component of Docker and is designed to deliver core container functionality for the Kubernetes Container Runtime Interface (CRI). It is significantly less complex than the full Docker daemon, and therefore has a smaller attack surface.  
Related information | 

  * [Container-Optimized OS overview](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits)

  
Item ID | MVSP-CO-1.41  
Mapping |  Related NIST-800-53 controls:

  * CM-7
  * SC-7
  * SC-38
  * SI-2
  * SI-7

Related CRI profile controls:

  * PR.PT-3.1

Compliance Manager control:

  * [Require Container-Optimized OS for a GKE Cluster](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-container-optimized-os)

  
  
## Intermediate level guidelines

After you implemented the basic guidelines, implement the following infrastructure guidelines.

Item | 

### Enforce OS Login for VMs  
  
---|---  
Description | If you let developers access Compute Engine resources using SSH, configure OS Login with 2-step verification. Use OS Login to manage SSH keys with Identity and Access Management (IAM) policies by setting the `compute.requireOsLogin` organization policy constraint. OS Login centralizes VM access by tying SSH permissions to a user's Google identity and IAM roles, eliminating the need to manage individual SSH keys on each machine.Tying SSH permissions to a user's identity is crucial for security because removing a user's IAM role instantly revokes their access across all instances, protecting against unauthorized entry from stale accounts. The system simplifies key management to help prevent key sprawl and provides a clear, centralized audit trail for all login events in Cloud Audit Logs. OS Login also lets you enforce two-factor authentication, adding a critical layer of protection against stolen SSH keys and credentials. An attacker with compromised OAuth tokens but no password or security key is blocked by this feature.  
Related information | 

  * [Set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin)

  
Item ID | MVSP-CO-1.26  
Mapping |  Related NIST-800-53 controls:

  * AC-2

Related CRI profile controls:

  * PR.AC-1.1

Compliance Manager control:

  * [Enable OS Login](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-os-login)

  
Item | 

### Restrict external IP addresses on VMs  
  
---|---  
Description | Unless needed, prevent the creation of Compute Engine instances with public IP addresses. The `compute.vmExternalIpAccess` list constraint defines the set of Compute Engine VM instances that can have external IP addresses.Prevent Compute Engine instances from having external IP addresses to drastically reduce their exposure to the internet. Any instance with an external IP address is immediately discoverable and becomes a direct target for automated scans, brute-force attacks, and attempts to exploit vulnerabilities. Instead, require instances to use private IP addresses and manage access through controlled, authenticated, and logged pathways like the Identity-Aware Proxy (IAP) tunnel or a bastion host.Adopting this deny-by-default posture is a foundational security best practice that helps minimize your attack surface and enforces a zero-trust approach to your network. This constraint isn't retroactive.  
Related information | 

  * [Restrict external IP addresses to specific instances](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip)
  * [View the network configuration for an instance](https://docs.cloud.google.com/compute/docs/instances/view-network-properties)

  
Item ID | MVSP-CO-1.27  
Mapping |  Related NIST-800-53 controls:

  * SC-7
  * SC-8

Related CRI profile controls:

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

Compliance Manager control:

  * [Restrict External IP Addresses to Specific VM Instances](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-external-ip-to-specific-vm-instances)

  
Item | 

### Use Workload Identity Federation for GKE  
  
---|---  
Description | Use Workload Identity Federation for GKE to securely authenticate to Google Cloud APIs from Google Kubernetes Engine (GKE) workloads. Workload Identity Federation for GKE provides a simpler and safer alternative to using service account keys.  
Related information | 

  * [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

  
Item ID | MVSP-CO-1.32  
Mapping |  Related NIST-800-53 controls:

  * IA-2

Related CRI profile controls:

  * PR.AC-1.1

Compliance Manager control:

  * [Enable Workload Identity Federation for GKE on clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-workload-identity-gke)

  
Item | 

### Use private GKE nodes  
  
---|---  
Description | Create private nodes to reduce internet exposure. Private Google Kubernetes Engine (GKE) nodes help reduce internet exposure by ensuring GKE nodes don't have a public IP address.  
Related information | 

  * [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)

  
Item ID | MVSP-CO-1.33  
Mapping |  Related NIST-800-53 controls:

  * SC-7

Related CRI profile controls:

  * PR.AC-3.1

Compliance Manager control:

  * [Enable Private Clusters for GKE](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-private-clusters-kubernetes)

  
Item | 

### Use Google Groups for RBAC  
  
---|---  
Description | Use Google Groups for role-based access control (RBAC), which also lets you integrate with your existing user account management practices, such as revoking access when someone leaves your organization. Google Groups for RBAC helps provide efficient management of cluster access using Identity and Access Management (IAM) and Google Groups, which is suitable for most organizations that use Google Groups.  
Related information | 

  * [Configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac)

  
Item ID | MVSP-CO-1.34  
Mapping |  Related NIST-800-53 controls:

  * AC-2

Related CRI profile controls:

  * PR.AC-1.1

Compliance Manager control:

  * [Use Google Groups for Kubernetes RBAC](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#use-google-group-rbac-gke)

  
  
## Advanced level guidelines

After you implemented the intermediate guidelines, implement the following infrastructure guidelines.

Item | 

### Enable GKE Sandbox  
  
---|---  
Description | Use GKE Sandbox to provide an extra layer of security to help prevent untrusted code from affecting the host kernel on your Google Kubernetes Engine (GKE) cluster nodes. GKE Sandbox enhances workload isolation for untrusted or sensitive workloads, providing an additional layer of protection against container escape attacks.  
Related information | 

  * [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)

  
Item ID | MVSP-CO-1.35  
Mapping |  Related NIST-800-53 controls:

  * SC-39

Related CRI profile controls:

  * PR.DS-1.1

Compliance Manager control:

  * [Require GKE Sandbox for GKE clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-sandbox-gke)

  
Item | 

### Enforce Binary Authorization  
  
---|---  
Description | Use Binary Authorization to make sure trusted images are deployed to Google Kubernetes Engine (GKE) and Cloud Run. Binary Authorization helps ensure that only verified and trusted container images can be deployed in your clusters, strengthening software supply chain security.  
Related information | 

  * [Binary Authorization overview](https://docs.cloud.google.com/binary-authorization/docs/overview)

  
Item ID | MVSP-CO-1.36  
Mapping |  Related NIST-800-53 controls:

  * SI-7

Related CRI profile controls:

  * PR.DS-6.1

Compliance Manager control:

  * [Require Binary Authorization on a Cluster](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-binary-authorization)

  
Item | 

### Use Confidential Google Kubernetes Engine Nodes  
  
---|---  
Description | Use Confidential GKE Nodes to enforce encryption of data in-use in your nodes and workloads. Confidential GKE Nodes help secure highly sensitive workloads by encrypting data in use through confidential computing.  
Related information | 

  * [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)

  
Item ID | MVSP-CO-1.37  
Mapping |  Related NIST-800-53 controls:

  * SC-28

Related CRI profile controls:

  * PR.DS-1.1

  
Item | 

### Run a custom certificate authority in GKE  
  
---|---  
Description | Run your own certificate authorities to manage keys within Google Kubernetes Engine (GKE). Using your own certificate authorities offers greater control over cryptographic operations. To request access to this feature, contact your Google Cloud account team.  
Related information | 

  * [Run your own certificate authorities and keys in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys)

  
Item ID | MVSP-CO-1.38  
Mapping |  Related NIST-800-53 controls:

  * SC-12

Related CRI profile controls:

  * PR.DS-1.1

  
Item | 

### Encrypt Kubernetes Secrets using Cloud KMS  
  
---|---  
Description | Encrypt Kubernetes Secrets at rest using Cloud Key Management Service (Cloud KMS) managed keys. Cloud KMS provides an additional layer of security for etcd data by letting you encrypt Kubernetes Secrets with a key that you own and manage.  
Related information | 

  * [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets)

  
Item ID | MVSP-CO-1.39  
Mapping |  Related NIST-800-53 controls:

  * SC-28

Related CRI profile controls:

  * PR.DS-1.1

Compliance Manager control:

  * [Enable Encryption on GKE Clusters](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-encryption-gke-cluster)

  
Item | 

### Use CMEK for node boot disks  
  
---|---  
Description | Use customer-managed encryption keys (CMEK) for node boot disk encryption. CMEK lets you encrypt a Kubernetes node's boot disk with a key that you own and manage.  
Related information | 

  * [Use CMEK-protected node boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek#boot-disks)

  
Item ID | MVSP-CO-1.40  
Mapping |  Related NIST-800-53 controls:

  * SC-28

Related CRI profile controls:

  * PR.DS-1.1

Compliance Manager control:

  * [Enable CMEK on GKE Node Pool Boot Disks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-cmek-nodepool-boot-disk)

  
  
## What's next

  * [Data protection guidelines](https://docs.cloud.google.com/docs/security/gcmvsp/data-protection)
  * [Overview of minimum viable secure platform](https://docs.cloud.google.com/docs/security/gcmvsp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
