---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/overview/
title: Solutions overview for GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:19:46.661574+00:00
---

# Solutions overview for GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Solutions overview for GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

The Google Distributed Cloud (GDC) air-gapped solutions guides bridge the gap between out-of-the-box product capabilities and production-ready enterprise architectures. These guides equip platform administrators and application operators with conceptual frameworks, reference architectures, and practical implementation steps to run critical workloads in GDC air-gapped environments.

The solutions guides adhere to strict requirements for performance, security, and data sovereignty.

## Document types

Solutions are documented across three complementary document types:

  * **Reference architectures** : Architectural blueprints that outline design principles, system topology, component interactions, and security controls for deploying a solution.
  * **Reference implementations** : Step-by-step guides for installing, configuring, and verifying the infrastructure, dependencies, and software deployment on GDC clusters.
  * **User guides** : Day-2 operational guides covering practical administration, service configuration, monitoring, scaling, and ongoing maintenance.



## Available solutions

The following sections list the available solution guides for GDC air-gapped, organized by technical domain matching the Google Cloud Architecture Center.

### AI and machine learning

  * **AI Gateway**
    * [Reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/reference-architecture): Centralized routing, protocol mediation, and traffic management for large language models (LLMs).
    * **Envoy**
      * [Reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/envoy/reference-implementation): Deploy Envoy Gateway and Envoy Agent Router on a standard cluster.
      * [Body-based routing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/ai-gateway/envoy/body-based-routing): Configure request payload inspection and content-based model routing.
  * **Elastic Stack**
    * [Reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/elasticstackgdcagarchitecture): Architecture for deploying the Elastic Stack and integrating it with an LLM service to enable Elastic's generative AI features.
    * [Reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/elasticstackgdcagimpl): Deploy the Elastic Stack and integrate it with an LLM service to evaluate Elastic's generative AI features.
  * **Open weight models**
    * [Reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/reference-architecture): Architecture for deploying and serving open weight large language models.
    * **Ollama**
      * [Reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/ollama/reference-implementation): Deploy Ollama to serve open weight models on standard clusters.
      * [Gemma models](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/ollama/gemma): Serve Gemma 4 models using Ollama; select the model and the GPU option in one guide.
    * **vLLM**
      * [Reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/vllm/reference-implementation): Deploy vLLM to serve high-throughput model inference on standard clusters with GPUs.
      * [Gemma models](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/vllm/gemma): Serve Gemma 4 models using vLLM; select the model and the GPU option in one guide.
      * [Mistral models](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/vllm/mistral): Serve Mistral 7B, Mistral NeMo 12B, Mistral Small 3.2 24B, Ministral 8B, Mixtral 8x7B, or Magistral Small 1.2 using vLLM; select the model and the GPU option in one guide.
    * [Open WebUI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/open-webui): Deploy and configure Open WebUI to interact with models served by Ollama and vLLM.



### Databases

  * **Self-managed MySQL databases**
    * [Reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/SelfManagedMySQLArchitecture): Design patterns for enterprise MySQL database topologies.
    * [Reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/SelfManagedMySQLImplementation): Deploy MySQL with replication and persistent volume management.
  * **Self-managed Oracle databases**
    * [Reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/db-self-managed-oracle-ref-arc): Architectural blueprints for migrating Oracle databases to virtual machines.
    * [Deploy self-managed Oracle databases](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/db-deploy-self-managed-oracle): Deploy single-instance Oracle databases on compute virtual machines.
    * [Deploy highly-available self-managed Oracle databases](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/db-deploy-ha-self-managed-oracle): Configure Oracle Data Guard for disaster recovery and high availability.
  * **Self-managed PostgreSQL databases**
    * [Reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/postgres-db-architecture): Architecture for scalable PostgreSQL database clusters.
    * [Reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/postgres-db-implementation): Deploy and configure PostgreSQL with automated backups and replication.



### Networking

  * **Self-managed Layer 7 load balancing**
    * [Reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-architecture): Architecture for application ingress routing and TLS termination.
    * [HAProxy reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-haproxy-impl): Deploy and tune HAProxy for high-throughput Layer 7 traffic routing.
    * [NGINX reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/l7-lb-nginx-impl): Deploy and configure NGINX reverse proxy services.



### Security and IAM

  * **Keyfactor EJBCA**
    * [Reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/keyfactor-ejbca-architecture): Public key infrastructure (PKI) and certificate authority architecture.
    * [Reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/keyfactor-ejbca-implementation): Deploy Keyfactor EJBCA for enterprise certificate lifecycle management.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
