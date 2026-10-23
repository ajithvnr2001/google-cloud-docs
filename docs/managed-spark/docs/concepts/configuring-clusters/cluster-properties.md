---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties/
title: Cluster properties \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:02.079866+00:00
---

# Cluster properties  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cluster properties Stay organized with collections  Save and categorize content based on your preferences. 

## Apache Hadoop YARN, HDFS, Spark, and related properties

The open source components installed on Managed Service for Apache Spark clusters contain many configuration files. For example, Apache Spark and Apache Hadoop have several XML and plain text configuration files. You can use the `‑‑properties` flag of the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create "gcloud dataproc clusters create") command to modify many common configuration files when creating a cluster.

### Formatting

The `gcloud dataproc clusters create --properties` flag accepts the following string format:
    
    
    file_prefix1:property1=value1,file_prefix2:property2=value2,...
    

  * The file_prefix maps to a predefined configuration file as shown in the table below, and the property maps to a property within the file.

  * The default delimiter used to separate multiple cluster properties is the comma (,). However, if a comma is included in a property value, you must change the delimiter by specifying a "^delimiter^" at the beginning of the property list (see [gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) for more information).

    * Example using a "#" delimiter: 
          
          --properties ^#^file_prefix1:property1=part1,part2#file_prefix2:property2=value2
          


**Best practice:** To ensure predictable cluster behavior, specify Boolean property values directly as lowercase `true` or `false`.

### Examples

### Google Cloud console

