---
url: https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls/
title: Overview of policy controls \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:54.491678+00:00
---

# Overview of policy controls  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of policy controls

Policy controls enforce standards for the operation of the certificate authority (CA) and the certificates that the CA issues. Policy controls are the rules and restrictions that you put in place to define how the CA will issue certificates and which parameters can be included in a request and which values are accepted. In Certificate Authority Service, policy controls are one of two types:

  * Coarse-grained policies such as [certificate issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls#issuance-policies): Certificate issuance policies apply to the entire CA pool and define high-level constraints such as permitted key types, allowed certificate lifetimes, and subject and Subject Alternative Name (SAN) constraints.

  * Fine-grained policies such as [certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls#certificate-template): Certificate templates let you define which certificate types can be issued and who has the authority to issue them, preventing misuse and maintaining security. Certificate templates offer more granular control by letting you define different types of certificates for different purposes. For example, you can create certificate templates for specific use cases like TLS certificates for web servers and code signing certificates for developers. You can also create templates for different departments or teams allowing each team to request certificates with the specific permissions they need.




In addition to the certificate issuance policies and certificate templates, you can also enforce specific policy controls such as [name constraints](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls#name-constraints) to prevent a CA from issuing certificates for unauthorized domains or entities.

## About certificate issuance policies

A certificate issuance policy defines controls over all certificate issuance within a CA pool. A CA Manager can attach a [certificate issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancepolicy) to a CA pool to define restrictions on the kind of certificates that the CAs in the CA pool can issue. Certificate issuance policies help you do the following:

  * Add constraints on allowed subject and SANs that can be requested. This validates who or what can be identified in the certificate, such as only allowing certificates for your company's domain.
  * Define restrictions on certificate identities, certificate lifetimes, key types, backdate duration, and certificate request modes.
  * Append specific X.509 extensions into all issued certificates.



We recommend using a certificate issuance policy when either one or both of the following scenarios apply to you:

  1. Your CA pool is designed to issue certificates according to a single, well-defined profile. For example, you have a dedicated CA pool that issues certificates only for your company's internal web servers. These certificates all need the same basic parameters.

     * All issued certificates have `O=My organization` in their subject.
     * All DNS names end with `.cymbalgroup.com`.
     * They're valid for 1 year.

A certificate issuance policy enforces these rules and ensures that every certificate issued from this CA pool adheres to this profile.

  2. You want to define a common baseline for X.509 extensions and additional restrictions that apply to all the certificate issuance profiles. For example, you have different types of certificates such as employee email signing certificates (valid for 2 years) and TLS certificates for public-facing websites (valid for 1 year). You can define a baseline issuance policy that applies to all certificates:

     * All certificates must include the company name in the subject.
     * All must use a specific set of X.509 extensions for your organization's security standards.

Then, you can use certificate templates to define the specific variations for each certificate type on top of that baseline.




For information about adding a certificate issuance policy, see [Add a certificate issuance policy to a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy#add-issuance-policy).

## About certificate templates

A certificate template represents a relatively static and well-defined certificate issuance schema within an organization. By using certificate templates, certificates issued from various CA pools share the same format and properties, regardless of the issuing CA. The `CertificateTemplate` resource includes the following:

  * A [Common Expression Language (CEL)](https://opensource.google/projects/cel) expression that is evaluated against the requested subject and SANs in all certificate requests that use the template. For more information about using CEL, see [Using CEL](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).
  * An allowlist specifying whether the subject or subject alternative name can be copied from the end-user request to the issued certificate.
  * An optional allowlist specifying which X.509 extensions, if any, can be copied from the end-user request to the issued certificate.
  * An optional set of X.509 extension values that are added to all the issued certificates that use the template.



A certificate template can become a complete vertical certificate issuance framework. For more details, see the full [CertificateTemplate](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.certificateTemplates#CertificateTemplate) message definition.

You can use a certificate template when you have a well-defined certificate issuance scenario. You can use certificate templates to enable consistency across certificates issued from different CA pools. You can also use a certificate template to restrict the kinds of certificates that different individuals can issue.

You can also use a combination of certificate templates and Identity and Access Management (IAM) conditional role bindings to define constraints that apply to certificate requests made by specific service accounts. For example, you can create a certificate template that allows only DNS names ending with `.altostrat.com`. Then, you can [add a conditional role binding](https://docs.cloud.google.com/iam/docs/allow-policies#conditional-bindings) to grant the service account `my-service-account@my-project.iam.gserviceaccount.com` permission to use only that template when requesting certificates from a specific CA Pool. This limits the service account to issuing certificates with that specific SAN restriction.

To learn how to create certificate templates, see [Create a certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template).

## CA certificate name constraints

CA Service enforces name constraints in CA certificates as defined in the [Name Constraints](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.10) section of the RFC 5280 document. Name constraints let you control which names are permitted or excluded in certificates issued from CAs.

Name constraints are implemented using the [Name Constraints extension in X.509 certificates](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters#nameConstraints). This extension lets you specify permitted and excluded namespaces for various name forms, such as DNS names, IP Addresses, email addresses, and URLs.

For example, you can create a CA with name constraints to enforce the following conditions:

  * Only `myownpersonaldomain.com` and its subdomains can be used as DNS names.
  * `examplepetstore.com` and its subdomains are prohibited as DNS names.



Name constraints are defined within the CA's own certificate. This means that any certificates issued by that CA are bound by these constraints. When a CA issues a certificate, it checks the requested subject name and any Subject Alternative Names (SANs) against the defined name constraints. If any name violates the constraints, the certificate issuance is rejected.

You can specify name constraints only at the time of creating the CA.

## Benefits of using policy controls

Policy controls help you achieve the following:

  * Enhance security by limiting what types of certificates can be issued and by reducing the risk of unauthorized certificates being created and misused.
  * Meet regulatory requirements and industry best practices for certificate management.
  * Reduce manual effort and potential errors. Certificate templates make it easier to issue certificates consistently and efficiently.
  * Establish trust as clearly defined policies and strong controls increase confidence in the certificates you issue.



## Enforcing policy controls

When someone requests a certificate, CA Service evaluates these policy controls at the following levels:

  1. Identity and Access Management (IAM) permissions: First, the service checks if the requester has the necessary IAM permissions to create certificates or use the specified certificate template. This ensures that only authorized users can obtain certificates.

  2. Certificate issuance policy: The service then validates the certificate request against the CA pool's issuance policy. This ensures that the request meets the general requirements for certificates issued from that CA.

  3. Certificate template: If a template is used, the request is further validated against the template's specific constraints. This ensures that the certificate is appropriate for its intended use.




X.509 extensions from the CA pool's certificate issuance policy and the certificate template are added to the certificate, and certain values are dropped based on those same policies. Before signing the certificate, name constraints in CA certificates are validated against the certificate to ensure the subject is compliant.

## Policy conflicts

When using different policy control mechanisms in conjunction, there is a possibility that policies on different levels can conflict. For example, a certificate template might allow a key type (like `ECDSA`) that the CA pool's issuance policy forbids. Or the certificate template and the issuance policy might specify different values for the same X.509 extension.

To learn how to manage policy conflicts in CA Service, see [About policy conflicts](https://docs.cloud.google.com/certificate-authority-service/docs/policy-conflicts).

## What's next

  * Learn how to [implement policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/manage-policy-controls).
  * Learn about [using Common Expression Language (CEL)](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
