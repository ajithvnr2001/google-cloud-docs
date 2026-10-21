---
url: https://docs.cloud.google.com/compute/docs/disks/create-storage-pools/
title: Create a Hyperdisk pool \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:30.273631+00:00
---

# Create a Hyperdisk pool  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/create-storage-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a Hyperdisk pool Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create Hyperdisk pools. Hyperdisk pools are block storage resources that help you manage your Hyperdisk block storage resources in aggregate. Hyperdisk pools are available in the following variants:

  * Hyperdisk Storage Pools: recommended for most workloads
  * Hyperdisk Exapools: recommended for very large workloads that require more than 100 GiB/s of concurrent performance

**Note:** Hyperdisk Exapools are generally available with an allowlist. To get access to this feature, [contact your account team](https://docs.cloud.google.com/tam).

To learn about the different types of Hyperdisk pools, see [Hyperdisk pools overview](https://docs.cloud.google.com/compute/docs/disks/pools).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to create a Hyperdisk pool, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM instance that can run as a service account: Service Account User (v1) (`roles/iam.serviceAccountUser` role) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a Hyperdisk pool. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a Hyperdisk pool:

  * `compute.storagePools.create` on the project
  * `compute.storagePools.setLabels` on the project



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

The following limitations apply when you create Hyperdisk Storage Pools:

**Resource limits** :

  * You can create a Hyperdisk Storage Pool with up to 5 PiB of provisioned capacity.
  * You can create a maximum of 5 Storage Pools per hour.
  * You can create a maximum of 10 Storage Pools per day.
  * You can create at most 20 Storage Pools per project, per region. This limit is shared between a project's Hyperdisk Balanced Storage Pools and Hyperdisk Throughput Storage Pools that are in the same region.
  * You can't change the provisioning model for a pool. For example, you can't change a Standard capacity Storage Pool to an Advanced capacity Storage Pool or an Advanced performance Storage Pool to a Standard performance Storage Pool.
  * Pools are zonal resources.
  * You can create up to 10,000 disks in a Storage Pool.
  * You can use Hyperdisk Storage Pools with only Compute Engine. Cloud SQL instances can't use Hyperdisk Storage Pools.
  * You can change the provisioned capacity or performance of a Storage Pool at most two times in a 24 hour period.
  * You can create only Hyperdisk Balanced disks in a Hyperdisk Balanced pool, and you can create only Hyperdisk Throughput disks in a Hyperdisk Throughput pool.
  * You must contact your account team to change the provisioned capacity, IOPS, or throughput of an Exapool.
  * You must contact your account team to delete an Exapool.



**Limits for disks in a pool** :

  * Only new disks in the same project and zone can be created in a pool.
  * You can't move disks in or out of a pool; you have to recreate the disk from a standard snapshot. For more information, see [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).
  * To create boot disks in a pool, you must use a Hyperdisk Balanced Storage Pool or Hyperdisk Balanced Exapool.
  * Pools don't support [regional disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).
  * You can't [clone](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#clone), [create instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) of, or [configure Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) for disks in a pool.



## Capacity ranges and provisioned performance limits

When you create a Storage Pool, the provisioned capacity, IOPS, and throughput can't exceed the limits described in [Limits for pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#pool-limits).

## Create a Hyperdisk Storage Pool

To create a new Hyperdisk Storage Pool, use the Google Cloud console, Google Cloud CLI, or REST. You must specify the following properties when you create a Storage Pool:

  * Zone
  * Storage Pool type
  * Capacity provisioning model
  * Pool provisioned capacity
  * Performance provisioning type
  * Pool provisioned IOPS and throughput




###  Console 

  1. Go to the **Create a storage pool** page in the Google Cloud console.   
[Go to the Create Storage Pool page](https://console.cloud.google.com/compute/storagePoolsAdd)
  2. In the **Name** field, enter a unique name for the Storage Pool.
  3. Optional: In the **Description** field, enter a description for the Storage Pool.
  4. Select the **Region** and **Zone** in which to create the Storage Pool.
  5. Choose a value for the **Storage pool type**.
  6. Choose a provisioning type in the **Capacity type** field and specify the capacity to provision for the Storage Pool in the **Storage pool capacity** field. You can specify a size from 10 TiB to 1 PiB.

To create a storage pool with large capacity, you might have to [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

  7. Choose a provisioning type in the **Performance type** field. You can use the following provisioning types with Hyperdisk Storage Pools:

     * Standard capacity: The capacity provisioned for each disk created in the Storage Pool is deducted from the total provisioned capacity of the Storage Pool.
     * Advanced capacity: The Storage Pool benefits from thin-provisioning and data reduction. Only the amount of actual written data is deducted from the total provisioned capacity of the Storage Pool.
     * Standard performance: The performance provisioned for each disk created in the Storage Pool is deducted from the total provisioned performance of the Storage Pool.
     * Advanced performance: The performance provisioned for each disk benefits from thin-provisioning. Only the amount of performance used by a disk is deducted from the total provisioned performance of the Storage Pool.
  8. For Hyperdisk Balanced Storage Pools, in the **Provisioned IOPS** field, enter the IOPS to provision for the Storage Pool.

  9. For a Hyperdisk Throughput Storage Pool or Hyperdisk Balanced Storage Pool, in the **Provisioned throughput** field, enter the throughput to provision for the Storage Pool.

  10. Click **Submit** to create the Storage Pool.




###  gcloud 

To create a Hyperdisk Storage Pool, use the [`gcloud compute storage-pools create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create).
    
    
    gcloud compute storage-pools create NAME  \
        --zone=ZONE   \
        --storage-pool-type=STORAGE_POOL_TYPE   \
        --capacity-provisioning-type=CAPACITY_TYPE \
        --provisioned-capacity=POOL_CAPACITY   \
        --performance-provisioning-type=PERFORMANCE_TYPE \
        --provisioned-iops=IOPS   \
        --provisioned-throughput=THROUGHPUT   \
        --description=DESCRIPTION
    

Replace the following:

  * NAME: the unique Storage Pool name.
  * ZONE: the zone in which to create the Storage Pool, for example, `us-central1-a`.
  * STORAGE_POOL_TYPE: the type of disk to store in the Storage Pool. The allowed values are `hyperdisk-throughput` and `hyperdisk-balanced`.
  * CAPACITY_TYPE: Optional: the capacity provisioning type of the Storage Pool. The allowed values are `advanced` and `standard`. If not specified, the value `advanced` is used.
  * POOL_CAPACITY: the total capacity to provision for the new Storage Pool, specified in GiB by default.
  * PERFORMANCE_TYPE: Optional: the performance provisioning type of the Storage Pool. The allowed values are `advanced` and `standard`. If not specified, the value `advanced` is used.
  * IOPS: the IOPS to provision for the Storage Pool. You can use this flag only with Hyperdisk Balanced Storage Pools.
  * THROUGHPUT: the throughput in MBps to provision for the Storage Pool.
  * DESCRIPTION: Optional: a text string that describes the Storage Pool.



###  REST 

Construct a `POST` request to create a Hyperdisk Storage Pool by using the [`storagePools.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools
    
    {
        "name": "NAME",
        "description": "DESCRIPTION",
        "poolProvisionedCapacityGb": "POOL_CAPACITY",
        "storagePoolType": "projects/PROJECT_ID/zones/ZONE/storagePoolTypes/STORAGE_POOL_TYPE",
        "poolProvisionedIops": "IOPS",
        "poolProvisionedThroughput": "THROUGHPUT",
        "capacityProvisioningType": "CAPACITY_TYPE",
        "performanceProvisioningType": "PERFORMANCE_TYPE"
    }
    

Replace the following:

  * PROJECT_ID: the project ID
  * ZONE: the zone in which to create the Storage Pool, for example, `us-central1-a`.
  * NAME: a unique name for the Storage Pool .
  * DESCRIPTION: Optional: a text string that describes the Storage Pool.
  * POOL_CAPACITY: the total capacity to provision for the new Storage Pool, specified in GiB by default.
  * STORAGE_POOL_TYPE: the type of disk to store in the Storage Pool. The allowed values are `hyperdisk-throughput` and `hyperdisk-balanced`.
  * IOPS: Optional: the IOPS to provision for the Storage Pool. You can use this flag only with Hyperdisk Balanced Storage Pools.
  * THROUGHPUT: Optional: The throughput in MBps to provision for the Storage Pool.
  * CAPACITY_TYPE: Optional: the capacity provisioning type of the Storage Pool. The allowed values are `advanced` and `standard`. If not specified, the value `advanced` is used.
  * PERFORMANCE_TYPE: Optional: the performance provisioning type of the Storage Pool. The allowed values are `advanced` and `standard`. If not specified, the value `advanced` is used.



###  Go 
    
    
    // createHyperdiskStoragePool creates a new Hyperdisk storage pool in the specified project and zone.
    func createHyperdiskStoragePool(w io.Writer, projectId, zone, storagePoolName, storagePoolType string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-west4-b"
    	// storagePoolName := "your_storage_pool_name"
    	// storagePoolType := "projects/**your_project_id**/zones/europe-west4-b/diskTypes/hyperdisk-balanced"
    
    	ctx := context.Background()
    	client, err := compute.NewStoragePoolsRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewStoragePoolsRESTClient: %v", err)
    	}
    	defer client.Close()
    
    	// Create the storage pool resource
    	resource := &computepb.StoragePool{
    		Name:                        proto.String(storagePoolName),
    		Zone:                        proto.String(zone),
    		StoragePoolType:             proto.String(storagePoolType),
    		CapacityProvisioningType:    proto.String("advanced"),
    		PerformanceProvisioningType: proto.String("advanced"),
    		PoolProvisionedCapacityGb:   proto.Int64(10240),
    		PoolProvisionedIops:         proto.Int64(10000),
    		PoolProvisionedThroughput:   proto.Int64(1024),
    	}
    
    	// Create the insert storage pool request
    	req := &computepb.InsertStoragePoolRequest{
    		Project:             projectId,
    		Zone:                zone,
    		StoragePoolResource: resource,
    	}
    
    	// Send the insert storage pool request
    	op, err := client.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Insert storage pool request failed: %v", err)
    	}
    
    	// Wait for the insert storage pool operation to complete
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	// Retrieve and return the created storage pool
    	storagePool, err := client.Get(ctx, &computepb.GetStoragePoolRequest{
    		Project:     projectId,
    		Zone:        zone,
    		StoragePool: storagePoolName,
    	})
    	if err != nil {
    		return fmt.Errorf("Get storage pool request failed: %v", err)
    	}
    
    	fmt.Fprintf(w, "Hyperdisk Storage Pool created: %v\n", storagePool.GetName())
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[InsertStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertStoragePoolRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool.html);
    import com.google.cloud.compute.v1.[StoragePoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateHyperdiskStoragePool {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the zone in which you want to create the storagePool.
        String zone = "us-central1-a";
        // Name of the storagePool you want to create.
        String storagePoolName = "YOUR_STORAGE_POOL_NAME";
        // The type of disk you want to create.
        // Storage types can be "hyperdisk-throughput" or "hyperdisk-balanced"
        String storagePoolType = String.format(
            "projects/%s/zones/%s/storagePoolTypes/hyperdisk-balanced", projectId, zone);
        // Optional: the capacity provisioning type of the storage pool.
        // The allowed values are advanced and standard. If not specified, the value advanced is used.
        String capacityProvisioningType = "advanced";
        // The total capacity to provision for the new storage pool, specified in GiB by default.
        long provisionedCapacity = 128;
        // the IOPS to provision for the storage pool.
        // You can use this flag only with Hyperdisk Balanced Storage Pools.
        long provisionedIops = 3000;
        // the throughput in MBps to provision for the storage pool.
        long provisionedThroughput = 140;
        // The allowed values are low-casing strings "advanced" and "standard".
        // If not specified, "advanced" is used.
        String performanceProvisioningType = "advanced";
    
        createHyperdiskStoragePool(projectId, zone, storagePoolName, storagePoolType,
                capacityProvisioningType, provisionedCapacity, provisionedIops,
            provisionedThroughput, performanceProvisioningType);
      }
    
      // Creates a hyperdisk storagePool in a project
      public static [StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool.html) createHyperdiskStoragePool(String projectId, String zone,
            String storagePoolName, String storagePoolType, String capacityProvisioningType,
            long capacity, long iops, long throughput, String performanceProvisioningType)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([StoragePoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.html) client = [StoragePoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.html).create()) {
          // Create a storagePool.
          [StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool.html) resource = [StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool.html).newBuilder()
                  .setZone(zone)
                  .setName(storagePoolName)
                  .setStoragePoolType(storagePoolType)
                  .[setCapacityProvisioningType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool.Builder.html#com_google_cloud_compute_v1_StoragePool_Builder_setCapacityProvisioningType_java_lang_String_)(capacityProvisioningType)
                  .setPoolProvisionedCapacityGb(capacity)
                  .setPoolProvisionedIops(iops)
                  .setPoolProvisionedThroughput(throughput)
                  .[setPerformanceProvisioningType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool.Builder.html#com_google_cloud_compute_v1_StoragePool_Builder_setPerformanceProvisioningType_java_lang_String_)(performanceProvisioningType)
                  .build();
    
          [InsertStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertStoragePoolRequest.html) request = [InsertStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertStoragePoolRequest.html).newBuilder()
                  .setProject(projectId)
                  .setZone(zone)
                  .setStoragePoolResource(resource)
                  .build();
    
          // Wait for the insert disk operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = client.insertAsync(request).get(1, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("StoragePool creation failed!");
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)().toString());
          }
    
          // Wait for server update
          TimeUnit.SECONDS.sleep(10);
    
          [StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool.html) storagePool = client.get(projectId, zone, storagePoolName);
    
          System.out.printf("Storage pool '%s' has been created successfully", storagePool.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool.html#com_google_cloud_compute_v1_StoragePool_getName__)());
    
          return storagePool;
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('@google-cloud/compute');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a storagePoolClient
    const storagePoolClient = new computeLib.StoragePoolsClient();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.ZoneOperationsClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // Project ID or project number of the Google Cloud project you want to use.
    const projectId = await storagePoolClient.getProjectId();
    // Name of the zone in which you want to create the storagePool.
    const zone = 'us-central1-a';
    // Name of the storagePool you want to create.
    // storagePoolName = 'storage-pool-name';
    // The type of disk you want to create. This value uses the following format:
    // "projects/{projectId}/zones/{zone}/storagePoolTypes/(hyperdisk-throughput|hyperdisk-balanced)"
    const storagePoolType = `projects/${projectId}/zones/${zone}/storagePoolTypes/hyperdisk-balanced`;
    // Optional: The capacity provisioning type of the storage pool.
    // The allowed values are advanced and standard. If not specified, the value advanced is used.
    const capacityProvisioningType = 'advanced';
    // The total capacity to provision for the new storage pool, specified in GiB by default.
    const provisionedCapacity = 10240;
    // The IOPS to provision for the storage pool.
    // You can use this flag only with Hyperdisk Balanced Storage Pools.
    const provisionedIops = 10000;
    // The throughput in MBps to provision for the storage pool.
    const provisionedThroughput = 1024;
    // Optional: The performance provisioning type of the storage pool.
    // The allowed values are advanced and standard. If not specified, the value advanced is used.
    const performanceProvisioningType = 'advanced';
    
    async function callCreateComputeHyperdiskPool() {
      // Create a storagePool.
      const storagePool = new compute.StoragePool({
        name: storagePoolName,
        poolProvisionedCapacityGb: provisionedCapacity,
        poolProvisionedIops: provisionedIops,
        poolProvisionedThroughput: provisionedThroughput,
        storagePoolType,
        performanceProvisioningType,
        capacityProvisioningType,
        zone,
      });
    
      const [response] = await storagePoolClient.insert({
        project: projectId,
        storagePoolResource: storagePool,
        zone,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create storage pool operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Storage pool: ${storagePoolName} created.`);
    }
    
    await callCreateComputeHyperdiskPool();

## Create a Hyperdisk Exapool

Hyperdisk Exapools are generally available with an allowlist. To create a Hyperdisk Exapool, [contact your account team](https://docs.cloud.google.com/tam).

## What's next?

  * [Add disks to a pool](https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity#create-disks-in-sp).
  * [Manage pools](https://docs.cloud.google.com/compute/docs/disks/manage-storage-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
