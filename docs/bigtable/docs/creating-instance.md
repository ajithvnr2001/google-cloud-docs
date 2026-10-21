---
url: https://docs.cloud.google.com/bigtable/docs/creating-instance/
title: Create an instance \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:09.193682+00:00
---

# Create an instance  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/creating-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an instance

A Bigtable instance serves as the top-level container for your clusters and tables, letting you configure storage and [replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) across up to 8 regions for high availability. You can create and configure an instance using the Google Cloud console, the Google Cloud CLI, the `cbt` CLI , or the Cloud Bigtable client libraries.

## Before you begin

Make sure that you are familiar with [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview) and [Instances, clusters, and nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes).

Prepare your environment:

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Bigtable API, Cloud Bigtable Admin API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigtable.googleapis.com,bigtableadmin.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Bigtable API, Cloud Bigtable Admin API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigtable.googleapis.com,bigtableadmin.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Run the following command to install the `cbt` CLI : 
         
         gcloud components install cbt




Plan your configuration:

  1. Optional: If you plan to enable replication, do the following:

     * Take a few minutes to read the [replication overview](https://docs.cloud.google.com/bigtable/docs/replication-overview).
     * Identify your [use case for replication](https://docs.cloud.google.com/bigtable/docs/replication-overview#use-cases).
     * Determine the [region or regions](https://docs.cloud.google.com/bigtable/docs/locations) that your instance should be in, based on your use case and the location of your application and traffic.
     * Decide how you'll use [application profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles) to route incoming requests.
  2. Optional: If you want to use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/use-cmek#view-key) instead of the default Google-managed encryption, have your CMEK key ID ready _before_ you create your new instance. You are not able to add CMEK protection to an instance after it has been created, and you cannot modify or replace the CMEK key after the instance is created. For more information, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/use-cmek).




## Create an instance

To create a Bigtable instance:

###  Console 

  1. In the Google Cloud console, go to the **Create instance** page.

[Go to Create instance](https://console.cloud.google.com/bigtable/create-instance)

  2. Enter a name for the instance.

The Google Cloud console displays this name to identify your instance.

  3. Enter an instance ID.

The instance ID is a permanent identifier for the instance.

  4. Click **Continue**.

  5. In the **Select your edition** section, select a Bigtable edition.

If you want to compare the specifications between the editions, then click **Compare editions**. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

  6. Click **Continue**.

  7. Choose whether to use an [SSD or HDD](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd) disk for your clusters. In most cases, SSD is best. If you want to enable the in-memory tier, then select **SSD**. This choice is permanent.

  8. Click **Continue**.

  9. Enter a cluster ID for the first cluster.

The cluster ID is a permanent identifier for the cluster.

  10. Choose the [region and zone](https://docs.cloud.google.com/bigtable/docs/locations) where the first cluster will run.

  11. Optional: To configure the cluster to always scale in increments of two nodes, select **Enable 2x node scaling**. 2x node scaling isn't available in all zones. For the Enterprise Plus edition, 2x node scaling is the default option. For more information, see [Node scaling factor](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling-factor).

  12. Optional: To use the in-memory tier at the cluster level, select **Enable in-memory**.

  13. Choose a node scaling mode for the cluster. In most cases, you should choose autoscaling. For scaling guidance, see [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling).

     1. For **Manual node allocation** , enter the number of Bigtable nodes for the first cluster. If you aren't sure how many nodes you need, use the default. You can add more nodes later. 
     2. For **Autoscaling** , enter values for the following: 
        * **Minimum** number of nodes
        * **Maximum** number of nodes
        * **CPU utilization target**
        * **Storage utilization target**
  14. Optional: To protect your instance with CMEK instead of the default Google-managed encryption, complete the following:

     1. Click **Show encryption options**.
     2. Select **Cloud KMS key**.
     3. In the **Key management type** field, select one of the following options: 
        * If you want to automate creation of Cloud KMS keys, select **Cloud KMS with Autokey** , and then click **Request a key**. A message indicates when your key has been successfully created and is ready for use.
        * If you want to add a key manually, select **Cloud KMS**. Select or enter the resource name for the [CMEK key](https://docs.cloud.google.com/bigtable/docs/use-cmek) that you want to use for the cluster. You cannot add this later. If you are prompted to grant permission to the CMEK key's service account, click **Grant**. Your user account must be granted the Cloud KMS Admin role to complete this task. Click **Save**.
  15. Optional: To enable replication now, complete the following additional steps:

     1. Click **Show advanced options**.
     2. Click **Add cluster** , enter the settings for the cluster, and then click **Add**. Repeat this step to create additional clusters in the instance. You can also enable replication later by [adding a cluster](https://docs.cloud.google.com/bigtable/docs/modifying-instance#clusters-adding).

Each [zone in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) can contain only one cluster. If the **Add cluster** button is disabled, change the zone for your first cluster.

To create an instance that has more than six clusters, first create an instance that has six clusters, then add more clusters to the instance.

  16. Click **Create** to create the instance.

  17. [Review the replication settings in the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to see if they make sense for your [replication use case](https://docs.cloud.google.com/bigtable/docs/replication-overview#use-cases). You might need to [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) or [create custom app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile). 




###  gcloud 

  1. Use the [`bigtable instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/create) to create an instance:
         
         gcloud bigtable instances create INSTANCE_ID \
             --display-name=DISPLAY_NAME \
             [--edition=EDITION] \
             [--cluster-storage-type=CLUSTER_STORAGE_TYPE] \
             [--cluster-config=id=CLUSTER_ID,zone=CLUSTER_ZONE, \
             nodes=NODES] \
             [--cluster-config=id=CLUSTER_ID,zone=CLUSTER_ZONE, \
             autoscaling-min-nodes=AUTOSCALING_MIN_NODES, \
             autoscaling-max-nodes=AUTOSCALING_MAX_NODES, \
             autoscaling-cpu-target=AUTOSCALING_CPU_TARGET, \
             autoscaling-storage-target=AUTOSCALING_STORAGE_TARGET, \
             kms-key=KMS_KEY], \
             [node-scaling-factor=NODE_SCALING_FACTOR]
         

Replace the following:

     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `DISPLAY_NAME`: A human-readable name that identifies the instance in the Google Cloud console. 
     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `CLUSTER_ZONE`: The [zone](https://docs.cloud.google.com/bigtable/docs/locations) where the cluster runs. 

You must configure at least one cluster for the instance, using the `--cluster-config` flag. To create an instance that has multiple clusters, **repeat the`--cluster-config` flag for each cluster**.

For _manual node allocation_ , setting `nodes` in the `--cluster-config` flag is optional. If no value is set, Bigtable allocates nodes to the cluster automatically based on your data footprint and optimizes for 50% storage utilization. This automatic allocation of nodes has a pricing impact. If you want to control the number of nodes in a cluster, replace `NODES` with the number of nodes that you want in the cluster. [Learn more about nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes).

In most cases, choose _autoscaling_ instead of manual node allocation. For_autoscaling, provide `autoscaling-` options in the `--cluster-config` flag (`autoscaling-storage-target` is optional) and don't use `nodes`. See [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling) for guidance on choosing the values for your autoscaling settings. Replace the following for the `cluster-config` option keys:

     * `AUTOSCALING_MIN_NODES`: The minimum number of nodes for the cluster.
     * `AUTOSCALING_MAX_NODES`: The maximum number of nodes for the cluster.
     * `AUTOSCALING_CPU_TARGET`: The target CPU utilization percentage for the cluster. This value must be from 10 to 80.
     * `AUTOSCALING_STORAGE_TARGET`: (Optional) The storage utilization target in GiB that Bigtable maintains by adding or removing nodes.
     * KMS_KEY: The CMEK key for the cluster.

The KMS_KEY value must be set in the following format:
           
           projects/PROJECT/locations/LOCATION/keyRings/KEYRING/cryptoKeys/KEY
           

Replace the following:

       * PROJECT: the permanent identifier for the project
       * LOCATION: the location of your cluster
       * KEYRING: the name of the key ring that contains the key
       * KEY: the name of the key

The following is an example:

`projects/examplestore.com:dev/locations/us-east1/keyRings/devt-cmek-2/cryptoKeys/key2`

If the instance is [CMEK-protected](https://docs.cloud.google.com/bigtable/docs/use-cmek#view-key), each cluster must be in the same region as its CMEK key. You can add CMEK clusters only to instances that are already CMEK-protected.

The command accepts the following optional flags: 

     * `--edition=EDITION`: the [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview) of the instance that you create. Accepted values are `ENTERPRISE` and `ENTERPRISE_PLUS`. The default value is `ENTERPRISE`.
     * `--cluster-storage-type=CLUSTER_STORAGE_TYPE`: the type of storage to use for the instance. The default value is `SSD`. In most cases, the default value is best. This choice is permanent. [Learn more](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd).

     * `--project=PROJECT`: the project in which to create the cluster if different from the current project.

     * `node-scaling-factor=NODE_SCALING_FACTOR`: a flag that enables [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling-factor). You can enable this feature with both manual scaling and autoscaling. Acceptable values are `node-scaling-factor-2x` or `node-scaling-factor-1x`.

To view a list of Bigtable zones that aren't available for 2x node scaling, see [Node scaling factor limitations](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling-limitations).

     * `--tags=TAGKEY_NAME=TAGVALUE_NAME`: a flag that adds tags to a new instance. You can specify both the tag key and the tag value by their permanent ID or namespaced name. You can provide multiple tags as a comma-separated list, for example:

       * Using permanent IDs:  
`--tags=tagKeys/984321798431=tagValues/567890123456,  
tagKeys/123456789012=tagValues/098765432109`
       * Using namespaced names:  
`--tags=123456789012/environment=123456789012/environment/prod,  
123456789012/costcenter=123456789012/costcenter/marketing`
  2. [Review the replication settings in the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to see if they make sense for your [replication use case](https://docs.cloud.google.com/bigtable/docs/replication-overview#use-cases). You might need to [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) or [create custom app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile). 




###  cbt 

**Note:** You can't create CMEK-protected resources or configure autoscaling using the `cbt` CLI . You also can't enable 2x node scaling with the `cbt` CLI .

  1. Start by creating an instance with a single cluster. Use the `createinstance` command to create an instance:
         
         cbt createinstance INSTANCE_ID \
             DISPLAY_NAME \
             CLUSTER_ID \
             CLUSTER_ZONE \
             CLUSTER_NUM_NODES \
             CLUSTER_STORAGE_TYPE
         

Provide the following: 

     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `DISPLAY_NAME`: A human-readable name that identifies the instance in the Google Cloud console. 
     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `CLUSTER_ZONE`: The [zone](https://docs.cloud.google.com/bigtable/docs/locations) where the cluster runs. 
     * `CLUSTER_NUM_NODES`: This field is optional. If no value is set, Bigtable automatically allocates nodes based on your data footprint and optimizes for 50% storage utilization. If you want to control the number of nodes in a cluster, update the `CLUSTER_NUM_NODES` value. Ensure that number of nodes is set to a non-zero value. [Learn more about nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes).
     * `CLUSTER_STORAGE_TYPE`: The type of storage to use for the cluster. Each cluster in an instance must use the same storage type. Accepts the values `SSD` and `HDD`. In most cases, `SSD` is best. This choice is permanent. [Learn more](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd).
  2. To enable replication, use the `createcluster` command to add a cluster:
         
         cbt -instance=INSTANCE_ID \
         createcluster CLUSTER_ID \
         ZONE \
         NUM_NODES \
         STORAGE_TYPE
         
         

Provide the following: 

     * `INSTANCE_ID`: The permanent identifier for the instance you just created. 
     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `ZONE`: The [zone](https://docs.cloud.google.com/bigtable/docs/locations) where the cluster runs. 

Each [zone in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) can contain only one cluster. For example, if an instance has a cluster in `us-east1-b`, you can add a cluster in a different zone in the same region, such as `us-east1-c`, or a zone in a separate region, such as `europe-west2-a`. 

     * `NUM_NODES`: This field is optional. If no value is set, Bigtable automatically allocates nodes based on your data footprint and optimizes for 50% storage utilization. If you want to control the number of nodes in a cluster, update the `NUM_NODES` value. Ensure that number of nodes is set to a non-zero value. 

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 

     * `STORAGE_TYPE`: The type of storage to use for the cluster. Each cluster in an instance must use the same storage type. Accepts the values `SSD` and `HDD`. 

  3. (Optional) [Review the replication settings in the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to see if they make sense for your [replication use case](https://docs.cloud.google.com/bigtable/docs/replication-overview#use-cases). You might need to [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) or [create custom app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile). 




### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace cbta = ::google::cloud::bigtable_admin;
    using ::google::cloud::future;
    using ::google::cloud::Location;
    using ::google::cloud::Project;
    using ::google::cloud::StatusOr;
    [](cbta::BigtableInstanceAdminClient instance_admin,
       std::string const& project_id, std::string const& instance_id,
       std::string const& zone) {
      auto const project = Project(project_id);
      std::string project_name = project.FullName();
      std::string cluster_id = instance_id + "-c1";
    
      google::bigtable::admin::v2::Instance in;
      in.set_type(google::bigtable::admin::v2::Instance::PRODUCTION);
      in.set_display_name("Put description here");
    
      google::bigtable::admin::v2::Cluster cluster;
      cluster.set_location(Location(project, zone).FullName());
      cluster.set_serve_nodes(3);
      cluster.set_default_storage_type(google::bigtable::admin::v2::HDD);
    
      std::map<std::string, google::bigtable::admin::v2::Cluster> cluster_map = {
          {cluster_id, std::move(cluster)}};
    
      future<StatusOr<google::bigtable::admin::v2::Instance>> instance_future =
          instance_admin.CreateInstance(project_name, instance_id, std::move(in),
                                        std::move(cluster_map));
      // Show how to perform additional work while the long running operation
      // completes. The application could use future.then() instead.
      std::cout << "Waiting for instance creation to complete " << std::flush;
      instance_future.wait_for(std::chrono::seconds(1));
      std::cout << '.' << std::flush;
      auto instance = instance_future.get();
      if (!instance) throw std::move(instance).status();
      std::cout << "DONE, details=" << instance->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Creates a production instance with "<intanceId>-prod" instance ID,
    // with cluster ID "ssd-cluster1", 3 nodes and location us-east1-b.
    displayName += " Prod"; // Display name is for display purposes only. It doesn't have to equal instanceId and can be amended after instance is created.
    string instanceId = Regex.Replace(displayName, @"[^A-Za-z0-9_\.~]+", "-").ToLower();
    
    // Please refer to the link below for the full list of available locations:
    // https://cloud.google.com/bigtable/docs/locations
    string zone1 = "us-east1-b";
    
    // The instance to create.
    Instance myInstance = new Instance
    {
        DisplayName = displayName,
        // You can choose DEVELOPMENT or PRODUCTION type here.
        // If not set, will default to PRODUCTION type.
        // Instance type can be upgraded from DEVELOPMENT to PRODUCTION but cannot be dowgraded after the instance is created.
        Type = Instance.Types.Type.Production,
        Labels = { { "prod-label", "prod-label" } }
    };
    
    // The first cluster to be created within the instance.
    Cluster myCluster1 = new Cluster
    {
        // You can choose SSD or HDD storage type here: StorageType.Ssd or StorageType.Hdd.
        // Cluster storage type can not be changed after the instance is created.
        // If not set will default to SSD type.
        DefaultStorageType = StorageType.Ssd,
        LocationAsLocationName = new LocationName(projectId, zone1),
        // Serve Nodes count can only be set if PRODUCTION type instance is being created.
        // Minimum count of 3 serve nodes must be specified.
        // Serve Nodes count can be increased and decreased after an instance is created.
        ServeNodes = 3
    };
    
    // Initialize request argument(s).
    CreateInstanceRequest request = new CreateInstanceRequest
    {
        ParentAsProjectName = new ProjectName(projectId),
        Instance = myInstance,
        InstanceId = instanceId,
        // Must specify at lease one cluster.
        // Only PRODUCTION type instance can be created with more than one cluster.
        // Currently all clusters must have the same storage type.
        // Clusters must be set to different locations.
        Clusters = { { "ssd-cluster1", myCluster1 } }
    };
    
    try
    {
        // Make a request.
        Operation<Instance, CreateInstanceMetadata> createInstanceResponse =
            bigtableInstanceAdminClient.CreateInstance(request);
        Console.WriteLine("Waiting for operation to complete...");
    
        // Poll until the returned long-running operation is complete
        Operation<Instance, CreateInstanceMetadata> completedResponse =
            createInstanceResponse.PollUntilCompleted();
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Exception while creating {displayName} instance");
        Console.WriteLine(ex.Message);
    }

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Instance admin is a sample program demonstrating use of the Cloud Bigtable client
    // library to perform basic instance admin operations.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"io"
    	"os"
    
    	"cloud.google.com/go/bigtable"
    )
    
    func main() {
    	projectID := "my-project-id" // The Google Cloud Platform project ID
    	instanceID := "my-bigtable-instance"
    	clusterID := "my-cluster"
    	zone := "us-central1-b"
    
    	// Allow overriding with flags
    	flag.StringVar(&projectID, "project", projectID, "The Google Cloud Platform project ID.")
    	flag.StringVar(&instanceID, "instance", instanceID, "The Google Cloud Bigtable instance ID to create.")
    	flag.StringVar(&zone, "zone", zone, "The zone for the initial cluster.")
    	flag.Parse()
    
    	if err := createInstance(os.Stdout, projectID, instanceID, clusterID, zone); err != nil {
    		fmt.Fprintf(os.Stderr, "Error creating instance: %v", err)
    	}
    }
    
    func createInstance(w io.Writer, projectID, instanceID, clusterID, zone string) error {
    	ctx := context.Background()
    
    	instanceAdminClient, err := bigtable.[NewInstanceAdminClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_InstanceAdminClient_NewInstanceAdminClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigtable.NewInstanceAdminClient: %w", err)
    	}
    	defer instanceAdminClient.Close()
    
    	// These are placeholders. You must create these in your GCP Organization/Project first.
    	// See [Creating and managing tags](https://docs.cloud.google.com/bigtable/docs/tags) for
    	// more information on creating a tag.
    	// tagKey := "tagKeys/12345"
    	// tagValue := "tagValues/56789"
    
    	instanceConf := &bigtable.[InstanceConf](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_InstanceConf){
    		InstanceId:   instanceID,
    		DisplayName:  instanceID,
    		ClusterId:    clusterID,
    		NumNodes:     1,
    		InstanceType: bigtable.[PRODUCTION](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_UNSPECIFIED_PRODUCTION_DEVELOPMENT),
    		StorageType:  bigtable.[SSD](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_SSD_HDD),
    		Zone:         zone,
    		// The 'Tags' field is optional. Uncomment the lines below (and the tagKey, tagValue lines above)
    		// only if you want to create an instance with tags.
    		// Ensure the tagKey and tagValue exist in your GCP project.
    		// Tags: map[string]string{tagKey: tagValue},
    	}
    
    	fmt.Fprintf(w, "Creating instance %s with cluster %s in %s...\n", instanceID, clusterID, zone)
    
    	if err := instanceAdminClient.CreateInstance(ctx, instanceConf); err != nil {
    		return fmt.Errorf("CreateInstance: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance %s created successfully.\n", instanceID)
    	return nil
    }
    
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Creates a Production Instance with the ID "ssd-instance",
    // cluster id "ssd-cluster", 3 nodes and location "us-central1-f".
    String parent = "projects/" + projectId;
    Instance.Builder instanceObjBuilder =
        Instance.newBuilder()
            .setDisplayName(instanceId)
            .setType(Instance.Type.PRODUCTION)
            .putLabels("department", "accounting");
    
    if (createWithTags) {
      System.out.println("Enabling tags for instance creation.");
      // These are placeholders. You must create these in your GCP Organization/Project first.
      String tagKey = "tagKeys/12345";
      String tagValue = "tagValues/6789";
      instanceObjBuilder.putTags(tagKey, tagValue);
    }
    Instance instanceObj = instanceObjBuilder.build();
    
    Cluster clusterObj =
        Cluster.newBuilder()
            .setLocation("projects/" + projectId + "/locations/us-central1-f")
            .setServeNodes(3)
            .setDefaultStorageType(StorageType.SSD)
            .build();
    CreateInstanceRequest request =
        CreateInstanceRequest.newBuilder()
            .setParent(parent)
            .setInstanceId(instanceId)
            .setInstance(instanceObj)
            .putClusters(clusterId, clusterObj)
            .build();
    // Creates a production instance with the given request.
    try {
      Instance instance = adminClient.createInstanceAsync(request).get();
      System.out.printf("PRODUCTION type instance %s created successfully%n", instance.getName());
    } catch (Exception e) {
      System.err.println("Failed to create instance: " + e.getMessage());
      throw new RuntimeException(e);
    }

### Node.js

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Creates a Production Instance with the ID "ssd-instance"
    // with cluster id "ssd-cluster", 3 nodes and location us-central1-f
    const {BigtableInstanceAdminClient} = require('[@google-cloud/bigtable](https://docs.cloud.google.com/nodejs/docs/reference/bigtable/latest/overview.html)').v2;
    const instanceAdminClient = new [BigtableInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/bigtable-api/latest/overview.html)();
    const projectId = await instanceAdminClient.getProjectId();
    
    const instanceOptions = {
      parent: `projects/${projectId}`,
      instanceId: instanceID,
      instance: {
        displayName: instanceID,
        labels: {'prod-label': 'prod-label'},
        type: 'PRODUCTION',
      },
      clusters: {
        [clusterID]: {
          location: `projects/${projectId}/locations/us-central1-f`,
          serveNodes: 3,
          defaultStorageType: 'SSD',
        },
      },
    };
    
    // Create production instance with given options
    const [prodInstance, operation] =
      await instanceAdminClient.createInstance(instanceOptions);
    await operation.promise();
    console.log(`Created Instance: ${prodInstance.name}`);

### PHP

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Exception;
    use Google\ApiCore\ApiException;
    use Google\Cloud\Bigtable\Admin\V2\Client\BigtableInstanceAdminClient;
    use Google\Cloud\Bigtable\Admin\V2\Cluster;
    use Google\Cloud\Bigtable\Admin\V2\CreateInstanceRequest;
    use Google\Cloud\Bigtable\Admin\V2\GetInstanceRequest;
    use Google\Cloud\Bigtable\Admin\V2\Instance;
    use Google\Cloud\Bigtable\Admin\V2\Instance\Type as InstanceType;
    use Google\Cloud\Bigtable\Admin\V2\StorageType;
    
    /**
     * Create a production Bigtable instance
     *
     * @param string $projectId The Google Cloud project ID
     * @param string $instanceId The ID of the Bigtable instance to be generated
     * @param string $clusterId The ID of the cluster to be generated
     * @param string $locationId The Bigtable region ID where you want your instance to reside
     */
    function create_production_instance(
        string $projectId,
        string $instanceId,
        string $clusterId,
        string $locationId = 'us-east1-b'
    ): void {
        $instanceAdminClient = new BigtableInstanceAdminClient();
    
        $projectName = $instanceAdminClient->projectName($projectId);
        $instanceName = $instanceAdminClient->instanceName($projectId, $instanceId);
    
        $serveNodes = 3;
        $storageType = StorageType::SSD;
        $production = InstanceType::PRODUCTION;
        $labels = ['prod-label' => 'prod-label'];
    
        $instance = new Instance();
        $instance->setDisplayName($instanceId);
    
        $instance->setLabels($labels);
        $instance->setType($production);
    
        $cluster = new Cluster();
        $cluster->setDefaultStorageType($storageType);
        $locationName = $instanceAdminClient->locationName($projectId, $locationId);
        $cluster->setLocation($locationName);
        $cluster->setServeNodes($serveNodes);
        $clusters = [
            $clusterId => $cluster
        ];
        try {
            $getInstanceRequest = (new GetInstanceRequest())
                ->setName($instanceName);
            $instanceAdminClient->getInstance($getInstanceRequest);
            printf('Instance %s already exists.' . PHP_EOL, $instanceId);
            throw new Exception(sprintf('Instance %s already exists.' . PHP_EOL, $instanceId));
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('Creating an Instance: %s' . PHP_EOL, $instanceId);
                $createInstanceRequest = (new CreateInstanceRequest())
                    ->setParent($projectName)
                    ->setInstanceId($instanceId)
                    ->setInstance($instance)
                    ->setClusters($clusters);
                $operationResponse = $instanceAdminClient->createInstance($createInstanceRequest);
                $operationResponse->pollUntilComplete();
                if (!$operationResponse->operationSucceeded()) {
                    print('Error: ' . $operationResponse->getError()->getMessage());
                } else {
                    printf('Instance %s created.', $instanceId);
                }
            } else {
                throw $e;
            }
        }
    }

### Python

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cluster = instance.cluster(
        cluster_id,
        location_id=location_id,
        serve_nodes=serve_nodes,
        default_storage_type=storage_type,
    )
    if not instance.exists():
        print("\nCreating an instance")
        # Create instance with given options
        operation = instance.create(clusters=[cluster])
        # Ensure the operation completes.
        operation.result(timeout=480)
        print("\nCreated instance: {}".format(instance_id))

### Ruby

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # instance_id      = "my-instance"
    # cluster_id       = "my-cluster"
    # cluster_location = "us-east1-b"
    puts "Creating a PRODUCTION Instance"
    job = bigtable.create_instance(
      instance_id,
      display_name: "Sample production instance",
      labels:       { "env": "production" },
      type:         :PRODUCTION # Optional as default type is :PRODUCTION
    ) do |clusters|
      clusters.add cluster_id, cluster_location, nodes: 3, storage_type: :SSD
    end
    
    job.wait_until_done!
    instance = job.instance
    puts "Created Instance: #{instance.instance_id}"

## What's next

  * Find out how Bigtable uses [instances, clusters, and nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes).
  * Learn about [Bigtable replication](https://docs.cloud.google.com/bigtable/docs/replication-overview).
  * [Review and update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) for replication, and [create custom app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile) as needed.
  * Find out how to [modify an existing instance](https://docs.cloud.google.com/bigtable/docs/modifying-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
