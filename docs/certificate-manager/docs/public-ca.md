---
url: https://docs.cloud.google.com/certificate-manager/docs/public-ca/
title: Public CA \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:36:53.008144+00:00
---

# Public CA  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/public-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback 

#  Public CA Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Public Certificate Authority to provision and deploy widely trusted X.509 certificates after validating that the certificate requester controls the domains. Public CA lets you directly and programmatically request publicly trusted TLS certificates that are already in the root of trust stores used by major browsers, operating systems, and applications. You can use these TLS certificates to authenticate and encrypt internet traffic.

Public CA lets you manage high volume use cases that other CAs have been unable to support. If you are a Google Cloud customer, you can request TLS certificates for your domains directly from Public CA.

Most certificate-related problems are due to human error or oversight, so we recommend automating certificate lifecycles. Public CA uses the [Automatic Certificate Management Environment (ACME)](https://tools.ietf.org/html/rfc8555) protocol for the automated provisioning, renewal, and revocation of certificates. Automated certificate management reduces downtime that expired certificates can cause and minimizes operational costs.

Public CA provisions TLS certificates for several Google Cloud services, such as [App Engine](https://docs.cloud.google.com/appengine/docs), [Cloud Shell](https://docs.cloud.google.com/shell/docs), [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs) and [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs).

## Who should use Public CA

You can use Public CA for the following reasons:

  * If you are looking for a TLS provider with high ubiquity, scalability, security, and reliability.
  * If you want most, if not all, TLS certificates for your infrastructure, including on-premises workloads and cross-cloud provider setups, from a single cloud provider.
  * If you need control and flexibility over the TLS certificate management to customize it to your infrastructure requirements.
  * If you want to automate the TLS certificate management but cannot use managed certificates in Google Cloud services, such as [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-certs) or [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs).



We recommend that you use publicly trusted certificates only when your business requirements do not allow another option. Given the historical cost and complexity of maintaining public key infrastructure (PKI) hierarchies, many enterprises use public PKI hierarchies even when a private hierarchy makes more sense.

Maintaining public and private hierarchies has become much simpler with multiple Google Cloud offerings. We recommend that you carefully choose the right type of PKI for your use case.

For non-public certificate requirements, Google Cloud offers two easy-to-manage solutions:

  * **Anthos Service Mesh** : [Cloud Service Mesh](https://docs.cloud.google.com/anthos/service-mesh) includes fully automated mTLS certificate provisioning for workloads running in GKE Enterprise using [Cloud Service Mesh certificate authority (Cloud Service Mesh certificate authority)](https://docs.cloud.google.com/service-mesh/docs/overview#security_features).

  * **Certificate Authority Service** : [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs) lets you deploy, manage, and secure custom private CAs efficiently without managing infrastructure.




## Benefits of Public CA

Public CA provides the following benefits:

  * **Automation** : As internet browsers aim for fully encrypted traffic and the reduction of certificate validity periods, there is a risk of using expired TLS certificates. Certificate expiration can lead to website errors, and can cause service outages. Public CA avoids the problem of certificate expiration by letting you set up your HTTPS server to automatically obtain and renew the necessary TLS certificates from our ACME endpoint.

  * **Compliance** : Public CA undergoes regular, rigorous independent audits of security, privacy, and compliance controls. The [Webtrust seals](https://pki.goog/) granted as a result of these annual audits demonstrate Public CA's conformity with all relevant industry standards.

  * **Security** : The architecture and operations of Public CA are designed to the highest level of security standards and regularly runs independent assessments to confirm the security of the underlying infrastructure. Public CA either meets or exceeds all the controls, operational practices, and security measures mentioned in the [Google Security whitepaper](https://cloud.google.com/security/overview/whitepaper).

Public CA's focus on security extends to features such as multi-perspective domain validation. Public CA's infrastructure is globally distributed. Therefore, Public CA requires a high degree of agreement across geographically diverse perspectives, which provides protection against [Border Gateway Protocol (BGP) hijacking](https://wikipedia.org/wiki/BGP_hijacking) and [Domain Name Server (DNS) hijacking](https://wikipedia.org/wiki/DNS_hijacking) attacks.

  * **Reliability** : The use of Google's proven technical infrastructure makes Public CA a highly available and scalable service.

  * **Ubiquity:** The strong browser ubiquity of [Google Trust Services](https://pki.goog/) helps ensure that services using certificates that Public CA issues work on the widest possible range of devices and operating systems.

  * **Streamlined TLS solutions for hybrid setups** : Public CA lets you build a custom TLS certificate solution that uses the same CA for diverse scenarios and use cases. Public CA effectively serves the use cases where workloads are running on-premises or in a cross-cloud provider environment.

  * **Scale** : Certificates have often been costly to obtain and difficult to provision and maintain. By offering access to large volumes of certificates, Public CA lets you utilize and manage certificates in ways that were previously considered impractical.




## Use Public CA with Certificate Manager

To use the Public CA feature of Certificate Manager, you must be familiar with the following concepts:

  * **ACME client**. An Automatic Certificate Management Environment (ACME) client is a certificate management client that uses the [ACME protocol](https://datatracker.ietf.org/doc/html/rfc8555). Your ACME client must support external account binding (EAB) to work with Public CA.

  * **External account binding (EAB)**. You must bind each ACME account you are using with Certificate Manager Public CA to the target Google Cloud project using external account binding. To do this, you must register each ACME account using a secret linked to its corresponding Google Cloud project. For more information, see [External account binding](https://datatracker.ietf.org/doc/html/rfc8555#section-7.3.4).




### Public CA challenges

When you use Public CA to request a certificate, Certificate Manager asks you to prove your control over the domains listed in that certificate. You can prove domain control by solving challenges. Public CA authorizes the domain names after you prove your control of the target domains.

After you obtain the required authorizations, you can request certificates that are valid only for a specific duration. After this duration, you must revalidate the domain name by solving one of the three challenge types to continue requesting certificates.

#### Challenge types

Public CA supports the following types of challenges:

  * **HTTP challenge**. This challenge involves creating a file at a well-known location on an HTTP server (port 80) for Public CA to retrieve and verify. For more information, see [HTTP challenge](https://datatracker.ietf.org/doc/html/rfc8555#section-8.3).

  * **TLS-Application Layer Protocol Negotiation (ALPN) challenge**. Requires a server to provide a specific certificate during a TLS negotiation on port 443 to prove control over a domain. For more information, see [ACME TLS-ALPN challenge extension](https://datatracker.ietf.org/doc/html/rfc8737).

  * **DNS challenge**. Requires adding a specific DNS record at a defined location to prove control over a domain. For more information, see [DNS challenge](https://datatracker.ietf.org/doc/html/rfc8555#section-8.4).




If you use the HTTP challenge or the TLS-ALPN challenge to validate a domain name, the client can only request the validated domain names to be included in a certificate. If you use the DNS challenge, the client can also request subdomains of that domain name to be included in a certificate.

For example, if you validate `*.myorg.example.com` using the DNS challenge, then `subdomain1.myorg.example.com` and `subdomain2.myorg.example.com` are automatically covered by the wildcard certificate. However, if you validate `myorg.example.com` using an HTTP or TLS-ALPN challenge, the client can only request to include `myorg.example.com` in the certificate and you cannot validate `*.myorg.example.com` using the non-DNS challenges.

#### Challenge solution logic

The Public CA challenge logic is as follows:

  1. Public CA provides a random token.
  2. The client makes the token available at a well-defined location. The location depends on the challenge.
  3. The client indicates to Public CA that it has prepared the challenge.
  4. Public CA checks if the token present at the expected location matches the expected value.



The domain name is authorized after this process is completed. The client can request a certificate with that domain name in it. You need to solve only one challenge per domain name.

## What's next

  * [Request a certificate using Public CA (tutorial)](https://docs.cloud.google.com/certificate-manager/docs/public-ca-tutorial)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
