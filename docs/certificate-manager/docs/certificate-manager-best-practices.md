---
url: https://docs.cloud.google.com/certificate-manager/docs/certificate-manager-best-practices/
title: Best practices for Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:36.711955+00:00
---

# Best practices for Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/certificate-manager-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Best practices for Certificate Manager Stay organized with collections  Save and categorize content based on your preferences. 

This page describes various best practices for configuring and managing certificates on Google Cloud by using Certificate Manager and Certificate Authority Service (CA Service). This page describes how to design your certificate management architecture.

Before reading this page, make sure that you're familiar with the [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview) and the [Certificate Authority Service overview](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) pages.

## Design your certificate management architecture

When designing an enterprise certificate management strategy, you must consider your organization's key use cases and the entire lifecycle of your certificates. These decisions affect the cost, operational overhead, and ease of implementing certificate-management capabilities such as issuance, revocation, and rotation.

The following sections explain our recommendations for each design choice.

### Choose a certificate type

When creating a certificate, you must make sure to select a certificate type that's appropriate for your use case depending on your application requirements and your organization's security policies.

To analyze the type of certificate that might work best for you, see the following flowchart:

[ ![Assess which certificate type to choose.](https://docs.cloud.google.com/static/certificate-manager/images/ccm-choose-certificate-type.svg)](https://docs.cloud.google.com/static/certificate-manager/images/ccm-choose-certificate-type.svg) Assess which certificate type to choose (click to enlarge).

Here are a few helpful documentation links for the topics mentioned in the flowchart:

  * [Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/core-components#google-managed-certificates)
  * [Certificate authority pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-concepts#ca-pool-resource)
  * [Certificate Authority Service overview](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)
  * [Self-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/core-components#certs)



### Streamline your private CA Service hierarchy

We recommend that you keep the hierarchy of your CA Service as straightforward as possible to ensure smooth operations and troubleshooting. You must store your root certificate authority (CA) in its own Google project. The root CA signs a few intermediate CAs, and those CAs then issue the final certificates.

This flat hierarchical structure enhances transparency, simplifies certificate revocation processes, and reduces the likelihood of misconfigurations. Although CA Service is a regional service, a root CA in one region can sign subordinate CAs located in other regions.

Follow these best practices in your CA Service hierarchy as shown in the diagram:

  * Isolate your root CA in its own Google Cloud project to sign the issuing CA.
  * Create issuing CAs in CA pools that are hosted in separate projects. Host these pools in separate projects and segment them by geographic location (region), software development lifecycle (development, production, test), or a specific use case.

  * Configure Certificate Manager to use an issuing CA pool that can issue privately trusted certificates for supported resources.


[ ![Recommended CA hierarchy design.](https://docs.cloud.google.com/static/certificate-manager/images/ccm-recommended-ca-design.svg)](https://docs.cloud.google.com/static/certificate-manager/images/ccm-recommended-ca-design.svg) Recommended design for your CA hierarchy (click to enlarge).**Important:** Even if you use a regional CA pool that's integrated with Certificate Manager, you can use the CA pool to issue a global Google-managed TLS certificate in any region.

### Use comprehensive hostname coverage

We recommend that you make sure your certificates provide sufficient hostname coverage for all the domains and subdomains that your services need to protect. Inadequate hostname coverage can lead to security warnings for users, service disruptions, and a negative user experience.

Avoid using a single certificate for multiple domains. If the single certificate either fails to renew or is accidentally deleted, then all domains that it covers become unsecured. We recommend that you create distinct certificates for different domains.

If you plan to add new subdomains or services later, then use wildcard characters to include the subdomains or services in your certificate from the outset. For example, a wildcard certificate for `*.myorg.example.com` secures only the first subdomain level, but not the deeper subdomain levels such as `sub.subdomain.myorg.example.com`.

### Use Google-managed certificates

For efficient public certificate management and ease of use, we recommend that you use [Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates#create_a_google-managed_certificate). This approach significantly reduces operational overhead, automating tasks such as certificate rotation and eliminating the risks associated with manual renewals.

In addition, Google-managed certificates offer seamless integration with other Google Cloud services. Certificate Manager only supports the [Public Certificate Authority](https://docs.cloud.google.com/certificate-manager/docs/public-ca) (`pki.goog`) and the Let's Encrypt CA (`letsencrypt.org`) for issuing publicly trusted Google-managed certificates. Certificate Manager provisions Google-managed certificates with a validity period of either 45 days or 90 days, depending on the issuing CA:

  * Certificates issued by Public CA are gradually transitioning from a 90-day validity period to a 45-day validity period. Existing 90-day certificates remain valid for 90 days until their next renewal.
  * Certificates issued by Let's Encrypt CA have a 90-day validity period.



Certificate Manager automatically starts the renewal process when approximately one-third of the certificate's validity period remains. Renewal begins about 15 days before expiry for 45-day certificates and about 30 days before expiry for 90-day certificates.

**Important:** You can prevent the creation of global self-managed TLS certificates in your organization by implementing the `constraints/compute.disableGlobalSelfManagedSslCertificate` policy constraint.

## Scale and improve your certificate performance

The following sections describe the best practices to scale your certificates and improve the performance of certificate-related actions, such as provisioning and renewal.

### Apply decentralized deployment for Certificate Manager

Use Certificate Manager on a per-project and per-location basis, which means that your certificates are stored in the same project as their associated resources in the same region. This strategy enhances reliability by preventing certificate reuse across different regions and effectively minimizing the impact in the unlikely event of a regional outage.

Furthermore, because [quotas and limits](https://docs.cloud.google.com/certificate-manager/docs/quotas) are applied at the Google Cloud project-level, deploying Certificate Manager across multiple projects increases your overall quotas. This is because the use of a resource in one project doesn't affect your available quota in another project.

### Use certificates with ECDSA keys

This section examines why we recommend ECDSA over RSA as a best practice for certificate signing keys.

#### Which key type to use

_ECDSA P-256_ is the recommended choice of key type for most TLS certificates because ECDSA P-256 offers strong cryptographic security, excellent performance for signing operations, and efficient use of network bandwidth.

Some of the possible reasons to use other certificate key types are as follows:

  * If you need to support legacy clients that don't support ECDSA certificates, you can provide RSA-2048 certificates in addition to ECDSA P-256 certificates.
  * If you have specific compliance requirements that require you to use larger key sizes or particular key types, then you can use ECDSA P-384, RSA-2048, RSA-3072, and RSA-4096 keys.



#### Why choose ECDSA over RSA

The primary advantage of ECDSA lies in its ability to provide an equivalent cryptographic security level with significantly smaller keys compared with RSA. This efficiency translates into tangible performance and resource benefits. A smaller key doesn't imply weaker security—ECDSA is based on the elliptic curve discrete logarithm problem, which provides stronger security per unit of key, and in some cases better computational efficiency compared with RSA.

For example:

  * A 256-bit ECDSA key provides a similar security level to an RSA-3072 key.
  * A 384-bit ECDSA key provides a greater security level than any widely supported RSA key size.



Key benefits of ECDSA:

  * **Performance** : ECDSA signing operations are significantly less computationally intensive than RSA operations providing an equivalent security level. This reduces CPU load and latency, which is crucial for high-throughput or latency-sensitive systems.

  * **Efficiency** : smaller keys and signatures require less bandwidth and storage, which is especially beneficial for resource-constrained environments like mobile and IoT devices.




You can create the following [custom organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints) to enforce the use of specific key types in your certificates. This is applicable only for Google-managed certificates from CA Service (private trust-managed certificates), not for self-managed certificates and public-trust Google-managed certificates.
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictAlgorithm \
        resourceTypes: \
        - certificatemanager.googleapis.com/CertificateIssuanceConfig \
        methodTypes: \
        - CREATE \
        - UPDATE \
        condition: "resource.keyAlgorithm == 'ECDSA_P256'" \
        actionType: ALLOW \
        displayName: Allow only ECDSA_P256 in Certificate Issuance configs \
        description: Only ECDSA_P256 certificates are allowed from CA Service.
    

### Use a CA pool to issue certificates from private CAs

We recommend that you use CA pools for your issuing CAs. A CA pool is a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy. Using a CA pool increases the total effective queries per second (QPS) by load balancing and distributing the incoming certificate requests across all enabled CAs within the pool. This improves performance without impacting either the workload or client-side changes.

CA pools provide a single endpoint for certificate issuance and retrieval. You can use CA pools to safely rotate your CAs without causing downtime due to certificate expiration or compromise.

### Use certificate maps

To ensure optimal scalability, we recommend that you use [certificate maps](https://docs.cloud.google.com/certificate-manager/docs/core-components#cert-maps) with supported resources. Certificate maps are designed to scale, supporting thousands of certificate entries by default and capable of handling millions of certificates. When used by load balancers, certificate map entries take precedence over other certificates, such as Compute Engine SSL certificates.

Certificate maps also let you configure your certificate selection logic. For example, during a handshake if a client's hostname doesn't match any entry in the provisioned certificate map, then the load balancer returns the primary certificate.

### Choose the correct domain authorization type

To issue Google-managed certificates, you can prove your domain ownership by using either [load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#lb-auth) or [DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization#dns-auth).

The following table describes the considerations for each approach:

Feature | Load balancer authorization | DNS authorization  
---|---|---  
Setup complexity | Doesn't require any additional configuration steps or changes to your DNS configuration. | Requires you to create a DNS authorization and add its corresponding CNAME record to your DNS configuration.  
Network security | The load balancer must be fully accessible by using the internet on port `443`, including the DNS configuration for all domains served by a certificate. Load balancer authorization doesn't work with other configurations. | DNS authorization works with highly complex configurations, such as ports other than 443, and CDN layers in front of the target proxy.   
Provisioning speed | Faster provisioning speed. You can provision certificates only after the load balancer is fully set up and is serving network traffic. | You can provision certificates in advance, before the target proxy is ready to serve network traffic.  
Wildcard certificates | Not supported. | Supported.  
  
### Automate rotation of self-managed certificates

Unlike Google-managed certificates, self-managed certificates need to be manually replaced before they expire. We recommend that you automate this process by using the Certificate Lifecycle Management (CLM) offerings of your choice. This helps reduce errors, downtime, and ensure operational efficiency.

You can also use certificate maps to orchestrate a seamless certificate rotation. This process includes the following steps:

  1. Monitor certificate expiration by using [Cloud Monitoring and alerts](https://docs.cloud.google.com/certificate-authority-service/docs/monitoring#ca_expiring_in_30_days). We recommend that you create an alert for certificates expiring in the next 15 to 30 days.
  2. Generate a certificate signing request (CSR) and a private key to submit to your CA.
  3. Submit your CSR and private key to your CA, and then retrieve the new certificate.
  4. Upload the new certificate to Certificate Manager to an appropriate certificate map.

     * If the domain names in the new certificate match with an about-to-expire certificate, then use the [`UpdateCertificate` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateRequest) on the existing certificate resource.
     * If the new certificate has different domain names, then first use the [`CreateCertificateRequest` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#createcertificaterequest) with the new PEM (privacy-enhanced mail) files to create it. Then, use the [`UpdateCertificateMapEntry` method](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#updatecertificatemapentryrequest) to replace the old certificate's reference in the certificate map with the new one.

**Important** : You must complete this process in one API call without resulting in any downtime.




## Apply appropriate access controls

We recommend that you consider the principles of least privilege and separation of duties when configuring your access controls. The following sections explain these recommendations in more detail.

### Apply the principle of least privilege

When assigning permissions to manage certificates, consider the principle of least privilege and grant the minimum permissions needed to perform a task. We strongly recommend that you avoid using basic IAM roles. Instead, grant predefined or custom Certificate Manager and CA Service roles to mitigate any risk of security incidents related to over-privileged access.

### Plan for separation of duties

We recommend that you maintain distinct identities and permissions for certificate administrators and those who have either the certificate issuer or certificate requester role. To do so, create separate administrator and requester groups at the top of the resource hierarchy for your users.

Make sure that your administrators group is responsible for performing the following actions:

  * Manage and maintain your certificate infrastructure such as CA provisioning.
  * Configure certificate templates.
  * Manage your certificate revocation list (CRL)) and online certificate status protocol (OCSP) responders.
  * Implement security policies for your CA.

**Important:** Make sure that your administrators group contains a small number of users to reduce the risk of misconfiguration or abuse.

For projects that host a root CA, avoid assigning basic roles such as Owner (`roles/owner`), Editor (`roles/editor`), and CA Service Admin (`roles/privateca.admin`) to any user or group. This practice prevents accidental deletion, misconfiguration, and over exposure. Instead, use [Privileged Access Manager (PAM)](https://docs.cloud.google.com/iam/docs/pam-overview) for just-in-time (JIT) access as needed with justification and approvals after the root CA is installed and configured.

Make sure that the requester group is responsible for the day-to-day operations of processing certificate requests and issuing certificates based on predefined templates.

The following table lists the IAM roles that are typically associated with various job functions:

Persona | Description | IAM roles  
---|---|---  
Certificate administrators | Set up and manage CA and certificate infrastructure. | Certificate Manager Owner (`roles/certificatemanager.owner`),  
CA Service Admin (`roles/privateca.admin`)  
Certificate requester | Request certificates for workloads. | Certificate Authority Service Certificate Requester (`roles/privateca.certificateRequester`)  
Workloads (automation service accounts) | Used by workloads or in pipelines to request certificates.  | Certificate Authority Service Workload Certificate Requester (`roles/privateca.workloadCertificateRequester`)   
Security engineers or PKI owners | Manage certificate policy, revocation, and lifecycle. | CA Service Operation Manager (`roles/privateca.caManager`), Certificate Authority Service Certificate Manager (`roles/privateca.certificateManager`)  
DevOps or platform engineers | Manage the deployment of certificates on load balancers, and more. | Certificate Manager Editor (`roles/certificatemanager.editor`)  
Auditor or compliance | Monitor certificates and their usage. | Certificate Manager Viewer (`roles/certificatemanager.viewer`), Certificate Authority Service Auditor (`roles/privateca.auditor`)  
  
### Use per-project DNS authorization for multi-region and multi-cloud deployments

We recommend that you use the [per-project DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations#gcloud) approach to independently manage multiple authorizations for projects across multiple regions, multiple clouds, and across the software development lifecycle (SDLC).

Compartmentalizing DNS authorizations helps ensure that each project maintains its own distinct set of DNS records and permissions. This level of control lets each project manage its DNS configurations autonomously, without interfering with or being affected by the operations of other projects. For example, a development team can experiment with new DNS configurations for their specific application without risking any adverse impact on the production systems or other ongoing projects.

### Use CAA records to protect your domains

Certification Authority Authorization (CAA) records are a security mechanism in the Domain Name System (DNS). CAA records provide domain owners with complete control to configure the public Certification Authorities (CAs) that can issue certificates for their domains. This control is important in preventing the unauthorized issuance of certificates. With CAA in place, the attack surface for fraudulent certificates is reduced, effectively making websites more secure.

For Google-managed certificates, we recommend that you manually authorize the following for the best reliability of your certificate issuance and renewal requests:

  * [`pki.goog`](https://pki.goog/)
  * [`letsencrypt.org`](https://letsencrypt.org/)



## Cloud Logging, Cloud Monitoring, and visibility

The following sections describe the best practices for audit logging and for monitoring certificate usage and expiration.

### Enable and aggregate audit logging

To monitor all resources of your organization, aggregate the [Admin activity audit logs](https://docs.cloud.google.com/certificate-manager/docs/audit-logging#permission-type) for all services, including Certificate Manager, into a centralized location.

This lets your security team or auditor review all activity related to creating or modifying Certificate Manager and CA Service resources in one place. For more information about configuring aggregated logs, see [Aggregate and store your organization's logs](https://docs.cloud.google.com/logging/docs/central-log-storage).

### Monitor certificate usage and expiration

We recommend that you set up log-based alerts for important Certificate Manager events, such as root CA usage, certificate expiration, and certificate deletion. These alerts help you triage operations, such as a high rate of certificate-creation failures, and can trigger a downstream process to either request a new certificate or increase the quota.

Configure the following log alerts and policies for privilege-related operations:

  * [Certificates close to expiry](https://docs.cloud.google.com/certificate-manager/docs/logs-metrics#configure_log_alerts)
  * [Expired Public certificates](https://docs.cloud.google.com/certificate-manager/docs/logs-metrics#configure_log_alerts)
  * [CA expiring in 30 days](https://docs.cloud.google.com/certificate-authority-service/docs/monitoring#ca_expiring_in_30_days)
  * [High rate of certificate creation failures](https://docs.cloud.google.com/certificate-authority-service/docs/monitoring#high_rate_of_certificate_creation_failures)
  * [Expired CA certificates](https://docs.cloud.google.com/certificate-authority-service/docs/monitoring#enabling_recommended_alerts)
  * [CA Service KMS key issue](https://docs.cloud.google.com/certificate-authority-service/docs/monitoring#monitoring_gauge_metrics)



## Compliance requirements

Typically, compliance frameworks specify high-level expectations and objectives for certificate management rather than for specific products or configurations.

For example, the Payment Card Industry Data Security Standard (PCI DSS) and National Institute of Standards and Technology (NIST) require organizations to document and implement rotation periods for signing keys. They also mandate the continuous monitoring of inventory and all trusted signing keys and certificates that protect cardholder data.

For more information about how Google Cloud services can help meet various compliance framework requirements, see the following resources:

  * [Google Cloud compliance offerings](https://cloud.google.com/security/compliance/offerings)
  * [CA Service security compliance](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-compliance#compliance)
  * [PCI Data Security Standard compliance](https://docs.cloud.google.com/architecture/pci-dss-compliance-in-gcp)



## What's next

  * [Best practices for Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/best-practices)
  * [Architecture of an mTLS deployment](https://docs.cloud.google.com/load-balancing/docs/mtls#architecture)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
