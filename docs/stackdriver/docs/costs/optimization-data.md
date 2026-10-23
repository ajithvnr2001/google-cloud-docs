---
url: https://docs.cloud.google.com/stackdriver/docs/costs/optimization-data/
title: About cost and utilization data \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:39.657908+00:00
---

# About cost and utilization data  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/costs/optimization-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  About cost and utilization data Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about the source of cost and optimization data in the Cost Explorer, how the data is categorized, and limitations on data availability.

## Cost data

  * **Source:** Cost data is based on the same information that powers your Cloud Billing reports and exports.
  * **Latency:** Google Cloud products report usage and cost data to Cloud Billing processes at varying intervals. You might see a delay between your use of Google Cloud services and when the usage and costs are available to the Cost Explorer. Typically, costs are available within a day, but this can sometimes take more than 24 hours.
  * **Gross costs:** The costs shown are generally _gross costs_ , reflecting usage at your contract prices _before_ any credits, such as Committed Use Discounts, sustained use discounts, or promotional credits, are applied.
  * **Currency:** When scoping by an App Hub application, all underlying resources within that application must use the same currency for costs to be aggregated. If resources are linked to billing accounts with different currencies, cost data for that application might be incomplete. 



## Utilization data

  * **Source:** Utilization metrics are sourced from Cloud Monitoring. 
  * **Availability:** Availability depends on the resource type and whether the appropriate agents (like the Ops Agent) are configured to collect detailed metrics.



## Product categories

The product names used in the Cost Explorer are designed to be logical and user-friendly. These might group costs differently than the service categories used within Cloud Billing reports. For example, costs that the Cost Explorer attributes to "Compute Engine" might encompass multiple underlying services from a Cloud Billing perspective.

Costs for products that the Cost Explorer doesn't support are reported under the product category **Other**. 

### Resource-level costs

This section lists supported products with resource-level cost data.

App Hub doesn't support all resources that the Cost Explorer supports, and there are some limitations for reported costs. For details, see Application costs.

[(Preview)](https://cloud.google.com/products#product-launch-stages) Data transfer costs are reported separately under **Networking costs** for some resources as indicated in the table of supported resources. 

Product name | Supported resources | Additional information | AlloyDB for PostgreSQL | Backup  
Cluster  
Instance |   
---|---|---  
App Engine | Service |  Data transfer costs are reported separately as networking costs.   
Bigtable | App Profile  
Instance |  **For instances** : Data transfer costs are reported separately as networking costs.  
Cloud Deploy | Delivery pipeline |   
Cloud Run | Job  
Service | 

  * Utilization data for Cloud Run is available for the 6-week period before the current date.
  * Data transfer costs are reported separately as networking costs.

  
Cloud Run functions | Function |  Data transfer costs are reported separately as networking costs.  
Compute Engine | Allocation  
Address  
Disk  
Forwarding rule  
Global address  
Image  
Instance  
Instant snapshot  
Machine image  
Managed instance group (MIG)  
Network attachment  
Reservation  
Snapshot  
Storage pool  
Target VPN gateway  
VPN gateway  
VPN tunnel | 

  * Local storage costs are reported under the product Persistent Disk.
  * **For instances and MIGs** : Data transfer costs are reported separately as networking costs.

  
Google Kubernetes Engine | Cluster | 

  * Resource cost includes Compute Engine VMs (vCPU, RAM, GPU) and the GKE [ cluster management fee](https://cloud.google.com/kubernetes-engine/pricing#cluster-management-fee).
  * Data transfer costs are reported separately as networking costs.
  * Local storage costs are reported under the product Persistent Disk. 

  
Dataflow | Job  
Snapshot |   
Cloud Data Fusion | Instance |   
Managed Service for Apache Spark | Batch  
Cluster  
Session | **For clusters** :

  * The resource cost includes the cost of the Compute Engine VMs (vCPU, RAM, GPU) and Managed Service for Apache Spark licensing fee.
  * Local storage costs are reported under the product Persistent Disk.
  * The following Managed Service for Apache Spark clusters don't support resource level costs: 
    * Clusters that use GKE as compute.
    * Clusters that use [unsupported image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-version-lists#unsupported-image-versions)

  
Dataproc Metastore | Service |   
Firestore | Database |  Data transfer costs are reported separately as networking costs.  
Cloud Interconnect ([Preview](https://cloud.google.com/products/#product-launch-stages)) | VLAN attachment |  The resource cost includes the hourly cost of the VLAN attachment. Data transfer costs for the VLAN attachment are reported separately as networking costs. Data transfer costs are not attributed to the resources that use the VLAN attachment.  
Backup for GKE | Backup plan |   
Cloud Load Balancing ([Preview](https://cloud.google.com/products/#product-launch-stages)) | Forwarding rule  
URL map | Data transfer and processing costs are not attributed to the resources that use the forwarding rule or URL map. 

  * For forwarding rules, the cost includes the hourly cost of the forwarding rule plus any hourly charges for proxy instances.
  * For URL maps, the cost includes the hourly cost of all forwarding rules grouped under the URL map.

Data transfer and data processing costs for a forwarding rule or URL map are reported separately as networking costs.  
Cloud Logging | Log bucket |   
Managed Service for Microsoft Active Directory | Domain |   
Memorystore for Redis | Instance |   
Secret Manager | Secret |   
Spanner | Instance  
Database |   
Cloud SQL Admin API | Instance |   
Cloud Storage | Bucket |  Data transfer costs are reported separately as networking costs.  
  
## Application costs

For an App Hub application, the total cost includes all resources that are fully used by the application.

The following limitations apply to application costs:

  * This total application cost doesn't include costs for the following: 
    * Resources that are shared across applications such as VLAN attachments.
    * Short-lived resources such as Managed Service for Apache Spark sessions and batches. 
  * Application cost only includes costs for resources that are [supported by App Hub](https://docs.cloud.google.com/app-hub/docs/supported-resources) and supported by the Cost Explorer. 
  * The cost for an application is only available if all application resources are linked to billing accounts in the same currency. 
  * You can't filter resources by location.



## What's next

  * [Optimize costs with the Cost Explorer](https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
