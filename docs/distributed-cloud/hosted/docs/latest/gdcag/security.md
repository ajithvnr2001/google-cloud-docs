---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/security/
title: Security \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:01.110923+00:00
---

# Security  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Security Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview that covers core concepts, layers, and operational roles for maintaining security within Google Distributed Cloud (GDC) air-gapped. GDC is designed for highly secure, disconnected environments and for compliance with strict data sovereignty requirements.

This document is for audiences within the infrastructure operator group, platform administrator group, and application operator group who manage security for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

This document helps you understand the key security attributes across the following categories:

  * Compliance
  * Security operations
  * Reliability operations
  * Cryptography
  * Identity and Access Management (IAM)
  * Network security
  * Application security
  * Host and node security
  * Hardware security
  * Facility security



## Security strategy

GDC takes a security-first approach with multiple layers of security to deliver maximum control, remain compliant with statutory regulations, and safeguard confidential data. It's designed to run on dedicated and secured hardware in a local data center to provide strict tenant isolation.

The layers of security provided by GDC include hardware security, host and node security, application security, network security, cryptography, Identity and Access Management (IAM), security and reliability operations, compliance, and security offerings.

GDC has a shared security model for securing the complete application stack. GDC provides Infrastructure as a Service (IaaS), Platform as a Service (PaaS) and Software as a Service (SaaS). In all configurations of GDC, Google and the operator are responsible for securing the layers of the infrastructure. The customer is responsible for securing the project setup and application layer, including the application containers, base images, and dependencies.

![A histogram illustrating the shared cloud, operator, and customer responsibilities for each layer of security.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/gdch-sec-shared-responsibility-graph.png)

From a security perspective, the following audience groups operate GDC:

  * **Infrastructure operator group** : manages the day-to-day operations of the system infrastructure, and has no access to customer data. This persona is the highest level administrator of the system and could be Google, a contracted third party or the customer, depending on the nature of sovereignty restrictions.

  * **Platform administrator group** : a customer persona that manages resources and permissions for projects. This is the highest level of administrative privilege granted to the customer and is the only administrative level that can grant access to customer data.

  * **Application operator group** : develops applications to deploy and execute, and configures granular resources and permissions on GDC. This persona works within policies established by the Platform Administrator (PA) to ensure their systems align with the customer's security and compliance requirements.




