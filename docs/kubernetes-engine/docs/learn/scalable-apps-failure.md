---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-failure/
title: Learning Path: Scalable applications - Simulate a failure \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:48.902406+00:00
---

# Learning Path: Scalable applications - Simulate a failure  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-failure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Scalable applications - Simulate a failure Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This set of tutorials is for IT administrators and Operators that want to deploy, run, and manage modern application environments that run on Google Kubernetes Engine (GKE). As you progress through this set of tutorials you learn how to configure monitoring and alerts, scale workloads, and simulate failure, all using the Cymbal Bank sample microservices application:

  1. [Create a cluster and deploy a sample application](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment)
  2. [Monitor with Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-monitor)
  3. [Scale workloads](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-autoscale)
  4. Simulate a failure (this tutorial)
  5. [Centralize change management](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-centralize)



## Overview and objectives

Applications should be able to tolerate outages and failures. This ability lets users continue to access your applications even when there's a problem. The Cymbal Bank sample application is designed to handle failures and continue to run, without the need for you to troubleshoot and fix things. To provide this resiliency, GKE regional clusters distribute compute nodes across zones, and the Kubernetes controller automatically responds to service issues within the cluster.

In this tutorial, you learn how to simulate a failure in Google Cloud and see how the application Services in your GKE cluster respond. You learn how to complete the following tasks:

  * Review the distribution of nodes and Services.
  * Simulate a node or zone failure.
  * Verify that Services continue to run across the remaining nodes.



## Costs

