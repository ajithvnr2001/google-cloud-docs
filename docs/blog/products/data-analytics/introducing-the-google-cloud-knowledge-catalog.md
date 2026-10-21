---
url: https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog/
title: Introducing the Google Cloud Knowledge Catalog | Google Cloud Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:44.627432+00:00
---

# Introducing the Google Cloud Knowledge Catalog | Google Cloud Blog

> Source: https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog/

Data Analytics

# 

Introducing the Google Cloud Knowledge Catalog

April 23, 2026

  * [](https://x.com/intent/tweet?text=Introducing%20the%20Google%20Cloud%20Knowledge%20Catalog%20@googlecloud&url=https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog&title=Introducing%20the%20Google%20Cloud%20Knowledge%20Catalog)
  * [](https://www.facebook.com/sharer/sharer.php?caption=Introducing%20the%20Google%20Cloud%20Knowledge%20Catalog&u=https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog)
  * [](mailto:?subject=Introducing%20the%20Google%20Cloud%20Knowledge%20Catalog&body=Check%20out%20this%20article%20on%20the%20Cloud%20Blog:%0A%0AIntroducing%20the%20Google%20Cloud%20Knowledge%20Catalog%0A%0AIntroducing%20the%20Knowledge%20Catalog:%20The%20evolution%20of%20Dataplex%20into%20a%20dynamic%20context%20engine%20for%20the%20enterprise.%20Unify%20metadata,%20enrich%20data%20with%20Gemini,%20and%20enable%20reliable%20AI%20agents%20with%20high-precision,%20secure%20retrieval.%0A%0Ahttps://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog)



![https://storage.googleapis.com/gweb-cloudblog-publish/images/GCN26_102_BlogHeader_2436x1200_Opt_12_Ligh.max-2500x2500.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/GCN26_102_BlogHeader_2436x1200_Opt_12_Ligh.max-2500x2500.jpg)

##### Chai Pydimukkala

Product Lead, Google Cloud

##### Sam McVeety

Tech Lead, Data Analytics

##### Try Gemini today

The front door to AI in the workplace

[Try now ](https://business.gemini.google/?utm_source=cloud.google.com/blog&utm_medium=et&utm_campaign=FY26-Q2-GLOBAL-GLO27877-physicalevent-er-next26-mc-105752)

Traditional data catalogs were built as manual inventories for technical users, focusing on table structures rather than the deep context that AI agents need. When agents lack business semantics and data relationships, this triggers hallucinations, high latency, and stale insights. 

To address this problem, we are evolving Dataplex into a dynamic, always-on [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog)**** that serves as the universal context engine for your enterprise, helping agents execute complex tasks with accuracy.

Customers like **Bloomberg Media** are already using the Knowledge Catalog to power agents with trusted context: 

“By unifying Bloomberg Media’s enterprise metadata and business context through the Knowledge Catalog, we successfully launched our Data Access AI Agent. This internal solution empowers stakeholders across the organization to intuitively explore our data lake, translating complex business inquiries into instant, AI-driven narratives. Crucially, by grounding our AI in trusted institutional context, we ensure confidence in the accuracy and quality of every insight generated."

— William Anderson, CTO, Bloomberg Media

The Knowledge Catalog operates on three foundational pillars:

  1. **Aggregation** : Unifying context and resolving conflicting definitions

  2. **Enrichment** : Generating continuous meaning and mapping relationships

  3. **Search** : Empowering agents with high-precision retrieval




### Aggregation: Unifying context across your data estate

To build true context, you must bring it together from everywhere. The Knowledge Catalog aggregates native context across your Google and partner data platforms, semantic models, and third-party catalogs, unifying them into a single, governed source of truth. 

  * **Broad metadata aggregation**(GA):**** To build a truly comprehensive context engine, you must leave no silo behind. The Knowledge Catalog automatically harvests technical metadata across your foundational systems — including BigQuery, AlloyDB, Spanner, Cloud SQL, Firestore (Preview), and Looker (Preview). It also supports integrations with third-party databases and partner catalogs like **Atlan, Collibra, Datahub, Ab Initio, and Anomalo,** ensuring that even your legacy metadata is brought into the agentic fold.

  * **Enterprise connectivity**(Preview): To truly understand your operations, semantic context must cover all the key systems in your enterprise. Using Google Cloud Lakehouse, we are interconnecting these systems with context federation, and Knowledge Catalog gains full and immediate visibility to applications, operating systems, and AI platforms — including **Palantir, Salesforce Data360, SAP, ServiceNow, and Workday**. For example, your SAP data products are automatically mapped to the Knowledge Catalog. 

  * **BigQuery measures**(Preview):**** We are redefining data consistency by embedding programmatic business logic directly into the SQL engine. BigQuery measures ensure every calculation is universally reusable and mathematically accurate. The Knowledge Catalog acts as the ultimate aggregator, pulling BigQuery measures and LookML together into a single, governed semantic foundation.

  * **Data products** (GA): Data products package data assets and context that grounds agents and makes them reliable in production. These self-contained blocks include built-in intent, SLAs, and governance constraints, providing the essential building blocks to scale complex AI use cases.




### Enrichment: Generating meaning through continuous learning 

The Knowledge Catalog provides continuous data enrichment — going beyond manual curation to actively mine structured schemas, query logs, and BI semantic models while extracting entity relationships from unstructured data. We are delivering this continuous enrichment where your teams work: 

  * **Smart Storage and Object Context API**(Preview):**** Built natively into Google Cloud Storage (GCS), Smart Storage automatically tags, embeds, and enriches files with metadata as soon as they land in your buckets. By integrating this intelligence feature with the Knowledge Catalog, unstructured data is instantly discoverable by agents. 

  * **Deep multimodal metadata extraction**(Preview):**** For collections of complex unstructured data, the Knowledge Catalog natively integrates with Gemini to identify useful business information and automatically build pipelines that extract entities and map complex business relationships directly from unstructured content.

  * **Automated context curation** (Preview):**** The Knowledge Catalog automatically generates natural language descriptions, including business glossaries, for datasets, data products, relationships, and verified SQL patterns that allow both humans and agents to interact with data without guesswork. By inferring these hidden relationships and intent-based patterns, it constructs a dynamic, evolving map of how data actually relates to the business.

  * **Verified queries and semantic guardrails** (Preview): One leading cause of AI failure is hallucinated logic and guessed SQL joins. To prevent this, the catalog provides verified SQL patterns and pre-generated natural language questions.




### Search: Unleashing agents with high-precision, secure retrieval

Creating a massive context layer is great, but in the agentic era, search has evolved to be the new query path. When autonomous agents are working on your behalf, they are iterating incredibly fast. The hardest problems at enterprise scale are speed, relevance, global reach, and security.

  * **High-precision semantic search**(GA): The Knowledge Catalog uses a hybrid search stack leveraging decades of Google innovation. Built on the same advanced query-rewriting and machine-learning technologies that power Google Search, it delivers the sub-second latency and pinpoint relevance that agents need. When an agent receives a prompt, the catalog instantly ranks and returns the right context to agents in real-time.

  * **Access control-aware search:** The ability to find the right data and its corresponding context is critical in the agentic era; if an agent retrieves the wrong context, it hallucinates. To gain trust, our global search respects metadata access permissions as defined in the source systems, ensuring agents can only retrieve and act on the assets they are explicitly authorized to see.

  * **Measurable context evaluation:** To ensure long-term accuracy, we are augmenting our search capabilities with a robust evaluation framework. This transforms context construction from a guessing game into a measurable engineering discipline. It allows your teams to quantitatively test and iterate on various context construction strategies, ensuring continuous optimization of the relevance and quality of the context feeding your agents.




With foundational data products, high-precision search, and guardrails in place, we can deploy advanced AI reliably. A prime example is the **Deep Research Agent in Gemini Enterprise, powered by the Knowledge Catalog**(Preview). Now natively powered by the Knowledge Catalog, this agent synthesizes live business data, internal documents, and web research to answer highly complex questions. It delivers deterministic precision and deep citations, executing tasks in minutes that previously required weeks of manual effort.

Stop forcing your agents to guess the unwritten rules of your business. Build the context once, and unleash your agents to do the rest.

Get started today with [Knowledge Catalog](https://cloud.google.com/dataplex).

Posted in

  * [Data Analytics](https://cloud.google.com/blog/products/data-analytics)
  * [BigQuery](https://cloud.google.com/blog/products/bigquery)
  * [Google Cloud Next](https://cloud.google.com/blog/topics/google-cloud-next)



##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/09_-_Data_Analytics_tFH57V6.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/09_-_Data_Analytics_tFH57V6.max-700x700.jpg)Data AnalyticsCross-cloud conversational analytics made simple with open standardsBy Praveen Kumar • 8-minute read](https://cloud.google.com/blog/products/data-analytics/cross-cloud-conversational-analytics-with-borderless-lakehouse)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/50_-_Business_Intelligence_lw8zsjF.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/50_-_Business_Intelligence_lw8zsjF.max-700x700.jpg)Business IntelligenceTrusted Data Apps for the Agentic Data Cloud, powered by LookerBy Ani Jain • 4-minute read](https://cloud.google.com/blog/products/business-intelligence/introducing-looker-data-apps)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/09_-_Data_Analytics_tFH57V6.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/09_-_Data_Analytics_tFH57V6.max-700x700.jpg)Data AnalyticsIntroducing TimesFM 3.0 with multivariate time-series forecasting in BigQueryBy Haiyang Qi • 11-minute read](https://cloud.google.com/blog/products/data-analytics/bigquery-timesfm-3-0-with-multivariate-time-series-forecasting)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/0_banner_image.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/0_banner_image.max-700x700.png)Data AnalyticsAgentic data science with the Data Agent KitBy Jeff Nelson • 5-minute read](https://cloud.google.com/blog/products/data-analytics/bringing-you-the-data-agent-kit)
