---
url: https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search/
title: RAG infrastructure for generative AI using Agent Platform and Vector Search \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:07.179428+00:00
---

# RAG infrastructure for generative AI using Agent Platform and Vector Search  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  RAG infrastructure for generative AI using Agent Platform and Vector Search Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-16 UTC

This document provides a reference architecture that you can use to design the infrastructure for a generative AI application with [retrieval-augmented generation (RAG)](https://developers.google.com/machine-learning/glossary#retrieval-augmented_generation) by using [Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview). Vector Search is a fully managed Google Cloud service that provides optimized serving infrastructure for very large-scale vector-similarity matching.

The intended audience for this document includes architects, developers, and administrators of generative AI applications. The document assumes a basic understanding of AI, machine learning (ML), and large language model (LLM) concepts. This document doesn't provide guidance about how to design and develop a generative AI application.

**Note:** Depending on your requirements for application hosting and AI infrastructure, you can consider other architectural approaches for your RAG-capable generative AI application. For more information, see the Design alternatives section in this document.

## Architecture

The following diagram shows a high-level view of the architecture that this document presents:

![A high-level view of the data ingestion and serving flows in the architecture.](https://docs.cloud.google.com/static/architecture/images/gen-ai-rag-vertex-ai-vector-search-high-level-architecture.png)![](https://docs.cloud.google.com/static/architecture/images/gen-ai-rag-vertex-ai-vector-search-high-level-architecture.png)

The architecture in the preceding diagram has two subsystems: data ingestion and serving.

  * The **data ingestion subsystem** ingests data that's uploaded from external sources. The subsystem prepares the data for RAG and interacts with Gemini Enterprise Agent Platform to generate [embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/glossary#embedding) for the ingested data and to build and update the [vector index](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/glossary#index).
  * The **serving subsystem** contains the generative AI application's frontend and backend services. 
    * The frontend service handles the query-response flow with application users and forwards queries to the backend service.
    * The backend service uses Agent Platform to generate query embeddings, perform vector-similarity search, and apply [Responsible AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai) safety filters and system instructions.



The following diagram shows a detailed view of the architecture:

![A detailed view of the data ingestion and serving flows in the architecture.](https://docs.cloud.google.com/static/architecture/images/gen-ai-rag-vertex-ai-vector-search-detailed-architecture.png)![](https://docs.cloud.google.com/static/architecture/images/gen-ai-rag-vertex-ai-vector-search-detailed-architecture.png)

The following sections describe the data flow within each subsystem of the preceding architecture diagram.

### Data ingestion subsystem

The data ingestion subsystem ingests data from external sources and prepares the data for RAG. The following are the steps in the data-ingestion and preparation flow:

  1. Data is uploaded from external sources to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets). The external sources might be applications, databases, or streaming services. 
  2. When data is uploaded to Cloud Storage, a [message is published to a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publish-message-overview). 
  3. When the Pub/Sub topic receives a message, it triggers a [ Cloud Run function](https://docs.cloud.google.com/functions/docs/concepts/overview). 
  4. The Cloud Run function parses the raw data, formats it as required, and divides it into chunks. 
  5. The function uses the [ Agent Platform Embeddings API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings) to create embeddings of the chunks by using an embedding model that you specify. Agent Platform supports [text](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-text-embeddings#supported-models) and [multimodal](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings#supported-models) embedding models. 
  6. The function then builds a Vector Search index of the embeddings and then deploys the index. 



When new data is ingested, the preceding steps are performed for the new data and the index is updated using [streaming updates](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/update-rebuild-index#update-streaming).

When the serving subsystem processes user requests, it uses the Vector Search index for vector-similarity search. The next section describes the serving flow.

### Serving subsystem

The serving subsystem handles the query-response flow between the generative AI application and its users. The following are the steps in the serving flow:

  1. A user submits a natural-language query to a [ Cloud Run service](https://docs.cloud.google.com/run/docs/resource-model#services) that provides a frontend interface (such as a chatbot) for the generative AI application. 
  2. The frontend service forwards the user query to a backend Cloud Run service. 
  3. The backend service processes the query by doing the following: 
     1. Converts the query to embeddings by using the same embeddings model and parameters that the data ingestion subsystem uses to generate embeddings of the ingested data. 
     2. Retrieves relevant [grounding data](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/glossary#ground_truth) by performing a vector-similarity search for the query embeddings in the Vector Search index. 
     3. Constructs an augmented prompt by combining the original query with the grounding data. 
     4. Sends the augmented prompt to an LLM that's deployed on Agent Platform. 
  4. The LLM generates a response.
  5. For each prompt, Agent Platform applies the Responsible AI safety filters that you've configured and then sends the filtered response and AI safety scores to the Cloud Run backend service. 
  6. The application sends the response to the user through the Cloud Run frontend service. 



You can store and view logs of the query-response activity in Cloud Logging, and you can set up logs-based monitoring by using Cloud Monitoring. You can also load the generated responses into BigQuery for offline analytics.

The [Agent Platform prompt optimizer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-optimizer) helps you improve prompts at scale, both during initial prompt design and for ongoing prompt tuning. The prompt optimizer evaluates your model's response to a set of sample prompts that ML engineers provide. The output of the evaluation includes the model's responses to the sample prompts, scores for metrics that the ML engineers specify, and a set of optimized system instructions that you can consider using.

## Products used

This reference architecture uses the following Google Cloud products:

  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview): A vector similarity-matching service that lets you store, index, and search semantically similar or related data. 
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Cloud Run functions](https://cloud.google.com/functions): A serverless compute platform that lets you run single-purpose functions directly in Google Cloud. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Pub/Sub](https://cloud.google.com/pubsub): An asynchronous and scalable messaging service that decouples services that produce messages from services that process those messages.
  * [ Cloud Logging](https://cloud.google.com/logging): A real-time log management system with storage, search, analysis, and alerting.
  * [ Cloud Monitoring](https://cloud.google.com/monitoring): A service that provides visibility into the performance, availability, and health of your applications and infrastructure. 
  * [ BigQuery](https://cloud.google.com/bigquery): An enterprise data warehouse that helps you manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence. 



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

### Alternative RAG architectures

The architecture in this document uses Agent Platform and Vector Search to provide a serverless RAG pipeline for large-scale vector-similarity matching. If you need agent-driven orchestration, co-located relational and vector data, or self-managed open-source models, consider the following alternative architectures:

  * [RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform](https://docs.cloud.google.com/architecture/rag-genai-gemini-enterprise-vertexai): An agent-driven architecture that orchestrates an end-to-end RAG dataflow for enterprise applications that require real-time data availability and enriched contextual search.

  * [RAG infrastructure for generative AI using Agent Platform and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai): An architecture that stores vector embeddings alongside your operational data in a fully managed database.

  * [RAG infrastructure for generative AI using GKE and Cloud SQL](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-gke): A flexible, container-based architecture that provides maximum control to build custom applications with open source tools such as Ray, Hugging Face, and LangChain.




### Application hosting options

The architecture in this document uses Cloud Run as the host for the generative AI application and data processing. Cloud Run is a developer-focused, fully managed application platform. If you need greater configuration flexibility and control over the compute infrastructure, you can deploy your application to [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs) clusters or to [Compute Engine](https://docs.cloud.google.com/compute/docs/overview) VMs.

The decision of whether to use Cloud Run, GKE, or Compute Engine as your application host involves trade-offs between configuration flexibility and management effort. With the serverless Cloud Run option, you deploy your application to a preconfigured environment that requires minimal management effort. With Compute Engine VMs and GKE containers, you're responsible for managing the underlying compute resources, but you have greater configuration flexibility and control. For more information about choosing an appropriate application hosting service, see the following documents:

  * [Is my app a good fit for a Cloud Run service?](https://docs.cloud.google.com/run/docs/fit-for-run)
  * [Choose compute options](https://docs.cloud.google.com/docs/compute-area/choose-compute-options)



## Design considerations

This section describes design factors, best practices, and design recommendations that you should consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, cost, and performance.

The guidance in this section isn't exhaustive. Depending on the specific requirements of your application and the Google Cloud and third-party products and features that you use, there might be additional design factors and trade-offs that you should consider.

### Security, compliance, and privacy

This section describes design considerations and recommendations to design a topology in Google Cloud that meets the security and compliance requirements of your workloads.

#### Agent Platform security considerations

To help ensure that your Agent Platform configurations and usage meet your security requirements, consider the following recommendations:

  * **Security controls** : Agent Platform supports Google Cloud security controls that you can use to meet your requirements for data residency, data encryption, network security, and access transparency. For more information, see [Security controls for machine learning services](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-controls) and [Security controls for Generative AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls).
  * **Model access** : You can set up organization policies to limit the type and versions of LLMs that can be used in a Google Cloud project. For more information, see [Control access to Model Garden models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access).
  * **Shared responsibility** : Agent Platform secures the underlying infrastructure and provides tools and security controls to help you protect your data, code, and models. For more information, see [Agent Platform shared responsibility](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/shared-responsibility).
  * **Data protection** : Use the [Cloud Data Loss Prevention API](https://docs.cloud.google.com/sensitive-data-protection/docs/apis) to discover and de-identify sensitive data, such as personally identifiable information (PII), in the prompts and responses and in log data. For more information, see [Text classification and redaction](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-text-redaction) and [De-identifying sensitive data in text content](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data).



#### Cloud Run security considerations

To help ensure that your Cloud Run implementation meets your security requirements, consider the following recommendations:

  * **Ingress security (frontend service)** : To control external access to the application, [disable the default run.app URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url) of the frontend Cloud Run service and [set up a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless). Along with load-balancing incoming traffic to the application, the load balancer handles SSL certificate management. For added protection, you can use [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor#serverless) to provide request filtering, DDoS protection, and rate limiting for the service.
  * **Ingress security (backend service)** : The Cloud Run service for the application's backend in this architecture doesn't need access from the internet. To ensure that only internal clients can access the service, set the `ingress` parameter to `internal`. For more information, see [Restrict network ingress for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress).
  * **Data encryption** : By default, Cloud Run encrypts data by using a Google-owned and Google-managed encryption key. To protect your containers by using a key that you control, you can use customer-managed encryption keys (CMEK). For more information, see [Using customer managed encryption keys](https://docs.cloud.google.com/run/docs/securing/using-cmek).
  * **Container image security** : To ensure that only authorized container images are deployed to the Cloud Run services, you can use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/run/overview).
  * **Data residency** : Cloud Run helps you to meet data residency requirements. Cloud Run container instances run within the region that you select.



For more guidance about container security, see [General Cloud Run development tips](https://docs.cloud.google.com/run/docs/tips/general#container-security).

#### Cloud Storage security considerations

To help ensure that your Cloud Storage configuration meets your security requirements, consider the following recommendations:

  * **Data encryption** : By default, the data that's stored in Cloud Storage is encrypted using Google-owned and Google-managed encryption keys. If required, you can use CMEKs or your own keys that you manage by using an external management method like customer-supplied encryption keys (CSEKs). For more information, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).
  * **Access control** : To control user access to your buckets and objects in Cloud Storage, you can use Identity and Access Management (IAM) and access control lists (ACLs). In most cases, we recommend that you use IAM, which lets you grant permissions at the bucket and project levels. For more information, see [Overview of access control](https://docs.cloud.google.com/storage/docs/access-control).
  * **Data protection** : The data that you load into the data ingestion subsystem through Cloud Storage might include sensitive data. To protect such data, you can discover, classify, and de-identify the data by using Sensitive Data Protection. For more information, see [Using Sensitive Data Protection with Cloud Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/dlp-gcs).
  * **Network control** : To mitigate the risk of data exfiltration from Cloud Storage, you can create a service perimeter by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_storage).
  * **Data residency** : Cloud Storage helps you to meet data residency requirements. Data is stored or replicated within the regions that you specify.



#### Pub/Sub security considerations

To help ensure that your Pub/Sub configuration meets your security requirements, consider the following recommendations:

  * **Data encryption** : By default, Pub/Sub encrypts all messages, both at rest and in transit, by using Google-owned and Google-managed encryption keys. Pub/Sub supports the use of CMEKs for message encryption at the application layer. For more information, see [Configure message encryption](https://docs.cloud.google.com/pubsub/docs/encryption).
  * **Data residency** : If you have data residency requirements, you can ensure that message data is stored in specific locations by configuring [message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).



#### Cloud Logging security considerations

To help ensure that your Cloud Logging configuration meets your security requirements, consider the following design factors and recommendations:

  * **Administrative activity audit** : Logging of [administrative activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) is enabled by default for all of the Google Cloud services that are used in this reference architecture. You can access the logs through Cloud Logging and use the logs to monitor API calls or other actions that modify the configuration or metadata of Google Cloud resources.
  * **Data access audit** : Logging of [data access events](https://docs.cloud.google.com/logging/docs/audit#data-access) is enabled by default for BigQuery. For the other services that are used in this architecture, you can enable Data Access audit logs. You can use these logs to monitor the following:

    * API calls that read the configuration or metadata of resources.
    * User requests to create, modify, or read user-provided resource data.
  * **Security of log data** : Google doesn't access or use the data in Cloud Logging.

  * **Data residency** : To help meet data residency requirements, you can configure Cloud Logging to store log data in the region that you specify. For more information, see [Regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs).




#### Security considerations for all of the products in the architecture

To help ensure that your architecture meets your security requirements, consider the following general recommendations:

  * **Mitigate data exfiltration risk** : To reduce the risk of data exfiltration, create a [VPC Service Controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls) perimeter around the infrastructure. VPC Service Controls supports all of the services that are used in this reference architecture.
  * **Post-deployment optimization** : After you deploy your application in Google Cloud, use the [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist) service to get recommendations that can help you to further optimize the security of your cloud resources. Review the recommendations and apply them as appropriate for your environment. For more information, see [Find recommendations in Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).
  * **Access control** : Follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) for every cloud service.



For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

### Reliability

This section describes design considerations and recommendations to build and operate reliable infrastructure for your deployment in Google Cloud.

#### Vector Search query scaling

To make sure that the Vector Search index can handle increases in query load, you can configure autoscaling for the index endpoint. When the query load increases, the number of nodes is increased automatically up to the maximum that you specify. For more information, see [Enable autoscaling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/deploy-index-vpc#autoscaling).

#### Cloud Run robustness to infrastructure outages

Cloud Run is a regional service. Data is stored synchronously across multiple zones within a region. Traffic is automatically load-balanced across the zones. If a zone outage occurs, Cloud Run continues to run and data isn't lost. If a region outage occurs, Cloud Run stops running until Google resolves the outage.

#### Cloud Storage data availability

You can create Cloud Storage buckets in one of three [location types](https://docs.cloud.google.com/storage/docs/locations): regional, dual-region, or multi-region. Data that's stored in regional buckets is replicated synchronously across multiple zones within a region. For higher availability, you can use dual-region or multi-region buckets, where data is replicated asynchronously across regions.

#### Pub/Sub reliability considerations

To help ensure that your Pub/Sub configuration meets your reliability requirements, consider the following recommendations:

  * **Rate control** : To avoid errors during periods of transient spikes in message traffic, you can limit the rate of publish requests by configuring [flow control](https://docs.cloud.google.com/pubsub/docs/flow-control-messages) in the publisher settings.
  * **Failure handling** : To handle failed publish attempts, adjust the retry-request variables as necessary. For more information, see [Retry requests](https://docs.cloud.google.com/pubsub/docs/retry-requests).



#### BigQuery robustness to infrastructure outages

Data that you load into BigQuery is stored synchronously in two zones within the region that you specify. This redundancy helps to ensure that your data isn't lost when a zone outage occurs. For more information about reliability features in BigQuery, see [Understand reliability](https://docs.cloud.google.com/bigquery/docs/reliability-intro).

#### Reliability recommendations for all of the products in the architecture

After you deploy your workload in Google Cloud, further optimize the reliability of your cloud resources by applying relevant [recommendations from Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).

For reliability principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build by using this reference architecture.

#### Vector Search cost considerations

To help optimize the cost of Vector Search, consider the following design factors and recommendations:

  * **Query batching** : Billing for Vector Search depends on the size of your index, queries per second (QPS), and the number and machine type of the nodes that you use for the index endpoint. For high-QPS workloads, batching the queries can help to reduce cost. For information about how you can estimate Vector Search cost, see [Vector Search pricing examples](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing#vector-search).
  * **Index endpoint autoscaling** : To improve the utilization of the compute nodes on which the Vector Search index is deployed, you can configure autoscaling for the index endpoint. When demand is low, the number of nodes is reduced automatically to the minimum that you specify. For more information, see [Enable autoscaling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/deploy-index-vpc#autoscaling).



#### Cloud Run cost considerations

To help ensure that your Cloud Run implementation meets your cost requirements, consider the following recommendations:

  * **Resource allocation** : When you create Cloud Run services, you specify the amount of memory and CPU to be allocated to the container instance. To control costs, start with the default (minimum) CPU and memory allocations. To improve performance, you can increase the allocation by configuring the CPU limit and memory limit. For more information, see the following documentation:

    * [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits)
    * [Configure CPU limits for services](https://docs.cloud.google.com/run/docs/configuring/services/cpu)
  * **Rate optimization** : If you can predict the CPU and memory requirements of your Cloud Run services, then you can save money by getting discounts for committed usage. For more information, see [Cloud Run committed use discounts](https://docs.cloud.google.com/run/cud).




#### Cloud Storage cost considerations

For the Cloud Storage bucket that you use to load data into the data ingestion subsystem, choose an appropriate [storage class](https://docs.cloud.google.com/storage/docs/storage-classes). When you choose the storage class, consider the data-retention and access-frequency requirements of your workloads. For example, to control storage costs, you can choose the Standard class and use [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle). Doing so enables automatic downgrade of objects to a lower-cost storage class or deletion of objects based on conditions that you set.

#### Cloud Logging cost considerations

To control the cost of storing logs, consider the following recommendations:

  * Reduce the volume of logs by excluding or filtering unnecessary log entries. For more information, see [Exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).
  * Optimize the log-retention period. For more information, see [Configure custom retention](https://docs.cloud.google.com/logging/docs/buckets#custom-retention).



#### BigQuery cost considerations

BigQuery lets you estimate the cost of queries before you run them. To optimize query costs, you need to optimize storage and query computation. For more information, see [Estimate and control costs](https://docs.cloud.google.com/bigquery/docs/best-practices-costs).

#### Cost-optimization recommendations for all of the products in the architecture

To help ensure that your architecture meets your cost requirements, consider the following general recommendations:

  * **Post-deployment optimization** : After you deploy your workload in Google Cloud, further optimize the cost of the deployed resources by applying relevant [recommendations from Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).
  * **Cost estimation** : To estimate the cost of your Google Cloud resources, use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).



For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

### Performance optimization

This section describes design considerations and recommendations to design a topology in Google Cloud that meets the performance requirements of your workloads.

#### Vector Search performance considerations

To help ensure that your Vector Search configuration meets your performance requirements, consider the following recommendations:

  * **Index configuration** : When you create the index, set the shard size, distance measure type, and number of embeddings for each leaf node based on your performance requirements. For example, if your application is extremely sensitive to latency variability, we recommend a large shard size. For more information, see [Configuration parameters that affect performance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/create-manage-index#performance-parameters).
  * **Compute capacity** : When you configure the compute capacity of the nodes on which the Vector Search index is deployed, consider your requirements for performance. Choose an appropriate machine type and set the maximum number of nodes based on the query load that you expect. For more information, see [Deployment settings that affect performance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/deploy-index-vpc#performance).
  * **Query parameters** : Configure the query parameters for the Vector Search index based on your requirements for query performance, availability, and cost. For example, the `approximateNeighborsCount` parameter specifies the number of neighbors that must be retrieved before exact reordering is performed. Decreasing the value of this parameter can help to reduce latency and cost. For more information, see [Query-time settings that affect performance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/query-index-vpc#performance).
  * **Index updates** : An index that's up-to-date helps to improve the accuracy of the generated responses. You can update your Vector Search index by using batch or streaming updates. Streaming updates let you perform near real-time queries on updated data. For more information, see [Update and rebuild an active index](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/update-rebuild-index).



#### Cloud Run performance considerations

To help ensure that your Cloud Run implementation meets your performance requirements, consider the following recommendations:

  * **Resource allocation** : By default, each Cloud Run container instance is allocated one CPU and 512 MiB of memory. Depending on the performance requirements, you can configure the CPU limit and the memory limit. For more information, see the following documentation:

    * [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits)
    * [Configure CPU limits for services](https://docs.cloud.google.com/run/docs/configuring/services/cpu)
  * **Minimum instances** : To help minimize latency even after a period of no traffic, you can configure a [minimum number of instances](https://docs.cloud.google.com/run/docs/configuring/min-instances). When such instances are idle, the CPU and memory that are allocated to the instances are billed at a lower price.




For more performance optimization guidance, see [General Cloud Run development tips](https://docs.cloud.google.com/run/docs/tips/general#optimize_performance).

#### Cloud Storage performance considerations

To upload large files, you can use a method called parallel composite uploads. With this strategy, the large file is split into chunks. The chunks are uploaded to Cloud Storage in parallel and then the data is recomposed in the cloud. When network bandwidth and disk speed aren't limiting factors, then parallel composite uploads can be faster than regular upload operations. However, this strategy has some limitations and cost implications. For more information, see [Parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads).

#### BigQuery performance considerations

To help ensure that your BigQuery usage meets your performance requirements, consider the following recommendations:

  * **Query performance insights** : BigQuery provides a query execution graph that you can use to analyze query performance and get performance insights for issues like slot contention and insufficient shuffle quota. For more information, see [Get query performance insights](https://docs.cloud.google.com/bigquery/docs/query-insights).
  * **Query computation optimization** : After you address the issues that you identify through query performance insights, you can further optimize queries by using techniques like reducing the volume of input and output data. For more information, see [Optimize query computation](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute).



#### Performance-optimization recommendations for all of the products in the architecture

After you deploy your workload in Google Cloud, further optimize the performance of your cloud resources by applying relevant [recommendations from Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/find-recommendations).

For performance optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization) in the Well-Architected Framework. 

## Deployment

To deploy a topology that's based on this reference architecture, you can download and use the Terraform sample configuration that's available in a repository in [GitHub](https://github.com/GoogleCloudPlatform/architecture-center-samples/tree/main/gen-ai-rag-vertex-ai-vector-search). Follow the instructions in the README in the repository. The sample code isn't intended for production use cases.

## What's next

  * [Build a generative AI application on Cloud Run](https://docs.cloud.google.com/run/docs/ai)
  * [RAG infrastructure for generative AI using Agent Platform and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai)
  * [RAG infrastructure for generative AI using GKE and Cloud SQL](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-gke)
  * [RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform](https://docs.cloud.google.com/architecture/rag-genai-gemini-enterprise-vertexai)
  * [GraphRAG infrastructure for generative AI using Agent Platform and Spanner Graph](https://docs.cloud.google.com/architecture/gen-ai-graphrag-spanner)
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer

Other contributors: 

  * [Assaf Namer](https://www.linkedin.com/in/assaf-namer-0677644) | Principal Cloud Security Architect
  * Deepak Michael | Networking Specialist Customer Engineer
  * [Divam Anand](https://www.linkedin.com/in/divam-anand-25469b50) | Product Strategy and Operations Lead
  * [Eran Lewis](https://www.linkedin.com/in/eranlewis) | Senior Product Manager
  * [Jerome Simms](https://www.linkedin.com/in/jeromesimms) | Director, Product Management
  * Katie McLaughlin | Senior Developer Relations Engineer
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Megan O'Keefe](https://www.linkedin.com/in/askmeegs) | Developer Advocate
  * [Nicholas McNamara](https://www.linkedin.com/in/nsbm) | Product and Commercialization Strategy Principal
  * [Preston Holmes](https://www.linkedin.com/in/ptone) | Outbound Product Manager - App Acceleration
  * [Rob Edwards](https://www.linkedin.com/in/robedwards) | Technology Practice Lead, DevOps
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Wietse Venema](https://www.linkedin.com/in/wietse-venema) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
