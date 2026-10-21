---
url: https://docs.cloud.google.com/managed-spark/docs/support/diagnose-clusters/
title: View cluster diagnostic data \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:31.104404+00:00
---

# View cluster diagnostic data  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/support/diagnose-clusters/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  View cluster diagnostic data Stay organized with collections  Save and categorize content based on your preferences. 

"View Managed Service for Apache Spark cluster diagnostic data"

You can take advantage of the following Managed Service for Apache Spark diagnostic data collection features to troubleshoot cluster and job issues:

  * **Checkpoint diagnostic data**: By default, Managed Service for Apache Spark collects checkpoint diagnostic data during the cluster lifecycle.
  * **Snapshot diagnostic data**: You can collect a one-time snapshot of cluster diagnostic data when needed.



## Checkpoint diagnostic data collection

By default, Managed Service for Apache Spark collects checkpoint diagnostic data during [cluster creation](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster), [cluster update](https://docs.cloud.google.com/managed-spark/docs/guides/manage-cluster#update_a_cluster), and [Managed Service for Apache Spark job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job) operations.

### Checkpoint data location

Managed Service for Apache Spark saves checkpoint diagnostic data in the cluster [temp bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) in Cloud Storage in the following folder (the `checkpoint diagnostic data folder`):
    
    
    gs://TEMP_BUCKET/google-cloud-dataproc-diagnostic/CLUSTER_UUID 
    

You can run the `gcloud dataproc clusters describe CLUSTER_NAME` command to list the cluster temp bucket

The default cluster temp bucket has a TTL retention period of 90 days. The data is deleted at the end of the retention period. You can [specify your own cluster temp bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket#create_your_own_staging_and_temp_buckets) with a different [TTL period](https://docs.cloud.google.com/storage/docs/managing-lifecycles) when you create a cluster.

### Checkpoint diagnostic data

  * **Cluster node detail logs:** Managed Service for Apache Spark runs the following commands to collect and write YARN and HDFS information to the following locations in the checkpoint diagnostic data folder in Cloud Storage. 

**Command executed** | **Location in diagnostic folder**  
---|---  
`yarn node -list -all` | `.../nodes/timestamp/yarn-nodes.log`  
`hdfs dfsadmin -report -live -decommissioning` | `.../nodes/timestamp/hdfs-nodes.log`  
`cp gs://STAGING_BUCKET/google-cloud-dataproc-metainfo/CLUSTER_UUID/nodes_exclude.xml` | `.../nodes/timestamp/nodes_exclude.xml`  
**Note:** Node detail snapshots capture cluster updates. The `timestamp` field in the path indicates the snapshot time.
  * **Job Details:** Managed Service for Apache Spark saves MapReduce job information and Spark job logs for jobs using the Managed Service for Apache Spark Jobs API. This job data is collected for each MapReduce and spark job submitted.

    * MapReduce `job.xml`: A file containing job configuration settings, saved at `.../jobs/JOB_UUID/mapreduce/job.xml`.
    * Spark event logs: Job execution details useful for debugging, saved at `.../jobs/JOB_UUID/spark/application-id`.
  * **Linux system information:** Managed Service for Apache Spark runs the following commands to collect and save system information in the following locations in the checkpoint diagnostic data folder in Cloud Storage.

**Command** | **Location in diagnostics folder**  
---|---  
`sysctl -a` | `.../system/sysctl.log`  
`cat /proc/sys/fs/file-nr` | `.../system/fs-file-nr.log`  
`ping -c 1` | `.../system/cluster-ping.log`  
`cp /etc/hosts` | `.../system/hosts_entries.log`  
`cp /etc/resolv.conf` | `.../system/resolv.conf`  
  * **Configuration files:** Managed Service for Apache Spark saves the following configuration files in the following locations in the checkpoint diagnostic data folder in Cloud Storage.

**Item(s) included** | **Location in diagnostics folder**  
---|---  
Managed Service for Apache Spark properties | `.../configs/dataproc/dataproc.properties`  
All files in   
`/etc/google-dataproc/` | `.../configs/dataproc/`  
All files in   
`/etc/hadoop/conf/` | `.../configs/hadoop/`  
All files in `/etc/hive/conf/` | `.../configs/hive/`  
All files in   
`/etc/hive-hcatalog/conf/` | `.../configs/hive-hcatalog/`  
All files in `/etc/knox/conf/` | `.../configs/knox/`  
All files in `/etc/pig/conf/` | `.../configs/pig/`  
All files in   
`/etc/presto/conf/` | `.../configs/presto/`  
All files in   
`/etc/spark/conf/` | `.../configs/spark/`  
All files in `/etc/tez/conf/` | `.../configs/tez/`  
All files in   
`/etc/zookeeper/conf/` | `.../configs/zookeeper/`  



### Share checkpoint diagnostic data with support

You can enable sharing checkpoint diagnostic data with [Google Cloud support](https://docs.cloud.google.com/managed-spark/docs/support/getting-support) in the following ways:

  * **Enable sharing at cluster creation** : Add the following [optional cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#examples) when you [create a cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster):
        
        dataproc:diagnostic.capture.access=GOOGLE_DATAPROC_DIAGNOSE
        

This property automatically shares collected checkpoint diagnostic data with [Google Cloud support](https://docs.cloud.google.com/managed-spark/docs/support/getting-support) so that you don't have to manually share after cluster creation each time.

**Note:** If you enable [**uniform bucket-level access**](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) on the cluster temp bucket, all of the temp bucket contents, including collected checkpoint diagnostic data and ephemeral data, such as MapReduce job history files, aggregated YARN logs, and Spark event logs, is shared with Google Cloud support.  
If **object-level access** control is enabled on the cluster temp bucket, only collected checkpoint diagnostic data (data in the checkpoint diagnostic data folder in Cloud Storage) is shared.
  * **Enable sharing after cluster creation** : You can enable sharing checkpoint data with [Google Cloud support](https://docs.cloud.google.com/managed-spark/docs/support/getting-support) after cluster creation by providing read access to checkpoint data to the service account used by the Google Cloud support, as follows:

    * If uniform bucket-level access is enabled on the temp bucket, add IAM policy binding: 
          
          gcloud storage buckets add-iam-policy-binding gs://TEMP_BUCKET \
              --member=serviceAccount:cloud-diagnose@cloud-dataproc.iam.gserviceaccount.com \
              --role=roles/storage.objectViewer
          

    * If object-level access control is enabled on the temp bucket, run the following command to share checkpoint diagnostic data: 
          
          gcloud storage objects update \
              gs://TEMP_BUCKET/google-cloud-dataproc-diagnostic/CLUSTER_UUID \
              --add-acl-grant=entity=user-cloud-diagnose@cloud-dataproc.iam.gserviceaccount.com,role=READER --recursive
          




### Disable checkpoint diagnostic data collection

To disable the collection of checkpoint diagnostic data on a cluster, set [`dataproc:diagnostic.capture.enabled=false`](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc_service_properties_table) when you create the cluster.

## Snapshot diagnostic data collection

You can run the following [`gcloud dataproc clusters diagnose`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/diagnose) command to collect a snapshot of diagnostic data from a running cluster. The data is written as an archive (tar) file to the Managed Service for Apache Spark [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) in Cloud Storage.
    
    
    gcloud dataproc clusters diagnose CLUSTER_NAME \
        --region=REGION \
        --tarball-access=GOOGLE_DATAPROC_DIAGNOSE \
        --tarball-gcs-dir=TARBALL_DIR
    

Notes:

  * CLUSTER_NAME: The name of the cluster to diagnose.
  * REGION: The cluster's region, for example, `us-central1`.
  * `--tarball-access`=`GOOGLE_DATAPROC_DIAGNOSE` This flag provides access to the diagnostic tar file to [Google Cloud support](https://docs.cloud.google.com/managed-spark/docs/support/getting-support). Provide Google Cloud support with the Cloud Storage path of the diagnostic tar file.

As an alternative to providing the tar file to support, you can provide the cluster UUID, operation ID of the diagnose command, and the Cloud Storage location of the cluster configuration bucket.

If you choose to write diagnostic tar file to a specific directory, provide Google Cloud support with the full Cloud Storage path of the tar file which is printed by the diagnose command.

**Bucket access and scope of shared content** : The access setting on the Cloud Storage bucket that contains the diagnostic tar file determines the scope of the content shared with Google Cloud support:

    * **Uniform bucket-level access** : If [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) is enabled on the Managed Service for Apache Spark staging bucket or, if a TARBALL_DIR is specified, on the bucket that contains the TARBALL_DIR, all of the bucket contents are shared with Google Cloud support.

    * **Object-level access** : If object-level access is enabled on the Managed Service for Apache Spark staging bucket or, if a TARBALL_DIR is specified, on the bucket that contains the TARBALL_DIR, only the diagnostic tar file is shared with Google Cloud support.

  * TARBALL_DIR: Optional. You can use this flag to specify a Cloud Storage directory where the diagnostic tar file will be written. If this flag is omitted, the diagnostic tar file will be written to the [Managed Service for Apache Spark staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket).

  * Additional flags:

    * `--start-time` with `--end-time`: Use both flags to specify a time range in `%Y-%m-%dT%H:%M:%S.%fZ` format for the collection of diagnostic data. Specifying a time range also enables the collection of Managed Service for Apache Spark autoscaling logs during the time range (by default, Managed Service for Apache Spark autoscaling logs are not collected in the diagnostic snapshot data).

    * You can use either of both of the following flags to collect specific job driver, Spark event, YARN application, and [Sparklens](https://spark-packages.org/package/qubole/sparklens) output logs:

      * `--job-ids`: A comma-separated list of job IDs
      * `--yarn-application-ids`: A comma-separated list of YARN application IDs 

        * YARN log aggregation must be enabled (`yarn.log-aggregation-enable=true`) for the collection of YARN application logs.
        * For MapReduce jobs, YARN application logs only are collected.



### Optional: Run the diagnostic script

The `gcloud dataproc clusters diagnose` command can fail or time-out if a cluster is in an error state and cannot accept diagnose tasks from the Managed Service for Apache Spark server. As an alternative to running the diagnose command, you can [use SSH](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) to connect to the cluster then run the script locally on the master node.
    
    
    gcloud compute ssh HOSTNAME
    gcloud storage cp gs://dataproc-diagnostic-scripts/diagnostic-script.sh .
    sudo bash diagnostic-script.sh

The diagnostic archive tar file is saved in a local directory. The command output lists the location of the tar file with instructions on how to upload the tar file to a Cloud Storage bucket.

### Diagnostic snapshot data

Cluster snapshot data includes a diagnostic summary and several archive sections. 

**Diagnostic summary:** The archive file includes `summary.txt` that is at the root of the archive. It provides an overview of cluster status, including YARN, HDFS, disk, and networking status, and includes warnings to alert you to potential problems.

**Archive sections:** The archive file includes the following information that is written to the following archive file locations.

  * **Daemons and services information**

Command executed | Location in archive  
---|---  
`yarn node -list -all` | `/system/yarn-nodes.log`  
`hdfs dfsadmin -report -live -decommissioning` | `/system/hdfs-nodes.log`  
`hdfs dfs -du -h` | `/system/hdfs-du.log`  
`service --status-all` | `/system/service.log`  
`systemctl --type service` | `/system/systemd-services.log`  
`curl "http://${HOSTNAME}:8088/jmx"` | `/metrics/resource_manager_jmx`  
`curl "http://${HOSTNAME}:8088/ws/v1/cluster/apps"` | `/metrics/yarn_app_info`  
`curl "http://${HOSTNAME}:8088/ws/v1/cluster/nodes"` | `/metrics/yarn_node_info`  
`curl "http://${HOSTNAME}:9870/jmx"` | `/metrics/namenode_jmx`  
  * **JVM information**

Command executed | Location in archive  
---|---  
`jstack -l "${DATAPROC_AGENT _PID}"_` | `jstack/agent${DATAPROC_AGENT_PID}.jstack`  
`jstack -l "${PRESTO _PID}"_` | `jstack/agent${PRESTO_PID}.jstack`  
`jstack -l "${JOB_DRIVER _PID}"_` | `jstack/driver${JOB_DRIVER_PID}.jstack`  
`jinfo "${DATAPROC_AGENT _PID}"_` | `jinfo/agent${DATAPROC_AGENT_PID}.jstack`  
`jinfo "${PRESTO _PID}"_` | `jinfo/agent${PRESTO_PID}.jstack`  
`jinfo "${JOB_DRIVER _PID}"_` | `jinfo/agent${JOB_DRIVER_PID}.jstack`  
  * **Linux system information**

Command executed | Location in archive  
---|---  
`df -h` | `/system/df.log`  
`ps aux` | `/system/ps.log`  
`free -m` | `/system/free.log`  
`netstat -anp` | `/system/netstat.log`  
`sysctl -a` | `/system/sysctl.log`  
`uptime` | `/system/uptime.log`  
`cat /proc/sys/fs/file-nr` | `/system/fs-file-nr.log`  
`ping -c 1` | `/system/cluster-ping.log`  
  * **Log files**

Item included | Location in archive  
---|---  
All logs in `/var/log` with the following prefixes in their filename:   
`cloud-sql-proxy`  
`dataproc`  
`druid`  
`gcdp`  
`google`  
`hadoop`  
`hdfs`  
`hive`  
`knox`  
`presto`  
`spark`  
`syslog`  
`yarn`  
`zookeeper` | Files are placed in the archive `logs` folder, and keep their original filenames.  
Managed Service for Apache Spark node startup logs for each node (master and worker) in your cluster. | Files are placed in the archive `node_startup` folder, which contains separate subfolders for each machine in the cluster.  
Component gateway logs from `journalctl -u google-dataproc-component-gateway` | `/logs/google-dataproc-component-gateway.log`  
  * **Configuration files**

Item(s) included | Location in archive  
---|---  
VM metadata | `/conf/dataproc/metadata`  
Environment variables in `/etc/environment` | `/conf/dataproc/environment`  
Managed Service for Apache Spark properties | `/conf/dataproc/dataproc.properties`  
All files in `/etc/google-dataproc/` | `/conf/dataproc/`  
All files in `/etc/hadoop/conf/` | `/conf/hadoop/`  
All files in `/etc/hive/conf/` | `/conf/hive/`  
All files in `/etc/hive-hcatalog/conf/` | `/conf/hive-hcatalog/`  
All files in `/etc/knox/conf/` | `/conf/knox/`  
All files in `/etc/pig/conf/` | `/conf/pig/`  
All files in `/etc/presto/conf/` | `/conf/presto/`  
All files in `/etc/spark/conf/` | `/conf/spark/`  
All files in `/etc/tez/conf/` | `/conf/tez/`  
All files in `/etc/zookeeper/conf/` | `/conf/zookeeper/`  



### Share the archive file

**Sensitive log information:** If you pass sensitive information in arguments, metadata, or driver output, your logs may contain sensitive information. Check archive file contents before sharing the archive.

You can share the archive file with Google Cloud support or users to obtain help to troubleshoot cluster or job issues.

To share the archive file:

  * [Copy the archive file](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) from Cloud Storage, and then share the downloaded archive, or
  * [Change the permissions](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update "Cloud Storage permission instructions") on the archive to allow other Google Cloud users or projects to access the file.

Example: The following command gives read permissions to the archive to owners of the project `test-project`:
        
        gcloud storage objects update PATH_TO_ARCHIVE --add-acl-grant=entity=project-owners-test-project,role=READER
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
