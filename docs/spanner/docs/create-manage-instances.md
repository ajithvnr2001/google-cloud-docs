---
url: https://docs.cloud.google.com/spanner/docs/create-manage-instances/
title: Create and manage instances \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:45.533649+00:00
---

# Create and manage instances  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/create-manage-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Create and manage instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create, list, edit, and delete Spanner [instances](https://docs.cloud.google.com/spanner/docs/instances).

**Note:** To explore Spanner using a 90-day free trial instance, see [Create a Spanner free trial instance](https://docs.cloud.google.com/spanner/docs/free-trial-quickstart).

## Create an instance

You can create an instance with the Google Cloud console, the [Google Cloud CLI](https://docs.cloud.google.com/spanner/docs/gcloud-spanner), or client libraries. You can also create an instance with a [custom instance configuration](https://docs.cloud.google.com/spanner/docs/instance-configurations#configuration) by adding optional [read-only replicas](https://docs.cloud.google.com/spanner/docs/replication#read-only).

**Note:** You don't need to provision storage in Spanner, and you are billed only for the storage that you use. Learn more about [storage pricing](https://docs.cloud.google.com/spanner/pricing#storage).

### Console

  1. In the Google Cloud console, go to the **Spanner Instances** page.

  2. Click **Create instance**.

[Go to Create instance](https://console.cloud.google.com/spanner/instances/new)

  3. In the **Select an edition** section, select a Spanner edition.

If you want to compare the specifications between the different editions, then click **Compare editions**. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview).

  4. Click **Continue**.

  5. In the **Name your instance** section, enter an **Instance name** to display in the Google Cloud console. The instance name must be unique within your Google Cloud project.

  6. Enter an **Instance ID** to permanently identify your instance. The instance ID must also be unique within your Google Cloud project. You can't change the instance ID later.

  7. Click **Continue**.

  8. In the **Configure your instance** section, under **Choose a configuration** , select **Regional** , **Dual-region** , or **Multi-region**.

**Note:** Dual-region and multi-region instance configurations are only available in the Enterprise Plus edition. If you want to compare the specifications between the three configurations, then click **Compare region configurations**.
  9. Select a configuration location from the drop-down.

  10. Optional: To add a read-only replica to a Spanner base configuration, first [create a custom instance configuration using the Google Cloud CLI](https://docs.cloud.google.com/spanner/docs/create-manage-configurations#gcloud_2). Adding optional read-only replicas to a base configuration is available in the [Enterprise edition and Enterprise Plus edition](https://docs.cloud.google.com/spanner/docs/editions-overview#features).

  11. Click **Continue**.

  12. In the **Allocate compute capacity** section, under **Select unit** , click one of the following:

     * **Nodes** for large instances. A node is 1000 processing units.
     * **Processing units** for small instances.

For more information, see [Compute capacity, nodes and processing units](https://docs.cloud.google.com/spanner/docs/compute-capacity).

  13. Under **Choose a scaling mode** , click one of the following:

     * **Manual allocation** if you want to manually set compute capacity for fixed compute resources and costs.

       * **Quantity** indicates the number of processing units or nodes to use for this instance.
     * **Autoscaling** to let Spanner automatically add and remove compute capacity. Managed autoscaler is available in the [Spanner Enterprise edition and Enterprise Plus edition](https://docs.cloud.google.com/spanner/docs/editions-overview). For more information about the managed autoscaler, see [Managed autoscaler for Spanner](https://docs.cloud.google.com/spanner/docs/managed-autoscaler). Configure the following managed autoscaler options:

       * **Minimum** indicates the minimum limit to scale down to, depending on the measurement unit that you choose for **Compute capacity**. For more information, see [Determine the minimum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-minimum).
       * **Maximum** indicates the maximum limit to scale up to, depending on the measurement unit that you choose for **Compute capacity**. For more information, see [Determine the maximum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-maximum).
       * **High priority CPU utilization target** indicates the target percentage of CPU to use for high priority tasks. For more information, see [Determine the CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-high-priority-cpu).
       * **Total CPU utilization target** indicates the target percentage of CPU to use for all low, medium, and high priority tasks. For more information, see [Determine the total CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-total-cpu).
       * **Storage utilization target** indicates the target percentage of storage to use. For more information, see [Determine the Storage Utilization Target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-storage).
  14. Optional: If you select **Autoscaling** as the scaling mode, you can click the **Show asymmetric autoscaling options** dropdown to autoscale your read-only replicas independently from other replicas. For more information, see [Asymmetric read-only autoscaling](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#asymmetric-read-only-autoscaling).

     1. Select the read-only replica you want to asymmetrically autoscale.

     2. Configure the following asymmetric autoscaler options:

        * **Minimum** indicates the minimum limit to scale down to, depending on the measurement unit that you choose for **Compute capacity**. For more information, see [Determine the minimum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-minimum).
        * **Maximum** indicates the maximum limit to scale up to, depending on the measurement unit that you choose for **Compute capacity**. For more information, see [Determine the maximum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-maximum).
        * **High priority CPU utilization target** indicates the target percentage of CPU to use for [high priority tasks](https://docs.cloud.google.com/spanner/docs/cpu-utilization#task-priority). For more information, see [Determine the high priority CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-high-priority-cpu).
        * **Total CPU utilization target** indicates the target percentage of CPU to use for all [low, medium, and high priority tasks](https://docs.cloud.google.com/spanner/docs/cpu-utilization#task-priority). The CPU percentage can range from 10 to 90%. The total CPU target has to be greater than the high priority CPU target. If you're optimizing for cost, then use a higher percentage. For more information, see [Determine the total CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-total-cpu).
        * **Disable total CPU** indicates that the autoscaler should explicitly ignore the total CPU target.
        * **Disable high priority CPU** indicates that the autoscaler should explicitly ignore the CPU target for high priority tasks.
  15. Under **Backups** , the **Enable default backup schedules** checkbox is checked by default. To disable default backup schedules, uncheck the checkbox. When enabled, all new databases in the instance have full backups created every 24 hours. These backups are retained for 7 days. You can edit or delete the default backup schedules at any time. For more information, see [Default backup schedules](https://docs.cloud.google.com/spanner/docs/backup#default-backup-schedules).

  16. Click **Create** to create the instance.




###  gcloud 

Use the [`gcloud spanner instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/create) command to create an instance. Specify the [compute capacity](https://docs.cloud.google.com/spanner/docs/compute-capacity) as the number of nodes or processing units that you want on the instance.
    
    
    gcloud spanner instances create INSTANCE_ID \
    --edition=EDITION \
    --config=INSTANCE_CONFIG \
    --description=INSTANCE_DESCRIPTION \
    --default-backup-schedule-type=DEFAULT_BACKUP_SCHEDULE_TYPE \
    --nodes=NODE_COUNT

or
    
    
    gcloud spanner instances create INSTANCE_ID \
    --edition=EDITION \
    --config=INSTANCE_CONFIG \
    --description=INSTANCE_DESCRIPTION \
    --default-backup-schedule-type=DEFAULT_BACKUP_SCHEDULE_TYPE \
    --processing-units=PROCESSING_UNIT_COUNT

Replace the following:

  * INSTANCE-ID: a permanent identifier that is unique within your Google Cloud project. You can't change the instance ID later.
  * INSTANCE-CONFIG: a permanent identifier of your instance configuration, which defines the geographic location of the instance and affects how data is replicated. For custom instance configurations, it starts with `custom-`. For more information, see [instance configurations](https://docs.cloud.google.com/spanner/docs/instances).
  * INSTANCE_DESCRIPTION: the name to display for the instance in the Google Cloud console. The instance name must be unique within your Google Cloud project.
  * DEFAULT_BACKUP_SCHEDULE_TYPE: the default backup schedule type that is used in the instance. Must be one of the following values:

    * `AUTOMATIC`: a default backup schedule is created automatically when a new database is created in the instance. The default backup schedule creates a full backup every 24 hours. These full backups are retained for 7 days. You can edit or delete the default backup schedule once it's created.
    * `NONE`: a default backup schedule isn't created automatically when a new database is created in the instance.
  * NODE-COUNT: the compute capacity of the instance, expressed as a number of nodes. Each node equals 1000 processing units.

  * PROCESSING_UNIT_COUNT: the compute capacity of the instance, expressed as a number of processing units. Enter quantities up to 1000 in multiples of 100 (100, 200, 300 and so on) and enter greater quantities in multiples of 1000 (1000, 2000, 3000 and so on). Note: Don't use this parameter if you're creating an instance that you intend to enable with the managed autoscaler later.




### Add managed autoscaling

You can also create [Enterprise edition and Enterprise Plus edition](https://docs.cloud.google.com/spanner/docs/editions-overview) instances to use managed autoscaling with the [`gcloud spanner instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/create) command. For more information, see [Managed autoscaler for Spanner](https://docs.cloud.google.com/spanner/docs/managed-autoscaler).

Use the following command to create an instance with managed autoscaler.
    
    
      gcloud spanner instances create INSTANCE_ID \
        --edition=EDITION \
        --config=INSTANCE_CONFIG \
        --description=INSTANCE_DESCRIPTION \
        --autoscaling-min-processing-units=MINIMUM_PROCESSING_UNITS \
        --autoscaling-max-processing-units=MAXIMUM_PROCESSING_UNITS \
        --autoscaling-high-priority-cpu-target=HIGH_PRIORITY_CPU_PERCENTAGE \
        --autoscaling-total-cpu-target=TOTAL_CPU_PERCENTAGE \
        --autoscaling-storage-target=STORAGE_PERCENTAGE \
        [--disable-downscaling | --no-disable-downscaling] \
        [--asymmetric-autoscaling-option \
           location=ASYMMETRIC_AUTOSCALING_LOCATION,\
           min_nodes=ASYMMETRIC_AUTOSCALING_MIN,\
           max_nodes=ASYMMETRIC_AUTOSCALING_MAX,\
           high_priority_cpu_target=ASYMMETRIC_HIGH_PRIORITY_CPU_TARGET,\
           total_cpu_target=ASYMMETRIC_TOTAL_CPU_TARGET \
           [,disable_total_cpu_autoscaling=TRUE|FALSE \
           | disable_high_priority_cpu_autoscaling=TRUE|FALSE]
        ]

or
    
    
      gcloud spanner instances create INSTANCE_ID \
        --edition=EDITION \
        --config=INSTANCE_CONFIG \
        --description=INSTANCE_DESCRIPTION \
        --autoscaling-min-nodes=MINIMUM_NODES \
        --autoscaling-max-nodes=MAXIMUM_NODES \
        --autoscaling-high-priority-cpu-target=HIGH_PRIORITY_CPU_PERCENTAGE \
        --autoscaling-total-cpu-target=TOTAL_CPU_PERCENTAGE \
        --autoscaling-storage-target=STORAGE_PERCENTAGE \
        [--disable-downscaling | --no-disable-downscaling] \
        [--asymmetric-autoscaling-option \
           location=ASYMMETRIC_AUTOSCALING_LOCATION,\
           min_nodes=ASYMMETRIC_AUTOSCALING_MIN,\
           max_nodes=ASYMMETRIC_AUTOSCALING_MAX,\
           high_priority_cpu_target=ASYMMETRIC_HIGH_PRIORITY_CPU_TARGET, \
           total_cpu_target=ASYMMETRIC_TOTAL_CPU_TARGET, \
           [,disable_total_cpu_autoscaling=TRUE|FALSE \
           | disable_high_priority_cpu_autoscaling=TRUE|FALSE]
        ]

Replace the following:

  * INSTANCE-ID: a permanent identifier that is unique within your Google Cloud project. You can't change the instance ID later.
  * INSTANCE-CONFIG: a permanent identifier of your instance configuration, which defines the geographic location of the instance and affects how data is replicated. For custom instance configurations, it starts with `custom-`. For more information, see [instance configurations](https://docs.cloud.google.com/spanner/docs/instances).
  * INSTANCE-DESCRIPTION: the name to display for the instance in the Google Cloud console. The instance name must be unique within your Google Cloud project.
  * MINIMUM_PROCESSING_UNITS, MINIMUM_NODES: the minimum number of processing units or nodes when scaling down. For more information, see [Determine the minimum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-minimum).
  * MAXIMUM_PROCESSING_UNITS, MAXIMUM_NODES: the maximum number of processing units or nodes when scaling up. For more information, see [Determine the maximum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-maximum).
  * HIGH_PRIORITY_CPU_PERCENTAGE: the target percentage of high priority CPU to use, based on the [priority of the task](https://docs.cloud.google.com/spanner/docs/cpu-utilization#task-priority). The CPU percentage can range from 10 to 90%. If you're optimizing for cost, then use a higher percentage. For more information, see [Determine the high priority CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-high-priority-cpu).
  * TOTAL_CPU_PERCENTAGE: the target percentage of total priority CPU to use. The total CPU target has to be greater than the high priority CPU target. The CPU percentage can range from 10 to 90%. If you're optimizing for cost, then use a higher percentage. For more information, see [Determine the total CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-total-cpu).
  * STORAGE_PERCENTAGE: the target percentage of storage to use, from 10 to 99%. For more information, see [Determine the storage utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-storage).



Optional flags:

  * `--disable-downscaling`: use this boolean flag to disable downscaling. When set to `TRUE`, it prevents the autoscaler from reducing the number of nodes or processing units. Upscaling continues to function normally to meet increased demand. To enable downscaling after disabling it, use the `--no-disable-downscaling` flag.
  * `--asymmetric-autoscaling-option`: use this flag to enable [asymmetric autoscaling](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#asymmetric-read-only-autoscaling). Replace the following parameters:

    * ASYMMETRIC_AUTOSCALING_LOCATION: if the flag is used, then this parameter is required. The location of the read-only region that you want to scale asymmetrically.
    * ASYMMETRIC_AUTOSCALING_MIN: optional parameter. The minimum number of nodes when scaling down. If not specified, this value is inherited from the base instance configuration.
    * ASYMMETRIC_AUTOSCALING_MAX: optional parameter. The maximum number of nodes when scaling up. If not specified, this value is inherited from the base instance configuration.
    * ASYMMETRIC_HIGH_PRIORITY_CPU_TARGET: optional parameter. The target percentage of CPU to use, based on the [priority of the task](https://docs.cloud.google.com/spanner/docs/cpu-utilization#task-priority). If not specified, this value is inherited from the base instance configuration. If you're optimizing for cost, then use a higher percentage. Replicas can have a different target percentage than the base instance and from other replicas, but for failover scenarios, we recommend that replicas use consistent targets across different replicas. For more information, see [Failover concerns](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#failover-concerns).
    * ASYMMETRIC_TOTAL_CPU_TARGET: optional parameter. Set the target from 10 to 90% for the [total CPU](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-total-cpu). If not specified, this value is inherited from the base instance configuration. If you're optimizing for cost, then use a higher percentage. Replicas can have a different target percentage than the base instance and from other replicas, but for failover scenarios, we recommend that replicas use consistent targets across different replicas. For more information, see [Asymmetric read-only autoscaling](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#asymmetric-read-only-autoscaling).
    * `disable_total_cpu_autoscaling`: set this parameter to `TRUE` if you don't want the autoscaler to autoscale total CPU on replicas. Don't specify this parameter if you want the instance to inherit the `total_cpu_autoscaling` target from the base instance. You can't disable both total CPU and high priority CPU on the same replica.
    * `disable_high_priority_cpu_autoscaling`: set the `disable_high_priority_cpu_autoscaling` to `TRUE` if you don't want the autoscaler to autoscale the high priority CPU on replicas. Don't specify this parameter if you want the instance to inherit the `high_priority_cpu_autoscaling` target from the base instance. You can't disable both total CPU and high priority CPU on the same replica.



### Examples for using custom configurations

To create an instance `test-instance` in the base regional instance configuration `us-central1`, run:
    
    
    gcloud spanner instances create test-instance --edition=STANDARD --config=regional-us-central1 \
      --description="Test Instance" --nodes=1
    

To create an instance `custom-eur6-instance` in the custom multi-region instance configuration `custom-eur6`, first [create a custom instance configuration](https://docs.cloud.google.com/spanner/docs/create-manage-configurations#create-configuration).

Then, run:
    
    
      gcloud spanner instances create custom-eur6-instance --edition=ENTERPRISE_PLUS --config=custom-eur6 \
          --description="Instance with custom read-only" --nodes=1
    

You should see a message similar to the following example after running either one of the previous commands:
    
    
    Creating instance...done.

### C++

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void CreateInstance(google::cloud::spanner_admin::InstanceAdminClient client,
                        std::string const& project_id,
                        std::string const& instance_id,
                        std::string const& display_name,
                        std::string const& config_id) {
      namespace spanner = ::google::cloud::spanner;
      spanner::Instance in(project_id, instance_id);
    
      auto project = google::cloud::Project(project_id);
      std::string config_name =
          project.FullName() + "/instanceConfigs/" + config_id;
      auto instance =
          client
              .CreateInstance(spanner::CreateInstanceRequestBuilder(in, config_name)
                                  .SetDisplayName(display_name)
                                  .SetNodeCount(1)
                                  .SetLabels({{"cloud_spanner_samples", "true"}})
                                  .Build())
              .get();
      if (!instance) throw std::move(instance).status();
      std::cout << "Created instance [" << in << "]:\n" << instance->DebugString();
    }

### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System;
    using System.Threading.Tasks;
    
    public class CreateInstanceAsyncSample
    {
        public async Task<Instance> CreateInstanceAsync(
            string projectId,
            string instanceId,
            Instance.Types.Edition edition = Instance.[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.html).[Edition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.Edition.html).[Standard](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.Edition.html#Google_Cloud_Spanner_Admin_Instance_V1_Instance_Types_Edition_Standard))
        {
            // Create the InstanceAdminClient instance.
            [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html) instanceAdminClient = await [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html#Google_Cloud_Spanner_Admin_Instance_V1_InstanceAdminClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Initialize request parameters.
            Instance instance = new Instance
            {
                InstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                ConfigAsInstanceConfigName = [InstanceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfigName.html).[FromProjectInstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfigName.html#Google_Cloud_Spanner_Admin_Instance_V1_InstanceConfigName_FromProjectInstanceConfig_System_String_System_String_)(projectId, "regional-us-central1"),
                DisplayName = "This is a display name.",
                NodeCount = 1,
                Labels =
                {
                    { "cloud_spanner_samples", "true" },
                },
                Edition = edition,
            };
            [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html).[FromProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_)(projectId);
    
            // Make the CreateInstance request.
            Operation<Instance, CreateInstanceMetadata> response = await instanceAdminClient.[CreateInstanceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html#Google_Cloud_Spanner_Admin_Instance_V1_InstanceAdminClient_CreateInstanceAsync_Google_Api_Gax_ResourceNames_ProjectName_System_String_Google_Cloud_Spanner_Admin_Instance_V1_Instance_Google_Api_Gax_Grpc_CallSettings_)(projectName, instanceId, instance);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            Operation<Instance, CreateInstanceMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while creating instance: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            Console.WriteLine($"Instance created successfully.");
    
            return completedResponse.Result;
        }
    }

### Create an instance without a default backup schedule
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System;
    using System.Threading.Tasks;
    
    public class CreateInstanceWithoutDefaultBackupSchedulesAsyncSample
    {
        public async Task<Instance> CreateInstanceWithoutDefaultBackupSchedulesAsync(string projectId, string instanceId)
        {
            // Create the InstanceAdminClient instance.
            [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html) instanceAdminClient = await [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html#Google_Cloud_Spanner_Admin_Instance_V1_InstanceAdminClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Initialize request parameters.
            Instance instance = new Instance
            {
                InstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                ConfigAsInstanceConfigName =
                    [InstanceConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfigName.html).[FromProjectInstanceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceConfigName.html#Google_Cloud_Spanner_Admin_Instance_V1_InstanceConfigName_FromProjectInstanceConfig_System_String_System_String_)(projectId, "regional-me-central2"),
                DisplayName = "This is a display name.",
                NodeCount = 1,
                Labels =
                {
                    { "cloud_spanner_samples", "true" },
                },
                DefaultBackupScheduleType = Instance.[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.html).[DefaultBackupScheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.DefaultBackupScheduleType.html).[None](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.DefaultBackupScheduleType.html#Google_Cloud_Spanner_Admin_Instance_V1_Instance_Types_DefaultBackupScheduleType_None),
            };
            [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html).[FromProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_)(projectId);
    
            // Make the CreateInstance request.
            Operation<Instance, CreateInstanceMetadata> response =
                await instanceAdminClient.[CreateInstanceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html#Google_Cloud_Spanner_Admin_Instance_V1_InstanceAdminClient_CreateInstanceAsync_Google_Api_Gax_ResourceNames_ProjectName_System_String_Google_Cloud_Spanner_Admin_Instance_V1_Instance_Google_Api_Gax_Grpc_CallSettings_)(projectName, instanceId, instance);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            Operation<Instance, CreateInstanceMetadata> completedResponse =
                await response.PollUntilCompletedAsync();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while creating instance: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            Console.WriteLine($"Instance created successfully.");
            return completedResponse.Result;
        }
    }

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	instance "cloud.google.com/go/spanner/admin/instance/apiv1"
    	"cloud.google.com/go/spanner/admin/instance/apiv1/instancepb"
    )
    
    func createInstance(w io.Writer, projectID, instanceID string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance"
    	ctx := context.Background()
    	instanceAdmin, err := instance.NewInstanceAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer instanceAdmin.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1.html#cloud_google_com_go_spanner_admin_instance_apiv1_InstanceAdminClient_Close)()
    
    	op, err := instanceAdmin.CreateInstance(ctx, &instancepb.CreateInstanceRequest{
    		Parent:     fmt.Sprintf("projects/%s", projectID),
    		InstanceId: instanceID,
    		Instance: &instancepb.Instance{
    			Config:      fmt.Sprintf("projects/%s/instanceConfigs/%s", projectID, "regional-us-central1"),
    			DisplayName: instanceID,
    			NodeCount:   1,
    			Labels:      map[string]string{"cloud_spanner_samples": "true"},
    			Edition:     instancepb.[Instance_STANDARD](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_EDITION_UNSPECIFIED_Instance_STANDARD_Instance_ENTERPRISE_Instance_ENTERPRISE_PLUS),
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("could not create instance %s: %w", fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID), err)
    	}
    	// Wait for the instance creation to finish.
    	i, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("waiting for instance creation to finish failed: %w", err)
    	}
    	// The instance may not be ready to serve yet.
    	if i.State != instancepb.[Instance_READY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_STATE_UNSPECIFIED_Instance_CREATING_Instance_READY) {
    		fmt.Fprintf(w, "instance state is not READY yet. Got state %v\n", i.State)
    	}
    	fmt.Fprintf(w, "Created instance [%s]\n", instanceID)
    	return nil
    }
    

### Create an instance with managed autoscaling using Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	instance "cloud.google.com/go/spanner/admin/instance/apiv1"
    	"cloud.google.com/go/spanner/admin/instance/apiv1/instancepb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // Example of creating an autoscaling instance with Go.
    // projectID is the ID of the project that the new instance will be in.
    // instanceID is the ID of the new instance to be created.
    func createInstanceWithAutoscalingConfig(w io.Writer, projectID, instanceID string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance"
    	ctx := context.Background()
    	instanceAdmin, err := instance.NewInstanceAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("could not create instance admin client for project %s: %w", projectID, err)
    	}
    	defer instanceAdmin.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1.html#cloud_google_com_go_spanner_admin_instance_apiv1_InstanceAdminClient_Close)()
    
    	instanceName := fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID)
    	fmt.Fprintf(w, "Creating instance %s.", instanceName)
    
    	op, err := instanceAdmin.CreateInstance(ctx, &instancepb.CreateInstanceRequest{
    		Parent:     fmt.Sprintf("projects/%s", projectID),
    		InstanceId: instanceID,
    		Instance: &instancepb.Instance{
    			Config:      fmt.Sprintf("projects/%s/instanceConfigs/%s", projectID, "regional-us-central1"),
    			DisplayName: "Create instance example",
    			AutoscalingConfig: &instancepb.AutoscalingConfig{
    				AutoscalingLimits: &instancepb.AutoscalingConfig_AutoscalingLimits{
    					MinLimit: &instancepb.AutoscalingConfig_AutoscalingLimits_MinNodes{
    						MinNodes: 1,
    					},
    					MaxLimit: &instancepb.AutoscalingConfig_AutoscalingLimits_MaxNodes{
    						MaxNodes: 2,
    					},
    				},
    				AutoscalingTargets: &instancepb.AutoscalingConfig_AutoscalingTargets{
    					HighPriorityCpuUtilizationPercent: 65,
    					StorageUtilizationPercent:         95,
    				},
    			},
    			Labels:  map[string]string{"cloud_spanner_samples": "true"},
    			Edition: instancepb.[Instance_ENTERPRISE_PLUS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_EDITION_UNSPECIFIED_Instance_STANDARD_Instance_ENTERPRISE_Instance_ENTERPRISE_PLUS),
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("could not create instance %s: %w", instanceName, err)
    	}
    	fmt.Fprintf(w, "Waiting for operation on %s to complete...", instanceID)
    	// Wait for the instance creation to finish.
    	i, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("waiting for instance creation to finish failed: %w", err)
    	}
    	// The instance may not be ready to serve yet.
    	if i.State != instancepb.[Instance_READY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_STATE_UNSPECIFIED_Instance_CREATING_Instance_READY) {
    		fmt.Fprintf(w, "instance state is not READY yet. Got state %v\n", i.State)
    	}
    	fmt.Fprintf(w, "Created instance [%s].\n", instanceID)
    
    	instance, err := instanceAdmin.GetInstance(ctx, &instancepb.GetInstanceRequest{
    		Name: instanceName,
    		// Get the autoscaling_config field from the newly created instance.
    		FieldMask: &field_mask.FieldMask{Paths: []string{"autoscaling_config"}},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to get instance [%s]: %w", instanceName, err)
    	}
    	fmt.Fprintf(w, "Instance %s has autoscaling_config: %s.", instanceID, instance.AutoscalingConfig)
    	return nil
    }
    

### Create an instance with asymmetric read-only autoscaling using Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	instance "cloud.google.com/go/spanner/admin/instance/apiv1"
    	"cloud.google.com/go/spanner/admin/instance/apiv1/instancepb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // createInstanceWithAsymmetricAutoscalingConfig is a code snippet to show
    // an example of creating an asymmetric autoscaling enabled instance in Go.
    //
    // projectID is the ID of the project that the new instance will be in.
    // instanceID is the ID of the new instance to be created.
    func createInstanceWithAsymmetricAutoscalingConfig(w io.Writer, projectID, instanceID string) error {
    	ctx := context.Background()
    	instanceAdmin, err := instance.NewInstanceAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("could not create instance admin client for project %s: %w", projectID, err)
    	}
    	defer instanceAdmin.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1.html#cloud_google_com_go_spanner_admin_instance_apiv1_InstanceAdminClient_Close)()
    
    	instanceName := fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID)
    	fmt.Fprintf(w, "Creating instance %s.", instanceName)
    
    	op, err := instanceAdmin.CreateInstance(ctx, &instancepb.CreateInstanceRequest{
    		Parent:     fmt.Sprintf("projects/%s", projectID),
    		InstanceId: instanceID,
    		Instance: &instancepb.Instance{
    			Config:      fmt.Sprintf("projects/%s/instanceConfigs/%s", projectID, "nam-eur-asia3"),
    			DisplayName: "Create instance example",
    			AutoscalingConfig: &instancepb.AutoscalingConfig{
    				AutoscalingLimits: &instancepb.AutoscalingConfig_AutoscalingLimits{
    					MinLimit: &instancepb.AutoscalingConfig_AutoscalingLimits_MinNodes{
    						MinNodes: 1,
    					},
    					MaxLimit: &instancepb.AutoscalingConfig_AutoscalingLimits_MaxNodes{
    						MaxNodes: 10,
    					},
    				},
    				AutoscalingTargets: &instancepb.AutoscalingConfig_AutoscalingTargets{
    					HighPriorityCpuUtilizationPercent: 65,
    					StorageUtilizationPercent:         95,
    				},
    				// Read-only replicas in europe-west1, europe-west4, and asia-east1 are autoscaled
    				// independly from other replicas based on the usage in the respective region.
    				AsymmetricAutoscalingOptions: []*instancepb.AutoscalingConfig_AsymmetricAutoscalingOption{
    					&instancepb.AutoscalingConfig_AsymmetricAutoscalingOption{
    						ReplicaSelection: &instancepb.ReplicaSelection{
    							Location: "europe-west1",
    						},
    					},
    					&instancepb.AutoscalingConfig_AsymmetricAutoscalingOption{
    						ReplicaSelection: &instancepb.ReplicaSelection{
    							Location: "europe-west4",
    						},
    					},
    					&instancepb.AutoscalingConfig_AsymmetricAutoscalingOption{
    						ReplicaSelection: &instancepb.ReplicaSelection{
    							Location: "asia-east1",
    						},
    					},
    				},
    			},
    			Labels:  map[string]string{"cloud_spanner_samples": "true"},
    			Edition: instancepb.[Instance_ENTERPRISE_PLUS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_EDITION_UNSPECIFIED_Instance_STANDARD_Instance_ENTERPRISE_Instance_ENTERPRISE_PLUS),
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("could not create instance %s: %w", instanceName, err)
    	}
    	fmt.Fprintf(w, "Waiting for operation on %s to complete...", instanceID)
    	// Wait for the instance creation to finish.
    	i, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("waiting for instance creation to finish failed: %w", err)
    	}
    	// The instance may not be ready to serve yet.
    	if i.State != instancepb.[Instance_READY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_STATE_UNSPECIFIED_Instance_CREATING_Instance_READY) {
    		fmt.Fprintf(w, "instance state is not READY yet. Got state %v\n", i.State)
    	}
    	fmt.Fprintf(w, "Created instance [%s].\n", instanceID)
    
    	instance, err := instanceAdmin.GetInstance(ctx, &instancepb.GetInstanceRequest{
    		Name: instanceName,
    		// Get the autoscaling_config field from the newly created instance.
    		FieldMask: &field_mask.FieldMask{Paths: []string{"autoscaling_config"}},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to get instance [%s]: %w", instanceName, err)
    	}
    	fmt.Fprintf(w, "Instance %s has autoscaling_config: %s.", instanceID, instance.AutoscalingConfig)
    	return nil
    }
    

### Create an instance without a default backup schedule
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	instance "cloud.google.com/go/spanner/admin/instance/apiv1"
    	"cloud.google.com/go/spanner/admin/instance/apiv1/instancepb"
    )
    
    // createInstanceWithoutDefaultBackupSchedule creates instance with default backup schedule disabled.
    func createInstanceWithoutDefaultBackupSchedule(w io.Writer, projectID, instanceID string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance"
    	ctx := context.Background()
    	instanceAdmin, err := instance.NewInstanceAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer instanceAdmin.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1.html#cloud_google_com_go_spanner_admin_instance_apiv1_InstanceAdminClient_Close)()
    
    	// Create an instance without default backup schedule, whicn means no default backup schedule will
    	// be created automatically on creation of a database within the instance.
    	req := &instancepb.CreateInstanceRequest{
    		Parent:     fmt.Sprintf("projects/%s", projectID),
    		InstanceId: instanceID,
    		Instance: &instancepb.Instance{
    			Config:                    fmt.Sprintf("projects/%s/instanceConfigs/%s", projectID, "regional-us-central1"),
    			DisplayName:               instanceID,
    			NodeCount:                 1,
    			Labels:                    map[string]string{"cloud_spanner_samples": "true"},
    			DefaultBackupScheduleType: instancepb.[Instance_NONE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_DEFAULT_BACKUP_SCHEDULE_TYPE_UNSPECIFIED_Instance_NONE_Instance_AUTOMATIC),
    		},
    	}
    
    	op, err := instanceAdmin.CreateInstance(ctx, req)
    	if err != nil {
    		return fmt.Errorf("could not create instance %s: %w", fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID), err)
    	}
    	// Wait for the instance creation to finish.  For more information about instances, see
    	// https://cloud.google.com/spanner/docs/instances.
    	instance, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("waiting for instance creation to finish failed: %w", err)
    	}
    	// The instance may not be ready to serve yet.
    	if instance.State != instancepb.[Instance_READY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_STATE_UNSPECIFIED_Instance_CREATING_Instance_READY) {
    		fmt.Fprintf(w, "instance state is not READY yet. Got state %v\n", instance.State)
    	}
    	fmt.Fprintf(w, "Created instance [%s]\n", instanceID)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.instance.v1.[InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html);
    import com.google.spanner.admin.instance.v1.[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.html);
    import com.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html);
    import com.google.spanner.admin.instance.v1.[InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html);
    import com.google.spanner.admin.instance.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ProjectName.html);
    import java.util.concurrent.ExecutionException;
    
    class CreateInstanceExample {
    
      static void createInstance() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        createInstance(projectId, instanceId);
      }
    
      static void createInstance(String projectId, String instanceId) {
        // Set Instance configuration.
        int nodeCount = 2;
        String displayName = "Descriptive name";
    
        // Create an Instance object that will be used to create the instance.
        [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) instance =
            [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).newBuilder()
                .setDisplayName(displayName)
                .setEdition([Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).Edition.STANDARD)
                .setNodeCount(nodeCount)
                .setConfig([InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html).of(projectId, "regional-us-east4").toString())
                .build();
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
                [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html) instanceAdminClient = spanner.[createInstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createInstanceAdminClient__)()) {
    
          // Wait for the createInstance operation to finish.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) createdInstance =
              instanceAdminClient
                  .createInstanceAsync(
                      [CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.html).newBuilder()
                          .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ProjectName.html).of(projectId).toString())
                          .[setInstanceId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.Builder.html#com_google_spanner_admin_instance_v1_CreateInstanceRequest_Builder_setInstanceId_java_lang_String_)(instanceId)
                          .setInstance(instance)
                          .build())
                  .get();
          System.out.printf("Instance %s was successfully created%n", createdInstance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)());
        } catch (ExecutionException e) {
          System.out.printf(
              "Error: Creating instance %s failed with error message %s%n",
              instance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)(), e.getMessage());
        } catch (InterruptedException e) {
          System.out.println("Error: Waiting for createInstance operation to finish was interrupted");
        }
      }
    }

### Create an instance with managed autoscaling using Java
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.instance.v1.[InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html);
    import com.google.spanner.admin.instance.v1.[AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html);
    import com.google.spanner.admin.instance.v1.[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.html);
    import com.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html);
    import com.google.spanner.admin.instance.v1.[InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html);
    import com.google.spanner.admin.instance.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ProjectName.html);
    import com.google.spanner.admin.instance.v1.[ReplicaSelection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ReplicaSelection.html);
    import java.util.concurrent.ExecutionException;
    
    class CreateInstanceWithAsymmetricAutoscalingConfigExample {
    
      static void createInstance() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        createInstance(projectId, instanceId);
      }
    
      static void createInstance(String projectId, String instanceId) {
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder()
                .setProjectId(projectId)
                .build()
                .getService();
            [InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html) instanceAdminClient = spanner.[createInstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createInstanceAdminClient__)()) {
          // Set Instance configuration.
          String configId = "nam-eur-asia3";
          String displayName = "Descriptive name";
    
          // Create an autoscaling config.
          // When autoscaling_config is enabled, node_count and processing_units fields
          // need not be specified.
          // The read-only replicas listed in the asymmetric autoscaling options scale independently
          // from other replicas.
          [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html) autoscalingConfig =
              [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).newBuilder()
                  .setAutoscalingLimits(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AutoscalingLimits.newBuilder().[setMinNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimits.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingLimits_Builder_setMinNodes_int_)(1).[setMaxNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimits.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingLimits_Builder_setMaxNodes_int_)(2))
                  .[setAutoscalingTargets](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_Builder_setAutoscalingTargets_com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingTargets_)(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AutoscalingTargets.newBuilder()
                          .[setHighPriorityCpuUtilizationPercent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingTargets.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingTargets_Builder_setHighPriorityCpuUtilizationPercent_int_)(65)
                          .[setStorageUtilizationPercent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingTargets.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingTargets_Builder_setStorageUtilizationPercent_int_)(95))
                  .[addAsymmetricAutoscalingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_Builder_addAsymmetricAutoscalingOptions_com_google_spanner_admin_instance_v1_AutoscalingConfig_AsymmetricAutoscalingOption_)(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AsymmetricAutoscalingOption.newBuilder()
                      .setReplicaSelection([ReplicaSelection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ReplicaSelection.html).newBuilder().setLocation("europe-west1")))
                  .[addAsymmetricAutoscalingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_Builder_addAsymmetricAutoscalingOptions_com_google_spanner_admin_instance_v1_AutoscalingConfig_AsymmetricAutoscalingOption_)(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AsymmetricAutoscalingOption.newBuilder()
                      .setReplicaSelection([ReplicaSelection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ReplicaSelection.html).newBuilder().setLocation("europe-west4")))
                  .[addAsymmetricAutoscalingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_Builder_addAsymmetricAutoscalingOptions_com_google_spanner_admin_instance_v1_AutoscalingConfig_AsymmetricAutoscalingOption_)(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AsymmetricAutoscalingOption.newBuilder()
                      .setReplicaSelection([ReplicaSelection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ReplicaSelection.html).newBuilder().setLocation("asia-east1")))
                  .build();
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) instance =
              [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).newBuilder()
                  .setAutoscalingConfig(autoscalingConfig)
                  .setDisplayName(displayName)
                  .setConfig(
                      [InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html).of(projectId, configId).toString())
                  .build();
    
          // Creates a new instance
          System.out.printf("Creating instance %s.%n", instanceId);
          try {
            // Wait for the createInstance operation to finish.
            [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) instanceResult = instanceAdminClient.createInstanceAsync(
                [CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.html).newBuilder()
                    .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ProjectName.html).of(projectId).toString())
                    .[setInstanceId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.Builder.html#com_google_spanner_admin_instance_v1_CreateInstanceRequest_Builder_setInstanceId_java_lang_String_)(instanceId)
                    .setInstance(instance)
                    .build()).get();
            System.out.printf("Asymmetric Autoscaling instance %s was successfully created%n",
                instanceResult.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)());
          } catch (ExecutionException e) {
            System.out.printf(
                "Error: Creating instance %s failed with error message %s%n",
                instance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)(), e.getMessage());
          } catch (InterruptedException e) {
            System.out.println("Error: Waiting for createInstance operation to finish was interrupted");
          }
        }
      }
    }

### Create an instance with asymmetric read-only autoscaling using Java
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.instance.v1.[InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html);
    import com.google.spanner.admin.instance.v1.[AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html);
    import com.google.spanner.admin.instance.v1.[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.html);
    import com.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html);
    import com.google.spanner.admin.instance.v1.[InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html);
    import com.google.spanner.admin.instance.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ProjectName.html);
    import com.google.spanner.admin.instance.v1.[ReplicaSelection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ReplicaSelection.html);
    import java.util.concurrent.ExecutionException;
    
    class CreateInstanceWithAsymmetricAutoscalingConfigExample {
    
      static void createInstance() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        createInstance(projectId, instanceId);
      }
    
      static void createInstance(String projectId, String instanceId) {
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder()
                .setProjectId(projectId)
                .build()
                .getService();
            [InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html) instanceAdminClient = spanner.[createInstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createInstanceAdminClient__)()) {
          // Set Instance configuration.
          String configId = "nam-eur-asia3";
          String displayName = "Descriptive name";
    
          // Create an autoscaling config.
          // When autoscaling_config is enabled, node_count and processing_units fields
          // need not be specified.
          // The read-only replicas listed in the asymmetric autoscaling options scale independently
          // from other replicas.
          [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html) autoscalingConfig =
              [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).newBuilder()
                  .setAutoscalingLimits(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AutoscalingLimits.newBuilder().[setMinNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimits.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingLimits_Builder_setMinNodes_int_)(1).[setMaxNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingLimits.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingLimits_Builder_setMaxNodes_int_)(2))
                  .[setAutoscalingTargets](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_Builder_setAutoscalingTargets_com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingTargets_)(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AutoscalingTargets.newBuilder()
                          .[setHighPriorityCpuUtilizationPercent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingTargets.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingTargets_Builder_setHighPriorityCpuUtilizationPercent_int_)(65)
                          .[setStorageUtilizationPercent](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.AutoscalingTargets.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_AutoscalingTargets_Builder_setStorageUtilizationPercent_int_)(95))
                  .[addAsymmetricAutoscalingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_Builder_addAsymmetricAutoscalingOptions_com_google_spanner_admin_instance_v1_AutoscalingConfig_AsymmetricAutoscalingOption_)(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AsymmetricAutoscalingOption.newBuilder()
                      .setReplicaSelection([ReplicaSelection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ReplicaSelection.html).newBuilder().setLocation("europe-west1")))
                  .[addAsymmetricAutoscalingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_Builder_addAsymmetricAutoscalingOptions_com_google_spanner_admin_instance_v1_AutoscalingConfig_AsymmetricAutoscalingOption_)(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AsymmetricAutoscalingOption.newBuilder()
                      .setReplicaSelection([ReplicaSelection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ReplicaSelection.html).newBuilder().setLocation("europe-west4")))
                  .[addAsymmetricAutoscalingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.Builder.html#com_google_spanner_admin_instance_v1_AutoscalingConfig_Builder_addAsymmetricAutoscalingOptions_com_google_spanner_admin_instance_v1_AutoscalingConfig_AsymmetricAutoscalingOption_)(
                      [AutoscalingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.AutoscalingConfig.html).AsymmetricAutoscalingOption.newBuilder()
                      .setReplicaSelection([ReplicaSelection](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ReplicaSelection.html).newBuilder().setLocation("asia-east1")))
                  .build();
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) instance =
              [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).newBuilder()
                  .setAutoscalingConfig(autoscalingConfig)
                  .setDisplayName(displayName)
                  .setConfig(
                      [InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html).of(projectId, configId).toString())
                  .build();
    
          // Creates a new instance
          System.out.printf("Creating instance %s.%n", instanceId);
          try {
            // Wait for the createInstance operation to finish.
            [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) instanceResult = instanceAdminClient.createInstanceAsync(
                [CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.html).newBuilder()
                    .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ProjectName.html).of(projectId).toString())
                    .[setInstanceId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.Builder.html#com_google_spanner_admin_instance_v1_CreateInstanceRequest_Builder_setInstanceId_java_lang_String_)(instanceId)
                    .setInstance(instance)
                    .build()).get();
            System.out.printf("Asymmetric Autoscaling instance %s was successfully created%n",
                instanceResult.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)());
          } catch (ExecutionException e) {
            System.out.printf(
                "Error: Creating instance %s failed with error message %s%n",
                instance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)(), e.getMessage());
          } catch (InterruptedException e) {
            System.out.println("Error: Waiting for createInstance operation to finish was interrupted");
          }
        }
      }
    }

