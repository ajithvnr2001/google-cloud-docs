---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade/
title: Upgrading Apigee hybrid to version 1.12 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:18:50.005667+00:00
---

# Upgrading Apigee hybrid to version 1.12  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrading Apigee hybrid to version 1.12 Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/upgrade.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/upgrade.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/upgrade.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/upgrade.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/upgrade.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/upgrade.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/upgrade.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/upgrade.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/upgrade.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/upgrade.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/upgrade.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/upgrade.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/upgrade.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/upgrade.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/upgrade.html)



This procedure covers upgrading from Apigee hybrid version 1.11.x to Apigee hybrid version 1.12.4 and from previous releases of hybrid 1.12.x to version 1.12.4. 

Use the same procedures for minor version upgrades (for example version 1.11 to 1.12) and for patch release upgrades (for example 1.12.0 to 1.12.4). 

If you are upgrading from Apigee hybrid version 1.10 or older, you must first upgrade to hybrid version 1.11 before upgrading to version 1.12.4. See the instructions for [Upgrading Apigee hybrid to version 1.11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade). 

## Changes from Apigee hybrid v1.11

Apigee hybrid version 1.12 introduces the following changes that impact the upgrade process. For a complete list of features in v1.12 see the [hybrid v1.12.0 Release Notes](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes). 

  * **Cassandra 4.x** : Starting in version 1.12, Apigee hybrid uses Cassandra version 4+. **Important:** Because of the database change, you cannot roll back the upgraded `apigee-datastore` component. Therefore, it is critical that you back up your Cassandra database and your hybrid installation before upgrading. If you need to roll back your upgrade, consider the following scenarios: 
    * **Cassandra not yet upgraded:** You can roll back all changes. 
    * **Cassandra upgraded and all Cassandra pods are healthy:** You can roll back changes to all components except `apigee-datastore`. Your v1.11.x installation will continue to work with a v1.12 instance of your `apigee-datastore` running Cassandra v4. 
    * **Cassandra upgraded and the Cassandra pods are in an unhealthy state:** You must uninstall hybrid v1.12 and restore your v.11 installation from a backup. 
  * **`apigeectl` deprecation:** Starting in version 1.12, Apigee hybrid only supports Helm for installing and managing your hybrid installation. **Caution** : `apigeectl` is [deprecated](https://cloud.google.com/terms/deprecation) as of April 17, 2024. The `apigeectl` tool is not supported for Apigee hybrid v1.12. Support for `apigeectl` for Apigee hybrid v1.10 and v1.11 will end on April 17, 2025. For more information, see [apigeectl deprecation](https://docs.cloud.google.com/apigee/docs/deprecations/apigeectl).**Important:** If you are managing v1.11 with `apigeectl`, you must first migrate your v1.11 installation to use Helm before upgrading to version 1.12. Follow the instructions in [Migrate Apigee hybrid to Helm charts from `apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/helm-migration). 
  * A new suite of metrics for monitoring Apigee proxies and target endpoints is now available. For hybrid v1.12, `ProxyV2` and `TargetV2` monitored resources will no longer be in use by default. All proxy and target metrics will be published to `Proxy` and `Target` monitored resources.

To continue to emit metrics to `ProxyV2` and `TargetV2` monitored resources, set `metrics.disablePrometheusPipeline` to `true` in the `overrides.yaml`. 

If you have metrics-based alerts configured, confirm the use of the correct metrics for your hybrid installation. For more information, see [Metric-based alerts](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications#new-metrics). 

  * **Stricter class instantiation checks** : Starting in version 1.12.4, Apigee hybrid, the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) now includes additional security during Java class instantiation. The enhanced security measure prevents the deployment of policies that directly or indirectly attempt actions that require permissions that are not allowed. 

In the most cases, existing policies will continue to function as expected without any issues. However, there is a possibility that policies relying on third-party libraries, or those with custom code that indirectly triggers operations requiring elevated permissions, could be affected. 

**Important:** To test your installation, follow the procedure in Validate policies after upgrade to 1.12.4 to validate policy behavior. 



##  Considerations before starting an upgrade to version 1.12 

### Cassandra considerations

Upgrading from Apigee hybrid version 1.11 to version 1.12 includes an upgrade of the Cassandra database from version 3.11.x to version 4.x. While the Cassandra upgrade is handled as part of the Apigee hybrid upgrade procedure, please plan for the following considerations: 

  * The Cassandra version upgrade will happen in the background and will take place on 1 pod (or Cassandra node) at a time so plan for a reduced database capacity during the upgrade.
  * Scale your Cassandra capacity and make sure the disk utilization is near or below 50% before you start upgrading.
  * Validate and test your Cassandra backup and restore procedures.
  * Back up the Cassandra data in your hybrid version 1.11 installation before you start upgrading and validate your backups.
  * Upgrading `apigee-datastore` will result in a temporary increase in CPU consumption due to post-upgrade tasks performed by `Cassandra`
  * Once you have upgraded the `apigee-datastore` (Cassandra) component, you cannot roll that component back to the previous version. There are two scenarios for rolling back an upgrade to hybrid v1.12 after upgrading the `apigee-datastore` component: 
    * If the `apigee-datastore` component is in a good state but other components require a roll back, you can roll back those other components individually. **Note:** You will not be able to add regions or scale Cassandra nodes while running components of different hybrid versions.
    * If the `apigee-datastore` component is in a bad state, you must restore from a v1.11 backup into a v1.11 installation. **Note:** You cannot mix versions when restoring. You must restore a backup taken in a v1.11 installation into a v1.11 installation.



###  Considerations before upgrading a single-region installation 

If you need to roll back to a previous version of Apigee hybrid, the process may require downtime. Therefore, if you are upgrading a single-region installation, you may want to create a second region and then upgrade only one region at a time in the following sequence: 

  1. Add a second region to your existing installation using the same hybrid version. See [Multi-region deployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/multi-region) in the version 1.11 documentation. 
  2. Backup and validate data from the first region before starting an upgrade. See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-backup-overview) in the version 1.11 documentation.
  3. Upgrade the newly added region to hybrid 1.12.
  4. Switch the traffic to the new region and validate traffic.
  5. Once validated, upgrade the older region with hybrid 1.12.
  6. Switch all the traffic back to the older region and validate traffic.
  7. Decommission the new region.



###  Considerations before upgrading a multi-region installation 

Apigee recommends the following sequence for upgrading a multi-region installation: 

  1. Backup and validate data from each region before starting upgrade.
  2. Upgrade the Hybrid version in one region and make sure all the pods are in a running state to validate the upgrade.
  3. Validate traffic in the newly upgraded region.
  4. Upgrade each subsequent region only after validating the traffic on the previous region.
  5. In case of the potential need to rollback an upgrade in a multi-region deployment, prepare to switch traffic away from failed regions, consider adding enough capacity in the region where traffic will be diverted to handle traffic for both regions.



## Prerequisites

