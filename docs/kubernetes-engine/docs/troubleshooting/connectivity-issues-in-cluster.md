---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/connectivity-issues-in-cluster/
title: Troubleshoot connectivity issues in your cluster \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:16.712758+00:00
---

# Troubleshoot connectivity issues in your cluster  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/connectivity-issues-in-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot connectivity issues in your cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) cluster network connectivity issues can cause connection timeouts, refused connections, unreachable Pods, Service disruptions, or inter-Pod communication failures.

Use this document to troubleshoot cluster connectivity by capturing network packets (by using `toolbox` and `tcpdump`) and diagnosing Pod network issues.

This information is important for Platform admins and operators and Application developers diagnosing and fixing network problems affecting GKE workloads. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Connectivity issues related to capturing network packets in GKE

This section describes how to troubleshoot connectivity issues related to capturing network packets, including symptoms like connection timeouts, connection refused errors, or unexpected application behavior. These connectivity issues can occur at the node level or at the Pod level.

Connectivity problems in your cluster network are often in the following categories:

  * **Pods not reachable** : A Pod might not be accessible from inside or outside the cluster due to network misconfigurations.
  * **Service disruptions** : A Service might be experiencing interruptions or delays.
  * **Inter-Pod communication issues** : Pods might not be able to communicate with each other effectively.



Connectivity issues in your GKE cluster can originate from various causes, including the following:

  * **Network misconfigurations** : Incorrect network policies, firewall rules, or routing tables.
  * **Application bugs** : Errors in application code affecting network interactions.
  * **Infrastructure problems** : Network congestion, hardware failures, or resource limitations.



The following section shows how to resolve the issue on the problematic nodes or Pods.

  1. Identify the node on which the problematic Pod is running by using the following command:
         
         kubectl get pods POD_NAME -o=wide -n NAMESPACE
         

Replace the following:

     * `POD_NAME` with the name of the Pod.
     * `NAMESPACE` with the Kubernetes namespace.
  2. Connect to the node:
         
         gcloud compute ssh NODE_NAME \
             --zone=ZONE
         

Replace the following:

     * `NODE_NAME`: name of your node.
     * `ZONE`: name of the zone in which the node runs.
  3. To debug a specific Pod, identify the `veth` interface associated with the Pod:
         
         ip route | grep POD_IP
         

Replace `POD_IP` with Pod IP address.

  4. Run the toolbox commands.




### `toolbox` commands

`toolbox` is a utility that provides a containerized environment within your GKE nodes for debugging and troubleshooting. This section describes how to install the `toolbox` utility and use it to troubleshoot the node.

  1. While connected to the node, start the `toolbox` tool:
         
         toolbox
         

This downloads the files that facilitate the `toolbox` utility.

  2. In the `toolbox` root prompt, install `tcpdump`:

     * For clusters with external IP addresses or Cloud NAT:
           
           apt update -y && apt install -y tcpdump
           

**Note:** This command needs internet access on your GKE nodes. Ensure that either your GKE nodes have external IP addresses or that a Cloud NAT Gateway is configured for the primary IPv4 address range of your cluster subnet. For private clusters, ensure that a Cloud NAT gateway is configured before running this command.
     * For private clusters without Cloud NAT:

If you have a private cluster without Cloud NAT, you can't install `tcpdump` using `apt`. Instead, download the `libpcap` and `tcpdump` release files from the [official repository](https://www.tcpdump.org/index.html) and copy the files to the VM using `gcloud compute scp` or `gcloud storage cp`. Then, install the libraries manually using the following steps:
           
           # Copy the downloaded packages to a staging area
           cp /media/root/home/USER_NAME/tcpdump-VERSION.tar.gz  /usr/sbin/
           cp /media/root/home/USER_NAME/libpcap-VERSION.tar.gz  /usr/sbin/
           cd /usr/sbin/
           
           # Extract the archives
           tar -xvzf tcpdump-VERSION.tar.gz
           tar -xvzf libpcap-VERSION.tar.gz
           
           # Build and install libpcap (a dependency for tcpdump)
           cd libpcap-VERSION
           ./configure ; make ; make install
           
           # Build and install tcpdump
           cd ../tcpdump-VERSION
           ./configure ; make ; make install
           
           # Verify tcpdump installation
           tcpdump --version
           

