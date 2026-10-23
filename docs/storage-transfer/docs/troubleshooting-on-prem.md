---
url: https://docs.cloud.google.com/storage-transfer/docs/troubleshooting-on-prem/
title: Troubleshoot file system transfers \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:06.350986+00:00
---

# Troubleshoot file system transfers  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/troubleshooting-on-prem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Troubleshoot file system transfers Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to troubleshoot and resolve transfer and agent issues, and where to find agent logs to help you troubleshoot issues.

## Errors

The following table describes transfer error messages, and how to resolve them:

Error message | Error type | What the error means | How to resolve the error  
---|---|---|---  
Modified during transfer | FILE_MODIFIED_FAILURE | The source file was modified during the transfer each time that Storage Transfer Service attempted to copy the source file.  | Prevent writes to the specified file during the next Storage Transfer Service operation.  
Failed to transfer | PRECONDITION_FAILURE | The Cloud Storage object associated with the source file was modified each time that Storage Transfer Service attempted to upload the file. | Prevent multiple transfer jobs from writing the same file to the same Cloud Storage bucket by using unique Cloud Storage object prefixes when you [create transfer jobs](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#create-transfer).   
Source directory not found | SOURCE_DIR_NOT_FOUND | Either the specified source path is incorrect, or the path is correct but not all agents have access to the path. | Check the transfer job configuration and verify that: 

  * The listed source path is correct
  * Each agent has [ access to the directory](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#restrict-directory-access)

  
Could not find the job's source or destination directory | ROOT_DIR_NOT_FOUND | Either the specified source/dest path is incorrect, or the path is correct but not all agents have access to the path. | Check the transfer job configuration and verify that: 

  * The listed source/dest path is correct
  * Relevant agents have [ access to the directory](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#restrict-directory-access)

  
File not found | FILE_NOT_FOUND_FAILURE | The source file was found, but deleted before it was transferred to Cloud Storage. | If the file was mistakenly deleted, restore it so that the next transfer job can upload it.  
Failed to find the destination bucket | BUCKET_NOT_FOUND | The destination bucket doesn't exist in Cloud Storage. | Verify that the destination bucket spelling is correct and that it exists.   
Failed to find an internal metadata object | METADATA_OBJECT_  
NOT_FOUND_FAILURE | Storage Transfer Service stores metadata in the destination bucket with the prefix `storage-transfer`. If the metadata files are deleted before their corresponding transfer operations complete, then this error is displayed.  | Avoid deleting objects with the prefix `storage-transfer/` in the destination bucket until after all transfer jobs complete.  
Failed due to invalid file name | INVALID_FILE_NAME | The path of a source file is invalid. | Verify and fix the specified file path. Verify that the path uses [ characters that are supported by Cloud Storage](https://docs.cloud.google.com/storage/docs/objects#naming).  
Failed due to invalid storage class | INVALID_FILE_STORAGE_CLASS | The storage class for the given source does not allow reads. | Find the documentation for your cloud provider to determine how to get the data into a storage class that allows copying the data out.  
Failed due to invalid resumable upload session URI | SESSION_URI_INVALID | The resumable upload ID or session URI is expired or cancelled. | The failure is being retried incorrectly. Please contact support.  
Failed due to invalid file size | INVALID_FILE_SIZE | The file size is invalid. | Verify file size is >= 0 and <= 5 TiB (max Cloud Storage object size) for transfers to Cloud Storage.  
Failed due to permissions | PERMISSION_FAILURE and UNAUTHENTICATED | A transfer agent didn't have sufficient permissions to perform an operation. There are two possibilities for this error: 

  * An agent had insufficient Google Cloud permissions.
  * An agent was unable to read a file or directory due to insufficient permissions on the source file system.

|  Verify the following:

  * [ Ensure that your agents have the following IAM roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#viewing-console): 
    * `storagetransfer.transferAgent`
    * `storage.admin` for all destination buckets
Either of these roles can be granted to a [service account](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#service-credentials) that is used by the agents, or a user with these roles can use their default credentials when [installing agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#install-agent). 
  * Ensure that all paths on the source file system are readable by each agent.

  
Object is subject to bucket's retention policy and cannot be deleted, overwritten or archived | PERMISSION_FAILURE |  The bucket has a retention policy in effect and the object already exists in the bucket. Storage Transfer Service cannot overwrite existing objects in the bucket. This error can be displayed if the file changed at the source, or if Storage Transfer Service attempts the upload twice due to network conditions and the first upload succeeded.  |  Verify that the data in your Cloud Storage bucket matches your expectations. You can confirm that the size and modified time (mtime) of the source files match their Cloud Storage object counterparts by re-running the job and confirming that there are no errors.   
Service lacked sufficient permissions | SERVICE_PERMISSION_FAILURE | Storage Transfer Service didn't have sufficient permissions to perform an operation. |  Storage Transfer Service uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), typically in the format of `project-PROJECT_NUMBER@storage-transfer-service.iam.gserviceaccount.com`, to access resources. To determine your specific `PROJECT_NUMBER`, use the [ `googleserviceaccounts.get`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get) API call. [ Verify that the service account has the following roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#viewing-console): 

  * `roles/storagetransfer.serviceAgent` for the project.
  * `roles/storage.admin` for all destination buckets.

  
Agent unsupported | AGENT_UNSUPPORTED_VERSION | The agent version is no longer compatible with Storage Transfer Service. | This is a temporary error, related to a bad agent update. If it occurs, do the following: 

  1. [ Stop all of your agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#stop-agent-cli).
  2. Pull the latest docker image by running: `sudo docker pull gcr.io/cloud-ingest/tsop-agent`
  3. Issue the Docker `run` command to start all of your agent containers.

If the issue persists, reach out to your support team.   
Failed due to hash mismatch | HASH_MISMATCH_FAILURE | Each time Storage Transfer Service tried to upload this file, the uploaded bytes were corrupted. This resulted in the hash of the on-premises file not matching the hash of the resulting Cloud Storage object. | This error may be caused by a number of potential issues. If you see a small percentage of hash mismatch failures (less than 1%) in a large transfer, retry the failed files. If you see a large percentage of hash mismatch failures (1% or greater), we recommend investigating potential memory, CPU, or other hardware failures on the agent machine.  
Failed due to an unsupported file mode | UNSUPPORTED_FILE_MODE | Storage Transfer Service encountered a file with an unsupported mode, such as a device, socket, named pipe, or irregular file. | Remove these special file types from the source directory.  
Failed due to an error in the file system | FILESYSTEM_ERROR | An agent encountered a file system or operating system error when performing a file system operation such as read, seek, or stat. | Read the failure description to understand which file system operation failed. Ensure the file system is accessible to the on-prem agent and responsive to basic file operations.  
Failed due to no space left on the file system | FILESYSTEM_NO_SPACE_ON_DEVICE | An agent ran out of space when performing a file system operation such as open or write. | Read the failure description to understand which file system operation failed. Ensure the file system has sufficient space to perform file operations.  
Failed due to an unknown error | UNKNOWN_FAILURE | An unexpected error occurred. | Read the failure description. If the failure description does not contain sufficient information to resolve the issue, please contact support.  
Failed due to an invalid specification | INVALID_SPEC | The agent received a corrupted internal specification. | Check for data corruption on agent hosts and contact support if you cannot find any.  
Failed due to an empty or invalid manifest file | CONFORMANCE_FAILURE | The agent cannot read or get valid CSV bytes due to invalid formatting or CSV entries. | Ensure that the manifest entries are valid file paths. If the failure description does not contain sufficient information to resolve the issue, please contact support.   
Falling back to resumable uploads instead of multipart uploads due to permission denied error | PERMISSION_FAILURE | [ Multipart uploads](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices#enable_multipart_uploads) have been enabled for this transfer, but the correct permissions have not been set on the bucket. | Refer to the **Multipart uploads** section of [ File system permissions](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions#multipart_uploads) for the required permissions.  
Entries listed out of order | INCOMPATIBLE_LIST_ORDER_FAILURE | The source file system returned a list of files in an order that is incompatible with Storage Transfer Service. Storage Transfer Service requires that the source file system return files in lexicographically sorted order. | Verify that the file system returns files in lexicographically sorted order.  
  
## Viewing agent logs

Agent logs contain information relevant to agent processes, and can help you troubleshoot agent connection problems. If your agents are listed as connected in Google Cloud console and you are experiencing transfer failures, see [Viewing errors](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#view-errors) to view a sample of transfer errors. To view logs that contain a record of every file Storage Transfer Service considered during a transfer, see [Viewing transfer logs](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#viewing-logs).

By default, agent logs are stored in `/tmp`. You can change the location with the `--log-dir=logs-directory` [command-line option](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-command-options).

The logs are named:

`agent.hostname.username.log.log-level.timestamp`

The log name components are as follows:

  * `hostname` \- hostname the agent is running on.
  * `username` \- username running the agent.
  * `log-level` is one of: 
    * **`INFO`** \- informational messages
    * **`ERROR`** \- errors encountered during transfer, but that don't prevent the transfer job from continuing.
    * **`FATAL`** \- errors encountered that prevent the transfer job from continuing.
  * `timestamp` \- timestamp in `YYYYMMDD-hhmmss.thread-id` format.



The logs directory contains symlinks to the most recent logs for each of the priority levels:

  * `agent.ERROR`
  * `agent.FATAL`
  * `agent.INFO`



## Slow transfer speed

If your data is taking a long time to transfer, check the following:

  1. The read throughput of your file system should be approximately 1.5 times your desired upload speed. You can use [FIO](https://fio.readthedocs.io/en/latest/fio_doc.html) to test the read throughput of your file system.

Install fio:
         
         sudo apt install -y fio
          

Create a new directory `fiotest`:
         
         TEST_DIR=/mnt/mnt_dir/fiotest
          sudo mkdir -p $TEST_DIR
          

Test read throughput:
         
         sudo fio --directory=$TEST_DIR --direct=1
             --rw=randread --randrepeat=0 --ioengine=libaio --bs=1M --iodepth=8
             --time_based=1 --runtime=180 --name=read_test --size=1G
          

After you run the commands above, Fio generates a report. The line labeled "bw" represents the total aggregate bandwidth of all threads, and it can be used as a proxy for read throughput.

  2. Use [iPerf3](https://iperf.fr/iperf-download.php) to check your available internet bandwidth to Storage Transfer Service.

  3. Make sure each of your transfer agents have at least 4 vCPU and 8GB of RAM.




If you've checked the conditions above and are still experiencing long transfer times, you can add additional agents to increase the number of concurrent connections to your data's file system.

For more information on how to maximize the performance of your transfer agents, see [Agent best practices](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices).

## Troubleshooting agent errors

The following sections describe how to troubleshoot and resolve transfer agent errors:

### Agents are not connected

If transfer agents are not displayed as connected within Google Cloud console:

  1. Verify that agents can connect to Cloud Storage APIs:

     1. Run the following command from the same machine as the transfer agent to test the agent's connection to Cloud Storage APIs:

`gcloud storage cp test.txt gs://my-bucket`

Replace:

`my-bucket` with the name of your Cloud Storage bucket.

  2. If your project uses VPC Service Controls, view the agent logs for errors. If VPC Service Controls is misconfigured, the `INFO` agent logs will contain the following error:

`Request is prohibited by organization's policy. vpcServiceControlsUniqueIdentifier: id`

In this output:

     * `id` is the [VPC Service Controls error's unique id](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#using_the_errors_unique_id)



### Agents are connected but jobs fail

If agents are displayed as connected but transfer jobs fail, check the [error details of the failed jobs](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#view-errors).

### Proxy rejects IP addresses

If you run behind a proxy like [Squid](https://www.squid-cache.org/) and you use an allowlist, you may see requests being denied because of IP addresses being used instead of hostnames.

To resolve this issue, use the [docker run command to run the agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#docker-run) and add the following flag:
    
    
    --transfer-service-endpoint=storagetransfer.googleapis.com:443
    

If you use an alternative endpoint to reach `googleapis.com` (e.g. for Private Service Connect), replace `googleapis.com` with the alternative endpoint.

### Agent is unable to connect to an HTTPS endpoint using a self-signed certificate

If your agent is unable to connect to an HTTPS endpoint using a self-signed certificate, use an extra `-v` option to mount your custom certificate bundle into the container's default location (`/etc/ssl/certs`).

To do this, modify the [`docker run` command](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#docker-run) by adding the following flag:
    
    
    -v PATH_TO_LOCAL_CERT:/etc/ssl/certs/ca-certificates.crt
    

Replace:

  * PATH_TO_LOCAL_CERT with the path to your custom certificate file.



### Agent fails to start: KDC did not respond appropriately to FAST negotiation

If when attempting to start the transfer agent for an HDFS transfer, the agent fails to start and returns an error similar to the following:

`Failed to start the agent, err = failed to create HDFS client: Couldn't find the hdfs client: no available namenodes: SASL handshake: [Root cause: KRBMessage_Handling_Error] KRBMessage_Handling_Error: AS Exchange Error: AS_REP is not valid or client password/keytab incorrect < KRBMessage_Handling_Error: KDC did not respond appropriately to FAST negotiation`

This error occurs when your Kerberos Key Distribution Center (KDC) does not support FAST negotiation, which the agent attempts to use by default for HDFS transfers.

To resolve this issue, prevent the agent from using FAST negotiation by adding the `--kerberos-disable-pa-fx-fast` flag when you start the agent.

This flag is only supported when running the agent using docker or podman. It is not supported when using the `gcloud transfer agents install` command.

Append the flag to your `docker run` or `podman run` command as follows:
    
    
    docker run --rm -v /usr/local/transfer_agent:/tmp/transfer_agent \
      gcr.io/cloud-ingest/tsop-agent:latest \
      --project-id=PROJECT_ID \
      --hostname=$(hostname) \
      --kerberos-disable-pa-fx-fast
    

See [Install and run transfer agents](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#install-agent) for more details about the docker and podman commands.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
