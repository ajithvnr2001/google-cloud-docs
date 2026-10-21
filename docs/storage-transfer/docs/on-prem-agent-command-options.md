---
url: https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-command-options/
title: Transfer agent command-line options \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:42.872242+00:00
---

# Transfer agent command-line options  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-command-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/storage-transfer/docs/apis)



Send feedback 

#  Transfer agent command-line options Stay organized with collections  Save and categorize content based on your preferences. 

Transfer agents transfer data from your file system to Google Cloud. You can control agent options when you run an agent through the flags and options described in this page.

## Command summary
    
    
    sudo docker run [--ulimit memlock=64000000 -d --rm -v host-directory:container-directory]
    --env environment-variable=variable-value
    gcr.io/cloud-ingest/tsop-agent:latest
    {--help | --version | --project-id=project-id}
    [--agent-id-prefix=id-prefix --creds-file=credential-file
    --enable_mount_directory --hostname=hostname
    --kerberos-disable-pa-fx-fast
    --log-dir=logs-directory
    --max-physical-mem=maximum-memory]
    

## Docker options

`--ulimit memlock=64000000`
    Locks shared memory for a shared pool for Docker, so that it is always in memory for access by multiple sessions.
`-d`
    

Starts the Docker container in detached mode, or in the background. This allows you to continue issuing commands from the Linux terminal.

For more information, see [Detached -d](https://docs.docker.com/engine/reference/run/#detached--d)

`--rm`
    

Deletes the container and the container's file system when Docker exits.

For more information, see [Clean up (--rm)](https://docs.docker.com/engine/reference/run/#clean-up---rm)

`-v host-directory:container-directory`
    

Specifies one or more [volumes](https://docs.docker.com/storage/volumes/) to map from the host to the container. When using `-v`, we require the `host-directory` and `container-directory` to be the same, otherwise Storage Transfer Service won't successfully locate your files for transfer.

For more information, see [VOLUME (shared file systems)](https://docs.docker.com/engine/reference/run/#volume-shared-filesystems)

`--env environment-variable=variable-value`
    

Specifies an environment variable for the Docker container. Use this flag to configure your agents to use a forward proxy. For more information, see [Using a forward proxy](https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details#using-forward-proxy).

## Agent options

`--agent-id-prefix=id-prefix`
    An optional prefix that is prepended to the agent ID to help identify the agent or its machine in the Google Cloud console. When a prefix is used, the agent ID is formatted as `prefix + hostname + Docker container ID`.
`--creds-file=credential-file`
    

An optional JSON-formatted service account credential file. For more information about generating a service account credential file, see [creating and managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).

**Note:** Unless you are using `--enable_mount_directory`, you must prefix this path with `/transfer_root`, for example `/transfer_root/path/to/cred_file.json`.
`--enable_mount_directory`
    

Optionally mounts the whole file system under the directory `/transfer_root` within the Docker container, rather than specifying individual [Docker `-v`volume mounts](https://docs.docker.com/storage/volumes/). When using this flag, you don't need to prefix `/transfer_root` to the log directory or the service account credentials file path, and `/transfer_root` isn't visible in transfer logs or GUI error samples.

`--help`
    

Displays brief usage help.

`--hostname=hostname`
    

set the hostname that the agent is running on. Used to report the hostname of the machine a particular agent is running on.

**Note:** We recommend passing `--hostname=$(hostname)` when using this flag.
`--kerberos-disable-pa-fx-fast`
    

Prevents agents from using FAST negotiation with Kerberos for HDFS transfers. Use this flag if your Kerberos Key Distribution Center (KDC) doesn't support FAST negotiation.

`--log-dir=logs-directory`
    

An optional directory that the agent writes logs to. The default directory is `/tmp/`.

**Note:** Unless you are using `--enable_mount_directory`, you must prefix this path with `/transfer_root`, for example, `/transfer/root/path/to/log_file`.
`--max-physical-mem=maximum-memory`
    

Agents default to using an 8GiB buffer pool. If the default doesn't fit your environment, you can specify a relevant maximum memory usage in the following formats:

`max-physical-mem` value | Maximum memory setting  
---|---  
`6g` | 6 gigabytes  
`6gb` | 6 gigabytes  
`6GiB` | 6 gibibytes  
**Note:** This flag does not limit total container memory. Set this to 50-60% of total container RAM to avoid OOMs.
`--project-id=project-id`
    

Required string of the project ID that is hosting the transfer resources that are created and billed.

`--version`
    

Displays the current version of the agent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
