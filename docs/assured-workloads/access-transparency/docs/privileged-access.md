---
url: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/privileged-access/
title: Privileged access at Google Cloud \u00a0|\u00a0 Access Transparency \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:55.500119+00:00
---

# Privileged access at Google Cloud  |  Access Transparency  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/privileged-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Transparency ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Privileged access at Google Cloud

Google Cloud systems are built with a focus on protecting your content using controls and monitoring. Your content stored on Google Cloud completely belongs to you. Occasionally, Google personnel might need to access your content but these accesses are never without a valid business justification.

## Why Google personnel request access to Customer Data

The most common reason why Google personnel request access to [Customer Data](https://cloud.google.com/terms/service-terms) is to resolve a customer support ticket. If you create a customer support request, then a Google personnel might be required to request access to your data. Access Transparency exists to provide customers visibility into these accesses. Google provides various controls to support the privacy of your data, regardless of whether Access Transparency is enabled on an organization. For more information about these controls, see [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design). 

## What is privileged access

Google personnel's access to your data to fulfill an obligation of providing a contracted service is called _privileged access_. Access to your data in Google Cloud is usually because of the following reasons:

  * You are accessing your own data.
  * A service you are using is accessing data on your behalf.



When requested to provide a contracted service, Google personnel acting as a privileged administrator can access your data.

## Foundational principles of privileged access management

Google Cloud's privileged access management strategy strictly limits what a single Google staff member can view and do with your data. Google Cloud's privileged access philosophy is based on the following principles:

  * **Least privilege** : Access to Customer Data is denied by default for all Google personnel. When access is granted, it is temporary and no greater than what is absolutely necessary to provide the contracted service.

  * **Limit singular access to data** : Singularly accessing Customer Data without another individual involved is extremely difficult for any and every Google personnel.

  * **All access must be justified** : By default, Google personnel don't have access to Customer Data. Google personnel can access your data only with an **active** , valid business justification. Google personnel can't access Customer Data for justifications that are closed or where the Google person is not a directly linked collaborator. For the list of valid business justifications, see [Justification reason codes](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#justification-reason-codes).

  * **Monitor and alerting** : Monitoring and response processes exist to identify, triage, and remediate violations of these principles.


For more information about Google Cloud's privileged access philosophy, see [Privileged access in Google Cloud](https://docs.cloud.google.com/docs/security/privileged-access-management). 

Google Cloud products regularly undergo independent, third-party audits and certifications to verify that their data protection practices match their controls and commitments. For more information about how Google Cloud products provide customers with transparency and control over their content, see the whitepaper on [Trusting your data with Google Cloud](https://services.google.com/fh/files/misc/072022_google_cloud_trust_whitepaper.pdf). 

## What's next

  * To know more about Google Cloud's commitment toward protecting the privacy of Customer Data, see [Google Cloud and common privacy principles](https://docs.cloud.google.com/privacy/common-privacy-principles).

  * To learn about the core principles upon which controls that prevent unauthorized administrative access are based, see [Overview of administrative access controls](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs/administrative-access).



  * To see the list of business justifications for which Google personnel can request to access customer data, see [Justification reason codes](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#justification-reason-codes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
