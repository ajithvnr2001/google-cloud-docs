---
url: https://docs.cloud.google.com/application-design-center/docs/enterprise-grade-production-gke/
title: Enterprise-grade production GKE cluster and workload \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:55.867262+00:00
---

# Enterprise-grade production GKE cluster and workload  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/enterprise-grade-production-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Enterprise-grade production GKE cluster and workload Stay organized with collections  Save and categorize content based on your preferences. 

Create a high-security Google Kubernetes Engine (GKE) cluster and workload optimized for production. This guide describes the following templates, which you can use to deploy a production web application:

  * **Enterprise-grade production GKE cluster template** : create the foundational infrastructure required for a production application. This template sets up a secure, private GKE cluster optimized for integrity, advanced networking, and disaster recovery.

  * **Enterprise-grade production GKE workload** ([Preview](https://cloud.google.com/products#product-launch-stages)): deploy a helm chart that includes the configuration for a highly available stateless web application. The workload is configured to enhance security, reliability, and service continuity.




For example, you might deploy the cluster and workload templates to address the following business needs:

Example | Business need | Implementation  
---|---|---  
Global trading platform | A financial institution requires a low latency, globally distributed trading platform with maximum uptime, stringent security, and auditable compliance to handle high-frequency trades. | Use globally distributed, multi-regional clusters with advanced networking to ensure ultra-low latency and resilience. Implement strong network policies, private cluster configurations, and advanced security features for data protection and regulatory compliance.  
Multi-tenant SaaS platform | A software-as-a-service (SaaS) provider needs to host a highly scalable, secure, and cost-optimized platform for thousands of enterprise customers, requiring strict tenant isolation, dynamic resource allocation, and continuous delivery of new features without downtime. | Use multi-tenant clusters with robust namespace isolation, network segmentation, and quota management to ensure fair resource sharing and security between tenants.  
Real-time inference for critical operations | An organization needs to deploy AI/ML models for real-time inference in mission-critical fraud detection applications, demanding extremely low latency, high throughput, and the ability to rapidly adapt to new model versions with full auditability. | Configure clusters with specialized node pools for AI inference. Ensure low-latency network connectivity and enable efficient traffic routing to inference endpoints.  
  
## Architecture

The following image shows the components and connections in the template:

![A cluster connected to a node pool in the design canvas](https://docs.cloud.google.com/static/application-design-center/images/gke-cluster-node-pool-template.png)

The following describes the component configurations in this template:

  * [GKE Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle): a cluster where your workload runs.

The following table describes the cluster configuration in this template:

Configuration | Purpose  
---|---  
`location: us-central1` | Ensures data locality and compliance within a geographical boundary. A multi-zonal setup within the region provides high availability.  
`network: projects/PROJECT_ID/global/networks/enterprise-vpc` | Specifies a pre-existing VPC that is typically designed for network segmentation and connectivity.  
`subnetwork: projects/PROJECT_ID/regions/us-central1/subnetworks/gke-subnet` | Specifies a subnetwork for the cluster in the VPC that is typically designed with proper IP allocation and network isolation.  
`master_authorized_networks_config: [{"cidr_block": "10.0.0.0/8", "display_name": "Internal Network"}]` | Restricts access to the control plane endpoint to specific, trusted IP CIDR blocks. This prevents unauthorized access to cluster management APIs.  
`private_cluster_config.enable_private_endpoint: true` | Ensures that the control plane is only accessible using internal IP addresses within the VPC or authorized networks. This enhances security by removing public exposure.  
`private_cluster_config.enable_private_nodes: true` | Ensures all worker nodes have only private IP addresses, isolating them from the public internet and reducing the attack surface.  
`release_channel: STABLE` | Predictable and thoroughly tested updates maintain stability in a production environment.  
`network_policy.enabled: true` | Enables Kubernetes Network Policy, which provides control over pod-to-pod communication for enhanced security and micro-segmentation.  
`binary_authorization: true` | Enforces deployment policies, ensuring only trusted and signed container images can run on the cluster.  
`database_encryption: {"state": "ENCRYPTED_WITH_CMEK", "key_name": "projects/PROJECT_ID/locations/us-central1/keyRings/gke-keyring/cryptoKeys/gke-etcd-key"}` | Customer-Managed Encryption Keys (CMEK) encrypt the database, providing data security and meeting compliance requirements.  
`workload_identity_config: {"enabled": true}` | Allows Kubernetes service accounts to act as Google Cloud service accounts, enabling fine-grained, secure access to resources using IAM.  
`logging_config` and `monitoring_config` are set to `{"component_config": {"enable_components": ["SYSTEM_COMPONENTS", "WORKLOADS"]}}` | Integrates with Cloud Logging and Cloud Monitoring, ensuring comprehensive observability, auditing, and alerting for production workloads.  
`maintenance_policy: {"daily_maintenance_window": {"start_time": "03:00"}, "recurring_window": {"start_time": "00:00", "end_time": "04:00", "recurrence": "FREQ=WEEKLY;BYDAY=SAT,SUN"}}` | Maintenance windows control when GKE performs automatic upgrades, minimizing disruption to critical applications.  
`enable_shielded_nodes: true` | Shielded GKE Nodes provide security features like secure boot and integrity monitoring to protect against rootkits and boot-level malware.  
`gateway_api_config: {"channel": "CHANNEL_STANDARD"}` | Advanced traffic management for complex routing, load balancing, and API management in enterprise applications.  
`security_posture_config: {"mode": "ENTERPRISE", "vulnerability_mode": "VULNERABILITY_ENTERPRISE"}` | Advanced security posture management, including vulnerability scanning and policy enforcement.  
  * [GKE node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools): a group of worker nodes that run the application's containers.

The following table describes the node pool configurations in this template:

Configuration | Purpose  
---|---  
`location: us-central1`. | Specifies the region where this node pool is created. Similar to the cluster's location, this ensures the node pool resources are in a single geographical area.  
`autoscaling: {"max_node_count":3, "min_node_count":1}`. | Configures the cluster autoscaler for this node pool. Ensures that the node pool always maintains at least one node, and sets the upper limit to three nodes to control costs and resource consumption.  
`node_config: {"machine_type":"e2-medium", "oauth_scopes":["https://www.googleapis.com/auth/cloud-platform"], "shielded_instance_config":{"enable_secure_boot":true}}`. | Groups configurations for the nodes within this pool. The machine type is a balance of CPU and memory suitable for general-purpose workloads. Defines the access granted to the service account. Enables Secure Boot for the Shielded VM instances, helping protect against boot-level malware.  



## Helm chart configuration

The following table lists the helm chart configurations, which have been customized for deploying and scaling a basic web application on GKE.

Configuration | Purpose  
---|---  
`replicaCount: 3` | Creates three initial replicas to establish an initial level of redundancy and basic high availability for the application.  
`image.repository: gcr.io/google-samples/hello-app` | Uses a basic web server Docker image as a placeholder.  
`resources.requests: {"cpu": "100m", "memory": "128Mi"}` | Specifies the minimum amount of CPU and memory that are reserved for each pod, ensuring available resources and efficient scheduling.  
`resources.limits: {"cpu": "250m", "memory": "256Mi"}` | Specifies the maximum amount of CPU and memory that are reserved for each pod, preventing resource monopolization by a single pod.  
`networkPolicy.enabled: true` | Activates Kubernetes Network Policies for the application, which lets you define rules for how pods communicate with each other and other network endpoints, enforcing network segmentation and isolation.  
`service: {"type": "ClusterIP", "port": 80}` | Configures the service for internal access within the cluster on the standard HTTP port.  
`pdb: {"enabled": true, "minAvailable": 1}` | Enables a Pod Disruption Budget to ensure that at least one replica remains available during voluntary disruptions, maintaining high availability.  
  
## Create your web application

Use the _Enterprise-grade production GKE cluster and workload_ templates to deploy your web application.

### Deploy your web infrastructure

Configure and deploy the _Enterprise-grade production GKE cluster_ template to create the foundational infrastructure where your web workload runs.

  1. [Duplicate and deploy](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates#duplicate-and-customize) the _Enterprise-grade production GKE cluster_ template as an application.

A GKE cluster is created in the deployment project that you choose.

  2. Configure the components. For more information, see the following:

     * [Configure a GKE Standard cluster](https://docs.cloud.google.com/application-design-center/docs/configure-gke-standard-cluster).

     * [Configure a GKE node pool](https://docs.cloud.google.com/application-design-center/docs/configure-gke-node-pool).

  3. Click **Deploy**. The application deploys after several minutes.

  4. In the **Application details** panel, click the **Outputs** tab.

  5. Identify the **cluster_id** for your application. You'll use this information when you deploy your helm chart.




### Deploy your web workload

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use the _Enterprise-grade production GKE workload_ template to deploy your web workload into the cluster you created. You'll deploy a helm chart that includes your web workload configuration.

  1. From the **Google catalog** page, on the **Enterprise-grade production GKE workload** template, click **Create new application**.

  2. In the **Name** field, enter a unique name for your application.

  3. In the **GKE Deployment Target** area, do the following:

     1. From the **Project list** , select the project where you deployed the GKE cluster from your _Enterprise-grade production GKE cluster_ application.

     2. From the **Region** list, select the region where you deployed the GKE cluster.

     3. From the **Clusters** list, select the deployed GKE cluster.

     4. From the **Namespace** list, enter the namespace for your workload. If you didn't change the name, enter `default`.

     5. Click **Create application**.

The application is created and the configuration files are displayed.

  4. In the **Helm chart** panel, do the following:

     1. Review the configuration details.

     2. Optional: customize the configuration to meet your unique needs.

     3. To deploy the helm chart to your cluster, click **Deploy**.

For detailed steps, see [Deploy applications](https://docs.cloud.google.com/application-design-center/docs/deploy-applications).

After several minutes, the helm chart configuration deploys to your GKE cluster.




## What's next

  * To learn how to duplicate and customize templates, see [Quickstart: Customize and deploy a Google template](https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Identify general architectural best practices with the [Google Cloud Architecture Framework](https://docs.cloud.google.com/architecture/framework).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