Before upgrading to hybrid version 1.12, make sure your installation meets the following requirements: 

  * An Apigee hybrid version 1.11 installation managed with Helm. 
    * If you are managing your hybrid installation with `apigeectl`, you must first migrate your clusters to Helm management. See [Migrate Apigee hybrid to Helm from `apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-migration) in the hybrid v1.11 documentation.
    * If your hybrid installation is running a version older than v1.11, you must upgrade to version 1.11 before upgrading to v1.12. see [Upgrading Apigee hybrid to version 1.11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade). 
  * Helm version v3.14.2+.
  * `kubectl` version 1.27, 1.28, or 1.29 (recommended).
  * cert-manager version v1.13.0. If needed, you will upgrade cert-manager in the Prepare to upgrade to version section below.



## Limitations

Keep the following limitations in mind when planning your upgrade from Apigee hybrid version 1.11 to version 1.12. Planning can help reduce the need for downtime if you need to roll back or restore after the upgrade. 

  * Backups from Hybrid 1.12 cannot be restored in Hybrid 1.11 and vice versa, due to incompatibility between the two versions.
  * You cannot scale datastore pods during the upgrade to version 1.12. Address your scaling needs in all regions before you start to upgrade your hybrid installation.
  * In a single region hybrid installation, you cannot roll back the datastore component once the datastore upgrade process has finished. You cannot roll a Cassandra 4.x datastore back to a Cassandra 3.x datastore. This will require restoring from your most recent back up of the Cassandra 3.x data (from your hybrid version 1.11 installation).
  * Deleting or adding a region is not supported during upgrade. In a multi-region upgrade, you must complete the upgrade of all regions before you can add or delete regions.



##  Upgrading to version 1.12.4 overview 

Upgrading to Apigee hybrid version 1.12 may require downtime. 

When upgrading the Apigee controller to version 1.12.4, all Apigee deployments undergo a rolling restart. To minimize downtime in production hybrid environments during a rolling restart, make sure you are running at least two clusters (in the same or different region/data center). Divert all production traffic to a single cluster and take the cluster you are about to upgrade offline, and then proceed with the upgrade process. Repeat the process for each cluster.

Apigee recommends upgrading all clusters as soon as possible to reduce the chances of production impact. There is no time limit on when all remaining clusters must be upgraded after the first one is upgraded. However, until all remaining clusters are upgraded the following operations will be impacted:

  * Cassandra backup and restore cannot work with mixed versions. For example, a backup from Hybrid 1.11 cannot be used to restore a Hybrid 1.12 instance.
  * Cassandra data streaming will not work between mixed Hybrid versions. Therefore, your Cassandra clusters cannot scale horizontally.
  * Region expansion and decommissioning will be impacted, because these operations depend on Cassandra data streaming.

**Note:** Management plane changes do not need to be suspended during an upgrade. Any required suspension to management plane changes are included in the upgrade instructions.

The procedures for upgrading Apigee hybrid are organized in the following sections: 

  1. Prepare to upgrade. 
     * Backup Cassandra.
     * Backup your hybrid installation directories.
  2. Install hybrid runtime version 1.12.4.



##  Prepare to upgrade to version 1.12 

### Backup cassandra

  * Backup your Cassandra database in all applicable regions and validate data in your hybrid version 1.11 installation before starting upgrade. See [Monitoring backups](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/monitor-cassandra-backups) in the version 1.11 documentation.
  * Restart all the Cassandra pods in the cluster before you start the upgrade process, so any lingering issues can surface. 

To restart and test the Cassandra pods, delete each pod individually, one pod at a time, and then validate that it comes back in a running state and that the readiness probe passes: 

    1. List the cassandra pods: 
           
           kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra

For example:
           
           kubectl get pods -n apigee -l app=apigee-cassandra
           NAME                         READY   STATUS    RESTARTS   AGE
           apigee-cassandra-default-0   1/1     Running   0          2h
           apigee-cassandra-default-1   1/1     Running   0          2h
           apigee-cassandra-default-2   1/1     Running   0          2h
           
           . . .

    2. Delete a pod: 
           
           kubectl delete pod -n APIGEE_NAMESPACE CASSANDRA_POD_NAME

For example:
           
           kubectl delete pod -n apigee apigee-cassandra-default-0

    3. Check the status by listing the cassandra pods again: 
           
           kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra

For example:
           
           kubectl get pods -n apigee -l app=apigee-cassandra
           NAME                         READY   STATUS    RESTARTS   AGE
           apigee-cassandra-default-0   1/1     Running   0          16s
           apigee-cassandra-default-1   1/1     Running   0          2h
           apigee-cassandra-default-2   1/1     Running   0          2h
           
           . . .

  * Apply the last known override file again to make sure there are no changes made to it so you can use the same configuration to upgrade to hybrid version 1.12.
  * Ensure that all Cassandra nodes in all regions are in the `UN` (_Up / Normal_) state. If any Cassandra node is in a different state, address that first before starting the upgrade. 

You can validate the state of your Cassandra nodes with the following commands: 

    1. List the cassandra pods: 
           
           kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra

For example:
           
           kubectl get pods -n apigee -l app=apigee-cassandra
           NAME                         READY   STATUS    RESTARTS   AGE
           apigee-cassandra-default-0   1/1     Running   0          2h
           apigee-cassandra-default-1   1/1     Running   0          2h
           apigee-cassandra-default-2   1/1     Running   0          2h
           apigee-cassandra-default-3   1/1     Running   0          16m
           apigee-cassandra-default-4   1/1     Running   0          14m
           apigee-cassandra-default-5   1/1     Running   0          13m
           apigee-cassandra-default-6   1/1     Running   0          9m
           apigee-cassandra-default-7   1/1     Running   0          9m
           apigee-cassandra-default-8   1/1     Running   0          8m

    2. Check the state the nodes for each Cassandra pod with the `kubectl nodetool status` command: 
           
           kubectl -n APIGEE_NAMESPACE exec -it CASSANDRA_POD_NAME -- nodetool status

For example: 
           
           kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool status
           Datacenter: us-east1
           ====================
           Status=Up/Down
           |/ State=Normal/Leaving/Joining/Moving
           --  Address      Load        Tokens       Owns (effective)  Host ID                               Rack
           UN  10.16.2.6    690.17 KiB  256          48.8%             b02089d1-0521-42e1-bbed-900656a58b68  ra-1
           UN  10.16.4.6    705.55 KiB  256          51.6%             dc6b7faf-6866-4044-9ac9-1269ebd85dab  ra-1
           UN  10.16.11.11  674.36 KiB  256          48.3%             c7906366-6c98-4ff6-a4fd-17c596c33cf7  ra-1
           UN  10.16.1.11   697.03 KiB  256          49.8%             ddf221aa-80aa-497d-b73f-67e576ff1a23  ra-1
           UN  10.16.5.13   703.64 KiB  256          50.9%             2f01ac42-4b6a-4f9e-a4eb-4734c24def95  ra-1
           UN  10.16.8.15   700.42 KiB  256          50.6%             a27f93af-f8a0-4c88-839f-2d653596efc2  ra-1
           UN  10.16.11.3   697.03 KiB  256          49.8%             dad221ff-dad1-de33-2cd3-f1.672367e6f  ra-1
           UN  10.16.14.16  704.04 KiB  256          50.9%             1feed042-a4b6-24ab-49a1-24d4cef95473  ra-1
           UN  10.16.16.1   699.82 KiB  256          50.6%             beef93af-fee0-8e9d-8bbf-efc22d653596  ra-1




###  Back up your hybrid installation directories 

  1. These instructions use the environment variable APIGEE_HELM_CHARTS_HOME for the directory in your file system where you have installed the Helm charts. If needed, change directory into this directory and define the variable with the following command: 

###  Linux 
         
         export APIGEE_HELM_CHARTS_HOME=$PWD
         echo **$APIGEE_HELM_CHARTS_HOME**

###  Mac OS 
         
         export APIGEE_HELM_CHARTS_HOME=$PWD
         echo **$APIGEE_HELM_CHARTS_HOME**

###  Windows 
         
         set APIGEE_HELM_CHARTS_HOME=%CD%
         echo %APIGEE_HELM_CHARTS_HOME%

  2. Make a backup copy of your version 1.11 `$APIGEE_HELM_CHARTS_HOME/` directory. You can use any backup process. For example, you can create a `tar` file of your entire directory with: 
         
         tar -czvf **$APIGEE_HELM_CHARTS_HOME** /../apigee-helm-charts-v1.11-backup.tar.gz **$APIGEE_HELM_CHARTS_HOME**

  3. Back up your Cassandra database following the instructions in [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-backup-overview).
  4. If you are using service cert files (`.json`) in your overrides to authenticate service accounts, make sure your service account cert files reside in the correct Helm chart directory. Helm charts cannot read files outside of each chart directory. 

This step is not required if you are using Kubernetes secrets or Workload Identity to authenticate service accounts.

The following table shows the destination for each service account file, depending on your type of installation:

### Prod

Service account | Default filename | Helm chart directory  
---|---|---  
`apigee-cassandra` | `PROJECT_ID-apigee-cassandra.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-datastore/`  
`apigee-logger` | `PROJECT_ID-apigee-logger.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-telemetry/`  
`apigee-mart` | `PROJECT_ID-apigee-mart.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-org/`  
`apigee-metrics` | `PROJECT_ID-apigee-metrics.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-telemetry/`  
`apigee-runtime` | `PROJECT_ID-apigee-runtime.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-env`  
`apigee-synchronizer` | `PROJECT_ID-apigee-synchronizer.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-env/`  
`apigee-udca` | `PROJECT_ID-apigee-udca.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-org/`  
`apigee-watcher` | `PROJECT_ID-apigee-watcher.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-org/`  
  
### Non-prod

Make a copy of the `apigee-non-prod` service account file in each of the following directories:

Service account | Default filename | Helm chart directories  
---|---|---  
`apigee-non-prod` | `PROJECT_ID-apigee-non-prod.json` | `$APIGEE_HELM_CHARTS_HOME/apigee-datastore/`  
`$APIGEE_HELM_CHARTS_HOME/apigee-telemetry/`  
`$APIGEE_HELM_CHARTS_HOME/apigee-org/`  
`$APIGEE_HELM_CHARTS_HOME/apigee-env/`  
  5. Make sure that your TLS certificate and key files (`.crt`, `.key`, and/or `.pem`) reside in the `$APIGEE_HELM_CHARTS_HOME/apigee-virtualhost/` directory. 



###  Upgrade your Kubernetes version 

Check your Kubernetes platform version and if needed, upgrade your Kubernetes platform to a version that is supported by both hybrid 1.11 and hybrid 1.12. Follow your platform's documentation if you need help. 

### _Click to expand a list of supported platforms_

| 1.10 ![not supported](https://docs.cloud.google.com/static/apigee/docs/images/not-supported.svg)(3) | 1.11 | 1.12  
---|---|---|---  
GKE on Google Cloud | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)  
GKE on AWS | 1.13.x (K8s v1.24.x)   
1.14.x (K8s v1.25.x)   
1.26.x(12)   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x (K8s v1.25.x)   
1.26.x(12)   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) |  1.26.x(12)   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)  
GKE on Azure | 1.13.x   
1.14.x   
1.26.x(12)   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x   
1.26.x(12)   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x(12)   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)  
Google Distributed Cloud (software only) on VMware (1) (13) | 1.13.x   
1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(12)   
1.29.x(≥ 1.12.1)  
Google Distributed Cloud (software only) on bare metal (1) | 1.13.x   
1.14.x (K8s v1.25.x)   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.27.x(12)(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.14.x   
1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(12)(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.15.x (K8s v1.26.x)   
1.16.x (K8s v1.27.x)   
1.28.x(12)   
1.29.x(≥ 1.12.1)  
EKS(7) | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)  
AKS(7) | 1.24.x   
1.25.x   
1.26.x   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) | 1.25.x   
1.26.x   
1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | 1.26.x   
1.27.x   
1.28.x   
1.29.x(≥ 1.12.1)  
OpenShift(7) | 4.11   
4.12   
4.14(≥ 1.10.5)   
4.15(≥ 1.10.5) | 4.12   
4.13   
4.14   
4.15(≥ 1.11.2)   
4.16(≥ 1.11.2) | 4.12   
4.13   
4.14   
4.15   
4.16(≥ 1.12.1)  
Rancher Kubernetes Engine (RKE) |  v1.26.2+rke2r1   
1.27.x(≥ 1.10.5)   
1.28.x(≥ 1.10.5) |  v1.26.2+rke2r1   
v1.27.x   
1.28.x(≥ 1.11.2)   
1.29.x(≥ 1.11.2) | v1.26.2+rke2r1  
v1.27.x  
  
1.28.x   
1.29.x(≥ 1.12.1)  
VMware Tanzu |  N/A |  N/A | v1.26.x   
  
### Components

| 1.10 | 1.11 | 1.12  
Cloud Service Mesh |  1.17.x(10) |  1.18.x(10) |  1.19.x(10)  
JDK |  JDK 11 |  JDK 11 |  JDK 11  
cert-manager |  1.10.x  
1.11.x  
1.12.x  |  1.11.x  
1.12.x  
1.13.x  |  1.11.x  
1.12.x  
1.13.x   
Cassandra |  3.11 |  3.11 |  4.0  
Kubernetes | 1.24.x  
1.25.x  
1.26.x  
| 1.25.x  
1.26.x  
1.27.x  
| 1.26.x  
1.27.x  
1.28.x  
  
kubectl |  |  | 1.27.x  
1.28.x  
1.29.x  
  
Helm | 3.10+ | 3.10+ | 3.14.2+  
Secret Store CSI driver |  | 1.3.4 | 1.4.1  
Vault |  | 1.13.x | 1.15.2  
**(1) On Anthos on-premises (Google Distributed Cloud) version 1.13, follow these instructions to avoid conflict with `cert-manager`: [Conflicting cert-manager installation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#conflicting-cert-manager-installation)** **(2) Support available with Apigee hybrid version 1.7.2 and newer**.  **(3) The official EOL dates for Apigee hybrid versions 1.10 and older have been reached. Regular monthly patches are no longer available. These releases are no longer officially supported except for customers with explicit and official exceptions for continued support. Other customers must upgrade**.  **(4) Anthos on-premises (Google Distributed Cloud) versions 1.12 and earlier are out of support. See the Distributed Cloud on bare metal [Version Support Policy](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/getting-support#version-support) and the Distributed Cloud on VMware [supported versions list](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#supported-versions).** **(5) Google Distributed Cloud on bare metal or VMware [ requires Cloud Service Mesh 1.14](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support#112) or later. We recommend that you upgrade to hybrid v1.8 and switch to Apigee ingress gateway which no longer requires you to install Cloud Service Mesh on your hybrid cluster.** **(6) Support available with Apigee hybrid version 1.8.4 and newer**.  **(7) Not supported with Apigee hybrid version 1.8.4 and newer**.  **(8) Support available with Apigee hybrid version 1.7.6 and newer**.  **(9) Not supported with Apigee hybrid version 1.8.5 and newer**.  **(10) Cloud Service Mesh is automatically installed with Apigee hybrid 1.9 and newer**.  **(11) Support available with Apigee hybrid version 1.9.2 and newer**.  **(12) GKE on AWS version numbers now reflect the Kubernetes versions. See [GKE Enterprise version and upgrade support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#gke_multi_cloud) for version details and recommended patches**.  **(13) Vault is not certified on Google Distributed Cloud for VMware. ** **(14) Support available with Apigee hybrid version 1.10.5 and newer**.  **(15) Support available with Apigee hybrid version 1.11.2 and newer**.  **(16) Support available with Apigee hybrid version 1.12.1 and newer**.   
  
###  About attached clusters 

For Apigee hybrid versions 1.7.x and older, you must use [GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached) if you want to run Apigee hybrid in a multi-cloud context on Elastic Kubernetes Service (EKS), Azure Kubernetes Service (AKS), or another supported third-party Kubernetes service provider. Cluster attachment allows Google to measure the usage of Cloud Service Mesh. 

For Apigee hybrid version 1.8.x, GKE attached clusters are required if you are using Cloud Service Mesh for your ingress gateway. If you are using Apigee ingress gateway, attached clusters are optional. 

**Note:** Hybrid installations are not currently supported on Autopilot clusters. 

##  Install the hybrid 1.12.4 runtime 

**Caution:** Do not create new environments during the upgrade process.

### Prepare for the Helm charts upgrade

This upgrade procedure assumes you are using the same namespace and service accounts for the upgraded installation. If you are making any configuration changes, be sure to reflect those changes in your overrides file before installing the Helm charts.

  1. Pull the Apigee Helm charts. 

Apigee hybrid charts are hosted in [Google Artifact Registry](https://docs.cloud.google.com/artifact-registry):

`oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts`

Using the `pull` command, copy all of the Apigee hybrid Helm charts to your local storage with the following command: 
         
         export **CHART_REPO** =oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts
         export **CHART_VERSION** =1.12.4
         helm pull **$CHART_REPO** /apigee-operator --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-datastore --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-env --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-ingress-manager --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-org --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-redis --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-telemetry --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-virtualhost --version **$CHART_VERSION** --untar
         

  2. Upgrade cert-manager if needed. 

If you need to upgrade your cert-manager version, install the new version with the following command:
         
         kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml
         

  3. Install the updated Apigee CRDs: **Note:** From this step onwards, all commands should be run under the chart repo root directory. **Note:** This is the only supported method for installing Apigee CRDs. Do not use `kubectl apply` without `-k`, do not omit `--server-side`. **Note:** This step requires elevated cluster permissions. 
     1. Use the `kubectl` dry-run feature by running the following command:
            
            kubectl apply -k  apigee-operator/etc/crds/default/ --server-side --force-conflicts --validate=false --dry-run
            

     2. After validating with the dry-run command, run the following command:
            
            kubectl apply -k  apigee-operator/etc/crds/default/ --server-side --force-conflicts --validate=false
            

     3. Validate the installation with the `kubectl get crds` command: 
            
            kubectl get crds | grep apigee

Your output should look something like the following:
            
            apigeedatastores.apigee.cloud.google.com                    2023-10-09T14:48:30Z
            apigeedeployments.apigee.cloud.google.com                   2023-10-09T14:48:30Z
            apigeeenvironments.apigee.cloud.google.com                  2023-10-09T14:48:31Z
            apigeeissues.apigee.cloud.google.com                        2023-10-09T14:48:31Z
            apigeeorganizations.apigee.cloud.google.com                 2023-10-09T14:48:32Z
            apigeeredis.apigee.cloud.google.com                         2023-10-09T14:48:33Z
            apigeerouteconfigs.apigee.cloud.google.com                  2023-10-09T14:48:33Z
            apigeeroutes.apigee.cloud.google.com                        2023-10-09T14:48:33Z
            apigeetelemetries.apigee.cloud.google.com                   2023-10-09T14:48:34Z
            cassandradatareplications.apigee.cloud.google.com           2023-10-09T14:48:35Z
            

  4. Check the labels on the cluster nodes. By default, Apigee schedules data pods on nodes with the label `cloud.google.com/gke-nodepool=apigee-data` and runtime pods are scheduled on nodes with the label `cloud.google.com/gke-nodepool=apigee-runtime`. You can customize your node pool labels in the `overrides.yaml` file. 

For more information, see [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/configure-dedicated-nodes). 




### Install the Apigee hybrid Helm charts

**Note:** Before executing any of the Helm upgrade/install commands, use the Helm dry-run feature by adding `--dry-run` at the end of the command. See `helm -h` to list supported commands, options, and usage. 

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Upgrade the Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm upgrade -h` for details 

Dry run:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           --force \
           -f OVERRIDES_FILE
         

Verify Apigee Operator installation:
         
         helm ls -n apigee-system
         
         
         NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                   APP VERSION
         operator   apigee-system   3          2023-06-26 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.12.4   1.12.4

Verify it is up and running by checking its availability:
         
         kubectl -n apigee-system get deploy apigee-controller-manager
         
         
         NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-controller-manager   1/1     1            1           7d20h

  3. Upgrade the Apigee datastore: 

Dry run:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --force \
           -f OVERRIDES_FILE
         

Verify `apigeedatastore` is up and running by checking its state:
         
         kubectl -n apigee get apigeedatastore default
         
         
         NAME      STATE       AGE
         default   running    2d

  4. Upgrade Apigee telemetry: 

Dry run:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --force \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its state:
         
         kubectl -n apigee get apigeetelemetry apigee-telemetry
         
         
         NAME               STATE     AGE
         apigee-telemetry   running   2d

  5. Upgrade Apigee Redis: 

Dry run:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --force \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its state:
         
         kubectl -n apigee get apigeeredis default
         
         
         NAME      STATE     AGE
         default   running   2d

  6. Upgrade Apigee ingress manager: 

Dry run:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --force \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking its availability:
         
         kubectl -n apigee get deployment apigee-ingressgateway-manager
         
         
         NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-ingressgateway-manager   2/2     2            2           2d

  7. Upgrade the Apigee organization: 

Dry run:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE \
           --dry-run
         

Upgrade the chart:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

**Note:** For installations migrated from `apigeectl` to Helm, use: 
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --force \
           -f OVERRIDES_FILE
         

Verify it is up and running by checking the state of the respective org:
         
         kubectl -n apigee get apigeeorg
         
         
         NAME                      STATE     AGE
         apigee-org1-xxxxx          running   2d

  8. Upgrade the environment. 

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME:

Dry run:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE \
           --dry-run
         

     * ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart. In hybrid v1.10, it is usually `apigee-env-ENV_NAME`. In Hybrid v1.11 and newer it is usually ENV_NAME.
     * ENV_NAME is the name of the environment you are upgrading.
     * OVERRIDES_FILE is your new overrides file for v.1.12.4

Upgrade the chart:
    
    helm upgrade ENV_RELEASE_NAME apigee-env/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --set env=ENV_NAME \
      -f OVERRIDES_FILE
    

**Note:** For installations migrated from `apigeectl` to Helm, use: 
    
    helm upgrade ENV_RELEASE_NAME apigee-env/ \
      --install \
      --namespace APIGEE_NAMESPACE \
      --set env=ENV_NAME \
      --force \
      -f OVERRIDES_FILE
    

Verify it is up and running by checking the state of the respective env:
    
    kubectl -n apigee get apigeeenv
    
    
    NAME                          STATE       AGE   GATEWAYTYPE
    apigee-org1-dev-xxx            running     2d

  9. Upgrade the environment groups (`virtualhosts`). 
     1. You must upgrade one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP_NAME. Repeat the following commands for each env group mentioned in the overrides.yaml file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --set envgroup=ENV_GROUP_NAME \
              -f OVERRIDES_FILE \
              --dry-run
            

ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. In hybrid v1.10, it is usually `apigee-virtualhost-ENV_GROUP_NAME`. In Hybrid v1.11 and newer it is usually ENV_GROUP_NAME.

Upgrade the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --set envgroup=ENV_GROUP_NAME \
              -f OVERRIDES_FILE
            

**Note:** For installations migrated from `apigeectl` to Helm, use: 
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --set envgroup=ENV_GROUP_NAME \
              --force \
              -f OVERRIDES_FILE
            

**Note:** ENV_GROUP_RELEASE_NAME must be unique within the `apigee` namespace. 

For example, if you have a an _environment_ named `prod` and an _environment group_ named `prod`, set the value of ENV_GROUP_RELEASE_NAME to something unique, like `prod-envgroup`. 

     2. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls env group related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n apigee get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2d
            
            kubectl -n apigee get ar
            
            
            NAME                                        STATE     AGE
            apigee-org1-dev-egroup-xxxxxx                running   2d




## Validate policies after upgrade to 1.12.4

Use this procedure to validate the behavior of the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) after upgrading from 1.12.3 or earlier to 1.12.4 or later.

  1. **Check whether the Java JAR files request unnecessary permissions**. 

