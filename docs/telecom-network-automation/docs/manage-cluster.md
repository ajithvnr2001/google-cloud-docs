---
url: https://docs.cloud.google.com/telecom-network-automation/docs/manage-cluster/
title: Manage the Orchestration cluster \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:44.392182+00:00
---

# Manage the Orchestration cluster  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/manage-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Manage the Orchestration cluster Stay organized with collections  Save and categorize content based on your preferences. 

The Telecom Network Automation Orchestration cluster is built on top of [Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview). Telecom Network Automation supports only one `OrchestrationCluster` at a time. This page describes how to manage Orchestration clusters.

## Create an Orchestration cluster

Before you create an Orchestration cluster, ensure you have the Telco Automation Admin (`roles/telcoautomation.admin`) role.

To create an Orchestration cluster, work through the following steps:

  1. Go to the **Overview** page. Click **Setup Telecom Network Automation**.
  2. On the next page, include the following details:

     * Add a unique name for the Orchestration cluster.
     * From the drop-down menu, select the region for the Orchestration cluster.
     * If you require management config, click **Enable management config** and input your values into the following fields. If not specified, default values are chosen for optional fields:

**Note:** For details on the fields to input, follow [Set up Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/config-controller-setup).
       * Select either **Standard management config** or **Full management config** :
       * **Standard management config** implies GKE Standard management config.
       * **Full management config** implies the GKE auto-pilot mode.
       * In the required field **Network** , input the name of the VPC network to include the GKE cluster and nodes. If the VPC does not exist, Telecom Network Automation creates one.
       * In the **Subnet** field, specify the subnet the interface is part of. You must specify the network key and the subnet must be a subnetwork of the specified network.
       * In the required field **Control plane address range** , input the **/28** network range for the main network to use.
       * In the field, **Cluster default pod address range** , input the IP address range for the cluster pod IP addresses.
       * To set a default size for a range, set the field blank.
       * For a range with a specific netmask, set to **/netmask**. For example, **/14**.
       * To select a specific range to use, set to a CIDR Notation, such as 10.96.0.0/14, from the RFC-1918 private networks. For example, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
       * In the field, **Service address range** , input the IP address range for the cluster service IP addresses.
       * To set a default size for a range, set the field blank.
       * For a range with a specific netmask, set to **/netmask**. For example, **/14**.
       * To select a specific range to use, set to a CIDR Notation, such as 10.96.0.0/14, from the RFC-1918 private networks. For example, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
       * In the field **Cluster named range** , enter the name of the existing secondary range in the cluster's subnetwork to use for a pod IP address.
       * To automatically create a range GKE manages, use **cluster_cidr_block**.
       * In the field, **Service named range** , enter the name of the existing secondary range in the cluster's subnetwork for service cluster IP addresses.
       * To automatically create a range GKE manages, use **cluster_cidr_block**.
       * To start the control plane authorized networks, click **Enable control plane authorized networks**.
       * To add one or more networks, click **Add authorized network**. 
         * For each authorized network, add fields **Name** and **CIDR range**. For more information, see [Add authorized networks for control plane access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).
  3. Click **Create**.

  4. Wait up to 20 minutes for the Orchestration cluster to create.




## Start Cloud Logging and Monitoring

After you create the Orchestration cluster, set the required permissions to use Cloud Logging and Monitoring. You require the following roles:

  * Resource Metadata Writer
  * Log Writer
  * Metric Writer



To start Cloud Logging and Monitoring, do the following:

  * Grant the required permissions to export the logs and metrics from workloads running on GDC clusters to Cloud Logging and Monitoring:
        
        gcloud projects add-iam-policy-binding $PROJECT_ID --member
        serviceAccount:${PROJECT_ID:?}.svc.id.goog[kube-system/metadata-agent] --role='roles/opsconfigmonitoring.resourceMetadata.writer'
        gcloud projects add-iam-policy-binding $PROJECT_ID --member
        serviceAccount:$PROJECT_ID.svc.id.goog[kube-system/stackdriver-log-forwarder] --role='roles/logging.logWriter'
        gcloud projects add-iam-policy-binding $PROJECT_ID --member
        serviceAccount:$PROJECT_ID.svc.id.goog[kube-system/gke-metrics-agent] --role='roles/monitoring.metricWriter'
        




## Delete an Orchestration cluster

Before you delete an Orchestration cluster, we recommend you to delete all blueprints and deployments in GDC, GKE, and the Edge Network that you've created through the Orchestration cluster. Ensure you have the Telco Automation Admin (`roles/telcoautomation.admin`) role to delete the Orchestration cluster.

To delete the Orchestration cluster, work through the following steps:

  1. From the navigation menu, click **Orchestration clusters**.
  2. In the **Orchestration Cluster** list, click the Action icon next to the orchestration cluster you want to delete.
  3. Click **Delete**. A dialog opens.
  4. Click **Delete**.
  5. Wait up to 20 minutes for the deletion to take effect.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
