---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/cassandra-pod-in-crashloopbackoff-status/
title: Cassandra Pods in CrashLoopBackOff Status \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:44:53.478383+00:00
---

# Cassandra Pods in CrashLoopBackOff Status  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/cassandra-pod-in-crashloopbackoff-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Cassandra Pods in CrashLoopBackOff Status Stay organized with collections  Save and categorize content based on your preferences. 

## Symptom

Cassandra pods can go into a `CrashLoopBackOff` state while either installing or upgrading Apigee hybrid. 

## Error messages

`kubectl get pods` output when run in `apigee` namespace shows one or more Cassandra pods in `CrashLoopBackOff` status: 
    
    
    kubectl get pods -n apigee
    
    NAME                          READY   STATUS            RESTARTS   AGE
    apigee-cassandra-default-0    0/1     CrashLoopBackoff  0          9m

## Possible causes

Cassandra pods can enter `CrashLoopBackOff` status for various reasons. 

Cause | Description  
---|---  
Failed hostname resolution | `UnknownHostException` thrown for DNS resolution  
Incorrect Image | Incorrect image url used in `overrides.yaml`  
Expansion problem | Connectivity issue to the Cassandra seed host  
Port conflict | Port 7000 or 7001 already in use  
Same IP Address | A node with address /10.10.x.x already exists  
  
## Cause 1: Failed hostname resolution

Hostname resolution for Cassandra nodes fails due to DNS configuration issues in the cluster. Cassandra's pod logs might show similar log entry: 
    
    
    ERROR [main] 2025-01-12 13:23:34,569 CassandraDaemon.java:803 -
    Local host name unknown: java.net.UnknownHostException: ip-xx-xx-xx-xx.example.com:
    ip-xx-xx-xx-xx.example.com: Name or service not known

### Resolution

The worker node where Cassandra pod is slated to come up should be able to resolve hostname to a valid IP address via the cluster DNS service. For a workaround, you can run the following command on all the worker nodes: 
    
    
    echo -e "\\n127.0.1.1 ${HOSTNAME}" >> "/etc/hosts"

**Note:** This issue may be due to the hostname not being included in your `etc/hosts` file. See the recommendations for your platform in [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/multi-region). 

## Cause 2: Incorrect Image

Incorrect Cassandra image used. 

### Diagnosis

Check the `overrides.yaml` file to make sure the correct image is configured for Cassandra. Here is a sample stanza in `overrides.yaml` with the correct Cassandra image. 
    
    
    cassandra:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra"
        tag: "1.15.0"
        pullPolicy: IfNotPresent

### Resolution

