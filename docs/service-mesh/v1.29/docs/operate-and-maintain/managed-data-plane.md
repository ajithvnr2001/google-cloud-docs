---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/operate-and-maintain/managed-data-plane/
title: Managed data plane \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:09.096391+00:00
---

# Managed data plane  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/operate-and-maintain/managed-data-plane/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managed data plane

This page describes how to manage the data plane for managed Cloud Service Mesh.

If you use managed Cloud Service Mesh, Google fully manages upgrades of your proxies.

With the managed data plane feature enabled, the sidecar proxies and injected gateways are actively and automatically updated in conjunction with the managed control plane by restarting workloads to re-inject new versions of the proxy. This starts after the control plane has been upgraded and normally completes within 2 weeks after starting.

Note that the managed data plane relies on the GKE release channel. If you change the GKE release channel while the managed data plane is enabled, managed Cloud Service Mesh will update the proxies of all existing workloads like an managed data plane rollout.

If disabled, proxy management is done passively, driven by the natural lifecycle of the pods in the cluster, and must be manually triggered by the user to control the update rate.

The managed data plane upgrades proxies by evicting pods that are running earlier versions of the proxy. The evictions are done gradually, honoring the pod disruption budget and controlling the rate of change.

**Note:** If the cluster has a [GKE maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) defined, pod evictions will commence at the start of the next available maintenance window and continue without pause until all managed pods have been updated (usually 12 hours). Maintenance window is not observed for CVE related rollouts.

## When new versions of the Cloud Service Mesh data plane are deployed

Managed Data Plane | Events that trigger a new Cloud Service Mesh data plane deployment  
---|---  
Cloud Service Mesh active updates 

* * *

Actively, when new versions are available.1 | New Pod creation 

* * *

When you or horizontal Pod autoscaling deploy new Workloads  | GKE Maintenance Windows 

* * *

When nodes are replaced during a GKE maintenance window   
Enabled |  |  |   
Disabled |  |  |   
  
1 Cloud Service Mesh active updates automatically replace `Pods` in Workloads, except for `StatefulSets`, `Jobs`, `DaemonSets`, and manually injected `Pods`. Cloud Service Mesh active updates honor `Pod` disruption budgets.

  * Low-priority active updates coincide with GKE maintenance windows.
  * High-priority active updates can happen as soon as Cloud Service Mesh makes them available to your cluster, without respect to GKE maintenance windows. High-priority active updates usually have at least one associated CVE.



Enable the managed data plane if you don't want to manage the lifecycle of the Cloud Service Mesh data plane yourself, and your Workloads can tolerate Pods being replaced at any time.

Disable the managed data plane if you'd like full control over the time of all Cloud Service Mesh data plane updates.