### Create an instance without a default backup schedule
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.instance.v1.[InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html);
    import com.google.spanner.admin.instance.v1.[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.html);
    import com.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html);
    import com.google.spanner.admin.instance.v1.[InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html);
    import com.google.spanner.admin.instance.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ProjectName.html);
    import java.util.concurrent.ExecutionException;
    
    class CreateInstanceWithoutDefaultBackupSchedulesExample {
    
      static void createInstanceWithoutDefaultBackupSchedules() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        createInstanceWithoutDefaultBackupSchedules(projectId, instanceId);
      }
    
      static void createInstanceWithoutDefaultBackupSchedules(String projectId, String instanceId) {
        // Set Instance configuration.
        int nodeCount = 2;
        String displayName = "Descriptive name";
    
        // Create an Instance object that will be used to create the instance.
        [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) instance =
            [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).newBuilder()
                .setDisplayName(displayName)
                .[setDefaultBackupScheduleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.Builder.html#com_google_spanner_admin_instance_v1_Instance_Builder_setDefaultBackupScheduleType_com_google_spanner_admin_instance_v1_Instance_DefaultBackupScheduleType_)([Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).DefaultBackupScheduleType.NONE)
                .setNodeCount(nodeCount)
                .setConfig([InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html).of(projectId, "regional-us-east4").toString())
                .build();
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
                [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html) instanceAdminClient = spanner.[createInstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createInstanceAdminClient__)()) {
    
          // Wait for the createInstance operation to finish.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) createdInstance =
              instanceAdminClient
                  .createInstanceAsync(
                      [CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.html).newBuilder()
                          .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ProjectName.html).of(projectId).toString())
                          .[setInstanceId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.CreateInstanceRequest.Builder.html#com_google_spanner_admin_instance_v1_CreateInstanceRequest_Builder_setInstanceId_java_lang_String_)(instanceId)
                          .setInstance(instance)
                          .build())
                  .get();
          System.out.printf("Instance %s was successfully created%n", createdInstance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)());
        } catch (ExecutionException e) {
          System.out.printf(
              "Error: Creating instance %s failed with error message %s%n",
              instance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)(), e.getMessage());
        } catch (InterruptedException e) {
          System.out.println("Error: Waiting for createInstance operation to finish was interrupted");
        }
      }
    }

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    const instanceAdminClient = await spanner.[getInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     **/
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    
    // Creates a new instance
    try {
      console.log(
        `Creating instance ${instanceAdminClient.instancePath(
          projectId,
          instanceId,
        )}.`,
      );
      const [operation] = await instanceAdminClient.createInstance({
        instanceId: instanceId,
        parent: instanceAdminClient.projectPath(projectId),
        instance: {
          config: instanceAdminClient.instanceConfigPath(
            projectId,
            'regional-us-central1',
          ),
          nodeCount: 1,
          displayName: 'Display name for the instance.',
          labels: {
            cloud_spanner_samples: 'true',
            created: Math.round(Date.now() / 1000).toString(), // current time
          },
          edition:
            protos.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance-class.html).[Edition](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.edition.html).[STANDARD](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.edition.html), //optional
        },
      });
    
      console.log(`Waiting for operation on ${instanceId} to complete...`);
      await operation.promise();
    
      console.log(`Created instance ${instanceId}.`);
    } catch (err) {
      console.error('ERROR:', err);
    }

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### Create an instance with managed autoscaling using Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Get the instance admin client
    const instanceAdminClient = spanner.[getInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    const autoscalingConfig =
      protos.google.spanner.admin.instance.v1.[AutoscalingConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.autoscalingconfig-class.html).[create](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.autoscalingconfig-class.html)({
        // Only one of minNodes/maxNodes or minProcessingUnits/maxProcessingUnits can be set.
        autoscalingLimits:
          protos.google.spanner.admin.instance.v1.[AutoscalingConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.autoscalingconfig-class.html).[AutoscalingLimits](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.autoscalingconfig.autoscalinglimits.html).[create](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.autoscalingconfig.autoscalinglimits.html)(
            {
              minNodes: 1,
              maxNodes: 2,
            },
          ),
        // highPriorityCpuUtilizationPercent and storageUtilizationPercent are both
        // percentages and must lie between 0 and 100.
        autoscalingTargets:
          protos.google.spanner.admin.instance.v1.[AutoscalingConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.autoscalingconfig-class.html).[AutoscalingTargets](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.autoscalingconfig.autoscalingtargets.html).[create](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.autoscalingconfig.autoscalingtargets.html)(
            {
              highPriorityCpuUtilizationPercent: 65,
              storageUtilizationPercent: 95,
            },
          ),
      });
    
    // Creates a new instance with autoscaling configuration
    // When autoscalingConfig is enabled, nodeCount and processingUnits fields
    // need not be specified.
    try {
      console.log(
        `Creating instance ${instanceAdminClient.instancePath(
          projectId,
          instanceId,
        )}.`,
      );
      const [operation] = await instanceAdminClient.createInstance({
        instanceId: instanceId,
        parent: instanceAdminClient.projectPath(projectId),
        instance: {
          config: instanceAdminClient.instanceConfigPath(
            projectId,
            'regional-us-central1',
          ),
          displayName: 'Display name for the instance.',
          autoscalingConfig: autoscalingConfig,
          labels: {
            cloud_spanner_samples: 'true',
            created: Math.round(Date.now() / 1000).toString(), // current time
          },
          // Managed autoscaler is available only for ENTERPRISE edition
          edition:
            protos.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance-class.html).[Edition](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.edition.html).[ENTERPRISE](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.edition.html),
        },
      });
    
      console.log(`Waiting for operation on ${instanceId} to complete...`);
      await operation.promise();
      console.log(`Created instance ${instanceId}.`);
    
      // get instance metadata
      const [metadata] = await instanceAdminClient.getInstance({
        name: instanceAdminClient.instancePath(projectId, instanceId),
      });
      console.log(
        `Autoscaling configurations of ${instanceId} are:  ` +
          '\n' +
          `Min nodes: ${metadata.autoscalingConfig.autoscalingLimits.minNodes} ` +
          'nodes.' +
          '\n' +
          `Max nodes: ${metadata.autoscalingConfig.autoscalingLimits.maxNodes}` +
          ' nodes.' +
          '\n' +
          `High priority cpu utilization percent: ${metadata.autoscalingConfig.autoscalingTargets.highPriorityCpuUtilizationPercent}.` +
          '\n' +
          `Storage utilization percent: ${metadata.autoscalingConfig.autoscalingTargets.storageUtilizationPercent}.`,
      );
    } catch (err) {
      console.error('ERROR:', err);
    }