For more information, see [Documentation audiences](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Facility security

You can deploy GDC in customer-designated, air-gapped data centers. Location-specific physical security will vary based on individual customer requirements. To comply with local regulations, data centers might need an accreditation, for example, ISO 27001. The data center must have multiple security measures in place, such as secure perimeter defense systems to prevent unauthorized access to the data center, comprehensive camera coverage to monitor all activity in the data center, physical authentication to ensure that only authorized personnel can access the data center, guard staff to patrol the data center 24 hours a day and all seven days and respond to any security incidents, strict access and security policies to regulate how personnel access and use the data center. These security measures are an important initial layer of protection to safeguard the data stored in the data center from unauthorized access, use, disclosure, disruption, modification, or destruction.

## Hardware security

Google has a rigorous process to ensure the security of its hardware. All GDC hardware is purchased and assembled from partners vetted and certified to meet customer-specific sovereignty and supply chain requirements. The hardware is tested and approved to meet Google's strict internal standards, and the needs of most security-conscious customers. All sub-components in GDC hardware come from trusted suppliers that are vetted and known to be reliable. Hardware integration into GDC racks is done at regional certified centers, which are facilities that Google has approved to handle sensitive hardware. All personnel who handle GDC hardware are background checked, which ensures that only authorized personnel have access to the hardware. In addition, the actual implementation of select high risk hardware and firmware components are security reviewed by a dedicated team. These reviews consider threats such as: supply chain attacks, physical attacks, and local execution attacks on hardware and firmware components, including persistent threats. These reviews build knowledge that directly informs our hardware security requirements including secure firmware and firmware updates, firmware integrity, secure boot, secure management and servicing. Google maintains close relationships with all vendors and teams using the hardware to ensure that top-level security features are provided. This means Google constantly works with its partners to ensure that the hardware is as secure as possible. Google pushes the bar by improving hardware and security requirements, performing interactive security reviews and working with product teams to implement new security features that are purpose-built for GDC and deeply integrated not only with the actual hardware and firmware, but also other product features.

## Host and node security

GDC ensures that only our custom-packaged secure Node operating system (OS) can be loaded onto the systems by default. Hardened images and configurations greatly reduce attack surfaces. Cryptographic modules that protect data at rest and in transit are FIPS 140-2/3 validated, which means they have been rigorously tested for security and vetted by an independent, accredited laboratory. GDC provides anti-malware software for the operating system running on the bare metal nodes and a solution to scan the storage systems. Google packages updates for these scanners and they are included in the regular system updates that the IO applies using the GDC upgrade process. Detection alerts are sent to the IO. GDC also provides integrity monitoring and violation detection tools to protect the system from unintentional changes. Overall, these security measures help to protect the system from a variety of attacks. The security measures make it difficult for attackers to access the system, exploit vulnerabilities, and install malware.

### Tenancy

GDC is a multi-tenant managed cloud platform similar to Google Cloud Platform. The architecture is designed to deliver strong isolation between tenants, providing a strong layer of protection between users of the cloud, and allowing users to meet stringent workload accreditation standards. GDC provides two tiers of tenant isolation. The first tier, called Organizations, provides strong physical compute isolation, and the second tier, Projects, offer more fine-grained resource allocation options through logical separation.

![A diagram of a GDC root admin cluster, with two org clusters and user clusters.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/tenancy-between-orgs-proj-clusters.png)

No physical compute servers are shared between organizations, and the operator layers also maintain tenancy. IOs are not allowed to access the PA layers. Likewise, the AOs cannot access the PA layers either.

![The GDC storage appliance operator layers.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/tenancy-operator-layers.png)

## Application security

To protect against software supply chain attacks, all GDC software is developed in accordance with the Supply chain Levels for Software Artifacts (SLSA), a supply chain security framework that Google developed in partnership with organizations including the CNCF and the Linux Foundation.

SLSA is a check-list of standards and controls to prevent tampering, improve integrity, and secure packages within the software supply chain. This checklist is designed to prevent exploits that attack source code repositories, build systems, and packages of third party dependencies.

All GDC source code and dependencies are stored in a Google version control system that is isolated and encrypted in secure Google data centers. All code has verified history and requires a second person to review code changes before those changes are accepted into the version control system.

Builds are delivered using a Google release orchestration system that leverages Google Cloud Build and Google automated test tools for a fully automated build, test, and release of container images and binaries. All builds are isolated, hermetic, and are defined using the build-as-code principle, and no individual has unilateral access in the software delivery process.

All images are scanned for vulnerabilities using multiple application security scanners and are validated at multiple points using a combination of cryptographic signatures and SHA256 checksums. Each release contains a Software Bill of Materials (SBOM) that includes details about the software components, dependencies and libraries, and data delivered.

## Network security

This section provides an overview of GDC network security.

### Physical network

While GDC is designed to be used in disconnected environments, in practicality, GDC systems are likely to be connected to a wider protected environment that is connected across a customer's internal private network, while still remaining disconnected from the public Internet.

All network traffic between the customer's private network and GDC systems passes through firewalls and Intrusion Detection & Prevention (IDS/IPS) systems. The firewall provides the first line of defense to control access to the system. The firewall and IDS/IPS control inbound and outbound traffic based on configurable security policies and uses machine learning to automatically analyze traffic and block unauthorized entry. The IDS/IPS system inspects all inbound and outbound communication for the infrastructure by default. PAs can also use the IDS/IPS system for their own workload traffic inspection. Both firewalls and IDS/IPS are also integrated with the organization's Observability stack for customer workloads and the IO's SIEM stack for the infrastructure to enable additional security analysis and forensics.

Firewalls enforce default deny rules as the initial security posture to prevent unintentional access and data leakages. The IO and PA have methods to define further access rules as needed. Inside GDC, there are two physically separate networks to isolate the administration and control functions from customer workload data.

The out-of-bound management (OOB) network is solely used for administrative functions such as configuration changes of the network devices, storage appliances, and other hardware components. Only the IO has access to the OOB network and they only have this access in exceptional cases. Network ACLs are configured such that only those servers that are in the root admin cluster that the IO controls are allowed access to this network. The data plane network connects the workload servers together and is accessible by the PA and AOs.

### Software defined networking

The data plane network is an overlay network based on Virtual Routing and Forwarding (VRF) for tenant traffic isolation. Each tenant organization has an external and internal VRF network. The external facing services, for example, external load balancer and egress NAT, would be in the external domain. Customer workloads reside in the internal VRF.

The internal network is used for communication within the tenant, such as workload traffic between nodes and to file and block storage inside the organization. The external network is used to communicate outside of an organization. Tenant management traffic to access control functions, or customer traffic to access projects, need to go through the external network. Each customer workload has load balancers and NAT gateways to configure for ingress and egress traffic.

### Virtual network

The GDC virtual networking is an organization level networking layer built on top of the overlay network. It's powered by GDC managed container network interface (CNI) driver - Anthos networking dataplane.

The virtual networking layer in GDC provides a soft-isolation within the organization which is referred to as "project". This layer provides the following network security features:

  * **Project network policy** : for project boundary protection.
  * **Organization network policy** : for organization boundary protection.



The project network and organization network policies have default deny configuration as the starting point to protect against unintended access and data leakage.

### Denial of service protection

All traffic into GDC passes through the IDS/IPS and a set of load balancers. The IDS/IPS detect and drop unauthorized traffic, and protects resources from session floods. The load balancers can throttle traffic appropriately to avoid loss of service. As any external connectivity is handled through the customer's private network, the customer can provide the extra layer of denial of service protection for distributed attacks.

## Cryptography

This section provides an overview of GDC cryptography.

### PKI

GDC provides a Public Key Infrastructure (PKI) for centralized X.509 CA management for infrastructure services. By default, GDC has per-installation private root CAs and intermediates and leafs distributed out of those. In addition to that, GDC can support installing customer issued certificates at customer facing endpoints, which increases flexibility in using certificates. GDC centrally coordinates the distribution of trust stores, which makes it easier for workloads and system services to authenticate and encrypt application traffic. Overall, GDC provides a powerful PKI solution to secure a variety of infrastructure services for convenient, yet tightly controlled, trust management.

### Key management service

GDC provides a Key Management Service (KMS) backed by Hardware Security Modules (HSMs). The KMS is a first-party service. The key material stays within the KMS, which in turn is backed by HSMs. Custom resource definitions (CRDs) hold encrypted key material. Only the KMS has access to raw key material in memory. There is one KMS per organization. All data at rest is encrypted by default using HSM backed keys. Customers can also choose to manage their own cryptographic keys. The KMS supports FIPS-approved algorithms and FIPS-validated modules. The KMS supports key import and export in a secure manner for key escrow, deletion, or disaster recovery use cases. These features make KMS a secure and reliable way to manage cryptographic keys.

GDC also offers customer-managed encryption keys (CMEK). CMEK gives customers control over the keys that protect their data at rest in GDC. One of the main motivations for CMEK adoption is cryptographic erasure, a high-assurance data destruction method for data spill remediation and off-boarding. Keys can be deleted out-of-band of the data they protect. All of the data in your organization is protected by a set of CMEK that your Platform Operators can monitor, audit, and delete as needed. CMEK keys are encryption keys that you can manage using HSM APIs. CMEK can be used to encrypted the data for block storage, virtual machine disks, database service and user container workloads.

### Encryption

This section provides an overview of GDC encryption.

#### Data at rest

All GDC data stored in file, block and object storage is encrypted at rest using multiple levels of encryption. In multi-tenant environments, each tenant's data is encrypted with a tenant-specific key before being written to file, block and object storage:

  * Block Storage (Application volumes, VM disks, database storage) is encrypted at three levels: 
    * **Software Layer** : Linux Unified Key Setup (LUKS) encryption performed within tenant-dedicated compute hardware with per-volume, HSM-backed keys, managed by the customer.
    * **Appliance Layer** : Volume Aggregate-level Encryption (NVE/NAE) encryption performed within Storage Appliance with per-tenant, HSM-backed keys, managed by the customer.
    * **Disk Layer** : Self-Encrypting Drives (SEDs) with per-drive, HSM-backed keys, managed by the IO.
  * Object Storage is encrypted at two layers 
    * **Bucket Layer** : Object data encryption coordinated within tenant-dedicated compute hardware with per-bucket, HSM-backed keys, managed by the customer.
    * **Disk Layer** : SEDs with per-drive, HSM-backed keys, managed by the IO.
  * Server Disk Storage, the system configuration data for a single tenant, is encrypted at one layer: 
    * **Disk Layer** : SEDs with per-drive, HSM-backed keys, managed by the customer.



#### Data in transit

All GDC traffic is encrypted by default using FIPS 140-2 certified cryptographic modules and industry standard protocols such as TLS 1.2+, HTTPS, and IPSec tunnels. Customers are also expected to use encrypted algorithms on the application layer, based on the shared responsibility model, to ensure that encryption requirements are met for all applications deployed on top of GDC.

## Identity and Access Management (IAM)

Access to the system is based on the principle of least privilege. Users are only given access to the resources they need. This process protects the system from unauthorized access and misuse. Additionally, the system enforces separation of duties, such as no unilateral access. No one person has complete control over any one system or process. This process helps prevent fraud and errors. GDC can integrate with customers' existing identity provider. The system supports SAML 2.0 and OIDC for IDP federation. This support lets users authenticate the users within the system using their existing identity provider to manage users in one location. All users and workloads are authenticated before accessing the system. RBAC and ABAC are used to authorize all control plane and data access. Users are only allowed to access the resources and perform actions only if they are authenticated and authorized. All accesses are audit logged, which lets administrators track who has accessed a resource and when. This process helps identify unauthorized access and misuse.

## Security operations

GDC Security Operations (SecOps) provides information assurance for entities with strict security, compliance, and sovereignty requirements to deliver maximum operational confidentiality, integrity, and availability of regulated customer air-gapped workloads. This security architecture is intended to meet the following objectives:

  * Correlate GDC platform logging for security analysis and response.
  * Promptly identify, report, and track security vulnerabilities.
  * Defend all OIC and GDC assets through Endpoint Detection & Response (EDR).
  * Provide tooling, processes, and runbooks to enable the SecOps operations center continuous monitoring for identification, containment, eradication, and recovery from cybersecurity incidents.

Feature | Description  
---|---  
Security Information & Event Management | Elastic Security is a security information and event management (SIEM) platform that collects, indexes, and analyzes security data from a variety of sources to help organizations detect and respond to threats.  
Vulnerability Management | Tenable Security Center is a vulnerability management platform that helps organizations identify and remediate security vulnerabilities.  
Endpoint Detection & Response | Elastic Security, Windows Defender, and ClamAV. Unified security platforms which provide organizations with a comprehensive view of their security posture to detect and respond to threats more effectively.  
Secure Case Management |  A software solution that lets organizations manage the security incident lifecycle.  
  
![GDC security operations diagram describing the software components and the people processes.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/gdch-sec-ops.png)

GDC SecOps enables IOs to deliver Security Operations functions. The GDC SecOps team deliver people-driven processes including incident response, vulnerability management, security engineering, and supply chain risk management. GDC SecOps lets a Security Operations Center (SOC) achieve the following:

Capability | Description  
---|---  
Detection | Our security infrastructure constantly monitors potential threats and vulnerabilities. When a threat or vulnerability is detected, the security operations team receives a report immediately.  
Triage | The security operations team triages each incident to determine the severity of the threat and appropriate response.  
Containment | The security operations team takes measures to contain the threat and prevent it from spreading.  
Investigation | The security operations team investigates the incident to determine the root cause and identify any weaknesses in our security posture.  
Response | The security operations team takes steps to respond to the incident and mitigate any damage that has been caused.  
Recovery | The security operations team takes steps to recover from the incident and restore our systems and networks to their normal state.  
  
### Vulnerability management

GDC runs multiple vulnerability identification processes at the pre-production environment before any release to stay on top of any potential Common Vulnerabilities and Exposure (CVEs). GDC also provides vulnerability scanning on the production environment for routine monitoring and reporting purposes. All findings on the production environment are integrated to Security Operations processes to track and mitigate threat hunting purposes.

### Security incident response

When vulnerabilities are discovered in code deployed to GDC or an incident occurs within the system, a set of incident response processes are available and executed by the IO and the GDC security team to mitigate, create and apply security patches, and communicate to affected parties. This incident management process parallels Google's standard incident management process with modifications for the disconnected nature of GDC.

For each CVE, or incident discovered, an incident commander (IC) is assigned to run the response process. The IC is responsible for managing the process, which includes verifying and validating the incident, assigning the vulnerability a The Common Vulnerability Scoring System (CVSS) score, managing the process of getting a patch created and ready for delivery, and creating the appropriate communications.

## Reliability operations

This section provides an overview of GDC reliability operations.

### Log and monitor

GDC ships with an Observability platform that provides monitoring, logging, tracing and reporting functionalities for GDC platform, services, and workloads.

The logging subsystem ingests and aggregates logs from all core GDC platforms and services and customer workloads into a time series database and makes that data available through an interactive user interface (UI) and APIs.

Critical audit log events include the following areas:

  * User authentication and authorization requests.
  * Generation and revocation of authentication tokens.
  * All Administrative access and changes.
  * All control plane API actions.
  * All security events, including IDS, IPS, firewall, anti-virus.



### Break glass access

The IO lacks access to customer data. However, in emergency situations, there might be cases where the IO needs access to customer data. In those cases, GDC has a set of emergency access procedures that a PA uses to explicitly grant access to the IO for troubleshooting.

All breakglass credentials are either stored offline in a safe, or encrypted with keys rooted in the HSM. Access to these credentials is an auditable event which can trigger alerts.

For example, in a case where the IAM configuration has been corrupted and prevents user access, the IO uses an SSH certificate-based authentication through secured work stations and requires multi-party approval to establish access. All actions taken are tracked and auditable. The SSH keys change after an emergency access incident.

### Disaster recovery

GDC ships with a backup system that lets PAs create and manage backup policies for clusters, namespaces or VMs. The backup system contains the typical systems for scheduling, running backups, restoring data and reporting.

### Upgrade and update system

Since GDC is an air-gapped environment, the Infrastructure Operator processes all updates to customer systems. Google signs and publishes binary updates in a secure location for the IO to download. The IO validates the binaries and moves the binaries into GDC for distribution and deployment.

This system includes all software and firmware updates, including updates to GDC software, the node-level OS, anti-virus and malware definitions and signatures, storage and network appliance, device updates, and any other binary updates.

### Change management - Infrastructure as Code

GDC uses Infrastructure as Code (IAC) to automate provisioning and deployment of GDC configurations. IAC separates the responsibilities among the infrastructure operations team. For example, proposing a configuration change versus authorizing the change, to make the entire process more secure. With GDC IAC, all configuration changes are validated through multi-party reviews and approval processes to ensure that only authorized configurations are deployed. These reviews create a transparent and auditable process, improves consistency of changes, and reduces configuration drift.

## Compliance processes

GDC is compliance ready for common regimes such as NIST 800-53, SOC 2 and helping certifications such as FIPS 140-2 and 3. GDC also goes through various certification processes, and meets the Google level security standards. Compliance is a continuous process. To enable customers and operators in this journey GDC provides continuous monitoring and tests. As part of the security practices for the continuous monitoring process, GDC tracks inventory changes, such as unknown software and hardware, or the addition of new software or hardware. GDC conducts regular penetration tests by simulating attacks from malicious actors. GDC periodically scans the systems for malware, and alerts GDC of any infections. The disaster recovery testing process tests GDC's ability to recover from a situation involving a disaster. These processes ensure GDC data and systems are secure.

### Security Technical Implementation Guide (STIG) compliance

Under STIG rule `RHEL-08-040320`, the `xorg-x11-server-common` package is an approved system dependency required for NVIDIA GPU drivers and hardware acceleration libraries (such as Vulkan and Mesa). The graphical display manager service is disabled and inactive on node operating system images.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
