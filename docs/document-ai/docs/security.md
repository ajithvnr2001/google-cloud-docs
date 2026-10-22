---
url: https://docs.cloud.google.com/document-ai/docs/security/
title: Document AI security and compliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:43.245862+00:00
---

# Document AI security and compliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Document AI security and compliance Stay organized with collections  Save and categorize content based on your preferences. 

Following are questions and answers applicable in various areas.

## Security

To ensure service security in Document AI, review the following topics.

### How does Google protect and ensure the security of the data I send to Document AI?

Refer to the [Google Cloud Security](https://docs.cloud.google.com/security/solutions) page, which describes the security measures in place for Google Cloud Services.

### What security features does Document AI offer to protect from horizontal attacks that move system to system?

Document AI supports the following:

  * [Data residency](https://cloud.google.com/terms/data-residency)
  * [Deny policy](https://docs.cloud.google.com/iam/docs/deny-overview)
  * [VPC Service Controls (VPC-SC)](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products)
    * [Identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups).
  * [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services)
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/using-other-products)
    * [Using CMEK with Document AI](https://docs.cloud.google.com/document-ai/docs/cmek)



## Security compliance

This section describes the questions related to compliance.

### What compliance does Document AI offer?

Google Cloud undergoes regular independent third-party audits to verify alignment with security, privacy, and compliance controls. Google Cloud has regular audits for standards such as ISO 27001, ISO 27017, ISO 27018, SOC 2, SOC 3, and PCI DSS.

You can read more about Google Cloud compliance on the [Compliance resource center](https://docs.cloud.google.com/security/compliance).

### Is Document AI FedRAMP compliant?

Document AI is [FedRAMP High compliant](https://docs.cloud.google.com/security/compliance/fedramp).

### Is Document AI HIPAA compliant?

Document AI is [HIPAA compliant](https://docs.cloud.google.com/security/compliance/hipaa-compliance).

## Security data usage

This section describes data inquiries.

### Does Google use customer data to improve models?

No. Google does not use any of your content (such as documents and predictions) for any purpose except to provide you with the Document AI service. See section 17 of the [Google Cloud Terms of Service](https://cloud.google.com/terms/service-terms).

At Google Cloud, we never use customer data to train our Document AI models.

For more information, see the [Transparency & data protection](https://docs.cloud.google.com/transparency) page.

### In the future, will Google share the document I send to Document AI?

We won't make the document that you send available to the public or share it with anyone else, except as necessary to provide the Document AI service. For example, sometimes we may need to use a third-party vendor to help us provide some aspect of our services, such as storage or transmission of data. Our vendors are under appropriate security and confidentiality contractual obligations. We don't share documents you send with other parties or make them public for any other purpose.

### How long and where will Google store documents I send to Document AI, their results, or other information about requests on its servers? Can I access it?

![security.1](https://docs.cloud.google.com/static/document-ai/docs/images/manage/security-1.png)

When you send a document to Document AI using a batch request, we must store that document (encrypted with an ephemeral key, meaning that no human has access to it) for a short period of time in order to perform the analysis and return the results to you. For batch operations, the stored document is typically deleted immediately after the processing, with a failsafe [Time to live (TTL)](https://en.wikipedia.org/wiki/Time_to_live) of one day. If the batch abends abnormally, the data may persist with a TTL of up to one day.

### Synchronous processes

![security-2](https://docs.cloud.google.com/static/document-ai/docs/images/manage/security-2.png)

For online (immediate response) operations, the document data (sent in the request) is processed in memory, encrypted in flight, and not persisted to disk. Google also temporarily logs some metadata about your Document AI API requests (such as the time the request was received and the size of the request) to improve our service and combat abuse.

For more information, see [Encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit) and [Regions](https://docs.cloud.google.com/document-ai/docs/regions).

### Does Google claim ownership of the content I send in the request to Document AI

Google does not claim any ownership in any of the content (including documents and predictions) that you transmit to Document AI. Documents and custom models are considered to be (private) customer data. We never use customer data to improve our models. In the rare circumstance where both parties agree to such an arrangement, an explicit data sharing agreement is crafted.

### What is considered Personally Identifiable Information (PII) that needs to be redacted on documents before being shared with Google?

**Note:** _Sharing_ refers to sending documents to Google for support and professional services purposes. It does not refer to documents processed through Document AI. Such documents are considered private customer data, much like Cloud Storage. No Google employee ever sees them nor extracts their data.

For document sharing purposes, PII is any information defined as personal identifiable data under applicable laws. Customers must redact the documents prior to sharing them with Google, for example when voluntarily done for technical support purposes to reproduce a problem.

Examples of PII include but are not limited to:

  * Date of birth, for example: `2/10/1988`
  * Names of individuals, for example: `Kiran Darko`
  * Personal address, for example: `Evergreen terrace 123`
  * Email address of individuals, for example: `rivelro@test-mail.com`
  * Telephone number of individuals, for example: `636-555-3226`
  * Driver's license number
  * National ID number
  * Employer identification number
  * Bank account information: account IDs, routing numbers, SWIFT IDs
  * Payment card number
  * Gender, for example: `Female, Male, Nonbinary`
  * Ethnicity, for example: `Berber, Italian, Japanese, Latino, Ukrainian`
  * Usernames, ID number of third parties
  * Passport number, for example: `AA1001111`
  * Marital status, for example: `Single, Divorced`
  * Number of allowances or exemptions
  * Dependent names
  * Vehicle identifiers (VIN, license plates, etc.)
  * Any other unique identifying number, characteristic, or code of an individual that could identify an individual consumer, family, or device over time or across services



### Can I resell the Document AI API?

No, you are not permitted to resell Document AI service. You can still integrate Document AI into applications of independent value.

### How can customers control Google Cloud support access to their documents or data?

All Document AI parsers support Access Transparency and access approvals. By default, Google support wouldn't have access to any of customer data or applications. In the situation where access is required from the Google support team, customers can use the [Access Approval](https://docs.cloud.google.com/access-approval/docs/overview) process to authorize access to data or applications. This process starts with the creation of a ticket in the Google support portal. The customer then receive a notification (usually email) and an option to authorize or deny access.

Google also offers a service called [Access Transparency](https://docs.cloud.google.com/security/products/access-transparency), which gives customer visibility into all the tasks that Google support performs while they have access to the system.

[ Next Customer-managed encryption keys (CMEK)  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/cmek)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