### Create an instance without a default backup schedule
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     **/
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    const instanceAdminClient = await spanner.[getInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    // Creates a new instance
    try {
      const [operation] = await instanceAdminClient.createInstance({
        instanceId: instanceId,
        parent: instanceAdminClient.projectPath(projectId),
        instance: {
          config: instanceAdminClient.instanceConfigPath(
            projectId,
            'regional-me-central2',
          ),
          nodeCount: 1,
          displayName: 'Display name for the instance.',
          labels: {
            cloud_spanner_samples: 'true',
            created: Math.round(Date.now() / 1000).toString(), // current time
          },
          defaultBackupScheduleType:
            protos.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance-class.html)
              .[DefaultBackupScheduleType](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.defaultbackupscheduletype.html).NONE,
        },
      });
      await operation.promise();
    
      console.log(
        `Created instance ${instanceId} without default backup schedules.`,
      );
    } catch (err) {
      console.error('ERROR:', err);
    }

### PHP

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Spanner\Admin\Instance\V1\Client\InstanceAdminClient;
    use Google\Cloud\Spanner\Admin\Instance\V1\CreateInstanceRequest;
    use Google\Cloud\Spanner\Admin\Instance\V1\Instance;
    
    /**
     * Creates an instance.
     * Example:
     * ```
     * create_instance($projectId, $instanceId);
     * ```
     *
     * @param string $projectId  The Spanner project ID.
     * @param string $instanceId The Spanner instance ID.
     */
    function create_instance(string $projectId, string $instanceId): void
    {
        $instanceAdminClient = new InstanceAdminClient();
        $parent = InstanceAdminClient::projectName($projectId);
        $instanceName = InstanceAdminClient::instanceName($projectId, $instanceId);
        $configName = $instanceAdminClient->instanceConfigName($projectId, 'regional-us-central1');
        $instance = (new Instance())
            ->setName($instanceName)
            ->setConfig($configName)
            ->setDisplayName('dispName')
            ->setNodeCount(1);
    
        $operation = $instanceAdminClient->createInstance(
            (new CreateInstanceRequest())
            ->setParent($parent)
            ->setInstanceId($instanceId)
            ->setInstance($instance)
        );
    
        print('Waiting for operation to complete...' . PHP_EOL);
        $operation->pollUntilComplete();
    
        printf('Created instance %s' . PHP_EOL, $instanceId);
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_instance(instance_id):
        """Creates an instance."""
        from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
    
        spanner_client = spanner.Client()
    
        config_name = "{}/instanceConfigs/regional-us-central1".format(
            spanner_client.project_name
        )
    
        operation = spanner_client.instance_admin_api.create_instance(
            parent=spanner_client.project_name,
            instance_id=instance_id,
            instance=spanner_instance_admin.Instance(
                config=config_name,
                display_name="This is a display name.",
                node_count=1,
                labels={
                    "cloud_spanner_samples": "true",
                    "sample_name": "snippets-create_instance-explicit",
                    "created": str(int(time.time())),
                },
                edition=spanner_instance_admin.Instance.Edition.STANDARD,  # Optional
            ),
        )
    
        print("Waiting for operation to complete...")
        operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print("Created instance {}".format(instance_id))
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Create an instance with managed autoscaling using Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_instance_with_autoscaling_config(instance_id):
        """Creates a Cloud Spanner instance with an autoscaling configuration."""
        from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
    
        spanner_client = spanner.Client()
    
        config_name = "{}/instanceConfigs/regional-us-central1".format(
            spanner_client.project_name
        )
    
        autoscaling_config = spanner_instance_admin.AutoscalingConfig(
            # Only one of minNodes/maxNodes or minProcessingUnits/maxProcessingUnits can be set.
            autoscaling_limits=spanner_instance_admin.AutoscalingConfig.AutoscalingLimits(
                min_nodes=1,
                max_nodes=2,
            ),
            # highPriorityCpuUtilizationPercent and storageUtilizationPercent are both
            # percentages and must lie between 0 and 100.
            autoscaling_targets=spanner_instance_admin.AutoscalingConfig.AutoscalingTargets(
                high_priority_cpu_utilization_percent=65,
                storage_utilization_percent=95,
            ),
        )
    
        #  Creates a new instance with autoscaling configuration
        #  When autoscalingConfig is enabled, nodeCount and processingUnits fields
        #  need not be specified.
        request = spanner_instance_admin.CreateInstanceRequest(
            parent=spanner_client.project_name,
            instance_id=instance_id,
            instance=spanner_instance_admin.Instance(
                config=config_name,
                display_name="This is a display name.",
                autoscaling_config=autoscaling_config,
                labels={
                    "cloud_spanner_samples": "true",
                    "sample_name": "snippets-create_instance_with_autoscaling_config",
                    "created": str(int(time.time())),
                },
                edition=spanner_instance_admin.Instance.Edition.ENTERPRISE,  # Optional
            ),
        )
    
        operation = spanner_client.instance_admin_api.create_instance(request=request)
    
        print("Waiting for operation to complete...")
        instance = operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print(
            "Created instance {} with {} autoscaling config".format(
                instance_id, instance.autoscaling_config
            )
        )
    
    

### Create an instance without a default backup schedule
    
    
    def create_instance_without_default_backup_schedules(instance_id):
        spanner_client = spanner.Client()
        config_name = "{}/instanceConfigs/regional-me-central2".format(
            spanner_client.project_name
        )
    
        operation = spanner_client.instance_admin_api.create_instance(
            parent=spanner_client.project_name,
            instance_id=instance_id,
            instance=spanner_instance_admin.Instance(
                config=config_name,
                display_name="This is a display name.",
                node_count=1,
                default_backup_schedule_type=spanner_instance_admin.Instance.DefaultBackupScheduleType.NONE,  # Optional
            ),
        )
    
        print("Waiting for operation to complete...")
        operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print("Created instance {} without default backup schedules".format(instance_id))
    
    

### Ruby

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # instance_config_id = "Your Spanner InstanceConfig ID"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/instance"
    
    instance_admin_client = Google::Cloud::Spanner::Admin::Instance.instance_admin
    
    project_path = instance_admin_client.project_path project: project_id
    instance_path = instance_admin_client.instance_path project: project_id, instance: instance_id
    instance_config_path = instance_admin_client.instance_config_path project: project_id, instance_config: instance_config_id
    
    job = instance_admin_client.create_instance parent: project_path,
                                                instance_id: instance_id,
                                                instance: { name: instance_path,
                                                            config: instance_config_path,
                                                            display_name: instance_id,
                                                            node_count: 2,
                                                            labels: { cloud_spanner_samples: "true" } }
    
    puts "Waiting for create instance operation to complete"
    
    job.wait_until_done!
    
    if job.error?
      puts job.error
    else
      puts "Created instance #{instance_id}"
    end

## List instances

You can show a list of your Spanner instances.

### Console

Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

The Google Cloud console shows a list of your Spanner instances, along with each instance's ID, display name, configuration, and [compute capacity](https://docs.cloud.google.com/spanner/docs/compute-capacity) expressed in both processing units and in nodes.

###  gcloud 

Use the [`gcloud spanner instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/list) command:
    
    
    gcloud spanner instances list
    

The gcloud CLI prints a list of your Spanner instances, along with each instance's ID, display name, configuration, and compute capacity.

## Edit an instance

The following sections explain how to upgrade the edition of your instance, and change an instance's display name, compute capacity, and default backup schedule type. You can't change the instance ID or instance configuration (however, you can [move your instance](https://docs.cloud.google.com/spanner/docs/move-instance)).

### Upgrade the edition

You can upgrade your Standard edition instances to a higher-tier edition. Standard edition instances can be upgraded to the Enterprise edition or Enterprise Plus edition as long as they have not been prevented by an [organization policy constraint](https://docs.cloud.google.com/spanner/docs/spanner-custom-constraints). Enterprise edition instances can be upgraded to the Enterprise Plus edition. The edition upgrade takes approximately 10 minutes to complete with zero downtime.

### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the name of the instance that you want to upgrade.

  3. Click **Upgrade** next to the edition type.

  4. In the **Edition instance** page, and under **Update edition** , select the new higher-tier edition for your instance.

  5. Click **Save**.




###  gcloud 

Use the [`gcloud spanner instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/update) command to upgrade your instance's edition:
    
    
    gcloud spanner instances update INSTANCE_ID --edition=EDITION \
    [--async]

Replace the following:

  * INSTANCE_ID: the permanent identifier for the instance.
  * EDITION: specify the new higher-tier edition for your instance. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview).



