---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions/
title: Initialization actions \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:33.868911+00:00
---

# Initialization actions  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Initialization actions Stay organized with collections  Save and categorize content based on your preferences. 

When [creating a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster), you can specify initialization actions in executables or scripts that Managed Service for Apache Spark will run on all nodes in your Managed Service for Apache Spark cluster immediately after the cluster is set up. Initialization actions often set up job dependencies, such as installing Python packages, so that jobs can be submitted to the cluster without having to install dependencies when the jobs are run.

You can find sample initialization action scripts at the following locations: Note: **Google does not support these samples**.

  * [GitHub repository](https://github.com/GoogleCloudDataproc/initialization-actions)
  * [Cloud Storage](https://docs.cloud.google.com/storage "Cloud Storage")—in the regional `gs://goog-dataproc-initialization-actions-REGION` public buckets



## Important considerations and guidelines

  * Don't create production clusters that reference initialization actions located in the `gs://goog-dataproc-initialization-actions-REGION` public buckets. These scripts are provided as reference implementations. They are synchronized with ongoing GitHub repository changes, and updates to these scripts can break your cluster creation. Instead, copy the initialization action from the public bucket into a versioned Cloud Storage bucket folder, as shown in the following example: 
        
        REGION=COMPUTE_REGION
        gcloud storage cp gs://goog-dataproc-initialization-actions-${REGION}/cloud-sql-proxy/cloud-sql-proxy.sh \
            gs://my-bucket/cloud-sql-proxy/v1.0/cloud-sql-proxy.sh
        

Then, create the cluster by referencing the copy in Cloud Storage: 
        
        gcloud dataproc clusters create CLUSTER_NAME \
            --region=${REGION} \
            --initialization-actions=gs://my-bucket/cloud-sql-proxy/v1.0/cloud-sql-proxy.sh \
            ...other flags...
        

  * Initialization actions are executed on each node in series during cluster creation. They are also executed on each added node when [scaling](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scaling-clusters) or [autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) clusters up.

  * When you update initialization actions—for example, when you sync your Cloud Storage initialization actions to changes made to public bucket or GitHub repository initialization actions—create a new (preferably version-named) folder to receive the updated initialization actions. If, instead, you update the initialization action in place, new nodes, such as those added by the autoscaler, will run the updated-in-place initialization action, not the prior-version initialization action that ran on existing nodes. Such initialization action differences can result in inconsistent or broken cluster nodes.

  * Initialization actions run as the `root` user. You **do not** need to use `sudo`.

  * Use **absolute paths** in initialization actions.

  * Use a [shebang line](https://goo.gl/IcHZya) in initialization actions to indicate how the script should be interpreted (such as `#!/bin/bash` or `#!/usr/bin/python`).

  * Use **Unix-style line endings** (LF) in initialization actions. If you create initialization actions on Windows, they might contain Windows-style line endings (CRLF), which can cause script execution failures.

  * If an initialization action terminates with a non-zero exit code, the cluster create operation will report an "ERROR" status. To debug the initialization action, use SSH to connect into the cluster's VM instances, and then examine the logs. After fixing the initialization action problem, you can delete, then re-create the cluster.

  * If you create a Managed Service for Apache Spark cluster with [internal IP addresses only](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network#create_a_cloud_dataproc_cluster_with_internal_ip_address_only), attempts to access `github.com` over the internet in an initialization action will fail unless you have configured routes to direct the traffic through [Cloud NAT](https://docs.cloud.google.com/nat/docs) or a [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn). Without access to the internet, you can enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) and place job dependencies in [Cloud Storage](https://docs.cloud.google.com/storage); cluster nodes can download the dependencies from Cloud Storage from internal IPs.

  * You can use [Managed Service for Apache Spark custom images](https://docs.cloud.google.com/managed-spark/docs/guides/images) instead of initialization actions to set up job dependencies.

  * **Initialization processing:**

    * Pre-2.0 image clusters: 
      * _Master_ : To allow initialization actions run on masters to write files to HDFS, master node initialization actions don't start until HDFS is writeable (until HDFS has exited safemode and at least two HDFS DataNodes have joined). 
      * _Worker_ : If you set the `dataproc:dataproc.worker.custom.init.actions.mode` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) to `RUN_BEFORE_SERVICES`, each worker runs its initialization actions before it starts its HDFS datanode and YARN nodemanager daemons. Since Managed Service for Apache Spark does not run master initialization actions until HDFS is writeable, which requires 2 HDFS datanode daemons to be running, setting this property may increase cluster creation time.
    * 2.0+ image clusters:

      * _Master_ : Master node initialization actions may run before HDFS is writeable. If you run initialization actions that stage files in HDFS or depend on the availability of HDFS-dependent services, such as Ranger, set the `dataproc.master.custom.init.actions.mode` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) to `RUN_AFTER_SERVICES`. Note: since this property setting can increase cluster creation time—see the explanation for cluster creation delay for pre-2.0 image cluster workers—use it only when necessary (as a general practice, rely on the default `RUN_BEFORE_SERVICES` setting for this property).
      * _Worker_ : The `dataproc:dataproc.worker.custom.init.actions.mode` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) is set to `RUN_BEFORE_SERVICES` and **cannot** be passed to the cluster when the cluster is created (you cannot change the property setting). Each worker runs its initialization actions before it starts its HDFS datanode and YARN nodemanager daemons. Since Managed Service for Apache Spark does not wait for HDFS to be writeable before running master initialization actions, master and worker initialization actions run in parallel.
    * Recommendations:

      * Use metadata to determine a node's role to conditionally execute an initialization action on nodes (see [Using cluster metadata](https://github.com/GoogleCloudDataproc/initialization-actions#using-cluster-metadata)).
      * Fork a copy of an initialization action to a Cloud Storage bucket for stability (see [How initialization actions are used](https://github.com/GoogleCloudDataproc/initialization-actions#how-initialization-actions-are-used)).
      * Add retries when you download from the internet to help stabilize the initialization action.



## Use initialization actions

Cluster initialization actions can be specified regardless of how you create a cluster:

  * Through the Google Cloud console
  * Using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)
  * Programmatically with the Dataproc [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API (see [NodeInitializationAction](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#NodeInitializationAction))



### Google Cloud console

* Open [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
* Click **Additional configuration** to expand that section.
* Edit **Customization & Other**.
* In the panel that opens, click **Add initialization actions** , then enter or browse to select the Cloud Storage location of an initialization action.

### gcloud CLI

When creating a cluster with the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command, specify one or more comma-separated Cloud Storage locations (URIs) of the initialization executables or scripts with the `--initialization-actions` flag. **Note:** Multiple consecutive "/"s in a Cloud Storage location URI after the initial "gs://", such as "gs://bucket/my//object//name", are not supported. Run `gcloud dataproc clusters create --help` for command information.
    
    
    gcloud dataproc clusters create cluster-name \
        --region=${REGION} \
        --initialization-actions=Cloud Storage URI(s) (gs://bucket/...) \
        --initialization-action-timeout=timeout-value (default=10m) \
        ... other flags ...
    

Notes: 

  * Use the `--initialization-action-timeout` flag to specify a timeout period for the initialization action. The default timeout value is 10 minutes. If the initialization executable or script has not completed by the end of the timeout period, Managed Service for Apache Spark cancels the initialization action.
  * Use the `dataproc:dataproc.worker.custom.init.actions.mode` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) to run the initialization action on primary workers _before_ the node manager and datanode daemons are started. 

**Let the Google Cloud console construct your cluster create request** : At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request. (Note: the Google Cloud console doesn't include the REST API `executionTimeout` field or the Google Cloud CLI `--initialization-action-timeout` flag).

### REST API

Specify one or more scripts or executables in a [ClusterConfig.initializationActions](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig) array as part a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request.

**Example**
    
    
    POST /v1/projects/my-project-id/regions/us-central1/clusters/
    {
      "projectId": "my-project-id",
      "clusterName": "example-cluster",
      "config": {
        "configBucket": "",
        "gceClusterConfig": {
          "subnetworkUri": "default",
          "zoneUri": "us-central1-b"
        },
        "masterConfig": {
          "numInstances": 1,
          "machineTypeUri": "n1-standard-4",
          "diskConfig": {
            "bootDiskSizeGb": 500,
            "numLocalSsds": 0
          }
        },
        "workerConfig": {
          "numInstances": 2,
          "machineTypeUri": "n1-standard-4",
          "diskConfig": {
            "bootDiskSizeGb": 500,
            "numLocalSsds": 0
          }
        },
        **"initializationActions":** [
          {
            **"executableFile":** "gs://cloud-example-bucket/my-init-action.sh"
          }
        ]
      }
    }
    

**Let the Google Cloud console construct your cluster create request** : At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request. (Note: the Google Cloud console doesn't include the REST `executionTimeout` field or the Google Cloud CLI `--initialization-action-timeout` flag).

### Pass arguments to initialization actions

Managed Service for Apache Spark sets special [metadata](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/metadata) values for the instances that run in your clusters. You can set your own [custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#custom) as a way to pass arguments to initialization actions.
    
    
    gcloud dataproc clusters create cluster-name \
        --region=${REGION} \
        --initialization-actions=Cloud Storage URI(s) (gs://bucket/...) \
        --metadata=name1=value1,name2=value2... \
        ... other flags ...
    

Metadata values can be read within initialization actions as follows:
    
    
    var1=$(/usr/share/google/get_metadata_value attributes/name1)
    

### Node selection

If you want to limit initialization actions to master, driver or worker nodes, you can add node-selection logic to your executable or script.
    
    
    ROLE=$(/usr/share/google/get_metadata_value attributes/dataproc-role)
    if [[ "${ROLE}" == 'Master' ]]; then
      ... master specific actions ...
    else if [[ "${ROLE}" == 'Driver' ]]; then
      ... driver specific actions ...
    else
      ... worker specific actions ...
    fi
    

### Stage binaries

A common cluster initialization scenario is the staging of job binaries on a cluster to eliminate the need to stage the binaries each time a job is submitted. For example, assume that the following initialization script is stored in `gs://my-bucket/download-job-jar.sh`, a Cloud Storage bucket location:
    
    
    #!/bin/bash
    ROLE=$(/usr/share/google/get_metadata_value attributes/dataproc-role)
    if [[ "${ROLE}" == 'Master' ]]; then
      gcloud storage cp gs://my-bucket/jobs/sessionalize-logs-1.0.jar home/username
    fi
    

The location of this script can be passed to the `gcloud dataproc clusters create` command:
    
    
    gcloud dataproc clusters create my-dataproc-cluster \
        --region=${REGION} \
        --initialization-actions=gs://my-bucket/download-job-jar.sh
    

Managed Service for Apache Spark will run this script on all nodes, and, as a consequence of the script's node-selection logic, will download the jar to the master node. Submitted jobs can then use the pre-staged jar:
    
    
    gcloud dataproc jobs submit hadoop \
        --cluster=my-dataproc-cluster \
        --region=${REGION} \
        --jar=file:///home/username/sessionalize-logs-1.0.jar
    

### Initialization actions samples

Frequently used and other sample initialization actions scripts are located in `gs://goog-dataproc-initialization-actions-<REGION>`, a regional public Cloud Storage buckets, and in a [GitHub repository](https://github.com/GoogleCloudDataproc/initialization-actions). To contribute a script, review the [`CONTRIBUTING.md`](https://github.com/GoogleCloudDataproc/initialization-actions/blob/master/CONTRIBUTING.md "Contributing to GitHub") document, and then file a pull request.

## Logging

Output from the execution of each initialization action is logged for each instance in `/var/log/dataproc-initialization-script-X.log`, where `X` is the zero-based index of each successive initialization action script. For example, if your cluster has two initialization actions, the outputs will be logged in `/var/log/dataproc-initialization-script-0.log` and `/var/log/dataproc-initialization-script-1.log`.

## What's next

Explore [GitHub initialization actions](https://github.com/GoogleCloudDataproc/initialization-actions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
