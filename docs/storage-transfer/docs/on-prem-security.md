---
url: https://docs.cloud.google.com/storage-transfer/docs/on-prem-security/
title: Protect file system data \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:51.892638+00:00
---

# Protect file system data  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/on-prem-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Protect file system data Stay organized with collections  Save and categorize content based on your preferences. 

You have several options for protecting the data and resources that you transfer.

## Protecting your file system resources

Agents access files from the environment they are running in. This means that you have several ways that you can protect access to your data:

  * Using a restricted user or role account to run the agent container.

  * Limiting the file systems that are mounted to the agent container.

  * Choose NFS mount permissions in accordance with your security policies, such as no write access.

  * [Restricting agent directory access](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#restrict-directory-access).


**Important:** Users able to create transfer jobs can retrieve data from, and download data to, any file system directory that is accessible by the agent. If agents are run as root and are given access to the entire file system, a malicious actor may be able to take over the host. It is strongly recommended that you [restrict agent access](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#restrict-directory-access) to only necessary directories.

## Protecting data in-flight

Storage Transfer Service encrypts your data over an HTTPS session with TLS for both connections through the public internet, and through private connections (such as Cloud Interconnect). If you are using Cloud Interconnect, you can obtain an additional layer of security by [using private API endpoints](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#direct-interconnect).

**Note:** Storage Transfer Service does not encrypt data on your behalf, such as in customer-managed encryption keys (CMEK). We only encrypt data in transit.

## Protecting Google Cloud resources

Agents use `gcloud auth` to connect to Storage Transfer Service and Cloud Storage resources used during the transfer. Therefore your Google Cloud resources are protected using Identity and Access Management and the account that you choose to provision for transfer agent use. You may also use a [service account](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#service-credentials), which can help make permissions management easier to use.

## IAM

Storage Transfer Service supports the following Storage Transfer Service [predefined IAM roles](https://docs.cloud.google.com/storage-transfer/docs/access-control#predefined-roles):

  * **Storage Transfer Admin** — Provides all Storage Transfer Service permissions.

  * **Storage Transfer User** — Can submit and monitor jobs, but can't delete jobs or see admin settings such as agent details or bandwidth settings.




Storage Transfer Service doesn't support custom IAM roles or the **Storage Transfer Viewer** predefined role. Users in either scenario may not see a polished user interface. If they attempt to load pages they don't have permissions for, the page will display an error or a blank page. However, the permitted actions remain restricted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
