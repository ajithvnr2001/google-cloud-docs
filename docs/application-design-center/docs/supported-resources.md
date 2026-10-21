---
url: https://docs.cloud.google.com/application-design-center/docs/supported-resources/
title: Supported resources for templates and applications \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:31.144711+00:00
---

# Supported resources for templates and applications  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/supported-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Supported resources for templates and applications Stay organized with collections  Save and categorize content based on your preferences. 

Application templates can include the following components:

  * Components designed by Google, incorporating Google Cloud best practices and default security configurations.
  * Your own [components that you import](https://docs.cloud.google.com/application-design-center/docs/import-components), based on your own Terraform modules.



The following components are designed by Google, and are included by default in Application Design Center:

Component category | Google Cloud product | Details | [Launch stage](https://cloud.google.com/products#product-launch-stages) | Configuration documentation  
---|---|---|---|---  
**Assets** | Authorization Extension | Service extensions for custom authorization logic. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-network-security-authz/tree/main/modules/authz-extension)  
Authorization Policy | Custom authorization policies for network services. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-network-security-authz/tree/main/modules/authz-policy)  
Authorization Policy Extension | Integrated authorization policy and extension. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-network-security-authz/tree/main/modules/policy-authz-extension)  
Compute Address | Reserve static internal or external IP address. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-address)  
Firebase AI Logic Prompt Template | Manage and deploy prompt templates centrally for Firebase AI Logic applications to maintain consistency. | General Availability | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-firebase/tree/main/modules/firebase_ai_logic_prompt_template)  
Firebase Multi-Platform App | Provisions a unified Firebase project along with registered application clients for Apple (iOS), Android, and web platforms. | General Availability | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-firebase/tree/main/modules/firebase_multi_platform_application)  
Routes | VPC network routes for traffic control. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-network/tree/main/modules/routes)  
Service Account | A service account is a special kind of account typically used by an application or compute workload, such as a Compute Engine instance, rather than a person. A service account is identified by its email address, which is unique to the account. | General Availability | [Configure a service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account)  
Agent Registry Agent | Data resource for agent for discovery and governance of AI agents. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-agent-registry/tree/main/modules/agent-registry-agent)  
Agent Registry Binding | A binding for Agent Registry and IAM connector. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-agent-registry/tree/main/modules/agent-registry-binding)  
Agent Registry Endpoint | Data resource for endpoint for discovery and governance of AI agents. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-agent-registry/tree/main/modules/agent-registry-endpoint)  
Agent Registry MCP Server | Data resource for MCP server for discovery and governance of AI agents. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-agent-registry/tree/main/modules/agent-registry-mcp-server)  
CA Service | Managed private certificate authorities for workload identities. | General Availability | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-certificate-authority-service)  
Compute Engine (Instance Template) | An instance template lets you describe a VM instance. You can then create groups of identical instances based on the template. | General Availability | [Configure a Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance)  
Firestore Security Rules | Deploy and manage robust security rules to establish strict access control and data validation for your database. | General Availability | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-firebase/tree/main/modules/firestore_rules)  
GKE Node Pool | A group of nodes within a cluster that have identical configuration and are updated at the same time. | General Availability | [Configure a GKE node pool](https://docs.cloud.google.com/application-design-center/docs/configure-gke-node-pool)  
IAM Connector | Managed identity and access connectors. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-iam-connectors-service)  
IAP Agent Registry Agent (IAM Binding) | Manages IAM policies for IAP-protected Agent Registry Agents. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-iap-policy/tree/main/modules/iap-agent-registry-agent-iam-binding)  
IAP Agent Registry Endpoint (IAM Binding) | Manages IAM policies for IAP-protected Agent Registry Endpoints. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-iap-policy/tree/main/modules/iap-agent-registry-endpoint-iam-binding)  
IAP Agent Registry MCP Server (IAM Binding) | Manages IAM policies for IAP-protected Agent Registry MCP Servers. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-iap-policy/tree/main/modules/iap-agent-registry-mcp-server-iam-binding)  
Model Armor Floor Setting | Base security policy for AI screening. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-vertex-ai/tree/main/modules/model-armor-floorsetting)  
Model Armor Template | Safety filters for AI prompts and responses. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-vertex-ai/tree/main/modules/model-armor-template)  
Secret Manager | A secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. | General Availability | [Configure a Secret Manager secret](https://docs.cloud.google.com/application-design-center/docs/configure-secret-manager)  
VPC Network | Virtual network for Google Cloud resources. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-network)  
**Services** | Cloud Workflows | Managed standalone workflows. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-cloud-workflows/tree/main/modules/simple_workflow)  
Firebase AI Logic | Execute large language models using Firebase Vertex AI, governed by the security of Firebase App Check. | General Availability | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-firebase/tree/main/modules/firebase_ai_logic_core)  
Firebase App Check | Protects your backend APIs from abuse, such as billing fraud and phishing, by attesting that traffic originates from your genuine app. | General Availability | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-firebase/tree/main/modules/firebase_app_check)  
Firebase Authentication | Backend services, easy-to-use SDKs, and ready-made UI libraries to securely authenticate users to your application. | General Availability | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-firebase/tree/main/modules/firebase_auth)  
Compute Firewall | VPC firewall rules for a project and a network. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-network/tree/main/modules/firewall-rules)  
Global Cloud Load Balancing (Backend) | Create a backend service for incoming traffic. | General Availability | [Configure a global Cloud Load Balancing backend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-backend)  
Global Cloud Load Balancing (Frontend) | Configure the load balancer frontend IP address, port, and protocol. Configure an SSL certificate if using HTTPS. | General Availability | [Configure a global Cloud Load Balancing frontend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-frontend)  
Cloud KMS | Managed encryption keys. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-kms)  
Internal Load Balancer | Regional internal load balancer for TCP/UDP traffic. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-lb-internal)  
Private Service Connect Endpoint | Regional address and forwarding rule to target a producer service attachment. | General Availability | [GitHub README](https://github.com/terraform-google-modules/terraform-google-network/tree/main/modules/private-service-connect-endpoints-for-published-services)  
Private Service Connect Producer | NAT subnets and a service attachment. | General Availability | [GitHub README](https://github.com/terraform-google-modules/terraform-google-network/tree/main/modules/private-service-connect-producer)  
Regional Cloud Load Balancing (Backend) | Create a backend service for incoming traffic. | General Availability | [Configure a regional Cloud Load Balancing backend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-backend)  
Regional Cloud Load Balancing (Frontend) | Configure the load balancer frontend IP address, port, and protocol. Configure an SSL certificate if using HTTPS. | General Availability | [Configure a regional Cloud Load Balancing frontend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-frontend)  
Agent Gateway | Central governance layer for AI agents. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-agent-gateway)  
Agent Registry Service | Registry for discovery and governance of AI agents. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-agent-registry/tree/main/modules/agent-registry-service)  
AlloyDB for PostgreSQL | A fully managed PostgreSQL-compatible database for your most demanding enterprise database workloads. | General Availability | [Configure an AlloyDB for PostgreSQL cluster](https://docs.cloud.google.com/application-design-center/docs/configure-alloydb)  
Artifact Registry | A universal package manager for all your build artifacts and dependencies. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-artifact-registry)  
BigQuery | A fully managed, petabyte-scale, and cost-effective analytics data warehouse that lets you run analytics over vast amounts of data in near real time. | General Availability | [Configure a BigQuery dataset](https://docs.cloud.google.com/application-design-center/docs/configure-bigquery)  
Bigtable | A NoSQL database service that offers extremely fast reads and writes, and is ideal for applications that require low-latency and high-throughput access to petabyte-scale data. | General Availability | [Configure a Bigtable instance](https://docs.cloud.google.com/application-design-center/docs/configure-bigtable)  
Cloud Run functions | Standalone functions on Cloud Run. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions)  
Cloud Run | A fully managed serverless compute platform that lets you deploy and run containerized applications and jobs. It abstracts away all infrastructure management, automatically scaling your services from zero to handle sudden traffic surges so you can focus on building great applications. | General Availability | [Configure a Cloud Run service](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run)  
Cloud Tasks | Regional service for managing distributed task execution. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-cloud-tasks)  
Managed Airflow | Managed workflow orchestration service. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-cloud-composer/tree/main/modules/google-composer-environment)  
Cloud DNS Managed Zone | Reliable, resilient, low-latency DNS serving. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-cloud-dns)  
Cloud DNS Response Policy | Response Policy for DNS. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-cloud-dns/tree/main/modules/dns_response_policy)  
Managed Service for Apache Spark Cluster | Google Cloud Dataproc lets you provision Apache Hadoop clusters and connect to underlying analytic data stores. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-dataproc)  
Document AI | Extract data from your documents using generative AI. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-document-ai)  
Firestore | A highly scalable and serverless NoSQL document database for building managed mobile and web applications with multi-region replication and high availability. | General Availability | [Configure a Firestore database](https://docs.cloud.google.com/application-design-center/docs/configure-firestore)  
GKE Autopilot Cluster | A managed Kubernetes cluster that automatically manages the underlying compute, networking, and storage infrastructure for your applications. | General Availability | [Configure a GKE Autopilot cluster](https://docs.cloud.google.com/application-design-center/docs/configure-gke-autopilot-cluster)  
GKE Standard Cluster | A Kubernetes cluster that you can use to run containerized applications. | General Availability | [Configure a GKE Standard cluster](https://docs.cloud.google.com/application-design-center/docs/configure-gke-standard-cluster)  
Memorystore for Redis | A highly scalable, available, and secure Redis service without the burden of managing complex Redis deployments. | General Availability | [Configure a Memorystore for Redis instance](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis)  
Memorystore for Redis Cluster | A highly scalable, available, secure Redis cluster without the burden of managing complex Redis deployments. Ideal for applications requiring extreme performance with large datasets that need horizontal scaling and high availability through data replication. | General Availability | [Configure a Memorystore for Redis Cluster](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis-cluster)  
Memorystore for Valkey | A fully managed Valkey service for Google Cloud that supports both Cluster Mode Enabled and Cluster Mode Disabled instances. Applications running on Google Cloud can achieve extreme performance by leveraging the highly scalable, available, and secure Valkey service without the burden of managing complex Valkey deployments. | General Availability | [Configure a Memorystore for Valkey instance](https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-valkey)  
Cloud NAT | Managed, software-defined network address translation. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-cloud-nat)  
Pub/Sub | Create a topic and add subscriptions. | General Availability | [Configure a Pub/Sub topic](https://docs.cloud.google.com/application-design-center/docs/configure-pubsub)  
Cloud Router | Distributed and managed offering for Border Gateway Protocol capabilities. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-cloud-router)  
Cloud Router Interface | Manages interfaces and Border Gateway Protocol peering for routers. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-cloud-router/tree/main/modules/interface)  
Spanner | A fully managed, relational database service that helps you build and manage relational databases for your applications. | General Availability | [Configure a Spanner database](https://docs.cloud.google.com/application-design-center/docs/configure-spanner)  
Cloud SQL (MySQL) | A fully managed database service that helps you set up, maintain, manage, and administer your MySQL relational databases. | General Availability | [Configure a Cloud SQL for MySQL instance](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-mysql)  
Cloud SQL (PostgreSQL) | A fully managed database service that helps you set up, maintain, manage, and administer your PostgreSQL relational databases. | General Availability | [Configure a Cloud SQL for PostgreSQL instance](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-postgresql)  
Cloud Storage | Worldwide storage and retrieval of any amount of data at any time. | General Availability | [Configure a Cloud Storage bucket](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-storage)  
Secure Web Proxy | Secure egress web traffic with granular policies. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-secure-web-proxy)  
Vertex AI | A machine learning (ML) platform that lets you train and deploy ML models and AI applications. | General Availability | [Configure a Vertex AI model](https://docs.cloud.google.com/application-design-center/docs/configure-vertex-ai)  
**Workloads** | Compute Instance | Create Compute Engine VMs. | Preview | [GitHub README](https://github.com/terraform-google-modules/terraform-google-vm/tree/main/modules/compute_instance)  
Cloud Run Job | A containerized application that runs a specific, non-HTTP task and then exits. It's ideal for things like scheduled batch processing, data transformations, or any other work that doesn't need to be constantly running and serving requests. | General Availability | [Configure a Cloud Run job](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run-job)  
Compute Engine (Managed Instance Group) | Collections of VM instances that use load balancing and automated services, like autoscaling and autohealing. | General Availability | [Configure a Compute Engine MIG](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-mig)  
Cloud Scheduler | Regional service for running scheduled jobs. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-cloud-scheduler)  
Agent Platform Runtime | Platform to deploy, manage, and scale AI agents. | Preview | [GitHub README](https://github.com/GoogleCloudPlatform/terraform-google-vertex-ai/tree/main/modules/agent-engine)  
  
## What's next

  * Enable required APIs and create an initial space by [setting up Application Design Center](https://docs.cloud.google.com/application-design-center/docs/setup).
  * Use your own Terraform modules in your template designs by [importing components](https://docs.cloud.google.com/application-design-center/docs/import-components).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
