---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/fetch-service-account-for-customer/
title: FetchServiceAccountForCustomer parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:20.562248+00:00
---

# FetchServiceAccountForCustomer parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/fetch-service-account-for-customer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FetchServiceAccountForCustomer parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Feed Management API (**`FetchFeedServiceAccount`**) to the modern Chronicle API (**`FetchServiceAccountForCustomer`**).

## Protocol and mapping overview

Feature | Legacy API (`FetchFeedServiceAccount`) | Modern Chronicle API (`FetchServiceAccountForCustomer`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/feedServiceAccounts.fetch`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `FetchServiceAccountForCustomerRequest` requires parent scoping instead of relying on implicit auth tokens.

Legacy field (`FetchFeedServiceAccountRequest`) | Modern field (`FetchServiceAccountForCustomerRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— _(empty request)_ | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** The legacy request took an empty body (`{}`) and derived customer bounds implicitly from auth token context. The modern API specifies parent resource paths explicitly: `projects/{project}/locations/{region}/instances/{instance}`.  
  
* * *

## Response payload field-by-field parity

The modern Chronicle API (`FetchServiceAccountForCustomer`) response wraps the service account in a standard Google Cloud resource format.

Legacy field (`FetchFeedServiceAccountResponse` message) | Modern field (`FeedServiceAccount` message) | Field type | Parity and migration notes  
---|---|---|---  
`service_account` | `name` | `string` | **Parity mapped / restructured:** Legacy returned the raw service account string. The modern API maps this into the standard canonical resource path under name: `projects/{project}/locations/{location}/instances/{instance}/feedServiceAccounts/{service_account_email}`.  
`subject_id` | `subject_id` | `string` | **Parity mapped:** Unique subject identifier for the service account. Rename to `subjectId` in JSON responses.  
  
* * *

## Key differences between the Backstory and Chronicle APIs

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings rather than relying on implicit auth tokens.
  * **Resource path formatting:**
    * Raw service account strings are encapsulated inside standard Google Cloud canonical resource names (`projects/.../feedServiceAccounts/<sa>`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
