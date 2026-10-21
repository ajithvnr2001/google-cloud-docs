---
url: https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution/
title: Traffic distribution for internal passthrough Network Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:24.321422+00:00
---

# Traffic distribution for internal passthrough Network Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Traffic distribution for internal passthrough Network Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

Passthrough Network Load Balancers distribute incoming traffic across available backend instances. This document explains how the load balancer selects backends, tracks connections, and manages session affinity, weighted load balancing, and failover.

Understanding how all these features work together helps you optimize your load balancing configuration for reliable performance and efficient resource utilization. These mechanisms are crucial for applications that require session persistence, letting them maintain consistent behavior for each user interaction.

## Backend selection and connection tracking

Backend selection and connection tracking work together to balance multiple connections across different backends and to route all packets for each connection to the same backend. This is accomplished with a two-part strategy. First, a backend is selected using consistent hashing. Then, this selection is recorded in a connection tracking table.

The following steps describe backend selection and connection tracking.

### **1**. Check for a connection tracking table entry

The load balancer determines whether a load-balanced packet belongs to a new connection or to an existing connection by using the following process:

  * _TCP packet with the`SYN` flag_:

    * If the load balancer's connection tracking mode is `PER_CONNECTION`, continue to the Identify eligible backends step. In `PER_CONNECTION` tracking mode, a TCP packet with the `SYN` flag always represents a new connection, regardless of the configured session affinity.

    * If the load balancer's connection tracking mode is `PER_SESSION` _and_ the session affinity is either `NONE` or `CLIENT_IP_PORT_PROTO`, continue to the Identify eligible backends step. In `PER_SESSION` tracking mode, a TCP packet with the `SYN` flag represents a new connection only when using one of the 5-tuple session affinity options (`NONE` or `CLIENT_IP_PORT_PROTO`).



  * _All other packets_ : the load balancer checks if the packet matches an existing connection tracking table entry. The granularity of the packet hash used to check for an existing connection tracking table entry depends on the connection tracking mode and session affinity you configured. For more information, see the table in the Connection tracking mode section.

    * If the packet matches a connection tracking table entry, the load balancer sends the packet to the previously selected backend.

    * If the packet doesn't match a connection tracking table entry, continue to the Identify eligible backends step.

For information about how long a connection tracking table entry persists and under what conditions it persists, see the Manage connection tracking table entries step.




### **2**. Backend selection steps

