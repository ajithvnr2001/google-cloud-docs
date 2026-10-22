---
url: https://docs.cloud.google.com/architecture/rag-genai-gemini-enterprise-vertexai/
title: RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:02.560797+00:00
---

# RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/rag-genai-gemini-enterprise-vertexai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-11-10 UTC

This document provides a reference architecture that you can use to design the infrastructure for a generative AI application with [retrieval-augmented generation (RAG)](https://developers.google.com/machine-learning/glossary#retrieval-augmented_generation) by using [Gemini Enterprise](https://cloud.google.com/gemini-enterprise) and [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform). This reference architecture demonstrates how to use managed services and deploy a single [AI agent](https://docs.cloud.google.com/docs/generative-ai/glossary#ai-agents) to facilitate an end-to-end RAG dataflow. Gemini Enterprise serves as the unified platform for agent orchestration across the enterprise. Agent Platform accelerates the development and deployment of custom agents and provides managed datastores to facilitate efficient retrieval for RAG.

The intended audience for this document includes architects, developers, and administrators of generative AI applications. The document assumes that you have a basic understanding of AI, machine learning (ML), and large language model (LLM) concepts. This document doesn't provide guidance about how to design and develop a generative AI application. For information about how to design an application, see [Develop a generative AI application](https://docs.cloud.google.com/docs/ai-ml/generative-ai/develop-generative-ai-application).

**Note:** To meet your requirements, you can consider other architectural approaches for your RAG-capable generative AI application. For more information, see the design alternatives section later in this document.

## Architecture

The following diagram shows a high-level view of the architecture that this document presents:

![A high-level view of the data ingestion and serving flows in the architecture.](https://docs.cloud.google.com/static/architecture/images/rag-capable-gen-ai-app-gemini-enterprise-vertexai-high-level.svg)![](https://docs.cloud.google.com/static/architecture/images/rag-capable-gen-ai-app-gemini-enterprise-vertexai-high-level.svg)

The architecture in the preceding diagram has two subsystems: data ingestion and serving.

  * The **data ingestion subsystem** ingests and prepares data from external sources for use in RAG. The subsystem generates [embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/glossary#embedding) for the ingested data and uses them to build and maintain a searchable [vector index](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/glossary#index) in a managed datastore.
  * The **serving subsystem** contains the generative AI application's frontend and backend services. 
    * The frontend service handles the query-response flow with application users and forwards queries to the backend service.
    * The backend service uses Gemini Enterprise and Agent Platform to build and deploy your AI agent to orchestrate the RAG process. This process uses the indexed vector data to generate responses that are contextually grounded and adhere to [Responsible AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai) safety filters.



The following diagram shows a detailed view of the architecture:

![A detailed view of the data ingestion and serving flows in the architecture.](https://docs.cloud.google.com/static/architecture/images/rag-capable-gen-ai-app-gemini-enterprise-vertexai-detail.png)![](https://docs.cloud.google.com/static/architecture/images/rag-capable-gen-ai-app-gemini-enterprise-vertexai-detail.png)

The following sections describe the data flow within each subsystem of the preceding architecture diagram.

### Data ingestion subsystem

The data ingestion subsystem ingests data from external sources and prepares the data for RAG. The following are the steps in the data-ingestion and preparation flow:

  1. Data engineers upload data from external sources to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets). The external sources might be applications, databases, or streaming services.
  2. Upon completion, Cloud Storage publishes a message to a Pub/Sub topic.
  3. The Pub/Sub topic triggers a processing job to run in [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview).
  4. Cloud Run functions processes the raw data by generating and storing the metadata as [JSON Lines (JSONL)](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#storage-unstructured) files. The JSONL files are stored into a separate Cloud Storage bucket.
  5. Upon completion, Cloud Run functions publishes a message to a Pub/Sub topic.
  6. The Pub/Sub topic triggers a processing job to run in the [managed datastore](https://docs.cloud.google.com/gemini/enterprise/docs/introduction-to-connectors-and-data-stores) within Gemini Enterprise. The processing job pulls the raw ingested data and metadata from the Cloud Storage buckets, then [parses and chunks the data](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#parse-chunk-rag) for efficient retrieval during serving. Gemini Enterprise automatically generates vector embeddings without any configuration necessary.



### Serving subsystem

The serving subsystem handles the query-response flow between the generative AI application and its users. The following are the steps in the serving flow:

  1. An application user sends a query through one of the [Cloud Run frontend services](https://docs.cloud.google.com/run/docs/resource-model#services). You can customize these services for different experiences, such as a chatbot UI, a search page, or a mobile application.
  2. The frontend service receives the query, and then forwards the query to a centralized Cloud Run backend service. This backend provides a single, unified endpoint to support all of the different frontend clients. The backend service also performs necessary preprocessing, which can include constructing filters for the search query. This approach keeps the logic transparent to the frontends.
  3. The backend service sends the prepared request to Gemini Enterprise by using the Gemini Enterprise API endpoint to initiate the RAG workflow.
  4. To process the query, Gemini Enterprise uses the enterprise search and custom agent to perform the following tasks: 
     1. Create an embedding of the user's query.
     2. Perform a semantic search on the indexed data in the Managed datastore to find the most relevant information.
     3. Augment the original query with the retrieved data from the managed datastore to create a detailed, contextual prompt.
     4. Generate a final response that's based on the augmented prompt.
  5. Gemini Enterprise sends the generated response to the Cloud Run backend service.
  6. The backend service returns the final response to the frontend service that sent the original request. The frontend service presents the answer to the application user.



## Products used

This reference architecture uses the following Google Cloud products:

  * [ Gemini Enterprise](https://cloud.google.com/gemini-enterprise): A fully-managed secure platform to deploy and manage AI agents within an enterprise. 
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
    * [ Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime): A platform that lets you run, manage, and scale AI agents in production. 
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Pub/Sub](https://cloud.google.com/pubsub): An asynchronous and scalable messaging service that decouples services that produce messages from services that process those messages.
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.



## Use cases

This architecture is designed for enterprise scenarios where your generative AI application needs access to the most current information and requires deep, contextual understanding to provide accurate responses.

The architecture includes a custom data ingestion subsystem to address two key enterprise requirements:

  * **Real-time data availability:** The event-driven pipeline processes new data as soon as it's available in your organization—for example, a new product guide or an updated report. The pipeline also makes the information available in your managed datastore. This design helps to mitigate information staleness because it ensures that there's a minimal delay between data availability and use.
  * **Enriched contextual search:** The custom processing job allows your organization to apply its own business logic to enrich data with valuable metadata. The Cloud Run function can tag each document with specific attributes like product line, author, location, or document type. This rich metadata helps the agent to narrow down its search and deliver more precise, context-aware answers.



RAG is an effective technique to improve the quality of output that's generated from an LLM. This section provides examples of use cases for which you can use RAG-capable generative AI applications.

### Personalized product recommendations

An online shopping site might use an LLM-powered chatbot to assist customers with finding products or getting shopping-related help. The questions from a user can be augmented by using historical data about the user's buying behavior and website interaction patterns. The data might include user reviews and feedback that's stored in an unstructured datastore or search-related metrics that are stored in a web analytics data warehouse. The augmented question can then be processed by the LLM to generate personalized responses that the user might find more appealing and compelling.

### Clinical assistance systems

Doctors in hospitals need to quickly analyze and diagnose a patient's health condition to make decisions about appropriate care and medication. A generative AI application that uses a medical LLM like [Med-PaLM](https://sites.research.google/med-palm/) can be used to assist doctors in their clinical diagnosis process. The responses that the application generates can be grounded in historical patient records by contextualizing the doctors' prompts with data from the hospital's electronic health record (EHR) database or from an external knowledge base like [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

### Efficient legal research

Generative AI-powered legal research lets lawyers quickly query large volumes of statutes and case laws to identify relevant legal precedents or summarize complex legal concepts. The output of such research can be enhanced by augmenting a lawyer's prompts with data that's retrieved from the law firm's proprietary corpus of contracts, past legal communication, and internal case records. This design approach ensures that the generated responses are relevant to the legal domain that the lawyer specializes in.

## Design alternatives

This section presents alternative design approaches that you can consider for your RAG-capable generative AI application in Google Cloud.

### AI infrastructure alternatives

For a list of architecture guides to design and deploy generative AI applications with RAG in Google Cloud, see [Generative AI with RAG](https://docs.cloud.google.com/architecture/rag-reference-architectures).

### Application hosting options

In the architecture that's shown in this document, Cloud Run is the host for the generative AI application and data processing. Cloud Run is an application that is developer-focused and fully managed. You can also deploy your application to [Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale), [GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs), or to [Compute Engine](https://docs.cloud.google.com/compute) VMs.

To choose an application host, consider the following trade-offs between configuration flexibility and management effort:

  * With the serverless Cloud Run option, you deploy your custom services to a preconfigured, managed environment. To host the frontend services and the custom backend logic for request pre-processing, this architecture requires the ability to deploy custom applications.
  * With the Agent Runtime option, you use a fully managed platform that's designed for agent serving. Agent Runtime reduces management overhead and ensures tight integration with Gemini Enterprise.
  * With Compute Engine VMs and GKE containers, you're responsible for managing the underlying compute resources, but you have greater configuration flexibility and control.



For more information about choosing an appropriate application hosting service, see the following documents:

  * [Is my app a good fit for Cloud Run?](https://docs.cloud.google.com/run/docs/fit-for-run)
  * [Select a managed container runtime environment](https://docs.cloud.google.com/architecture/select-managed-container-runtime-environment)
  * [Hosting Applications on Google Cloud](https://cloud.google.com/hosting-options)



### Other infrastructure options

For information about other infrastructure options, supported models, and grounding techniques that you can use for generative AI applications in Google Cloud, see [Choose models and infrastructure for your generative AI application](https://docs.cloud.google.com/docs/generative-ai/choose-models-infra-for-ai).

## Design considerations

This section provides guidance to help you develop a RAG-capable generative AI architecture in Google Cloud that meets your specific requirements for security and compliance, reliability, cost, and performance. The guidance in this section isn't exhaustive. Depending on the specific requirements of your generative AI application and the Google Cloud products and features that you use, you might need to consider additional design factors and trade-offs.

For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 

### Security, privacy, and compliance

This section describes design considerations and recommendations to design a topology in Google Cloud that meets your workload's security and compliance requirements.

For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

#### Agent Platform

Agent Platform supports Google Cloud security controls that you can use to meet your requirements for data residency, data encryption, network security, and access transparency. For more information, see the following documentation:

  * [Security controls for machine learning services](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-controls)
  * [Security controls for Generative AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls)
  * [Agent Platform and zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention)
  * [Enable access transparency for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/access-transparency)
  * [Compliance and security controls for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/compliance-security-controls)



Gemini Enterprise deletes user-requested data within 60 days. For more information, see [Data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).

Generative AI models might produce harmful responses, especially when they are explicitly prompted for such responses. To enhance safety and mitigate potential misuse, you can configure content filters to act as barriers to harmful responses. For more information, see [Safety and content filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters).

#### Cloud Run

By default, Cloud Run encrypts data by using Google-owned and Google-managed encryption keys. To protect your containers by using keys that you control, you can use customer-managed encryption keys (CMEKs). For more information, see [Using customer managed encryption keys](https://docs.cloud.google.com/run/docs/securing/using-cmek).

To ensure that only authorized container images are deployed to Cloud Run, you can use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview).

Cloud Run helps you meet data residency requirements. Your Cloud Run functions run within the selected [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).

#### Cloud Storage

By default, Cloud Storage encrypts the data that it stores by using Google-owned and Google-managed encryption keys. If required, you can use CMEKs or your own keys that you manage by using an external management method like customer-supplied encryption keys (CSEKs). For more information, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

Cloud Storage supports two methods to grant users access to your buckets and objects: Identity and Access Management (IAM) and access control lists (ACLs). In most cases, we recommend that you use IAM, which lets you grant permissions at the bucket and project levels. For more information, see [Overview of access control](https://docs.cloud.google.com/storage/docs/access-control).

The data that you load into the data ingestion subsystem through Cloud Storage might include sensitive data. You can use Sensitive Data Protection to discover, classify, and de-identify sensitive data. For more information, see [Using Sensitive Data Protection with Cloud Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/dlp-gcs).

Cloud Storage helps you meet data residency requirements. Cloud Storage stores or replicates data within the region that you specify.

#### Pub/Sub

By default, Pub/Sub encrypts all of the messages, which includes at rest and in transit messages, by using Google-owned and Google-managed encryption keys. Pub/Sub supports the use of CMEKs for message encryption at the application layer. For more information, see [Configure message encryption](https://docs.cloud.google.com/pubsub/docs/encryption).

If you have data residency requirements, to ensure that message data is stored in specific locations, you can [configure message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).

### Reliability

This section describes design considerations and recommendations to build and operate reliable infrastructure for your deployment in Google Cloud.

For reliability principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

#### Agent Platform

Agent Platform ensures data residency at rest. Agent Platform stores your source data, which includes data for RAG in the managed datastore, within the Google Cloud [location](https://cloud.google.com/about/locations) that you have selected. This separation of processing from storage is a fundamental aspect of how the platform provides both high reliability and compliance.

#### Cloud Run

Cloud Run is a regional service that stores data synchronously across multiple zones within a region. The service automatically load-balances the traffic across the zones. If a zone outage occurs, Cloud Run jobs continue to run and data isn't lost. If a region outage occurs, the Cloud Run jobs stop running until Google resolves the outage.

Individual Cloud Run jobs or tasks might fail. To handle such failures, you can use [task retries](https://docs.cloud.google.com/run/docs/configuring/max-retries) and checkpointing. For more information, see [Jobs retries and checkpoints best practices](https://docs.cloud.google.com/run/docs/jobs-retries).

#### Cloud Storage

You can create Cloud Storage buckets in one of three [location types](https://docs.cloud.google.com/storage/docs/locations): regional, dual-region, or multi-region. For data in regional buckets, Cloud Storage synchronously replicates that data across multiple zones within a region. For higher availability, you can use dual-region or multi-region buckets, where Cloud Storage replicates data asynchronously across regions. Ensure that your choice aligns with your compliance requirements.

### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build by using this reference architecture.

For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

#### Agent Platform

The underlying AI model that the agent invokes can directly influence the cost to use that agent. Pricing is calculated based on the number of input and output tokens for each request. For more information, see [Generative AI on Agent Platform quotas and system limits](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas) and the [Google Cloud pricing calculator](https://cloud.google.com/products/calculator).

For information about how to minimize token count to reduce cost, see the [Context caching overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview).

#### Cloud Run functions

When you create Cloud Run jobs, you specify the amount of memory and CPU to be allocated to the container instance. To control costs, start with the default CPU and memory allocations. To improve performance, you can increase the allocation by configuring the [CPU limit](https://docs.cloud.google.com/run/docs/configuring/jobs/cpu) and [memory limit](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits).

If you can predict the CPU and memory requirements of your Cloud Run jobs, then you can save money with discounts for committed usage. For more information, see [Cloud Run committed use discounts](https://docs.cloud.google.com/run/cud).

#### Cloud Storage

For the Cloud Storage bucket that you use to load data into the data ingestion subsystem, choose an appropriate [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) based on the data-retention and access-frequency requirements of your workloads. For example, you can choose the Standard storage class, and use [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to control storage costs. Object Lifecycle Management automatically downgrades objects to a lower-cost storage class or deletes objects based on conditions that you set.

### Performance optimization

This section describes design considerations and recommendations to design a topology in Google Cloud that meets the performance requirements of your workloads.

For performance optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization) in the Well-Architected Framework. 

#### Gemini Enterprise

To reduce latency during serving, stream responses by sending model responses before the agent generates the complete output. This enables real-time processing of the output, and you can immediately update your user interface and perform other concurrent tasks. Streaming enhances perceived responsiveness and creates a more interactive user experience. For more information, see [Stream answers](https://docs.cloud.google.com/gemini/enterprise/docs/stream-answer).

#### Cloud Run

Adjust the memory and CPU allocation for the Cloud Run instances based on performance requirements. For more information, see [Configure CPU limits for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/cpu) and [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits).

#### Cloud Storage

To upload large files, you can use a method called [parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads). With this strategy, the large file is split into chunks. You upload the chunks to Cloud Storage in parallel, and Cloud Storage then reassembles the data in Google Cloud. Parallel composite uploads can be faster than regular upload operations if you have sufficient network bandwidth and disk speed. However, this strategy has some limitations and cost implications. For more information, see [Parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads).

## Deployment

To deploy this reference architecture, use the Terraform example that's available in GitHub. For more information, see [RAG Infrastructure for Generative AI Applications using Gemini Enterprise and Agent Platform](https://github.com/yelshater/rag-infrastructure-for-gemini-enterprise).

## What's next

  * Learn how [Gemini Enterprise chunks documents for RAG](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents#parse-chunk-rag).
  * Learn how to [host AI apps and agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * Learn about [responsible AI best practices and Agent Platform safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai).
  * Learn about [prompting strategies for LLMs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer

Other contributors: 

  * Deepak Michael | Networking Specialist Customer Engineer
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Yehia Elshater](https://www.linkedin.com/in/yehiaz/) | Field Solutions Architect, Generative AI, Google Cloud
  * [Paarth Mahajan](https://www.linkedin.com/in/paarthmahajan/) | Network Specialist, Google Cloud



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-10 UTC."],[],[]] 
