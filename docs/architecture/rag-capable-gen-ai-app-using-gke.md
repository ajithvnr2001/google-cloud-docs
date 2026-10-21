---
url: https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-gke/
title: RAG infrastructure for generative AI using GKE and Cloud SQL \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:33.046131+00:00
---

# RAG infrastructure for generative AI using GKE and Cloud SQL  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  RAG infrastructure for generative AI using GKE and Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-02-24 UTC

This document provides a reference architecture that you can use to design the infrastructure to run a generative AI application with [retrieval-augmented generation (RAG)](https://developers.google.com/machine-learning/glossary/#retrieval-augmented_generation) using Google Kubernetes Engine (GKE), Cloud SQL, and open source tools like Ray, Hugging Face, and LangChain. To help you experiment with this reference architecture, a sample application and Terraform configuration are provided in [GitHub](https://github.com/GoogleCloudPlatform/ai-on-gke/blob/main/applications/rag).

This document is for developers who want to rapidly build and deploy RAG-capable generative AI applications by using open source tools and models. It assumes that you have experience with using GKE and Cloud SQL and that you have a conceptual understanding of AI, machine learning (ML), and large language models (LLMs). This document doesn't provide guidance about how to design and [develop a generative AI application](https://docs.cloud.google.com/docs/ai-ml/generative-ai/develop-generative-ai-application).

## Architecture

The following diagram shows a high-level view of an architecture for a RAG-capable generative AI application in Google Cloud:

![A high-level architecture for a RAG-capable generative AI application in Google Cloud.](https://docs.cloud.google.com/static/architecture/images/rag-capable-gen-ai-app-using-gke-architecture-high-level.svg)

The architecture contains a serving subsystem and an embedding subsystem.

  * The **serving subsystem** handles the request-response flow between the application and its users. The subsystem includes a frontend server, an inference server, and a [responsible AI (RAI)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai) service. The serving subsystem interacts with the embedding subsystem through a [vector database](https://cloud.google.com/discover/what-is-a-vector-database).
  * The **embedding subsystem** enables the RAG capability in the architecture. This subsystem does the following: 
    * Ingests data from data sources in Google Cloud, on-premises, and other cloud platforms.
    * Converts the ingested data to [embedding vectors](https://developers.google.com/machine-learning/glossary#embedding-vector).
    * Stores the embeddings in a vector database.



The following diagram shows a detailed view of the architecture:

![A detailed architecture for a RAG-capable generative AI application in Google Cloud.](https://docs.cloud.google.com/static/architecture/images/rag-capable-gen-ai-app-using-gke-architecture.svg)

![](https://docs.cloud.google.com/static/architecture/images/rag-capable-gen-ai-app-using-gke-architecture.svg)

As shown in the preceding diagram, the frontend server, inference server, and embedding service are deployed in a regional GKE cluster in [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) mode. Data for RAG is ingested through a Cloud Storage bucket. The architecture uses a Cloud SQL for PostgreSQL instance with the [`pgvector`](https://github.com/pgvector/pgvector) extension to store embedding vectors and perform semantic searches.

**Note:** The preceding diagram doesn't show networking resources. For guidance to design and configure networking, see [Private connectivity for RAG-capable generative AI applications](https://docs.cloud.google.com/architecture/private-connectivity-rag-capable-gen-ai) and [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking).

The following sections describe the components and data flow within each subsystem of the architecture.

### Embedding subsystem

The following is the flow of data in the embedding subsystem:

  1. Data from external and internal sources is uploaded to the Cloud Storage bucket by human users or programmatically. The uploaded data might be in files, databases, or streamed data.
  2. (Not shown in the architecture diagram.) The data upload activity triggers an event that's published to a messaging service like Pub/Sub. The messaging service sends a notification to the embedding service.
  3. When the embedding service receives a notification of a data upload event, it does the following: 
     1. Retrieves data from the Cloud Storage bucket through the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver).
     2. Reads the uploaded data and preprocesses it using [Ray Data](https://docs.ray.io/en/latest/data/data.html). The preprocessing can include chunking the data and transforming it into a suitable format for embedding generation.
     3. Runs a [Ray job](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/index.html) to create embedding vectors of the preprocessed data by using an open-source model that's deployed in the same cluster.
     4. Writes the embedding vectors to the Cloud SQL for PostgreSQL vector database.



As described in the following section, when the serving subsystem processes user requests, it uses the embedding vectors to retrieve relevant domain-specific data.

### Serving subsystem

The following is the request-response flow in the serving subsystem:

  1. A user submits a natural-language request to a frontend server through a web-based chat interface. The frontend server runs on GKE.
  2. The frontend server runs a [LangChain](https://www.langchain.com/) process that does the following: 
     1. Converts the natural-language request to embedding vectors by using the same model and parameters that the embedding service uses.
     2. Retrieves relevant grounding data by performing a [semantic search](https://cloud.google.com/discover/what-is-semantic-search) for the embeddings in the vector database.
     3. Constructs a contextualized prompt by combining the original request with the grounding data that was retrieved.
     4. Sends the contextualized prompt to the inference server, which runs on GKE.
  3. The inference server uses the [Hugging Face TGI](https://github.com/huggingface/text-generation-inference) serving framework to serve an open model like [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) or [Gemma](https://ai.google.dev/gemma).
  4. The LLM generates a response to the prompt, and the inference server sends the response to the frontend server.

You can store and view logs of the request-response activity in Cloud Logging, and you can set up logs-based monitoring by using Cloud Monitoring. You can also load the generated responses into BigQuery for offline analytics.

  5. The frontend server invokes an RAI service to apply the required safety filters to the response. You can use tools like [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) and [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs/reference/rest) to discover, filter, classify, and de-identify sensitive content in the responses.

  6. The frontend server sends the filtered response to the user.




## Products used

The following is a summary of the Google Cloud and open-source products that the preceding architecture uses:

### Google Cloud products

  * [ Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine): A Kubernetes service that you can use to deploy and operate containerized applications at scale using Google's infrastructure. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Cloud SQL](https://cloud.google.com/sql): A fully managed relational database service that helps you provision, operate, and manage your MySQL, PostgreSQL, and SQL Server databases on Google Cloud. 



### Open-source products

  * [ Hugging Face Text Generation Inference (TGI)](https://huggingface.co/docs/text-generation-inference/en/index): A toolkit for deploying and serving LLMs.
  * [ Ray](https://www.ray.io/): An open-source unified compute framework that helps you scale AI and Python workloads.
  * [ LangChain](https://www.langchain.com/): A framework for developing and deploying applications powered by LLMs. 



## Use cases

RAG is an effective technique to improve the quality of output that's generated from an LLM. This section provides examples of use cases for which you can use RAG-capable generative AI applications.

### Personalized product recommendations

An online shopping site might use an LLM-powered chatbot to assist customers with finding products or getting shopping-related help. The questions from a user can be augmented by using historical data about the user's buying behavior and website interaction patterns. The data might include user reviews and feedback that's stored in an unstructured datastore or search-related metrics that are stored in a web analytics data warehouse. The augmented question can then be processed by the LLM to generate personalized responses that the user might find more appealing and compelling.

### Clinical assistance systems

Doctors in hospitals need to quickly analyze and diagnose a patient's health condition to make decisions about appropriate care and medication. A generative AI application that uses a medical LLM like [Med-PaLM](https://sites.research.google/med-palm/) can be used to assist doctors in their clinical diagnosis process. The responses that the application generates can be grounded in historical patient records by contextualizing the doctors' prompts with data from the hospital's electronic health record (EHR) database or from an external knowledge base like [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

### Efficient legal research

Generative AI-powered legal research lets lawyers quickly query large volumes of statutes and case laws to identify relevant legal precedents or summarize complex legal concepts. The output of such research can be enhanced by augmenting a lawyer's prompts with data that's retrieved from the law firm's proprietary corpus of contracts, past legal communication, and internal case records. This design approach ensures that the generated responses are relevant to the legal domain that the lawyer specializes in.

## Design alternatives

This section presents alternative design approaches that you can consider for your RAG-capable generative AI application in Google Cloud.

### Fully managed vector search

If you need an architecture that uses a fully managed vector search product, you can use Gemini Enterprise Agent Platform and Vector Search, which provides optimized serving infrastructure for very large-scale vector search. For more information, see [RAG infrastructure for generative AI using Gemini Enterprise Agent Platform and Vector Search](https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search).

### Other RAG architectures

For information about additional architecture options for RAG workloads, see [Generative AI with RAG](https://docs.cloud.google.com/architecture/rag-reference-architectures).

## Design considerations

This section provides guidance to help you develop and run a GKE-hosted RAG-capable generative AI architecture that meets your specific requirements for security and compliance, reliability, cost, and performance. The guidance in this section isn't exhaustive. Depending on the specific requirements of your application and the Google Cloud products and features that you use, you might need to consider additional design factors and trade-offs.

For design guidance related to the open-source tools in this reference architecture, see the documentation for those tools.

### Security, privacy, and compliance

This section describes factors that you should consider when you design and build a RAG-capable generative AI application in Google Cloud that meets your security, privacy, and compliance requirements.

Product | Design considerations  
---|---  
GKE |  In the Autopilot mode of operation, GKE pre-configures your cluster and manages nodes according to security best practices, which lets you focus on workload-specific security. For more information, see [GKE Autopilot security measures](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security).  To ensure enhanced access control for your applications running in GKE, you can use Identity-Aware Proxy (IAP). IAP integrates with the GKE Ingress resource and ensures that only authenticated users with the correct Identity and Access Management (IAM) role can access the applications. For more information, see [ Enabling IAP for GKE](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto).  By default, your data in GKE is encrypted [ at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [ in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit) using Google-owned and Google-managed encryption keys. As an additional layer of security for sensitive data, you can encrypt data at the application layer by using a key that you own and manage with Cloud KMS. For more information, see [ Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).  If you use a Standard GKE cluster, then you can use the following additional data-encryption capabilities: 

  * Encrypt data in use (that is, in memory) by using Confidential Google Kubernetes Engine Nodes. For more information about the features, availability, and limitations of Confidential GKE Nodes, see [ Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes). 
  * If you need more control over the encryption keys that are used to encrypt Pod traffic across GKE nodes, then you can encrypt the data in transit by using keys that you manage. For more information, see [ Encrypt your data in-transit in GKE with user-managed encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-inter-node-transparent-encryption). 

  
Cloud SQL |  The Cloud SQL instance in the architecture doesn't need to be accessible from the public internet. If external access to the Cloud SQL instance is necessary, you can encrypt external connections by using [ SSL/TLS](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl) or the [ Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) connector. The Auth Proxy connector provides connection authorization by using IAM. The connector uses a TLS 1.3 connection with a 256-bit AES cipher to verify client and server identities and encrypt data traffic. For connections that are created by using Java, Python, Go, or Node.js, use the appropriate [Language Connector](https://docs.cloud.google.com/sql/docs/postgres/language-connectors) instead of the Auth Proxy connector. By default, Cloud SQL uses Google-owned and Google-managed data encryption keys (DEK) and key encryption keys (KEK) to encrypt data at rest. If you need to use KEKs that you control and manage, you can use [ customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/sql/docs/postgres/cmek).  To prevent unauthorized access to the Cloud SQL Admin API, you can create a service perimeter by using [ VPC Service Controls](https://docs.cloud.google.com/sql/docs/postgres/admin-api/configure-service-controls).  For information about configuring Cloud SQL to help meet data residency requirements, see [ Data residency overview](https://docs.cloud.google.com/sql/docs/postgres/data-residency-overview).   
Cloud Storage |  By default, the data that's stored in Cloud Storage is encrypted using Google-owned and Google-managed encryption keys. If required, you can use CMEKs or your own keys that you manage by using an external management method like customer-supplied encryption keys (CSEKs). For more information, see [ Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).  Cloud Storage supports two methods for controlling user access to your buckets and objects: IAM and access control lists (ACLs). In most cases, we recommend using IAM, which lets you grant permissions at the bucket and project levels. For more information, see [ Overview of access control](https://docs.cloud.google.com/storage/docs/access-control).  The data that you load into the embedding subsystem through Cloud Storage might include sensitive data. To protect such data, you can use Sensitive Data Protection to discover, classify, and de-identify the data. For more information, see [ Using Sensitive Data Protection with Cloud Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/dlp-gcs).  To mitigate the risk of data exfiltration from Cloud Storage, you can create a service perimeter by using [ VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_storage).  Cloud Storage helps you meet data residency requirements. Data is stored or replicated within the [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) that you specify.   
All of the products in this architecture |  [ Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) are enabled by default for all of the Google Cloud services that are used in this reference architecture. You can access the logs through Cloud Logging. Use these logs to monitor API calls or other actions that modify the configuration or metadata of Google Cloud resources.  [ Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) are also enabled by default for all of the Google Cloud services in this architecture. You can use these logs to monitor the following: 

  * API calls that read the configuration or metadata of resources. 
  * User requests to create, modify, or read user-provided resource data. 

Google doesn't access or use the data in Cloud Logging.  After you deploy your application in Google Cloud, get recommendations to further optimize security by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).   
  
For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

### Reliability

This section describes design factors that you should consider to build and operate reliable infrastructure for a RAG-capable generative AI application in Google Cloud.

Product | Design considerations  
---|---  
GKE |  With the Autopilot mode of operation that's used in this architecture, GKE provides the following built-in reliability capabilities: 

  * Your workload uses a [ regional GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters). The control plane and worker nodes are spread across three different zones within a region. Your workloads are robust against zone outages. Regional GKE clusters have a higher uptime [ SLA](https://cloud.google.com/kubernetes-engine/sla) than zonal clusters. 
  * You don't need to create nodes or manage node pools. GKE automatically creates the required node pools and scales them automatically based on the load. 

To ensure that sufficient GPU capacity is available when required for autoscaling the GKE cluster, you can create and use _reservations_. A reservation provides assured capacity in a specific zone for a specified resource. A reservation can be specific to a project, or shared across multiple projects. You incur charges for reserved resources even if the resources aren't provisioned or used. For more information, see [ Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).  Minimize the startup time for the inference server by using techniques like optimized data loading, Image streaming, and fast-starting nodes. For more information, see [Optimize cold start latency for inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference#optimize-cold-start).   
Cloud SQL |  To ensure that the vector database is robust against database failures and zone outages, use an [ HA-configured](https://docs.cloud.google.com/sql/docs/postgres/high-availability) Cloud SQL instance. In the event of a failure of the primary database or a zone outage, Cloud SQL fails over automatically to the standby database in another zone. You don't need to change the IP address for the database endpoint.  To ensure that your Cloud SQL instances are covered by the [ SLA](https://cloud.google.com/sql/sla), follow the recommended operational guidelines. For example, ensure that CPU and memory are properly sized for the workload, and [ enable automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen). For more information, see [ Operational guidelines](https://docs.cloud.google.com/sql/docs/postgres/operational-guidelines).   
Cloud Storage |  You can create Cloud Storage buckets in one of the following [ location types](https://docs.cloud.google.com/storage/docs/locations): regional, dual-region, or multi-region. Data that's stored in regional buckets is replicated synchronously across multiple zones within a region. For higher availability, you can use dual-region or multi-region buckets, where data is replicated asynchronously across regions.   
All of the products in the architecture |  After you deploy your application in Google Cloud, get recommendations to further optimize reliability by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).   
  
For reliability principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

### Cost optimization

This section provides guidance to help you optimize the cost of setting up and operating a RAG-capable generative AI application in Google Cloud.

Product | Design considerations  
---|---  
GKE |  In Autopilot mode, GKE optimizes the efficiency of your cluster's infrastructure based on workload requirements. You don't need to constantly monitor resource utilization or manage capacity to control costs.  If you can predict the CPU, memory, and ephemeral storage usage of your GKE Autopilot cluster, then you can save money by getting discounts for committed usage. For more information, see [ GKE committed use discounts](https://docs.cloud.google.com/kubernetes-engine/cud).  To reduce the cost of running your application, you can use [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) for your GKE nodes. Spot VMs are priced lower than standard VMs, but they might be [preempted](https://docs.cloud.google.com/compute/docs/instances/spot#preemption).  For more cost-optimization guidance, see the following resources:

  * [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke)
  * [Optimize for efficiency and cost](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference#efficiency)

  
Cloud SQL |  A high availability (HA) configuration helps to reduce downtime for your Cloud SQL database when the zone or instance becomes unavailable. However, the [ cost of an HA-configured instance](https://docs.cloud.google.com/sql/pricing) is higher than that of a standalone instance. If you don't need HA for the vector database, then you can reduce cost by using a standalone instance, which isn't robust against zone outages.  You can detect whether your Cloud SQL instance is over-provisioned and optimize billing by using Cloud SQL cost insights and recommendations powered by Active Assist. For more information, see [ Reduce over-provisioned Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned).  If you can predict the CPU and memory requirements of your Cloud SQL instance, then you can save money by getting discounts for committed usage. For more information, see [ Cloud SQL committed use discounts](https://docs.cloud.google.com/sql/cud).   
Cloud Storage |  For the Cloud Storage bucket that you use to load data into the embedding subsystem, choose an appropriate [ storage class](https://docs.cloud.google.com/storage/docs/storage-classes). When you choose the storage class, consider the data-retention and access-frequency requirements of your workloads. For example, to control storage costs, you can choose the Standard class and use [ Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle). Doing so enables automatic downgrade of objects to a lower-cost storage class or deletion of objects based on conditions that you set.   
All of the products in the architecture |  After you deploy your application in Google Cloud, get recommendations to further optimize cost by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).   
  
To estimate the cost of your Google Cloud resources, use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).

For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

### Performance optimization

This section describes the factors that you should consider when you design and build a RAG-capable generative AI application in Google Cloud that meets your performance requirements.

Product | Design considerations  
---|---  
GKE |  Choose appropriate [ compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use) for your Pods based on the performance requirements of the workloads. For the Pods that run the inference server and the embedding service, we recommend that you use a [ GPU machine type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) like `nvidia-l4`.   
Cloud SQL |  To optimize the performance of your Cloud SQL instance, ensure that the CPU and memory that are allocated to the instance are adequate for the workload. For more information, see [ Optimize underprovisioned Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/recommender-underprovisioned).  To improve the response time for approximate nearest neighbor (ANN) vector search, use the [ Inverted File with Flat Compression (IVFFlat)](https://github.com/pgvector/pgvector#ivfflat) index or [ Hierarchical Navigable Small World (HNSW)](https://github.com/pgvector/pgvector#hnsw) index  To help you analyze and improve the query performance of the databases, Cloud SQL provides a Query Insights tool. You can use this tool to monitor performance and trace the source of a problematic query. For more information, see [ Use Query insights to improve query performance](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).  To get an overview of the status and performance of your databases and to view detailed metrics such as peak connections and disk utilization, you can use the System Insights dashboard. For more information, see [ Use System insights to improve system performance](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights).   
Cloud Storage |  To upload large files, you can use a method called _parallel composite uploads_. With this strategy, the large file is split into chunks. The chunks are uploaded to Cloud Storage in parallel and then the data is recomposed in the cloud. When network bandwidth and disk speed aren't limiting factors, then parallel composite uploads can be faster than regular upload operations. However, this strategy has some limitations and cost implications. For more information, see [ Parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads).   
All of the products in the architecture |  After you deploy your application in Google Cloud, get recommendations to further optimize performance by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).   
  
For performance optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization) in the Well-Architected Framework. 

## Deployment

To deploy a topology that's based on this reference architecture, you can download and use the open-source sample code that's available in a repository in [GitHub](https://github.com/ai-on-gke/quick-start-guides/tree/main/rag). The sample code isn't intended for production use cases. You can use the code to experiment with setting up AI infrastructure for a RAG-enabled generative AI application.

The sample code does the following:

  1. Provisions a Cloud SQL for PostgreSQL instance to serve as the vector database.
  2. Deploys Ray, JupyterHub, and Hugging Face TGI to a GKE cluster that you specify.
  3. Deploys a sample web-based chatbot application to your GKE cluster to let you verify the RAG capability.

**Note:** The sample code doesn't set up a messaging component to notify the embedding service when data is uploaded to Cloud Storage. The code includes a Jupyter notebook that you use to upload data to Cloud Storage and trigger the Ray job to generate embeddings.

For instructions to use the sample code, see the [README](https://github.com/ai-on-gke/website/blob/main/site/content/docs/blueprints/rag-on-gke/index.md) for the code. If any errors occur when you use the sample code, and if open [GitHub issues](https://github.com/ai-on-gke/quick-start-guides/issues) don't exist for the errors, then create issues in GitHub.

The sample code deploys billable Google Cloud resources. When you finish using the code, remove any resources that you no longer need.

## What's next

  * Review the following GKE best practices guides: 
    * [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)
    * [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke)
  * [Serve Gemma open models using GPUs on GKE with Hugging Face TGI](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-tgi).
  * [Build RAG infrastructure for generative AI using Agent Platform and Vector Search](https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search).
  * [Build RAG infrastructure for generative AI using Agent Platform and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai).
  * [Build RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform](https://docs.cloud.google.com/architecture/rag-genai-agentspace-vertexai).
  * [Build GraphRAG infrastructure for generative AI using Agent Platform and Spanner Graph](https://docs.cloud.google.com/architecture/gen-ai-graphrag-spanner).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer

Other contributors: 

  * [Anna Berenberg](https://www.linkedin.com/in/annaberenberg) | Engineering Fellow
  * [Ali Zaidi](https://www.linkedin.com/in/alizaidis) | Solutions Architect
  * [Bala Narasimhan](https://www.linkedin.com/in/balanarasimhan) | Group Product Manager
  * [Bill Bernsen](https://www.linkedin.com/in/billbernsen) | Security Engineer
  * [Brandon Royal](https://www.linkedin.com/in/brandonroyal) | Outbound Product Manager
  * [Cynthia Thomas](https://www.linkedin.com/in/cynthia-thomas) | Product Manager
  * [Geoffrey Anderson](https://www.linkedin.com/in/geoffsdesk) | Product Manager
  * [Gleb Otochkin](https://www.linkedin.com/in/glebotochkin) | Cloud Advocate, Databases
  * [Jack Wotherspoon](https://www.linkedin.com/in/jack-wotherspoon) | Developer Advocate
  * [Julie Amundson](https://www.linkedin.com/in/julieamundson) | Senior Staff Software Engineer
  * [Kent Hua](https://www.linkedin.com/in/kenthua) | Solutions Manager
  * [Kavitha Rajendran](https://www.linkedin.com/in/kavitharajendran88) | AI/ML Specialist, Solutions Architect
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Megan O'Keefe](https://www.linkedin.com/in/askmeegs) | Developer Advocate
  * [Mofi Rahman](https://www.linkedin.com/in/moficodes) | Google Cloud Advocate



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
