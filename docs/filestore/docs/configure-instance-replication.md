---
url: https://docs.cloud.google.com/filestore/docs/configure-instance-replication/
title: Manage instance replication \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:17.042676+00:00
---

# Manage instance replication  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/configure-instance-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Manage instance replication Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure instance replication to pair a source instance with a standby replica. You can use instance replication in the following scenarios:

  * **Protect instances against outages** : Maintain a continuously updated cross-region failover instance for disaster recovery.
  * **Migrate data** : Promote a standby replica to permanently migrate an instance to a new location with minimal downtime.
  * **Run operational tests** : Pause replication to temporarily mount the replica and run isolated disaster recovery drills or test workloads without affecting your primary instance.



## Before you begin

Create a [Filestore](https://docs.cloud.google.com/filestore/docs/creating-instances) instance to use as a source instance for your replica.

### Enable APIs

Enable the Filestore API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=file.googleapis.com)

### Required roles

To get the permissions that you need to configure instance replication and monitor replicas, ask your administrator to grant you the following IAM roles on your project: 

  * Create and manage Filestore instances: [Cloud Filestore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`) 
  * View instance replication metrics: [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) 
  * Create and manage metrics dashboards: [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you are creating a [cross-project replica](https://docs.cloud.google.com/filestore/docs/instance-replication#cross-project-replication), you must have the Cloud Filestore Editor (`roles/file.editor`) role on set on both the source and replica projects. This role includes the `file.instances.create` permission, which is required on the source project to create a cross-project replica.

## Create an instance replica

You can't use Google Cloud console to create a [cross-project replica](https://docs.cloud.google.com/filestore/docs/instance-replication#cross-project-replication). Instead, use gcloud CLI or REST API.

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore **Instances** page.

[Go to Instances](https://console.cloud.google.com/filestore/instances)

  2. Click the **Instance ID** of the instance that you want to replicate.

  3. In the instance details page, click the **Replications** tab.

  4. Click **Create replica**.

  5. Verify the source instance details, review the supported recovery point objective and click **Next**.

  6. Create the instance. For more information, see [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances). Consider the following:

     * The specified capacity must be greater than or equal to the source instance capacity.
     * The [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) and [Filestore protocol](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) must be the same for source instance and replica.
     * For a robust disaster recovery solution, we recommend that you choose a different region for the replica, rather than just a different zone.
  7. Click **Next**.

  8. Review the details and click **Next**.

  9. Click **Create**.

  10. Wait for the operation to complete. When the process finishes, the replica is listed under the source instance on the **Replications** page. Click the replica **Instance ID** to view its details.




### gcloud

  1. To create a replica instance, run the [`filestore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/create) command.
         
         gcloud filestore instances create INSTANCE_ID \
           --source-instance=projects/SOURCE_PROJECT_ID/locations/SOURCE_LOCATION/instances/SOURCE_INSTANCE_ID \
           --project=REPLICA_PROJECT_ID \
           --location=LOCATION \
           --network=name="NETWORK" \
           --tier=TIER \
           --file-share=name="FILE_SHARE_NAME",capacity=FILE_SHARE_SIZE \
         




Replace the following:

  * INSTANCE_ID with the name of the replica instance that you want to create. For example, `sample-replica`.
  * SOURCE_PROJECT_ID with the project ID of the Google Cloud project where the source instance is located.
  * SOURCE_LOCATION with the location where the source instance resides.
  * SOURCE_INSTANCE_ID with the name of the source instance for which you want to create a replica. For example, `sample-instance`.
  * REPLICA_PROJECT_ID with the project ID of the Google Cloud project where you want the replica instance to reside.
  * LOCATION with the location where you want the replica instance to reside, such as `us-central1-a`. If the source is in a zonal service tier, you must specify both a region and zone for the replica.
  * NETWORK with the name of the network you want to use, such as `default`.
  * TIER with the [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) you need, for example,`ZONAL`. The tier and capacity range must match the source instance.
  * FILE_SHARE_NAME with the name you specify for the NFS file share that is served from the instance, such as `vol1`.
  * FILE_SHARE_SIZE with the size you want for the file share, such as `1.25TiB`.