After the policy is deployed, check the runtime logs to see if the following log message is present: `"Failed to load and initialize class ..."`. If you observe this message, it suggests that the deployed JAR requested unnecessary permissions. To resolve this issue, investigate the Java code and update the JAR file.

  2. **Investigate and update the Java code**. 

Review any Java code (including dependencies) to identify the cause of potentially unallowed operations. When found, modify the source code as required.

  3. **Test policies with the security check enabled**. 

In a _non-production environment_ , enable the security check flag and redeploy your policies with an updated JAR. To set the flag: 

     * In the `apigee-env/values.yaml` file, set `conf_security-secure.constructor.only` to `true` under `runtime:cwcAppend:`. For example: 
           
           # Apigee Runtime
           runtime:
             cwcAppend:
               conf_security-secure.constructor.only: true

     * Update the `apigee-env` chart for the environment to apply the change. For example: 
           
           helm upgrade ENV_RELEASE_NAME apigee-env/ \
             --install \
             --namespace APIGEE_NAMESPACE \
             --set env=ENV_NAME \
             -f OVERRIDES_FILE

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts class="external"](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

If the log message `"Failed to load and initialize class ..."` is still present, continue modifying and testing the JAR until the log message no longer appears.

  4. **Enable the security check in the production environment**. 

After you have thoroughly tested and verified the JAR file in the non-production environment, enable the security check in your production environment by setting the flag `conf_security-secure.constructor.only` to `true` and updating the `apigee-env` chart for the production environment to apply the change. 


**Congratulations!** You have upgraded to Apigee hybrid version 1.12.4. To test your upgrade, call a proxy against the new installation. For an example, see [Step 10: Deploy an API proxy](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-deploy-proxy) in the Apigee hybrid 1.12 installation guide. 

##  Rolling back to a previous version 

This section is divided into sections depending on the state of your `apigee-datastore` component after upgrading to Apigee hybrid version 1.12. There are procedures for single region or multi-region rollback with the `apigee-datastore` component in a good state and procedures for recovery or restore from a backup when `apigee-datastore` is in a bad state. 

###  Single region rollback and recovery 

#### Rolling back when `apigee-datastore` is in a good state

This procedure explains how to roll back every Apigee hybrid component from v1.12 to v1.11 _except`apigee-datastore`_. The v1.12 `apigee-datastore` component is backwards compatible with hybrid v1.11 components. 

**Warning:** Rolling back `apigee-datastore` is not possible. Data incompatibility between different versions of the Cassandra database prevents rolling back to the previous version.

To roll back your single region installation to version 1.11: 

  1. Before starting rollback, validate all the pods are in a running state: 
         
         kubectl get pods -n APIGEE_NAMESPACE
         
         kubectl get pods -n apigee-system

  2. Validate the release of components using helm: 
         
         helm -n APIGEE_NAMESPACE list
         
         helm -n apigee-system list

For example
         
         helm -n apigee list
         NAME              NAMESPACE   REVISION   UPDATED                                   STATUS     CHART                           APP VERSION
         datastore         apigee      2          2024-03-29 17:08:07.917848253 +0000 UTC   deployed   apigee-datastore-1.12.0         **1.12.0**
         ingress-manager   apigee      2          2024-03-29 17:21:02.917333616 +0000 UTC   deployed   apigee-ingress-manager-1.12.0   **1.12.0**
         redis             apigee      2          2024-03-29 17:19:51.143728084 +0000 UTC   deployed   apigee-redis-1.12.0             **1.12.0**
         telemetry         apigee      2          2024-03-29 17:16:09.883885403 +0000 UTC   deployed   apigee-telemetry-1.12.0         **1.12.0**
         myhybridorg       apigee      2          2024-03-29 17:21:50.899855344 +0000 UTC   deployed   apigee-org-1.12.0               **1.12.0**

  3. Roll back each component _except`apigee-datastore`_ with the following commands: 
     1. Create the following environment variable: 
        * PREVIOUS_HELM_CHARTS_HOME: The directory where the previous Apigee hybrid Helm charts are installed. This is the version you are rolling back to.
     2. Roll back the virtualhosts. Repeat the following command for each environment group mentioned in the overrides file. 
            
            helm upgrade ENV_GROUP_RELEASE_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-virtualhost/ \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=ENV_GROUP_NAME \
              -f PREVIOUS_OVERRIDES_FILE
            

ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. In hybrid v1.10, it is usually `apigee-virtualhost-ENV_GROUP_NAME`. In Hybrid v1.11 and newer it is usually ENV_GROUP_NAME.

     3. Roll back Envs. Repeat the following command for each environment mentioned in the overrides file. 
            
            helm upgrade apigee-env-ENV_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=ENV_NAME \
              -f PREVIOUS_OVERRIDES_FILE
            

ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart. In hybrid v1.10, it is usually `apigee-env-ENV_NAME`. In Hybrid v1.11 and newer it is usually ENV_NAME.

Verify it is up and running by checking the state of the respective env:
            
            kubectl -n apigee get apigeeenv
            
            
            NAME                  STATE     AGE   GATEWAYTYPE
            apigee-org1-dev-xxx   running   2d

     4. Roll back Org: 
            
            helm upgrade ORG_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify it is up and running by checking the state of the respective org:
            
            kubectl -n apigee get apigeeorg
            
            
            NAME                STATE     AGE
            apigee-org1-xxxxx   running   2d

     5. Roll back the Ingress Manager: 
            
            helm upgrade ingress-manager $PREVIOUS_HELM_CHARTS_HOME/apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify it is up and running by checking its availability:
            
            kubectl -n apigee get deployment apigee-ingressgateway-manager
            
            
            NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-ingressgateway-manager   2/2     2            2           2d

     6. Roll back Redis: 
            
            helm upgrade redis $PREVIOUS_HELM_CHARTS_HOME/apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify it is up and running by checking its state:
            
            kubectl -n apigee get apigeeredis default
            
            
            NAME      STATE     AGE
            default   running   2d

     7. Roll back Apigee Telemetry: 
            
            helm upgrade telemetry $PREVIOUS_HELM_CHARTS_HOME/apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify it is up and running by checking its state:
            
            kubectl -n apigee get apigeetelemetry apigee-telemetry
            
            
            NAME               STATE     AGE
            apigee-telemetry   running   2d

     8. Roll back the Apigee Controller: 
            
            helm upgrade operator $PREVIOUS_HELM_CHARTS_HOME/apigee-operator/ \
              --install \
              --namespace apigee-system \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE

Verify Apigee Operator installation:
            
            helm ls -n apigee-system
            
            
            NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                   APP VERSION
            operator   apigee-system   3          2023-06-26 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.12.4   1.12.4

Verify it is up and running by checking its availability:
            
            kubectl -n apigee-system get deploy apigee-controller-manager
            
            
            NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-controller-manager   1/1     1            1           7d20h

     9. Roll back the Apigee hybrid CRDs: 
            
            kubectl apply -k  $PREVIOUS_HELM_CHARTS_HOME/apigee-operator/etc/crds/default/ --server-side --force-conflicts --validate=false
            

  4. Validate all the pods are either in a running or completed state: 
         
         kubectl get pods -n APIGEE_NAMESPACE
         
         kubectl get pods -n apigee-system

  5. Validate the release of all components. All components should be in the previous version except for datastore: 
         
         helm -n APIGEE_NAMESPACE list
         
         helm -n apigee-system list

For example
         
         helm -n apigee  list
         NAME              NAMESPACE  REVISION  UPDATED                                  STATUS    CHART                          APP VERSION
         **datastore**         apigee     2         2024-03-29 18:47:55.979671057 +0000 UTC  deployed  apigee-datastore-1.12.0        **1.12.0**
         ingress-manager   apigee     3         2024-03-14 19:14:57.905700154 +0000 UTC  deployed  apigee-ingress-manager-1.11.0  **1.11.0**
         redis             apigee     3         2024-03-14 19:15:49.406917944 +0000 UTC  deployed  apigee-redis-1.11.0            **1.11.0**
         telemetry         apigee     3         2024-03-14 19:17:04.803421424 +0000 UTC  deployed  apigee-telemetry-1.11.0        **1.11.0**
         myhybridorg       apigee     3         2024-03-14 19:13:17.807673713 +0000 UTC  deployed  apigee-org-1.11.0              **1.11.0**




#### Restoring when `apigee-datastore` is not in a good state

If the upgrade of the `apigee-datastore` component was not successful, you cannot roll back `apigee-datastore` from version 1.12 to version 1.11. Instead you must restore from a backup made of a v1.11 installation. Use the following sequence to restore your previous version. 

  1. If you do not have an active installation of Apigee hybrid version 1.11 (for example in another region), create a new installation of v1.11 using your backed up charts and overrides files. See the [Apigee hybrid version 1.11 installation instructions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/big-picture).
  2. Restore the v1.11 region (or new installation) from your backup following the instructions in: 
     * **Cloud Storage Interface (CSI) backups:** [Cassandra CSI backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-csi-backup-restore#restore-a-backup).
     * **Non-CSI backups:** [Restoring in a single region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/restore-cassandra-single-region). 
  3. Verify traffic to the restored installation
  4. **Optional:** Remove the version 1.12 installation following the instructions in [Uninstall hybrid runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/uninstall).



###  Multi-region rollback and recovery 

#### Rolling back when `apigee-datastore` is in a good state

**Note:** > Use this rollback method to rollback from an upgraded hybrid region to the previous hybrid version. This method is intended to recover from a failed upgrade when **not all the regions have not been upgraded yet**.

This procedure explains how to roll back every Apigee hybrid component from v1.12 to v1.11 _except`apigee-datastore`_. The v1.12 `apigee-datastore` component is backwards compatible with hybrid v1.11 components. 

  1. Before starting rollback, validate all the pods are in a running state: 
         
         kubectl get pods -n APIGEE_NAMESPACE
         
         kubectl get pods -n apigee-system

  2. Ensure that all Cassandra nodes in all regions are in the `UN` (_Up / Normal_) state. If any Cassandra node is in a different state, address that first before starting the upgrade process. 

You can validate the state of your Cassandra nodes with the following commands: 

     1. List the cassandra pods: 
            
            kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra

For example:
            
            kubectl get pods -n apigee -l app=apigee-cassandra
            NAME                         READY   STATUS    RESTARTS   AGE
            apigee-cassandra-default-0   1/1     Running   0          2h
            apigee-cassandra-default-1   1/1     Running   0          2h
            apigee-cassandra-default-2   1/1     Running   0          2h
            apigee-cassandra-default-3   1/1     Running   0          16m
            apigee-cassandra-default-4   1/1     Running   0          14m
            apigee-cassandra-default-5   1/1     Running   0          13m
            apigee-cassandra-default-6   1/1     Running   0          9m
            apigee-cassandra-default-7   1/1     Running   0          9m
            apigee-cassandra-default-8   1/1     Running   0          8m

     2. Check the state the nodes for each Cassandra pod with the `kubectl nodetool status` command: 
            
            kubectl -n APIGEE_NAMESPACE exec -it CASSANDRA_POD_NAME -- nodetool -u JMX_USER -pw JMX_PASSWORD

For example: 
            
            kubectl -n apigee exec -it apigee-cassandra-default-0 -- nodetool -u jmxuser -pw JMX_PASSWORD status
            Datacenter: us-east1
            ====================
            Status=Up/Down
            |/ State=Normal/Leaving/Joining/Moving
            --  Address      Load        Tokens   Owns (effective)   Host ID                                Rack
            UN  10.16.2.6    690.17 KiB  256      48.8%              b02089d1-0521-42e1-bbed-900656a58b68   ra-1
            UN  10.16.4.6    705.55 KiB  256      51.6%              dc6b7faf-6866-4044-9ac9-1269ebd85dab   ra-1
            UN  10.16.11.11  674.36 KiB  256      48.3%              c7906366-6c98-4ff6-a4fd-17c596c33cf7   ra-1
            UN  10.16.1.11   697.03 KiB  256      49.8%              ddf221aa-80aa-497d-b73f-67e576ff1a23   ra-1
            UN  10.16.5.13   703.64 KiB  256      50.9%              2f01ac42-4b6a-4f9e-a4eb-4734c24def95   ra-1
            UN  10.16.8.15   700.42 KiB  256      50.6%              a27f93af-f8a0-4c88-839f-2d653596efc2   ra-1
            UN  10.16.11.3   697.03 KiB  256      49.8%              dad221ff-dad1-de33-2cd3-f1.672367e6f   ra-1
            UN  10.16.14.16  704.04 KiB  256      50.9%              1feed042-a4b6-24ab-49a1-24d4cef95473   ra-1
            UN  10.16.16.1   699.82 KiB  256      50.6%              beef93af-fee0-8e9d-8bbf-efc22d653596   ra-1

If not all Cassandra pods are in a `UN` state, follow the instructions in Remove DOWN nodes from Cassandra Cluster. 

  3. Navigate to the directory where the previous Apigee hybrid Helm charts are installed 
  4. Change the context to the region that was upgraded 
         
         kubectl config use-context UPGRADED_REGION_CONTEXT
             

  5. Validate all the pods are in a running state: 
         
         kubectl get pods -n APIGEE_NAMESPACE
         
         kubectl get pods -n apigee-system

  6. Use the helm command to make sure all the releases were upgraded to Hybrid v1.12: 
         
         helm -n APIGEE_NAMESPACE list
         
         helm -n apigee-system list

For example
         
         helm -n apigee list
         NAME             NAMESPACE  REVISION  UPDATED                                  STATUS    CHART                          APP VERSION
         datastore        apigee     2         2024-03-29 17:08:07.917848253 +0000 UTC  deployed  apigee-datastore-1.12.0        **1.12.0**
         ingress-manager  apigee     2         2024-03-29 17:21:02.917333616 +0000 UTC  deployed  apigee-ingress-manager-1.12.0  **1.12.0**
         redis            apigee     2         2024-03-29 17:19:51.143728084 +0000 UTC  deployed  apigee-redis-1.12.0            **1.12.0**
         telemetry        apigee     2         2024-03-29 17:16:09.883885403 +0000 UTC  deployed  apigee-telemetry-1.12.0        **1.12.0**
         myhybridorg      apigee     2         2024-03-29 17:21:50.899855344 +0000 UTC  deployed  apigee-org-1.12.0              **1.12.0**

  7. Roll back each component _except`apigee-datastore`_ with the following commands: 
     1. Create the following environment variable: 
        * PREVIOUS_HELM_CHARTS_HOME: The directory where the previous Apigee hybrid Helm charts are installed. This is the version you are rolling back to.
     2. Roll back the virtualhosts. Repeat the following command for each environment group mentioned in the overrides file. 
            
            helm upgrade ENV_GROUP_RELEASE_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-virtualhost/ \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=ENV_GROUP_NAME \
              -f PREVIOUS_OVERRIDES_FILE
            

ENV_GROUP_RELEASE_NAME is the name with which you previously installed the `apigee-virtualhost` chart. In hybrid v1.10, it is usually `apigee-virtualhost-ENV_GROUP_NAME`. In Hybrid v1.11 and newer it is usually ENV_GROUP_NAME.

     3. Roll back Envs. Repeat the following command for each environment mentioned in the overrides file. 
            
            helm upgrade apigee-env-ENV_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=ENV_NAME \
              -f PREVIOUS_OVERRIDES_FILE
            

ENV_RELEASE_NAME is the name with which you previously installed the `apigee-env` chart. In hybrid v1.10, it is usually `apigee-env-ENV_NAME`. In Hybrid v1.11 and newer it is usually ENV_NAME.

Verify each env is up and running by checking the state of the respective env:
            
            kubectl -n apigee get apigeeenv
            
            
            NAME                  STATE     AGE   GATEWAYTYPE
            apigee-org1-dev-xxx   running   2d

     4. Roll back Org: 
            
            helm upgrade ORG_NAME $PREVIOUS_HELM_CHARTS_HOME/apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify it is up and running by checking the state of the respective org:
            
            kubectl -n apigee get apigeeorg
            
            
            NAME                STATE     AGE
            apigee-org1-xxxxx   running   2d

     5. Roll back the Ingress Manager: 
            
            helm upgrade ingress-manager $PREVIOUS_HELM_CHARTS_HOME/apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify it is up and running by checking its availability:
            
            kubectl -n apigee get deployment apigee-ingressgateway-manager
            
            
            NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-ingressgateway-manager   2/2     2            2           2d

     6. Roll back Redis: 
            
            helm upgrade redis $PREVIOUS_HELM_CHARTS_HOME/apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify it is up and running by checking its state:
            
            kubectl -n apigee get apigeeredis default
            
            
            NAME      STATE     AGE
            default   running   2d

     7. Roll back Apigee Telemetry: 
            
            helm upgrade telemetry $PREVIOUS_HELM_CHARTS_HOME/apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify it is up and running by checking its state:
            
            kubectl -n apigee get apigeetelemetry apigee-telemetry
            
            
            NAME               STATE     AGE
            apigee-telemetry   running   2d

     8. Roll back the Apigee Controller: 
            
            helm upgrade operator $PREVIOUS_HELM_CHARTS_HOME/apigee-operator/ \
              --install \
              --namespace apigee-system \
              --atomic \
              -f PREVIOUS_OVERRIDES_FILE
            

Verify Apigee Operator installation:
            
            helm ls -n apigee-system
            
            
            NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                   APP VERSION
            operator   apigee-system   3          2023-06-26 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.12.4   1.12.4

Verify it is up and running by checking its availability:
            
            kubectl -n apigee-system get deploy apigee-controller-manager
            
            
            NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-controller-manager   1/1     1            1           7d20h

     9. Roll back the Apigee hybrid CRDs: 
            
            kubectl apply -k  $PREVIOUS_HELM_CHARTS_HOME/apigee-operator/etc/crds/default/ --server-side --force-conflicts --validate=false
            

  8. Validate the release of all components. All components should be in the previous version except for `datastore`: 
         
         helm -n APIGEE_NAMESPACE list
         
         helm -n apigee-system list

For example
         
         helm -n apigee  list
         NAME              NAMESPACE  REVISION  UPDATED                                  STATUS    CHART                          APP VERSION
         **datastore**         apigee     2         2024-03-29 18:47:55.979671057 +0000 UTC  deployed  apigee-datastore-1.12.0        **1.12.0**
         ingress-manager   apigee     3         2024-03-14 19:14:57.905700154 +0000 UTC  deployed  apigee-ingress-manager-1.11.0  **1.11.0**
         redis             apigee     3         2024-03-14 19:15:49.406917944 +0000 UTC  deployed  apigee-redis-1.11.0            **1.11.0**
         telemetry         apigee     3         2024-03-14 19:17:04.803421424 +0000 UTC  deployed  apigee-telemetry-1.11.0        **1.11.0**
         myhybridorg       apigee     3         2024-03-14 19:13:17.807673713 +0000 UTC  deployed  apigee-org-1.11.0              **1.11.0**
         

At this point all the releases except `datastore` have been rolled back to the previous version. 


**Important:** Currently, the Cassandra datastore is partially upgraded. We recommend attempting to upgrade again by addressing any issues encountered during the previous upgrade and retrying the process. If it is not feasible to attempt another upgrade, the recommendation is to recover the datastore using the instructions in Recovering a multi-region installation to a previous version.

###  Recovering a multi-region installation to a previous version 

Recover the region where upgrade failed in a multi region upgrade by removing references to it from multiple region installations. This method is only possible when there is at least 1 live region on Hybrid 1.11. The v1.12 datastore is compatible with v 1.11 components.

To recover failed region(s) from a healthy region, perform the following steps:

  1. Redirect the API traffic from the impacted region(s) to the good working region. Plan the capacity accordingly to support the diverted traffic from failed region(s).
  2. Decommission the impacted region. For each impacted region, follow the steps outlined in [Decommission a hybrid region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/decommission-region). Wait for decommissioning to complete before moving on to the next step. 
  3. Clean up the failed region following the instructions in Recover a region from a failed upgrade. 
  4. Recover the impacted region. To recover, create a new region, as described in [Multi-region deployment on GKE, GKE on-prem, and AKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/multi-region). 



###  Restoring a multi-region installation from a backup with `apigee-datastore` in a bad state 

If the upgrade of the `apigee-datastore` component was not successful, you cannot roll back from version 1.12 to version 1.11. Instead you must restore from a backup made of a v1.11 installation. Use the following sequence to restore your previous version. 

**Tip:** To minimize downtime in multi-region installations, Apigee recommends rebuilding and restoring one region at a time.

  1. If you do not have an active installation of Apigee hybrid version 1.11 (for example in another region), create a new installation of v1.11 using your backed up charts and overrides files. See the [Apigee hybrid version 1.11 installation instructions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/big-picture).
  2. Restore the v1.11 region (or new installation) from your backup following the instructions in: 
     * **Cloud Storage Interface (CSI) backups:** [Cassandra CSI backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-csi-backup-restore#restore-a-backup).
     * **Non-CSI backups:** [Restoring in multiple regions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/restore-cassandra-multi-region). 
  3. Verify traffic to the restored installation
  4. For multi-region installations, rebuild and restore the next region. See the instructions in [Restoring from a backup in Restoring in multiple regions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-multi-region#restore-nongcs). 
  5. Remove the version 1.12 installation following the instructions in [Uninstall hybrid runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/uninstall).



##  APPENDIX: Recover a region from a failed upgrade 

Remove a Datacenter if the upgrade fails from 1.11 to 1.12. 

  1. Validate Cassandra cluster status from a live region: 
     1. Switch the kubectl context to the region to be removed: 
            
            kubectl config use-context CONTEXT_OF_LIVE_REGION

     2. List the cassandra pods: 
            
            kubectl get pods -n APIGEE_NAMESPACE -l app=apigee-cassandra

For example:
            
            kubectl get pods -n apigee -l app=apigee-cassandra
            NAME                 READY   STATUS    RESTARTS   AGE
            apigee-cassandra-default-0   1/1     Running   0          2h
            apigee-cassandra-default-1   1/1     Running   0          2h
            apigee-cassandra-default-2   1/1     Running   0          2h

     3. Exec into one of the cassandra pods: 
            
            kubectl exec -it -n CASSANDRA_POD_NAME -- /bin/bash

     4. Check the status of the Cassandra cluster: 
            
            nodetool -u JMX_USER -pw JMX_PASSWORD status

The output should look something like the following: 
            
            Datacenter: dc-1
            ================
            Status=Up/Down
            |/ State=Normal/Leaving/Joining/Moving
            --  Address      Load        Tokens       Owns (effective)  Host ID                               Rack
            UN  10.48.12.16  813.84 KiB  256          100.0%            a6340ad9-37ba-4ec8-a8c2-f7b7ac931807  ra-1
            UN  10.48.14.16  859.89 KiB  256          100.0%            39f03c51-e387-4dac-8360-6d8732e690a7  ra-1
            UN  10.48.0.18   888.95 KiB  256          100.0%            0d57df49-52e4-4c01-832d-d9df845ab732  ra-1
            

     5. Describe the cluster to verify that you only see IPs of Cassandra pods from the live region and all of them on the same schema version: 
            
            nodetool -u JMX_USER -pw JMX_PASSWORD describecluster

The output should look something like the following: 
            
            nodetool -u JMX_USER -pw JMX_PASSWORD describecluster
            
            Schema versions:
                4bebf2de-0582-31b4-9c5f-e36f60127e1b: [10.48.14.16, 10.48.12.16, 10.48.0.18]
            

  2. Cleanup Cassandra keyspace replication: 
     1. Get the `user-setup` job and delete it. A new `user-setup` job will be created immediately. 
            
            kubectl get jobs -n APIGEE_NAMESPACE

For example: 
            
            kubectl get jobs -n apigee
              NAME                                                           COMPLETIONS   DURATION   AGE
              apigee-cassandra-schema-setup-myhybridorg-8b3e61d          1/1           6m35s      3h5m
              apigee-cassandra-schema-val-myhybridorg-8b3e61d-28499150   1/1           10s        9m22s
             **apigee-cassandra-user-setup-myhybridorg-8b3e61d            0/1           21s        21s**
            
            
            kubectl delete jobs USER_SETUP_JOB_NAME -n APIGEE_NAMESPACE

The output should show the new job starting: 
            
            kubectl delete jobs apigee-cassandra-user-setup-myhybridorg-8b3e61d -n apigee
            
              apigee-cassandra-user-setup-myhybridorg-8b3e61d-wl92b         0/1     Init:0/1    0               1s
              

     2. Validate Cassandra keyspace replication settings by creating a client container following the instructions in [Create the client container](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-the-client-container). 
     3. Get all the keyspaces. Exec into cassandra-client pod and then starting a cqlsh client: 
            
            kubectl exec -it -n APIGEE_NAMESPACE cassandra-client -- /bin/bash

Connect to the Cassandra server with `ddl user` as it has permissions required to run the following commands:
            
            cqlsh apigee-cassandra-default.apigee.svc.cluster.local -u DDL_USER -p DDL_PASSWORD --ssl

Get the keyspaces:
            
            select * from system_schema.keyspaces;

The output should look like following where `dc-1` is the live DC:
            
            select * from system_schema.keyspaces;
            
             keyspace_name            | durable_writes | replication
            --------------------------+----------------+--------------------------------------------------------------------------------
               kvm_myhybridorg_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                          system_auth |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                        system_schema |           True |                        {'class': 'org.apache.cassandra.locator.LocalStrategy'}
             quota_myhybridorg_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
             cache_myhybridorg_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
               rtc_myhybridorg_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                   system_distributed |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                               system |           True |                        {'class': 'org.apache.cassandra.locator.LocalStrategy'}
                               perses |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                        system_traces |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
               kms_myhybridorg_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
            
            (11 rows)
            

     4. If for some reason the `user-setup` job continues to error out and validation is failing, use the following commands to correct the replication in keyspaces. **Caution:** Use the following commands with extreme care.
            
            kubectl exec -it -n APIGEE_NAMESPACE cassandra-client -- /bin/bash

Connect to the Cassandra server with `ddl user` as it has permissions required to run the following commands:
            
            cqlsh apigee-cassandra-default.apigee.svc.cluster.local -u DDL_USER -p DDL_PASSWORD --ssl

Get the keyspaces:
            
            select * from system_schema.keyspaces;

Use the keyspace names from the command above and replace them in the following examples 
            
            alter keyspace quota_myhybridorg_hybrid WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};
            alter keyspace kms_myhybridorg_hybrid WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};
            alter keyspace kvm_myhybridorg_hybrid WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};
            alter keyspace cache_myhybridorg_hybrid WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};
            alter keyspace perses_myhybridorg_hybrid WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};
            alter keyspace rtc_myhybridorg_hybrid WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};
            alter keyspace system_auth WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};
            alter keyspace system_distributed WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};
            alter keyspace system_traces WITH replication = {'class': 'NetworkTopologyStrategy', 'LIVE_DC_NAME':'3'};

     5. Validate that all the keyspaces are replicating in the right region with the following `cqlsh` command: 
            
            select * from system_schema.keyspaces;

