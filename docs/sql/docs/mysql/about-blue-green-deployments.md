---
url: https://docs.cloud.google.com/sql/docs/mysql/about-blue-green-deployments/
title: About blue-green deployments in Cloud SQL \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:02.923566+00:00
---

# About blue-green deployments in Cloud SQL  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/about-blue-green-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  About blue-green deployments in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides an overview of Cloud SQL blue-green deployments, which let you perform database updates, such as major version upgrades and hardware modifications, while minimizing downtime.

## Deployment intents and use cases

You can create a blue-green deployment with or without intent to perform a major version upgrade:

  * **Create with intent (major version upgrade):** upgrades your database engine to a newer major version. During deployment creation, Cloud SQL runs the major version upgrade pre-check API to verify compatibility before proceeding with the upgrade workflow.
  * **Create without intent (configuration or hardware changes):** stages modifications at the current database version. Use cases include changing machine types (CPU/RAM scaling), testing database flags, or evaluating storage modifications without upgrading the engine version.



## How blue-green deployments work

Cloud SQL blue-green deployments provide an automated workflow by staging changes in a temporary secondary environment before switching over live traffic.

During a blue-green deployment, Cloud SQL creates a separate staging environment (green) that mirrors your existing production environment (blue). The service maintains continuous logical replication from blue to green. You can thoroughly test application compatibility and performance on the green environment without affecting production traffic. When you're ready, you trigger a rapid _switchover_ that assigns the green environment to production read and write status with minimal application downtime (typically in seconds).

## Components of a blue-green deployment

A blue-green deployment consists of the following components:

  * **Blue environment (source):** your existing production environment that actively serves application traffic. It consists of the source read and write instance and any associated configuration.
  * **Green environment (target):** a temporary, isolated staging environment created by Cloud SQL as a clone of the blue environment. The green environment incorporates your requested changes (such as a newer database version) and stays synchronized with the blue environment by using continuous replication. Cloud SQL automatically names the green staging instance using the pattern `BLUE_INSTANCE_NAME-green-UNIQUE_ID` (where BLUE_INSTANCE_NAME is truncated to a maximum of 48 characters and UNIQUE_ID is an 8-character hexadecimal identifier).
  * **Switchover:** the planned, user-initiated process of converting the green environment to become the new production read and write instance. During switchover, Cloud SQL swaps connection endpoints so applications connect to the green environment with a brief connection drop (typically in seconds). Expected downtime during switchover varies based on the Cloud SQL edition:

    * **Cloud SQL Enterprise Plus edition:** switchover downtime is typically sub-second.
    * **Cloud SQL Enterprise edition:** switchover downtime is typically less than 60 seconds, depending on workload and replication lag.

Unlike an unplanned _failover_ (which is triggered automatically during an outage), a switchover is a controlled operation used for planned change management.

  * **Deletion:** the process of removing the blue-green deployment resource. Deletion behavior differs depending on whether switchover has occurred:

    * **Before switchover:** deleting the deployment removes the green staging instance and the deployment resource. Your blue production instance is unaffected and continues serving traffic.
    * **After switchover:** deleting the deployment removes the deployment metadata. By default, both the converted instance (green) and the blue instance are retained. You can optionally delete the blue instance to avoid ongoing charges.



## Deployment lifecycle and states

