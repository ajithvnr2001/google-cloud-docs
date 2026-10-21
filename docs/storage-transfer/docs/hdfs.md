---
url: https://docs.cloud.google.com/storage-transfer/docs/hdfs/
title: Transfer from HDFS to Cloud Storage \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:44:51.416039+00:00
---

# Transfer from HDFS to Cloud Storage  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/hdfs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer from HDFS to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Storage Transfer Service supports transfers from cloud and on-premises Hadoop Distributed File System (HDFS) sources.

Transfers from HDFS must use Cloud Storage as the destination.

Use cases include migrating from on-premises storage to Cloud Storage, archiving data to free up on-premises storage space, replicating data to Google Cloud for business continuity, or transferring data to Google Cloud for analysis and processing.

## Configure permissions

Before creating a transfer, you must configure permissions for the following entities:

![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/account_circle/wght600fill1/48px.svg) | The **user account** being used to create the transfer. This is the account that is signed in to the Google Cloud console, or the account that is specified when authenticating to the `gcloud` CLI. The user account can be a regular user account, or a user-managed service account.  
---|---  
![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/cloud_circle/wght600fill1/48px.svg) | The **[service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)** used by Storage Transfer Service. This account is generally identified by its email address, which uses the format `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`.   
![](https://docs.cloud.google.com/static/storage-transfer/docs/create-transfers/images/forklift-circle.png) | The **transfer agent account** that provides Google Cloud permissions for transfer agents. Transfer agent accounts use the credentials of the user installing them, or the credentials of a user-managed service account, to authenticate.  
  
See [Agent-based transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions) for instructions.

## Install agents into an agent pool

Agent-based transfers use software agents to orchestrate transfers. These agents must be installed on one or more machines with access to your file system. Agents must have access to the namenode, all datanodes, the Hadoop Key Management Server (KMS), and the Kerberos Key Distribution Center (KDC).

Transfer agents work together in an agent pool. Increasing the number of agents can increase overall job performance, but this is dependent on several factors.

  * Adding more agents can help, up to about half the number of nodes in your HDFS cluster. For example, with a 30-node cluster, increasing from 5 to 15 agents should improve performance, but beyond 15 is unlikely to make much difference.

  * For a small HDFS cluster, one agent may be sufficient.

  * Additional agents tend to have a larger impact on performance when a transfer includes a large number of small files. Storage Transfer Service achieves high throughput by parallelizing transfer tasks among multiple agents. The more files in the workload, the more benefit there is to adding more agents.




Don't include sensitive information such as personally identifiable information (PII) or security data in your agent pool name or agent ID prefix. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

### Create an agent pool

Create an [agent pool](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-pools). Use your **user account** ![User account symbol](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/account_circle/wght600fill1/24px.svg) for this action.

### Install agents

Install agents into the agent pool. Use your **transfer agent account** ![](https://docs.cloud.google.com/static/storage-transfer/docs/create-transfers/images/forklift-circle.png) for this action.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Agent pools** page.

[Go to Agent pools](https://console.cloud.google.com/transfer/agent-pools)

  2. Select the agent pool to which to add the new agent.

  3. Click **Install agent**.

  4. Follow the instructions to install and run the agent.

For more information about the agent's command-line options, see [Agent command-line options](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-command-options).




###  gcloud CLI 

To install one or more agents using the gcloud CLI, run `gcloud transfer agents install`:
    
    
    gcloud transfer agents install --pool=POOL_NAME \
      --count=NUM_AGENTS \
      --mount-directories=MOUNT_DIRECTORIES \
      --hdfs-namenode-uri=HDFS_NAMENODE_URI \
      --hdfs-username=HDFS_USERNAME \
      --hdfs-data-transfer-protection=HDFS_DATA_TRANSFER_PROTECTION \
      --kerberos-config-file=KERBEROS_CONFIG_FILE \
      --kerberos-keytab-file=KERBEROS_KEYTAB_FILE \
      --kerberos-user-principal=KERBEROS_USER_PRINCIPAL \
      --kerberos-service-principal=KERBEROS_SERVICE_PRINCIPAL \
    

Replace the following:

  * `--hdfs-namenode-uri` specifies an HDFS cluster including a schema, namenode, and port, in URI format. For example:

    * `rpc://my-namenode:8020`
    * `http://my-namenode:9870`

Use HTTP or HTTPS for WebHDFS. If no schema is provided, we assume RPC. If no port is provided, the default is `8020` for RPC, `9870` for HTTP, and `9871` for HTTPS. For example, the input `my-namenode` becomes `rpc://my-namenode:8020`.

If your cluster is configured with multiple namenodes, specify the current primary node. See Clusters with multiple namenodes for more information.

  * `--hdfs-username` is the username for connecting to an HDFS cluster with simple auth. Omit this flag if you're authenticating with Kerberos, or if you're connecting without any authentication.

  * `--hdfs-data-transfer-protection` (optional) is the client-side quality of protection (QOP) setting for Kerberized clusters. The value cannot be more restrictive than the server-side QOP value. Valid values are: `authentication`, `integrity`, and `privacy`.




If you're authenticating with Kerberos, also include the following flags:

  * `--kerberos-config-file` is the path to a Kerberos configuration file. For example, `--kerberos-config-file=/etc/krb5.conf`.

  * `--kerberos-user-principal` is the Kerberos user principal to use. For example, `--kerberos-user-principal=user1`.

  * `--kerberos-keytab-file` is the path to a Keytab file containing the user principal specified with the `--kerberos-user-principal` flag. For example, `--kerberos-keytab-file=/home/me/kerberos/user1.keytab`.

  * `--kerberos-service-principal` is the Kerberos service principal to use, of the form `<primary>/<instance>`. Realm is mapped from your Kerberos configuration file; any supplied realm is ignored. If this flag is not specified, the default is `hdfs/<namenode_fqdn>` where `<namenode_fqdn>` is the fully qualified domain name specified in the configuration file.

For example, `--kerberos-service-principal=hdfs/my-namenode.a.example.com`.




The tool walks you through any required steps to install the agent(s). This command installs NUM_AGENTS agent(s) on your machine, mapped to the pool name specified as POOL_NAME, and authenticates the agent using your `gcloud` credentials. The pool name must exist, or an error is returned.

The `--mount-directories` flag is optional but is strongly recommended. Its value is a comma-separated list of directories on the file system to which to grant the agent access. Omitting this flag mounts the entire file system to the agent container. See the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--mount-directories) for more details.

###  `docker run`

Before using `docker run` to install agents, follow the instructions to [install Docker](https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up#install_docker).

The `docker run` command installs one agent. To increase the number of agents in your pool, re-run this command as many times as required.

The required command flags depend on the authentication type you're using.

###  Kerberos 

To authenticate to your file system using Kerberos, use the following command:
    
    
    sudo docker run -d --ulimit memlock=64000000 --rm \
      --network=host \
      -v /:/transfer_root \
      gcr.io/cloud-ingest/tsop-agent:latest \
      --enable-mount-directory \
      --project-id=${PROJECT_ID} \
      --hostname=$(hostname) \
      --creds-file="service_account.json" \
      --agent-pool=${AGENT_POOL_NAME} \
      --hdfs-namenode-uri=cluster-namenode \
      --kerberos-config-file=/etc/krb5.conf \
      --kerberos-user-principal=user \
      --kerberos-keytab-file=/path/to/folder.keytab
    

Replace the following:

  * `--network=host` should be omitted if you're running more than one agent on this machine.
  * `--hdfs-namenode-uri`: A schema, namenode, and port, in URI format, representing an HDFS cluster. For example:

    * `rpc://my-namenode:8020`
    * `http://my-namenode:9870`



Use HTTP or HTTPS for WebHDFS. If no schema is provided, we assume RPC. If no port is provided, the default is `8020` for RPC, `9870` for HTTP, and `9871` for HTTPS. For example, the input `my-namenode` becomes `rpc://my-namenode:8020`.

If your cluster is configured with multiple namenodes, specify the current primary node. See Clusters with multiple namenodes for more information.

  * `--kerberos-config-file`: Path to a Kerberos configuration file. Default is `/etc/krb5.conf`.
  * `--kerberos-user-principal`: The Kerberos user principal.
  * `--kerberos-keytab-file`: Path to a Keytab file containing the user principal specified with `--kerberos-user-principal`.
  * `--kerberos-service-principal`: Kerberos service principal to use, of the form 'service/instance'. Realm is mapped from your Kerberos configuration file; any supplied realm is ignored. If this flag is not specified, the default is `hdfs/<namenode_fqdn>` where `fqdn` is the fully qualified domain name.



###  Simple auth

To authenticate to your file system using simple auth:
    
    
    sudo docker run -d --ulimit memlock=64000000 --rm \
      --network=host \
      -v /:/transfer_root \
      gcr.io/cloud-ingest/tsop-agent:latest \
      --enable-mount-directory \
      --project-id=${PROJECT_ID} \
      --hostname=$(hostname) \
      --creds-file="${CREDS_FILE}" \
      --agent-pool="${AGENT_POOL_NAME}" \
      --hdfs-namenode-uri=cluster-namenode \
      --hdfs-username="${USERNAME}"
    

Replace the following:

  * `--hdfs-username`: Username to use when connecting to an HDFS cluster using simple auth.
  * `--hdfs-namenode-uri`: A schema, namenode, and port, in URI format, representing an HDFS cluster. For example: 
    * `rpc://my-namenode:8020`
    * `http://my-namenode:9870`



Use HTTP or HTTPS for WebHDFS. If no schema is provided, we assume RPC. If no port is provided, the default is `8020` for RPC, `9870` for HTTP, and `9871` for HTTPS. For example, the input `my-namenode` becomes `rpc://my-namenode:8020`.

If your cluster is configured with multiple namenodes, specify the current primary node. See Clusters with multiple namenodes for more information.

###  No auth

To connect to your file system without any authentication:
    
    
    sudo docker run -d --ulimit memlock=64000000 --rm \
      --network=host \
      -v /:/transfer_root \
      gcr.io/cloud-ingest/tsop-agent:latest \
      --enable-mount-directory \
      --project-id=${PROJECT_ID} \
      --hostname=$(hostname) \
      --creds-file="${CREDS_FILE}" \
      --agent-pool="${AGENT_POOL_NAME}" \
      --hdfs-namenode-uri=cluster-namenode \
    

Replace the following:

  * `--hdfs-namenode-uri`: A schema, namenode, and port, in URI format, representing an HDFS cluster. For example: 
    * `rpc://my-namenode:8020`
    * `http://my-namenode:9870`



Use HTTP or HTTPS for WebHDFS. If no schema is provided, we assume RPC. If no port is provided, the default is `8020` for RPC, `9870` for HTTP, and `9871` for HTTPS. For example, the input `my-namenode` becomes `rpc://my-namenode:8020`.

If your cluster is configured with multiple namenodes, specify the current primary node. See Clusters with multiple namenodes for more information.

## Transfer options

The following Storage Transfer Service features are available for transfers from HDFS to Cloud Storage.

  * [Filter by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers)
  * [Delete at source](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec#transferoptions)
  * [Manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest)
  * [Cloud Monitoring](https://docs.cloud.google.com/storage-transfer/docs/monitor-transfer-jobs)



Files transferred from HDFS do not retain their [metadata](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation).

## Create a transfer

Don't include sensitive information such as personally identifiable information (PII) or security data in your transfer job name. Resource names may be propagated to the names of other Google Cloud resources and may be exposed to Google-internal systems outside of your project. 

Storage Transfer Service provides multiple interfaces through which to create a transfer.

###  Google Cloud console 

  1. Go to the **Storage Transfer Service** page in the Google Cloud console.

[Go to Storage Transfer Service](https://console.cloud.google.com/transfer/)

  2. Click **Create transfer job**. The **Create a transfer job** page is displayed.

  3. Select **Hadoop Distributed File System** as the **Source type**. The destination must be **Google Cloud Storage**.

Click **Next step**.




### Configure your source

  1. Specify the required information for this transfer:

     1. Select the agent pool you configured for this transfer.

     2. Enter the **Path** to transfer from, relative to the root directory.

  2. Optionally, specify any [filters](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers) to apply to the source data.

  3. Click **Next step**.




### Configure your sink

  1. In the **Bucket or folder** field, enter the destination bucket and (optionally) folder name, or click **Browse** to select a bucket from a list of existing buckets in your current project. To create a new bucket, click ![Bucket icon](https://docs.cloud.google.com/static/storage-transfer/docs/images/bucket_icon.png)**Create new bucket**.

  2. Click **Next step**.




### Schedule the transfer

You can schedule your transfer to run one time only, or configure a recurring transfer.

Click **Next step**.

### Choose transfer settings

  1. In the **Description** field, enter a description of the transfer. As a best practice, enter a description that is meaningful and unique so that you can tell jobs apart.

  2. Under **Metadata options** , select your Cloud Storage storage class, and whether to save each objects' creation time. See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details.

  3. Under **When to overwrite** , select one of the following:

     * **Never** : Do not overwrite destination files. If a file exists with the same name, it will not be transferred.

     * **If different** : Overwrites destination files if the source file with the same name has different Etags or checksum values.

     * **Always** : Always overwrites destination files when the source file has the same name, even if they're identical.

  4. Under **When to delete** , select one of the following:

     * **Never** : Never delete files from either the source or destination.

     * **Delete files from destination if they're not also at source** : If files in the destination Cloud Storage bucket aren't also in the source, then delete the files from the Cloud Storage bucket.

This option ensures that the destination Cloud Storage bucket exactly matches your source.

  5. Select whether to enable [transfer logging](https://docs.cloud.google.com/storage-transfer/docs/on-prem-transfer-log-format) and/or [Pub/Sub notifications](https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer).




Click **Create** to create the transfer job.

###  gcloud CLI 

To create a new transfer job, use the `gcloud transfer jobs create` command. Creating a new job initiates the specified transfer, unless a schedule or `--do-not-run` is specified.
    
    
    gcloud transfer jobs create \
      hdfs:///PATH/ gs://BUCKET_NAME/PATH/
      --source-agent-pool=AGENT_POOL_NAME
    

Replace the following:

  * `PATH` is an absolute path from the root of the HDFS cluster. The cluster namenode and port are configured at the agent level, so the job creation command only needs to specify the (optional) path and the agent pool.

  * `--source-agent-pool` specifies the source agent pool to use for this transfer.




Additional options include:

  * `--do-not-run` prevents Storage Transfer Service from running the job upon submission of the command. To run the job, [update](https://docs.cloud.google.com/storage-transfer/docs/manage-transfers#update-job) it to add a schedule, or use `jobs run` to [start it manually](https://docs.cloud.google.com/storage-transfer/docs/manage-transfers#run-job).

  * `--manifest-file` specifies the path to a CSV file in Cloud Storage containing a list of files to transfer from your source. For manifest file formatting, see [Transfer specific files or objects using a manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest).

  * **Job information** : You can specify `--name` and `--description`.

  * **Schedule** : Specify `--schedule-starts`, `--schedule-repeats-every`, and `--schedule-repeats-until`, or `--do-not-run`.

  * **Object conditions** : Use conditions to determine which objects are transferred. These include `--include-prefixes` and `--exclude-prefixes`, and the time-based conditions in `--include-modified-[before | after]-[absolute | relative]`. If you specified a folder with your source, prefix filters are relative to that folder. See [Filter source objects by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers) for more information.

  * **Transfer options** : Specify whether to overwrite destination files (`--overwrite-when=different` or `always`) and whether to delete certain files during or after the transfer (`--delete-from=destination-if-unique` or `source-after-transfer`); and optionally set a storage class on transferred objects (`--custom-storage-class`).

  * **Notifications** : Configure [Pub/Sub notifications for transfers](https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer) with `--notification-pubsub-topic`, `--notification-event-types`, and `--notification-payload-format`.




To view all options, run `gcloud transfer jobs create --help` or refer to the [`gcloud` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/create).

###  REST API 

To create a transfer from an HDFS source using the REST API, create a JSON object similar to the following example.
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    {
      ...
      "transferSpec": {
        "source_agent_pool_name":"POOL_NAME",
        "hdfsDataSource": {
          "path": "/mount"
        },
        "gcsDataSink": {
          "bucketName": "SINK_NAME"
        },
        "transferOptions": {
          "deleteObjectsFromSourceAfterTransfer": false
        }
      }
    }
    

Refer to the [`transferJobs.create`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create) reference for details about additional supported fields.

## Clusters with multiple namenodes

Storage Transfer Service agents can only be configured with a single namenode. If your HDFS cluster is configured with multiple namenodes ("high availability"), and there's a failover event that results in a new primary namenode, you must re-install your agents with the correct namenode.

To delete the old agents, refer to [Delete an agent](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#delete_an_agent).

Your cluster's active namenode can be retrieved by running:
    
    
    hdfs haadmin -getAllServiceState
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
