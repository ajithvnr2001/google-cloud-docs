---
url: https://docs.cloud.google.com/architecture/partners/model-development-data-labeling-labelbox-google-cloud/
title: Model development and data labeling with Google Cloud and Labelbox \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:47.361335+00:00
---

# Model development and data labeling with Google Cloud and Labelbox  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/model-development-data-labeling-labelbox-google-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Model development and data labeling with Google Cloud and Labelbox Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-03-21 UTC

By: David Mok, Robert Wood - [Labelbox](https://labelbox.com/) | Akash Gupta - Google

This document provides a reference architecture for building a standardized pipeline with Google Cloud and [Labelbox](https://labelbox.com/). This architecture can help you to develop your ML models more quickly, particularly models for computer vision, NLP and generative AI use cases. This document is intended for machine learning (ML) engineers and data scientists who want to incorporate automation and a human-in-the-loop (HITL) approach to data labeling and data curation.

## Architecture

The following diagram shows the architecture for the standardized pipeline with Google Cloud and Labelbox that you create:

![A standardized pipeline with Labelbox and Google Cloud.](https://docs.cloud.google.com/static/architecture/images/model-development-data-labeling-labelbox-google-cloud.png)

The architecture has the following arrangement:

  * Unstructured data is stored in [Cloud Storage](https://docs.cloud.google.com/storage). That data, along with any associated metadata, is stored in a [BigQuery](https://docs.cloud.google.com/bigquery) table.
  * You connect Labelbox to Google Cloud using [identity and access management (IAM) delegated access](https://docs.labelbox.com/docs/using-google-cloud-storage) for Google Cloud Storage and the [Labelbox BigQuery Connector](https://docs.labelbox.com/reference/bigquery-connector). You can then use [Labelbox Catalog](https://labelbox.com/product/catalog/) as a visual, no-code tool for exploring, organizing, and structuring training datasets.
  * Using data that Labelbox has structured and prepared, your organization can train models in [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform). [Labelbox Model ](https://labelbox.com/product/model/) can also be used to diagnose performance by taking a data-focused approach.
  * After model errors and data quality issues have been identified, your organization can use Labelbox Catalog to find and target similar, unlabeled or incorrectly labeled data to build and refine the next iteration of their model's dataset.



The preceding diagram includes the following Labelbox components:

  * **Catalog** : An unstructured data search platform which provides large scale data discovery and organization. Catalog is integrated with Cloud Storage and BigQuery. This integration lets analysts more effectively search and organize BigQuery tables when using unstructured data.
  * **Annotate** : This component provides model assisted labeling combined with enterprise review and workforce management workflows to create the ground truth for model training. Labelbox can use the models that are available through Agent Platform for assisted labeling.
  * **Model** : A model diagnostics platform that lets you search and filter each version of your dataset based on metrics or metadata to identify problem cases. This component also lets you observe and evaluate Agent Platform models and create an active learning loop.
  * **Boost** : This component provides managed access to various types of specialized labeling solutions, including specialized engagements and human labeling services.



## Products used

This reference architecture uses the following Google Cloud and third-party products:

  * Labelbox: An end-to-end AI platform that you can use to create and manage high-quality training data.
  * Cloud Storage: An enterprise-ready service that provides low-cost, limitless object storage for diverse data types. Data is accessible from both inside and outside of Google Cloud and is replicated across multiple geographic locations.
  * BigQuery: A fully managed, highly scalable data warehouse with built-in ML capabilities.
  * Agent Platform: A service for managing the AI and ML development lifecycle.



## Use cases

This section describes some example use cases for which a standardized pipeline with Google Cloud and Labelbox is an appropriate choice.

Online retail companies use Labelbox to build personalization and recommendation models for their ecommerce product listings, for example, [Etsy](https://labelbox.com/customers/ecommerce-shopping-customer-story/). Each listing is represented by its hero image and associated categorical and customer interaction metadata. Business users can search through listings using structured (metadata search) and unstructured (vector search) methods.

Content media and entertainment companies are also building personalization and recommendation models, using high-volumes of video and image content. These companies can effectively develop content personalization and recommendation algorithms by quickly organizing and structuring their content to train models. By using the Labelbox search interface, content specialists can build ML datasets without spending weeks or months sifting through content.

Customers and organizations can achieve the following by using Labelbox with BigQuery and Agent Platform:

  * Effectively structure their data through Labelbox Model Assisted Labeling and Enterprise Workflows to prepare datasets for training models on Agent Platform.
  * After organizations have a trained Agent Platform model in place, Labelbox efficiently improves performance through data-centric error analysis. This analysis helps teams to pinpoint problematic edge cases, focus on issues, and label data more effectively to build the next version of their training dataset.



## Design considerations

This section provides guidance to help you use this reference architecture to develop an architecture that meets your specific requirements for security, reliability, operational efficiency, cost, and performance. For more best practices, see the [Labelbox documentation](https://docs.labelbox.com/docs/optimize-editor-performance).

### Security, privacy, and compliance

This section describes factors that you should consider when you use this reference architecture to design and build a standardized pipeline with Google Cloud and Labelbox.

Labelbox integrates with Cloud Storage through delegated access and ephemeral signed URLs. Data is encrypted in flight and can be sealed off behind a firewall using asset proxy servers and SSO. BigQuery and Agent Platform integration is secured through Identity and Access Management-authenticated client and service accounts.

For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

### Cost optimization

The pipeline that this architecture describes can help you to optimize costs in the following ways:

  * Helping you to reduce overall labeling costs and annual budgets dedicated to data labeling by providing transparency and workflows that optimize for labeling performance.
  * Saving time by improving collaboration between data scientists, AI product owners, and teams responsible for data labeling operations which in turn reduces the manual back and forth nature of managing data labeling at each model iteration.
  * Helping ensure model training costs are reduced by delivering better data quality and tools for quality assurance. Less manual human-labeled data is required for building performant models because this architecture lets you use tools for curating high-impact data. It also provides automation, which helps teams effectively iterate on the quality of labeled data.
  * Teams can focus on building AI-powered products and delivering models, instead of building data labeling infrastructure.



For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

### Operational efficiency

Labelbox enables organizations and teams to search through, curate, and label unstructured data, without the need for input from data scientists and machine learning engineers. Typically, organizations would spend years and millions of dollars building and managing these products and the pipelines to connect them together.

For operational excellence principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence) in the Well-Architected Framework. 

## Deployment

Labelbox operates as a managed, hosted service on Google Cloud. Its unstructured data and models use a customer managed infrastructure on Google Cloud. You can purchase Labelbox from the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/labelbox-tackle-public/labelbox-product-gcp).

This reference architecture uses GitHub repositories that let you do the following:

  * [Connect Labelbox and Google BigQuery](https://github.com/Labelbox/labelbox-bigquery#labelbox-connector-for-google-bigquery)
  * [Connect Labelbox and BigQuery](https://github.com/Labelbox/vertex-model-training)



## What's next

For more information about Labelbox, see the following:

  * [Learn about Labelbox](https://labelbox.com)
  * See the [Labelbox offering on Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/labelbox-tackle-public/labelbox-product-gcp)
  * Review the [Labelbox and BigQuery Connector details](https://docs.labelbox.com/reference/bigquery-connector)
  * See [Labelbox and Google Cloud retail use cases](https://labelbox.com/blog/how-to-accelerate-time-to-value-when-building-ai-for-retail-and-e-commerce/)
  * Learn more about the following Google Cloud products: 
    * [Google Cloud Storage](https://cloud.google.com/storage/pricing)
    * [BigQuery](https://cloud.google.com/bigquery/pricing)
    * [Agent Platform ](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing)
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Robert Wood](https://www.linkedin.com/in/robert-wood-b221189a) | Solutions Architect (Labelbox)
  * [David Mok](https://www.linkedin.com/in/davidmok21) | Director Content and Partnerships (Labelbox)
  * [Akash Gupta](https://www.linkedin.com/in/akashgupta1689) | ISV Partner Engineer



Other contributors: 

  * [Bala Desikan](https://www.linkedin.com/in/bala-desikan) | Principal Architect
  * [Samson Leung](https://www.linkedin.com/in/samleung314) | AI Engineer
  * [Valentín Huerta](https://www.linkedin.com/in/valentinhuerta/) | AI Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-03-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-03-21 UTC."],[],[]] 
