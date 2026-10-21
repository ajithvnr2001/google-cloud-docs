---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/add-monitoring-points/
title: Add Monitoring Points \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:22.806560+00:00
---

# Add Monitoring Points  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/add-monitoring-points/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Add Monitoring Points Stay organized with collections  Save and categorize content based on your preferences. 

Monitoring Points are lightweight software agents that execute the active synthetic probes necessary to monitor your network and web application performance. They are the source of all synthetic network traffic and can also be a target of testing.

## Monitoring architecture

Cloud Network Insights uses a centralized management model with Monitoring Points.

  * Google Cloud project - the central control where you enable Cloud Network Insights. You use this project to do the following: 
    * Download Monitoring Point installation packages (Docker, Helm, OVA/QCOW2, TF)
    * View the status and inventory of all your deployed Monitoring Points
    * [Access Cloud Monitoring dashboards](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/view-dashboards) for metrics
    * [Configure Alert Policies and Notification Channels](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts) in Google Cloud Observability
  * Monitoring locations - the target hosts in the environments you want to monitor. This is where you install the Monitoring Points.



## Deployment locations

When installing Monitoring Points in the monitoring locations, select critical network segments, such as a central VPC, remote branch office, or specific cloud region. The following environments are supported:

  * Google Cloud Virtual Private Cloud (VPC) networks in the same or different projects
  * Remote branch offices or retail locations
  * On-premises data centers
  * Other cloud environments, for example, AWS or Azure



If you need help to determine where to install Monitoring Points to target strategic web application deployment, use VPC Flow Logs or `vm_flow` metrics in a performance dashboard to understand where traffic is flowing in your network.

We don't recommend installing Monitoring Points on the project with Cloud Network Insights enabled or directly on the workloads you want to monitor. For more information, see [Best practices](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/best-practices) or [AppNeta's Deployment Best Practices](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/appliance-where.html).

## Supported Monitoring Point types

Cloud Network Insights supports the following Monitoring Point types.

| **Monitoring Point type** | **Best for** | **Link to AppNeta documentation**  
---|---|---|---  
**Containers** | **Docker container** | Lightweight and ideal for cloud instances.  
Linux VMs, Google Compute Engine instances, or any Docker-enabled host, including on-premises environments. | [c50-Docker/Podman](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/docker-mp-intro.html)  
**Kubernetes (Helm)** | Best for orchestrated environments.  
Google Kubernetes Engine (GKE), Amazon EKS, Azure AKS, or on-premises Kubernetes clusters. | [c50-Kubernetes (Helm)](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/kubernetes-mp-intro.html)  
**Virtual machines (VM)** | **VMware (OVA)** | On-premises data centers running VMware ESXi or vCenter.  
Deploys as a full virtual machine. | [v35-VMware](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-vmware-mp-intro.html)  
**KVM (QCOW2)** | Monitor telco clouds or private Linux clouds.  
Linux-based virtualized environments such as OpenStack, custom Linux hypervisors. | [v35-KVM](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/v35-kvm-mp-intro.html)  
**Cloud** | **Google Cloud** | Embed a Monitoring Point optimized for your Google Cloud infrastructure.   
| [Google CE Cloud Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/gce-mp-intro.html)  
**Microsoft Azure** | Embed a Monitoring Point optimized for your Microsoft Azure infrastructure.   
| [Azure VM Cloud Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/azure-vm-mp-intro.html)  
**Amazon EC2** | Embed a Monitoring Point optimized for your AWS infrastructure.   
| [AWS EC2 Cloud Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/aws-ec2-mp-intro.html)  
  
## What's next

  * [Deploy Google Cloud Monitoring Points](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-gce-monitoring-points)

  * [Deploy Microsoft Azure Monitoring Points](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-azure-monitoring-points)

  * [Deploy AWS Monitoring Points](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-aws-monitoring-points)

  * [Deploy container Monitoring Points](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-container-monitoring-points)

  * [Deploy VM Monitoring Points](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/deploy-vms-monitoring-points)




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
