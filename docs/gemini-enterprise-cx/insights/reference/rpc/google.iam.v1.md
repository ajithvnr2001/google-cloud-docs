---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.iam.v1
title: Package google.iam.v1 \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:05:28.370166+00:00
---

# Package google.iam.v1  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.iam.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Package google.iam.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[IAMPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy)` (interface)



## IAMPolicy

API Overview

Manages Identity and Access Management (IAM) policies.

Any implementation of an API that offers access control features implements the google.iam.v1.IAMPolicy interface.

##### Data model

Access control is applied when a principal (user or service account), takes some action on a resource exposed by a service. Resources, identified by URI-like names, are the unit of access control specification. Service implementations can choose the granularity of access control and the supported permissions for their resources. For example one database service may allow access control to be specified only at the Table level, whereas another might allow access control to also be specified at the Column level.

##### Policy Structure

See google.iam.v1.Policy

This is intentionally not a CRUD style API because access control policies are created and deleted implicitly with the resources to which they are attached.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