### REST API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To create an instance replica, use the following request:
         
         curl -s \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Content-Type: application/json" \
           --request POST \
           -d '{"tier": "TIER",
               "networks": { "network": "NETWORK" },
               "file_shares": {"name": "SHARE_NAME","capacity_gb": "CAPACITY"},
               "replication": {"replicas":[{"peer_instance": "projects/SOURCE_PROJECT_ID/locations/ACTIVE_LOCATION/instances/ACTIVE_NAME"}], "role":"standby"},
               "description": "DESCRIPTION" }' \
           "https://file.googleapis.com/v1/projects/REPLICA_PROJECT_ID/locations/REPLICA_LOCATION/instances?instanceId=REPLICA_INSTANCE_NAME"
         

Replace the following:

     * `TIER` is the name of the service tier you want to use for the replica. For example, `REGIONAL`.
     * `NETWORK` is the name of the network you want to use for the replica. For example, `default`. You must use the same network as the source.
     * `SHARE_NAME` is the name of the file share. For example, `vol1`.
     * `CAPACITY` is the size, in GiB, you want to allocate for the replica. For example, `1024`. Capacity must be greater than or equal to that of the source instance.
     * `REPLICA_PROJECT_ID` is the name of the project where you want the replica to reside. For example, `sample-project`.
     * `SOURCE_PROJECT_ID` is the name of the project where your source instance resides.
     * `ACTIVE_LOCATION` is the location where the source resides. For example, `us-east1`.
     * `ACTIVE_NAME` is the name of the instance you want to replicate. For example, `sample-instance`.
     * `DESCRIPTION` is a description of the replica instance you want to create. For example, `A sample replica`.
     * `REPLICA_LOCATION` is the location where you want the replica to reside. For example, `us-central1`.
     * `REPLICA_INSTANCE_NAME` is the name of the replica instance you want to create. For example, `sample-replica`.



## View replica status

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore **Replications** page.



