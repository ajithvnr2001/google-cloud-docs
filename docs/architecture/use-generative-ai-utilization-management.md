---
url: https://docs.cloud.google.com/architecture/use-generative-ai-utilization-management/
title: Automate utilization-review of health insurance claims using generative AI \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:02.524181+00:00
---

# Automate utilization-review of health insurance claims using generative AI  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/use-generative-ai-utilization-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Automate utilization-review of health insurance claims using generative AI Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-19 UTC

This document describes a reference architecture for health insurance companies who want to automate prior authorization (PA) request processing and improve their utilization review (UR) processes by using Google Cloud. It's intended for software developers and program administrators in these organizations. This architecture helps to enable health plan providers to reduce administrative overhead, increase efficiency, and enhance decision-making by automating data ingestion and the extraction of insights from clinical forms. It also allows them to use AI models for prompt generation and recommendations.

## Architecture

The following diagram describes an architecture and an approach for automating the data ingestion workflow and optimizing the utilization management (UM) review process. This approach uses data and AI services in Google Cloud.

![Data ingestion and UM review process high-level overview.](https://docs.cloud.google.com/static/architecture/images/um-review-process.svg)

The preceding architecture contains two flows of data, which are supported by the following subsystems:

  * **Claims data activator (CDA)**, which extracts data from unstructured sources, such as forms and documents, and ingests it into a database in a structured, machine-readable format. CDA implements the flow of data to ingest PA request forms.
  * **Utilization review service (UR service)**, which integrates PA request data, policy documents, and other care guidelines to generate recommendations. The UR service implements the flow of data to review PA requests by using generative AI.



The following sections describe these flows of data.

### CDA flow of data

The following diagram shows the flow of data for using CDA to ingest PA request forms.

![PA case managers flow of data.](https://docs.cloud.google.com/static/architecture/images/pa-case-manager-dataflow.svg)

As shown in the preceding diagram, the PA case manager interacts with the system components to ingest, validate, and process the PA requests. The PA case managers are the individuals from the business operations team who are responsible for the intake of the PA requests. The flow of events is as follows:

  1. The PA case managers receive the PA request forms (`pa_forms`) from the healthcare provider and uploads them to the `pa_forms_bkt` Cloud Storage bucket.
  2. The `ingestion_service` service listens to the `pa_forms_bkt` bucket for changes. The `ingestion_service` service picks up `pa_forms`forms from the `pa_forms_bkt` bucket. The service identifies the pre-configured Document AI processors, which are called `form_processors`. These processors are defined to process the `pa_forms` forms. The `ingestion_service` service extracts information from the forms using the `form_processors` processors. The data extracted from the forms is in JSON format.
  3. The `ingestion_service` service writes the extracted information with field-level confidence scores into the Firestore database collection, which is called `pa_form_collection`.
  4. The `hitl_app` application fetches the information (JSON) with confidence scores from the `pa_form_collection` database. The application calculates the document-level confidence score from the field-level confidence scores made available in the output by the `form_processors` machine learning (ML) models.
  5. The `hitl_app` application displays the extracted information with the field and document level confidence scores to the PA case managers so that they can review and correct the information if the extracted values are inaccurate. PA case managers can update the incorrect values and save the document in the `pa_form_collection` database.



### UR service flow of data

The following diagram shows the flow of data for the UR service.

![UR specialist flow of data.](https://docs.cloud.google.com/static/architecture/images/ur-specialist-dataflow.svg)

As shown in the preceding diagram, the UR specialists interact with the system components to conduct a clinical review of the PA requests. The UR specialists are typically nurses or physicians with experience in a specific clinical area who are employed by healthcare insurance companies. The case management and routing workflow for PA requests is out of scope for the workflow that this section describes.

The flow of events is as follows:

  1. The `ur_app` application displays a list of PA requests and their review status to the UR specialists. The status shows as `in_queue`, `in_progress`, or `completed`.
  2. The list is created by fetching the `pa_form information` data from the `pa_form_collection` database. The UR specialist opens a request by clicking an item from the list displayed in the `ur_app` application.
  3. The `ur_app` application submits the `pa_form information` data to the `prompt_model` model. It uses the Agent Platform Gemini API to generate a prompt that's similar to the following:
         
         Review a PA request for {medication|device|medical service} for our member, {Patient Name}, who is {age} old, {gender} with {medical condition}. The patient is on {current medication|treatment list}, has {symptoms}, and has been diagnosed with {diagnosis}.
         

  4. The `ur_app` application displays the generated prompt to the UR specialists for review and feedback. UR specialists can update the prompt in the UI and send it to the application.

  5. The `ur_app` application sends the prompt to the `ur_model` model with a request to generate a recommendation. The model generates a response and returns to the application. The application displays the recommended outcome to the UR specialists.

  6. The UR specialists can use the `ur_search_app` application to search for `clinical documents`, `care guidelines`, and `plan policy documents`. The `clinical documents`, `care guidelines`, and `plan policy documents` are pre-indexed and accessible to the `ur_search_app` application.




### Components

The architecture contains the following components:

  * **Cloud Storage buckets**. UM application services require the following Cloud Storage buckets in your Google Cloud project:

    * `pa_forms_bkt`: A bucket to ingest the PA forms that need approval.
    * `training_forms`: A bucket to hold historical PA forms for training the DocAI form processors.
    * `eval_forms`: A bucket to hold PA forms for evaluating the accuracy of the DocAI form processors.
    * `tuning_dataset`: A bucket to hold the data required for tuning the large language model (LLM).
    * `eval_dataset`: A bucket to hold the data required for evaluation of the LLM.
    * `clinical_docs`: A bucket to hold the clinical documents that the providers submit as attachments to the PA forms or afterward to support the PA case. These documents get indexed by the search application in Agent Search service.
    * `um_policies`: A bucket to hold medical necessity and care guidelines, health plan policy documents, and coverage guidelines. These documents get indexed by the search application in the Agent Search service.
  * `form_processors`: These processors are trained to extract information from the `pa_forms` forms.

  * `pa_form_collection`: A Firestore datastore to store the extracted information as JSON documents in the NoSQL database collection.

  * `ingestion_service`: A microservice that reads the documents from the bucket, passes them to the DocAI endpoints for parsing, and stores the extracted data in Firestore database collection.

  * `hitl_app`: A microservice (web application) that fetches and displays data values extracted from the `pa_forms`. It also renders the confidence score reported by form processors (ML models) to the PA case manager so that they can review, correct, and save the information in the datastore.

  * `ur_app`: A microservice (web application) that UR specialists can use to review the PA requests using Generative AI. It uses the model named `prompt_model` to generate a prompt. The microservice passes the data extracted from the `pa_forms` forms to the `prompt_model` model to generate a prompt. It then passes the generated prompt to `ur_model` model to get the recommendation for a case.

  * Agent Platform medically-tuned LLMs: Agent Platform has a variety of [generative AI foundation models](https://cloud.google.com/discover/what-are-foundation-models) that can be tuned to reduce cost and latency. The models used in this architecture are as follows:

    * `prompt_model`: An adapter on the LLM tuned to generate prompts based on the data extracted from the `pa_forms`.
    * `ur_model`: An adapter on the LLM tuned to generate a draft recommendation based on the input prompt.
  * `ur_search_app`: A search application built with Agent Search to find personalized and relevant information to UR specialists from clinical documents, UM policies, and coverage guidelines.




## Products used

This reference architecture uses the following Google Cloud products:

  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Agent Search](https://cloud.google.com/enterprise-search): A platform that lets you create and deploy enterprise-grade AI-powered agents and applications. 
  * [ Document AI](https://cloud.google.com/document-ai): A document processing platform that takes unstructured data from documents and transforms it into structured data. 
  * [ Firestore](https://cloud.google.com/firestore): A NoSQL document database built for automatic scaling, high performance, and ease of application development. 
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Cloud Logging](https://cloud.google.com/logging): A real-time log management system with storage, search, analysis, and alerting.
  * [ Cloud Monitoring](https://cloud.google.com/monitoring): A service that provides visibility into the performance, availability, and health of your applications and infrastructure. 



## Use case

UM is a process used by health insurance companies primarily in the United States, but similar processes (with a few modifications) are used globally in the healthcare insurance market. The goal of UM is to help to ensure that patients receive the appropriate care in the correct setting, at the optimum time, and at the lowest possible cost. UM also helps to ensure that medical care is effective, efficient, and in line with evidence-based standards of care. PA is a UM tool that requires approval from the insurance company before a patient receives medical care.

The UM process that many companies use is a barrier to providing and receiving timely care. It's costly, time-consuming, and overly administrative. It's also complex, manual, and slow. This process significantly impacts the ability of the health plan to effectively manage the quality of care, and improve the provider and member experience. However, if these companies were to modify their UM process, they could help ensure that patients receive high-quality, cost-effective treatment. By optimizing their UR process, health plans can reduce costs and denials through expedited processing of PA requests, which in turn can improve patient and provider experience. This approach helps to reduce the administrative burden on healthcare providers.

When health plans receive requests for PA, the PA case managers create cases in the case management system to track, manage and process the requests. A significant amount of these requests are received by fax and mail, with attached clinical documents. However, the information in these forms and documents is not easily accessible to health insurance companies for data analytics and business intelligence. The current process of manually entering information from these documents into the case management systems is inefficient and time-consuming and can lead to errors.

By automating the data ingestion process, health plans can reduce costs, data entry errors, and administrative burden on the staff. Extracting valuable information from the clinical forms and documents enables health insurance companies to expedite the UR process.

## Design considerations

This section provides guidance to help you use this reference architecture to develop one or more architectures that help you to meet your specific requirements for security, reliability, operational efficiency, cost, and performance.

### Security, privacy, and compliance

This section describes the factors that you should consider when you use this reference architecture to help design and build an architecture in Google Cloud which helps you to meet your security, privacy, and compliance requirements.

In the United States, the Health Insurance Portability and Accountability Act (known as HIPAA, as amended, including by the Health Information Technology for Economic and Clinical Health — HITECH — Act) demands compliance with HIPAA's [Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html?language=es), [Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html?language=es), and [Breach Notification Rule](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html?language=es). [Google Cloud supports HIPAA compliance](https://cloud.google.com/security/compliance/hipaa), but ultimately, you are responsible for evaluating your own HIPAA compliance. Complying with HIPAA is a shared responsibility between you and Google. If your organization is subject to HIPAA and you want to use any Google Cloud products in connection with Protected Health Information (PHI), you must review and accept Google's Business Associate Agreement (BAA). The Google products covered under the BAA meet the requirements under HIPAA and align with our [ISO/IEC 27001, 27017, and 27018 certifications](https://www.iso.org/standard/iso-iec-27000-family) and [SOC 2 report](https://cloud.google.com/security/compliance/soc-2).

Not all LLMs hosted in the Model Garden support HIPAA. Evaluate and use the LLMs that support HIPAA.

To assess how Google's products can meet your HIPAA compliance needs, you can reference the third party audit reports in the [Compliance resource center](https://cloud.google.com/compliance).

We recommend that customers consider the following when selecting AI use cases, and design with these considerations in mind:

  * [Data privacy](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-unveils-ai-and-ml-privacy-commitment): The Google Cloud Agent Platform platform and Document AI don't utilize customer data, data usage, content, or documents for improving or training the [foundation models](https://docs.cloud.google.com/model-garden#:%7E:text=First%2Dparty%20models-,Foundation%20models,-Leverage%20state%2Dof). You can [tune the foundation models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning) with your data and documents within your secured tenant on Google Cloud.
  * Firestore server client libraries use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/permissions-reference) to manage access to your database. To learn about Firebase's security and privacy information, see [Privacy and Security in Firebase](https://firebase.google.com/support/privacy).
  * To help you store sensitive data,`ingestion_service`, `hitl_app`, and `ur_app` service images can be encrypted using [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/run/docs/securing/using-cmek) or integrated with [Secret Manager](https://docs.cloud.google.com/secret-manager/docs).
  * [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/shared-responsibility) implements Google Cloud security controls to help secure your models and training data. Some security controls aren't supported by the generative AI features in Agent Platform. For more information, see [Security controls for machine learning services](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-controls) and [Security Controls for Generative AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls).
  * We recommend that you use IAM to implement the principles of least-privilege and separation-of-duties with cloud resources. This control can limit access at the project, folder, or dataset levels.
  * Cloud Storage automatically stores data in an encrypted state. To learn more about additional methods to encrypt data, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).



Google's products follow [Responsible AI principles](https://ai.google/responsibility/principles/).

For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

### Reliability

This section describes design factors that you should consider to build and operate reliable infrastructure to automate PA request processing.

Document AI `form_processors` is a regional service. Data is stored synchronously across multiple zones within a region. Traffic is automatically load-balanced across the zones. If a zone outage occurs, data isn't lost1. If a region outage occurs, the service is unavailable until Google resolves the outage.

You can create Cloud Storage buckets in one of three [locations](https://docs.cloud.google.com/storage/docs/locations): regional, dual-region, or multi-region, using `pa_forms_bkt`, `training_forms`, `eval_forms`, `tuning_dataset`, `eval_dataset`, `clinical_docs` or `um_policies` buckets. Data stored in regional buckets is replicated synchronously across multiple zones within a region. For higher availability, you can use dual-region or multi-region buckets, where data is replicated asynchronously across regions.

In [Firestore](https://firebase.google.com/docs/database/rtdb-vs-firestore#reliability_and_performance), the information extracted from the `pa_form_collection` database can sit across multiple data centers to help to ensure global scalability and reliability.

The Cloud Run services, `ingestion_service`,`hitl_app`, and `ur_app`, are regional services. Data is stored synchronously across multiple zones within a region. Traffic is automatically load-balanced across the zones. If a zone outage occurs, Cloud Run jobs continue to run and data isn't lost. If a region outage occurs, the Cloud Run jobs stop running until Google resolves the outage. Individual Cloud Run jobs or tasks might fail. To handle such failures, you can use [task retries](https://docs.cloud.google.com/run/docs/configuring/max-retries) and checkpointing. For more information, see [Jobs retries and checkpoints best practices](https://docs.cloud.google.com/run/docs/jobs-retries). [Cloud Run general development tips](https://docs.cloud.google.com/run/docs/tips/general) describes some best practices for using Cloud Run.

Agent Platform is a comprehensive and user-friendly machine learning platform that provides a unified environment for the machine learning lifecycle, from data preparation to model deployment and monitoring.

For reliability principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

### Cost optimization

This section provides guidance to optimize the cost of creating and running an architecture to automate PA request processing and improve your UR processes. Carefully managing resource usage and selecting appropriate service tiers can significantly impact the overall cost.

[**Cloud Storage storage classes**](https://cloud.google.com/storage/pricing): Use the different storage classes (Standard, Nearline, Coldline, or Archive) based on the data access frequency. Nearline, Coldline, and Archive are more cost-effective for less frequently accessed data.

**Cloud Storage lifecycle policies** : Implement lifecycle policies to automatically transition objects to lower-cost storage classes or delete them based on age and access patterns.

[**Document AI**](https://cloud.google.com/document-ai/pricing) is priced based on the number of processors deployed and based on the number of pages processed by the Document AI processors. Consider the following:

  * **Processor optimization** : Analyze workload patterns to determine the optimal number of Document AI processors to deploy. Avoid overprovisioning resources.
  * **Page volume management** : Pre-processes documents to remove unnecessary pages or optimize resolution can help to reduce processing costs.



[**Firestore**](https://firebase.google.com/docs/firestore/pricing) is priced based on activity related to documents, index entries, storage that the database uses, and the amount of network bandwidth. Consider the following:

  * **Data modeling** : Design your data model to minimize the number of index entries and optimize query patterns for efficiency.
  * **Network bandwidth** : Monitor and optimize network usage to avoid excess charges. Consider caching frequently accessed data.



[**Cloud Run**](https://cloud.google.com/run/pricing) charges are calculated based on on-demand CPU usage, memory, and number of requests. Think carefully about resource allocation. Allocate CPU and memory resources based on workload characteristics. Use autoscaling to adjust resources dynamically based on demand.

[**Agent Platform**](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing) LLMs are typically charged based on the input and output of the text or media. Input and output token counts directly affect LLM costs. Optimize prompts and response generation for efficiency.

[**Agent Search**](https://cloud.google.com/generative-ai-app-builder/pricing#enterprise_pricing) search engine charges depend on the features that you use. To help manage your costs, you can choose from the following three options:

  * Search Standard Edition, which offers unstructured search capabilities.
  * Search Enterprise Edition, which offers unstructured search and website search capabilities.
  * Search LLM Add-On, which offers summarization and multi-turn search capabilities.



You can also consider the following additional considerations to help optimize costs:

  * **Monitoring and alerts** : Set up Cloud Monitoring and billing alerts to track costs and receive notifications when usage exceeds the thresholds.
  * **Cost reports** : Regularly review cost reports in the Google Cloud console to identify trends and optimize resource usage.
  * **Consider committed use discounts** : If you have predictable workloads, consider committing to using those resources for a specified period to get discounted pricing.



Carefully considering these factors and implementing the recommended strategies can help you to effectively manage and optimize the cost of running your PA and UR automation architecture on Google Cloud.

For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

## Deployment

The reference implementation code for this architecture is available under open-source licensing. The architecture that this code implements is a prototype, and might not include all the features and hardening that you need for a production deployment. To implement and expand this reference architecture to more closely meet your requirements, we recommend that you contact [Google Cloud Consulting](https://cloud.google.com/consulting).

The starter code for this reference architecture is available in the following git repositories:

  * [CDA git repository](https://github.com/hcls-solutions/claims-data-activator/blob/main/README.md): This repository contains Terraform deployment scripts for infrastructure provisioning and deployment of application code.
  * [UR service git repository](https://github.com/hcls-solutions/ur-service): This repository contains code samples for the UR service.



You can choose one of the following two options for to implement support and services for this reference architecture:

  * Engage [Google Cloud Consulting](https://cloud.google.com/consulting).
  * Engage a [partner who has built a packaged offering](https://www.productiveedge.com/solutions/nexauth-ai-powered-prior-authorization-platform) by using the products and solution components described in this architecture.



## What's next

  * [RAG infrastructure for generative AI using Agent Platform and Vector Search](https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search)
  * [RAG infrastructure for generative AI using Agent Platform and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai)
  * [RAG infrastructure for generative AI using GKE and Cloud SQL](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-gke)
  * [RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform](https://docs.cloud.google.com/architecture/rag-genai-agentspace-vertexai)
  * [GraphRAG infrastructure for generative AI using Agent Platform and Spanner Graph](https://docs.cloud.google.com/architecture/gen-ai-graphrag-spanner)
  * [Google Cloud options for grounding generative AI responses](https://docs.cloud.google.com/docs/ai-ml/generative-ai#grounding)
  * [Optimize Python applications for Cloud Run](https://docs.cloud.google.com/run/docs/tips/python)
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Dharmesh Patel](https://www.linkedin.com/in/pateldharmesh) | Industry Solutions Architect, Healthcare

Other contributors: 

  * [Ben Swenka](https://www.linkedin.com/in/bswenka) | Key Enterprise Architect
  * [Emily Qiao](https://www.linkedin.com/in/emily-qiao) | AI/ML Customer Engineer
  * [Luis Urena](https://www.linkedin.com/in/urena-luis) | Developer Relations Engineer
  * [Praney Mittal](https://www.linkedin.com/in/praney) | Group Product Manager
  * [Lakshmanan Sethu](https://www.linkedin.com/in/lakshmanansethu) | Technical Account Manager



* * *

  1. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). ↩




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-19 UTC."],[],[]] 
