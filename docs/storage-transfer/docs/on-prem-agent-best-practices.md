---
url: https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices/
title: Best practices for file system transfers \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:45.974046+00:00
---

# Best practices for file system transfers  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/on-prem-agent-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Best practices for file system transfers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for file system transfers.

## Performance best practices

The following are best practices for ensuring good transfer performance:

  * Maximize your transfer agent performance.

  * Benchmark your performance by transferring a large data corpus, typically at least 100 GB in size.

Storage Transfer Service is a large-scale, throughput-optimized service, so your performance on very small test data sets is not indicative of your performance on large data sets in production.

  * Limit individual source folders to 1 million files. Directories containing millions of files can slow down the entire transfer.

  * Run agents in separate virtual machines (VMs) so that you can scale your resource consumption more effectively.

  * Verify that the network interface on the agent machines is sized for the read/write bandwidth you need.

For example, if you intend to fully utilize a 20 Gbps wide-area network (WAN), your agent machine's network interface must support 20 Gbps to read data from your networked file system, and another 20 Gbps to transfer data to Cloud Storage, or 40 Gbps of total bandwidth.

  * Monitor the CPU, memory, and network on agent machines to ensure that the machines aren't overwhelmed by other workloads, as this can negatively affect performance. Refer to the [agent hardware requirements](https://docs.cloud.google.com/storage-transfer/docs/on-prem-set-up#requirements) for suggested memory and CPU figures.




## Multipart uploads

If your transfer is from a POSIX file system to Cloud Storage, or between POSIX file systems, consider enabling [multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads). Multipart uploads can speed up transfers that include large files by up to 300% by breaking large files (>1 GiB) into smaller parts and uploading those parts in parallel.

HDFS and S3-compatible file systems do not support multipart uploads.

### Enable multipart uploads

To enable multipart uploads:

  * You must [grant the required permissions](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions#multipart_uploads) to the account authorizing transfer agents, either a user account or a service account.

  * The destination or intermediate bucket must not have a retention policy or object hold.




Once enabled, Storage Transfer Service uses multipart uploading automatically when doing so is likely to speed up a transfer.

### Configure multipart object lifecycle rules

You can use Cloud Storage Object Lifecycle Management to abort an incomplete multipart upload and delete the associated parts. See [Abort incomplete multipart uploads](https://docs.cloud.google.com/storage/docs/lifecycle#abort-mpu) in the Cloud Storage documentation.

We recommend setting an `age` value of 7 days.

### Disable multipart uploads

To disable multipart uploads, reinstall the transfer agents using `docker run` and pass `--enable-multipart=false`:
    
    
    sudo docker run --ulimit memlock=64000000 -d --rm \
    -v /usr/local/research:/usr/local/research \
    gcr.io/cloud-ingest/tsop-agent:latest \
    --project-id=PROJECT_ID \
    --agent-pool=AGENT_POOL \
    --creds-file=CREDENTIAL_FILE \
    --hostname=$(hostname) \
    --enable-multipart=false
    

Replace the following:

  * `PROJECT_ID` specifies the project ID that is hosting the transfer.
  * `CREDENTIAL_FILE`: if the transfer agent is using a service account for authentication, specify the path to a JSON-formatted service account credential file.



Alternatively, [revoke the required permissions](https://docs.cloud.google.com/storage-transfer/docs/file-system-permissions#multipart_uploads) from the account authorizing transfer agents, either a user account or a service account.

## Maximize transfer agent performance

Your transfer performance is affected by the following variables:

  * File system capabilities.

  * Underlying hardware limitations.

The hard drive media type, input/output bus, and local area network (LAN) connectivity all affect performance.

  * WAN throughput and utilization.

A slower or highly utilized WAN slows performance.

  * File characteristics.

For example, many large files have a higher network throughput than many small files due to networking overhead.




Because of these variables, we can't predict actual performance or provide an optimal number of agents to use.

At a minimum, we recommend that you use three agents, across different machines if possible, so that your transfer remains fault-tolerant. You can add transfer agents while transfers are running, as performance dynamically increases.

To observe the impact of adding agents, and to choose the number of agents that works best for your environment, do the following:

  1. Start a large transfer that takes at least 1 hour to run. For example, start a transfer that contains at least 100k files and is at least 100 GB in total size.

  2. Use [Cloud Monitoring to observe the overall agent throughput](https://cloud.google.com/storage-transfer/docs/managing-on-prem-agents#monitor-agent-stackdriver).

  3. Wait for the throughput to level off, and determine if you are limited by your WAN capacity or your bandwidth cap.

  4. If you haven't saturated your WAN capacity, and you haven't reached your desired transfer limit, add another agent. The additional agent automatically increases transfer throughput. Wait approximately 3 minutes to throughput stabilize in Cloud Monitoring.




Repeat steps 3 and 4, adding one agent at a time until you reach your desired limit. As long as computational, file system, and network resources are available, you can run up to 100 agents concurrently per agent pool.

If you saturate your outbound bandwidth before you reach your desired limit, you can do any of the following:

  * [Control the bandwidth used by Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/obtaining-bandwidth-on-prem).
  * [Obtain more network bandwidth](https://docs.cloud.google.com/storage-transfer/docs/obtaining-bandwidth-on-prem#moar_bandwidth).



If you've added agents, but the throughput isn't increasing and your WAN isn't saturated, [investigate the file system throughput](https://docs.cloud.google.com/storage-transfer/docs/troubleshooting-on-prem#slow-transfer-speed). In rare cases the file system throughput is saturated, hampering your ability to increase your transfer performance.

## Naming agents

When naming agents, we recommend that you do the following:

  * Always include the hostname in your agent. This helps you find the machine an agent is running on. We recommend that you pass `--hostname=$(hostname)` to the Docker `run` command.

  * Choose an agent prefix scheme that helps you identify agents in the context of your monitoring and infrastructure organization. For example:

    * If you have three separate transfer projects, you may want to include the team name in your agent. For example, `logistics`.

    * If you are running two different transfer projects for two different data centers, you may want to include the data center name in the agent prefix. For example, `omaha`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
