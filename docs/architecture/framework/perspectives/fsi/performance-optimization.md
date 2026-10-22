---
url: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/performance-optimization/
title: Financial services perspective: Performance optimization \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:44.781699+00:00
---

# Financial services perspective: Performance optimization  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/fsi/performance-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Financial services perspective: Performance optimization Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-28 UTC

This document in the [Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi) provides an overview of principles and recommendations to optimize the performance of your FS workloads in Google Cloud. The recommendations in this document align with the [performance optimization pillar](https://docs.cloud.google.com/architecture/framework/performance-optimization) of the Well-Architected Framework.

Performance optimization has a long history in financial services. It has helped FS organizations surpass technical challenges and it's nearly always been an enabler or accelerator for the creation of new business models. For example, ATMs ([introduced in 1967](https://en.wikipedia.org/wiki/ATM#Invention)) automated the cash dispensation process and they helped banks to decrease the cost of their core business. Techniques like bypassing the OS kernel and pinning application threads to compute cores helped to achieve deterministic and low latency for trading applications. The reduction in latency facilitated higher and firmer liquidity with tighter spreads in the financial markets.

The cloud creates new opportunities for performance optimization. It also challenges some of the historically accepted optimization patterns. Specifically, the following trade-offs are more transparent and controllable in the cloud:

  * Time to market versus cost.
  * End-to-end performance at the system level versus performance at the node level.
  * Talent availability versus agility of technology-related decision making.



For example, adapting hardware and IT resources to specific skill requirements is a trivial task in the cloud. To support GPU programming, you can create GPU-based VMs. You can scale capacity in the cloud to accommodate demand spikes without over-provisioning resources. This capability helps to ensure that your workloads can handle peak loads, such as on [nonfarm payroll](https://en.wikipedia.org/wiki/Nonfarm_payrolls) days and when [trading volumes are significantly greater than historical levels](https://cloud.google.com/blog/topics/financial-services/how-bidfx-developed-liquidity-provision-analytics-on-google-cloud?e=48754805). Instead of spending on writing highly optimized code at the level of individual servers (like highly fine-tuned code in the C language) or writing code for conventional high performance computing (HPC) environments, you can scale out optimally by using a well-architected Kubernetes-based distributed system.

The performance optimization recommendations in this document are mapped to the following core principles:

  * Align technology performance metrics with key business indicators
  * Prioritize security without sacrificing performance for unproven risks
  * Rethink your architecture to adapt to new opportunities and requirements
  * Future-proof your technology to meet present and future business needs



## Align technology performance metrics with key business indicators

You can map performance optimization to business-value outcomes in several ways. For example, in a [buy-side](https://corporatefinanceinstitute.com/resources/career/buy-side-vs-sell-side/) research desk, a business objective could be to optimize the output per research hour or to prioritize experiments from teams that have a proven track record, such as higher [Sharpe ratios](https://en.wikipedia.org/wiki/Sharpe_ratio). On the sell side, you can use analytics to track client interest and accordingly prioritize the throughput to AI models that support the most interesting research.

Connecting performance goals to business key performance indicators (KPIs) is also important for funding performance improvements. Business innovation and transformation initiatives (sometimes called _change-the-bank_ efforts) have different budgets and they have potentially different degrees of access to resources when compared to business-as-usual (BAU) or _run-the-bank_ operations. For example, Google Cloud helped the risk management and technology teams of a [G-SIFI](https://www.fsb.org/work-of-the-fsb/market-and-institutional-resilience/global-systemically-important-financial-institutions-g-sifis/) to collaborate with the front-office quantitative analysts on a solution to perform risk analytics calculations (such as [XVA](https://en.wikipedia.org/wiki/XVA)) in minutes instead of hours or days. This solution helped the organization to meet relevant compliance requirements. It also enabled the traders to have higher quality conversations with their clients, potentially offering tighter spreads, firmer liquidity, and more cost-effective hedging.

When you align your performance metrics with business indicators, consider the following recommendations:

  * Connect each technology initiative to the relevant business [objectives and key results (OKRs)](https://en.wikipedia.org/wiki/Objectives_and_key_results), such as increasing revenue or profit, reducing costs, and mitigating risk more efficiently or holistically.
  * Focus on optimizing performance at the system level. Look beyond the conventional change-the-bank versus run-the-bank separation and the front-office versus back-office silos.



## Prioritize security without sacrificing performance for unproven risks

Security and regulatory compliance in FS organizations must be unequivocally of a high standard. Maintaining a high standard is essential to avoid losing clients and to prevent irreparable damage to an organization's brand. Often, the highest value is derived through technology innovations such as [generative AI](https://cloud.google.com/ai/generative-ai) and unique, managed services like [Spanner](https://docs.cloud.google.com/spanner). Don't automatically discard such technology options due to a blanket misconception about prohibitive operational risk or inadequate regulatory compliance posture.

Google Cloud has worked closely with G-SIFIs to make sure that an AI-based approach for [Anti-Money Laundering (AML)](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview) can be used across the jurisdictions where the institutions serve customers. For example, [HSBC](https://services.google.com/fh/files/misc/hsbc_celent_model_risk_manager_of_the_year_2023.pdf) significantly enhanced the performance of its financial crime (Fincrime) unit with the following results:

  * Nearly two to four times more confirmed suspicious activity.
  * Lower operational costs due to elimination of over 60% of false positives and focused investigation time only on high-risk, actionable alerts.
  * Auditable and explainable outputs to support regulatory compliance.



Consider the following recommendations:

  * Confirm that the products that you intend to use can help meet the security, resilience, and compliance requirements for the jurisdictions where you operate. To achieve this objective, work with Google Cloud account teams, risk teams, and product teams.
  * Create more powerful models _and_ provide transparency to customers by leveraging AI explainability.
  * Achieve transparency for generative AI workloads by using techniques like [citations to sources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/beginners-guide#citation_check), [grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview), and [RAG](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview).

  * When explainability isn't enough, separate out the decision making steps in your value streams and use AI to automate only the non-decision making steps. In some cases, explainable AI might not be sufficient or a process might require human intervention due to regulatory concerns (for example, [GDPR, Article 22](https://gdpr-info.eu/art-22-gdpr/#:%7E:text=Protection%20Regulation%20\(GDPR\)-,Art.,significantly%20affects%20him%20or%20her.)). In such cases, present all the information that the human agent needs for decision making in a single control pane, but automate the data gathering, ingestion, manipulation, and summarization tasks.




## Rethink your architecture to adapt to new opportunities and requirements

Augmenting your current architectures with cloud-based capabilities can provide significant value. To achieve more transformative outcomes, you need to periodically rethink your architecture by using a cloud-first approach.

Consider the following recommendations to periodically rethink the architecture of your workloads to further optimize performance.

### Use cloud-based alternatives to on-premises HPC systems and schedulers

To take advantage of higher elasticity, improved security posture, and extensive monitoring and governance capabilities, you can run HPC workloads in the cloud or [burst](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern) on-premises workloads to the cloud. However, for certain numerical modeling use cases like simulation of investment strategies or XVA modeling, [combining Kubernetes with Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro) might offer a more powerful solution.

### Switch to graph-based programming for simulations

[Monte Carlo simulations](https://en.wikipedia.org/wiki/Monte_Carlo_method) might be much more performant in a graph-based execution system such as [Dataflow](https://cloud.google.com/products/dataflow). For example, [HSBC](https://cloud.google.com/customers/hsbc-risk-advisory-tool#:%7E:text=Spurred%20by%20an%20enthusiastic%20commitment,a%20wealth%20of%20future%20possibilities.) uses Dataflow to run risk calculations 16 times faster compared to their previous approach.

### Run cloud-based exchanges and trading platforms

Conversations with Google Cloud customers reveal that the [80/20 Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle) applies to the performance requirements of markets and trading applications.

  * More than 80% of trading applications don't need extremely low latency. However, they get significant benefits from the resilience, security, and elasticity capabilities of the cloud. For example, [BidFX](https://cloud.google.com/blog/topics/financial-services/how-bidfx-developed-liquidity-provision-analytics-on-google-cloud?e=48754805), a foreign exchange multi-dealer platform uses the cloud to launch new products quickly and to significantly increase their availability and footprint without increasing resources.
  * The remaining applications (less than 20%) need low latency (less than a millisecond), determinism, and fairness in the delivery of messages. Conventionally, these systems run in rigid and expensive colocated facilities. Increasingly, even this category of applications is being replatformed on the cloud, either at the [edge](https://cloud.google.com/blog/topics/hybrid-cloud/deutsche-bank-uses-google-distributed-cloud?e=48754805) or as [cloud-first applications](https://cloud.google.com/blog/topics/financial-services/lessons-from-deutsche-borse-groups-cloud-native-trading-engine?e=48754805).



## Future-proof your technology to meet present and future business needs

Historically, many FS organizations built proprietary technologies to gain a competitive edge. For example, in the early 2000s, successful investment banks and trading firms had their own implementations of foundational technologies such as pub-sub systems and message brokers. With the evolution of open source technologies and the cloud, such technologies have become commodities and don't offer incremental business value.

Consider the following recommendations to future-proof your technology.

### Adopt a data-as-a-service (DaaS) approach for faster time to market and cost transparency

FS organizations often evolve through a combination of organic growth and mergers and acquisitions (M&A). As a result, the organizations need to integrate disparate technologies. They also need to manage duplicate resources, such as data vendors, data licenses, and integration points. Google Cloud provides [opportunities](https://cloud.google.com/blog/topics/perspectives/google-cloud-can-help-with-post-merger-integration-strategy?e=48754805) to create differentiated value in post-merger integrations.

For example, you can use services like [BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction) to build an analysis-ready data-as-a-service (DaaS) platform. The platform can provide both market data and inputs from alternative sources. This approach eliminates the need to build redundant data pipelines and it lets you focus on more valuable initiatives. Further, the merged or acquired companies can quickly and efficiently rationalize their post-merger data licensing and infrastructure needs. Instead of spending effort on adapting and merging legacy data estates and operations, the combined business can focus on new business opportunities.

### Build an abstraction layer to isolate existing systems and address emerging business models

Increasingly, the competitive advantage for banks isn't the core banking system but their customer experience layer. However, legacy banking systems often use monolithic applications that were developed in languages like Cobol and are integrated across the entire banking value chain. This integration made it difficult to separate the layers of the value chain, so it was nearly impossible to upgrade and modernize such systems.

One solution to address this challenge is to use an isolation layer such as an [API management system](https://cloud.google.com/apigee) or a staging layer like Spanner that duplicates the book of record and facilitates the modernization of services with advanced analytics and AI. For example, [Deutsche Bank](https://cloud.google.com/blog/products/databases/deutsche-bank-scales-online-banking-platform-with-spanner?e=48754805) used Spanner to isolate their legacy core banking estate and start their innovation journey.

[ Previous arrow_back  Cost optimization  ](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/cost-optimization)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
