---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/security-and-compliance-features/
title: Security and compliance features \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:14:42.486889+00:00
---

# Security and compliance features  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/security-and-compliance-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Security and compliance features Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the security and compliance features supported by AML AI.

**Identity and Access Management (IAM)** \- IAM lets you grant granular access to specific AML AI and Google Cloud resources. IAM also helps prevent access to other resources.

See [Access control in AML AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/access-control) or the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

**Encryption at Rest** \- Customer Managed Encryption Keys (CMEK) give you control over the keys that protect and encrypt your data at rest in Google Cloud. AML AI lets you manage your keys through Cloud KMS which supports a range of options for storing encryption keys. These include:

  * Software security keys
  * Hardware backed security keys using [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm)



Read more about [encryption at rest in AML AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/cmek).

**Encryption in Transit** \- Data in transit within Google Cloud and between the AML AI endpoint and your network is always encrypted. Read more about [encryption in transit in AML AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/understand-encryption-in-transit) or [encryption in transit in Google cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit).

**VPC Service Controls** \- VPC Service Controls allow a similar level of protection to private endpoints. It adds a layer of protection on top of IAM, preventing access to Google services, including AML AI, from unauthorized networks and services outside of a perimeter. Read more about [VPC Service Controls in AML AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/vpc-service-controls) and the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs).

**Monitoring and logging** \- [Platform logs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/logging) and, optionally, [audit logs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/audit-logging), help you to answer the questions, "Who did what, where, and when?" within your AML AI and Google Cloud resources in real time. Platform logs are always collected, but you must enable audit logs to collect them. _Model monitoring_ is a separate topic for which [AML AI provides artifacts](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/collect-model-risk-governance-artifacts) to support your processes.

**Data Residency** \- Data residency ensures that your data is stored only in the regions you specify when an AML AI instance is created. AML AI is implemented with strict data residency policies. See [data residency in AML AI](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/data-residency).

**Access Transparency Logs (AxT)** \- Access transparency logs record the actions taken by Google personnel on your AML AI resources. Read more in the [AxT overview](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview), or why Google support personnel might need to access your data at [privileged access at Google Cloud](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/privileged-access).

**Data Deletion** \- Read more about [how Google Cloud deletes data](https://docs.cloud.google.com/docs/security/deletion) and the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum).

**SLAs** \- AML AI offers [documented SLAs](https://cloud.google.com/anti-money-laundering-ai/sla) for the availability of the AML AI service.

**Disaster Recovery** \- Input and output data from AML AI resides in BigQuery which provides a number of [options for disaster recovery](https://docs.cloud.google.com/bigquery/docs/reliability-intro#disaster_planning). While internal artifacts such as model weights can't be exported outside of AML AI, you can [copy models to an instance in another region or project](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/copy-model-instances) for recovery. See the [disaster recovery for AML AI](https://docs.cloud.google.com/architecture/disaster-recovery#anti_money_laundering_ai) page.

**Geographic Resilience** \- AML AI is deployed regionally, providing resilience against zonal outages but not regional outages. To build a multi-region disaster recovery plan, you can configure resilience across two layers:

  * **Data layer:** Set up [BigQuery cross-region dataset replication](https://docs.cloud.google.com/bigquery/docs/data-replication) to synchronize your input data and prediction results to a secondary region.
  * **Model layer:** Copy trained models to an AML AI instance in the secondary region ahead of time to support failover. For more information, see [Copy models to new instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/copy-model-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
