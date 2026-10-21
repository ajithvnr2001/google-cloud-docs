---
url: https://docs.cloud.google.com/composer/docs/composer-2/perform-failover-tests/
title: Perform failover tests for highly resilient environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:09.688861+00:00
---

# Perform failover tests for highly resilient environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/perform-failover-tests/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Perform failover tests for highly resilient environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/perform-failover-tests "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | Managed Airflow (Legacy Gen 1)

This page describes how to perform database and cluster failover tests for [highly resilient environments](https://docs.cloud.google.com/composer/docs/composer-2/set-up-highly-resilient-environments).

Failover tests for your environment simulate a complete outage of a zone in a data center. In such a scenario, a zonal outage of a cluster and a zonal outage of a database might happen at the same time. By performing the two failover tests, you can monitor how your highly resilient environment performs a failover and check how this affects your DAGs and tasks.

## Before you begin

  * To perform failover tests, your Google Account must have the following roles and permissions:

    * `composer.environments.update` permission. See [Access control with IAM](https://docs.cloud.google.com/composer/docs/composer-2/access-control#user-account) for a list of roles with this permission.

    * **Kubernetes Engine Cluster Admin** (`roles/container.clusterAdmin`) role to run `kubectl` commands on the environment's cluster. As an alternative, you can provision [Kubernetes RBAC roles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) directly in GKE.

  * If you use [authorized networks](https://docs.cloud.google.com/composer/docs/composer-2/configure-authorized-networks), and your then you must run `kubectl` commands from a machine that can access the GKE cluster's control plane endpoint. Depending on how you set up access to your environment's control plane endpoint, you can use several options. For more information, see [Running commands on a private IP environment](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli#private-ip). 




## Check that your environment is healthy

Make sure to perform failover tests only on healthy environments. To check that your environment is healthy:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Monitoring** tab.

  4. Make sure that all health metrics are green.




## Perform a database failover test

You can perform a database failover test, which simulates a zonal outage, by triggering it with a Google Cloud CLI command. For example, you might want to do it to measure the amount of time it takes for your environment's database to switch to another zone.

**Important:** The database failover test represents a zonal outage **only for the database of your environment**. During a zonal outage, the cluster of your environment might also be affected. You can perform a separate failover test for your environment's cluster.**Note:** The database failover test is not intended for troubleshooting; it is not possible to fix issues with the database component of an environment with the failover test.

To perform a database failover test for your environment:

  1. Make sure that your environment is healthy.

  2. Get the primary zone of your environment's database:
         
         gcloud composer environments fetch-database-properties \
             ENVIRONMENT_NAME \
             --location LOCATION
         

Replace the following:

     * `ENVIRONMENT_NAME`: the name of your Cloud Composer environment.
     * `LOCATION`: the region where the environment is located.

Example:
    
    gcloud composer environments fetch-database-properties \
        example-environment \
        --location us-central1
    

  3. Start the database failover test:
         
         gcloud composer environments database-failover \
             ENVIRONMENT_NAME \
             --location LOCATION
         

Replace the following:

     * `ENVIRONMENT_NAME`: the name of your Cloud Composer environment.
     * `LOCATION`: the region where the environment is located.

Example:
    
    gcloud composer environments database-failover \
        example-environment \
        --location us-central1
    

  4. Wait until the database failover test is finished. The process can take up to 3 minutes.

  5. Check that the primary zone of your environment's database is changed:
         
         gcloud composer environments fetch-database-properties \
             ENVIRONMENT_NAME \
             --location LOCATION
         

  6. Check your environment's health metrics to make sure that your environment is healthy.

  7. Your environment's database becomes ready for another failover when the **Database available for failover** (`composer.googleapis.com/environment/database/available_for_failover`) environment metric becomes `True`. For more information about viewing your environment's metrics in Cloud Monitoring, see [Monitor environments](https://docs.cloud.google.com/composer/docs/composer-2/monitor-environments#view-metrics).




## Perform your environment's cluster failover test

You can perform a failover test for your environment's cluster, which simulates a zonal outage. For example, you might want to do it to measure the amount of time it takes for your environment to switch to another zone.

**Important:** The environment's cluster failover test represents a zonal outage **only for the cluster of your environment**. During a zonal outage, the database of your environment might also be affected. You can perform a separate failover test for your environment's database.

### Check that your environment is healthy

Before starting the test, make sure that your environment is healthy.

### Configure credentials for your environment's cluster

To obtain cluster credentials:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. Click **View cluster details**.

  5. Click **Connect**.

  6. Copy and execute the displayed Google Cloud CLI command.

For example:
         
         gcloud container clusters get-credentials \
           us-central1-exam-db23ee12-gke \
           --region us-central1 \
           --project example-project
         




### Inspect your environment's cluster

Check zones and nodes where the workloads run in your environment's cluster. You use this information to simulate a zonal outage later. You can also run these commands again while you perform the failover test to see how your environment's cluster performs the failover.

  1. Check nodes and zones:
         
         kubectl get nodes \
           -o=custom-columns=NAME:.metadata.name,NODE:.metadata.labels.topology\\.gke\\.io/zone
         

  2. Check pods:
         
         kubectl get pods --all-namespaces \
         -o=custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName \
         --field-selector metadata.namespace!=kube-system
         

  3. View more detailed information about pods:
         
         kubectl get pods --all-namespaces -o wide \
         --field-selector metadata.namespace!=kube-system
         




### Drain nodes

Choose a zone where you want to simulate an outage. If you perform the cluster failover test together with the database failover test, you might want to choose the primary zone of your environment's [highly available Cloud SQL instance](https://docs.cloud.google.com/composer/docs/composer-2/set-up-highly-resilient-environments#about-database). For example, if the primary Cloud SQL instance runs in `us-central1-a` then you can simulate an outage in the whole `us-central1-a` zone by first performing the database failover test and then the cluster's failover test in `us-central1-a`.

The following command simulates a set of nodes becoming unavailable in a specific zone. It forcefully evicts Pods from nodes in the specified zone and prevents rescheduling Pods on these nodes. Because new Pods can't be scheduled, new nodes are added to the cluster.

**Important:** New nodes that are added to the cluster **might be located in the zone where a failure is simulated**. This behavior does not invalidate the failover procedure, which tests your environment's ability to continue running after some cluster nodes are made not available. In case of a real zonal failure, GKE adds new nodes in an operational zone.

This command does not affect workloads that run in the `composer-system` namespace. You might see related error messages in the command output. This does not affect the failover test. The nodes that exist in the selected zone are still marked as unschedulable.

To simulate a cluster zone failure in the selected zone:
    
    
    kubectl get nodes -o name -l "topology.gke.io/zone=ZONE" | \
    xargs kubectl drain \
    --ignore-daemonsets --delete-emptydir-data --force --disable-eviction
    

Replace the following:

  * `ZONE`: the zone where you want to simulate a cluster zone failure.



### Check environment metrics

[ ![Environment metrics during a simulated zone outage](https://docs.cloud.google.com/static/composer/docs/images/composer-2-failover-metrics.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-2-failover-metrics.png) **Figure 1.** Environment metrics during a simulated zone outage (click to enlarge) 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Monitoring** tab.

  4. Check that following metrics are either "green" during the failover operation, or remain the "red" status for at most several minutes.

     * Environment health
     * Scheduler heartbeat
     * Web server health
     * Database health
     * Active workers
     * Active schedulers
     * Active web servers
     * Active triggers

Note that the simulated outage is marked as a "Cluster maintenance operation".

  5. You do not need to do any additional actions to return your environment's cluster to failover readiness after the test. During the test, the environment's cluster automatically adds new nodes that replace the ones affected by the simulated outage.




## What's next

  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)
  * [Monitor environments](https://docs.cloud.google.com/composer/docs/composer-2/monitor-environments)
  * [Disaster recovery with environment snapshots](https://docs.cloud.google.com/composer/docs/composer-2/disaster-recovery-with-snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
