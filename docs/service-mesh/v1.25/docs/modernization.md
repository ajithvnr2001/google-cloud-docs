---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/modernization/
title: Managed control plane modernization \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:25.383966+00:00
---

# Managed control plane modernization  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/modernization/

You are viewing archived v1.25 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managed control plane modernization

## Overview

Google will gradually update existing fleets which used the `ISTIOD` managed control plane implementation to use the `TRAFFIC_DIRECTOR` implementation. By default Google will automatically migrate your fleets, but you may opt to drive the migration yourself. To check which control plane your fleet is using, see [Check control plane implementation](https://docs.cloud.google.com/service-mesh/v1.25/docs/check-control-plane-implementation).

Consider the following when preparing your fleet for modernization:

  1. To prepare for modernization, you have two ways to control the process:

     * Google driven automatic migration (default) - You can customize the order that your clusters get modernized using instructions in Google-driven modernization.

     * Customer driven migration (optional) - You can choose to drive the modernization of your fleets yourself by labeling them according to instructions in Customer-driven modernization.

  2. Google-driven modernization is the default. With this option, Google determines when your fleets are ready for modernization. Google schedules your fleets for modernization and notifies you before starting the process.

  3. Modernizing a cluster will restart workloads that have proxies. This shouldn't cause downtime if you follow Kubernetes best-practices. In addition, Google will trigger modernization during a [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions), if you have configured one. Once started, it runs to completion with an additional 6 days of soak time before being marked as finalized. If your monitoring detects issues, you may request a rollback.

  4. For customer-driven modernization, Google notifies you when your fleets are ready for modernization. You can then choose when to trigger modernization, cluster by cluster. Once complete, you mark each fleet modernization as complete.

  5. Once a fleet is modernized, Google removes all Istiod-based components.

  6. The `TRAFFIC_DIRECTOR` control plane implementation requires that your cluster be registered to a fleet with the mesh feature enabled. If you onboarded using legacy tooling, Google will automatically register your cluster to its project's fleet, using the `gkehub.googleapis.com` Membership API. If you have any automation that unregisters a cluster, you must remove it before modernization.




## Google-driven modernization

This option is the default if you don't label your fleets for customer-driven modernization. Google will monitor your fleets to determine when they are ready to be safely modernized. When all mesh-enabled fleets in your [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) are ready, then your organization will be scheduled for modernization.

### Multiple fleets

If your organization has multiple fleets with managed Cloud Service Mesh, you can control the order in which Google modernizes your fleets by setting a project label of `mesh-modernization-order` to one of the values: `early`, `default`, `late`. Google will complete modernization of each group before beginning the modernization of any fleet in the next group. Fleets that you have opted for customer-driven modernization won't be considered in this ordering.

Use the following command to set the `mesh-modernization-order` label for a fleet:
    
    
    gcloud alpha projects update FLEET_PROJECT_ID --update-labels="mesh-modernization-order=VALUE"
    

For instructions on setting project labels using the Console or REST, see the [creating and managing labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) document.

If you don't use Google Cloud organizations, then your fleets will be scheduled and modernized independently, and you cannot control the ordering.

### Multi-cluster meshes

If a fleet has multiple clusters using managed Cloud Service Mesh, you can control the order in which Google modernizes the clusters by setting the cluster label of `mesh-modernization-order` to one of the values: `early`, `default`, `late`. Google will begin modernization of each group and wait for automated modernization steps to complete, before beginning the modernization of any cluster in the next group. Note that this ordering will only apply within a fleet, it won't affect other fleets in your organization that may be modernizing in parallel.

Use the following command to set the `mesh-modernization-order` label for a cluster:
    
    
    gcloud container clusters update CLUSTER_NAME \
      --location LOCATION \
      --update-labels="mesh-modernization-order=VALUE"
    

## Notifications and Scheduling

This section describes how you will be notified of the upcoming modernization of your fleets and clusters.

### Notification that modernization will be scheduled soon

First, you will be notified when your fleets have been selected for Google-driven modernization to take place in the upcoming weeks.

This notification will be sent prior to the first US business day of a month. The earliest possible cluster modernization start date is 14 days after the first US business day of a month, and Google will make a best effort to begin the first cluster modernization for your organization by the end of the next calendar month. For example, notifications will be in place before April 1, 2025, cluster modernizations may begin starting April 15, 2025, and your first cluster modernization should start before May 31, 2025.

You will be notified simultaneously for each of the fleets in your organization (excluding those you have opted for [customer-driven modernization](https://docs.cloud.google.com/service-mesh/v1.25/docs/modernization#customer-driven-modernization)).

This notification is available in your fleet-level feature state conditions. Use the following Google Cloud CLI command to check the notification:
    
    
    gcloud alpha container fleet mesh describe --project $FLEET_PROJ
    

Once the fleet is scheduled, you will see a condition with `code: MODERNIZATION_WILL_BE_SCHEDULED` and `details` similar to the following:
    
    
    state:
      servicemesh:
        conditions:
          - code: MODERNIZATION_WILL_BE_SCHEDULED
            details: We will soon schedule clusters in this fleet to be modernized to use the TRAFFIC_DIRECTOR
              control plane implementation. Please confirm your fleet and cluster preferences prior to
              scheduling. Cluster modernization dates will be on or after 2025-03-17.
            documentation_link: ...
            severity: INFO
    

### Cluster-level notification that modernization is scheduled

You will be notified, at the cluster level, of the estimated start date for Google-driven modernization of that cluster, at least 1 day before cluster modernization begins.

Following the fleet-level notification, this gives you much more precise timing of modernization of individual clusters.

Notifications are available in your cluster-level feature state conditions. Use the following Google Cloud CLI command to check the notification:
    
    
    gcloud container hub mesh describe --project=PROJECT_ID
    

You will see results similar to the following:
    
    
    membershipStates:
      projects/656460026795/locations/us-central1/memberships/cluster:
        servicemesh:
          conditions:
          - code: MODERNIZATION_SCHEDULED
            details: This cluster has been scheduled for modernization on or after 2025-03-17.
            documentationLink: ...
            severity: INFO
    

## Active modernization for Google-driven migration

This section describes the steps of Google-driven modernization.

### Modernizing fleets

Google will trigger active modernization of each of your organization's fleets. This means for each fleet the following steps are executed:

  1. Modernize all clusters with `mesh-modernization-order` of `early`.
  2. Modernize all clusters with `mesh-modernization-order` of `default` or unspecified.
  3. Modernize all clusters with `mesh-modernization-order` of `late`.
  4. Wait for each cluster's modernization to be marked as finalized. This means waiting at least 6 business days after restarting the last pod in any cluster in this fleet.
  5. Finalize this fleet's modernization, eventually removing Istiod-based components.



### Modernizing a cluster

During active modernization of a cluster, both control plane implementations are temporarily run side by side, and in a safe and controlled way the following tasks are processed:

  1. Enable the new control plane implementation. If you configured maintenance windows for your cluster, and are using Google-driven modernization, this step will begin during a maintenance window and continue until complete. 
     * To enable health checking, the `snk` daemonset is created in the `kube-system` namespace of the cluster and a per-cluster firewall rule is created. 
       * To enable [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs) ingestion, the annotation `cloud.google.com/neg` is added to all Kubernetes services.
       * New Google Cloud resources such as [mesh](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview), [routes](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-routing-overview), [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service), and [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) are created in the cluster.
       * Some of the new resources are quota-limited. You can [view quotas and request more if necessary](https://docs.cloud.google.com/load-balancing/docs/quotas).
       * The cluster is monitored during soak time prior to moving to the next step.
  2. Shift traffic to the new control plane implementation. If you configured maintenance windows for your cluster, and are using Google-driven modernization, this step will begin during a maintenance window and continue until complete. 
     * Pods managed by Kubernetes deployment that have Cloud Service Mesh proxies are restarted, so they reconnect to the new control plane.
     * Pods are restarted in progressively-larger waves with soak time after each wave for monitoring.
  3. There is a wait of at least 6 business days of soak time before a cluster's modernization is marked as finalized.



Use the following Google Cloud CLI command to check the status of active modernization:
    
    
    gcloud container fleet mesh describe --project FLEET_PROJECT_ID
    

You will see a condition like one of the following in the per-cluster `membershipStates` field:
    
    
    ...
    membershipStates:
      projects/FLEET_PROJ/locations/us-central1/memberships/MEMBERSHIP:
        servicemesh:
          conditions:
          - code: MODERNIZATION_IN_PROGRESS
            details: ...
            documentationLink: ...
            severity: INFO
    ...
          # If you see this, see instructions provided in the details and documentationLink fields.
          - code: MODERNIZATION_ACTION_REQUIRED
            details: [details about required actions]
            documentationLink: [link to documentation for required actions]
            severity: WARNING
    ...
          - code: MODERNIZATION_COMPLETED
            details: ...
            documentationLink: ...
            severity: INFO
    

## Customer-driven modernization

You can opt to control the exact timing of modernization yourself at the fleet level. To do this, apply a [label](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) on the fleet host project using the following command:
    
    
    gcloud alpha projects update FLEET_PROJECT_ID \
      --update-labels="mesh-modernization-mode=manual"
    

Note that if your Google Cloud organization has multiple fleets, any fleet not labeled will be scheduled for Google-driven modernization.

Once your fleet is eligible to be modernized, you will get a notification in the fleet-level feature state. You must trigger modernization within 3 months of receiving this notification.

This documentation will be updated to include details on how to manually trigger modernization. Subscribe to the [Cloud Service Mesh release notes feed](https://docs.cloud.google.com/service-mesh/v1.25/docs/release-notes) to get notified.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
