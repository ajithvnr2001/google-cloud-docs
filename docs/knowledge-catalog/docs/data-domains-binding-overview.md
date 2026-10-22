---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-binding-overview/
title: About resource binding and inclusion \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:38.476423+00:00
---

# About resource binding and inclusion  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-binding-overview/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  About resource binding and inclusion Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to include individual resources such as tables, datasets, data products, and entire projects in a data domain by creating resource bindings.

## About resource binding and inclusion

Understanding resource management in data domains involves two key concepts:

  * **Binding** : When you bind a resource to a domain, you create a link between the resource or a project and the data domain.
  * **Inclusion** : The membership that results from binding the resource to a domain. When a container resource, such as a project or dataset, is included in a domain, all of its descendants automatically inherit inclusion in that domain.



## Inheritance and overrides

Resource inclusion follows hierarchical inheritance rules:

  * **Automatic inheritance** : If you include a dataset or a project in a domain, this means that all assets under this dataset or project are also included in the domain, unless you explicitly override this setting.
  * **Explicit overrides** : Specific lower-level bindings take precedence over inherited parent assignments. If a child resource is explicitly bound to a different domain, that explicit binding overrides its inherited parent domain assignment.



**Example** : If a project containing two datasets (`dataset_1` and `dataset_2`) is bound to the **Finance** domain, both datasets inherit inclusion in **Finance**. However, if `dataset_2` is explicitly bound to the **Marketing** domain, `dataset_2` belongs to **Marketing** , while `dataset_1` remains in **Finance**.

![Diagram illustrating the difference between data domain resource binding and inclusion inheritance override](https://docs.cloud.google.com/static/knowledge-catalog/images/domain-binding-inclusion.svg)![Diagram illustrating the difference between data domain resource binding and inclusion inheritance override.](https://docs.cloud.google.com/static/knowledge-catalog/images/domain-binding-inclusion.svg)**Figure 1.** Data domain resource binding versus inherited inclusion (click to enlarge)

## What's next

  * Learn more about [data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview).
  * Learn how to [create data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-create).
  * Learn how to [include resources in data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