Enabling GKE and deploying the Cymbal Bank sample application for this series of tutorials means that you incur per-cluster charges for GKE on Google Cloud as listed on our [Pricing page](https://cloud.google.com/kubernetes-engine/pricing) until you disable GKE or delete the project.

You are also responsible for other Google Cloud costs incurred while running the Cymbal Bank sample application, such as charges for Compute Engine VMs.

## Before you begin

To learn how to simulate a failure, you must complete the [first tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment) to create a GKE cluster that uses Autopilot and deploy the Cymbal Bank sample microservices-based application.

We recommend that you complete this set of tutorials for scalable apps in order. As you progress through the set of tutorials, you learn new skills and use additional Google Cloud products and services.

## Review distribution of nodes and Services

In Google Cloud, a _region_ is a specific geographical location where you can host your resources. Regions have three or more _zones_. For example, the `us-central1` region denotes a region in the Midwest region of the United States that has multiple zones, such as `us-central1-a`, `us-central1-b`, and `us-central1-c`. Zones have high-bandwidth, low-latency network connections to other zones in the same region.

To deploy fault-tolerant applications that have high availability, Google recommends that you deploy applications across multiple zones and multiple regions. This approach helps protect against unexpected failures of components, up to and including a zone or region.

When you created your GKE cluster in the first tutorial, some default configuration values were used. By default, a GKE cluster that uses Autopilot creates and runs nodes that span across zones of the region that you specify. This approach means that the Cymbal Bank sample application is already deployed across multiple zones, which helps to protect against unexpected failures.

  1. Check the distribution of nodes across your GKE cluster:
         
         kubectl get nodes -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The result is similar to the following example output that shows the nodes are spread across all three zones in the region:
         
         NAME                         ZONE            INT_IP
         scalable-apps-pool-2-node5   us-central1-c   10.148.0.6
         scalable-apps-pool-2-node6   us-central1-c   10.148.0.7
         scalable-apps-pool-2-node2   us-central1-a   10.148.0.8
         scalable-apps-pool-2-node1   us-central1-a   10.148.0.9
         scalable-apps-pool-2-node3   us-central1-b   10.148.0.5
         scalable-apps-pool-2-node4   us-central1-b   10.148.0.4
         

  2. Check the distribution of the Cymbal Bank sample application Services across your GKE cluster nodes:
         
         kubectl get pods -o wide
         

The following example output shows that the Services are distributed across nodes in the cluster. From the previous step to check how the nodes are distributed, this output shows that the Services run across zones in the region:
         
         NAME                                  READY   STATUS    RESTARTS   AGE     IP          NODE
         accounts-db-0                         1/1     Running   0          6m30s   10.28.1.5   scalable-apps-pool-2-node3
         balancereader-7dc7d9ff57-shwg5        1/1     Running   0          6m30s   10.28.5.6   scalable-apps-pool-2-node1
         contacts-7ddc76d94-qv4x5              1/1     Running   0          6m29s   10.28.4.6   scalable-apps-pool-2-node2
         frontend-747b84bff4-xvjxq             1/1     Running   0          6m29s   10.28.3.6   scalable-apps-pool-2-node6
         ledger-db-0                           1/1     Running   0          6m29s   10.28.5.7   scalable-apps-pool-2-node1
         ledgerwriter-f6cc7889d-mttmb          1/1     Running   0          6m29s   10.28.1.6   scalable-apps-pool-2-node3
         loadgenerator-57d4cb57cc-7fvrc        1/1     Running   0          6m29s   10.28.4.7   scalable-apps-pool-2-node2
         transactionhistory-5dd7c7fd77-cmc2w   1/1     Running   0          6m29s   10.28.3.7   scalable-apps-pool-2-node6
         userservice-cd5ddb4bb-zfr2g           1/1     Running   0          6m28s   10.28.5.8   scalable-apps-pool-2-node1
         




## Simulate an outage

Google designs zones to minimize the risk of correlated failures caused by physical infrastructure outages like power, cooling, or networking. However, unexpected issues can happen. If a node or zone becomes unavailable, you want Services to continue to run on other nodes or in zones in the same region.

The Kubernetes controller monitors the status of the nodes, Services, and Deployments in your cluster. If there's an unexpected outage, the controller restarts affected resources, and traffic is routed to working nodes.

To simulate an outage in this tutorial, you cordon and drain nodes in one of your zones. This approach simulates what happens when a node fails, or when a whole zone has an issue. The Kubernetes controller should recognize that some Services are no longer available and must be restarted on nodes in other zones:

  * Cordon and drain nodes in one of the zones. The following example targets the two nodes in `us-central1-a`:
        
        kubectl drain scalable-apps-pool-2-node1 \
            --delete-emptydir-data --ignore-daemonsets
        
        kubectl drain scalable-apps-pool-2-node2 \
            --delete-emptydir-data --ignore-daemonsets
        

This command marks the nodes as unschedulable so that Pods can no longer run on these nodes. Kubernetes reschedules Pods to other nodes in functioning zones.




## Check the simulated failure response

In a [previous tutorial in this series](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-monitor), you learned how to configured the managed Prometheus instance for your GKE cluster to monitor some of the Services and generate alerts if there's a problem. If Pods were running on nodes in the zone where you simulated an outage, you get Slack notification messages from the alerts generated by Prometheus. This behavior shows how you can build a modern application environment that monitors the health of your Deployments, alerts you if there's a problem, and can automatically adjust for load changes or failures.

Your GKE cluster automatically responds to the simulated outage. Any Services on affected nodes are restarted on remaining nodes.

  1. Check the distribution of nodes across your GKE cluster again:
         
         kubectl get nodes -o=custom-columns='NAME:.metadata.name,ZONE:.metadata.labels.topology\.kubernetes\.io/zone,INT_IP:.status.addresses[0].address'
         

The result is similar to the following example output that shows the nodes are now only spread across two of the zones in the region:
         
         NAME                         ZONE            INT_IP
         scalable-apps-pool-2-node5   us-central1-c   10.148.0.6
         scalable-apps-pool-2-node6   us-central1-c   10.148.0.7
         scalable-apps-pool-2-node3   us-central1-b   10.148.0.5
         scalable-apps-pool-2-node4   us-central1-b   10.148.0.4
         

  2. The Kubernetes controller recognizes that two of the nodes are no longer available, and redistributes Services across the available nodes. All of the Services should continue to run.

Check the distribution of the Cymbal Bank sample application Services across your GKE cluster nodes:
         
         kubectl get pods -o wide
         

The following example output shows that the Services are distributed across the remaining nodes in the cluster. From the previous step to check how the nodes are distributed, this output shows that the Services now only run across two zones in the region:
         
         NAME                                  READY   STATUS    RESTARTS   AGE     IP          NODE
         accounts-db-0                         1/1     Running   0          28m     10.28.1.5   scalable-apps-pool-2-node3
         balancereader-7dc7d9ff57-shwg5        1/1     Running   0          9m21s   10.28.5.6   scalable-apps-pool-2-node5
         contacts-7ddc76d94-qv4x5              1/1     Running   0          9m20s   10.28.4.6   scalable-apps-pool-2-node4
         frontend-747b84bff4-xvjxq             1/1     Running   0          28m     10.28.3.6   scalable-apps-pool-2-node6
         ledger-db-0                           1/1     Running   0          9m24s   10.28.5.7   scalable-apps-pool-2-node3
         ledgerwriter-f6cc7889d-mttmb          1/1     Running   0          28m     10.28.1.6   scalable-apps-pool-2-node3
         loadgenerator-57d4cb57cc-7fvrc        1/1     Running   0          9m21s   10.28.4.7   scalable-apps-pool-2-node5
         transactionhistory-5dd7c7fd77-cmc2w   1/1     Running   0          28m     10.28.3.7   scalable-apps-pool-2-node6
         userservice-cd5ddb4bb-zfr2g           1/1     Running   0          9m20s   10.28.5.8   scalable-apps-pool-2-node1
         

  3. Look at the `AGE` of the Services. In the previous example output, some of the Services have a younger age than others in the Cymbal Bank sample application. These younger Services previously ran on one of the nodes where you simulated failure. The Kubernetes controller restarted these Services on available nodes.


**Objective:** Congratulations! You have simulated the failure of nodes or in a zone in your GKE cluster and verified that Services in the Cymbal Bank sample application continue to run.

In a real scenario, you would troubleshoot the issue, or wait for the underlying maintenance issue to be resolved. If you configured Prometheus to send Slack messages based on alerts, you see these notifications come through. You can also optionally repeat the steps from [the previous tutorial to scale resources](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-autoscale) to see how your GKE cluster responds with increased load when only two zones are available with the region. The cluster should scale up with the two remaining zones available.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete the project you created.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

Learn how to [centralize change management with Config Sync](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-centralize) in the next tutorial.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
