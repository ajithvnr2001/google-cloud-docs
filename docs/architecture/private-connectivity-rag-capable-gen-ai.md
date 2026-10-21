---
url: https://docs.cloud.google.com/architecture/private-connectivity-rag-capable-gen-ai/
title: Private connectivity for RAG-capable generative AI applications \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:32.506230+00:00
---

# Private connectivity for RAG-capable generative AI applications  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/private-connectivity-rag-capable-gen-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Private connectivity for RAG-capable generative AI applications Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-12-12 UTC

This document provides a reference architecture that you can use to help secure the network infrastructure for [applications with retrieval-augmented generation (RAG)](https://docs.cloud.google.com/architecture/rag-reference-architectures). A RAG architecture typically contains separate subsystems to handle the data processing and content retrieval flows. This reference architecture demonstrates how to use Shared VPC to do the following:

  * Create separation between the subsystems by using Identity and Access Management (IAM) permissions.
  * Connect the application components by using private IP addresses.



The intended audience for this document includes architects, developers, and networking and security administrators. The document assumes that you have a basic understanding of networking. This document doesn't describe the creation of a RAG-based application.

## Architecture

The following diagram shows the networking architecture that this document presents:

![Networking architecture for applications with RAG.](https://docs.cloud.google.com/static/architecture/images/private-connectivity-rag-capable-gen-ai-apps.svg)![](https://docs.cloud.google.com/static/architecture/images/private-connectivity-rag-capable-gen-ai-apps.svg)

![Connections and traffic flow for the networking architecture.](https://docs.cloud.google.com/static/architecture/images/private-connectivity-connections-traffic.svg)

The architecture in the preceding diagram shows the following components:

Component | Purpose  
---|---  
External network, either on-premises or in another cloud | 

  * Provides network connectivity to data engineers who upload raw RAG data.
  * Terminates external network connectivity.
  * Hosts external routers.
  * Provides connectivity to the Private Service Connect endpoint in the Google Cloud routing Virtual Private Cloud (VPC) network.
  * Contains DNS servers that point to the Private Service Connect endpoint.

  
Routing project | 

  * Hosts the routing VPC network, which connects to the external network through a Cloud Interconnect or Cloud VPN connection.
  * Hosts a Network Connectivity Center (NCC) hub that connects the external network, routing VPC network, and Shared VPC networks together.
  * Hosts a Private Service Connect endpoint that connects to a regional Cloud Storage endpoint. This endpoint lets data engineers upload RAG data to the Cloud Storage bucket. 

  
RAG Shared VPC host project | Hosts a Shared VPC network that hosts the frontend service internal Application Load Balancer and any other services that need a VPC network. All service projects have access to that Shared VPC network.  
Data ingestion service project |  Contains a Cloud Storage bucket for raw data input. Contains the data ingestion subsystem, which includes the following components:

  * **Ingestion processing** : Reads raw data and processes it.
  * **Ingestion output** : Writes to the final datastore.

  
Serving service project |  Contains the serving subsystem, which includes the following components that provide the services and functions for inference and interaction:

  * RAG datastore that contains the output of the data ingestion subsystem.
  * Serving processes that feed the model by combining the inference query with data from the RAG datastore.
  * The model that the serving subsystem uses to create vectors from the uploaded RAG data and to process the end-user request.

  
Frontend service project |  Contains the serving subsystem, which is an Application Load Balancer in front of a user-interaction service that runs on Cloud Run or Google Kubernetes Engine (GKE). The project also contains Google Cloud Armor, which helps limit how your service is accessed. If you want to provide access from the internet, you can add a regional external Application Load Balancer.  
VPC Service Controls perimeter | Helps protect against data exfiltration. Data that's stored in Cloud Storage buckets can't be copied to anywhere outside of the perimeter, and control plane operations are protected.  
  
The following sections describe the connections and the traffic flows that are in the architecture.

### Connections between components

This section describes the connections between the components and networks in this architecture.

#### External network to routing VPC network

The external networks connect to the Google Cloud routing VPC network over Cloud Interconnect or Cloud VPN, which are hybrid spokes of an NCC hub.

Cloud Routers in the routing VPC network and the external routers in the external network exchange Border Gateway Protocol (BGP) routes:

  * Routers in external networks announce the routes for external subnets to the routing VPC Cloud Router. You can express the preference of the routes by using BGP metrics and attributes.
  * Cloud Routers in the routing VPC network advertise the routes for prefixes in Google Cloud's VPCs to the external networks.



#### Routing VPC network to Shared VPC network

You connect the routing VPC network and the RAG VPC network by using the NCC VPC spokes of the NCC hub. The hub also hosts the hybrid spokes to the external network.

#### Resource-to-resource within the Shared VPC network

In this design, a Cloud Storage bucket receives data from the external network. Inference requests come through a regional internal Application Load Balancer. For the rest of your system, you have the following options:

  * Host everything in Google SaaS infrastructure, such as Cloud Storage buckets, Gemini Enterprise Agent Platform, Cloud Run, and Pub/Sub. In this case, the components communicate over private Google infrastructure.
  * Host everything in workloads that run in Compute Engine VMs, GKE clusters, Cloud SQL databases, or other components that run in VPC networks. In this case, systems communicate by using private IP addresses across networks that you link through NCC or VPC Network Peering.
  * Use a mixture of fully-managed, platform, and infrastructure services. In this case, you can make connections between a VPC network and a fully managed service by using the following methods: 
    * **Private Google Access** : With this method, workloads that don't have external IP addresses and that run in VPC networks can access Google APIs. This access happens internally over Google infrastructure and this process doesn't expose such traffic to the internet.
    * **Private Service Connect** : With this method, you can create an endpoint in your service project for services like AlloyDB for PostgreSQL that are hosted in managed VPC networks.



#### External network to frontend service Application Load Balancer

The endpoint of the regional internal Application Load Balancer is an IP address in the RAG network. The RAG network, the routing network, and the hybrid connections to the external network are all spokes of the same NCC hub. Therefore, you can instruct NCC to export all of the spoke subranges to the hub, which then re-exports those subranges to the other spoke networks. End users of the system can then reach the load balanced service from the external network.

### Traffic flows

The traffic flows in this reference architecture include a RAG data flow and an inference flow.

#### RAG population flow

This flow describes how RAG data flows through the system from data engineers to vector storage.

  1. From the external network, data engineers upload raw data over the Cloud Interconnect connection or Cloud VPN connection. The data is uploaded to the Private Service Connect endpoint in the routing VPC network.
  2. The data travels over Google's internal infrastructure to the Cloud Storage bucket in the data ingestion service project.
  3. Within the data ingestion service project, data travels between systems by using one of the following methods:

     * Private Google Access
     * Private Service Connect endpoints
     * Direct Google infrastructure

The method depends on whether the systems are hosted in Google Cloud VPC networks or directly in Google Cloud. As part of this flow, the data ingestion subsystem feeds chunked RAG data to the model, which produces vectors for each chunk.

  4. The data ingestion subsystem writes the vector data and chunked data to the appropriate datastore.




#### Inference flow

This flow describes customer requests.

  1. From the external network, a customer sends a request to the IP address of the service.
  2. The request travels over the Cloud Interconnect connection or Cloud VPN connection to the routing VPC network.
  3. The request travels over the VPC spoke connection to the RAG VPC network.
  4. The customer request arrives at the Application Load Balancer, which passes the request to the frontend subsystem.
  5. The frontend subsystem forwards the request to the serving subsystem.
  6. The serving subsystem augments the request by using the relevant contextual data from the datastore.
  7. The serving subsystem sends the augmented prompt to the AI model, which generates a response.



## Products used

This reference architecture uses the following Google Cloud products:

  * [ Virtual Private Cloud (VPC)](https://cloud.google.com/vpc): A virtual system that provides global, scalable networking functionality for your Google Cloud workloads. VPC includes VPC Network Peering, Private Service Connect, private services access, and Shared VPC.
  * [ Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc): A feature of Virtual Private Cloud that lets you connect resources from multiple projects to a common VPC network by using internal IP addresses from that network.
  * [ Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect): A feature that lets consumers access managed services privately from inside their VPC network.
  * [ Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access): A feature that lets VM instances without external IP addresses reach the external IP addresses of Google APIs and services.
  * [ Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/overview): A service that extends your external network to the Google network through a high-availability, low-latency connection.
  * [ Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn): A service that securely extends your peer network to Google's network through an IPsec VPN tunnel.
  * [ Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview): A distributed and fully managed offering that provides Border Gateway Protocol (BGP) speaker and responder capabilities. Cloud Router works with Cloud Interconnect, Cloud VPN, and Router appliances to create dynamic routes in VPC networks based on BGP-received and custom learned routes.
  * [ Network Connectivity Center](https://cloud.google.com/network-connectivity-center): An orchestration framework that simplifies network connectivity among spoke resources that are connected to a central management resource called a _hub_. 
  * [ VPC Service Controls](https://cloud.google.com/security/vpc-service-controls): A managed networking functionality that minimizes data exfiltration risks for your Google Cloud resources.
  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing): A portfolio of high performance, scalable, global and regional load balancers. 
  * [ Model Armor](https://cloud.google.com/security/products/model-armor): A service that provides protection for your generative and agentic AI resources against prompt injection, sensitive data leaks, and harmful content.
  * [ Google Cloud Armor](https://cloud.google.com/security/products/armor): A network security service that offers web application firewall (WAF) rules and helps to protect against DDoS and application attacks. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.



## Use cases

This architecture is designed for enterprise scenarios where the input, output, and internal communications of the overall system must use private IP addresses and must not traverse the internet:

  * **Private input** : Uploaded data doesn't travel over the internet. Instead, you host your Cloud Storage bucket behind a Private Service Connect endpoint in your Google Cloud routing VPC network. You copy RAG data over your Cloud Interconnect or your Cloud VPN connection by using only private IP addresses.
  * **Private inter-service connectivity** : Services talk to each other over Google's internal interfaces or through private addresses that are internal to your VPC networks.
  * **Private output** : Inference results aren't reachable over the internet unless you choose to set up that access. By default, only users in the designated external network can reach the private endpoint of your service.



## Design alternatives

This section presents alternative network-design approaches that you can consider for your RAG-capable application in Google Cloud.

### Make the service available publicly

In the architecture that's shown in this document, only users in your internal network can send queries to your application. If your application must be accessible to clients on the internet, use a [regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https).

### Use GKE Inference Gateway

If your frontend subsystem runs on GKE, you can use an [Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) instead of an Application Load Balancer.

## Design considerations

This section provides additional guidance to help you deploy networking to support private connectivity for a RAG-capable architecture. This guidance can help you meet your specific requirements for security and compliance, reliability, cost, and performance. The guidance in this section isn't exhaustive. For your particular deployment, you might need to consider additional design factors that aren't covered in this section.

### Security, privacy, and compliance

In most cases, you deploy [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) in front of the AI model to evaluate both inbound prompts and outbound results. Model Armor helps prevent potential risks and helps ensure responsible AI practices.

In order to reject inappropriate requests before they get to the serving subsystem, you can [attach Model Armor to the Application Load Balancer](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services).

This architecture uses [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), which helps prevent unauthorized data exfiltration.

This design uses established security principles to help secure your RAG workloads. For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

### Cost optimization

For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

### Performance optimization

For performance optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization) in the Well-Architected Framework. 

## Deployment

This section describes the steps to create your application:

  1. Identify the region for workloads.
  2. Create Google Cloud projects and VPC networks.
  3. Connect your external networks to your routing VPC network.
  4. Link networks by using NCC.
  5. Identify components for RAG deployment and create service accounts.
  6. Configure VPC Service Controls.
  7. Build the data ingestion subsystem.
  8. Build the serving subsystem.
  9. Build the frontend subsystem.
  10. Make your application reachable from the internet.



### Identify the region for workloads

In general, you want to place connectivity, VPC subnets, and Google Cloud workloads in close proximity to your on-premises networks or other cloud clients. For more information about how to choose a region for your workloads, see [Google Cloud Region Picker](https://cloud.withgoogle.com/region-picker/) and [Best practices for Compute Engine regions selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection).

### Create Google Cloud projects and VPC networks

If your organization has set up [Cross-Cloud Network for distributed applications](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity) already, your routing project and routing VPC network should already exist.

Create the [Google Cloud projects](https://developers.google.com/workspace/guides/create-project) and a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) in the following order:

  1. Create the routing project.
  2. Create the routing VPC network with Private Google Access enabled.
  3. Create the RAG project.
  4. [Promote the RAG project to be a Shared VPC host project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#enable-shared-vpc-host).
  5. Create the data ingestion service project.
  6. Create the serving service project.
  7. Create the frontend service project.
  8. Create the Shared VPC RAG network with Private Google Access enabled.
  9. Give the service projects permission to use the RAG network.



### Connect your external networks to your routing VPC network

You can skip this step if you have already set up [Cross-Cloud Network for distributed applications](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity).

Set up the connectivity between the external networks and your routing network. To understand the relevant technologies, see [External and hybrid connectivity](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity#external-and-hybrid-connectivity). For guidance about how to choose a connectivity product, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

### Link networks by using NCC

  1. In the routing project, [create an NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-hub).
  2. Add the Cloud Interconnect connections as [VLAN attachment spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vlan-spoke), or add Cloud VPN connections as [VPN spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpn-spoke).
  3. Add the RAG VPC network and the routing VPC network to the hub as VPC spokes.



### Identify components for RAG deployment and create service accounts

  1. Choose a [RAG deployment](https://docs.cloud.google.com/architecture/rag-reference-architectures) and make a list of the components that it needs.
  2. Identify what access each component needs.
  3. For each component, [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with the appropriate permissions. In some cases, this means that you give a component permission to read from or write to a different service project.



This design assumes that you use a Cloud Storage bucket as your data input component and that you use a Application Load Balancer in your inference frontend. The rest of your design can vary as needed.

Ideally, each component runs as its own service account. Ensure that each component has only the minimum IAM permissions that are necessary to perform its required functions. For example, a Cloud Run job in the data ingestion subsystem needs to read from the input Cloud Storage bucket, but it doesn't need to write to the bucket. In this example, the service project that runs the Cloud Run job should have permission to only read from the bucket, with no write permission.

### Configure VPC Service Controls

  1. [Create a VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) around your deployment.
  2. [Configure access rules](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).



### Build the data ingestion subsystem

The data ingestion subsystem takes raw data from data engineers and processes it for use by the serving subsystem.

  1. In the data ingestion service project, [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  2. In the routing VPC network, [create a regional Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#create-regional-endpoint), and connect the endpoint to the bucket.
  3. In the external network, add a DNS entry for the endpoint by using the IP address and URL that were generated in the previous step.
  4. Update external network firewall rules to allow access to the endpoint IP address.
  5. In the data ingestion service project, build out the rest of your ingestion pipeline according to your chosen RAG architecture.
  6. Grant IAM permissions so that the relevant resource in the ingestion pipeline can access the model that produces the vectors.
  7. Grant IAM permissions so that the relevant resource in the ingestion pipeline can write to the vector datastore.



### Build the serving subsystem

  1. In the serving service project, build your serving pipeline.
  2. Grant IAM permissions so that the service account in the frontend system can access the output of the serving subsystem.



### Build the frontend subsystem

This section assumes that you use a regional internal Application Load Balancer that uses a serverless NEG in front of Cloud Run. However, you can use a different load balancer and backend.

  1. Create the code for your frontend system.
  2. In the frontend service project, [deploy your load-balanced frontend system](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless), which includes the optional step to configure a Cloud Armor security policy.
  3. Configure Cloud Router in the routing VPC network to [forward routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip#cloud-router) from the RAG VPC network to the on-premises routers. This configuration allows clients to reach the Application Load Balancer.
  4. In your external network, configure the firewall rules to make the load balancer frontend reachable from your external network.
  5. In your external network, update the DNS to point to the Application Load Balancer forwarding rule.



### Make your application reachable from the internet

This section is optional.

This design assumes that you want your service to be reachable from your external network only, but you can also make the service reachable from the internet.

To make the service reachable from the internet, complete the following steps:

  1. [Create a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless) that points to the same backend that the internal Application Load Balancer points to. Complete the optional step to configure a Cloud Armor security policy.
  2. [Update VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) to let service customers reach backend services.



## What's next

  * Learn about [Cross-Cloud Network for distributed applications](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design).
  * Learn how to [host AI apps and agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * Learn about [responsible AI best practices and Agent Platform safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai).
  * Learn about [prompting strategies for LLMs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * Deepak Michael | Networking Specialist Customer Engineer
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking



Other contributors: 

  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer
  * [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer
  * [Aspen Sherrill](https://www.linkedin.com/in/aspensherrill/) | Cloud Security Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