For example:
            
            select * from system_schema.keyspaces;
            
             keyspace_name           | durable_writes | replication
            -------------------------+----------------+--------------------------------------------------------------------------------
            kvm_myhybridorg_hybrid   |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                      system_auth    |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                    system_schema    |           True |                        {'class': 'org.apache.cassandra.locator.LocalStrategy'}
            quota_myhybridorg_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
            cache_myhybridorg_hybrid |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
            rtc_myhybridorg_hybrid   |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
               system_distributed    |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                           system    |           True |                        {'class': 'org.apache.cassandra.locator.LocalStrategy'}
                           perses    |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
                    system_traces    |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
            kms_myhybridorg_hybrid   |           True | {'class': 'org.apache.cassandra.locator.NetworkTopologyStrategy', 'dc-1': '3'}
            
            (11 rows)




At this stage you have completely removed all the references for the dead DC from the Cassandra cluster.

##  APPENDIX: Remove DOWN nodes from Cassandra Cluster 

Use this procedure when you are rolling back a multi-region installation and not all Cassandra pods are in an Up / Normal (`UN`) state. 

  1. Exec into one of the cassandra pods: 
         
         kubectl exec -it -n CASSANDRA_POD_NAME -- /bin/bash

  2. Check the status of the Cassandra cluster: 
         
         nodetool -u JMX_USER -pw JMX_PASSWORD status

  3. Validate that the node is actually Down (`DN`). Exec into Cassandra pod in a region where the Cassandra pod is not able to come up. 
         
         Datacenter: dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address      Load        Tokens  Owns (effective)  Host ID                               Rack
         UN  10.48.12.16  1.15 MiB    256     100.0%            a6340ad9-37ba-4ec8-a8c2-f7b7ac931807  ra-1
         UN  10.48.0.18   1.21 MiB    256     100.0%            0d57df49-52e4-4c01-832d-d9df845ab732  ra-1
         UN  10.48.14.16  1.18 MiB    256     100.0%            39f03c51-e387-4dac-8360-6d8732e690a7  ra-1
         
         Datacenter: us-west1
         ====================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address      Load        Tokens  Owns (effective)  Host ID                               Rack
         **DN  10.8.4.4     432.42 KiB  256     100.0%            cd672398-5c45-4c88-a424-86d757951e53  rc-1**
         UN  10.8.19.6    5.8 MiB     256     100.0%            84f771f3-3632-4155-b27f-a67125d73bc5  rc-1
         UN  10.8.21.5    5.74 MiB    256     100.0%            f6f21b70-348d-482d-89fa-14b7147a5042  rc-1
         

  4. Remove the reference to the down (`DN`) node. From the above example we are going to remove reference for host `10.8.4.4`
         
         kubectl exec -it -n apigee apigee-cassandra-default-2 -- /bin/bash
          nodetool -u JMX_USER -pw JMX_PASSWORD removenode HOST_ID
         

  5. After the reference is removed, terminate the pod. The new Cassandra pod should come up and join the cluster 
         
         kubectl delete pod -n POD_NAME

  6. Validate that the new Cassandra pod has joined the cluster. 
         
         Datacenter: dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address      Load        Tokens  Owns (effective)  Host ID                               Rack
         UN  10.48.12.16  1.16 MiB    256     100.0%            a6340ad9-37ba-4ec8-a8c2-f7b7ac931807  ra-1
         UN  10.48.0.18   1.22 MiB    256     100.0%            0d57df49-52e4-4c01-832d-d9df845ab732  ra-1
         UN  10.48.14.16  1.19 MiB    256     100.0%            39f03c51-e387-4dac-8360-6d8732e690a7  ra-1
         
         Datacenter: us-west1
         ====================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address      Load        Tokens  Owns (effective)  Host ID                               Rack
         UN  10.8.19.6    5.77 MiB    256     100.0%            84f771f3-3632-4155-b27f-a67125d73bc5  rc-1
         UN  10.8.4.5     246.99 KiB  256     100.0%            0182e675-eec8-4d68-a465-69211b621601  rc-1
         UN  10.8.21.5    5.69 MiB    256     100.0%            f6f21b70-348d-482d-89fa-14b7147a5042  rc-1




