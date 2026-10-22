---
url: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/exclusions/
title: Access Transparency exclusions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:54.024563+00:00
---

# Access Transparency exclusions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/exclusions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Transparency ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access Transparency exclusions

Access Transparency logs are generated when Google personnel access content that you've uploaded into an Access Transparency [supported service](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services), **except** in the following scenarios:

  1. Google is legally prohibited from notifying you of the access. For details, refer to Google Cloud's [Transparency Report](https://transparencyreport.google.com/user-data/enterprise?enterprise_legal_process_breakdown=product:1;authority:;series:requests,accounts,compliance&lu=enterprise_legal_process_breakdown).

  2. You've granted the Google personnel access to your content by using your Identity and Access Management (IAM) policy; their activities are recorded in [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) (when enabled), not Access Transparency logs.

  3. The access doesn't target [Customer Data](https://cloud.google.com/terms/service-terms); for example, Google personnel querying for the average size of records in a database that contains content from multiple Google Cloud customers.

  4. The content in question is a public resource identifier or a [resource name](https://google.aip.dev/122). For example:

     * Google Cloud project IDs
     * Cloud Storage bucket names
     * Compute Engine VM names
     * Google Kubernetes Engine cluster names
     * BigQuery resource names (including datasets, tables, and reservations)
  5. The access originates from Google's standard automated systems and code. These system accesses are validated by code authorization, which verifies that the job originates from code that was checked into production and subject to a multi-party security and privacy review, including a verified source code owner.




## What's next

  * Learn about the [services that Access Transparency supports](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