Optional flags:

  * `--async`: Use this flag if you want your request to return immediately, without waiting for the operation in progress to complete. You can check the status of your request by running [`gcloud spanner operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/operations/describe).



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	instance "cloud.google.com/go/spanner/admin/instance/apiv1"
    	"cloud.google.com/go/spanner/admin/instance/apiv1/instancepb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    func updateInstance(w io.Writer, projectID, instanceID string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance"
    	ctx := context.Background()
    	instanceAdmin, err := instance.NewInstanceAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer instanceAdmin.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1.html#cloud_google_com_go_spanner_admin_instance_apiv1_InstanceAdminClient_Close)()
    
    	req := &instancepb.UpdateInstanceRequest{
    		Instance: &instancepb.Instance{
    			Name: fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID),
    			// The edition selected for this instance.
    			// Different editions provide different capabilities at different price points.
    			// For more information, see https://cloud.google.com/spanner/docs/editions-overview.
    			Edition: instancepb.[Instance_ENTERPRISE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_EDITION_UNSPECIFIED_Instance_STANDARD_Instance_ENTERPRISE_Instance_ENTERPRISE_PLUS),
    		},
    		FieldMask: &field_mask.FieldMask{
    			Paths: []string{"edition"},
    		},
    	}
    	op, err := instanceAdmin.UpdateInstance(ctx, req)
    	if err != nil {
    		return fmt.Errorf("could not update instance %s: %w", fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID), err)
    	}
    	// Wait for the instance update to finish.
    	_, err = op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("waiting for instance update to finish failed: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated instance [%s]\n", instanceID)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html);
    import com.google.common.collect.Lists;
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html);
    import com.google.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html);
    import com.google.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceName.html);
    import com.google.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.UpdateInstanceRequest.html);
    import java.util.concurrent.ExecutionException;
    
    public class UpdateInstanceExample {
    
      static void updateInstance() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        updateInstance(projectId, instanceId);
      }
    
      static void updateInstance(String projectId, String instanceId) {
        // Set Instance configuration.
        int nodeCount = 2;
        String displayName = "Updated name";
    
        // Update an Instance object that will be used to update the instance.
        [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) instance =
            [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).newBuilder()
                .setName([InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceName.html).of(projectId, instanceId).toString())
                .setDisplayName(displayName)
                .setNodeCount(nodeCount)
                .setEdition([Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).Edition.ENTERPRISE)
                .setConfig([InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html).of(projectId, "regional-us-east4").toString())
                .build();
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
                [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html) instanceAdminClient = spanner.[createInstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createInstanceAdminClient__)()) {
    
          // Wait for the updatedInstance operation to finish.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) updatedInstance =
              instanceAdminClient
                  .updateInstanceAsync(
                      [UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.UpdateInstanceRequest.html).newBuilder()
                          .setFieldMask(
                              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(Lists.newArrayList("edition")))
                          .setInstance(instance)
                          .build())
                  .get();
          System.out.printf("Instance %s was successfully updated%n", updatedInstance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)());
        } catch (ExecutionException e) {
          System.out.printf(
              "Error: Updating instance %s failed with error message %s%n",
              [instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)(), e.getMessage());
        } catch (InterruptedException e) {
          System.out.println("Error: Waiting for updateInstance operation to finish was interrupted");
        }
      }
    }
    

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    const instanceAdminClient = spanner.[getInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Updates an instance
    try {
      console.log(
        `Updating instance ${instanceAdminClient.instancePath(
          projectId,
          instanceId,
        )}.`,
      );
      const [operation] = await instanceAdminClient.updateInstance({
        instance: {
          name: instanceAdminClient.instancePath(projectId, instanceId),
          labels: {
            updated: 'true',
            created: Math.round(Date.now() / 1000).toString(), // current time
          },
          edition:
            protos.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance-class.html).[Edition](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.edition.html).[ENTERPRISE](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.edition.html), //optional
        },
        // Field mask specifying fields that should get updated in an Instance
        fieldMask: (protos.google.protobuf.[FieldMask](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.protobuf.fieldmask.html) = {
          paths: ['labels', 'edition'],
        }),
      });
    
      console.log(`Waiting for operation on ${instanceId} to complete...`);
      await operation.promise();
      console.log(`Updated instance ${instanceId}.`);
      const [metadata] = await instanceAdminClient.getInstance({
        name: instanceAdminClient.instancePath(projectId, instanceId),
      });
      console.log(
        `Instance ${instanceId} has been updated with the ${metadata.edition} ` +
          'edition.',
      );
    } catch (err) {
      console.error('ERROR:', err);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_instance(instance_id):
        """Updates an instance."""
        from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
    
        spanner_client = spanner.Client()
    
        name = "{}/instances/{}".format(spanner_client.project_name, instance_id)
    
        operation = spanner_client.instance_admin_api.update_instance(
            instance=spanner_instance_admin.Instance(
                name=name,
                labels={
                    "sample_name": "snippets-update_instance-explicit",
                },
                edition=spanner_instance_admin.Instance.Edition.ENTERPRISE,  # Optional
            ),
            field_mask=field_mask_pb2.FieldMask(paths=["labels", "edition"]),
        )
    
        print("Waiting for operation to complete...")
        operation.result(900)
    
        print("Updated instance {}".format(instance_id))
    
    

### Downgrade the edition

You can downgrade your Spanner instances to a lower-tier edition. You must stop using the higher-tier edition features in order to downgrade. Enterprise edition instances can be downgraded to the Standard edition. Enterprise Plus edition instances can be downgraded to the Enterprise edition or Standard edition. The edition downgrade takes approximately 10 minutes to complete with zero downtime.

To monitor the usage of Enterprise edition and Enterprise Plus edition edition features in your instance, use the [Feature usage](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-spanner) (`instance/edition/feature_usage`) monitoring metric. For more information, see [Monitor edition usage](https://docs.cloud.google.com/spanner/docs/editions-overview#monitor-edition-usage)

### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the name of the instance that you want to downgrade.

  3. In the **Instance overview** page, click **Edit instance**.

  4. On the **Edit instance** page under **Choose a Spanner edition** , select the lower-tier edition.

  5. Click **Update instance**.




###  gcloud 

Use the [`gcloud spanner instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/update) command to downgrade your instance's edition:
    
    
    gcloud spanner instances update INSTANCE_ID --edition=EDITION

