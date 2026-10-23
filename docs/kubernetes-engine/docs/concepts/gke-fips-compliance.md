---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-fips-compliance/
title: About FIPS-validated encryption in GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:58.298376+00:00
---

# About FIPS-validated encryption in GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-fips-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  About FIPS-validated encryption in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how Google Cloud and Google Kubernetes Engine (GKE) maintain compliance with the [Federal Information Processing Standards (FIPS)](https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips) as you process and transmit data through your GKE clusters that run on Google Cloud.

This page is intended for security managers, security engineers, and compliance officers who want to meet strict data security and privacy requirements related to FIPS. You can also use this page to show an auditor that GKE on Google Cloud implements FIPS-validated protections for data security by default.

## Key takeaways about FIPS-validated encryption in GKE

  * The FedRAMP® security controls for data encryption in transit (SC-28) and at rest (SC-8(1)) require that your data is encrypted using FIPS 140-2 validated cryptographic modules or newer. These security controls don't explicitly mandate enabling "FIPS mode" at the operating system (OS) level. Additionally, OS-level FIPS mode isn't a guarantee of compliance.
  * Data that's stored in FedRAMP authorized Google Cloud systems is encrypted at rest by default using FIPS 140-2 validated cryptographic modules or newer. As long as your data is stored in these authorized systems, the data meets the FedRAMP requirements for protecting data at rest (security control SC-28). For a list of authorized systems, see the [FedRAMP High services in scope](https://cloud.google.com/security/compliance/fedramp#services-in-scope).
  * Data that you transmit inside the Google Cloud Virtual Private Cloud (VPC) network is automatically encrypted and is protected by authentication and authorization mechanisms. VPC is authorized at FedRAMP High. As long as your data is being transmitted within the Google Cloud VPC network, the data meets the FedRAMP requirements for protecting data in transit (security control SC-8(1)).
  * You don't need to build your applications using FIPS-compliant build processes to meet the FedRAMP requirements for data protection at rest and in transit. This is because data that's transmitted within the Google Cloud VPC network and is stored in FedRAMP authorized Google Cloud storage systems is protected in compliance with these FedRAMP requirements for data protection by default.



## About FIPS and FedRAMP