Ensure the version and name of the Cassandra image is accurate in `overrides.yaml` file and attempt the install or upgrade command again. You can use List option in [`apigee-pull-push` script](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/hybrid/apigee-pull-push#list-the-images-in-your-repository) to list all the images in your repo. You can then review those images to ensure they are all the images from the intended version of Hybrid. 

## Cause 3: Expansion problem

The Cassandra pod might not be able to connect to the Seed node while expanding to a new region. 

### Diagnosis

  1. Cassandra pod logs may show similar log entries as in the following example: 
         
         INFO  [main] 2024-07-28 05:25:15,662 GossipingPropertyFileSnitch.java:68 - Unable to load cassandra-topology.properties; compatibility mode disabled
         The seed provider lists no seeds.
         WARN  [main] 2024-07-28 05:25:15,703 SimpleSeedProvider.java:60 - Seed provider couldn't lookup host apigee-cassandra-default-0.apigee-cassandra-default.apigee.svc.cluster.local
         Exception (org.apache.cassandra.exceptions.ConfigurationException) encountered during startup: The seed provider lists no seeds.
         ERROR [main] 2024-07-28 05:25:15,703 CassandraDaemon.java:803 - Exception encountered during startup: The seed provider lists no seeds.
         INFO  [ScheduledTasks:1] 2024-07-28 05:25:15,833 StorageService.java:136 - Overriding RING_DELAY to 30000ms

  2. Check connectivity between the current failing node and the seed node.
  3. Identify the seed node configured in `overrides.yaml` for the new region. Seed node is configured in `overrides.yaml` at the time of region expansion under the field name: `multiRegionSeedHost`. 

Sample Cassandra stanza from your `overrides.yaml` showing the `multiRegionSeedHost`. 
         
         cassandra:
           multiRegionSeedHost: "1.2.X.X"
           datacenter: "dc-1"
           rack: "rc-1"
           hostNetwork: false
           clusterName: QA

  4. Create a client container to check connectivity between failing Cassandra pod and seed node by following instructions in [Create a client container for debugging](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-a-client-container-for-debugging)
  5. After you `ssh` into the client container and have a bash shell, use telnet to check connectivity from current node to seed node via ports 7001 and 7199 

Sample telnet command and output showing connection failure 
         
         telnet 10.0.0.0 7001
         Trying 10.0.0.0...
         telnet: Unable to connect to remote host: Connection timed out
         telnet 10.0.0.0 7199
         Trying 10.0.0.0...
         telnet: Unable to connect to remote host: Connection timed out




### Resolution

  1. Work with your cluster admin team to ensure there is network connectivity between Cassandra nodes across all the clusters that are part of the same org. 
  2. Ensure there are no firewall rules blocking traffic from the failing node to seed node.



## Cause 4: Port conflict

Port conflict

Cassandra was trying to come up to listen on port 7000 and 7001 but some other service such as ssh was already listening on that port. 

### Diagnosis

Cassandra's pod logs may show similar entries as in the following example: 
    
    
    Unable to create ssl socket
    Fatal configuration error; unable to start server.  See log for stacktrace.
    ERROR [main] 2023-02-27 13:01:54,239 CassandraDaemon.java:803 - Fatal configuration error
    org.apache.cassandra.exceptions.ConfigurationException: Unable to create ssl socket
           at org.apache.cassandra.net.MessagingService.getServerSockets(MessagingService.java:701) ~[apache-cassandra-3.11.9.jar:3.11.9]
           at org.apache.cassandra.net.MessagingService.listen(MessagingService.java:681) ~[apache-cassandra-3.11.9.jar:3.11.9]
           at org.apache.cassandra.net.MessagingService.listen(MessagingService.java:665) ~[apache-cassandra-3.11.9.jar:3.11.9]
           at org.apache.cassandra.service.StorageService.prepareToJoin(StorageService.java:831) ~[apache-cassandra-3.11.9.jar:3.11.9]
           at org.apache.cassandra.service.StorageService.initServer(StorageService.java:717) ~[apache-cassandra-3.11.9.jar:3.11.9]
           at org.apache.cassandra.service.StorageService.initServer(StorageService.java:666) ~[apache-cassandra-3.11.9.jar:3.11.9]
           at org.apache.cassandra.service.CassandraDaemon.setup(CassandraDaemon.java:395) [apache-cassandra-3.11.9.jar:3.11.9]
           at org.apache.cassandra.service.CassandraDaemon.activate(CassandraDaemon.java:633) [apache-cassandra-3.11.9.jar:3.11.9]
           at org.apache.cassandra.service.CassandraDaemon.main(CassandraDaemon.java:786) [apache-cassandra-3.11.9.jar:3.11.9]
    Caused by: java.net.BindException: Address already in use (Bind failed)
    Caused by: java.net.BindException: Address already in use (Bind failed)

This suggests that the port is already used.

### Resolution

Stop and remove any service other than Cassandra listening on Ports 7000 and 7001, this should allow Cassandra applications to come up. 

## Cause 5: Same IP address

An older Cassandra pod with the same IP exists in the cluster. This situation can arise after uninstalling Hybrid or reinstalling Hybrid. 

### Diagnosis

  1. Review Cassandra's `system.log` file for the following error: 
         
         INFO  [HANDSHAKE-/10.106.32.131] 2020-11-30 04:28:51,432 OutboundTcpConnection.java:561 - Handshaking version with /10.10.1.1
         Exception (java.lang.RuntimeException) encountered during startup: A node with address /10.10.1.1 already exists, cancelling join. Use cassandra.replace_address if you want to replace this node.
         java.lang.RuntimeException: A node with address /10.10.1.1 already exists, cancelling join. Use cassandra.replace_address if you want to replace this node.
            at org.apache.cassandra.service.StorageService.checkForEndpointCollision(StorageService.java:558)
            at org.apache.cassandra.service.StorageService.prepareToJoin(StorageService.java:804)
            at org.apache.cassandra.service.StorageService.initServer(StorageService.java:664)
            at org.apache.cassandra.service.StorageService.initServer(StorageService.java:613)
            at org.apache.cassandra.service.CassandraDaemon.setup(CassandraDaemon.java:379)
            at org.apache.cassandra.service.CassandraDaemon.activate(CassandraDaemon.java:602)
            at org.apache.cassandra.service.CassandraDaemon.main(CassandraDaemon.java:691)
         ERROR [main] 2020-11-30 04:28:52,287 CassandraDaemon.java:708 - Exception encountered during startup
         java.lang.RuntimeException: A node with address /10.10.1.1 already exists, cancelling join. Use cassandra.replace_address if you want to replace this node.

  2. Review the output of `nodetool status` command from any of the DCs that are still up to see if a Cassandra node is shown with the same IP as in the error message - 10.10.1.1. 

Sample nodetool status command output 
         
         kubectl exec apigee-cassandra-default-0 -n  -- nodetool status
         Datacenter dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens  Owns (effective)  Host ID                               Rack
         UN  10.10.1.1  649.6 KiB  256     100.0%            4d96eaf5-7e75-4aeb-bc47-9e45fdb4b533  ra-1
         UN  10.10.1.2  885.2 KiB  256     100.0%            261a15dd-1b51-4918-a63b-551a64e74a5e  ra-1
         UN  10.10.1.3  693.74 KiB 256     100.0%            91e22ba4-fa53-4340-adaf-db32430bdda9  ra-1




### Resolution

  1. Remove the old Cassandra node by using `nodetool remove` command: 
         
         nodetool removenode HOST_ID

The host id can be found in the output of nodetool status. For example: `4d96eaf5-7e75-4aeb-bc47-9e45fdb4b533` in the previous sample nodetool status output. 

  2. Once the older Cassandra node is removed, retry Hybrid installation.



## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID.
  2. The Apigee hybrid organization.
  3. The `overrides.yaml` files from both source and new regions, masking any sensitive information.
  4. The outputs from the commands in [Apigee hybrid must-gather](https://docs.cloud.google.com/apigee/docs/support/best-practices#apigee-hybrid-must-gather).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