At this point you can proceed with the upgrade or roll back of the remaining regions of the cluster. 

##  APPENDIX: Troubleshooting: `apigee-datastore` in a stuck state after rollback 

Use this procedure when you have rolled back `apigee-datastore` to hybrid 1.11 after upgrade, and it is in a stuck state. 

  1. Before correcting the datastore controller state again, validate that it is in a `releasing` state and the pods are not coming up along with Cassandra cluster state. 
     1. Validate using the Helm command that datastore was rolled back: 
            
            helm -n APIGEE_NAMESPACE list

For example:
            
            helm -n apigee list
            NAME              NAMESPACE  REVISION  UPDATED                                   STATUS    CHART                              APP VERSION
            datastore         apigee     3         2024-04-04 22:15:08.792539892 +0000 UTC   deployed   **apigee-datastore-1.11.0**           1.11.0
            ingress-manager   apigee     1         2024-04-02 22:24:27.564184968 +0000 UTC   deployed   apigee-ingress-manager-1.12.0     1.12.0
            redis             apigee     1         2024-04-02 22:23:59.938637491 +0000 UTC   deployed   apigee-redis-1.12.0               1.12.0
            telemetry         apigee     1         2024-04-02 22:23:39.458134303 +0000 UTC   deployed   apigee-telemetry-1.12             1.12.0
            myhybridorg       apigee     1         2024-04-02 23:36:32.614927914 +0000 UTC   deployed   apigee-org-1.12.0                 1.12.0
            

     2. Get the status of the Cassandra pods: 
            
            kubectl get pods -n APIGEE_NAMESPACE

