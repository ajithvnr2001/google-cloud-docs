---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/cas-overview/
title: Certificate Authority Service overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:25.545361+00:00
---

# Certificate Authority Service overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/cas-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Certificate Authority Service overview Stay organized with collections  Save and categorize content based on your preferences. 

Certificate Authority Service is a scalable Google Distributed Cloud (GDC) air-gapped service that lets you simplify, automate, and customize the deployment, management, and security of private certificate authorities (CA). Private certificate authorities are one of the most common ways to authenticate users, machines, or services over networks. Private CAs issue digital certificates for entity identity, issuer identity, and cryptographic signatures.

With CA Service, you can create both root CAs and sub CAs:

  * Root CAs: The root CA has a self-signed certificate. This certificate type sits at the top of the certificate chain.
  * Sub CAs: The signer of the CA certificate is either another CA created in the CA Service, or an external CA.



CA Service provides the following capabilities:

  * **Manage certificate authorities:** Create and manage your own root CAs and subordinate CAs. Subordinate CAs can be chained to a root CA managed within the service or to an external root CA.

  * **Issue certificates:** Request certificates for your applications and services. CA Service supports issuing certificates using ACME-enabled CAs or ACME-disabled CAs through a `CertificateRequest` custom resource.

  * **Use predefined certificate templates:** Simplify and standardize certificate creation using predefined certificate templates. These templates offer pre-configured X.509 parameters tailored for common use cases, and enforce compatibility with the issuing CA's allowed profile.

  * **Revoke certificates:** Invalidate certificates before their scheduled expiration date if they can no longer be trusted (such as due to key compromise). CA Service enables this by publishing Certificate Revocation Lists (CRLs), which clients can check to verify a certificate's status.




## What's next

  * [Create a root CA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/create-root-ca)
  * [Create a managed subordinate certificate authority](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/create-subca)
  * [Request a certificate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/request-cert)
  * [Predefined certificate templates](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/predefined-certificate-templates)
  * [Revoke a certificate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/ca-service/revoke-cert)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