For a new connection, the load balancer uses [consistent hashing](https://en.wikipedia.org/wiki/Consistent_hashing) to select a backend from among the eligible backends.

The following steps outline the process to select an eligible backend for a new connection and then record that connection in a connection tracking table.

### **2.1** Identify eligible backends

_Eligible backends_ are the backends that are candidates to receive new connections. The following table defines the set of eligible backends depending on whether the load balancer uses failover.

Failover | Eligible backends  
---|---  
| When the failover load balancing feature is disabled, all configured backends are primary backends. The set of eligible backends is defined as follows:

  * When at least one backend is healthy, the set of eligible backends consists of all healthy backends.
  * When all backends are unhealthy, the set of eligible backends consists of _all_ backends.

  
| When the failover load balancing feature is enabled, the load balancer uses health check information and failover policy configuration to define the set of eligible backends:

  * When at least one (primary or failover) backend is healthy, the eligible backends are those that come from the first of the following sets that isn't empty: 
    1. If there are no healthy primary backends, the eligible backends are _all healthy failover backends_.
    2. If there are no healthy failover backends, the eligible backends are _all healthy primary backends_.
    3. If the failover ratio is set to `0.0` (the default value), the eligible backends are _all healthy primary backends_.
    4. If the ratio of the number of healthy primary backends compared to the total number of primary backends is greater than or equal to the configured failover ratio, the eligible backends consists of _all healthy primary backends_.
    5. The eligible backends consist of _all healthy failover backends_.
  * When there are no healthy (primary and failover) backends, the set of eligible backends depends exclusively on the failover policy configuration: 
    * If the failover policy is configured to drop new connections when all primary and failover backends are unhealthy, the set of eligible backends is empty. Consequently, the load balancer drops packets for new connections.
    * If the failover policy is _not_ configured to drop new connections when all primary and failover backends are unhealthy, the eligible backends are _all unhealthy primary backends_.

  
  
### **2.2** Adjust eligible backends for zonal affinity

This step is skipped if any of the following is true:

  * [Zonal affinity](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity) is disabled
  * The client is [incompatible with zonal affinity](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#compatible-clients)
  * A [zonal match](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#zonal-match) with the zone of a compatible client doesn't happen



If zonal affinity is enabled, a client is compatible with zonal affinity, and a zonal match happens, new connections from the client are routed to an adjusted set of eligible backends. For more information, see the following:

  * [How `ZONAL_AFFINITY_STAY_WITHIN_ZONE` works](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#zonal-affinity-stay-in-zone)

  * [How `ZONAL_AFFINITY_SPILL_CROSS_ZONE` and spillover ratio work](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#zonal-affinity-spillover-ratio)




### **2.3** Select an eligible backend

The load balancer maintains hashes of eligible backends, with each backend hash mapped to a unit circle. 

When processing a packet for a connection that's not in the connection tracking table, the load balancer computes a hash of the packet characteristics and maps that hash to the same unit circle, selecting an eligible backend on the circle's circumference. The set of packet characteristics used to calculate the packet hash is defined by the session affinity setting. For example, when the selected session affinity results in a 2-tuple or 3-tuple backend selection hash, all TCP connections from a source IP address are mapped to the same eligible backend.

  * If a session affinity isn't explicitly configured, the `NONE` session affinity is the default.


  * Consistent hashing ensures the load balancer assigns new connections to eligible backends in a way that minimizes mapping disruptions even if the number of eligible backends changes.

    * The load balancer _always_ selects the same eligible backend for a connection, and more generally, _always_ selects the same eligible backend for all packets with identical packet characteristics as defined by the session affinity setting, if the set of eligible backends does _not_ change.

    * If an eligible backend is added or removed, consistent hashing aims to minimize the disruption of mappings to the other eligible backends—that is, most connections that map to other eligible backends continue to map to the same eligible backend.

  * Furthermore, consistent hashing ensures the load balancer distributes new connections among eligible backends as fairly as possible. For all possible packet hashes as defined by the configured session affinity setting (and more specifically, for all possible connections when the session affinity results in a 5-tuple hash for backend selection):

    * When an eligible backend is added, approximately `1/N` new connections map to the newly added backend. In this situation, `N` is the count of backends _after_ the new backend is added.

    * When an eligible backend is removed, approximately `1/N` new connections map to one of the `N-1` remaining backends. In this situation, `N` is the count of backends _before_ the eligible backend is removed.




### **2.4** Create a connection tracking table entry

After selecting a backend, the load balancer creates a connection tracking table entry. The connection tracking table entry maps packet characteristics to the selected backend. The packet header fields used for this mapping depend on the connection tracking mode and session affinity you configured. 

For information about what packet characteristics are used for the hash in the connection tracking table, see the table in the Connection tracking mode section.

### **3**. Manage connection tracking table entries

The load balancer manages connection tracking table entries, according to the following events and rules:

  * _Idle entries are removed_ : a connection tracking table entry is removed after a certain amount of time if no new ingress packets are processed by the load balancer. Unless you configure a custom idle timeout, the load balancer uses a default idle timeout of 600 seconds. For more information, see Idle timeout.

  * _Entries are evicted when client connection tracking tables are full_ : Connection tracking tables for internal passthrough Network Load Balancers are implemented on _client_ systems, such as a host running a VM instance, a host powering a VLAN attachment, or a host running a Cloud VPN tunnel. When a client's connection tracking table is full, it removes the entries for the least recently used connections.



  * _Closed TCP connections_ : connection tracking table entries for TCP connections are _not_ removed when a TCP connection is closed with a `FIN` or `RST` packet. They might be removed later as an idle entry. Each _new_ TCP connection always carries the `SYN` flag, and is subject to the processing described in the Check for a connection tracking table entry step.

  * _When connections don't persist on failover_ : when at least one failover backend is configured and the connection draining on failover setting is disabled, the load balancer removes all entries in the connection tracking table after the set of eligible backends switches between primary and failover backends, subject to the following rules:

    * The load balancer doesn't proactively remove connection tracking table entries at the moment when the set of eligible backends switches between primary and failover backends. Instead, the load balancer removes each connection tracking table entry when a _next packet_ for the connection arrives, _provided that_ the set of eligible backends hasn't switched back.

    * If the set of eligible backends switches between primary and failover backends and back (for example, from primary to failover, then back to primary), and no packets for the connection arrived between the switching events, the connection tracking table entry is kept, unless another reason or event removes the connection tracking table entry.

For more information, see Connection draining on failover.

  * _When connections don't persist on unhealthy backends_ : when connection persistence on unhealthy backends is disabled for the packet's protocol, the load balancer removes connection tracking table entries on unhealthy backends according to the following rules:

    * The load balancer doesn't proactively remove connection tracking table entries to a previously-selected backend at the moment when the backend becomes unhealthy. Instead, the load balancer removes a connection tracking table entry when a _next packet_ for the connection arrives, _provided that_ the previously-selected backend _remains unhealthy_. Subsequent packets for the connection are treated as a new connection, because the load balancer selects a new eligible backend and creates a new connection tracking table entry.

    * If a previously-selected backend changes from healthy to unhealthy, then back to healthy, and no packets for the connection arrived while the previously-selected backend was unhealthy, the connection tracking table entry is kept, unless another reason or event removes the connection tracking table entry.

  * _Connection draining for removed, stopped, or deleted backends_ : if connection draining for removed, stopped, or deleted backends is enabled, connection tracking table entries are removed after a configurable connection draining timeout. Counting to the timeout begins when the command to remove (abandon), stop, or delete a backend is received (including deletion commands that are the result of scaling down a managed instance group). If connection draining for removed, stopped, or deleted backends is disabled, connection tracking table entries are removed when the command to remove, stop, or delete a backend is received. For more information, see [Enable connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining).




## Session affinity

The session affinity setting of an internal passthrough Network Load Balancer defines the packet hash for backend selection, and, based on the connection tracking mode, the packet hash for connection tracking.

You configure session affinity on the backend service, not on each backend instance group or NEG. The session affinity determines which IP and Layer 4 headers are used to calculate a hash of packet characteristics. The hash of packet characteristics is used in the Backend selection steps.

Internal passthrough Network Load Balancers support the following session affinity settings.

Hash method for backend selection | Session affinity setting  
---|---  
5-tuple hash (consists of source IP address, source port, protocol, destination IP address, and destination port) for non-fragmented packets that include port information (TCP packets and non-fragmented UDP packets) _OR_ 3-tuple hash (consists of source IP address, destination IP address, and protocol) for fragmented UDP packets and packets of all other protocols |  `NONE`1  
 _OR_  
`CLIENT_IP_PORT_PROTO`  
3-tuple hash   
(consists of source IP address, destination IP address, and protocol) | `CLIENT_IP_PROTO`  
2-tuple hash   
(consists of source IP address and destination IP address) | `CLIENT_IP`  
1-tuple hash   
(consists of source IP only) | `CLIENT_IP_NO_DESTINATION`  
  
1`NONE` session affinity doesn't indicate that there is no session affinity. Instead, it means that session affinity is done with a 5-tuple hash or a 3-tuple hash of packet characteristics—functionally the same behavior as when `CLIENT_IP_PORT_PROTO` is set.

### Session affinity and load balancer next hop

When an internal passthrough Network Load Balancer load balancer is a next hop of a static route, the destination IP address is not limited to the forwarding rule IP address of the load balancer. Instead, the destination IP address of the packet can be _any_ IP address that fits within the destination range of the static route.

Selecting an eligible backend depends on calculating a hash of packet characteristics. Except for the `CLIENT_IP_NO_DESTINATION` session affinity (1-tuple hash), the hash depends, in part, on the _packet_ destination IP address.

The load balancer selects the same backend for all possible new connections that have identical packet characteristics, as defined by session affinity, if the set of eligible backends does not change. If you need the same backend VM to process all packets from a client, based solely on the source IP address, regardless of destination IP addresses, use the `CLIENT_IP_NO_DESTINATION` session affinity. 

## Connection tracking policy

This section describes the settings in the load balancer's connection tracking policy:

  * Connection tracking mode
  * Connection persistence on unhealthy backends
  * Idle timeout



### Connection tracking mode

This section describes how the load balancer creates entries in its connection tracking table. Internal passthrough Network Load Balancers track connections for all protocols that they support and for all session affinity options. 

The connection tracking mode, protocol, and session affinity determine the set of packet characteristics that are used to make the packet hash in each connection tracking table entry. 

The connection tracking mode can be one of the following:

  * **`PER_CONNECTION`**. This is the default and most granular connection tracking mode. Each connection is defined as either a 5-tuple hash or a 3-tuple hash of packet characteristics, depending on whether port information is present in the packet. Non-fragmented packets that include port information (such as TCP packets and non-fragmented UDP packets) are tracked with 5-tuple hashes. All other packets are tracked with 3-tuple hashes.

  * **`PER_SESSION`**. This less granular connection tracking mode uses a hash that matches the session affinity hash. Depending on the chosen session affinity, the `PER_SESSION` tracking mode can treat multiple distinct connections as a single connection for connection tracking purposes. This reduces the frequency that a connection is considered new and subject to the Backend selection steps.




The following table summarizes:

  * The packet hashes used for _backend selection_ ; and
  * The packet hashes used for _connection tracking_ , based on the connection tracking mode, protocol, and session affinity.

Session affinity | Packet hash for backend selection | Packet hash for connection tracking  
---|---|---  
When using `PER_CONNECTION` tracking mode (default) | When using `PER_SESSION` tracking mode  
`NONE` (Default)  
_OR_  
`CLIENT_IP_PORT_PROTO` | 

  * **TCP and unfragmented UDP:** 5-tuple hash
  * **Fragmented UDP and all other protocols:** 3-tuple hash

| 

  * **TCP and unfragmented UDP:** connection tracking on, 5-tuple hash
  * **Fragmented UDP and all other protocols:** connection tracking on, 3-tuple hash

| 

  * **TCP and unfragmented UDP:** connection tracking on, 5-tuple hash
  * **Fragmented UDP and all other protocols:** connection tracking on, 3-tuple hash

  
`CLIENT_IP_PROTO` | 

  * **All protocols:** 3-tuple hash

| 

  * **TCP and unfragmented UDP:** connection tracking on, 5-tuple hash
  * **Fragmented UDP and all other protocols:** connection tracking on, 3-tuple hash

| 

  * **All protocols:** connection tracking on, 3-tuple hash

  
`CLIENT_IP` | 

  * **All protocols:** 2-tuple hash

| 

  * **TCP and unfragmented UDP:** connection tracking on, 5-tuple hash
  * **Fragmented UDP and all other protocols:** connection tracking on, 3-tuple hash

| 

  * **All protocols:** connection tracking on, 2-tuple hash

  
`CLIENT_IP_NO_DESTINATION` | 

  * **All protocols:** 1-tuple hash

| 

  * **TCP and unfragmented UDP:** connection tracking on, 5-tuple hash
  * **Fragmented UDP and all other protocols:** connection tracking on, 3-tuple hash

| 

  * **All protocols:** connection tracking on, 1-tuple hash

  
  
To learn how to change the connection tracking mode, see [Configure a connection tracking policy](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-connection-tracking-policy).

### Connection persistence on unhealthy backends

_Connection persistence on unhealthy backends_ controls whether existing connections can persist on a previously-selected backend VM if the previously-selected VM becomes unhealthy. Connection persistence on unhealthy backends requires that the backend VM remain a member of a load-balanced instance group or NEG.

The following connection persistence options are available:

  * `DEFAULT_FOR_PROTOCOL` (default)
  * `NEVER_PERSIST`
  * `ALWAYS_PERSIST`



The following table describes the connection persistence on unhealthy backends behavior depending on the connection persistence on unhealthy backends option, the connection tracking mode, the session affinity, and the protocol.

Connection persistence on unhealthy backends option | Connection persistence on unhealthy backends behavior  
---|---  
When using `PER_CONNECTION` tracking mode (default) | When using `PER_SESSION` tracking mode  
`DEFAULT_FOR_PROTOCOL` | 

  * **TCP, SCTP (all session affinities):** connections persist on unhealthy backends, subject to the other events and rules in the manage connection tracking table entries step
  * **All other protocols:** connections don't persist on unhealthy backends

| 

  * **TCP, SCTP (`NONE` and `CLIENT_IP_PORT_PROTO` session affinities):** connections persist on unhealthy backends, subject to the other events and rules in the manage connection tracking table entries step
  * **TCP, SCTP (all other session affinities) and all other protocols:** connections don't persist on unhealthy backends

  
`NEVER_PERSIST` | **All protocols:** connections don't persist on unhealthy backends   
`ALWAYS_PERSIST` This option should only be used for advanced use cases. | 

  * **All protocols (all session affinities):** connections persist on unhealthy backends, subject to the other events and rules in the Manage connection tracking table entries step

| Configuration not possible  
  
To learn how to change the connection persistence behavior, see [Configure a connection tracking policy](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-connection-tracking-policy).

#### TCP connection persistence behavior on unhealthy backends

The load balancer uses 5-tuple hash connection tracking for TCP connections in these situations:

  * When using the `PER_CONNECTION` tracking mode (all session affinities), or
  * When using the `PER_SESSION` tracking mode, _and_ the session affinity is _either_ `NONE` or `CLIENT_IP_PORT_PROTO`.



When the load balancer uses a 5-tuple hash connection tracking for TCP connections, keep the following behaviors in mind:

  * If the unhealthy backend continues to respond to packets, the connection continues until it is reset or closed (by either the unhealthy backend or the client).
  * If the unhealthy backend sends a TCP reset (RST) packet or does not respond to packets, then the client might retry with a new connection, letting the load balancer select a different eligible backend. (TCP `SYN` packets are treated as new connections in the Identify eligible backends step.)



### Idle timeout

A connection tracking table entry is removed after the connection has been idle for a certain period of time. Unless you configure a custom idle timeout, the load balancer uses a default idle timeout value of 600 seconds (10 minutes). 

The following table shows the minimum and maximum configurable idle timeout values for different combinations of session affinity and connection tracking mode settings.

Session affinity | Connection tracking mode | Default idle timeout | Minimum configurable idle timeout | Maximum configurable idle timeout  
---|---|---|---|---  
Any connection tuple | `PER_CONNECTION` | 600 seconds | 60 seconds | 600 seconds  
  
  * 1-tuple (`CLIENT_IP_NO_DESTINATION`)
  * 2-tuple (`CLIENT_IP`)
  * 3-tuple (`CLIENT_IP_PROTO`)

| `PER_SESSION` | 600 seconds | 60 seconds | 57,600 seconds  
5-tuple (`NONE`, `CLIENT_IP_PORT_PROTO`) | `PER_SESSION` | 600 seconds | 60 seconds | 600 seconds  
  
To learn how to change the idle timeout value, see [Configure a connection tracking policy](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-connection-tracking-policy).

## Connection draining for removed, stopped, or deleted backends

Connection draining provides a configurable minimum amount of time for existing connections to persist in the load balancer's connection tracking table when one of the following happens:

  * A virtual machine (VM) instance is removed from a backend instance group (this includes abandoning an instance in a backend managed instance group)
  * A VM is stopped or deleted (this includes automatic actions like rolling updates or scaling down a backend managed instance group)
  * An endpoint is removed from a backend network endpoint group (NEG)



By default, connection draining when backends are removed, stopped, or deleted is disabled. For more information, see [Enabling connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining).

## Failover

The failover feature lets you influence the set of eligible backends by classifying backend instance groups or NEGs and their endpoints like this:

  * _Primary backends_ are VMs or endpoints in an instance group or NEG that's configured as a _primary backend group_.
  * _Failover backends_ are VMs or endpoints in an instance group or NEG that's configured as a _failover backend group_.



By default, when you add an instance group or NEG to a backend service, the instance group or NEG is a primary backend group. You can add up to 50 primary backend groups and 50 failover backend groups to a backend service.

To enable the failover feature, you must configure the load balancer's backend service with both of the following:

  * At least one non-empty primary backend group
  * At least one non-empty failover backend group



When failover is enabled, the following factors determine the set of eligible backends:

  * The health state of each backend
  * The failover ratio in the failover policy
  * The _drop traffic if backends are unhealthy_ setting in the failover policy 

**Note:** A load balancer that has the failover feature enabled doesn't mean that its eligible backends are always failover backends. The failover feature requires both primary backends and failover backends, and the load balancer switches its eligible backends according to the configuration of the failover policy.

### Failover policy

You can adjust the following settings in the _failover policy_ of a backend service. The failover policy is only relevant if failover is enabled.

  * _Failover ratio_: a number between `0.0` and `1.0`, inclusive.
  * _Drop traffic if backends are unhealthy_ : a boolean that determines the load balancer's last resort behavior. The _failover ratio_ and the _drop traffic if backends are unhealthy_ setting work together with other factors to control the set of eligible backends.
  * Connection draining on failover: a boolean that controls whether connections persist on previously-selected backends when the set of eligible backends switches between primary and failover backends.



### Failover ratio

The failover ratio determines when the set of eligible backends switches between primary and failover backends. The ratio can be a number between `0.0` to `1.0`, inclusive. If you don't specify a failover ratio, Google Cloud uses a default value of `0.0`. It's a best practice to set your failover ratio to a number that works for your use case rather than relying on this default.

### Connection draining on failover

_Connection draining on failover_ controls whether an existing connection persists on a previously-selected backend VM or endpoint when the set of eligible backends switches between primary and failover backends.

Connection draining on failover is enabled by default. The following table summarizes whether connections persist, depending on the connection draining on failover option and protocol:

Connection draining on failover option | Behavior when the set of eligible backends switches between primary and failover backends  
---|---  
Enabled (default) | **All protocols:** connections persist, as long as a corresponding connection tracking table entry exists, when the set of eligible backends switches between primary and failover backends. For more information, see the manage connection tracking table entries step.   
Disabled | **All protocols:** connections don't persist when the set of eligible backends switches between primary and failover backends  
  
Disabling connection draining on failover is useful for the following scenarios:

  * **Patching backend VMs**. Prior to patching, you can configure healthy primary backends to fail health checks, so that the eligible backends can be healthy failover backends. By disabling connection draining on failover, the load balancer removes connection tracking table entries, applies the Backend selection steps to subsequent packets and delivers them to a different eligible backend. The different backend then closes the connection with a TCP reset, so that client VMs can quickly establish a new connection to the load balancer.

  * **Single backend VM for data consistency**. If you need to ensure that the set of eligible backends has no more than one member VM or endpoint, disabling connection draining on failover reduces the possibility of data inconsistencies.




To learn how to disable connection draining on failover, see [Defining a failover policy](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-failover#creating_failover_policy).

## Best practices and guidance

You can optimize the an internal passthrough Network Load Balancer by following these operational guidelines. The following sections provide technical requirements for managing fragmented UDP packets and best practices for testing load distribution from a single client.

### Handling UDP fragmentation

Internal passthrough Network Load Balancers can process both fragmented and unfragmented UDP packets. If your application uses fragmented UDP packets, keep the following in mind: 

  * UDP packets might become fragmented before reaching a Google Cloud VPC network.
  * Google Cloud VPC networks forward UDP fragments as they arrive (without waiting for all fragments to arrive).
  * Non-Google Cloud networks and on-premises network equipment might forward UDP fragments as they arrive, delay fragmented UDP packets until all fragments have arrived, or discard fragmented UDP packets. For details, see the documentation for the network provider or network equipment.



If you expect fragmented UDP packets and need to route them to the same backends, use the following forwarding rule and backend service configuration parameters:

  * **Forwarding rule configuration:** Use only one `UDP` forwarding rule per load-balanced IP address, and configure the forwarding rule to accept traffic on all ports. This ensures that all fragments arrive at the same forwarding rule. Even though the fragmented packets (other than the first fragment) lack a destination port, configuring the forwarding rule to process traffic for all ports also configures it to receive UDP fragments that have no port information. To configure all ports, either use the Google Cloud CLI to set [`--ports=ALL`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules) or use the API to set [`allPorts` to `True`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules).

  * **Backend service configuration:** Set the backend service's session affinity to `CLIENT_IP` (2-tuple hash) or `CLIENT_IP_PROTO` (3-tuple hash) so that the same backend is selected for UDP packets that include port information and UDP fragments (other than the first fragment) that lack port information. Set the backend service's connection tracking mode to `PER_SESSION` so that the connection tracking table entries are built by using the same 2-tuple or 3-tuple hashes.




### Testing from a single client

When testing an internal passthrough Network Load Balancer from a single client, keep the following in mind:

  * **If the client VM is not a backend of the load balancer** : new connections are processed as described in the Backend selection and connection tracking steps. In the Select an eligible backend step, the load balancer creates a hash of packet characteristics according to the session affinity.

Remember that all session affinity options rely on at least the IP address of the client, connections from the same client might be distributed to the same eligible backend more frequently than you might expect. Consequently, you can't accurately model the overall distribution of new connections by connecting to an internal passthrough Network Load Balancer from a single client.

  * **If the client VM is also a backend VM of the load balancer** : new connections aren't actually processed by the load balancer at all. Outbound packets with the destination IP address of the load balancer's forwarding rule are routed locally within the guest OS of the client due to the presence of a local route for the forwarding rule.




## What's next

  * To configure and test an internal passthrough Network Load Balancer that uses failover, see [Configure failover for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-failover).
  * To configure and test an internal passthrough Network Load Balancer, see [Set up an internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