For example:
            
            kubectl get pods -n apigee
            NAME                         READY   STATUS             RESTARTS      AGE
            apigee-cassandra-default-0   1/1     Running            0             2h
            apigee-cassandra-default-1   1/1     Running            0             2h
            apigee-cassandra-default-2   0/1     CrashLoopBackOff   4 (13s ago)   2m13s
            

     3. Validate that `apigeeds` controller is stuck in releasing state: 
            
            kubectl get apigeeds -n APIGEE_NAMESPACE

For example:
            
            kubectl get apigeeds -n apigee
            NAME      STATE       AGE
            default   releasing   46h

     4. Validate Cassandra nodes status (notice that one node is in a `DN` state which is the node stuck in `CrashLoopBackOff` state): 
            
            kubectl exec apigee-cassandra-default-0 -n APIGEE_NAMESPACE  -- nodetool -u JMX_USER -pw JMX_PASSWORD status

For example:
            
            kubectl exec apigee-cassandra-default-0 -n apigee  -- nodetool -u jmxuser -pw JMX_PASSWORD status
            Defaulted container "apigee-cassandra" out of: apigee-cassandra, apigee-cassandra-ulimit-init (init)
            Datacenter: us-west1
            ====================
            Status=Up/Down
            |/ State=Normal/Leaving/Joining/Moving
            --   Address       Load       Tokens   Owns (effective)   Host ID                               Rack
            UN   10.68.7.28    2.12 MiB   256      100.0%             4de9df37-3997-43e7-8b5b-632d1feb14d3  rc-1
            UN   10.68.10.29   2.14 MiB   256      100.0%             a54e673b-ec63-4c08-af32-ea6c00194452  rc-1
            **DN   10.68.6.26    5.77 MiB   256      100.0%             0fe8c2f4-40bf-4ba8-887b-9462159cac45   rc-1**
            

  2. Upgrade the datastore using the 1.12 charts. **Note:** The controller will go in to `releasing` state again but this time it will create pods with the images for Hybrid 1.12 which will come up and Cassandra will join the cluster and become `UN` (UP/NORMAL).
         
         helm upgrade datastore APIGEE_HELM_1.12.0_HOME/apigee-datastore/   --install   --namespace APIGEE_NAMESPACE   -f overrides.yaml

  3. Validate all the pods are `Running` and Cassandra cluster is healthy again. 
     1. Validate all the pods are `READY` again: 
            
            kubectl get pods -n APIGEE_NAMESPACE

