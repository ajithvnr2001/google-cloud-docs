---
url: https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details/
title: Advanced options \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:47.042943+00:00
---

# Advanced options  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Advanced options Stay organized with collections  Save and categorize content based on your preferences. 

This document describes advanced setup options for file system transfers, including:

  * Copying data on CIFS or SMB volumes
  * Using service account credentials
  * Adjusting maximum agent memory
  * Restricting agent directory access
  * Coordinating agents with Kubernetes
  * Using a Forward Proxy
  * Copying to a bucket with a retention policy
  * Options for obtaining more network bandwidth



### Copying data on CIFS or SMB volumes

Transfer agents aren't [directly supported on Windows servers](https://docs.cloud.google.com/storage-transfer/docs/known-limitations-transfer#supported-configurations). However, you can move data stored on any POSIX-compliant file system by mounting it on a Linux server or virtual machine (VM), and then running an agent from the Linux server or VM to copy your data to Cloud Storage.

To move data from a CIFS or SMB volume:

  1. Provision a Linux server or VM.

For supported operating systems, see [Prerequisites](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-jobs#prerequisites).

  2. Run the following command on the Linux server or VM you provisioned to mount the volume:
         
         sudo mount -t cifs -o
         username=WINDOWS-SHARE-USER,password=WINDOWS-SHARE-PASSWORD //IP-ADDRESS/SHARE-NAME /mnt
         

Replace the following:

     * `IP-ADDRESS`: the IP address of the Microsoft Windows server that the CIFS or SMB volume is located on.
     * `SHARE-NAME`: the share name you are mounting.
     * `WINDOWS-SHARE-USER`: an authorized user for accessing the CIFS or SMB volume.
     * `WINDOWS-SHARE-PASSWORD`: the password for the authorized user of the CIFS or SMB volume.
  3. Confirm that the CIFS volume is mounted by running the following command:
         
         findmnt -l
         

  4. Confirm that the user that will run the agent can list and copy files on the mounted volume by running the following commands:
         
         sudo -u USERNAME cp /mnt/FILE1 /mnt/FILE2
         

Replace the following:

     * `USERNAME`: the user that will run the agent.
     * `FILE1`: the file to copying from.
     * `FILE2`: filename to copy to.
  5. [Install the transfer agent](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#install-agent).




### Using service account credentials

You can use service account credentials to run the agent. Using service account credentials provides you a way to authenticate the transfer agent without relying on a single user account. For more information about account types, see [Principals](https://docs.cloud.google.com/docs/authentication#principals).

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  1. Create a service account key. For more information, see [Creating and managing service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).

  2. Pass the service key location to the agent creation command:
         
         gcloud transfer agents install --pool=POOL_NAME --count=NUM_AGENTS \
           --mount-directories=MOUNT_DIRECTORIES \
           --creds-file=RELATIVE_PATH_TO/KEY_FILE.JSON
         

The credential file is automatically mounted by `gcloud transfer` and does not need to be specified with the `--mount-directories` flag.




### Adjusting maximum agent memory

Transfer agents default to using a maximum of 8GiB of system memory. You can adjust the maximum memory used by the agents to fit your environment by passing `--max-physical-mem=MAXIMUM-MEMORY`, replacing `MAXIMUM-MEMORY` with a value that fits your environment. This flag is only supported by the [`docker run`](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents#docker) command.

The following are memory requirements for Transfer service for on-premises data agents: 

  * Minimum memory: 1GiB
  * Minimum memory to support high-performance uploads: 6GiB



We recommend the default of 8GiB.

The following table describes examples of acceptable formats for `MAXIMUM-MEMORY`:

`max-physical-mem` value | Maximum memory setting  
---|---  
`6g` | 6 gigabytes  
`6gb` | 6 gigabytes  
`6GiB` | 6 gibibytes  
  
### Restricting agent directory access

Users able to create transfer jobs can retrieve data from, and download data to, any file system directory that is accessible by the agent.

If agents are run as root and are given access to the entire file system, a malicious actor may be able to take over the host. It is strongly recommended that you restrict agent access to only necessary directories.

To restrict an agent's access to specific directories:

###  gcloud 

To specify directories that the agent can access on a file system, use the `--mount-directories` flag with `gcloud transfer agents install`:
    
    
    gcloud transfer agents install --pool=POOL_NAME --count=NUM_AGENTS \
      --mount-directories=MOUNT_DIRECTORIES
    

Specify multiple directories by separating each one with a comma and no space:
    
    
    gcloud transfer agents install --pool=POOL_NAME --count=NUM_AGENTS \
      --mount-directories=MOUNT_DIRECTORY_1,MOUNT_DIRECTORY_2
    

If you're specifying a credentials file using the `--creds-file` flag, `gcloud transfer` automatically mounts the credentials file. Other files in the same directory as the credentials file are not mounted.

###  `docker run`

To specify directories that the agent can access while performing a transfer, pass `-v HOST_DIRECTORY:CONTAINER_DIRECTORY` to the agent, and specify the following:

  * `HOST_DIRECTORY` is the directory on the host machine that you intend to copy from.
  * `CONTAINER_DIRECTORY` is the directory mapped within the agent container.



`HOST_DIRECTORY` and `CONTAINER_DIRECTORY` must be the same so that the agent can locate files to copy.

When using this option:

  * Do not specify `--enable-mount-directory`.
  * Do not preface your file path with `/transfer_root`.



The `--enable-mount-directory` option mounts the entire file system under the `/transfer_root` directory on the container. If `--enable-mount-directory` is specified, directory restrictions are not applied.

You can use more than one `-v` flag to specify additional directories to copy from. For example:
    
    
    sudo docker run --ulimit memlock=64000000 -d -rm --volumes-from gcloud-config \
    -v /usr/local/research:/usr/local/research \
    -v /usr/local/billing:/usr/local/billing \
    -v /tmp:/tmp \
    gcr.io/cloud-ingest/tsop-agent:latest \
    --project-id=PROJECT_ID \
    --hostname=$(hostname) \
    --agent-id-prefix=ID_PREFIX
    

If you are using a service account, ensure that you mount the credentials file into the container and pass the `--creds-file=CREDENTIAL_FILE`. For example:
    
    
    sudo docker run --ulimit memlock=64000000 -d -rm \
    -v HOST_DIRECTORY:CONTAINER_DIRECTORY \
    -v /tmp:/tmp \
    -v FULL_CREDENTIAL_FILE_PATH:FULL_CREDENTIAL_FILE_PATH \
    gcr.io/cloud-ingest/tsop-agent:latest \
    --project-id=PROJECT_ID \
    --creds-file=CREDENTIAL_FILE \
    --hostname=$(hostname) \
    --agent-id-prefix=ID_PREFIX
    

Replace the following:

  * `HOST_DIRECTORY`: the directory on the host machine that you intend to copy from.
  * `CONTAINER_DIRECTORY`: the directory mapped within the agent container.
  * `FULL_CREDENTIAL_FILE_PATH`: the fully-qualified path to the credentials file.
  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that is hosting the transfer resources are created and billed.
  * `CREDENTIAL_FILE`: a JSON-formatted service account credential file. For more information about generating a service account credential file, see [creating and managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
  * `ID_PREFIX`: the prefix that is prepended to the agent ID to help identify the agent or its machine in the Google Cloud console. When a prefix is used, the agent ID is formatted as `prefix + hostname + Docker container ID`.



### Coordinating agents with Kubernetes

Docker is a [supported container runtime for Kubernetes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#docker). You can use Kubernetes to orchestrate starting and stopping many agents simultaneously. From Kubernetes perspective, the agent container is considered a stateless application, so you can follow [Kubernetes instructions for deploying a stateless application](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#docker).

### Using private API endpoints in Cloud Interconnect

To use private API endpoints in Cloud Interconnect:

  1. Log into the on-premises host that you intend to run the agent.

  2. Configure Private Google Access. For more information, see [Configuring Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid).

  3. Confirm that you can connect to Cloud Storage APIs:

     1. For Cloud Storage APIs, run the following command from the same machine as the transfer agent to test moving a file into your Cloud Storage bucket: `gcloud storage cp test.txt gs://MY-BUCKET` where `MY-BUCKET` is the name of your Cloud Storage bucket. If the transfer works, the test is successful. 



### Using a forward proxy

Transfer agents support using a forward proxy on your network by passing the `HTTPS_PROXY` environment variable.

For example:
    
    
    sudo docker run -d --ulimit memlock=64000000 --rm \
    --volumes-from gcloud-config \
    -v /usr/local/research:/usr/local/research \
    --env HTTPS_PROXY=PROXY\
    gcr.io/cloud-ingest/tsop-agent:latest \
    --enable-mount-directory \
    --project-id=PROJECT_ID \
    --hostname=$(hostname) \
    --agent-id-prefix=ID_PREFIX
    

Replace the following:

  * `PROXY`: the HTTP URL and port of the proxy server. Ensure that you specify the HTTP URL, and not an HTTPS URL, to avoid double-wrapping requests in TLS encryption. Double-wrapped requests prevent the proxy server from sending valid outbound requests.
  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that is hosting the transfer resources are created and billed.
  * `ID_PREFIX`: the prefix that is prepended to the agent ID to help identify the agent or its machine in the Google Cloud console. When a prefix is used, the agent ID is formatted as `prefix + hostname + Docker container ID`.



## Copy to a bucket with a retention policy

To transfer to a bucket with a retention policy, we recommend the following process:

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) within the same region as the final bucket. Ensure that this temporary bucket does not have a retention policy.

For more information about regions, see [Bucket locations](https://docs.cloud.google.com/storage/docs/locations).

  2. Use Storage Transfer Service to transfer your data to the temporary bucket you created without a retention policy.

  3. Perform a [bucket-to-bucket transfer](https://docs.cloud.google.com/storage/docs/moving-buckets) to transfer the data to the bucket with a retention policy.

  4. [Delete the Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) that you created to temporarily store your data.




## Options for obtaining more network bandwidth

There are several options for obtaining more network bandwidth for file system transfers. Increasing your network bandwidth will help decrease transfer times, especially for large data sets.

  * **Peering with Google** —Peering is where you directly interconnect with Google to support traffic exchange. We have [direct peering locations](https://docs.cloud.google.com/vpc/docs/edge-locations) world-wide. To learn about the benefits and our policies, see [Peering](https://peering.google.com/#/options/peering).

  * **Cloud Interconnect** —Cloud Interconnect is similar to peering, but you'll use an interconnect to connect to Google. There are two types of [interconnects to choose from](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect):

    * **Dedicated Interconnect** — You connect directly from your data center to a Google data center via a private, dedicated connection. For more information, see [Dedicated Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview).

    * **Partner Interconnect** —You work with a service provider to establish a connection to a Google data center via a service partner's network. For more information, see [Partner Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview).

  * **Obtain bandwidth from your ISP** —Your internet service provider (ISP) may be able to offer more bandwidth for your needs. Consider contacting them to ask what options they have available.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
