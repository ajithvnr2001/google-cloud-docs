---
url: https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview/
title: Certificate Authority Service overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:50.269035+00:00
---

# Certificate Authority Service overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Certificate Authority Service overview

Certificate Authority Service (CA Service) is a highly scalable Google Cloud service that lets you simplify and automate the deployment, management, and security of private certificate authorities (CA). Private CAs issue digital certificates that include entity identity, issuer identity, and cryptographic signatures. Private certificates are one of the most common ways to authenticate users, machines, or services over networks. Private certificates are often used in DevOps environments to protect containers, microservices, virtual machines, and service accounts.

Using CA Service, you can do the following:

  * Create custom root and subordinate CAs.
  * Define the subject, key algorithm, and location of the CA. 
  * Select a subordinate CA's region independent of its root CA's region. 
  * Create reusable and parameterized templates for common certificate issuance scenarios.
  * Bring your own root CA and configure other CAs to chain up to the existing root CA running on-premises or anywhere else outside Google Cloud. 
  * Store your private CA keys using [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm), which is FIPS 140-2 Level 3 validated and available in several regions across the Americas, Europe, and Asia Pacific. 
  * Obtain logs and gain visibility into who did what, when, and where with [Cloud Audit Logs](https://docs.cloud.google.com/audit-logs).
  * Define granular access controls with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) and virtual security perimeters with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls?hl=en).
  * Manage high volumes of certificates knowing that CA Service supports issuing up to 25 certificates per second per CA (DevOps tier), which means that each CA can issue millions of certificates. You can create multiple CAs behind one issuance endpoint called a CA pool and distribute the incoming certificate requests across all the CAs. Using this feature, you can effectively issue up to 100 certificates per second.
  * Manage, automate, and integrate private CAs in whichever way is most convenient for you: using APIs, the Google Cloud CLI, the Google Cloud console, or [Terraform](https://www.terraform.io/).



## Certificate use cases

You can use your private CAs to issue certificates for the following use cases:

  * **Software supply chain integrity and code identity** : Code signing, artifact authentication, and application identity certificates.
  * **User identity** : Client authentication certificates used as user identity for zero trust networking, VPN, document signing, email, smartcard, and more.
  * **IoT and mobile device identity** : Client authentication certificates used as device identity and authentication, for example, wireless access.
  * **Intraservice identity** : mTLS certificates used by microservices.
  * **Continuous integration and continuous delivery (CI/CD) channels** : Code signing certificates used throughout the CI/CD build to improve code integrity and security.
  * **Kubernetes and Istio** : Certificates to secure connections between the Kubernetes and Istio components.



## Why choose a private PKI

In a typical Web Public Key Infrastructure (PKI), millions of clients across the world trust a set of independent certificate authorities (CAs) to assert identities (such as domain names) in certificates. As part of their responsibilities, CAs commit to only issuing certificates when they have independently validated the identity in that certificate. For example, a CA typically needs to verify that somebody requesting a certificate for the domain name `example.com` actually controls the said domain before they issue a certificate to them. Since those CAs can issue certificates for millions of customers where they might not have an existing direct relationship, they are limited to asserting identities that are publicly verifiable. Those CAs are limited to certain well-defined verification processes that are consistently applied across the Web PKI.

Unlike Web PKI, a private PKI often involves a smaller CA hierarchy, which is directly managed by an organization. A private PKI sends certificates only to clients that inherently trust the organization to have the appropriate controls (for example, machines owned by that organization). Since the CA admins often have their own ways of validating identities for which they issue certificates (for example, issuing certificates to their own employees), they aren't limited by the same requirements as for Web PKI. This flexibility is one of the main advantages of private PKI over Web PKI. A private PKI enables new use cases such as securing internal websites with short domain names without requiring unique ownership of those names, or encoding alternative identity formats (such as [SPIFFE IDs](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/)) into a certificate.

In addition, the Web PKI requires all CAs to log every certificate they've issued to public [Certificate Transparency](https://certificate.transparency.dev/howctworks/) logs, which may not be required for organizations issuing certificates to their internal services. Private PKI allows organizations to keep their internal infrastructure topology, such as the names of their network services or applications, private from the rest of the world.

## What's next

  * Understand [CA Service pricing](https://cloud.google.com/certificate-authority-service/pricing).


  * Learn about [security and compliance](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-compliance).


  * Review CA Service [locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).


  * Get started with the [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs/create-certificate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