Maintenance notifications are **not** sent by default. For more information, in this document, see [Enable maintenance notifications for the managed data plane](https://docs.cloud.google.com/service-mesh/v1.29/docs/onboarding/provision-control-plane#enable_maintenance_notifications_for_the_managed_data_plane).

## Limitations

The managed data plane doesn't manage the following:

  * Uninjected pods
  * Manually injected pods
  * Jobs
  * StatefulSets
  * DaemonSets



If you have provisioned managed Cloud Service Mesh on an older cluster, you can enable data plane management for the entire cluster:
    
    
    kubectl annotate --overwrite controlplanerevision -n istio-system \
    REVISION_LABEL \
    mesh.cloud.google.com/proxy='{"managed":"true"}'
    

Alternatively, you can enable the managed data plane selectively for a specific namespace or pod by annotating it with the same annotation. If you control individual components selectively, then the order of precedence is control plane revision, then namespace, then pod.

It could take up to ten minutes for the service to be ready to manage the proxies in the cluster. Run the following command to check the status:
    
    
    gcloud container fleet mesh describe --project FLEET_PROJECT_ID
    

Expected output
    
    
    membershipStates:
      projects/PROJECT_NUMBER/locations/global/memberships/CLUSTER_NAME:
        servicemesh:
          dataPlaneManagement:
            details:
            - code: OK
              details: Service is running.
            state: ACTIVE
        state:
          code: OK
          description: 'Revision(s) ready for use: asm-managed-rapid.'
    

If the service does not become ready within ten minutes, see [Managed data plane status](https://docs.cloud.google.com/service-mesh/v1.29/docs/managed/troubleshoot-managed-anthos-service-mesh#managed_data_plane_state) for next steps.

## Disable the managed data plane (optional)

If you are provisioning managed Cloud Service Mesh on a new cluster, then you can disable the managed data plane completely, or for individual namespaces or pods. The managed data plane will continue to be disabled for existing clusters where it was disabled by default or manually.

To disable the managed data plane at the cluster level and revert back to managing the sidecar proxies yourself, find every controlplanerevision then change each annotation.

  1. Find all the control plane revisions:
         
         kubectl get controlplanerevisions -n istio-system
         

  2. Change the annotation:
         
         kubectl annotate --overwrite controlplanerevision CONTROL_PLANE_REVISION_NAME -n istio-system mesh.cloud.google.com/proxy='{"managed":"false"}'
         

Repeat this step for each control plane revision.

Replace CONTROL_PLANE_REVISION_NAME with the output from the previous command.

To disable the managed data plane for a namespace:
         
         kubectl annotate --overwrite namespace NAMESPACE \
          mesh.cloud.google.com/proxy='{"managed":"false"}'
         

To disable the managed data plane for a pod:
         
         kubectl annotate --overwrite pod POD_NAME \
          mesh.cloud.google.com/proxy='{"managed":"false"}'
         




## Enable maintenance windows for the managed data plane

If you have a GKE maintenance window configured, active upgrades will commence at the start of the next available maintenance window and continue without pause until all managed pods have been updated (usually 12 hours). The maintenance window is not observed for CVE related rollouts.

Cloud Service Mesh uses the [GKE maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions) to align with GKE.

## Enable maintenance notifications for the managed data plane

You can request to be notified about upcoming managed data plane maintenance **scheduled within a maintenance window** up to a week before the maintenance is scheduled. Maintenance notifications are not sent by default. You must also [Configure a GKE maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions) before you can receive notifications. When enabled, notifications are sent at least two days before the upgrade operation.

**Important:** Maintenance notifications are **not** sent for upgrades that occur outside of a maintenance window, such as for a CVE rollout. In those cases, you should rely on updates published in the release notes.

To opt in to managed data plane maintenance notifications:

  1. Go to the **Communication** page.

[Go to the Communication page](https://console.cloud.google.com/user-preferences/communication/)

  2. In the **Cloud Service Mesh Upgrade** row, under the **Email** column, select the radio button to turn maintenance notifications **ON**.




Each user who wants to receive notifications must opt in separately. If you want to set an email filter for these notifications, the subject line is:

`Upcoming upgrade for your Cloud Service Mesh cluster "CLUSTER_LOCATION/CLUSTER_NAME"`.

The following example shows a typical managed data plane maintenance notification:

> Subject Line: Upcoming upgrade for your Cloud Service Mesh cluster "`<location/cluster-name>`"
> 
> Dear Cloud Service Mesh user,
> 
> The Cloud Service Mesh components in your cluster ${instance_id} (https://console.cloud.google.com/kubernetes/clusters/details/${instance_id}/details?project=${project_id}) are scheduled to upgrade on ${scheduled_date_human_readable} at ${scheduled_time_human_readable}.
> 
> You can check the release notes (https://cloud.google.com/service-mesh/docs/release-notes) to learn about the new update.
> 
> In the event that this maintenance gets canceled, you'll receive another email.
> 
> Sincerely,
> 
> The Cloud Service Mesh Team
> 
> (c) 2023 Google LLC 1600 Amphitheater Parkway, Mountain View, CA 94043 You have received this announcement to update you about important changes to Google Cloud Platform or your account. You can opt out of maintenance window notifications by editing your user preferences: https://console.cloud.google.com/user-preferences/communication?project=${project_id}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
