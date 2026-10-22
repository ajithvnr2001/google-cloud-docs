---
url: https://docs.cloud.google.com/memorystore/docs/redis/troubleshoot-issues/
title: Troubleshoot issues \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:00.167443+00:00
---

# Troubleshoot issues  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/troubleshoot-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Troubleshoot issues Stay organized with collections  Save and categorize content based on your preferences. 

This page explains various issues, the error messages for these issues, and troubleshooting steps to resolve the issues.

## Connectivity issues

If your Memorystore for Redis instance experiences connectivity issues, then check the issues in this section to see if one of them causes the problem.

If an issue in this section doesn't match your issue, then Telnet to one of your Redis nodes and [run some Redis commands](https://docs.cloud.google.com/memorystore/docs/redis/create-instance-gcloud#connecting-compute-engine) to see if the instance responds.

If the node is unresponsive, then see if any of the networking issues are the reason why your node's network connection is blocked. If none of these issues resolves the problem, then contact [Cloud Customer Care](https://docs.cloud.google.com/support).

### You provision resources in different VPC networks.

To connect to a Memorystore for Redis instance from a Google Cloud resource, such as a Compute Engine VM, you must provision the resources on the same authorized VPC network as the instance.

Attempting to Telnet to an instance from a resource that's in a different region or VPC network results in the following error message:

`telnet: Unable to connect to remote host: Connection timed out`

### You delete a VPC network peering.

When you create a Memorystore for Redis instance, you create a VPC peering between your VPC network and an internal Google VPC network.

The network peering uses the following format:

`redis-peer-############`

If this network peering is deleted, then attempting to Telnet to the instance results in the following error message:

`telnet: Unable to connect to remote host: Connection timed out`

To re-establish the deleted network peering, create another instance. Then, delete this instance. Your original instance now has the network peering that it needs.

### You create firewall rules that block your instance's IP addresses.

If you create egress firewall rules that block either the port (6379) or IP address of your Memorystore for Redis instance, then you might experience connectivity issues. Don't create network firewall rules that block the IP address range of your instance.

### You have unresponsive connections

We strongly recommend configuring your client application to detect unresponsive connections to Memorystore for Redis. When an unresponsive connection is detected, the client must reset it. To build a resilient application, we recommend the following client configurations:

  * **Configure TCP keep-alive parameters** : set the `TCP keepalive time`, `TCP keepalive interval`, and `TCP keepalive probes` parameters so that clients detect and drop unresponsive connections proactively, even when connections are idle. For example, if you set the `TCP keepalive time` parameter to 30 seconds, `TCP keepalive interval` to 10 seconds, and `TCP keepalive probes` to 3, then clients reset unresponsive idle connections within a minute.
  * **Configure TCP user timeouts** : set this timeout in your clients to reset connections that have outstanding requests and stop responding. For example, if you set the timeout to 15 seconds, then clients reset unresponsive connections that have outstanding requests after 15 seconds.



## CPU usage issues

This section explains CPU usage issues that your Memorystore for Redis instance might encounter.

### Your instance experiences high latency or doesn't respond.