The Federal Risk and Authorization Management Program (FedRAMP) is a US government program that defines a standardized approach to security and risk assessment for cloud technologies. GKE is included in the list of Google Cloud services that have FedRAMP High provisional authority to operate (P-ATO). To learn more about the Google Cloud FedRAMP P-ATO, see the [Google Cloud FedRAMP overview](https://cloud.google.com/security/compliance/fedramp#fedramp).

FIPS is a publicly announced set of standards issued by the National Institute of Standards and Technology (NIST). FIPS publication 140-2 defines the requirements for approving cryptographic modules. For details, see [FIPS 140-2 on NIST](https://csrc.nist.gov/pubs/fips/140-2/upd2/final).

The FedRAMP High P-ATO includes controls for protecting data in transit (SC-8(1)) and protecting data at rest (SC-28(1)) using FIPS-validated cryptographic modules.

## Default FIPS-validated data protection in GKE

The following sections explain how Google Cloud and GKE implement FIPS-validated encryption to protect data at rest and in transit. This information is covered in more detail in the Google Cloud system security plan (SSP), which you can request from your Google Cloud sales team, Google Cloud representative, or from the Google Cloud FedRAMP Program Management Office if you're a government customer. For details, see [Google Cloud FedRAMP Compliance](https://cloud.google.com/security/compliance/fedramp#google-clouds-fedramp-compliance).

### FIPS-validated data protection at rest

GKE data is encrypted at rest using a FIPS 140-2 validated Google Cloud encryption module named _BoringCrypto_. For details, see [FIPS 140-2 validation in Google Cloud](https://cloud.google.com/security/compliance/fips-140-2-validated).

For more information about encryption at rest, see the following resources:

  * [Default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption)
  * [Google Cloud services in scope for FedRAMP P-ATO](https://cloud.google.com/security/compliance/fedramp)
  * [NIST 800-57: Recommendations for Key Management](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
  * [NIST BoringCrypto module validation](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4444)
  * [Encrypt your data in-transit in GKE with user-managed encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-inter-node-transparent-encryption)



### FIPS-validated data protection in transit

The Google Cloud VPC has a FedRAMP High P-ATO. Any data that you transmit within your VPC network is automatically encrypted. In GKE, this means that all traffic to and from containers, Pods, the `kubelet` process on each node, all nodes, control plane instances, and other Google Cloud services within the VPC is protected in transit. All connections to Google APIs use transport layer security (TLS) 1.2 or higher to encrypt network traffic. _No additional action is needed to be FIPS-compliant for data protection in transit within the Google Cloud VPC network._

For more information about how your data is encrypted in transit, see the [Encryption in transit whitepaper](https://docs.cloud.google.com/docs/security/encryption-in-transit).

## Recommendations for protecting data outside of Google Cloud

The default encryption of data in transit for GKE and Google Cloud apply only within the Google Cloud VPC network. You must use FIPS-compliant cryptography to protect data that's outside of the VPC network boundary. The following recommendations help you to ensure that all incoming and outgoing data outside of your Google Cloud FIPS environment in transit is encrypted with FIPS-compliant cryptography.

### Intercept and encrypt incoming traffic from the internet

For incoming traffic to your Google Cloud environment from the internet, use SSL policies in Google Cloud load balancers to define an allowed set of FIPS-validated cryptographic ciphers or mechanisms with which the data must be protected when it enters the Google Cloud environment. For details, see the following resources:

  * [SSL policies for SSL and TLS protocols](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)
  * [Create SSL policies with a custom profile](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies#create-an-ssl-policy-with-a-custom-profile)
  * [Encryption between proxy load balancers and backends](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends#encryption-to-backends)



### Intercept and encrypt outbound traffic to the internet

Define a perimeter that limits outbound data connections to a set of known third parties that you trust by [configuring firewalls](https://docs.cloud.google.com/firewall/docs/firewalls). Diagram and document any external network requirements, such as pulling data from sources like GitHub, and where those external connections will occur within your environment. Consider using a reverse proxy to intercept outbound traffic from your VPC.

If you have HTTP traffic that's leaving the perimeter of your FedRAMP-compliant Google Cloud environment, consider setting up an HTTP forward proxy to intercept the data before it leaves the environment. Re-encrypt the data using a FIPS 140-2 validated cryptographic module before you allow it to leave your perimeter. This approach is more manageable at scale than trying to ensure that every internal client uses compliant encryption libraries for external communication.

### Enable private nodes

GKE lets you disable the external IP address for new nodes in your clusters, so that workloads that run on the nodes can't communicate with the internet by default. Use the `http_proxy` or `https_proxy` environment variables to send all traffic to your configured HTTP proxy.

You can configure more transparent interception of this traffic with routing rules. However, because you're proxying TLS traffic, the proxy can't be completely transparent to the applications you run on GKE.

For details, see the following resources:

  * [About network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#cluster-access)
  * [Restrict network access to the control plane and nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_access_to_the_control_plane)



### Use Cloud VPN for network layer connections to GKE

You might sometimes need an encrypted network layer connection to your GKE clusters. For example, you might need to set up FIPS-compliant networking between GKE nodes and on-premises nodes. Cloud VPN is a FedRAMP High authorized service that encrypts your data in transit between your VPC network and your on-premises network. For details, see [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

### Use Cloud KMS for cryptographic operations

If you need to perform cryptographic operations in your Google Cloud environment, use [Cloud Key Management Service](https://cloud.google.com/security/products/security-key-management). Cloud KMS is a FedRAMP High authorized service. Cloud KMS lets you perform cryptographic operations that comply with either FIPS 140-2 Level 1 or Level 3. For details, see the following resources:

  * [Key backends and protection levels](https://docs.cloud.google.com/docs/security/key-management-deep-dive#key_backends_and_protection_levels)
  * [Raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption)



### Build FIPS-validated libraries in GKE workloads

To use the BoringCrypto encryption module in your GKE applications, install BoringSSL. BoringSSL is an open source fork of OpenSSL that includes the BoringCrypto library. To build, compile, and statically link the BoringCrypto module to BoringSSL, see section 12.1, "Installation Instructions", in [the BoringCrypto FIPS 140-2 Security Policy PDF](https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp4407.pdf)

### Consider third-party FIPS-compliant container images

We recommend that you use proxies at the boundary of your FIPS-compliant Google Cloud environment to comprehensively enforce FIPS compliance. You can also run FIPS-compliant workloads without being limited to node host machines that have FIPS-compliant kernels. Some third-party vendors provide container images that use a separate, FIPS-compliant source of entropy.

Evaluate the third-party vendor's implementation to verify that it is actually FIPS-compliant.

## What's next

  * [Read the Google Cloud FedRAMP implementation guide](https://docs.cloud.google.com/docs/security/compliance/fedramp-implementation-guide)
  * [Use an organization policy constraint to restrict TLS to version 1.2](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