[Go to Replications](https://console.cloud.google.com/filestore/replications)

  1. Click the replica **Instance ID** to view its details.



### gcloud

  1. To view information about a specific instance, run the [`instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/describe) command:
         
         gcloud filestore instances describe <var>INSTANCE_ID</var> \
            --project=<var>PROJECT_ID</var> \
           --location=<var>LOCATION</var> \
         




Replace the following:

  * INSTANCE_ID with the instance ID of the Filestore instance that you want to view, such as `genomics-instance`.
  * PROJECT_ID with the project ID of the Google Cloud project that contains the Filestore instance.
  * LOCATION with the location where instance resides, such as `us-east1-b`.

The response to the `instances describe` command is similar to any of the following examples.

This response example shows a source instance with instance replication enabled. Notice the role specified is `ACTIVE`:
        
        createTime: '2024-06-17T22:17:26.475900265Z'
        fileShares:
        - capacityGb: '1024'
          name: vol1
        name: projects/genomics-project/locations/us-east1-b/instances/genomics-instance-source
        networks:
        - connectMode: DIRECT_PEERING
          ipAddresses:
          - 172.27.220.2
          modes:
          - MODE_IPV4
          network: default
          reservedIpRange: 172.27.220.0/26
        replication:
          replicas:
          - peerInstance: projects/genomics-project/locations/us-central1-a/instances/genomics-instance-replica
            state: READY
          role: ACTIVE
        state: READY
        tier: ZONAL
        

This response example shows a replica instance that was promoted to a regular instance. Note that replication isn't specified as it is not active yet:
        
        createTime: '2024-06-20T17:11:56.048062134Z'
        fileShares:
        - capacityGb: '1024'
          name: vol1
        name: projects/genomics-project/locations/us-west2-a/instances/genomics-instance-replica
        networks:
        - connectMode: DIRECT_PEERING
          ipAddresses:
          - 10.155.90.194
          network: default
          reservedIpRange: 10.155.90.192/26
        satisfiesPzi: true
        state: READY
        tier: ZONAL
        

This response example shows a replica that was paired with an active instance. The replication role is `STANDBY`:
        
        createTime: '2024-06-21T04:15:21.721579074Z'
        fileShares:
        - capacityGb: '1280'
          name: vol1
        name: projects/genomics-project/locations/us-west1-a/instances/genomics-replica
        networks:
        - connectMode: DIRECT_PEERING
          ipAddresses:
          - 10.153.44.194
          network: default
          reservedIpRange: 10.153.44.192/26
        replication:
          replicas:
          - peerInstance: projects/genomics-project/locations/us-west2-a/instances/genomics-instance
            state: READY
          role: STANDBY
        satisfiesPzi: true
        state: READY
        tier: ZONAL
        




### REST API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To view replica status, use the following request:
         
         curl -s \
             --header "Authorization: Bearer $(gcloud auth print-access-token)" \
             --header "Content-Type: application/json" \
             --request GET \
             "https://file.googleapis.com/v1/projects/<var>PROJECT</var>/locations/<var>LOCATION</var>/instances/<var>INSTANCE_NAME</var>"
         

Replace the following:

     * `PROJECT` is the name of the project where your instance is located. For example, `sample-project`.
     * `LOCATION` is the location where your instance resides. For example, `us-west1-a`.
     * `INSTANCE_NAME` is the name of the instance you want to view. For example, `sample-instance`.



## List all replicas in a project

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore **Replications** page.

[Go to Replications](https://console.cloud.google.com/filestore/replications)




The table lists source instances with their replicas. Click the replica **Instance ID** to view its details.

### gcloud

  1. To see a list of all instances in the project, run the [`instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/list) command:
         
         gcloud filestore instances list
           --project=PROJECT_ID \
         

Replace PROJECT_ID with the project ID of the project you want to view.

The response returns a list of instances and replicas, similar to the following:
         
         INSTANCE_NAME                       LOCATION     TIER      CAPACITY_GB  FILE_SHARE_NAME  IP_ADDRESS     STATE  CREATE_TIME
         genomics-source-1                   us-east1-b   ZONAL     1024         vol1             172.27.220.2   READY  2024-06-17T22:17:26
         genomics-source-1-replica           us-west1-a   ZONAL     1024         vol1             10.142.57.194  READY  2024-06-17T23:47:19
         




### REST API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To list replicas in a specific project, use the following request:
         
         curl -s \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Content-Type: application/json" \
           --request GET \
           "https://file.googleapis.com/v1/projects/PROJECT/locations/LOCATION/instances"

Replace the following:

     * `PROJECT` is the name of the project where your instance is located. For example, `sample-project`.
     * `LOCATION` is the location you want to search. To search all instances in any location within a project, use the [`list`](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/list) endpoint.



## Pause replication

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore **Instances** page.

[Go to Instances](https://console.cloud.google.com/filestore/instances)

  2. Click the **Instance ID** of the replica you want to pause.

  3. In the **Description** section, click the **Replications** tab.

  4. In the **Active instance details** section, click **Pause replication**.

  5. Read the alert before continuing and confirm by clicking **Pause replication**.




The replication status changes to **Pausing**. After the operation is finished, the **Replication Status** changes to **Paused**.

### gcloud

To pause a replica, run the [`gcloud filestore instances pause-replica`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/pause-replica) command.
    
    
      gcloud filestore instances pause-replica INSTANCE_ID \
          --project=PROJECT_ID \
          --location=LOCATION \
    

Replace the following:

  * INSTANCE_ID with the instance ID of the Filestore instance that you want to pause, such as `my-replica`.
  * PROJECT_ID with the project ID of the Google Cloud project that contains the Filestore instance.
  * LOCATION with the location where the replica resides, such as `us-central1`.



When successfully completed, the following response or similar is returned:
    
    
    createTime: '2025-12-22T14:03:33.727531128Z'
    customPerformanceSupported: true
    description: Replica of active, us-east1-b
    fileShares:
    - capacityGb: '1024'
      name: share
    name: projects/genomics-project/locations/us-west2-a/instances/my-replica
    networks:
    - connectMode: DIRECT_PEERING
      ipAddresses:
      - 10.229.150.130
      modes:
      - MODE_IPV4
      network: default
      reservedIpRange: 10.229.150.128/26
    performanceLimits:
      maxIops: '12000'
      maxReadIops: '12000'
      maxReadThroughputBps: '125829120'
      maxWriteIops: '4000'
      maxWriteThroughputBps: '104857600'
    protocol: NFS_V3
    replication:
      replicas:
      - peerInstance: projects/genomics-project/locations/us-east1-b/instances/my-source
        state: PAUSED
        stateUpdateTime: '2025-12-22T14:24:27.558413891Z'
      role: STANDBY
    state: READY
    tier: REGIONAL
    

### REST API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To pause a replica, use the following request:
         
         curl -s \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Content-Type: application/json" \
           --request POST \
           -d '{}' \
           "https://file.googleapis.com/v1/projects/PROJECT/locations/LOCATION/instances/REPLICA_NAME:pauseReplica"

Replace the following:

     * `PROJECT` is the name of the project where your replica resides For example, `sample-project`.
     * `LOCATION` is the location where the replica resides. For example, `us-west1-a`.
     * `REPLICA_NAME` is the name of the instance you want to pause. For example, `sample-replica`.



## Resume replication

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore **Instances** page.

[Go to Instances](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID of the replica you want to use.

  3. In the **Description** section, click the **Replications** tab.

  4. In the **Active instance details** section, click **Resume replication**.

  5. Read the alert before continuing and confirm by entering `resume` in the provided field.




The replication status changes to **Resuming**. After the operation is finished, the **Replication Status** changes to **Ready**.

### gcloud

You can resume a replica instance by running the [`gcloud filestore instances resume-replica`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/resume-replica) command.
    
    
      gcloud filestore instances resume-replica INSTANCE_ID \
          --project=PROJECT_ID \
          --location=LOCATION \
    

Replace the following:

  * INSTANCE_ID with the instance ID of the Filestore replica instance that you want to resume, such as `my-replica`.
  * PROJECT_ID with the project ID of the Google Cloud project that contains the Filestore replica instance.
  * LOCATION with the location where the replica resides, such as `us-central1`.



When successfully completed, the following response or similar is returned:
    
    
      createTime: '2025-12-22T14:03:33.727531128Z'
      customPerformanceSupported: true
      description: Replica of active, us-central1
      fileShares:
      - capacityGb: '1024'
        name: share
      name: projects/genomics-project/locations/us-central1/instances/my-replica
      networks:
      - connectMode: DIRECT_PEERING
        ipAddresses:
        - 10.229.150.130
        modes:
        - MODE_IPV4
        network: default
        reservedIpRange: 10.229.150.128/26
      performanceLimits:
        maxIops: '12000'
        maxReadIops: '12000'
        maxReadThroughputBps: '125829120'
        maxWriteIops: '4000'
        maxWriteThroughputBps: '104857600'
      protocol: NFS_V3
      replication:
        replicas:
        - peerInstance: projects/genomics-project/locations/us-central1/instances/my-source
          state: READY
          stateUpdateTime: '2025-12-22T14:24:27.558413891Z'
        role: STANDBY
      state: READY
      tier: REGIONAL
    

### REST API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To resume replication, use the following request:


    
    
    curl -s \
          --header "Authorization: Bearer $(gcloud auth print-access-token)" \
          --header "Content-Type: application/json" \
          --request POST \
          -d '{}' \
          "https://file.googleapis.com/v1/projects/PROJECT/locations/LOCATION/instances/REPLICA_NAME:resumeReplica"

Replace the following:

  * `PROJECT` is the name of the project where your replica is located. For example, `sample-project`.
  * `LOCATION` is the location where the replica resides. For example, `us-west1-a`.
  * `REPLICA_NAME` is the name of the instance you want to resume. For example, `sample-replica`.



## Break replication and promote replica

Breaking replication between the active and standby instances promotes the replica to a regular instance. This operation is irreversible.

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore **Instances** page.

[Go to Instances](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID of the replica you want to use.

  3. Click **Break replication**.

  4. Enter the **Instance ID** of the replica, then click **Break replication**.

  5. Wait for the operation to complete.




### gcloud

To promote a replica instance, run the [`gcloud filestore instances promote-replica`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/promote-replica) command.
    
    
      gcloud filestore instances promote-replica INSTANCE_ID   
    
          --project=PROJECT_ID   
    
          --location=LOCATION   
    

Replace the following:

  * INSTANCE_ID with the instance ID of the Filestore instance that you want to promote, such as `my-replica`.
  * PROJECT_ID with the project ID of the Google Cloud project that contains the Filestore instance.
  * LOCATION with the location where the replica resides, such as `us-central1`.



When successfully completed, the following response or similar is returned:
    
    
    capacityGb: '1024'
    capacityStepSizeGb: '256'
    createTime: '2024-06-20T17:11:56.048062134Z'
    fileShares:
    - capacityGb: '1024'
      name: vol1
    maxCapacityGb: '9984'
    maxShareCount: '1'
    name: projects/genomics-project/locations/us-west2-a/instances/my-replica
    networks:
    - connectMode: DIRECT_PEERING
      ipAddresses:
      - 10.155.90.194
      network: default
      reservedIpRange: 10.155.90.192/26
    protocol: NFS_V3
    replication:
      replicas:
      - lastActiveSyncTime: '2024-06-21T00:13:23Z'
        peerInstance: projects/genomics-project/locations/us-east1-b/instances/my-source
      role: STANDBY
    satisfiesPzi: true
    state: PROMOTING
    tier: ZONAL
    

### REST API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To promote the replica, use the following request:
         
         curl -s \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Content-Type: application/json" \
           --request POST \
           -d '{}' \
           "https://file.googleapis.com/v1/projects/PROJECT/locations/LOCATION/instances/REPLICA_NAME:promoteReplica"

Replace the following:

     * `PROJECT` is the name of the project where your replica is located. For example, `sample-project`.
     * `LOCATION` is the location where the replica resides. For example, `us-west1-a`.
     * `REPLICA_NAME` is the name of the instance you want to promote. For example, `sample-replica`.



## Delete a replica instance

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore instances page.

[Go to Instances](https://console.cloud.google.com/filestore/instances)

Replicas are listed under their associated source instances. If you don't see a replica, see the `gcloud` commands for this task.

  2. Click the instance ID of the instance you want to delete.

  3. Click **Delete**.




### gcloud

  1. To see a list of all instances, including replicas, run the [`instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/list) command:
         
         gcloud filestore instances list
           --project=PROJECT_ID \
         

Replace PROJECT_ID with the project ID of the project you want to view.

  2. Copy the details of the instance you want to delete.

  3. To delete a replica instance, run the [`filestore instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/delete) command.
         
         gcloud filestore instances delete INSTANCE_ID \
           --location=LOCATION \
         




Replace the following:

  * INSTANCE_ID with the instance ID of the Filestore instance that you want to delete, such as `my-replica`.
  * LOCATION with the location where the replica resides, such as `us-central1-a`.



### REST API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To delete a replica instance, use the following request:
         
         curl -s \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Content-Type: application/json" \
           --request DELETE \
           "https://file.googleapis.com/v1/projects/PROJECT/locations/LOCATION/instances/INSTANCE_NAME"

Replace the following:

     * `PROJECT` is the name of the project where your instance is located. For example, `sample-project`.
     * `LOCATION` is the location where your instance resides. For example, `us-west1-a`.
     * `INSTANCE_NAME` is the name of the instance you want to delete. For example, `sample-instance`.



## Monitor instance replication

###  Google Cloud console 

To see Filestore instance replication metrics in a Cloud Monitoring dashboard, follow these steps:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Select a metric** expandable section.

  3. In the **Filter by resource or metric name** field, type `filestore` and select the **Filestore Instance** expandable section.

  4. Select the **Instance** expandable section and then click **RPO**.

  5. The RPO metric `times_since_last_replication` is displayed. This metric becomes available several minutes after the initial synchronization of replicated data completes.




## What's next

  * Find more about [instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication).
  * Read [Instance replication reference documentation](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/promoteReplica).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