Replace the following:

       * `USER_NAME`: your username on the system where the files are located.
       * `VERSION`: the specific version number of the `tcpdump` and `libpcap` packages.
  3. Start the packet capture:
         
         tcpdump -i eth0 -s 100 "port PORT" \
         -w /media/root/mnt/stateful_partition/CAPTURE_FILE_NAME
         

Replace the following:

     * `PORT`: name of your port number.
     * `CAPTURE_FILE_NAME`: name of your capture file.
  4. Stop the packet capture and interrupt the `tcpdump`.

  5. Leave the toolbox by typing `exit`.

  6. List the packet capture file and check its size:
         
         ls -ltr /mnt/stateful_partition/CAPTURE_FILE_NAME
         

  7. Copy the packet capture from the node to the current working directory on your computer:
         
         gcloud compute scp NODE_NAME:/mnt/stateful_partition/CAPTURE_FILE_NAME \
             --zone=ZONE
         

Replace the following:

     * `NODE_NAME`: name of your node.
     * `CAPTURE_FILE_NAME`: name of your capture file.
     * `ZONE`: name of your zone.



### Alternative commands

You can also use the following ways to troubleshoot connectivity issues on the problematic Pods:

  * [Ephemeral debug workload](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#ephemeral-container-example) attached to the Pod container.

  * Run a shell directly on the target Pod using `kubectl exec`, then install and launch the `tcpdump` command.




## Pod network connectivity issues

As mentioned in the [Network Overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#pods) discussion, it is important to understand how Pods are wired from their network namespaces to the root namespace on the node in order to troubleshoot effectively. For the following discussion, unless otherwise stated, assume that the cluster uses GKE's native CNI rather than Calico's. That is, no [network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) has been applied.

### Pods on select nodes have no availability

If Pods on select nodes have no network connectivity, ensure that the Linux bridge is up:
    
    
    ip address show cbr0
    

**Note:** The virtual network bridge `cbr0` is only created if there are Pods which set `hostNetwork: false`.

If the Linux bridge is down, raise it:
    
    
    sudo ip link set cbr0 up
    

Ensure that the node is learning Pod MAC addresses attached to cbr0:
    
    
    arp -an
    

### Pods on select nodes have minimal connectivity

If Pods on select nodes have minimal connectivity, you should first confirm whether there are any lost packets by running `tcpdump` in the toolbox container:
    
    
    sudo toolbox bash
    

Install `tcpdump` in the toolbox if you have not done so already:
    
    
    apt install -y tcpdump
    

Run `tcpdump` against cbr0:
    
    
    tcpdump -ni cbr0 host HOSTNAME and port PORT_NUMBER and [TCP|UDP|ICMP]
    

Should it appear that large packets are being dropped downstream from the bridge (for example, the TCP handshake completes, but no SSL hellos are received), ensure that the MTU for each Linux Pod interface is correctly set to the MTU of the cluster's VPC network.
    
    
    ip address show cbr0
    

When overlays are used (for example, Weave or Flannel), this MTU must be further reduced to accommodate encapsulation overhead on the overlay.

#### GKE MTU

The MTU selected for a Pod interface is dependent on the Container Network Interface (CNI) used by the cluster Nodes and the underlying VPC MTU setting. For more information, see [Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#pods).

Autopilot is configured to always inherit the VPC MTU. 

The Pod interface MTU value is either `1460` or inherited from the primary interface of the Node.

CNI | MTU | GKE Standard  
---|---|---  
kubenet | 1460 | Default  
kubenet  
(GKE version 1.26.1 and later)  | Inherited | Default  
Calico | 1460 |  Enabled by using `--enable-network-policy`. For details, see [Control communication between Pods and Services using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy).  
netd | Inherited |  Enabled by using any of the following: 

  * [Intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility)
  * [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
  * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network)

  
GKE Dataplane V2 | Inherited |  Enabled by using `--enable-dataplane-v2`. For details, see [Using GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2).  
  
### Intermittent failed connections

Connections to and from the Pods are forwarded by iptables. Flows are tracked as entries in the conntrack table and, where there are many workloads per node, conntrack table exhaustion may manifest as a failure. These can be logged in the serial console of the node, for example:
    
    
    nf_conntrack: table full, dropping packet
    

If you are able to determine that intermittent issues are driven by conntrack exhaustion, you may increase the size of the cluster (thus reducing the number of workloads and flows per node), or increase `nf_conntrack_max`:
    
    
    new_ct_max=$(awk '$1 == "MemTotal:" { printf "%d\n", $2/32; exit; }' /proc/meminfo)
    sysctl -w net.netfilter.nf_conntrack_max="${new_ct_max:?}" \
      && echo "net.netfilter.nf_conntrack_max=${new_ct_max:?}" >> /etc/sysctl.conf
    

You can also use [NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache) to reduce connection tracking entries.

### "bind: Address already in use " reported for a container

A container in a Pod is unable to start because according to the container logs, the port where the application is trying to bind to is already reserved. The container is crash looping. For example, in Cloud Logging:
    
    
    resource.type="container"
    textPayload:"bind: Address already in use"
    resource.labels.container_name="redis"
    
    2018-10-16 07:06:47.000 CEST 16 Oct 05:06:47.533 # Creating Server TCP listening socket *:60250: bind: Address already in use
    2018-10-16 07:07:35.000 CEST 16 Oct 05:07:35.753 # Creating Server TCP listening socket *:60250: bind: Address already in use
    

When Docker crashes, sometimes a running container gets left behind and is stale. The process is still running in the network namespace allocated for the Pod, and listening on its port. Because Docker and the kubelet don't know about the stale container they try to start a new container with a new process, which is unable to bind on the port as it gets added to the network namespace already associated with the Pod.

To diagnose this problem:

  1. You need the UUID of the Pod in the `.metadata.uuid` field:
         
         kubectl get pod -o custom-columns="name:.metadata.name,UUID:.metadata.uid" ubuntu-6948dd5657-4gsgg
         
         name                      UUID
         ubuntu-6948dd5657-4gsgg   db9ed086-edba-11e8-bdd6-42010a800164
         

  2. Get the output of the following commands from the node:
         
         docker ps -a
         ps -eo pid,ppid,stat,wchan:20,netns,comm,args:50,cgroup --cumulative -H | grep [Pod UUID]
         

  3. Check running processes from this Pod. Because the UUID of the cgroup namespaces contain the UUID of the Pod, you can grep for the Pod UUID in `ps` output. Grep also the line before, so you will have the `docker-containerd-shim` processes having the container ID in the argument as well. Cut the rest of the cgroup column to get a simpler output:
         
         # ps -eo pid,ppid,stat,wchan:20,netns,comm,args:50,cgroup --cumulative -H | grep -B 1 db9ed086-edba-11e8-bdd6-42010a800164 | sed s/'blkio:.*'/''/
         1283089     959 Sl   futex_wait_queue_me  4026531993       docker-co       docker-containerd-shim 276e173b0846e24b704d4 12:
         1283107 1283089 Ss   sys_pause            4026532393         pause           /pause                                     12:
         1283150     959 Sl   futex_wait_queue_me  4026531993       docker-co       docker-containerd-shim ab4c7762f5abf40951770 12:
         1283169 1283150 Ss   do_wait              4026532393         sh              /bin/sh -c echo hello && sleep 6000000     12:
         1283185 1283169 S    hrtimer_nanosleep    4026532393           sleep           sleep 6000000                            12:
         1283244     959 Sl   futex_wait_queue_me  4026531993       docker-co       docker-containerd-shim 44e76e50e5ef4156fd5d3 12:
         1283263 1283244 Ss   sigsuspend           4026532393         nginx           nginx: master process nginx -g daemon off; 12:
         1283282 1283263 S    ep_poll              4026532393           nginx           nginx: worker process
         

  4. From this list, you can see the container ids, which should be visible in `docker ps` as well.

In this case:

     * `docker-containerd-shim 276e173b0846e24b704d4` for pause
     * `docker-containerd-shim ab4c7762f5abf40951770` for sh with sleep (sleep-ctr)
     * `docker-containerd-shim 44e76e50e5ef4156fd5d3` for nginx (echoserver-ctr)
  5. Check those in the `docker ps` output:
         
         # docker ps --no-trunc | egrep '276e173b0846e24b704d4|ab4c7762f5abf40951770|44e76e50e5ef4156fd5d3'
         44e76e50e5ef4156fd5d383744fa6a5f14460582d0b16855177cbed89a3cbd1f   registry.k8s.io/echoserver@sha256:3e7b182372b398d97b747bbe6cb7595e5ffaaae9a62506c725656966d36643cc                   "nginx -g 'daemon off;'"                                                                                                                                                                                                                                                                                                                                                                     14 hours ago        Up 14 hours                             k8s_echoserver-cnt_ubuntu-6948dd5657-4gsgg_default_db9ed086-edba-11e8-bdd6-42010a800164_0
         ab4c7762f5abf40951770d3e247fa2559a2d1f8c8834e5412bdcec7df37f8475   ubuntu@sha256:acd85db6e4b18aafa7fcde5480872909bd8e6d5fbd4e5e790ecc09acc06a8b78                                                "/bin/sh -c 'echo hello && sleep 6000000'"                                                                                                                                                                                                                                                                                                                                                   14 hours ago        Up 14 hours                             k8s_sleep-cnt_ubuntu-6948dd5657-4gsgg_default_db9ed086-edba-11e8-bdd6-42010a800164_0
         276e173b0846e24b704d41cf4fbb950bfa5d0f59c304827349f4cf5091be3327   registry.k8s.io/pause-amd64:3.1
         

In normal cases, you see all container ids from `ps` showing up in `docker ps`. If there is one you don't see, it's a stale container, and probably you will see a child process of the `docker-containerd-shim process` listening on the TCP port that is reporting as already in use.

To verify this, execute `netstat` in the container's network namespace. Get the pid of any container process (so NOT `docker-containerd-shim`) for the Pod.

From the preceding example:

     * 1283107 - pause
     * 1283169 - sh
     * 1283185 - sleep
     * 1283263 - nginx master
     * 1283282 - nginx worker
    
    # nsenter -t 1283107 --net netstat -anp
    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      1283263/nginx: mast
    Active UNIX domain sockets (servers and established)
    Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
    unix  3      [ ]         STREAM     CONNECTED     3097406  1283263/nginx: mast
    unix  3      [ ]         STREAM     CONNECTED     3097405  1283263/nginx: mast
    
    gke-zonal-110-default-pool-fe00befa-n2hx ~ # nsenter -t 1283169 --net netstat -anp
    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      1283263/nginx: mast
    Active UNIX domain sockets (servers and established)
    Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
    unix  3      [ ]         STREAM     CONNECTED     3097406  1283263/nginx: mast
    unix  3      [ ]         STREAM     CONNECTED     3097405  1283263/nginx: mast
    

You can also execute `netstat` using `ip netns`, but you need to link the network namespace of the process manually, as Docker is not doing the link:
    
    # ln -s /proc/1283169/ns/net /var/run/netns/1283169
    gke-zonal-110-default-pool-fe00befa-n2hx ~ # ip netns list
    1283169 (id: 2)
    gke-zonal-110-default-pool-fe00befa-n2hx ~ # ip netns exec 1283169 netstat -anp
    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      1283263/nginx: mast
    Active UNIX domain sockets (servers and established)
    Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
    unix  3      [ ]         STREAM     CONNECTED     3097406  1283263/nginx: mast
    unix  3      [ ]         STREAM     CONNECTED     3097405  1283263/nginx: mast
    gke-zonal-110-default-pool-fe00befa-n2hx ~ # rm /var/run/netns/1283169
    




Mitigation:

The short term mitigation is to identify stale processes by the method outlined preceding, and end the processes using the `kill [PID]` command.

Long term mitigation involves identifying why Docker is crashing and fixing that. Possible reasons include:

  * Zombie processes piling up, so running out of PID namespaces
  * Bug in docker
  * Resource pressure / OOM



## What's next

  * For general information about diagnosing Kubernetes DNS issues, see [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
