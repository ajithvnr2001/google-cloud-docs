---
url: https://docs.cloud.google.com/memorystore/docs/memcached/troubleshoot-issues/
title: Troubleshoot issues \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:06.297719+00:00
---

# Troubleshoot issues  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/troubleshoot-issues/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Troubleshoot issues Stay organized with collections  Save and categorize content based on your preferences. 

This page explains various error scenarios, the error messages for those scenarios, and troubleshooting steps to resolve the errors.

## Networking error scenarios

#### Allocated IP range is exhausted

Memorystore for Memcached requires that you use a [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) connection and an associated IP address range for that connection. It is possible to exhaust the IP addresses available in that range with Memcached instances and other Google Cloud resources.

If the IP addresses are exhausted, creating an instance returns the following error message:

`ERROR: (gcloud.memcache.instances.create) { "code": 9, "message": "Unable to create instance. The allocated private IP address space is exhausted. For information on expanding the allocation, see https://cloud.google.com/vpc/docs/configure-private-services-access#modify-ip-range" }`

You can resolve this issue by allocating additional IP addresses. For more information on how to do this, see [IP address range exhaustion](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modify-ip-range).

#### You do not have a private services access connection established for your network

If you attempt to create a Memorystore for Memcached instance without a private services access connection established for your project's network, the creation will fail with the following error:

`Google private service access is not enabled. Enable private service access and try again`

In order to successfully create an instance, follow the private services access setup instructions at [Establishing a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).

#### The network peering for private services access is deleted

Establishing a [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) connection creates a network peering connection called `servicenetworking-googleapis-com`, which appears in your project's [VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering) page.

Deleting this network peering may cause you to receive the following errors:

  * `telnet: Unable to connect to remote host: Connection timed out`
  * `Unable to create instance. Enable private service access for the authorized network and try again. For information on enabling private service access, see https://cloud.google.com/service-infrastructure/docs/enabling-private-services-access`



To resolve this issue, follow the last step of the gcloud instructions at [Establishing a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).

#### Firewall rules block your instance IP addresses

Connectivity issues can arise if you create firewall rules that block IP addresses from the allocated IP range associated with your private services access connection.

Make sure not to create network firewall rules that block the IP range of your Memcached instances.

## Errors connecting to your Memcached instance from other Google Cloud resources

#### Errors connecting to your instance from the App Engine standard environment or Cloud Run functions

If you cannot connect to a Memcached instance using the App Engine standard environment or Cloud Run functions, it is possible that you did not set up a Serverless VPC Access connector for your environment.

For instructions on setting up Serverless VPC Access for the App Engine standard environment, see [Connecting to a VPC network](https://docs.cloud.google.com/appengine/docs/standard/python/connecting-vpc).

For instructions on setting up Serverless VPC Access for Cloud Run functions, see [Connecting to a VPC network](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc).

#### Errors when connecting to your instance using a Google Kubernetes Engine cluster

You cannot connect to a Memorystore for Memcached instance from a GKE cluster without VPC-native/IP aliasing enabled on your cluster. It is easiest to enable VPC-native/IP aliasing during GKE cluster creation. When creating your cluster, select **VPC Native** under advanced options. For more details, see [Creating VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).

#### Errors when connecting to your instance using the App Engine flexible environment or Compute Engine VMs

If your instance experiences connectivity issues, follow these troubleshooting steps:

  1. Ensure that your Memcached instance is provisioned in the same region and network as the client trying to access it.

  2. Check that your project does not have any network firewall rules blocking your Memcached instance's node IPs.

     * To view the IP addresses of your nodes, view the nodes tab of your Memcached instance in the Google Cloud console.
  3. Telnet to one of your memcached nodes, and [run some simple Memcached `set` and `get`](https://docs.cloud.google.com/memorystore/docs/memcached/create-instance-gcloud#connecting_to_your_instance_from_a_vm) commands to see if the instance is responsive or not.

     * If the node is unresponsive, see if any of the troubleshooting issues from [Networking error scenarios](https://docs.cloud.google.com/memorystore/docs/memcached/troubleshoot-issues#networking_error_scenarios) are blocking your node's network connection. If not, contact [Google Cloud Support](https://docs.cloud.google.com/support).



## Identity and Access Management ( IAM ) error scenarios

#### Restoring a deleted service account

Memorystore for Memcached uses the following service accounts to manage your Memcached instances:

  * service-project-number@service-networking.iam.gserviceaccount.com
  * service-project-number@cloud-memcache-sa.iam.gserviceaccount.com



Deleting the policy bindings for these service accounts prevents you from being able to create new instances.

If you attempt to create a Memcached instance using gcloud in this scenario, you may receive the following error message:

`ERROR: (gcloud.memcache.instances.create) { "code": 13, "message": "an internal error has occurred" }`

To re-establish the policy binding for these service accounts, run one of the following commands, replacing variables with appropriate values. Run the command associated with the deleted service account.
    
    
    gcloud projects add-iam-policy-binding project-id --member='serviceAccount:service-project-number@service-networking.iam.gserviceaccount.com' --role='roles/servicenetworking.serviceAgent'
    
    
    
    gcloud projects add-iam-policy-binding project-id --member='serviceAccount:service-project-number@cloud-memcache-sa.iam.gserviceaccount.com' --role='roles/memcache.serviceAgent'
    

## Operation timeout errors

The following error scenarios result in an unresponsive Memcached instance and/or instance/node operation timeouts.

#### Network partition error

Sometimes Google Cloud resources cannot communicate across zones within a region due to a network partition error in Google Cloud servers. This can cause your instance to lose connection, resulting in a timeout error.

After Google Cloud resolves the network partition error for the region or zone where your instance is provisioned, connectivity should resume normally.

In this scenario, you may see a connectivity error message such as the following:

`telnet: Unable to connect to remote host: Connection timed out`

If you are not able to identify the cause of the timeout error, reach out to [Google Cloud Support](https://docs.cloud.google.com/support).

#### Improper application reference to node IPs

If your client is timing out when attempting to connect to a node(s), one potential issue is that your application may not be specifying the proper IP address of the node(s) to which you are trying to connect. Verify that your application is pointing to the IP addresses of the nodes in your cluster.

In this scenario, you may see a connectivity error message, such as the following message:

`telnet: Unable to connect to remote host: Connection timed out`

To resolve this issue, look up the IP addresses of your nodes, and make sure that your application points accurately to the node addresses.

## Additional error scenarios

#### Unsupported Compute Engine IP address ranges

You cannot access Memorystore for Memcached from Compute Engine VMs that have an IP address within the range `172.17.0.0/16`, because that range is reserved for an internal component.

#### Unbalanced node distribution across zones in a region

If a zone in a Google Cloud region is unavailable at the time you provision a Memcached instance, nodes are created in the available zones. This can lead to an imbalanced distribution of Memached nodes across zones in a region.

This should not have a noticeable impact on your application performance. However, ideally, your nodes should be distributed across all zones in a region to protect your data from zonal outages.

If you are unsatisfied with the distribution of nodes across zones when you create an instance, you can either wait until that zone is back online to create your instance, or you can use the following strategy to attempt to re-distribute nodes across zones at a later time:

To re-distribute Memcached nodes among the available nodes in a zone, [scale up](https://docs.cloud.google.com/memorystore/docs/memcached/scaling-instances) your instance, then scale back down to the desired number of nodes. If the desired zone(s) is back online, the scaling process will re-distribute nodes evenly across available zones. Also, note that scaling causes a cache flush for the data in your Memcached instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