A blue-green deployment transitions through four distinct lifecycle phases:

  1. **Creation and staging (`PROVISIONING`):** when you request a blue-green deployment, Cloud SQL provisions a temporary green target instance that clones your blue production environment. In the case of a major version upgrade, Cloud SQL also runs the major version upgrade pre-check API to validate database compatibility before proceeding with the upgrade workflow. Cloud SQL applies the requested upgrade or configuration change to the green environment and starts continuous logical replication from blue to green.
  2. **Staging verification (`SWITCHOVER_READY` or `SWITCHOVER_NOT_READY`):** when initial replication finishes, the deployment enters `SWITCHOVER_READY` (or `SWITCHOVER_NOT_READY` if replication is broken or if errors occur). Blue continues serving live production traffic. You connect to green to run validation tests, verify application compatibility, and test query performance.
  3. **Switchover execution (`SWITCHOVER_IN_PROGRESS` or `SWITCHOVER_COMPLETED`):** when you trigger switchover, Cloud SQL runs safety pre-checks, swaps connection endpoints, and sets the green instance as your active production read and write instance (`SWITCHOVER_COMPLETED`), and transitions the blue instance to a standalone read and write instance. Active read and write operations are routed exclusively to the green instance and logical replication from blue to green is terminated. For more information, see [Perform a blue-green deployment switchover](https://docs.cloud.google.com/sql/docs/mysql/switchover-blue-green-deployment).
  4. **Deletion (`DELETING`):** when you finish testing or after you verify production operations, you delete the deployment resource. The deletion behavior differs depending on the deployment state:

     * **Before switchover (cancel):** if you decide not to proceed with the deployment or if verification issues arise, deleting the deployment removes the green staging instance and deletes the deployment metadata. The original blue production instance remains untouched and continues serving traffic without interruption.
     * **After switchover (clean up):** after switchover completes and you verify operations on the new production instance, deleting the deployment removes the deployment metadata. By default, both the new production instance (green) and the blue instance are retained as standalone read and write instances. You can optionally specify the `--delete-old-source` flag to permanently delete the blue instance and stop incurring charges for it.

For more information, see [Delete a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/delete-blue-green-deployment).




### Deployment resource states

When you inspect a blue-green deployment, the `state` field indicates its current lifecycle status:

  * **`PROVISIONING`:** the deployment is being created. For major version upgrades, Cloud SQL runs the pre-check API to validate compatibility before proceeding. Cloud SQL provisions the green environment, applies requested upgrades, and sets up continuous logical replication.
  * **`SWITCHOVER_READY`:** the green environment is provisioned, logical replication from blue to green is healthy, and the deployment is ready for switchover.
  * **`SWITCHOVER_NOT_READY`:** the deployment is provisioned, but switchover can't be initiated. This occurs if logical replication is broken or stopped, if initial replication hasn't completed, or if a paired node encountered an error.
  * **`SWITCHOVER_IN_PROGRESS`:** a switchover operation is actively running. Cloud SQL is swapping connection endpoints and converts the green instance to the active production read and write instance.
  * **`SWITCHOVER_COMPLETED`:** the switchover operation has completed successfully. The green instance is now your active production read and write instance, and the blue instance is retained as a standalone read and write instance.
  * **`DELETING`:** the deployment is being deleted. If deleting before switchover, Cloud SQL removes the green staging instance and deletes deployment metadata. If deleting after switchover, Cloud SQL removes the deployment metadata and optionally deletes the blue instance if the `--delete-old-source` flag is specified.
  * **`STATE_UNSPECIFIED`:** the state of the deployment is unknown.



### Switchover states and readiness

Switchover readiness depends on replication health and node status to protect your production database against data loss or extended downtime:

  * **Replication health and lag:** if logical replication between blue and green is broken, paused, or fails, the deployment status transitions to `SWITCHOVER_NOT_READY`. The deployment `state` and describe output don't report replication lag, and Cloud SQL doesn't evaluate replication lag as a precheck when determining deployment status. However, the switchover operation fails if replication lag is too high when switchover is initiated. To help ensure a successful switchover, make sure that replication lag is minimal before starting the switchover. You can monitor replication lag in [Cloud Monitoring](https://console.cloud.google.com/monitoring/dashboards/resourceList/cloudsql_database) (by checking metrics such as `replica_lag` in the [Cloud SQL metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudsql)) or directly on the green instance. For more information, see [Monitor replication lag](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag#metrics).
  * **Paired node status:** under `deploymentMappings`, each paired node reports its own node state (such as `PROVISIONED`, `UPGRADED`, `UPGRADE_FAILED`, `SWITCHOVER_IN_PROGRESS`, `SWITCHOVER_SUCCEEDED`, or `SWITCHOVER_FAILED`). If a paired node encounters an error (`UPGRADE_FAILED` or `SWITCHOVER_FAILED`), the overall deployment state transitions to `SWITCHOVER_NOT_READY`. If a switchover fails, routing remains on the blue instance with zero data loss.
  * **Troubleshooting switchover readiness:** if your deployment reports `SWITCHOVER_NOT_READY`, check the `errorDetail` field to diagnose replication or node errors. Before initiating switchover, make sure that replication lag is minimal and verify that active batch DDL operations or long-running write transactions on the blue instance are complete.



## Limitations

Review the following limitations before using blue-green deployments:

  * **Supported engines and versions:** Cloud SQL for MySQL instances on MySQL 5.7 and later are supported for configuration staging (create without intent). Major version upgrade targets (create with intent) are supported from MySQL 8.0 to 8.4. MySQL 8.0.18 isn't supported for blue-green deployments.
  * **Unsupported database engines:** Cloud SQL for PostgreSQL and Cloud SQL for SQL Server aren't supported.
  * **Instances with read replicas:** blue-green deployments don't support instances with read replicas.
  * **Unsupported network configurations:** blue-green deployments don't support Private Service Connect outbound configurations.
  * **IAM group authentication:** blue-green deployments are incompatible with MySQL [IAM group authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-group-auth) and can cause switchover failures.
  * **Network architecture requirement:** Cloud SQL instances must use the [new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture). Instances that use the old network architecture aren't supported.
  * **Binary logging requirement:** MySQL instances must have automated backups and binary logging enabled to support continuous logical replication to the green environment.
  * **Maintenance version requirement:** your blue source instance must run the latest maintenance version before you create a blue-green deployment. To check or update your instance maintenance version, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).
  * **Resource availability:** instance provisioning during blue-green deployment workflows—including creating the green staging instance and creating the blue instance after switchover—can be affected by compute resource constraints in the selected region or zone.
  * **Unplanned outages and failover:** blue-green deployment switchover is strictly a planned operation that requires a healthy, `RUNNING` blue source instance. The green staging instance functions as a specialized read replica; like standard read replicas, the green instance cannot be used as a failover target during an unplanned outage of the source instance. For automated outage recovery, configure your instance for [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability) or use a disaster recovery (DR) replica.



## Billing and pricing

There's no additional charge for using blue-green deployments. However, because a complete parallel green environment is provisioned during deployment, _you're billed standard rates for both the blue and green instances_ for the entire duration that both environments exist.

To avoid unnecessary charges, delete the deployment and associated instances:

  * **Before switchover:** if you cancel the deployment, delete the deployment to remove the green staging instance and stop charges for it.
  * **After switchover:** delete the deployment and specify the `--delete-old-source` flag to permanently delete the blue instance after you verify the new production instance. If you don't delete the blue instance, you continue to be billed for both instances.



## What's next

  * [Create and stage a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/create-blue-green-deployment).
  * [Describe and list blue-green deployments](https://docs.cloud.google.com/sql/docs/mysql/describe-blue-green-deployment).
  * [Switchover a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/switchover-blue-green-deployment).
  * [Delete a blue-green deployment](https://docs.cloud.google.com/sql/docs/mysql/delete-blue-green-deployment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
