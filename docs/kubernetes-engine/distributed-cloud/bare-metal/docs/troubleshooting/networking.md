---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/networking/
title: Troubleshoot Google Distributed Cloud networking issues \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:04.689220+00:00
---

# Troubleshoot Google Distributed Cloud networking issues  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot Google Distributed Cloud networking issues Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve networking issues with Google Distributed Cloud. General troubleshooting information and guidance is provided, along with suggested tools. DNS troubleshooting information and some common issues for MetalLB are also included.

## Network connectivity troubleshooting

GKE Enterprise networking relies on your physical network infrastructure. For example, MetalLB relies on your switches honoring gratuitous ARP, bundled load balancing with Border Gateway Protocol (BGP) relies on your routers, and all nodes should be able to communicate with each other. When you have a networking issue in your GKE clusters, you must identify if the problem is in the GKE Enterprise components or in your own infrastructure.

First determine the scope of the problem, and then try to identify the affected components. The scope of an issue can be one of three categories: _the subject_ (from where), _the target_ (to which), and _the network layer_.

The _scope of subject_ can be one of the following:

  * All nodes (or [hostNetwork](https://kubesec.io/basics/spec-hostnetwork/) Pod) cluster-wide.
  * All Pods cluster-wide.
  * All Pods on a single node or a set of nodes.
  * All Pods from the same Deployment or DaemonSet.
  * Client from outside the cluster.



The _scope of target_ can be one or more of the following:

  * All other Pod IP addresses from the same cluster.
  * All other Pod IP addresses from the same node.
  * ClusterIP Service VIP from the same cluster.
  * LoadBalancer Service VIP from the same cluster.
  * Ingress Layer 7 LoadBalancer (Istio).
  * Other nodes from the same cluster.
  * Internal DNS name (like `*.svc.cluster.local`).
  * External DNS name (like `google.com`).
  * Entities from outside the cluster.
  * Entities on the internet.



The _network layer_ can be one or more of the following:

  * Layer 2 link layer problems like neighbor system, ARP, or NDP.
  * Layer 3 IP address routing problems.
  * Layer 4 TCP or UDP endpoint problems.
  * Layer 7 HTTP or HTTPS problems.
  * DNS resolution problems.



Understanding the scope of a problem helps to identify the components involved in the issue, and at what layer the issue occurs. Collecting information when the issue occurs is important because some issues are temporary, so snapshots after the system recovers won't include enough information for root cause analysis.

### Ingress issues

If the subject is a client from outside the cluster and it failed to connect to a LoadBalancer Service, it's a North-South connectivity issue. The following diagram shows that in a working example the incoming traffic travels through the stack from left to right, and return traffic travels back through the stack from right to left. 

![Ingress traffic passes from the user to the physical infrastructure, through a
load balancer to anetd / kube-proxy, and then to the backend.](https://docs.cloud.google.com/static/anthos/clusters/docs/images/anthos-networking-traffic-flows.svg)

When there's a problem with this flow of traffic, use the following troubleshooting flowchart to help identify where the problem is:

![Troubleshooting network ingress issues by reviewing each step a packet takes
as it moves through your environment. Check if the appropriate actions and
connectivity exists along the way.](https://docs.cloud.google.com/static/anthos/clusters/docs/images/anthos-networking-troubleshooting-flowchart.svg)

In this flowchart, the following troubleshooting guidance helps determine where the issue is:

  * Does the packet leave the client? If not, you likely have a network infrastructure issue. 
  * Are you using MetalLB? If so, does the packet arrive at the LB node, and is ARP then sent correctly? If not, you likely have a network infrastructure issue.
  * Are you using F5 BIG-IP, and if so, have you checked for F5 problems?
  * Is network address translation (NAT) performed correctly? If not, you likely have a kube-proxy / Dataplane V2 issue.
  * Does the packet arrive at the worker node? If not, you likely have a Dataplane v2 Pod-to-Pod issue.
  * Does the packet arrive at the Pod? If not, you likely have a Dataplane v2 local forwarding issue.



The following sections provide steps to troubleshoot each stage to determine if the traffic flows correctly or not.

#### Does the packet leave the client?

Check if the packet correctly leaves the client and passes through the router that's configured in your physical network infrastructure.

  1. Use `tcpdump` the check the packet as it leaves the client for the destination service:
         
         tcpdump -ni any host SERVICE_VIP and port SERVICE_PORT
         

If you don't see traffic going out, this is the source of the problem.




#### Does the packet arrive at a LoadBalancer node?

If you use MetalLB as the load balancer:

  1. Look at the `metallb-controller` log to determine which load balancer node serves the service VIP:
         
         kubectl -n kube-system logs -l app=metallb --all-containers=true | grep SERVICE_VIP
         

  2. Connect to the node using SSH.

  3. For a MetalLB node, use `tcpdump` to review the traffic:
         
         tcpdump -ni any host SERVICE_VIP and port SERVICE_PORT
         

For ManualLB, the traffic could land on any node. Depending on the load balancer configuration, you can choose one or several nodes. Use `tcpdump` to review the traffic:
         
         tcpdump -ni any host NODE_IP and port NODE_PORT
         

The command is different between load balancer types as MetalLB doesn't do NAT before forwarding the packet to nodes.

If you don't see traffic going into any node, this is the source of the problem.




#### Is there a F5 BIG-IP issue?

To troubleshoot for F5 BIG-IP issues, see one of the following sections on F5 Service doesn't receive traffic.

#### Is ARP correctly sent?

The load balancer node for MetalLB relies on ARP to advertise service VIP. If the ARP response is correctly sent out, but traffic isn't coming in, it's a signal of an issue in your physical networking infrastructure. A common cause of this issue is that some advanced dataplane learning features ignore ARP response in software defined network (SDN) solutions.

  1. Use `tcpdump` to detect ARP responses:
         
         tcpdump -ni any arp
         

Try to find the message that advertises the VIP you experience issues with.

  2. For MetalLB, it doesn't send gratuitous ARP. The frequency that you see a response depends on when another device like a top of rack (ToR) switch sends an ARP request.




#### Is NAT performed?

Dataplane v2 / kube-proxy performs destination network address translation (destination NAT or DNAT) to translate the destination VIP to a backend Pod IP address. If you know which node is the backend for load balancer, connect to the node using SSH.

  1. Use `tcpdump` to check if the Service VIP is correctly translated:
         
         tcpdump -ni any host BACKEND_POD_IP and port CONTAINER_PORT
         

  2. For Dataplane v2, you can additionally connect to the `anetd` pods and use the embedded Cilium debug tools:
         
         cilium monitor --type=drop
         




For more information, see one of the following sections on Dataplane v2 / Cilium issues.

#### Does the packet arrive at a worker node?

On the worker nodes, the packet arrives on the external interface and is then delivered to the Pods.

  1. Check if the packet arrives at the external interface, usually named `eth0` or `ens192`, using `tcpdump`:
         
         tcpdump -ni any host BACKEND_POD_IP and port CONTAINER_PORT
         


For Google Distributed Cloud, the packet is encapsulated in a tunnel. When the packet is decapsulated, it comes out from a network interface named `cilium_geneve`. 

Since normal Service backends contain multiple Pods across different nodes, it might be hard to troubleshoot which node is at fault. A common workaround is to either capture the problem long enough so that some packet eventually arrives, or limit the number of backends to one.

If the packet never arrives at the work node, it's an indication of a network infrastructure issue. Check with the networking infrastructure team to see why the packet is dropped between LoadBalancer nodes and worker nodes. Some common issues include the following:

  * Check your software-defined network (SDN) logs. Sometimes, the SDN could drop packets for various reasons, such as segmentation, wrong checksum, or anti-spoofing.
  * Firewall rules that filters geneve packets UDP port 6081. 



If the packet arrives at the node's external interface or tunnel interface, it needs to be forwarded to the destination Pod. If the Pod is a host networking Pod, this step isn't needed because the Pod shares the network namespace with the node. Otherwise, additional packet forwarding is required.

Each Pod has virtual ethernet interface pairs, which work like pipes. A packet sent to one end of the interface is received from the other end of the interface. One of the interfaces is moved to the Pod's network namespace, and renamed to `eth0`. The other interface is kept in the host namespace. Different CNIs have different schema. For Dataplane v2, the interface is normally named as `lxcxxxx`. The names have consecutive interface numbers, like `lxc17` and `lxc18`. You can check if the packet arrives at the Pod using `tcpdump`, or you can also specify the interface:
    
    
    tcpdump -ni lcxxxx host BACKEND_POD_IP and port CONTAINER_PORT
    

If the packet arrives at the node but fails to arrive at the Pod, check the routing table as follows:
    
    
    ip route
    

Normally, each Pod should have a routing entry route the Pod IP address to the `lxc` interface. If the entry is missing, it normally means the CNI datapath has an error. To determine the root cause, check the CNI DaemonSet logs.

### Egress issues

If traffic can ingress to a Pod, you might have an issue with traffic as it egresses the Pod. The following diagrams shows that in a working example the incoming traffic travels through the stack from left to right:

![Egress traffic passes from the Pod through the external interface of the host
to the physical infrastructure and then to the external service.](https://docs.cloud.google.com/static/anthos/clusters/docs/images/anthos-networking-egress-traffic-flows.svg)

  1. To verify that the outgoing packet correctly masquerades as the node IP address, check the external service (Layer 4).

The packet's source IP address should be mapped from the Pod IP address to the node IP address with source network address translation (source NAT or SNAT). In Dataplane v2, this process is achieved by [ebpf that's loaded on an external interface](https://docs.cilium.io/en/latest/network/concepts/masquerading/). 

Use `tcpdump` to check if the source IP address is correctly translated from Pod IP address to node IP address:
         
         tcpdump -ni EXTERNAL_INTERFACE host EXTERNAL_IP and port EXTERNAL_PORT
         

If `tcpdump` shows that packets are correctly masqueraded but the remote service doesn't respond, check the connection to the external service in your infrastructure.

  2. If the outgoing packets are correctly masqueraded as the node IP address, check external host (Layer 3) connectivity using `tcpdump`:
         
         tcpdump -ni EXTERNAL_INTERFACE host EXTERNAL_IP and icmp
         

At the same time as running `tcpdump`, ping from one of the Pods:
         
         kubectl exec POD_NAME ping EXTERNAL_IP
         

If you don't see ping responses, check the connection to the external service in your infrastructure.




### In-cluster issues

For Pod-to-Pod connectivity issues, try to scope the problem to nodes. Often, a group of nodes can't communicate with another group of nodes.

  1. In Dataplane v2, check node connectivity from the current node to all other nodes in the same cluster. From inside the `anetd` Pod, check the health status:
         
         cilium status --all-health
         




### Network layer issues

Identifying which network layer the connectivity issue happens in is an important step. An error message like, _"A connectivity issue from a source to a destination"_ isn't informative enough to help resolve the issue, which could be an application error, routing issue, or DNS issue. Understanding at which layer the issue happens helps to fix the right component.

Many times, error messages directly indicate which layer the issue happens. The following examples can help you troubleshoot network layer questions:

  * HTTP errors indicate that it's a Layer 7 issue. 
    * HTTP codes `40x`, `50x`, or TLS handshake errors means that everything works normally at Layer 4.
  * _"Connection reset by peer"_ errors indicate that it's a Layer 4 issue. 
    * Many times, the remote socket can't agree with the current state of a connection and so send a `RESET` packet. This behavior could be a mistake in connection tracking, or NAT.
  * _"No route to host"_ and _"Connection timeout"_ errors are normally a Layer 3 or Layer 2 issue. 
    * These errors indicate that the packet can't be correctly routed to the destination.



## Useful troubleshooting tools

Network-related DaemonSets run on your nodes and could be the cause of connectivity issues. However, misconfiguration of your nodes, top of rack (ToR) switches, spine routers, or firewalls can also cause issues. You can use the following tools to help determine the scope or layer of the issue and determine if it's a problem with your GKE Enterprise nodes or your physical infrastructure.

### Ping

Ping works at Layer 3 (IP layer) and checks the route between a source and destination. If ping fails to reach a destination, it often means the issue is at layer 3.

However, not all IP addresses are pingable. For example, some load balancer VIPs aren't pingable if it's a pure Layer 4 load balancer. The `ClusterIP` Service is an example where the VIP might not return a ping response. At layer 4, this Service only returns a ping response when you specify a port number, such as `VIP:port`.

The BGPLB and MetalLB load balancers in Google Distributed Cloud all work at layer 3. You can use ping to check the connectivity. Although F5 is different, it also supports ICMP. You can use ping to check connectivity to the F5 VIP.

### Arping

Arping is similar to ping, except that it works at layer 2. Layer 2 and layer 3 issues often have similar error messages from applications. Arping and ping can help to differentiate the issue. For example, if the source and destination are in the same subnet but you can't arping the destination, it's a Layer 2 issue.

A successful `arping <ip>` returns the MAC address of the destination. At layer 2, this address often indicates a physical infrastructure issue. This issue is often a physical switch between nodes. 

Arping can also detect IP address conflicts. An IP address conflict is when two machines are configured to use the same IP address on the same subnet, or a VIP is used by another physical machine. IP address conflicts can create intermittent issues that are hard to troubleshoot. If `arping <ip>` returns more than one MAC address entry, it's an indication that there's an IP address conflict.

After you get the MAC address from arping, you can use <https://maclookup.app/> to look up the manufacturer of the MAC address. Every manufacturer owns a MAC prefix, so you can use this information to help determine which device is trying to use the same IP address. For example, VMware owns the `00:50:56` block, so a MAC address `00:50:56:xx:yy:zz` is a VM in your vSphere environment.

### `iproute2`

The `ip` CLI for `iproute2` has many useful subcommands, such as the following:

  * `ip r`: print the route table
  * `ip n`: print the neighbor table for IP address to MAC address mapping
  * `ip a`: print all the interfaces on the machine



A missing route or missing entry in the neighbor table might cause connectivity issues from the node. Anetd manages the route table and neighbor table. A misconfiguration in those tables can cause connectivity issues.

### Cilium / Hubble CLI for Dataplane v2

Each `anetd` Pod has several useful debugging tools for connectivity issues:

  * `cilium monitor --type=drop`
    * Print the log for every packet that is dropped by anetd / Cilium.
  * `hubble observe`
    * Print all the packets going through anetd's ebpf stack.
  * `cilium status --all-health`
    * Print Cilium's status, including the node-to-node connectivity status. Each anetd Pod checks the health of all other nodes in the cluster and can help determine any node-to-node connectivity issues.



### Iptables

Iptables are used in many Kubernetes components and subsystems. `kube-proxy` uses iptables to implement service resolution. 

  1. To troubleshoot network issues at the iptables level, use the following command:
         
         iptables -L -v | grep DROP
         

Review the drop rules, and check the packet counts and byte counts to see if they increase over time.




### Tcpdump

Tcpdump is a powerful packet capture tool that generates a lot of network traffic data. A common practice is to run tcpdump from both the source and the destination. If a packet is captured when it leaves the source node but never captured on the destination node, it means that something in between drops the packet. This behavior usually indicates that something in your physical infrastructure mistakenly drops the packet.

### Metrics

Google Distributed Cloud contains multiple metrics to help you track the behavior of your network. The following metrics provide a good starting point:

Category | Metric | Description  
---|---|---  
Dropped packets | `cilium_drop_bytes_total` | Total dropped bytes, tagged by drop reason and ingress/egress direction. This metric is a good starting point for investigating byte-level drops.  
`cilium_drop_count_total` | Total dropped packets, tagged by drop reason and ingress/egress direction.  
`container_network_receive_packets_dropped_total` | Cumulative count of packets dropped while receiving. Sampled every 60 seconds.  
`container_network_transmit_packets_dropped_total` | Cumulative count of packets dropped while transmitting. Sampled every 60 seconds.  
Forwarded packets | `cilium_forward_bytes_total` | Total forwarded bytes, tagged by ingress/egress direction. Sampled every 60 seconds. This metric gives you byte-level forwarding information.   
`cilium_forward_count_total` | Total forwarded packets, tagged by ingress/egress direction. Sampled every 60 seconds. This metric gives you the packet count for forwarded traffic.  
`cilium_policy_l7_forwarded_total` | Total L7 forwarded requests.  
Received packets | `cilium_policy_l7_received_total` | Number of total L7 received requests/responses. Sampled every 60 seconds.  
`container_network_receive_bytes_total` | Cumulative count of bytes received. Sampled every 60 seconds.  
`container_network_receive_packets_total` | Cumulative count of packets received. Sampled every 60 seconds.  
`container_network_receive_errors_total` | Cumulative count of errors encountered while receiving. Sampled every 60 seconds.  
`cilium_kubernetes_events_received_total` | Number of Kubernetes events received labeled by scope, action, valid data and equalness. Sampled every 60 seconds.  
BPF | `cilium_bpf_maps_virtual_memory_max_bytes` | BPF maps kernel max memory usage size in bytes.  
`cilium_bpf_progs_virtual_memory_max_bytes` | BPF programs kernel max memory usage size in bytes.  
Conntrack | `node_nf_conntrack_entries` | Number of currently allocated flow entries for connection tracking. Sampled every 60 seconds.  
`node_nf_conntrack_entries_limit` | Maximum size of connection tracking table. Sampled every 60 seconds.   
Connectivity | `cilium_node_connectivity_latency_seconds` | The last observed latency between the current Cilium agent and other Cilium nodes in seconds. Sampled every 60 seconds.  
`cilium_node_connectivity_status` | The last observed status of both ICMP and HTTP connectivity between the current Cilium agent and other Cilium nodes. Sampled every 60 seconds.   
Cilium operators | `cilium_operator_process_cpu_seconds_total` | Total user and system CPU time spent in seconds. Sampled every 60 seconds.  
`cilium_operator_process_max_fds` | Maximum number of open file descriptors. Sampled every 60 seconds.   
`cilium_operator_process_open_fds` | Number of open file descriptors. Sampled every 60 seconds.  
`cilium_operator_process_resident_memory_bytes` | Resident memory size in bytes. Sampled every 60 seconds.  
`cilium_operator_process_start_time_seconds` | Start time of the process since unix epoch in seconds. Sampled every 60 seconds.  
`cilium_operator_process_virtual_memory_bytes` | Virtual memory size in bytes. Sampled every 60 seconds.  
`cilium_operator_process_virtual_memory_max_bytes` | Maximum amount of virtual memory available in bytes. Sampled every 60 seconds.  
`cilium_operator_identity_gc_entries` | The number of alive and deleted identities at the end of a garbage collector run. Sampled every 60 seconds.  
`cilium_operator_identity_gc_runs` | The number of times identity garbage collector has run. Sampled every 60 seconds.  
  
To receive notifications when any of these metrics exceed or fall below a certain threshold, create alerting policies. To learn more see, [Creating alerting policies](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/alerting-policies-creating). 

To learn more about these metrics and to see the complete list of metrics, see [Google Distributed Cloud metrics](/kubernetes-engine/distributed-cloud/bare-metal/docs/metrics-anthos). 

## DNS troubleshooting

DNS resolution issues fall into two main categories:

  * Regular Pods, which use the in-cluster DNS servers.
  * Host-network Pods or nodes, which don't use in-cluster DNS servers



The following sections provide some information on cluster DNS architecture and helpful tips before you start to troubleshoot one of these categories.

### Cluster DNS architecture

A Cluster DNS service resolves DNS requests for Pods in the cluster. CoreDNS provides this service for all versions of Google Distributed Cloud. 

Each cluster has two or more `coredns` Pods, and an autoscaler that's responsible for scaling the number of DNS Pods relative to the cluster size. There's also a service named `kube-dns` that load-balances requests between all backend `coredns` Pods.

Most Pods have their upstream DNS configured to the `kube-dns` Service IP address, and Pods send DNS requests to one of the `coredns` Pods. DNS requests can be grouped into one of the following destinations:

  * If the request is for a `cluster.local` domain, it's an in-cluster DNS name that references a Service or Pod in the cluster. 
    * CoreDNS watches the `api-server` for all Services and Pods in the cluster, and responds to requests for valid `cluster.local` domains.
  * If the request isn't for a `cluster.local` domain, then it's for an external domain. 
    * CoreDNS forwards the request to the upstream nameserver(s). By default, CoreDNS uses the upstream nameservers that are configured on the node it is running on.



For more information, see the [overview of how DNS works and is configured in Kubernetes](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).

### DNS troubleshooting tips

To troubleshoot DNS issues, you can use the `dig` and `nslookup` tools. These tools let you send DNS requests to test if DNS resolution works correctly. The following examples show you how to use `dig` and `nslookup` to check for DNS resolution issues.

  * Use `dig` or `nslookup` to send a request for `google.com`:
        
        dig google.com
        nslookup google.com
        

  * Use `dig` to send a request for `kubernetes.default.svc.cluster.local` to server `192.168.0.10`:
        
        dig @192.168.0.10 kubernetes.default.svc.cluster.local
        

  * You can also use `nslookup` to perform the same DNS lookup as the previous `dig` command:
        
        nslookup kubernetes.default.svc.cluster.local 192.168.0.10
        

Review the output of the dig or nslookup commands. If you receive an incorrect response, or no response, this indicates a DNS resolution issue.




### Regular Pods

The first step to debug a DNS issue is to determine whether requests make it to the `coredns` Pods or not. Often a general cluster connectivity issue appears as DNS issues because a DNS request is the first type of traffic that a workload sends.

Review error messages from your applications. Errors like `io timeout` or similar indicate there's no response and a general network connectivity issue.

Error messages that include a DNS error code like `NXDOMAIN` or `SERVFAIL` indicate there's connectivity to the in-cluster DNS server, but the server failed to resolve the domain name:

  * `NXDOMAIN` errors indicate that the DNS server reports that the domain doesn't exist. Verify that the domain name your application requests is valid.
  * `SERVFAIL` or `REFUSED` errors indicate that the DNS server sent back a response, but it wasn't able to resolve the domain or validate that it doesn't exist. For more information, check the logs of the `coredns` Pods.



You can find the IP address of the `kube-dns` service using the following command:
    
    
    kubectl -n kube-system get svc kube-dns
    

From a Pod where DNS isn't working, try to send a DNS request to this IP address using `dig` or `nslookup` as detailed in a previous section:

  * If these requests don't work, try to send requests to the IP address of each `coredns` Pod.
  * If some Pods work but not others, check if there are any discernible patterns, such as DNS resolution works for Pods on the same node as the `coredns` Pod, but not across nodes. This behavior could indicate some in-cluster connectivity issue.



If CoreDNS can't resolve external domain names, see the following section to troubleshoot the host-network Pods. CoreDNS behaves like a host network Pod and uses the node's upstream DNS servers for name resolution.

### Host-network Pods or nodes

Host-network Pods and the nodes use the nameservers configured on the node for DNS resolution, not the in-cluster DNS service. Depending on the OS, this nameserver is configured in either `/etc/resolv.conf` or `/run/systemd/resolve/resolv.conf`. This configuration means they can't resolve `cluster.local` domain names.

If you have issues with host-network name resolution, use the troubleshooting steps in the previous sections to test if DNS works correctly for your upstream nameservers.

Verify that all nodes have the same set of servers configured. If you have different nameservers configured, you might see inconsistencies in DNS resolution on different nodes. Verify that each nameserver works individually by sending a request to each one using `dig` or `nslookup`. If some nameservers work but others don't, you see this type of inconsistent DNS resolution failures. 

## Common network issues

The following sections detail some common networking issues that you might encounter. To help resolve your issue, follow the appropriate troubleshooting guidance. If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support). 

### Dataplane v2 / Cilium

**Common error:** `[PUT /endpoint/{id}][429] putEndpointIdTooManyRequests`

This error means that the Pod creation event has been rejected by the Cilium agent due to a rate limit. For each node, [Cilium has a limit of four concurrent requests to the PUT endpoint](https://docs.cilium.io/en/v1.9/configuration/api-rate-limiting/). When there's a burst of requests to one node, this behavior is expected. The Cilium agent should catch up on delayed requests.

In GKE Enterprise 1.14 and later, the rate limit auto adjusts to the node capacity. The rate limiter can converge to a more reasonable number, with higher rate limits for more powerful nodes.

**Common error:** `Ebpf map size is full`

Dataplane v2 stores state in an eBFP map. State includes Service, connect tracking, Pod identity, and Network Policy rules. If a map is full, the agent can't insert entries, which creates a discrepancy between the control plane and the data plane. For example, the Service map has a 64k entry limit.

  1. To check eBFP map entries and their current size, use `bpftool`. The following example checks the load balancer maps:
         
         bpftool map dump pinned \
         /sys/fs/bpf/tc/globals/cilium_lb4_services_v2 | tail -n -1
         
         bpftool map dump pinned \ /sys/fs/bpf/tc/globals/cilium_lb4_backends_v2 | tail -n -1
         

  2. If the map is close to the 64k limit, clean up the maps. The following example cleans up the load balancer maps:
         
         bpftool map dump pinned /sys/fs/bpf/tc/globals/cilium_lb4_services_v2 | \
             awk '{ print "0x"$2, "0x"$3, "0x"$4, "0x"$5, "0x"$6, "0x"$7, "0x"$8, "0x"$9, "0x"$10, "0x"$11, "0x"$12, "0x"$13}' | \
             head -n -1 | \
             xargs -L 1 bpftool map delete pinned /sys/fs/bpf/tc/globals/cilium_lb4_services_v2 key
         
         bpftool map dump pinned /sys/fs/bpf/tc/globals/cilium_lb4_backends_v2 | \
             awk '{ print "0x"$2, "0x"$3, "0x"$4, "0x"$5 }' | \
             head -n -1 | \
             xargs -L 1 bpftool map delete pinned /sys/fs/bpf/tc/globals/cilium_lb4_backends_v2 key
         

  3. To refill the state into the eBFP map, restart `anetd`.




### Node unready because of NetworkPluginNotReady errors

If the CNI Pod isn't running on the node, you might see an error similar to the following:
    
    
      "Container runtime network not ready" networkReady="NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized
    

The node might also be in an unready state, with an error similar to the following example:
    
    
      "Network plugin not installed"
    

When a node is initialized, `kubelet` waits for several events to happen before it marks the node as `Ready`. One of the events that `kubelet` checks is that the Container Network Interface (CNI) plugin is installed. The CNI plugin should be installed by anetd using an init container to install both the CNI binary and the CNI config into the required host directories.

To troubleshoot this issue, check why those Pods aren't running on the node. Usually, the error isn't due to network issues. Those pods run on the host network, so there's no network dependency.

  1. Check the state of the `anetd` Pod. Review the following troubleshooting steps to help determine the cause of the issue:

     * If the Pod is in a `Crashlooping` state, check the logs to see why the Pod can't run correctly.
     * If the Pod is in a `Pending` state, use `kubectl describe` and review the Pod events. For example, the Pod might be missing a resource like a Volume.
     * If the Pod is in `Running` state, check the logs and the configuration. Some CNI implementations provide options to disable CNI installation, like in [Cilium](https://docs.cilium.io/en/v1.11/concepts/kubernetes/configuration/#adjusting-cni-configuration).
     * There's a config option in anetd called `custom-cni-conf`. If this setting is configured as `true`, anetd won't install their CNI binary.



### Node NOT READY due to stale ARP entries

Sometimes, stale ARP entries in admin cluster control plane nodes can cause a mismatch in MAC addresses. This address mismatch can, in turn, cause connection timeouts to the control plane VIPs of managed user clusters. The connection timeouts can lead to the node with stale ARP entries being marked as `NOT READY`. Nodes marked as `NOT READY` can stall cluster installations and upgrades.

In this situation, the kubelet log on the node with stale ARP entries contains a TLS handshake timeout error like the following:
    
    
    failed to get API group resources: unable to retrieve the complete list of server APIs: v1: Get "https://128.160.252.101:443/api/v1": net/http: **TLS handshake timeout**

Use the following steps to verify and resolve the problem:

  1. Use SSH to connect to the user cluster control plane node.

  2. Verify the MAC address of the interface to which the VIP address is bound:
         
         ip a | grep DEVICE_NAME: -A 6
         

Replace `DEVICE_NAME` with the network device name for the control plane node.

  3. Use SSH to connect to an admin cluster control plane node.

  4. Check the ARP cache on the admin cluster control plane for the user cluster control plane VIP address:
         
         ip n | grep VIP_ADDRESS
         

Replace `VIP_ADDRESS` with the IP address of the user cluster control plane VIP (`controlPlaneVIP`).

If the two `ip` commands return a different mac address, you're affected by this issue.

  5. To resolve the issue, flush the ARP cache on the admin cluster control plane node:
         
         ip n flush all
         




### F5 Service doesn't receive traffic

If no traffic passes to the F5 Service, review the following troubleshooting steps:

  1. Check that every partition in F5 BIG-IP is [configured in one cluster](https://docs.cloud.google.com/architecture/partners/installing-f5-big-ip-adc-for-gke-on-prem#additional_configuration), either admin or user clusters. If one partition is shared by multiple different clusters, you experience intermittent connection interruptions. This behavior is because two clusters try to seize control over the same partition, and delete Services from other clusters.

  2. Verify that the following two Pods are running. Any non-running Pods indicate an error:
         
         Load-balancer-f5
         K8s-bigip-ctlr-deployment-577d57985d-vk9wj
         

The `Load-balancer-f5` owned by GKE Enterprise, and creates ConfigMaps for every LoadBalancer type Service. The ConfigMap is eventually consumed by `bigip` controller.

  3. Make sure that the ConfigMap exists for each port of each Service. For example, with the following ports:
         
         Kube-server-443-tcp     2   31h
         Kube-server-8132-tcp        2   31h
         

The `kube-server` Service should look similar to the following example:
         
         Kube-server LoadBalancer  10.96.232.96  21.1.7.16   443:30095/TCP,8132:32424/TCP  31h
         

The data section in the ConfigMap should have the frontend VIP and port, as shown in the following example:
         
         data: '{"virtualServer":{"backend":{"serviceName":"kube-apiserver","servicePort":443,"healthMonitors":[{"protocol":"tcp","interval":5,"timeout":16}]},"frontend":{"virtualAddress":{"bindAddr":"21.1.7.16","port":443},"partition":"herc-b5bead08c95b-admin","balance":"ratio-member","mode":"tcp"}}}'
           schema: f5schemadb://bigip-virtual-server_v0.1.7.json
         

  4. Check your BIG-IP instance logs and metrics. If the ConfigMap is correctly configured, but the BIG-IP instance fails to honor the config, it could be an F5 issue. For issues that happen inside the BIG-IP instance, [contact F5 support](https://www.f5.com/services/support) to diagnose and troubleshoot the issues.




### NAT failure with too many parallel connections

For a given node in your cluster, the node IP address provides network address translation (NAT) for packets routed to an address outside of the cluster. Similarly, when inbound packets enter a load-balancing node configured to use bundled load balancing (`spec.loadBalancer.mode: bundled`), source network address translation (SNAT) routes the packets to the node IP address before they are forwarded on to a backend Pod.

The port range for NAT used by Google Distributed Cloud is `32768-65535`. This range limits the number of parallel connections to 32,767 per protocol on that node. Each connection needs an entry in the conntrack table. If you have too many short-lived connections, the conntrack table runs out of ports for NAT. A garbage collector cleans up the stale entries, but the cleanup isn't immediate.

When the number of connections on your node approaches 32,767, you start seeing packet drops for connections that need NAT.

To determine if you're affected by this problem:

  1. Run the following command on the `anetd` Pod on the problematic node:
         
         kubectl -n kube-system anetd-XXX -- hubble observe \
             --from-ip $IP --to-ip $IP -f
         

You should see errors of the following form:
         
         No mapping for NAT masquerade DROPPED
         




As a workaround for this issue, redistribute your traffic to other nodes.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