For example:
            
            kubectl get pods -n apigee
            NAME                         **READY**   STATUS    RESTARTS   AGE
            apigee-cassandra-default-0   **1/1**     Running   0          29h
            apigee-cassandra-default-1   **1/1**     Running   0          29h
            apigee-cassandra-default-2   **1/1**     Running   0          60m

     2. Validate Cassandra cluster status: 
            
            kubectl exec apigee-cassandra-default-0 -n APIGEE_NAMESPACE  -- nodetool -u JMX_USER -pw JMX_PASSWORD status

For example:
            
            kubectl exec apigee-cassandra-default-0 -n apigee  -- nodetool -u jmxuser -pw JMX_PASSWORD status
            Datacenter: us-west1
            ====================
            Status=Up/Down
            |/ State=Normal/Leaving/Joining/Moving
            --   Address       Load      Tokens   Owns (effective)   Host ID                                Rack
            **UN**   10.68.4.15    2.05 MiB  256      100.0%             0fe8c2f4-40bf-4ba8-887b-9462159cac45   rc-1
            **UN**   10.68.7.28    3.84 MiB  256      100.0%             4de9df37-3997-43e7-8b5b-632d1feb14d3   rc-1
            **UN**   10.68.10.29   3.91 MiB  256      100.0%             a54e673b-ec63-4c08-af32-ea6c00194452   rc-1
              

     3. Validate status of the `apigeeds` controller: 
            
            kubectl get apigeeds -n APIGEE_NAMESPACE

For example:
            
            kubectl get apigeeds -n apigee
            NAME      STATE     AGE
            default   **running**   2d1h




At this point you have fixed the datastore and it should be in a `running` state. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
