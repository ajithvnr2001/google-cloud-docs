---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-configure-ha/
title: Configure high availability \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:54.376602+00:00
---

# Configure high availability  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-configure-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure high availability Stay organized with collections  Save and categorize content based on your preferences. 

The purpose of a high availability configuration is to reduce downtime when a database cluster instance becomes unavailable. This might happen when an instance runs out of memory. With high availability, your data continues to be available to client applications.

Within a site, the configuration is made up of a primary instance and a standby replica. All writes made to the primary instance are replicated to the standby replica before a transaction is reported as committed. If your primary instance becomes unavailable, GDC automatically promotes the standby replica to act as the new primary instance. Application traffic is then rerouted to the new primary instance. This process is called a _failover_.

An automatic failover starts after 3 consecutive health check failures on the primary instance, that are each 30 seconds apart.

GDC supports both automatic and manual failover. Automatic failover is enabled by default, and you can disable automatic failover if needed. You can also manually trigger a failover at any time to recover from an unexpected failure and minimize downtime.

The failover involves the following process, in order:

  1. GDC takes the primary instance offline.

  2. GDC turns the standby replica into the new active database cluster.

  3. GDC deletes the previous active database cluster.

  4. GDC creates a new standby replica.




## Update an existing cluster

You can update your high availability settings for an existing database cluster:

###  Console 

  1. In the navigation menu, select **Database Service**.

  2. From the database cluster list, click the database cluster to update.

  3. Select edit **Edit** in the **High availability** section.

![Edit the high availability settings of a database cluster.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/dbs-edit-ha.png)

  4. Select **Enable same zone standby** to either toggle on or off the availability of a standby instance in the same zone as your primary database cluster.

  5. Click **Save**.

  6. Verify your database cluster reflects your high availability update by viewing its status in the **High availability** column of the database cluster list.




###  gdcloud 

  1. Update your database cluster's high availability configuration:
         
         gdcloud database clusters update CLUSTER_NAME \
             --availability-type HA_TYPE
         

Replace the following:

     * `CLUSTER_NAME`: the name of the database cluster.
     * `HA_TYPE`: the high availability level for the database cluster. You can set `zonal` or `zonal_ha`. The `zonal` value is set by default.
  2. Verify your database cluster reflects your high availability update:
         
         gdcloud database clusters list
         




###  API 

  1. Update your database cluster's high availability configuration:
         
         kubectl patch dbcluster.postgresql.dbadmin.gdc.goog DBCLUSTER_NAME \
             -n USER_PROJECT \
             -p '{"spec": {"availability": {"enableHighAvailability": HA_ENABLED}}}' \
             --type=merge
         

Replace the following variables:

     * `DBCLUSTER_NAME`: the name of the database cluster.
     * `USER_PROJECT`: the name of the user project where the database cluster was created.
     * `HA_ENABLED`: the high availability level for the database cluster. You can set `true` or `false`. The `false` value is set by default.
  2. Verify your database cluster reflects your high availability update:
         
         kubectl get dbcluster.DBENGINE_NAME.dbadmin.gdc.goog DBCLUSTER_NAME \
           -n USER_PROJECT \
           -o yaml
         




## Migrate to the latest high availability implementation

To verify that your high availability database cluster is using the latest implementation, check if the annotation `dbcluster.dbadmin.goog/raasEnabled` exists on your high availability database cluster CR. This annotation will only appear on clusters using the new implementation. If you don't have this annotation, you can enable it and migrate your cluster with the following steps:

  1. Check with your Infrastructure Operator that your GDC environment is upgraded to version 1.15.1 or later.
  2. Disable high availability on your database cluster. Wait for the `HAReady` condition to disappear, and then re-enable high availability.
  3. After you see `HAReady in progress` or `HAReady setup complete`, check your database cluster CR for the annotation `dbcluster.dbadmin.goog/raasEnabled`. If it appears, then your database cluster has been successfully migrated.



## Trigger a failover

If you have configured high availability for your database cluster, you can trigger a failover. To trigger a failover, complete the following steps:

###  Console 

  1. In the navigation menu, select **Database Service**.

  2. From the database cluster list, click the database cluster to trigger a failover for. Your database cluster must have high availability enabled to be eligible for a failover.

  3. Click **Failover**.

  4. Type the cluster's ID for the confirmation phrase and click **Failover** to trigger the failover process.




###  gdcloud 

  * Trigger the failover for the database cluster:
        
        gdcloud database clusters failover CLUSTER_NAME
        

Replace `CLUSTER_NAME` with the name of the database cluster.




###  API 
    
    
      apiVersion: fleet.dbadmin.gdc.goog/v1
      kind: Failover
      metadata:
        name: FAILOVER_NAME
        namespace: USER_PROJECT
      spec:
        dbclusterRef: DBCLUSTER_NAME
    

Replace the following variables:

  * `DBCLUSTER_NAME`, the name of the database cluster.
  * `USER_PROJECT`: the name of the user project where the database cluster was created.
  * `FAILOVER_NAME`, the unique name of the failover, for example `failover-sample`.



## Disable automatic failover

Automatic failover is enabled by default on high availability database clusters.

To disable automatic failover, set `enableAutoFailover` to `false` in the database cluster's manifest:
    
    
    spec:
      availability:
        enableAutoFailover: false
    

To update the automatic failover configuration for an existing database cluster using the API, run the following command:
    
    
    kubectl patch dbcluster.postgresql.dbadmin.gdc.goog DBCLUSTER_NAME \
      -n USER_PROJECT \
      -p '{"spec": {"availability": {"enableAutoFailover": AUTO_FAILOVER_ENABLED}}}' \
      --type=merge
    

Replace the following variables:

  * `DBCLUSTER_NAME`: the name of the database cluster.
  * `USER_PROJECT`: the name of the user project where the database cluster was created.
  * `AUTO_FAILOVER_ENABLED`: the automatic failover setting for the database cluster. You can set `true` or `false`. The `true` value is set by default.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