If your Memorystore for Redis instance experiences high latency or unresponsiveness, then these issues might be caused by using the following resource-intensive Redis commands:

  * [KEYS](https://redis.io/commands/keys)
  * [LRANGE](https://redis.io/commands/lrange)
  * [EVAL](https://redis.io/commands/eval)
  * [HGETALL](https://redis.io/commands/hgetall)
  * [ZRANGE](https://redis.io/commands/zrange)



These commands can put heavy CPU pressure on your instance. We recommend that you don't run the `KEYS` command in production environments. Instead, use `SCAN` because this command uses fewer resources than `KEYS`.

Using `LRANGE` to query all or a large subset of your keyspace can demand high CPU resources. To resolve this, we recommend that you reduce the number of keys in the keyset that you query in a single operation.

Using a complex Lua script with `EVAL` can also cause high CPU usage. We recommend that you use less-complex Lua scripts.

`HGETALL` and `ZRANGE` can return a large number of keys, adversely affecting the performance of your server. Instead of `HGETALL`, we recommend that you run the `HSCAN` command. Also, before using `ZRANGE`, we recommend that you limit the size of the range that you use for a query.

Before you run a resource-intensive command, check the size of the data structures that the command queries to ensure that it doesn't cause latency.

If your instance experiences high latency or unresponsiveness, then do the following:

  1. Check your client-side logs to find if any resource-intensive commands ran. If so, then note the date and time.
  2. [Use Cloud Monitoring](https://docs.cloud.google.com/memorystore/docs/redis/monitoring-instances) to view the `redis.googleapis.com/stats/cpu_utilization` metric. See if periods of high CPU utilization coincide with the same periods when the resource-intensive commands ran.



### The output buffer of your instance runs out of space.

If the output buffer of your Memorystore for Redis instance runs out of space, then do the following:

  * Set a smaller value for the [`maxmemory-gb`](https://docs.cloud.google.com/memorystore/docs/redis/supported-redis-configurations#modifiable_configuration_parameters) parameter.
  * Use the [`allkeys-lru`](https://docs.cloud.google.com/memorystore/docs/redis/supported-redis-configurations#maxmemory_policies) `maxmemory` policy.



When the memory of your instance is full, and a new write comes in, Memorystore for Redis evicts keys to make room for the write, based on your instance's `maxmemory` policy. The `allkeys-lru` policy evicts the least recently used (LRU) keys from the entire keyset.

We recommend that you monitor your instance's `maxmemory` and used memory. This helps you to know if your instance reaches the provisioned instance capacity. Also, by reducing the value for the `maxmemory-gb` parameter, you get more space for the overhead.

### External metrics are missing for your instance

If your instance either experiences high CPU utilization or the instance's resources become exhausted (for example, by having too many connections), then the instance might misbehave and external metrics might be missing.

### Isolate the source of your instance's latency

To determine whether the latency that you experience originates from your instance, your client application, or your network environment, use the `redis-cli` tool to run a continuous latency test.

To isolate the source of your instance's latency, do the following:

  1. Connect to a Compute Engine VM that's located in the same region and VPC network as your instance.

  2. If it's not already installed, then install the `redis-cli` tool on your VM.

     * For Debian or Ubuntu-based VMs, run the following command:
           
           sudo apt-get install redis-tools
           

     * For RHEL or CentOS-based VMs, run the following command:
           
           sudo yum install redis
           

  3. To measure the instance's latency in milliseconds, run the following command:
         
         redis-cli --latency -h IP_ADDRESS -p PORT
         

If your instance has Redis AUTH or in-transit encryption enabled, then ensure that you append the required authentication (`-a`) or TLS (`--tls`) flags.

Make the following replacements:

     * IP_ADDRESS: your instance's IP address.
     * PORT: the port number that's reserved for your instance. Typically, this port number is 6379.
  4. Let the command run for a few minutes. The tool continuously pings the server and calculates the minimum, maximum, and average latency values.

  5. To stop the command and view the results, press `Ctrl+C`.




If the command outputs a consistently low average latency (typically 1 millisecond or less), then the instance is healthy and responding quickly.

If the command shows consistently low latency, but your client application still experiences delays, then the following issues might cause the latency:

  * **Network** : Traffic routed across different regions or zones between your client and the instance might introduce significant network delays.
  * **Client** : High CPU or memory utilization on the client, exhausted connection pools, or application logic bottlenecks might increase the total round-trip time that the client experiences.



## Networking issues

This section explains networking issues that your instance might encounter.

### You exhaust the allocated IP range or a conflicting route exists.

When you create resources within the IP address range dedicated for Memorystore for Redis, you might exhaust all of the IP addresses. Or, there might be a [route that conflicts](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) with the IP address of the Memorystore for Redis instance that you're trying to create.

These issues cause the following error message to appear:

`The IP ranges for the connection do not have enough available IPs. Allocate a new range or expand existing range and try again.`

To resolve this issue, allocate additional IP addresses or remove the route conflict discrepancy. For more information, see [IP address range exhaustion](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modify-ip-range).

### You don't have a private services access connection established for your network.

If your Memorystore for Redis instance uses the [private services access connection mode](https://docs.cloud.google.com/memorystore/docs/redis/networking#private_services_access), but a [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) connection doesn't exist for your network, then you might receive the following error message:

`Google private service access is not enabled. Enable private service access and try again`

To resolve this issue, [establish a private services access connection](https://docs.cloud.google.com/memorystore/docs/redis/establishing-connection).

### You delete the network peering for the private services access connection.

When you establish a [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) connection, Memorystore for Redis creates a network peering connection called `servicenetworking-googleapis-com`. This connection appears in your project's [VPC network peering](https://console.cloud.google.com/networking/vpc-connectivity/peering) page.

If you delete the network peering, then the following error message appears for existing instances:

`telnet: Unable to connect to remote host: Connection timed out`

In addition, if you delete the network peering and you [create an instance](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances), then the following error message appears:

`Private services access is not configured correctly. For steps on how to verify the connection, check the documentation.`

To resolve this issue, [create a private service access connection](https://docs.cloud.google.com/memorystore/docs/redis/establish-connection#gcloud) between your network and the private services access network by running the following command:
    
    
    gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com --ranges=RESERVED_RANGE_NAME --network=VPC_NETWORK --project=PROJECT_ID
    

### You use conflicting parameters.

If you use both the `--reserved-ip-range` parameter and the `--connect-mode=private-service-access` parameter, then you receive the following error message:

`Reserved IP range is not supported for --connect-mode private services access`

You can't use both parameters at the same time because Memorystore for Redis doesn't support the `--reserved-ip-range` parameter for the private services access connection mode.

To resolve this issue, do one of the following:

  * Use the `--reserved-ip-range` parameter with the `--connect-mode=direct-peering` parameter.
  * Don't use the `--reserved-ip-range` parameter.



### You exceed the subnetwork quota for your project.

There's a limit to the number of subnetworks that you can create within your Google Cloud project. If you exceed this quota, then you receive one of the following error messages:

`Internal network quota exceeded. Please request higher limit here: https://forms.gle/ZfVduUGq2iSYcYGm8`

or

`Unable to create instance. Network quota limit has been reached. Please request higher limit here: https://forms.gle/ZfVduUGq2iSYcYGm8`

To resolve this issue, either fill out the form that appears in the error messages or contact [Cloud Customer Care](https://docs.cloud.google.com/support).

### You don't attach your service project to your host project.

If you use [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) and you don't attach your service project to your host project, then you receive the following error message:

`Invalid network name <network-name>. Project <project-name> referenced is not the host project for <service-project-name>.`

To resolve this issue, [attach your service project to your host project](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared).

### You create an instance in a service project with the direct peering connection mode and designate a Shared VPC network.

If you create a Memorystore for Redis instance in a [service project](https://docs.cloud.google.com/vpc/docs/shared-vpc) and you designate a Shared VPC network from the host project for the instance, then you can't use the [direct peering](https://docs.cloud.google.com/memorystore/docs/redis/networking#connection_modes) connection mode.

By default, the connection mode is set to direct peering. If you attempt to use this connection mode when you create an instance, and you also choose a Shared VPC network from the host project as the value for the `--network` parameter, then you receive the following error message:

`Authorized_network must exist in the same project as redis instance`

To resolve this issue, do one of the following:

  * When you create your instance, use the private services access connection mode  
(`--connect-mode=private-service-access`).
  * Choose an authorized VPC network that's in the same project as your instance.



### You use an IP address range for Compute Engine that Memorystore for Redis can't access.

You can't access your Memorystore for Redis instance from a Compute Engine VM that has an IP address in the `172.17.0.0/16` range. This range is reserved for an internal component.

To resolve this issue, access your instance from a Compute Engine VM that has an IP address in a different range.

## Issues connecting to your instance from other Google Cloud resources

This section explains issues that your Memorystore for Redis instance might encounter when other resources attempt to connect to it.

### You can't connect to your instance from serverless environments that require a Serverless VPC Access connector

If you can't connect to your Memorystore for Redis instance by using one of the [serverless environments that require a Serverless VPC Access connector](https://docs.cloud.google.com/memorystore/docs/redis/supported-environments#serverless-environments-that-need-a-serverless-vpc-access-connector), then verify whether you set up this connector for your environment. For more information, see [Serverless VPC Access connector requirement](https://docs.cloud.google.com/memorystore/docs/redis/supported-environments#serverless-vpc-access-connector-requirement).

### You can't connect to your instance from a Google Kubernetes Engine (GKE) cluster

To connect to your Memorystore for Redis instance from a GKE cluster, you must enable VPC-native/IP aliasing on the cluster.

It's easiest to enable VPC-native/IP aliasing when you create the cluster. In the advanced options section, select **VPC Native**. For more information, see [Create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).

## Identity and Access Management (IAM) issues

This section explains IAM issues that your Memorystore for Redis instance might encounter.

### You want to restore a deleted policy binding for a service account

Memorystore for Redis uses the following service accounts to manage your instances:
    
    
    service-PROJECT_NUMBER@service-networking.iam.gserviceaccount.com
    
    service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com
    

If you delete the policy bindings for these service accounts, then you can't create instances.

If you attempt to create a Memorystore for Redis instance by using the Google Cloud CLI, then you might receive the following error message:

` (gcloud.redis.instances.create) FAILED_PRECONDITION: A required IAM policy might be missing. Please run this command:"gcloud projects add-iam-policy-binding YOUR_PROJECT_ID --member='serviceAccount:service-YOUR_PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com' --role='roles/redis.serviceAgent'" and try again. `

To re-establish the policy binding for the `service-networking` service account, run the following command. Replace VARIABLES with appropriate values.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member='serviceAccount:service-PROJECT_NUMBER@service-networking.iam.gserviceaccount.com' --role='roles/servicenetworking.serviceAgent'
    

To re-establish the policy binding for the `cloud-redis` service account, run the following command. Replace VARIABLES with appropriate values.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member='serviceAccount:service-PROJECT_NUMBER@cloud-redis.iam.gserviceaccount.com' --role='roles/redis.serviceAgent'
    

## Operation timeout issues

The following issues result in an unresponsive Redis instance and/or instance/node operation timeouts.

### Network partition issues

Sometimes Google Cloud resources cannot communicate across zones within a region due to a network partition error in Google Cloud servers. This can cause your instance to lose connection, resulting in a timeout error.

After Google Cloud resolves the network partition error for the region or zone where your instance is provisioned, connectivity should resume normally.

In this issue, you may see a connectivity error message such as the following:

`telnet: Unable to connect to remote host: Connection timed out`

If you are not able to identify the cause of the timeout error, reach out to [Google Cloud Support](https://docs.cloud.google.com/support).

### Service project and host project not in the same VPC service control perimeter

If you are using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) and a [VPC service control](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter, and your Redis instance creation operation times out, this may indicate that your service project and host project are not in the same service perimeter. Your service project and host project must be in the same perimeter in order for your Redis instance to communicate with connecting clients over the Shared VPC network.

To see if you are experiencing this issue, [check your Redis instance's audit logs](https://docs.cloud.google.com/memorystore/docs/redis/audit-logging) for the following error:

`violationReason: "NETWORK_NOT_IN_SAME_SERVICE_PERIMETER"`

To resolve this issue, put your host network and your service network in the same service perimeter.

## Troubleshooting import and export issues

This section outlines some common issues you may run into when using import and export for Memorystore for Redis.

### Import and export buttons are disabled in the Google Cloud console

Issue: the user logged into the console does not have the `redis.instances.import` and/or `redis.instances.export` permissions required to import and/or export RDB files.

Solution: [grant the permissions](https://docs.cloud.google.com/memorystore/docs/redis/import-export-restricted-permissions) to the user, and refresh the instance details page.

### The import operation completed but the data was not restored

If an import operation completes but the data is not restored, first check either the Google Cloud console or the command line for an error message, and resolve any issues described by the error message.

If there is a failure during the import process, the instance is recovered using an empty RDB file. You can attempt to restore the data by importing the same RDB file again, or using a different RDB file.

### The import failed because the RDB file was too big

If you received the error message "Import RDB file gs://bucket/object.rdb size exceeds max memory 10GB", you should scale up your instance and retry the import. You can also try to import a smaller RDB file into your instance.

## Troubleshooting Google Cloud CLI issues

If you run into an issue where a gcloud CLI command is unavailable, or if the command behaves differently from how it is documented, try updating the gcloud CLI:
    
    
    gcloud components update
    

## Stopping all ongoing commands and connections for a Redis instance

As Memorystore for Redis is a Google managed product, there are some commands that are [blocked in your Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/supported-commands#blocked-commands) in order to provide a safe and reliable environment. One of the restricted commands is `CLIENT`, which includes `CLIENT KILL`, used to stop commands.

If a Redis command is consuming a lot of CPU/RAM utilisation and is affecting your production environment, you need to restart the instance (for **Basic Tier** configurations), or to failover into a replica (for **Standard Tier** configurations). This restart/failover operation stops all the commands running on the Redis server, and ends all the ongoing connections.

Below you'll find commands to perform restarts or failovers for each Memorystore for Redis configuration.

### Stopping commands in Standard tier Memorystore for Redis instances
    
    
    gcloud redis instances failover INSTANCE_NAME --data-protection-mode=limited-data-loss

**Warning:** Any failover from the primary to the replica risks some data loss. The `limited-data-loss` mode keeps data loss to a minimum by verifying that the difference in synchronization between your primary and replica is below 30MB before initiating the failover. See [manual failover](https://docs.cloud.google.com/memorystore/docs/redis/manual-failover-overview) for additional information.

### Stopping commands in Basic tier Memorystore for Redis instances

The only way to perform a restart in a Memorystore for Redis instances is changing its configuration, like scaling up the instance. An example of a command that you can run to restart your instance can be found below.
    
    
    gcloud redis instances update INSTANCE_NAME --region REGION_ID --size NUMBER_GB

After you scale your instance to a different size, you can run another scaling operation to return it to the original size.

## Organization policy issues with domain restricted sharing

There's a known issue where the `iam.allowedPolicyMemberDomains` organization policy causes errors when it's used with Memorystore for Redis instances that use the `PROJECT_NUMBER-compute@developer.gserviceaccount.com` service account format.

Depending on when your instance was created, Memorystore for Redis uses one of two different service account formats. To identify your instance's service account format, see [Memorystore for Redis service account format](https://docs.cloud.google.com/memorystore/docs/redis/access-control#memorystore_for_redis_service_account_format).

When this issue occurs, you might encounter the following error message: `One or more users named in the policy do not belong to a permitted customer.`

Depending on your organization's policy and whether you can recreate your instance, you can resolve this error using one of the following options:

  1. **Recreate your instance** : older instances use the `PROJECT_NUMBER-compute@developer.gserviceaccount.com` service account format, which domain restricted sharing policies often block. Newly created instances use a modern service account format that's compatible with most organization policies.

If your organization policy blocks all external domains, then this option doesn't work. To bypass the policy, you must use the second option.

  2. **Force account access** : if you can't recreate your instance to get the new service account format, or if your organization's policy blocks the new service account domain, then you must bypass the policy by forcing account access for your project. For more information, see [Forcing account access](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains#forcing_access).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
