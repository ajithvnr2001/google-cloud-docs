---
url: https://docs.cloud.google.com/application-design-center/docs/single-region-gke/
title: Single region GKE cluster and workload \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:32.567311+00:00
---

# Single region GKE cluster and workload  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/single-region-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Single region GKE cluster and workload Stay organized with collections  Save and categorize content based on your preferences. 

Create a cost-efficient Google Kubernetes Engine (GKE) cluster and workload optimized for resource management in a single location. This guide describes the following templates, which you can use to deploy a basic web application:

  * **Single region GKE cluster template** : create the foundational infrastructure required for a single region application. This template sets up a secure, private GKE cluster optimized for resource management.

  * **Single region GKE workload** ([Preview](https://cloud.google.com/products#product-launch-stages)): deploy a helm chart that includes the configuration for a basic web application. The workload is configured to scale based on CPU load, and ensure application availability during voluntary disruptions.




For example, you might deploy the cluster and workload templates to address the following business needs:

Example | Business need | Implementation  
---|---|---  
Internal line-of-business application | An internal application requires strict data residency in a specific region, cost-effectiveness for predictable internal usage, and high reliability. | Use the single region deployment to ensure data locality. Use autoscaling to efficiently manage resources for internal user demand.  
Regional ecommerce backend | An ecommerce platform needs high availability in a specific region to ensure continuous service, scalability to handle traffic spikes during sales events, and robust security for customer transactions and data. | Create a multi-zonal cluster configuration provides regional high availability. Use the secure boot configuration to bolster the security posture for sensitive customer data.  
Regional data processing and analytics platform | A platform for processing and analyzing large datasets requires data locality for compliance and performance, cost-optimized compute for intermittent batch jobs, and secure access to data. | The single-region deployment ensures data remains within geographical boundaries. Scale resources for large processing tasks and idle periods.  
  
## Architecture

The following image shows the components and connections in the template:

![A cluster connected to a node pool in the design canvas](https://docs.cloud.google.com/static/application-design-center/images/gke-cluster-node-pool-template.png)

The following describes the component configurations in this template:

  * [GKE Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle): a cost-effective single-region cluster where your workload runs.

The following table describes the cluster configuration in this template:

Configuration | Purpose  
---|---  
`location` is set to `us-central1`. | Confines cluster resources to a single geographical area, ensuring data locality and minimizing cross-region data transfer costs and latency.  
`initial_node_count` is set to `1`. | Defines an initial node to create in the cluster's default node pool when the cluster is first provisioned. In regional clusters, this is the number of nodes per zone.  
`release_channel` is set to `{"channel":"REGULAR"}`. | Ensures that your GKE cluster receives stable and predictable updates, providing a balance between new features and reliability.  
`enable_intranode_visibility` is set to `true`. | Enables visibility for intranode traffic in VPC Flow Logs, which is required for network monitoring, troubleshooting, and security analysis.  
`control_plane_endpoints_config` is set to `{"dns_endpoint_config":{"allow_external_traffic":true}}`. | The GKE control plane is configured to be publicly accessible to let you manage the cluster outside your Virtual Private Cloud (VPC) network.  
  * [GKE node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools): a group of worker nodes that run the application's containers.

The following table describes the node pool configurations in this template:

Configuration | Purpose  
---|---  
`location` is set to `us-central1`. | Specifies the region where this node pool is created. Similar to the cluster's location, this ensures the node pool resources are in a single geographical area.  
`autoscaling` is set to `{"max_node_count":3, "min_node_count":1}`. | Configures the cluster autoscaler for this node pool. Ensures that the node pool always maintains at least one node, and sets the upper limit to three nodes to control costs and resource consumption.  
`node_config` is set to `{"machine_type":"e2-medium", "oauth_scopes":["https://www.googleapis.com/auth/cloud-platform"], "shielded_instance_config":{"enable_secure_boot":true}}`. | Groups configurations for the nodes within this pool. The machine type is a balance of CPU and memory suitable for general-purpose workloads. Defines the access granted to the service account. Enables Secure Boot for the Shielded VM instances, helping protect against boot-level malware.  



## Helm chart configuration

The following table lists the helm chart configurations, which have been customized for deploying and scaling a basic web application on GKE.

Configuration | Purpose  
---|---  
`replicaCount: 2` | Creates two initial replicas to establish an initial level of redundancy.  
`image.repository: gcr.io/google-samples/hello-app` | Uses a basic web server Docker image.  
`resources.requests: {"cpu": "100m", "memory": "128Mi"}` | Specifies the minimum amount of CPU and memory that are reserved for each pod, ensuring available resources and efficient scheduling.  
`hpa: {"enabled": true, "minReplicas": 2, "maxReplicas": 10, "targetCPUUtilizationPercentage": 60}` | Activates the Horizontal Pod Autoscaler to automatically adjust the number of pods between 2 and 10 based on CPU utilization, ensuring performance and cost efficiency.  
`service: {"type": "ClusterIP", "port": 80}` | Configures the service for internal access within the cluster on the standard HTTP port.  
`pdb: {"enabled": true, "minAvailable": 1}` | Enables a Pod Disruption Budget to ensure that at least one replica remains available during voluntary disruptions, maintaining high availability.  
  
## Create your web application

Use the _Single region GKE cluster and workload_ templates to deploy your web application.

### Deploy your web infrastructure

Configure and deploy the _Single region GKE cluster_ template to create the foundational infrastructure where your web workload runs.

  1. [Duplicate and deploy](https://docs.cloud.google.com/application-design-center/docs/build-on-google-templates#duplicate-and-customize) the _Single region GKE cluster_ template as an application.

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

Use the _Single region GKE workload_ template to deploy your web workload into the cluster you created. You'll deploy a helm chart that includes your web workload configuration.

  1. From the **Google catalog** page, on the **Single region GKE workload** template, click **Create new application**.

  2. In the **Name** field, enter a unique name for your application.

  3. In the **GKE Deployment Target** area, do the following:

     1. From the **Project list** , select the project where you deployed the GKE cluster from your _Single region GKE cluster_ application.

     2. From the **Region** list, select the region where you deployed the GKE cluster.

     3. From the **Clusters** list, select the deployed GKE cluster.

     4. From the **Namespace** list, enter the namespace where you deployed your GKE cluster. If you didn't change the name, enter `default`.

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
