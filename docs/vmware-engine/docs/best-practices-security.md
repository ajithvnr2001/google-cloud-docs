---
url: https://docs.cloud.google.com/vmware-engine/docs/best-practices-security/
title: Best practices for VMware Engine security \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:04.715343+00:00
---

# Best practices for VMware Engine security  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/best-practices-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Best practices for VMware Engine security

This document describes the recommended security best practices for managing and configuring Google Cloud VMware Engine and is intended for users who are already familiar with VMware Engine. If you are a beginner, you may consider starting with learning about the [prerequisites](https://docs.cloud.google.com/vmware-engine/docs/quickstart-prerequisites) and [VMware Engine security](https://cloud.google.com/vmware-engine/docs/concepts-security).

VMware Engine has a [shared responsibility](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) model for security. Trusted security in the cloud is achieved through the shared responsibilities of customers and Google as a service provider. Following these best practices can help you save time, prevent errors, and mitigate the effects of points of failure.

## VMware Engine Networking

The following sections introduce best practices for networking in a VMware Engine environment.

### Identify and understand all traffic flows of your environment

VMware Engine leverages [VMware Engine networks](https://docs.cloud.google.com/vmware-engine/docs/networking/vmware-engine-network) and [VPC peerings](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network) to connect a private network connection from a VMware Engine private cloud network to your VPC network. Inbound traffic from a VPC in your Google Cloud environment or from an on-premises network traverses a Google-managed tenancy unit network.

### Use VMware Engine's Public IP Service for internet data transfer

Internet traffic can enter a private cloud directly using the Public IP Service of VMware Engine. Alternatively, internet traffic can enter using a public load balancer on Google Cloud. In that case, the traffic is routed like any other inbound traffic. Note that these options are mutually exclusive. If custom controls are required for internet traffic, such as URL filtering, IPS/IDS or traffic inspection provided by a central instance or service in your Google Cloud environment, you should route internet-bound traffic through VPC network.

If this is not applicable to you or you have the controls implemented within your private cloud, we recommend that you include the external IP address service in VMware Engine. In addition, we recommend using [external access rules](https://docs.cloud.google.com/vmware-engine/docs/networking/external-access-rules) to deny traffic patterns from the internet that don't apply to your applications.

### Separate north-south and east-west firewall rules on gateway and distributed firewall in VMware Engine NSX

Configure the distributed firewall (DFW) in NSX on the tier-1 logical router to segment internal traffic between your virtual layer 2 domains. The NSX DFW is designed to handle (internal) east-west network traffic between segments and allows firewall rules that allow and deny traffic between individual instances inside a segment.

For fine-grained network access control make sure to apply a restricted default policy on the DFW to deny network traffic between instances by default. Use the DFW to specifically allow traffic between applications and between services inside your application.

Configure the NSX [gateway firewall](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-A52E1A6F-F27D-41D9-9493-E3A75EC35481.html) to control north-south traffic that enters and leaves the private cloud.

The NSX gateway firewall is designed to control north-south traffic and recommended for use cases such as [controlling the traffic at a perimeter to another security zone](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/docs/vmware-nsx-gateway-firewall.pdf). If you need to configure the north-south traffic for the entire private cloud consistently, then configure the gateway firewall on the tier-0 router. If you need to configure the north-south traffic for each individual NSX segment, then configure the gateway firewall on the tier-1 router.

In addition to NSX firewalls, we recommend using the VPC firewall to allow and block east-west traffic between workloads in the VMware Engine private cloud and workloads in VPCs. Inbound data transfer to Compute Engine instances from VMware Engine workloads should be restricted by default with only consciously opened traffic.

Outbound data transfer to management appliances as well as to the vSphere/vSAN CIDR range should be blocked from VPCs as well using the VPC firewall. Only open outbound data transfer towards management appliances from trusted hosts and IP addresses inside your network. It's important to note that management appliances are not inside an NSX segment and hence, DFW rules don't apply to restrict access.

### Apply Zero Trust Security principles and micro-segmentation in NSX

Use the NSX DFW to implement traffic controls for security segments that are as granular as individual virtual machines. This principle of protecting traffic between individual VMs that is denied by default is often also referred to as ["Micro-segmentation"](https://www.vmware.com/topics/glossary/content/micro-segmentation.html), which is a more granular approach for firewalling than the conventional implementation of firewalls between Layer 3 domains.

The DFW is enabled in the hypervisor kernel on all VMware Engine vSphere hosts in your private cloud and can control traffic flow between workloads that are either in the same or in separate NSX segments. Firewall rules to allow traffic to and from VMs can be defined by organizing the VMs into [policy groups](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-9DFF6EE2-2E00-4097-A412-B72472596E4D.html), which can have flexible membership criteria such as VM tag or name matching.

Micro-segmentation lets you implement a network with fine-grained traffic control where a traffic pattern needs to be explicitly allowed. The security concept where all network flows are controlled by identity and device verification processes rather than implicit trust is often also called [Zero Trust Security](https://www.vmware.com/topics/glossary/content/zero-trust-security.html).

### Deploy a third-party firewall appliance from the Cloud Marketplace portal for IPS/IDS capabilities

If you require advanced Layer 7 security, including IDS/IPS capabilities for inbound traffic into the private cloud from the rest of your network or between your NSX network segments, consider deploying a third-party firewall appliance. The third-party appliance can be deployed either as a multi-NIC appliance between two VPCs in your Google Cloud network or inside the private cloud with an integration with NSX.

For a deep-dive in VMware Engine architectures with centralized appliances, which can be used for a variety of advanced security use cases, such as IPS/IDS, DDoS, SSL offloading and more, consult the document network security using centralized appliances in the [Cloud Architecture Center](https://docs.cloud.google.com/architecture).

### Use Google Cloud Armor to help protect web services on VMware Engine from DDoS attacks

If you route inbound traffic to workloads on VMware Engine through the customer VPC, then we recommend placing VMware Engine workloads in hybrid network endpoint groups behind Cloud Service Mesh and leveraging the external HTTP(S) load balancer. Either setup lets you include Google Cloud Armor for public-facing applications, mitigating DDoS attacks and common vulnerabilities like SQL injections or cross-site scripting.

If you require Cloud Service Mesh features such as advanced traffic management using the Envoy proxy or integration of Certificate Authority Service, we recommend Cloud Service Mesh. In all other cases, we recommend the external HTTP(S) load balancer.

Follow the documentation on how VMware Engine workloads can be added to Hybrid NEGs in either one of the following setups:

  * [Regional external HTTP(S) load balancing with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-hybrid)
  * [Global external HTTP(S) load balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-ext-global-https-hybrid)



### Connect to Google Cloud Services privately without internet access

VMware Engine private cloud workloads can access Google Cloud APIs such as the Cloud Storage API using Private Google Access. We recommend you use Private Google Access to access Google services without sending traffic over the internet because it reduces outbound data transfer cost and latency. This also removes the need for a network path to the internet for workloads that only need Google API access. Follow the deep-dive into Private Google Access for more technical details and configuration steps.

Similarly, VMware Engine workloads which need to access Google Cloud resources from a service producer network such as Cloud SQL or Memorystore instances should connect privately using PSA. For more information, visit the section on PSA for VMware Engine.

### Encrypt the communication between your on-premises environment and Google Cloud

Workloads on VMware Engine that need to communicate with on-premises systems should connect over an encrypted channel. We recommend a layered approach for encryption in-transit between your on-premises data centers and Google Cloud. The link between on-premises systems and Google Cloud can either be encrypted by setting up Cloud VPN with an IPsec tunnel or by using the built-in IPsec on VLAN attachments of the Interconnect. In addition, application layer encryption should be enabled between application components using TLS.

### Help protect your data from exfiltration using VPC Service Controls

We recommend mitigating data exfiltration risks using VPC Service Controls by placing your sensitive resources such as Cloud Storage buckets and BigQuery datasets into a VPC Service Controls perimeter. Workloads that need to access data inside a perimeter need to be placed into the perimeter as well. Specifically, the Google Cloud project that hosts the private cloud needs to be part of the VPC Service Controls perimeter to access resources that are protected by VPC Service Controls.

You need to configure inbound and outbound data transfer policies in your VPC Service Controls configuration to allow the VMware Engine producer service APIs into the perimeter. For detailed guidance on the setup, follow our documentation pages on VPC Service Controls with VMware Engine.

## VMware Engine IAM and permissions

The following sections introduce best practices for user permissions in a VMware Engine environment. It's important to take care of permissions within the VMware Engine environment and the Google Cloud project in which the private cloud is deployed.

### Use predefined roles or custom roles to grant access

The VMware Engine approach to manage [vSphere roles and permissions](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-5372F580-5C23-4E9C-8A4E-EF1B4DD9033E.html) can be leveraged the same way you are used to leveraging from other VMware Engine environments. However, activities like deploying a cluster require permissions in Identity and Access Management (IAM). The following table lists relevant access managers, the identity sources that they grant permissions to, and example activities that they enable.

Platform | Component | Identity source | Where to configure permissions | Example activities  
---|---|---|---|---  
Google Cloud | VMware Engine portal | Cloud Identity | Identity and Access Management | Private cloud deployment and cancelation, cluster deployment and cancelation, for example.  
VMware Engine | vCenter | LDAP | Hosts and clusters, VMs and folders, datastores in the vCenter UI | VM creation, VM folder creation, datastore object creation and deletion, for example  
NSX | LDAP | "Users and Roles" in the NSX Manager UI | NSX segment creation, firewall configuration, load balancer configuration, for example.  
vCenter | VM Guest Operating System | Active Directory, LDAP, Local Users, for example | Guest Operating System | SSH or RDP Login, file operations, for example  
  
In Google Cloud IAM, there are two predefined roles with permissions to the VMware Engine portal:

  * VMware Engine Service Admin - gives full access to the VMware Engine service on Google Cloud.
  * VMware Engine Service Viewer - gives read-only access to the VMware Engine service on Google Cloud.



These permissions relate to actions in the VMware Engine portal and don't relate to actions in the API or CLI. Note that also the basic roles include the ability to manage the VMware Engine service (Owner, Editor) or to view the service details (Viewer). Generally, we recommend you use predefined roles instead of basic roles because they provide more fine-grained permissions.

Programmatic access to the VMware Engine using service accounts using the API or CLI should be constrained using predefined roles or custom roles because they include more fine-grained permissions that apply only to VMware Engine. If programmatic access is only used for a task that requires only a specific subset of the permissions of the predefined roles, then we recommend you create a custom role.

Choose an appropriate location for the IAM role assignment in your organization's resource hierarchy. If you are running all your VMware Engine private clouds in one project only the roles can be assigned on project level. If there are technical or organizational requirements that result in your private clouds being located in separate projects, define the required roles in a folder that is common to the projects used for your private clouds.

Cloud IAM permissions are not required for activities that only need to be done inside vCenter, NSX or HCX. Staff that only needs to operate these environments don't require the previously listed IAM roles. Instead, they should use LDAP identities with permissions configured in vCenter and NSX. We recommend to provide the VMware Engine Service Admin or VMware Engine Service Viewer roles only to a very limited number of users since these roles grant access to the powerful CloudOwner user account for vCenter and the administrator user account for NSX. These user accounts should only be used for initial setup or emergency procedures.

### Restrict and actively audit administrator access

The VMware Engine Service Admin role is very powerful and should only be assigned to users who need to manage the lifecycle of the VMware Engine private cloud and their clusters. Typically, the manual addition or deletion of clusters and nodes is an action that does not happen frequently and may have a high impact on billing or the availability of the cluster. Only assign this role to very few people in your organization.

Make sure to regularly audit who has been assigned the VMware Engine Service Admin role, either directly on the project that is used for VMware Engine or on one of the parent levels of the resource hierarchy. This audit should include other roles, like the basic Editor and Owner roles that include critical permissions related to VMware Engine. You can use services like the IAM roles recommender to help identify overly privileged roles.

### Configure an LDAP or Active Directory identity source

An identity provider which supports LDAP authentication, such as Active Directory, should be configured to enable user authentication for vCenter and NSX Manager. This is a recommended practice to have central identity lifecycle management, group management, password management and more. Note that directly joining vCenter and NSX to Active Directory for integrated Windows authentication is not supported.

### Rotate the passwords of built-in service accounts

VMware Engine generates credentials to access management appliances in the private cloud (such as vCenter, NSX and HCX). We recommend that you establish a process to rotate the passwords of the default vCenter service account CloudOwner@gve.local and the default NSX service account administrator. Both user accounts should only be used for the initial configuration and emergency procedures and their passwords be rotated regularly (for example, every 60 or 90 days). Equivalently, regularly rotate the passwords of solution user accounts which are commonly used for the integration of third-party tooling. The more often you rotate service account passwords, the less likely it is that the password is still valid when a bad actor finds it.

## VMware Engine Logging and Monitoring

The following sections introduce best practices for logging and monitoring of both VM workloads and the VMware Engine infrastructure, which provides the resources that workloads consume.

### Ingest VMware Engine logs and metrics

Many organizations want to collect and analyze logs in a centralized "Single Pane of Glass." In Google Cloud, the Cloud Logging and Cloud Monitoring products provide services which can be used for centralized management of logs and metrics. VMware Engine can be integrated with Cloud Monitoring using a standalone agent. In this configuration, vCenter forwards metrics such as ESXi CPU and memory utilization to Cloud Monitoring. We recommend you create dashboards based on metrics that are forwarded by vCenter, or to get started with some sample dashboards that have been published on GitHub.

To collect platform logs, VMware Engine private clouds can forward Syslog logs to a centralized log aggregator. This can be done both for vCenter and NSX Syslog messages. Collecting, retaining and analyzing Syslog messages from vCenter has important security use cases, such as real-time alerting based on administrative user (or emergency user) logins, which should be performed only in exceptional circumstances. To analyze Syslog messages, a Syslog aggregator such as Fluentd or the Standalone agent needs to be configured to relay the messages to Cloud Logging.

We recommend that you analyze logs from VMware Engine in a central dashboard in a single project. If your VMware Engine environment spans multiple projects, you additionally need to aggregate your projects by configuring log sinks and monitoring scopes.

### Use the Cloud Logging agent for workload VM logging

VMware Engine workload VMs can send logs directly to Cloud Logging API, using the Logging agent. The Logging agent is based on fluentd and streams logs from common third-party applications and system software to Cloud Logging. As a best practice, align the approach for collecting and analyzing logs for workload VMs on VMware Engine with the approach for Compute Engine instances and your on-premises estate (if applicable). The use of the Logging agent on VMware Engine matches the approach that is used for VMs on Compute Engine such that workloads on both platforms send their logs to Cloud Logging.

### Apply equivalent capabilities of Access Transparency and Access Approval policies

While VMware Engine doesn't support access transparency (AxT) and access approval (AxA) in Google Cloud, we have implemented processes with equivalent capabilities that can be enabled by request.

For access transparency equivalency you need to consider several sources of logs, including:

  * vCenter logs - exportable using remote syslog server configuration.
  * ESXi logs - these can be collected using remote syslog configuration, however, you need to file a support request with Google Cloud to configure ESXi syslog forwarding.



If you have strict regulatory requirements, we implement a policy to provide equivalent capabilities for access approval. In this policy, standard service operations require a support ticket to be generated with a reason why access service operators require access.

Google Cloud Access Approval [exclusions](https://cloud.google.com/assured-workloads/access-approval/docs/overview#exclusions) apply.

## VMware Engine Encryption

The following sections introduce best practices for the encryption of storage in the private cloud, and driving factors to consider when choosing a key provider for your private cloud.

### Use a Google-owned and managed key provider enabled for vSAN encryption at rest

Encryption of data at rest is implemented using vSAN software based encryption. By default, VMware Engine enables vSAN encryption on each ESXi cluster and configures a default key provider in vCenter. Google requires customers to keep vSAN encryption enabled on their ESXi clusters and disabling vSAN encryption is a violation of the service terms for VMware Engine. Many organizations require encryption at rest as part of their company policies or are obligated by regulations to encrypt data (for example, NIST, FIPS).

Each ESXi host encrypts data using the standard AES-256 XTS mode with different, randomly generated Data Encryption Keys (DEK). The DEK is encrypted using a Key Encryption Key (KEK) and only stored on the disk in encrypted form. The vCenter server only stores the ID of the KEK but not the KEK itself which is stored in a Cloud Key Management Service (KMS). You can choose the location of the Cloud KMS where your KEK is kept.

We recommend you use the Google-managed default key provider. If, however, you are required to manage your Cloud KMS yourself, you can use a third-party KMIP 1.1 compliant Cloud KMS by one of the supported vendors. In both cases, the key provider can be used to encrypt data at-rest and vMotion traffic in-transit.

The following table highlights key differences between the default key provider and third-party Cloud KMS integrations:

Key provider | Pros | Cons  
---|---|---  
Default Google-owned and managed key provider | 

  * Simplicity: Deployed "out of the box" with no vendor management and no operational burden
  * End-to-end support by Google
  * Simplest method of the ability to rotate DEKs/KEKs is the key requirement
  * No additional cost
  * Built-in zone redundancy for high availability

| 

  * Not possible to bring your own key material (BYOK)
  * The KEKs are stored and managed in the Google infrastructure. External Key Managers (EKM) are not supported.

  
Third-party Cloud KMS key provider | 

  * Full control over the encrypted data and encryption key
  * Hardware backed keys can be stored in an HSM appliance

| 

  * Additional complexity and operational overhead
  * Additional cost
  * Possible additional latency, especially in the case of SaaS KMS
  * Possible lower availability

  
  
Google doesn't recommend enabling VM-level encryption together with vSAN datastore encryption because [deduplication efficiency drops to zero](https://kb.vmware.com/s/article/2148947) for encrypted VMs.

### Automate the rotation of encryption keys according to your organization's standards

You are responsible for rotating the KEK in VMware Engine vSphere. This applies whether you use the default key provider or an external Cloud KMS. You can initiate KEK rotation from vCenter or by using the vCenter API. Consider automating KEK rotation to meet your organization's security requirements. You can find an example PowerCLI script on GitHub.

#### Requirement for encrypted virtual machines

You can manage encryption keys for VMs by using the default Google-owned and managed key provider or Cloud Key Management Service.

If you enable **VM Encryption** (or vTPM) for any VMs in your private cloud and use a KMS to manage encryption keys, you must re-encrypt (shallow re-key) each VM after you rotate your KMS key.

A shallow re-key replaces only the key encryption key (KEK) and doesn't change the data encryption key (DEK) of the VMs. You typically trigger a shallow re-key by using the **Re-encrypt** action in the vSphere Client.

During this operation, the system re-wraps (re-encrypts) the existing DEK by using a new KEK. This process is fast because it doesn't rewrite actual data on the disk; instead, it only updates the small key bundle that contains the encrypted DEK. For more information, see the following VMware documentation:

  * [Generate New Encryption Keys](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vsan.doc/GUID-15393A27-5F38-4814-94E0-ED37A7E65249.html)
  * [Virtual Machine Re-encryption](https://techdocs.broadcom.com/us/en/vmware-cis/cloud/vmware-cloud-on-aws/SaaS/operations-guide/about-managing-virtual-machines-in-vmware-cloud-on-aws/bring-your-own-key-for-virtual-machine-encryption/virtual-machine-reencryption.html)



#### Risks of failing to re-key encrypted VMs

Failing to re-key encrypted VMs before you delete the rotated (old) KMS key version can cause the following issues:

  * **Failed vMotions** : ESXi hosts can't decrypt VM DEKs during vMotion if you reboot the destination hosts or add them to the cluster after the KMS key rotation but before you perform the VM re-key.
  * **Power-on failures** : If a host reboots or clears its local key cache, it can't reacquire keys from the KMS. If you deleted the required keys from the KMS, the host can't decrypt the DEK, which prevents encrypted VMs from powering on.



#### Steps to perform a re-key operation on workload VMs

  1. In the vSphere Client, right-click the VM.
  2. Select **VM Policies > Re-encrypt**.
  3. Confirm the re-encryption request in the dialog that appears.
  4. Wait for the task to complete.
  5. Verify the re-key by migrating the VM to a host that you rebooted or added to the cluster after the KMS key rotation.



## VMware Engine backup and disaster recovery

It's important to protect your data against threats like ransomware, corruption, and human error. Further, business-critical applications rely on your data being available virtually at all times, leaving you little time to recover data from sudden outages. This section does not contain a full coverage of all backup and disaster recovery aspects that are relevant to effectively design a backup and DR strategy to keep your data secure and available but contain key considerations when choosing the right strategy for your VMware Engine environment.

### Backup your workloads using Backup and DR Service

With Backup and DR Service Google Cloud offers a centrally managed, built-in backup solution that can be used for a variety of use cases, including backup of workloads on Compute Engine and Google Cloud VMware Engine. Backup and DR Service is Google's recommended single solution for workload backups because it offers benefits such as a broad spectrum of workload support, space-efficient, incremental-forever backups, and flexible storage options.

Google Cloud VMware Engine also supports using third-party, agent-based backup solutions. You may prefer these if you already have licenses for a third-party backup product. Prerequisites for these kinds of tools include the following:

  * They provide application-level backups
  * They are certified by the application vendors
  * They are certified by VMware Engine for vSAN
  * They support the VMware Engine vStorage API for Data Protection (VADP) protocol standard or take application-level backups



Regardless of the backup solution of your choice, we recommend Cloud Storage as a cost-effective storage option for long-term retention of backups. Cloud Storage is a highly durable, cost-effective object storage. Cloud Storage buckets can be configured to automatically replicate storage objects across multiple regions which is ideal for multi-regional cloud topologies.

Cloud Storage is also ideal for long-term archival as it provides lifecycle policies to automatically move storage objects to another storage tier once their lifetime exceeds a predefined value. Use this option for a cost-effective backup storage location and medium to high RPOs, especially if cost is a driving factor.

Alternatively, you can choose vSAN storage to minimize RPO instead. Use this storage option if a higher cost for backup storage is acceptable and RPO requirements can't be met with Cloud Storage. Avoid this option for long-term archival, since there is a risk that VMware Engine cluster sizes become storage bound.

### Implement disaster recovery with Backup and DR Service

We recommend restoring applications on VMware Engine using Backup and DR Service. To help protect your production workloads from outages of a single zone inside a region, we recommend that you deploy and operate a private cloud in a secondary zone inside the region if VMware Engine is available in more than one zone of that region. If this is not the case, we recommend restoring your applications in a secondary region.

In addition to Google Cloud Backup and DR, VMware Engine is compatible with other options for DR such as VMware Engine SRM and Zerto. Both VMware Engine SRM and Zerto rely on vSphere replication for disaster recovery which generally supports lower RPO targets. If your RPO target is minutes rather than hours, consider DR solutions based on vSphere replication.

## Checklist summary

The following checklist summarizes the security best practices for using the VMware Engine.

Task | Topic  
---|---  
VMware Engine Networking | 

  * Identify and understand all traffic flows of your environment
  * Use VMware Engine's Public IP Service for internet data transfer in
  * Separate north-south and east-west firewall rules on gateway and distributed firewall in VMware Engine NSX
  * Apply Zero Trust Security principles and micro-segmentation in NSX
  * Deploy a third-party firewall appliance from the Cloud Marketplace portal for IPS/IDS capabilities
  * Use Google Cloud Armor to help protect web services on VMware Engine from DDoS attacks
  * Connect to Google Cloud Services privately without internet access
  * Encrypt the communication between your on-premises environment and Google Cloud
  * Help protect your data from exfiltration using VPC Service Controls

  
VMware Engine IAM and Permissions | 

  * Use predefined roles or custom roles to grant access to VMware Engine
  * Restrict and actively audit administrator access to VMware Engine
  * Configure an LDAP or Active Directory identity source
  * Rotate the passwords of built-in VMware Engine service accounts

  
VMware Engine Logging and Monitoring | 

  * Ingest VMware Engine logs and metrics
  * Use the Cloud Logging agent for workload VM logging
  * Apply equivalent capabilities of Access Transparency and Access Approval policies

  
VMware Engine Encryption | 

  * Use a Google-managed Key provider enabled for vSAN encryption at rest
  * Automate the rotation of encryption keys according to your organization's standards

  
VMware Engine Backup and Disaster Recovery | 

  * Backup your workloads using Backup and DR
  * Implement disaster recovery with Backup and DR

  
  
## What's next

  * Try out Google Cloud VMware Engine for yourself. Visit [features, benefits, and use cases](https://docs.cloud.google.com/vmware-engine/docs/overview) for more information.
  * Read about [VMware Engine security concepts](https://docs.cloud.google.com/vmware-engine/docs/concepts-security).
  * Explore reference architectures, diagrams, tutorials, and best practices about Google Cloud. Visit [Cloud Architecture Center](https://docs.cloud.google.com/architecture) for more information.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
