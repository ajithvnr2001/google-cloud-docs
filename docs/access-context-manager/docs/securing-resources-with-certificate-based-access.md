---
url: https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access/
title: Context-Aware Access with mTLS overview \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:54.777700+00:00
---

# Context-Aware Access with mTLS overview  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Context-Aware Access with mTLS overview Stay organized with collections  Save and categorize content based on your preferences. 

You can use Context-Aware Access with mTLS, which is also known as certificate-based access (CBA) to require verified X.509 certificates for access to Google Cloud resources. The additional credential provides a stronger signal of device identity and helps protect your organization from credential theft or accidental loss by requiring that both the user credentials and the original device certificate are present before granting access.

Relying only on credentials, like bearer tokens, to grant access to the Google Cloud APIs and resources can put you at risk. Those credentials can be exposed by user error or become prime targets for attackers. If attackers obtain the credentials, they can replay the credentials to access resources.

By using CBA, you enhance the security of your resources by requiring an additional authorization factor, a device certificate. Device certificates are validated and verified using a mutual TLS handshake. This requires users to prove possession of the private key associated with the certificate, thereby providing a strong signal of device identity.

Following is a high-level illustration of the CBA access flow:

![CBA access flow](https://docs.cloud.google.com/access-context-manager/images/cba-overview.svg)

### The benefits of using Google CBA

Following are some of the benefits of using CBA.

Comprehensive Security
    Protects your important resources by preventing access using stolen credentials from untrusted devices, such as cookie theft.
    Protects all Google Cloud API requests regardless of access points, including on-premises or Google networks, and web browsers or desktops applications.
Fine-grained Policy Control
    Works seamlessly with VPC Service Controls service perimeters and lets you to specify fine-grained access control over your resources.
    Works seamlessly with user groups and lets you apply CBA to a group of users.
Good Developer Experience
    Automated CBA support in common libraries and tools, such as the gcloud CLI, which reduces the programming cost of using CBA.

## What's next

  * [Understand mutual TLS at Google Cloud](https://docs.cloud.google.com/access-context-manager/docs/understand-mtls)
  * [Set up certificate-based access](https://docs.cloud.google.com/access-context-manager/docs/set-up-cba)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
