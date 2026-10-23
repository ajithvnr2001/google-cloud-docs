---
url: https://docs.cloud.google.com/service-mesh/docs/modernization/
title: Managed control plane modernization \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:44.129101+00:00
---

# Managed control plane modernization  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/modernization/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managed control plane modernization

**Caution:** managed Cloud Service Mesh with the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must modernize all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` implementation. 

You must modernize your Cloud Service Mesh fleets from the [deprecated](https://docs.cloud.google.com/service-mesh/deprecations) `ISTIOD` control plane implementation to the `TRAFFIC_DIRECTOR` implementation before the end-of-support deadline. You can initiate modernization on your own schedule, or let Google schedule it automatically once your organization is compatible.

There are two modernization pathways, and you may also mix and match them:

  * **Customer-triggered modernization (Self-service)** : You initiate and control the exact timing of fleet modernization yourself using the Google Cloud CLI, independent of Google-driven schedules.
  * **Google-driven modernization (Default)** : Google evaluates fleet compatibility and automatically schedules modernization across your [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) according to [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions) and advance notifications. Google waits for all fleets in your organization to be compatible, so a single incompatible fleet will block your modernization.



Regardless of which pathway you choose, you need to complete the following core steps to modernize your control plane:

  1. **Check your compatibility** : Enable compatibility checks, and understand your fleets' compatibility with modernization.
  2. **Plan and configure your modernization** : Choose your pathway, configure cluster and fleet rollout ordering, or defer specific fleets.
  3. **Remediate compatibility gaps** : Ensure that your fleets meet all compatibility requirements before initiating modernization.
  4. **Initiate modernization** : Trigger customer-triggered modernization on your schedule, or await Google-driven scheduling.
  5. **Active cluster modernization** : During configured maintenance windows, dual control planes run side by side, and Deployments (workloads and gateways) transition automatically to the new control plane. You will need to manually restart StatefulSet and DaemonSet workloads.
  6. **Monitor status, soak, and finalize** : Monitor condition progress, resolve any stalls, observe workloads during the soaking period (at least 6 business days), with full rollback support prior to fleet-level finalization.



## Check fleet compatibility & remediate gaps

Before any fleet can modernize—under either customer-triggered or Google-driven modernization—the fleet must be verified as compatible. You must enable compatibility reporting to inspect potential blocker conditions and remediate configuration gaps. For more details, see [Understanding Cloud Service Mesh compatibility](https://docs.cloud.google.com/service-mesh/docs/migrate/eligibility).

  * For **Google-driven modernization** : Google will only schedule organizations where all non-deferred fleets are compatible.
  * For **Customer-triggered modernization** : You must verify that your target fleet reports `MODERNIZATION_COMPATIBLE` before initiating modernization.



Compatibility checks evaluate your fleet's Istio CRD configurations, Pod annotations, infrastructure dependencies (such as Workload Identity), and scale parameters.

### Handling unsupported features

As part of the `ISTIOD` control plane deprecation, Google Cloud is ending support for features that are incompatible with the `TRAFFIC_DIRECTOR` control plane implementation. See details of [API support](https://docs.cloud.google.com/service-mesh/docs/onboarding/api-support).

If you are using unsupported features, you must take one of the following actions before support ends (see [Deprecations](https://docs.cloud.google.com/service-mesh/deprecations)):

  * **Refactor your configuration (Recommended)** : Remove the unsupported fields or replace them with supported Cloud Service Mesh alternatives so your fleet reports `MODERNIZATION_COMPATIBLE`, and then modernize to the `TRAFFIC_DIRECTOR` control plane implementation.
  * **Migrate to open source (OSS) Istio** : If your workloads strictly require features that managed Cloud Service Mesh with `TRAFFIC_DIRECTOR` does not support, you cannot modernize those clusters to `TRAFFIC_DIRECTOR`. You must migrate those workloads to self-managed open source Istio.
  * **Uninstall Cloud Service Mesh** : You can [uninstall managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/uninstall-managed).



## Plan and configure your modernization

Make a plan for how your fleet(s) should be modernized. If you don't do this, Google-driven modernization is applied in a default way. You must take action to ensure your non-prod fleets are modernized first and your critical fleets are modernized last. Further, Google-driven modernization won't schedule your organization's modernization until 100% of non-deferred fleets in your entire organization are compatible, so your modernization could be blocked by local incompatibilities.

Before initiating modernization, review your options and configure your rollout settings across your organization's fleets and clusters.

### Available pathways

Approach | Description | Best For | Scope | Prerequisites | Advance Notice | Rollback Capability  
---|---|---|---|---|---|---  
**Customer-Triggered Modernization** | You initiate modernization fleet-by-fleet on your own schedule. | Granular control over fleet modernization timing (you decide when to initiate and when to roll back at the fleet level). Leveraging your existing application monitoring to alert you if a rollback is needed. | Fleet-by-fleet (`FLEET_PROJECT_ID`). | Target fleet must be modernization-compatible. | N/A. | Immediate self-service rollback using Google Cloud CLI.  
**Google-Driven Modernization (Default)** | Google automatically schedules modernization across your organization. | Automated modernization once all fleets across your organization are compatible. | Entire Google Cloud organization (all non-deferred fleets). | All non-deferred fleets in the organization must be modernization-compatible. | 14+ day fleet notification + 24+ hour cluster notification before starting. | Google will roll back if standardized monitoring shows an error. You must contact Cloud Customer Care if your application monitoring shows an error.  
  
### Managing multiple fleets across an organization

If your Google Cloud organization manages multiple fleets, you don't need to choose a single approach for all of them. You can combine strategies, for example:

  * Defer complex or critical fleets: Pin specific fleets to the legacy implementation using `--modernization-strategy deferred` so they are excluded from Google-driven scheduling while you remediate dependencies or plan customer-triggered execution.
  * Start with customer-triggered modernization on selected fleets: Modernize test, development, or evaluation fleets first to validate behavior on your own timeline.
  * Allow Google to modernize remaining fleets: Any compatible, non-deferred fleets remain opted into Google-driven scheduling.



### Deferring fleet modernization (opt-out)

To opt an individual fleet out of Google-driven modernization, set its strategy to `DEFERRED`:
    
    
    gcloud alpha container fleet mesh update \
      --modernization-strategy deferred \
      --project FLEET_PROJECT_ID
    

Replace FLEET_PROJECT_ID with the ID of the fleet host project.

Setting `--modernization-strategy deferred` is the recommended way to:

  * Exclude specific fleets from Google-driven scheduling because you intend to modernize them on your own timeline using customer-triggered modernization.
  * Temporarily hold off modernization on complex or critical fleets while you remediate dependencies, allowing other compatible fleets in your organization to proceed with Google-driven scheduling.



Note that the legacy project label `mesh-modernization-mode=manual` remains respected, but `--modernization-strategy deferred` is recommended. Other non-deferred fleets in your organization remain eligible for Google-driven scheduling once they are all compatible.

**Warning:** Setting a fleet to `deferred` (or leaving compatibility gaps unresolved) only opts the fleet out of automated Google-driven scheduling; it **does not extend support past the deadline** (see [Deprecations](https://docs.cloud.google.com/service-mesh/deprecations)). 

### Configuring rollout ordering

You can control the sequential rollout order across your clusters and fleets using the `mesh-modernization-order` label (early, default, or late).

#### Cluster rollout ordering (applies to both pathways)

If a fleet contains multiple clusters, you can control the order in which clusters modernize by applying the `mesh-modernization-order` label to each cluster. When you or Google triggers a fleet's modernization, each cluster group is modernized sequentially, waiting for automated modernization steps to complete on the current group before beginning the next:
    
    
    gcloud container clusters update CLUSTER_NAME \
      --location LOCATION \
      --update-labels="mesh-modernization-order=VALUE"
    

Replace CLUSTER_NAME with the name of the cluster, LOCATION with the cluster's location, and VALUE with one of the following:

  * `early`: The cluster is modernized in the first wave of modernization.
  * `default`: The cluster is modernized in the second wave of modernization.
  * `late`: The cluster is modernized in the third and final wave of modernization.



#### Fleet rollout ordering (Google-driven only)

In organizations with multiple fleets undergoing Google-driven modernization, you can control the order in which Google modernizes your fleets by setting the project-level label on the fleet host project:
    
    
    gcloud alpha projects update FLEET_PROJECT_ID \
      --update-labels="mesh-modernization-order=VALUE"
    

Replace FLEET_PROJECT_ID with the ID of the fleet host project and VALUE with one of the following:

  * `early`: The fleet is modernized in the first wave of modernization.
  * `default`: The fleet is modernized in the second wave of modernization.
  * `late`: The fleet is modernized in the third and final wave of modernization.



Google completes modernization of each fleet tier before starting the next, early, then default (and unlabeled), then late. Fleets marked as deferred are not included in this ordering.

For example you could set your non-prod fleets to `early`, an especially critical fleet to `late`, and leave others at the default.

If you don't use Google Cloud organizations, then your fleets will be scheduled and modernized independently, and you cannot control the ordering.

## Customer-triggered modernization (self-service)

Customer-triggered modernization gives you direct control over when modernization starts for an individual fleet.

### Triggering fleet modernization

Once your target fleet [reports](https://docs.cloud.google.com/service-mesh/docs/migrate/eligibility#fleet-level-compatibility) `MODERNIZATION_COMPATIBLE`, trigger modernization using the following command:
    
    
    gcloud alpha container fleet mesh update \
      --modernization-strategy automatic \
      --project FLEET_PROJECT_ID
    

Replace FLEET_PROJECT_ID with the ID of the fleet host project.

  * **Maintenance Windows** : Google respects configured cluster maintenance windows and exclusions. Cluster modernization begins during the cluster's next open maintenance window.
  * **Cluster Ordering** : If you configured `mesh-modernization-order` labels on your clusters, Google honors that ordering.



### Monitor progress

Follow the instructions at Check Modernization Status to monitor the progress of fleet and cluster modernization. Watch your application monitoring to determine if you need a rollback, especially during the `MODERNIZATION_PREPARING` and `MODERNIZATION_MIGRATING_WORKLOADS` statuses.

### Rolling back a customer-triggered modernization

If you detect issues during active cluster modernization or during the fleet soaking period (before fleet-level finalization), you can trigger an immediate rollback:
    
    
    gcloud alpha container fleet mesh update \
      --modernization-strategy deferred \
      --project FLEET_PROJECT_ID
    

Replace FLEET_PROJECT_ID with the ID of the fleet host project.

This will leave your fleet in the deferred state, that is it won't be considered for Google-driven modernization. When you are ready to retry modernization, re-run the command to trigger fleet modernization.

**Important:** Rollback triggers immediately, bypassing maintenance windows. Workloads are returned to the legacy ISTIOD control plane. Rollback is supported throughout active modernization and during the soaking period, but is no longer possible once the fleet reaches `MODERNIZATION_FINALIZED`.

## Google-driven modernization (automated default)

If you don't initiate customer-triggered modernization, Google manages modernization across your organization automatically.

### Organization-wide scheduling

Google continuously monitors your fleets. After all mesh-enabled fleets in your organization (excluding any deferred fleets) are modernization-compatible, Google schedules your organization for modernization.

### Advance notifications and scheduling

Google provides two levels of advance notification before starting modernization:

#### Fleet-level notification

First, you will be notified when your fleets have been identified as modernization-compatible, and selected for Google-driven modernization to take place in the future.

  * Your cluster modernization can start as early as 14 days after the first US business day of the month following your notification. For example, if Google determines your organization is ready on January 10, 2027, we'll notify you by January 31, 2027, that your earliest possible modernization start date is February 15, 2027.

  * You will be notified simultaneously for each of the fleets in your organization (excluding those you have deferred). This notification is available in your fleet-level feature state conditions (`MODERNIZATION_WILL_BE_SCHEDULED`).




#### Cluster-level notification

You will be notified, at the cluster level, of the estimated start date for Google-driven modernization of that cluster, at least 1 day (24 hours) before cluster modernization begins.

Following the fleet-level notification, this gives you much more precise timing of modernization of individual clusters. This notification is available in your cluster-level feature state conditions (`MODERNIZATION_SCHEDULED`).

### Requesting rollback for Google-driven modernization

If issues arise during active modernization or soaking on a Google-driven modernization fleet, contact [Cloud Customer Care](https://cloud.google.com/support) to request a rollback.

## What happens during active modernization

This section describes what happens during the active modernization of fleets and clusters.

### Modernizing fleets

For each fleet undergoing modernization (whether Google-driven or customer-triggered), we enable the new control plane implementation for all clusters based on ordering (early → default → late).

Once the control plane is enabled for all clusters, we shift traffic to the new control plane implementation for all clusters based on ordering (early → default → late).

See Check fleet modernization status to check current status.

#### Fleet soak period

Once traffic is shifted for all clusters, the fleet enters a soaking period. The fleet remains in the soaking period (`MODERNIZATION_MODERNIZED`) for **at least 6 business days** after all clusters complete modernization before transitioning to `MODERNIZATION_FINALIZED`. Full rollback capability is preserved throughout the soak period. Once modernization is finalized, rollback is no longer possible, and `ISTIOD` components may be deprovisioned.

### Modernizing a cluster

During active modernization of a cluster, both control plane implementations are temporarily run side by side, and in a safe and controlled way the following tasks are processed:

  1. Enable the new control plane implementation. If you configured maintenance windows for your cluster, this step will begin during a maintenance window and continue until complete. Note the following details: 
     * To enable health checking, the `snk` daemonset is created in the `kube-system` namespace of the cluster and a per-cluster firewall rule is created.
     * To enable [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs) ingestion, the annotation `cloud.google.com/neg` is added to all Kubernetes services.
     * New Google Cloud resources such as [mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview), [routes](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview), [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service), and [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) are created in the cluster.
     * Some of the new resources are quota-limited. You can [view quotas and request more if necessary](https://docs.cloud.google.com/load-balancing/docs/quotas).
     * The cluster is monitored during soak time prior to moving to the next step.
  2. Shift traffic to the new control plane implementation. If you configured maintenance windows for your cluster, this step will begin during a maintenance window and continue until complete. Note the following details: 
     * Pods managed by Kubernetes deployment that have Cloud Service Mesh proxies are restarted, so they reconnect to the new control plane.
     * Pods are restarted in progressively-larger waves with soak time after each wave for monitoring.
  3. Manual Workload Restarts for Non-Deployments (Customer Action Required). 

     * Google automatically restarts workloads managed by Kubernetes Deployments. Workloads managed by other types of Kubernetes resources, such as StatefulSets and DaemonSets, must be restarted manually.
     * Restart these workloads after the cluster status reports `MODERNIZATION_COMPLETED` (that is, when the cluster is in the soaking period).
     * You must restart these workloads before the fleet's modernization is finalized, otherwise those proxies remain connected to the legacy Istiod control plane that is scheduled for deprovisioning.
     * Restart workloads using standard Kubernetes approaches, such as `kubectl rollout restart ...`
  4. Once all workloads in a cluster are transitioned, the cluster waits for the fleet soak period.




To monitor the active modernization status of your clusters, see Check modernization status.

## Check modernization status & take action

You can monitor the modernization progress of your fleets and clusters using the Google Cloud CLI:
    
    
    gcloud container fleet mesh describe --project FLEET_PROJECT_ID
    

Replace FLEET_PROJECT_ID with the ID of the fleet host project.

The output is similar to:
    
    
      membershipStates:
        projects/123456789/locations/global/memberships/cluster-1:
          servicemesh:
            conditions:
            - code: MODERNIZATION_MIGRATING_WORKLOADS
              documentationLink: https://cloud.google.com/service-mesh/docs/...
              severity: INFO
      state:
        servicemesh:
          conditions:
          - code: MODERNIZATION_MODERNIZING
            documentationLink: https://cloud.google.com/service-mesh/docs/...
            severity: INFO
    

Modernization status is reported in the `state.servicemesh.conditions` (fleet-level) and `membershipStates.<MEMBERSHIP_NAME>.servicemesh.conditions` (cluster-level) fields:

### Status of a successful fleet modernization

In a successful fleet modernization, the fleet's status will start as `MODERNIZATION_MODERNIZING`.

Each cluster would then go through the statuses:

  * `MODERNIZATION_SCHEDULED`
  * `MODERNIZATION_PREPARING`
  * `MODERNIZATION_PREPARED`
  * `MODERNIZATION_MIGRATING_WORKLOADS`
  * `MODERNIZATION_COMPLETED`



Once all clusters in the fleet have completed their modernization, the fleet will go through statuses:

  * `MODERNIZATION_MODERNIZED`
  * `MODERNIZATION_FINALIZED`



### Rollbacks

Google-driven modernization monitors your deployment readiness and health throughout the modernization process, and we will automatically trigger a rollback if we detect problems. If you detect an issue, contact [Cloud Customer Care](https://cloud.google.com/support) to request a rollback.

For customer-triggered modernization you may trigger a rollback at any time.

During a rollback the fleet shows the status `MODERNIZATION_ROLLING_BACK_FLEET` and the cluster shows the status `MODERNIZATION_ROLLING_BACK_CLUSTER`.

Once a cluster rollback completes, it temporarily shows the status `MODERNIZATION_ABORTED`.

### Handling errors and stalls (customer-triggered only)

During customer-triggered modernization, if a cluster encounters an issue that prevents forward progress, its condition transitions to `MODERNIZATION_STALLED`. Google won't trigger rollbacks for customer-triggered modernization. You must triage the issue and decide whether to fix-forward or to trigger a rollback.

When a cluster reports `MODERNIZATION_STALLED`, inspect the condition details, for a direct link to the relevant error section:

#### User-actionable errors

If we detect an incompatible mesh or cluster configuration, we will halt the modernization. Ensure that compatibility reporting is enabled, and review your fleet- and cluster-level conditions for gaps, as described in [Understanding Cloud Service Mesh compatibility](https://docs.cloud.google.com/service-mesh/docs/migrate/eligibility).

  * **Immediate Retry** : As soon as the blocker is resolved, we detect the change and resume modernization immediately, without waiting for the next maintenance window.



#### Internal errors

Internal Google service issues are reviewed by Google engineers, and they will resume your modernization if possible. Note that modernization could resume outside of a maintenance window, just like for user-actionable errors. To avoid this you may trigger a rollback.

If your modernization is stalled for more than 24 hours, and no compatibility gaps are present, contact Cloud Customer Care for more details or trigger a rollback if production workloads are impacted.

### Fleet-level conditions reference

Condition | Description  
---|---  
`MODERNIZATION_COMPATIBLE` | The fleet is compatible with the new control plane implementation.  
`MODERNIZATION_WILL_BE_SCHEDULED` | Google-driven modernization: All non-deferred fleets in the organization are compatible, and have been queued for scheduling.  
`MODERNIZATION_MODERNIZING` | Modernization is actively in progress for one or more clusters in the fleet.  
`MODERNIZATION_MODERNIZED` | All clusters have completed active modernization. The fleet is in the soak period.  
`MODERNIZATION_FINALIZED` | Modernization is complete and finalized. Legacy Istiod components will be removed. Rollback is no longer possible.  
`MODERNIZATION_ROLLING_BACK_FLEET` | A fleet-level rollback is in progress.  
  
### Cluster-level conditions reference

Condition | Description  
---|---  
`MODERNIZATION_SCHEDULED` | The cluster is scheduled for modernization on or after the date specified in the condition. If maintenance windows/exclusions are configured for your cluster, the date will indicate the target maintenance window.  
`MODERNIZATION_PREPARING` | Enabling the new control plane implementation.  
`MODERNIZATION_PREPARED` | The new control plane implementation is enabled. Workload migration has not started yet.  
`MODERNIZATION_MIGRATING_WORKLOADS` | The cluster is actively migrating workloads to the new control plane implementation.  
`MODERNIZATION_COMPLETED` | The cluster has completed modernization and is in the soaking period.  
`MODERNIZATION_STALLED` | Modernization is stalled due to an error (Customer-Triggered only). See condition details for resolution.  
`MODERNIZATION_ROLLING_BACK_CLUSTER` | The cluster is actively being rolled back.  
`MODERNIZATION_ABORTED` | The cluster was rolled back to the legacy control plane. Reported for a short time.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