To change the `spark.master` setting in the `spark-defaults.conf` file:

  1. In the Google Cloud console, open [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Customization & Other**.
  4. In the panel that opens, in the **Cluster properties** section, click **\+ Add properties**.
  5. Select **spark** in the **Prefix** list.
  6. In the **Key** field, enter `spark.master`.
  7. In the **Value** field, enter the setting.
  8. Click **Save**.



### gcloud CLI

To change the `spark.master`setting in the `spark-defaults.conf` file, add the following `gcloud dataproc clusters create --properties` flag:
    
    
    --properties 'spark:spark.master=spark://example.com'
    

You can change several properties at once, in one or more configuration files, by using a comma separator. Each property must be specified in the full `file_prefix:property=value` format. For example, to change the `spark.master` setting in the `spark-defaults.conf` file and the `dfs.hosts` setting in the `hdfs-site.xml` file, use the following `--properties`flag when creating a cluster:
    
    
    --properties 'spark:spark.master=spark://example.com,hdfs:dfs.hosts=/foo/bar/baz'
    

### REST API

To set `spark.executor.memory` to `10g`, insert the following `properties` setting in the [SoftwareConfig](https://docs.cloud.google.com/static/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig.FIELDS.properties) section of your [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request:
    
    
    "properties": {
      "spark:spark.executor.memory": "10g"
    }
    

An easy way to see how to construct the JSON body of a Dataproc API clusters REST request is to initiate the equivalent `gcloud` command using the `--log-http` flag. Here is a sample `gcloud dataproc clusters create` command, which sets cluster properties with the `--properties spark:spark.executor.memory=10g` flag. The stdout log shows the resulting REST request body (the `properties` snippet is shown below):
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --properties=spark:spark.executor.memory=10g \
        --log-http \
        other args ...
    

**Output:**
    
    
    ...
    == body start ==
    {"clusterName": "my-cluster", "config": {"gceClusterConfig": ...
    "masterConfig": {... "softwareConfig": {"properties": {"spark:spark.executor.memory": "10g"}},
      
    ...
    == body end ==
    ...
    

**Make sure to cancel the command** after the JSON body appears in the output if you do not want the command to take effect.

### Cluster versus job properties

The Apache Hadoop YARN, HDFS, Spark, and other file-prefixed properties are applied at the cluster level when you create a cluster. These properties cannot be applied to a cluster after cluster creation. However, many of these properties can also be applied to specific jobs. **When applying a property to a job, the file prefix is not used**.

The following example sets Spark executor memory to 4g for a Spark job (`spark:` prefix omitted).
    
    
    gcloud dataproc jobs submit spark \
        --region=REGION \
        --properties=spark.executor.memory=4g \
        other args ...
    

Job properties can be submitted in a file using the `gcloud dataproc jobs submit job-type --properties-file` flag (see, for example, the [\--properties-file](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/hadoop#--properties-file) description for an Hadoop job submission).
    
    
    gcloud dataproc jobs submit JOB_TYPE \
        --region=REGION \
        --properties-file=PROPERTIES_FILE \
        other args ...
    

The `PROPERTIES_FILE` is a set of line-delimited `key`=`value` pairs. The property to be set is the `key`, and the value to set the property to is the `value`. See the [java.util.Properties](https://docs.oracle.com/javase/7/docs/api/java/util/Properties.html#load\(java.io.Reader) class for a detailed description of the properties file format.

The following is an example of a properties file that can be passed to the `--properties-file` flag when submitting a Managed Service for Apache Spark job.
    
    
     dataproc:conda.env.config.uri=gs://some-bucket/environment.yaml
     spark:spark.history.fs.logDirectory=gs://some-bucket
     spark:spark.eventLog.dir=gs://some-bucket
     capacity-scheduler:yarn.scheduler.capacity.root.adhoc.capacity=5
    

### File-prefixed properties table

File prefix | File | File purpose  
---|---|---  
capacity-scheduler | capacity-scheduler.xml | Hadoop YARN Capacity Scheduler configuration  
core | core-site.xml | [Hadoop general configuration](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
distcp | distcp-default.xml | Hadoop Distributed Copy configuration  
flink | flink-conf.yaml | [Flink configuration](https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/config/)  
flink-log4j | log4j.properties | Log4j settings file  
hadoop-env | hadoop-env.sh | [Hadoop specific environment variables](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
hadoop-log4j | log4j.properties | Log4j settings file  
hbase | [hbase-site.xml](https://github.com/apache/hbase/blob/master/hbase-server/src/test/resources/hbase-site.xml) | HBase configuration  
hbase-log4j | log4j.properties | Log4j settings file  
hdfs | hdfs-site.xml | [Hadoop HDFS configuration](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
hive | hive-site.xml | Hive configuration  
hive-log4j2 | hive-log4j2.properties | Log4j settings file  
hudi | hudi-default.conf | Hudi configuration  
mapred | mapred-site.xml | [Hadoop MapReduce configuration](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
mapred-env | mapred-env.sh | [Hadoop MapReduce specific environment variables](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
pig | pig.properties | Pig configuration  
pig-log4j | log4j.properties | Log4j settings file  
presto | config.properties | Presto configuration  
presto-jvm | jvm.config | Presto specific JVM configuration  
spark | spark-defaults.conf | [Spark configuration](https://spark.apache.org/docs/latest/configuration.html)  
spark-env | spark-env.sh | [Spark specific environment variables](https://spark.apache.org/docs/latest/configuration.html)  
spark-log4j | log4j.properties | Log4j settings file  
tez | tez-site.xml | Tez configuration  
webcat-log4j | webhcat-log4j2.properties | Log4j settings file  
yarn | yarn-site.xml | [Hadoop YARN configuration](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
yarn-env | yarn-env.sh | [Hadoop YARN specific environment variables](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html)  
zeppelin | zeppelin-site.xml | Zeppelin configuration  
zeppelin-env | zeppelin-env.sh | Zeppelin specific environment variables (Optional Component only)  
zeppelin-log4j | log4j.properties | Log4j settings file  
zookeeper | zoo.cfg | Zookeeper configuration  
zookeeper-log4j | log4j.properties | Log4j settings file  
  
**Notes**

  * Some properties are reserved and cannot be overridden because they impact the functionality of the Managed Service for Apache Spark cluster. If you try to change a reserved property, you will receive an error message when creating your cluster.
  * You can specify multiple changes by separating each with a comma.
  * The `--properties` flag cannot modify configuration files not shown above.
  * Changes to properties will be applied **before** the daemons on your cluster start.
  * If the specified property exists, it will be updated. If the specified property does not exist, it will be added to the configuration file.



## Managed Service for Apache Spark properties

The properties listed in this section are specific to Managed Service for Apache Spark. These properties can be used to further configure the functionality of your Managed Service for Apache Spark cluster.

**Note:** These cluster properties are specified at cluster creation. They cannot be specified or updated after cluster creation.

### Formatting

The `gcloud dataproc clusters create --properties` flag accepts the following string format:
    
    
    property_prefix1:property1=value1,property_prefix2:property2=value2,...
    

  * The default delimiter used to separate multiple cluster properties is the comma (,). However, if a comma is included in a property value, you must change the delimiter by specifying "^delimiter^" at the beginning of the property list (see [gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) for more information).

    * Example using a "#" delimiter: 
          
          --properties ^#^property_prefix1:property1=part1,part2#property_prefix2:property2=value2
          




**Example:**

Create a cluster and set [Enhanced Flexibility Mode](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flex) to Spark primary worker shuffle.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --properties=dataproc:efm.spark.shuffle=primary-worker \
        other args ...
    

**Best practice:** To ensure predictable cluster behavior, specify Boolean property values directly as lowercase `true` or `false`.

### Managed Service for Apache Spark properties table

Property prefix | Property | Values | Description  
---|---|---|---  
dataproc | agent.process.threads.job.min | `number` | Managed Service for Apache Spark runs user job drivers concurrently in a thread pool. This property controls the minimum number of threads in the thread pool for fast startup even when no jobs are running (default: 10).  
dataproc | agent.process.threads.job.max | `number` | Managed Service for Apache Spark runs user job drivers concurrently in a thread pool. This property controls the maximum number of threads in the thread pool, therefore limiting the maximum concurrency of user jobs. Increase this value for higher concurrency (default: 100).  
dataproc | am.primary_only | `true` or `false` | Set this property to `true` to prevent application master from running on Managed Service for Apache Spark cluster preemptible workers. **Note** : This feature is only available with Managed Service for Apache Spark 1.2 and higher. The default value is `false`.  
dataproc | conda.env.config.uri | `gs://<path>` | Location in Cloud Storage of the Conda environment config file. A new Conda environment will be created and activated based on this file. For more information, see [Using Conda related Cluster properties](https://docs.cloud.google.com/managed-spark/docs/tutorials/python-configuration#using_conda_related_cluster_properties). (default: `empty`).  
dataproc | conda.packages | Conda packages | This property takes a list of comma-separated Conda packages with specific versions to be installed in the `base` Conda environment. For more information, see [Using Conda related Cluster properties](https://docs.cloud.google.com/managed-spark/docs/tutorials/python-configuration#using_conda_related_cluster_properties). (default: `empty`).  
dataproc | dataproc.allow.zero.workers | `true` or `false` | Set this [SoftwareConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig) property to `true` in a `clusters.create` API request to create a [Single node cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters), which changes default number of workers from 2 to 0, and places worker components on the master host. A Single node cluster can also be created from the Google Cloud console or with the Google Cloud CLI by setting the number of workers to `0`.  
dataproc | dataproc.alpha.master.nvdimm.size.gb | 1500-6500 | Setting a value creates a Managed Service for Apache Spark master with [Intel Optane DC Persistent memory](https://www.intel.com/content/www/us/en/content-details/841964/intel-optane-persistent-memory-start-up-guide.html). Note: Optane VMs can only be created in `us-central1-f` zones, only with `n1-highmem-96-aep` machine type and only under whitelisted projects.  
dataproc: | dataproc.alpha.worker.nvdimm.size.gb | 1500-6500 | Setting a value creates a Managed Service for Apache Spark worker with [Intel Optane DC Persistent memory](https://www.intel.com/content/www/us/en/content-details/841964/intel-optane-persistent-memory-start-up-guide.html). Note: Optane VMs can only be created in `us-central1-f` zones, only with `n1-highmem-96-aep` machine type and only under whitelisted projects.  
dataproc: | dataproc.await-new-workers-service-registration | `true` or `false` | This property is available in images 2.0.49+. Default value is `false`. Set this property to `true` to wait for new primary workers to register service leaders, such as HDFS NameNode and YARN ResourceManager, during cluster creation or cluster scale-up (only HDFS and YARN services are monitored). When set to `true`, if a new worker fails to register to a service, the worker is assigned a `FAILED` status. A failed worker is removed if the cluster is scaling up. If the cluster is being created, a failed worker is removed if the [`gcloud dataproc clusters create --action-on-failed-primary-workers=DELETE`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--action-on-failed-primary-workers) flag or the API [`actionOnFailedPrimaryWorkers=DELETE`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create#FailureAction.ENUM_VALUES.DELETE) field was specified as part of the `gcloud` command or API cluster create request.  
dataproc: | dataproc.beta.secure.multi-tenancy.user.mapping | `user-to-service account mappings` | This property takes a list of user-to-service account mappings. Mapped users can submit interactive workloads to the cluster with isolated user identities (see [Managed Service for Apache Spark Service Account Based Secure Multi-tenancy](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/sa-multi-tenancy)).  
dataproc: | dataproc.cluster.caching.enabled | `true` or `false` | When the [cluster caching is enabled](https://docs.cloud.google.com/managed-spark/docs/concepts/cluster-caching), the cluster caches Cloud Storage data accessed by Spark jobs, which improves job performance without compromising consistency. (default: `false`).  
dataproc | dataproc.cluster-ttl.consider-yarn-activity | `true` or `false` | When set to `true`, [Cluster Scheduled Deletion](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-deletion) considers both YARN and Jobs API activity when calculating cluster idle time. When set to `false`, Jobs API activity only is considered. (default: `true`). For more information, see [Cluster idle time calculation](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-deletion#cluster_idle_time_calculation).  
dataproc | dataproc.conscrypt.provider.enable | `true` or `false` | Enables (`true`) or disables (`false`) [Conscrypt](https://github.com/google/conscrypt) as the primary Java security provider. **Note** : Conscrypt is enabled by default in Managed Service for Apache Spark 1.2 and higher, but disabled in 1.0/1.1.  
dataproc | dataproc.cooperative.multi-tenancy.user.mapping | `user-to-service account mappings` | This property takes a list of comma-separated user-to-service account mappings. If a cluster is created with this property set, when a user submits a job, the cluster will attempt to impersonate the corresponding service account when accessing Cloud Storage through the [Cloud Storage connector](https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/cloud-storage). This feature requires Cloud Storage connector version [`2.1.4`](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v2.1.4) or higher. For more information, see [Managed Service for Apache Spark cooperative multi-tenancy](https://cloud.google.com/blog/topics/developers-practitioners/dataproc-cooperative-multi-tenancy). (default: `empty`).  
dataproc | dataproc.control.max.assigned.job.tasks | `100` | This property limits how many tasks can concurrently run on a cluster master node. If the active task count exceeds the task limit, new jobs queue until running jobs complete and resources are freed up to allow new tasks to be scheduled. **Note:** Setting a default task limit in excess of `100` (the default) is not recommended since this can cause an out-of-memory condition in the master node.  
dataproc | dataproc:hudi.version | Hudi version | Sets the Hudi version used with the optional [Managed Service for Apache Spark Hudi component](https://docs.cloud.google.com/managed-spark/docs/concepts/hudi). **Note:** This version is set by Managed Service for Apache Spark to be compatible with the cluster image version. If it is set by the user, cluster creation can fail if the specified version is not compatible with the cluster image.  
dataproc | dataproc.lineage.enabled | `true` | Enables [data lineage](https://docs.cloud.google.com/managed-spark/docs/guides/lineage) in a Managed Service for Apache Spark cluster for Spark jobs.  
dataproc | dataproc.localssd.mount.enable | `true` or `false` | Whether to mount local SSDs as Hadoop/Spark temp directories and HDFS data directories (default: `true`).  
dataproc | dataproc.logging.extended.enabled | `true` or `false` | Enables (`true`) or disables (`false`) logs in [Cloud Logging](https://docs.cloud.google.com/logging/docs) for the following: `knox`, `zeppelin`, `ranger-usersync`, `jupyter_notebook`, `jupyter_kernel_gateway`, and `spark-history-server` (default: `true`). For more information, see [Managed Service for Apache Spark cluster logs in Logging](https://docs.cloud.google.com/managed-spark/docs/guides/logging#cluster-logs).  
dataproc | dataproc.logging.stackdriver.enable | `true` or `false` | Enables (`true`) or disables (`false`) [Cloud Logging](https://docs.cloud.google.com/logging/docs) (default: `true`). See [Cloud Logging Pricing](https://cloud.google.com/stackdriver/pricing#logging-costs) for associated charges.  
dataproc | dataproc.logging.stackdriver.job.driver.enable | `true` or `false` | Enables (`true`) or disables (`false`) Managed Service for Apache Spark job driver logs in [Cloud Logging](https://docs.cloud.google.com/logging/docs). See [Managed Service for Apache Spark job output and logs](https://docs.cloud.google.com/managed-spark/docs/guides/job-output) (default: `false`).  
dataproc | dataproc.logging.stackdriver.job.yarn.container.enable | `true` or `false` | Enables (`true`) or disables (`false`) YARN container logs in [Cloud Logging](https://docs.cloud.google.com/logging/docs). See [Spark job output options](https://docs.cloud.google.com/managed-spark/docs/guides/driver-output#and_spark_job_properties_overview). (default: `false`).  
dataproc | dataproc.logging.syslog.enabled | `true` or `false` | Enables (`true`) or disables (`false`) VM syslogs in [Cloud Logging](https://docs.cloud.google.com/logging/docs) (default: `true`).  
dataproc | dataproc.master.custom.init.actions.mode | `RUN_BEFORE_SERVICES` or `RUN_AFTER_SERVICES` | For 2.0+ image clusters, when set to `RUN_AFTER_SERVICES`, initialization actions on the master will run after HDFS and any services that depend on HDFS are initialized. Examples of HDFS-dependent services include: HBase, Hive Server2, Ranger, Solr, and the Spark and MapReduce history servers. (default: `RUN_BEFORE_SERVICES`).  
dataproc | dataproc.monitoring.stackdriver.enable | `true` or `false` | Enables (`true`) or disables (`false`) the [Monitoring agent](https://docs.cloud.google.com/monitoring/agent) (default: `false`). This property is **deprecated**. See [Enable custom metric collection](https://docs.cloud.google.com/managed-spark/docs/guides/metrics#enable_custom_metric_collection) to enable the collection of Managed Service for Apache Spark OSS metric collection in Monitoring.  
dataproc | dataproc.scheduler.driver-size-mb | `number` | The average driver memory footprint, which determines the maximum number of concurrent jobs a cluster will run. The default value is `1`GB. A smaller value, such as `256`, may be appropriate for Spark jobs.  
dataproc | dataproc.scheduler.job-submission-rate | `number` | Jobs are throttled if this rate is exceeded. The default rate is `1.0` QPS.  
dataproc | dataproc.scheduler.max-concurrent-jobs | `number` | The maximum number of concurrent jobs. If this value is not set when the cluster is created, the upper limit on concurrent jobs is calculated as `max((masterMemoryMb - 3584) / masterMemoryMbPerJob, 5)`. `masterMemoryMb` is determined by the master VM's machine type. `masterMemoryMbPerJob` is `1024` by default, but is configurable at cluster creation with the`dataproc:dataproc.scheduler.driver-size-mb` cluster property.  
dataproc | dataproc.scheduler.max-memory-used | `number` | The maximum amount of the RAM that can be used. If current usage is above this threshold, new jobs cannot be scheduled. The default is `0.9` (90%). If set to `1.0`, master-memory-utilization job throttling is disabled.  
dataproc | dataproc.scheduler.min-free-memory.mb | `number` | The minimum amount of free memory in megabytes needed by the Managed Service for Apache Spark job driver to schedule another job on the cluster. The default is `256` MB.  
dataproc | dataproc.snap.enabled | `true` or `false` | Enables or disables Ubuntu Snap daemon. The default value is `true`. If set to`false`, pre-installed Snap packages in the image are not affected, but auto refresh is disabled. Applies to 1.4.71, 1.5.46, 2.0.20 and newer Ubuntu images.  
dataproc | dataproc.worker.custom.init.actions.mode | `RUN_BEFORE_SERVICES` | For pre-2.0 image clusters, RUN_BEFORE_SERVICES **is not** set, but can be set by the user when the cluster is created. For 2.0+ image clusters, RUN_BEFORE_SERVICES **is** set, and the **property cannot be passed to the cluster** (it cannot be changed by the user). For information on the effect of this setting, see [Important considerations and guidelines—Initialization processing](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions#important_considerations_and_guidelines).  
dataproc | dataproc.yarn.orphaned-app-termination.enable | `true` or `false` | Default value is `true`. Set to `false` to prevent Managed Service for Apache Spark from terminating "orphaned" YARN apps. Managed Service for Apache Spark considers a YARN app to be orphaned if the job driver that submitted the YARN app has exited. **Warning:** If you use Spark cluster mode (`spark.submit.deployMode=cluster`) and you set `spark.yarn.submit.waitAppCompletion=false`, the Spark driver exits without waiting for YARN apps to complete; in this case, set `dataproc:dataproc.yarn.orphaned-app-termination.enable=false`. Also set this property to `false` if you submit Hive jobs.  
dataproc | diagnostic.capture.enabled | `true` or `false` | Enables the collection of cluster [checkpoint diagnostic data](https://docs.cloud.google.com/managed-spark/docs/support/diagnose-clusters#checkpoint_diagnostic_data_collection). (default: `true`).  
dataproc | diagnostic.capture.access | `GOOGLE_DATAPROC_DIAGNOSE` | If set to `GOOGLE_DATAPROC_DIAGNOSE`, cluster [checkpoint diagnostic data](https://docs.cloud.google.com/managed-spark/docs/support/diagnose-clusters#checkpoint_diagnostic_data_collection), which is saved in Cloud Storage, is shared with Managed Service for Apache Spark support. (default: not set).  
dataproc | efm.spark.shuffle | `primary-worker` | If set to `primary-worker`, Spark shuffle data is written to primary workers". See [Managed Service for Apache Spark Enhanced Flexibility Mode](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flex) for more information.  
dataproc | job.history.to-gcs.enabled | `true` or `false` | Allows persisting MapReduce and Spark history files to the Managed Service for Apache Spark temp bucket (default: `true` for image versions 1.5+). Users can overwrite the locations of job history file persistence through the following properties: `mapreduce.jobhistory.done-dir`, `mapreduce.jobhistory.intermediate-done-dir`, `spark.eventLog.dir`, and `spark.history.fs.logDirectory`. See [Managed Service for Apache Spark Persistent History Server ](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server#set_up_a_job_cluster) for information on these and other cluster properties associated with the Managed Service for Apache Spark job history and event files.  
dataproc | jobs.file-backed-output.enable | `true` or `false` | Configures Managed Service for Apache Spark jobs to pipe their output to temporary files in the `/var/log/google-dataproc-job` directory. Must be set to `true` to enable job driver logging in [Cloud Logging](https://docs.cloud.google.com/logging/docs) (default: `true`).  
dataproc | jupyter.listen.all.interfaces | `true` or `false` | To reduce the risk of remote code execution over unsecured notebook server APIs, the default setting for image versions 1.3+ is `false`, which restricts connections to `localhost` (`127.0.0.1`) when [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways) is enabled (Component Gateway activation is not required for 2.0+ images). This default setting can be overridden by setting this property to `true` to allow all connections.  
dataproc | jupyter.notebook.gcs.dir | `gs://<dir-path>` | Location in Cloud Storage to save Jupyter notebooks.  
dataproc | kerberos.beta.automatic-config.enable | `true` or `false` | When set to `true`, users do not need to specify the Kerberos root principal password with the `--kerberos-root-principal-password` and `--kerberos-kms-key-uri` flags (default: `false`). See [Enabling Hadoop Secure Mode via Kerberos](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/security#enabling_hadoop_secure_mode_via_kerberos) for more information.  
dataproc | kerberos.cross-realm-trust.admin-server | `hostname/address` | hostname/address of remote admin server (often the same as the KDC server).  
dataproc | kerberos.cross-realm-trust.kdc | `hostname/address` | hostname/address of remote KDC.  
dataproc | kerberos.cross-realm-trust.realm | `realm name` | Realm names can consist of any UPPERCASE ASCII string. Usually, the realm name is the same as your DNS domain name (in UPPERCASE). Example: If machines are named "machine-id.example.west-coast.mycompany.com", the associated realm may be designated as "EXAMPLE.WEST-COAST.MYCOMPANY.COM".  
dataproc | kerberos.cross-realm-trust.shared-password.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted shared password.  
dataproc | kerberos.kdc.db.key.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted file containing the KDC database master key.  
dataproc | kerberos.key.password.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted file that contains the password of the key in the keystore file.  
dataproc | kerberos.keystore.password.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted file containing the keystore password.  
dataproc | kerberos.keystore.uri**1** | `gs://<dir-path>` | Location in Cloud Storage of the keystore file containing the wildcard certificate and the private key used by cluster nodes.  
dataproc | kerberos.kms.key.uri | `KMS key URI` | The URI of the KMS key used to decrypt root password, for example `projects/project-id/locations/region/keyRings/key-ring/cryptoKeys/key` (see [Key resource ID](https://docs.cloud.google.com/kms/docs/object-hierarchy#key)).  
dataproc | kerberos.root.principal.password.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted password for Kerberos root principal.  
dataproc | kerberos.tgt.lifetime.hours | `hours` | Max life time of the ticket granting ticket.  
dataproc | kerberos.truststore.password.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted file that contains the password to the truststore file.  
dataproc | kerberos.truststore.uri**2** | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted trust store file containing trusted certificates.  
dataproc | pip.packages | Pip packages | This property takes a list of comma-separated Pip packages with specific versions, to be installed in the `base` Conda environment. For more information, see [Conda related Cluster properties](https://docs.cloud.google.com/managed-spark/docs/tutorials/python-configuration#conda_related_cluster_properties). (default: `empty`).  
dataproc | ranger.kms.key.uri | `KMS key URI` | The URI of the KMS key used to decrypt Ranger admin user password, for example `projects/project-id/locations/region/keyRings/key-ring/cryptoKeys/key` (see [Key resource ID](https://docs.cloud.google.com/kms/docs/object-hierarchy#key)).  
dataproc | ranger.admin.password.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted password for Ranger admin user.  
dataproc | ranger.db.admin.password.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted password for Ranger database admin user.  
dataproc | ranger.cloud-sql.instance.connection.name | `cloud sql instance connection name` | The connection name of the Cloud SQL instance, for example `project-id:region:name.`  
dataproc | ranger.cloud-sql.root.password.uri | `gs://<dir-path>` | Location in Cloud Storage of the KMS-encrypted password for the root user of the Cloud SQL instance.  
dataproc | ranger.cloud-sql.use-private-ip | `true` or `false` | Whether the communication between cluster instances and the Cloud SQL instance should be over private IP (default value is `false`).  
dataproc | solr.gcs.path | `gs://<dir-path>` | Cloud Storage path to act as Solr home directory.  
dataproc | startup.component.service-binding-timeout.hadoop-hdfs-namenode | `seconds` | The amount of time the Managed Service for Apache Spark startup script will wait for the hadoop-hdfs-namenode to bind to ports before deciding that its startup has succeeded. The maximum recognized value is 1800 seconds (30 minutes).  
dataproc | startup.component.service-binding-timeout.hive-metastore | `seconds` | The amount of time the Managed Service for Apache Spark startup script will wait for the hive-metastore service to bind to ports before deciding that its startup has succeeded. The maximum recognized value is 1800 seconds (30 minutes).  
dataproc | startup.component.service-binding-timeout.hive-server2 | `seconds` | The amount of time the Managed Service for Apache Spark startup script will wait for the hive-server2 to bind to ports before deciding that its startup has succeeded. The maximum recognized value is 1800 seconds (30 minutes).  
dataproc | user-attribution.enabled | `true` or `false` | Set this property to `true` to attribute a Managed Service for Apache Spark job to the identity of the user who submitted it (default value is `false`).  
dataproc | yarn.docker.enable | `true` or `false` | Set to `true` to enable the [Managed Service for Apache Spark Docker on YARN](https://docs.cloud.google.com/managed-spark/docs/guides/docker-yarn) feature (default value is `false`).  
dataproc | yarn.docker.image | `docker image` | When enabling the [Managed Service for Apache Spark Docker on YARN](https://docs.cloud.google.com/managed-spark/docs/guides/docker-yarn) feature (`dataproc:yarn.docker.enable=true`), you can use this optional property to specify your docker image (for example, `dataproc:yarn.docker.image=gcr.io/project-id/image:1.0.1`). If specified, the image is download and cached in all nodes of the cluster during cluster creation.  
dataproc | yarn.log-aggregation.enabled | `true` or `false` | Allows (`true`) turning on YARN log aggregation to the cluster's [`temp bucket`](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket). The bucket name is of the following form: `dataproc-temp-<REGION>-<PROJECT_NUMBER>-<RANDOM_STRING>`. (default: `true` for image versions 1.5+). **Note:** The cluster's temp bucket is not deleted when the cluster is deleted. Users can also set the location of aggregated YARN logs by overwriting the [`yarn.nodemanager.remote-app-log-dir`](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/ClusterSetup.html) YARN property.  
knox | gateway.host | `ip address` | To reduce the risk of remote code execution over unsecured notebook server APIs, the default setting for image versions 1.3+ is `127.0.0.1`, which restricts connections to `localhost` when [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways) is enabled. The default setting can be overridden, for example by setting this property to `0.0.0.0` to allow all connections.  
zeppelin | zeppelin.notebook.gcs.dir | `gs://<dir-path>` | Location in Cloud Storage to save Zeppelin notebooks.  
zeppelin | zeppelin.server.addr | `ip address` | To reduce the risk of remote code execution over unsecured notebook server APIs, the default setting for image versions 1.3+ is `127.0.0.1`, which restricts connections to `localhost` when [Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways) is enabled. This default setting can be overridden, for example by setting this property to `0.0.0.0` to allow all connections.  
  
**1** Keystore file: The keystore file contains the SSL certificate. It should be in Java KeyStore (JKS) format. When copied to VMs, it is renamed to `keystore.jks`. The SSL certificate should be a wildcard certificate that applies to each node in the cluster.

**2** Truststore file: The truststore file should be in Java KeyStore (JKS) format. When copied to VMs, it is renamed to `truststore.jks`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