Replace the following:

  * INSTANCE_ID: the permanent identifier for the instance.
  * EDITION: specify the new lower-tier edition for your instance. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview).



### Change the display name

### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the name of the instance that you want to rename.

  3. Click **Edit instance**.

  4. Enter a new instance name. This name must be unique within the Google Cloud project.

  5. Click **Save**.




###  gcloud 

Use the [`gcloud spanner instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/update) command:
    
    
    gcloud spanner instances update INSTANCE_ID --description=INSTANCE_NAME

Replace the following:

  * INSTANCE_ID: the permanent identifier for the instance.
  * INSTANCE_NAME: the name to display for the instance in the Google Cloud console. The instance name must be unique within your Google Cloud project.



### Change the compute capacity

You must provision enough [compute capacity](https://docs.cloud.google.com/spanner/docs/compute-capacity) to keep [CPU utilization](https://docs.cloud.google.com/spanner/docs/cpu-utilization#recommended-max) and [storage utilization](https://docs.cloud.google.com/spanner/docs/storage-utilization) below the recommended maximums. For more information, see the [quotas and limits](https://docs.cloud.google.com/spanner/quotas) for Spanner.

You can reduce the compute capacity of a Spanner instance except in the following scenarios:

  * You can't store more than 10 TiB of data per node (1000 processing units).

  * There are a large number of [splits](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#database-splits) for your instance's data. In this scenario, Spanner might not be able to manage the splits after you reduce compute capacity. You can try reducing the compute capacity by progressively smaller amounts until you find the minimum capacity that Spanner needs to manage all of the instance's splits.

Spanner can create a large number of splits to accommodate your usage patterns. If your usage patterns change, then after one or two weeks, Spanner might merge some splits together and you can try to reduce the instance's compute capacity.




When removing compute capacity, monitor your CPU utilization and request latencies in [Cloud Monitoring](https://docs.cloud.google.com/spanner/docs/monitoring-cloud) to ensure CPU utilization stays under 65% for regional instances and 45% for each region in multi-region instances. You might experience a temporary increase in request latencies while removing compute capacity.

If you want to increase the compute capacity of an instance, your Google Cloud project must have sufficient quota to add the compute capacity. The time it takes for the increase request to complete depends on the size of the request. In most cases, requests complete within a few minutes. On rare occasions, a scale up might take up to an hour to complete.

### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the name of the instance that you want to change.

  3. Click **Edit Instance**.

  4. Change the compute capacity by choosing the measurement units (processing units or nodes) and then entering a quantity. When using processing units, enter quantities up to 1000 in multiples of 100 (100, 200, 300 and so on) and enter greater quantities in multiples of 1000 (1000, 2000, 3000 and so on). Each node equals 1000 processing units.

  5. Click **Save**.




If you see a dialog that says you have insufficient quota to add compute capacity in this location, follow the instructions to request a higher quota.

###  gcloud 

Use the [`gcloud spanner instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/update) command. When using this command, specify the [compute capacity](https://docs.cloud.google.com/spanner/docs/compute-capacity) as a number of nodes or processing units.
    
    
    gcloud spanner instances update INSTANCE_ID --nodes=NODE_COUNT
    [--async]

or
    
    
    gcloud spanner instances update INSTANCE_ID
    --processing-units=PROCESSING_UNIT_COUNT [--async]

Replace the following:

  * INSTANCE_ID: the permanent identifier for the instance.
  * NODE_COUNT: the compute capacity of the instance, expressed as a number of nodes. Each node equals 1000 processing units.
  * PROCESSING_UNIT_COUNT: the compute capacity of the instance, expressed as a number of processing units. Enter quantities up to 1000 in multiples of 100 (100, 200, 300 and so on) and enter greater quantities in multiples of 1000 (1000, 2000, 3000 and so on).



Optional flags:

  * `--async`: Use this flag if you want your request to return immediately, without waiting for the operation in progress to complete. You can check the status of your request by running [`gcloud spanner operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/operations/describe).



### Enable or modify managed autoscaler on an instance

You can enable or modify autoscaling on a Spanner instance using the Google Cloud console, the [gcloud CLI](https://cloud.google.com/sdk/docs/install), or the [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). The following limitations apply when you add or change the managed autoscaling feature on an existing instance:

  * Managed autoscaler is only available in the Enterprise edition or Enterprise Plus edition.
  * You can't enable the managed autoscaler on an instance that you are moving.
  * You can't move an instance while the managed autoscaler is enabled.




### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the name of the instance that you want to enable the managed autoscaler on.

  3. Click **Edit instance**.

  4. Under **Configure compute capacity** , click **Autoscaling**.

  5. For **Minimum** , select the minimum limit to use when scaling down. For more information, see [Determine the minimum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-minimum).

  6. For **Maximum** , select the maximum limit to use when scaling up. For more information, see [Determine the maximum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-maximum).

  7. For **High priority CPU utilization target** , select the percentage of CPU to use for high priority tasks. For more information, see [Determine the CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-high-priority-cpu).

  8. For **Total CPU utilization target** , select the target CPU percentage to use for all [low, medium, and high priority tasks](https://docs.cloud.google.com/spanner/docs/cpu-utilization#task-priority). The CPU percentage can range from 10 to 90%. For more information, see [Determine the total CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-total-cpu).

  9. For **Storage utilization target** , select the percentage of storage to use. For more information, see [Determine the storage utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-storage).

  10. Optional: If you select **Autoscaling** as the scaling mode, then you can click the **Show asymmetric autoscaling options** dropdown to autoscale your read-only replicas independently from other replicas.

     1. Select the read-only replica you want to asymmetrically autoscale.

     2. Configure the following autoscaler options:

        * **Minimum** indicates the minimum limit to scale down to, depending on the measurement unit that you choose for **Compute capacity**. For more information, see [Determine the minimum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-minimum).
        * **Maximum** indicates the maximum limit to scale up to, depending on the measurement unit that you choose for **Compute capacity**. For more information, see [Determine the maximum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-maximum).
        * **High priority CPU utilization target** indicates the target percentage of CPU to use for high priority tasks. For more information, see [Determine the high priority CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-high-priority-cpu).
        * **Total CPU utilization target** indicates the target percentage of CPU to use for all [low, medium, and high priority tasks](https://docs.cloud.google.com/spanner/docs/cpu-utilization#task-priority). The CPU percentage can range from 10 to 90%. For more information, see [Determine the total CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-total-cpu).
  11. Click **Save**.




###  gcloud 

Use the [`gcloud spanner instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/update) command to add the managed autoscaler to an instance. For more information and limitations, see [`Google Cloud CLI` flags and limitations](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#flags_and_limitations).

You can add the managed autoscaler with the following command:
    
    
      gcloud spanner instances update INSTANCE_ID \
        --autoscaling-min-processing-units=MINIMUM_PROCESSING_UNITS \
        --autoscaling-max-processing-units=MAXIMUM_PROCESSING_UNITS \
        --autoscaling-high-priority-cpu-target=HIGH_PRIORITY_CPU_PERCENTAGE \
        --autoscaling-total-cpu-target=TOTAL_CPU_PERCENTAGE \
        --autoscaling-storage-target=STORAGE_PERCENTAGE \
        [--disable-downscaling | --no-disable-downscaling] \
        [--asymmetric-autoscaling-option \
           location=ASYMMETRIC_AUTOSCALING_LOCATION,\
           min_nodes=ASYMMETRIC_AUTOSCALING_MIN,\
           max_nodes=ASYMMETRIC_AUTOSCALING_MAX,\
           high_priority_cpu_target=ASYMMETRIC_HIGH_PRIORITY_CPU_TARGET,\
           total_cpu_target=ASYMMETRIC_TOTAL_CPU_TARGET,\
           disable_total_cpu_autoscaling=TRUE|FALSE
           | disable_high_priority_cpu_autoscaling=TRUE|FALSE]

or
    
    
      gcloud spanner instances update INSTANCE_ID \
        --autoscaling-min-processing-units=MINIMUM_NODES \
        --autoscaling-max-processing-units=MAXIMUM_NODES \
        --autoscaling-high-priority-cpu-target=HIGH_PRIORITY_CPU_PERCENTAGE \
        --autoscaling-total-cpu-target=TOTAL_CPU_PERCENTAGE \
        --autoscaling-storage-target=STORAGE_PERCENTAGE \
        [--disable-downscaling | --no-disable-downscaling] \
        [--asymmetric-autoscaling-option \
           location=ASYMMETRIC_AUTOSCALING_LOCATION,\
           min_nodes=ASYMMETRIC_AUTOSCALING_MIN,\
           max_nodes=ASYMMETRIC_AUTOSCALING_MAX,\
           high_priority_cpu_target=ASYMMETRIC_HIGH_PRIORITY_CPU_TARGET,\
           total_cpu_target=ASYMMETRIC_TOTAL_CPU_TARGET,\
           disable_total_cpu_autoscaling=TRUE|FALSE
           | disable_high_priority_cpu_autoscaling=TRUE|FALSE]

Replace the following:

  * INSTANCE_ID: the permanent identifier for the instance.
  * MINIMUM_PROCESSING_UNITS, MINIMUM_NODES: the minimum number of processing units or nodes to use when scaling down. For more information, see [Determine the minimum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-minimum).
  * MAXIMUM_PROCESSING_UNITS, MAXIMUM_NODES: the maximum number of processing units or nodes to use when scaling up. For more information, see [Determine the maximum limit](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-maximum).
  * HIGH_PRIORITY_CPU_PERCENTAGE: the target percentage of high priority CPU to use, based on the [priority of the task](https://docs.cloud.google.com/spanner/docs/cpu-utilization#task-priority). The CPU percentage can range from 10 to 90%. If you're optimizing for cost, then use a higher percentage. For more information, see [Determine the high priority CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-high-priority-cpu).
  * TOTAL_CPU_PERCENTAGE: the target percentage of total priority CPU to use. The total CPU target has to be greater than the high priority CPU target. The CPU percentage can range from 10 to 90%. If you're optimizing for cost, then use a higher percentage. For more information, see [Determine the total CPU utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-total-cpu).
  * STORAGE_PERCENTAGE: the target percentage of storage to use, from 10% to 99%. For more information, see [Determine the storage utilization target](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-storage).



Optional flags:

  * `--disable-downscaling`: use this boolean flag to disable downscaling. When set to `TRUE`, it prevents the autoscaler from reducing the number of nodes or processing units. Upscaling continues to function normally to meet increased demand. To enable downscaling after disabling it, use the `--no-disable-downscaling` flag.
  * `--asymmetric-autoscaling-option`: Use this flag to enable [asymmetric autoscaling](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#asymmetric-read-only-autoscaling).

Replace the following parameters:

    * ASYMMETRIC_AUTOSCALING_LOCATION: if the asymmetric autoscaling flag is used, then this parameter is required. The location of the read-only region that you want to scale asymmetrically.
    * ASYMMETRIC_AUTOSCALING_MIN: optional parameter. The minimum number of nodes when scaling down. If not specified, this value is inherited from the base instance configuration.
    * ASYMMETRIC_AUTOSCALING_MAX: optional parameter. The maximum number of nodes when scaling up. If not specified, this value is inherited from the base instance configuration.
    * ASYMMETRIC_HIGH_PRIORITY_CPU_TARGET: optional parameter. The target percentage of CPU to use, based on the [priority of the task](https://docs.cloud.google.com/spanner/docs/cpu-utilization#task-priority). If not specified, this value is inherited from the base instance configuration. If you're optimizing for cost, then use a higher percentage. Replicas can have a different target percentage than the base instance and from other replicas, but for failover scenarios, we recommend that replicas use consistent targets across different replicas. For more information, see [Failover concerns](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#failover-concerns).
    * ASYMMETRIC_TOTAL_CPU_TARGET: optional parameter. Set the target from 10 to 90% for the [total CPU](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#determine-total-cpu). If not specified, this value is inherited from the base instance configuration. If you're optimizing for cost, then use a higher percentage. Replicas can have a different target percentage than the base instance and from other replicas, but for failover scenarios, we recommend that replicas use consistent targets across different replicas. For more information, see [Asymmetric read-only autoscaling](https://docs.cloud.google.com/spanner/docs/managed-autoscaler#asymmetric-read-only-autoscaling).
    * `disable_total_cpu_autoscaling`: set this parameter to `TRUE` if you don't want the autoscaler to autoscale total CPU on replicas. Don't specify this parameter if you want the instance to inherit the `total_cpu_autoscaling` target from the base instance. You can't disable both total CPU and high priority CPU on the same replica.
    * `disable_high_priority_cpu_autoscaling`: set the `disable_high_priority_cpu_autoscaling` to `TRUE` if you don't want the autoscaler to autoscale the high priority CPU on replicas. Don't specify this parameter if you want the instance to inherit the `high_priority_cpu_autoscaling` target from the base instance. You can't disable both total CPU and high priority CPU on the same replica.



After you add the managed autoscaler to an instance, you can also modify the managed autoscaler settings. For example, if you want to increase the maximum number of processing units to 10000, run the following command:
    
    
    gcloud spanner instances update test-instance \
         --autoscaling-max-processing-units=10000
    

### Change an instance from using managed autoscaler to manual scaling

You can change whether a Spanner instance uses manual or managed scaling by using the Google Cloud console, the [gcloud CLI](https://cloud.google.com/sdk/docs/install), or the [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries).

### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the name of the instance that you want to disable managed autoscaler on.

  3. Under **Choose a scaling mode** , click **Manual allocation**.

  4. Click **Save**.




###  gcloud 

Use the [`gcloud spanner instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/update) command to update the instance.

Use the following command to change an instance from using the managed autoscaler to manual scaling:
    
    
      gcloud spanner instances update INSTANCE_ID \
      --processing-units=PROCESSING_UNIT_COUNT

or
    
    
      gcloud spanner instances update INSTANCE_ID \
      --nodes=NODE_COUNT

Replace the following:

  * INSTANCE_ID: the permanent identifier for the instance.
  * NODE_COUNT: the compute capacity of the instance, expressed as a number of nodes. Each node equals 1000 processing units.
  * PROCESSING_UNIT_COUNT: the compute capacity of the instance, expressed as a number of processing units. Enter quantities up to 1000 in multiples of 100 (100, 200, 300 and so on) and enter greater quantities in multiples of 1000 (1000, 2000, 3000 and so on).



### Label an instance

Labels help organize your resources.

### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Select the checkbox for the instance. The **Info panel** appears on the right-hand side of the page.

  3. Click the **Labels** tab in the **Info panel**. You can then add, delete or update labels for the Spanner instance.




### Edit the default backup schedule type

Default backup schedules are automatically enabled for all new instances. You can enable or disable default backup schedules in an instance when creating the instance or by editing the instance later. For more information, see [Default backup schedules](https://docs.cloud.google.com/spanner/docs/backup#default-backup-schedules).

### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.



[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  1. Click the name of the instance that you want to edit the default backup schedule.
  2. Click **Edit instance**.
  3. Under **Backups** , the **Enable default backup schedules** checkbox determines whether default backup schedules are enabled or not. When enabled, all new databases in this instance have a default backup schedule created.
  4. Click **Save**.



###  gcloud 

Use the [`gcloud spanner instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/update) command to edit the default backup schedules type.

You can edit the default backup schedule type by running the following command:
    
    
      gcloud spanner instances update INSTANCE_ID \
        --default-backup-schedule-type=DEFAULT_BACKUP_SCHEDULE_TYPE

Replace the following:

  * INSTANCE_ID: the permanent identifier for the instance.
  * DEFAULT_BACKUP_SCHEDULE_TYPE: the default backup schedule type that is used in the instance. Must be one of the following values:

    * `AUTOMATIC`: a default backup schedule is created automatically when a new database is created in the instance. The default backup schedule creates a full backup every 24 hours. These full backups are retained for 7 days. You can edit or delete the default backup schedule once it's created.
    * `NONE`: a default backup schedule isn't created automatically when a new database is created in the instance.



### C#

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Spanner.Admin.Instance.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Threading.Tasks;
    
    public class UpdateInstanceDefaultBackupScheduleTypeAsyncSample
    {
        public async Task<Instance> UpdateInstanceDefaultBackupScheduleTypeAsync(string projectId, string instanceId)
        {
            // Create the InstanceAdminClient instance.
            [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html) instanceAdminClient = await [InstanceAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html#Google_Cloud_Spanner_Admin_Instance_V1_InstanceAdminClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Initialize request parameters.
            Instance instance = new Instance
            {
                InstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                DefaultBackupScheduleType = Instance.[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.html).[DefaultBackupScheduleType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.DefaultBackupScheduleType.html).[Automatic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.Instance.Types.DefaultBackupScheduleType.html#Google_Cloud_Spanner_Admin_Instance_V1_Instance_Types_DefaultBackupScheduleType_Automatic),
            };
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) mask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) 
            {
                Paths = { "default_backup_schedule_type" }
            };
    
            // Make the CreateInstance request.
            Operation<Instance, UpdateInstanceMetadata> response =
                await instanceAdminClient.[UpdateInstanceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Instance.V1/latest/Google.Cloud.Spanner.Admin.Instance.V1.InstanceAdminClient.html#Google_Cloud_Spanner_Admin_Instance_V1_InstanceAdminClient_UpdateInstanceAsync_Google_Cloud_Spanner_Admin_Instance_V1_Instance_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(instance, mask);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            Operation<Instance, UpdateInstanceMetadata> completedResponse =
                await response.PollUntilCompletedAsync();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while updating instance: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            Console.WriteLine($"Instance updated successfully.");
            return completedResponse.Result;
        }
    }
    

### Go

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	instance "cloud.google.com/go/spanner/admin/instance/apiv1"
    	"cloud.google.com/go/spanner/admin/instance/apiv1/instancepb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // updateInstanceDefaultBackupScheduleType updates instance default backup schedule type to AUTOMATIC.
    // This means a default backup schedule will be created automatically on creation of a database within the instance.
    func updateInstanceDefaultBackupScheduleType(w io.Writer, projectID, instanceID string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance"
    	ctx := context.Background()
    	instanceAdmin, err := instance.NewInstanceAdminClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer instanceAdmin.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1.html#cloud_google_com_go_spanner_admin_instance_apiv1_InstanceAdminClient_Close)()
    
    	// Updates the default backup schedule type field of an instance.  The field mask is required to
    	// indicate which field is being updated.
    	req := &instancepb.UpdateInstanceRequest{
    		Instance: &instancepb.Instance{
    			Name: fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID),
    			// Controls the default backup behavior for new databases within the instance.
    			DefaultBackupScheduleType: instancepb.[Instance_AUTOMATIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/instance/apiv1/instancepb.html#cloud_google_com_go_spanner_admin_instance_apiv1_instancepb_Instance_DEFAULT_BACKUP_SCHEDULE_TYPE_UNSPECIFIED_Instance_NONE_Instance_AUTOMATIC),
    		},
    		FieldMask: &field_mask.FieldMask{
    			Paths: []string{"default_backup_schedule_type"},
    		},
    	}
    	op, err := instanceAdmin.UpdateInstance(ctx, req)
    	if err != nil {
    		return fmt.Errorf("could not update instance %s: %w", fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID), err)
    	}
    	// Wait for the instance update to finish.
    	_, err = op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("waiting for instance update to finish failed: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated instance [%s]\n", instanceID)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html);
    import com.google.common.collect.Lists;
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html);
    import com.google.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html);
    import com.google.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceName.html);
    import com.google.spanner.admin.[instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).v1.[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.UpdateInstanceRequest.html);
    import java.util.concurrent.ExecutionException;
    
    public class UpdateInstanceDefaultBackupScheduleTypeExample {
    
      static void updateInstanceDefaultBackupScheduleType() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        updateInstanceDefaultBackupScheduleType(projectId, instanceId);
      }
    
      static void updateInstanceDefaultBackupScheduleType(String projectId, String instanceId) {
        // Set Instance configuration.
        int nodeCount = 2;
        String displayName = "Updated name";
    
        // Update an Instance object that will be used to update the instance.
        [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) instance =
            [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).newBuilder()
                .setName([InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceName.html).of(projectId, instanceId).toString())
                .setDisplayName(displayName)
                .setNodeCount(nodeCount)
                .[setDefaultBackupScheduleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.Builder.html#com_google_spanner_admin_instance_v1_Instance_Builder_setDefaultBackupScheduleType_com_google_spanner_admin_instance_v1_Instance_DefaultBackupScheduleType_)([Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html).DefaultBackupScheduleType.AUTOMATIC)
                .setConfig([InstanceConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.InstanceConfigName.html).of(projectId, "regional-us-east4").toString())
                .build();
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
                [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [InstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.instance.v1.InstanceAdminClient.html) instanceAdminClient = spanner.[createInstanceAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createInstanceAdminClient__)()) {
    
          // Wait for the updatedInstance operation to finish.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Instance.html) updatedInstance =
              instanceAdminClient
                  .updateInstanceAsync(
                      [UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.UpdateInstanceRequest.html).newBuilder()
                          .setFieldMask(
                              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                                  .[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(Lists.newArrayList("default_backup_schedule_type")))
                          .setInstance(instance)
                          .build())
                  .get();
          System.out.printf("Instance %s was successfully updated%n", updatedInstance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)());
        } catch (ExecutionException e) {
          System.out.printf(
              "Error: Updating instance %s failed with error message %s%n",
              [instance](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageLite.Builder.html#com_google_protobuf_GeneratedMessageLite_Builder_instance).[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.Instance.html#com_google_spanner_admin_instance_v1_Instance_getName__)(), e.getMessage());
        } catch (InterruptedException e) {
          System.out.println("Error: Waiting for updateInstance operation to finish was interrupted");
        }
      }
    }
    

### Node.js

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    const instanceAdminClient = await spanner.[getInstanceAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Updates an instance
    try {
      const [operation] = await instanceAdminClient.updateInstance({
        instance: {
          name: instanceAdminClient.instancePath(projectId, instanceId),
          defaultBackupScheduleType:
            protos.google.spanner.admin.instance.v1.[Instance](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance-class.html)
              .[DefaultBackupScheduleType](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.defaultbackupscheduletype.html).[AUTOMATIC](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.instance.defaultbackupscheduletype.html), // optional
        },
        // Field mask specifying fields that should get updated in an Instance
        fieldMask: (protos.google.protobuf.[FieldMask](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.protobuf.fieldmask.html) = {
          paths: ['default_backup_schedule_type'],
        }),
      });
    
      await operation.promise();
      const [metadata] = await instanceAdminClient.getInstance({
        name: instanceAdminClient.instancePath(projectId, instanceId),
      });
      console.log(
        `Instance ${instanceId} has been updated with the ${metadata.defaultBackupScheduleType}` +
          ' default backup schedule type.',
      );
    } catch (err) {
      console.error('ERROR:', err);
    }

### Python

To learn how to install and use the client library for Spanner, see [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). 

To authenticate to Spanner, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_instance_default_backup_schedule_type(instance_id):
        spanner_client = spanner.Client()
    
        name = "{}/instances/{}".format(spanner_client.project_name, instance_id)
    
        operation = spanner_client.instance_admin_api.update_instance(
            instance=spanner_instance_admin.Instance(
                name=name,
                default_backup_schedule_type=spanner_instance_admin.Instance.DefaultBackupScheduleType.AUTOMATIC,  # Optional
            ),
            field_mask=field_mask_pb2.FieldMask(paths=["default_backup_schedule_type"]),
        )
    
        print("Waiting for operation to complete...")
        operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print("Updated instance {} to have default backup schedules".format(instance_id))
    
    

## Move an instance

**Note:** You can't move an instance that has managed autoscaler enabled.

For instructions on how to move your instance from any instance configuration to any other instance configuration, including between regional and multi-regional configurations, see [Move an instance](https://docs.cloud.google.com/spanner/docs/move-instance#how-instance-move).

## Delete an instance

**Warning:** Deleting an instance permanently removes the instance and all its databases. You can't undo this later. Also, you can't create another free trial instance once you've deleted your first free trial instance. You can create one free trial instance per project lifecycle. 

You can delete an instance with the Google Cloud console or the [Google Cloud CLI](https://docs.cloud.google.com/spanner/docs/gcloud-spanner).

If you want to delete an instance that has one or more databases with deletion protection enabled, you must first [disable the deletion protection](https://docs.cloud.google.com/spanner/docs/prevent-database-deletion#disable) on all databases in that instance before you can delete the instance.

### Console

  1. Go to the **Spanner Instances** page in the Google Cloud console.

[Go to the Instances page](https://console.cloud.google.com/spanner/instances)

  2. Click the name of the instance that you want to delete.

  3. Click **Delete instance**.

  4. Follow the instructions to confirm that you want to delete the instance.

  5. Click **Delete**.




###  gcloud 

Use the [`gcloud spanner instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/list) command, replacing INSTANCE_ID with the instance ID:
    
    
    gcloud spanner instances delete INSTANCE_ID

## Stop or restart an instance

Spanner is a fully managed database service which oversees its own underlying tasks and resources, including monitoring and restarting processes when necessary with zero downtime. As there is no need to manually stop or restart a given instance, Spanner does not offer a way to do so.

## What's next

  * Learn how to insert, update, and delete data with [Data Manipulation Language (DML)](https://docs.cloud.google.com/spanner/docs/dml-tasks) or the [gcloud CLI](https://docs.cloud.google.com/spanner/docs/modify-gcloud).
  * Grant [Identity and Access Management roles](https://docs.cloud.google.com/spanner/docs/grant-permissions) for the instance and its databases.
  * Understand how to [design a Spanner schema](https://docs.cloud.google.com/spanner/docs/schema-design).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
