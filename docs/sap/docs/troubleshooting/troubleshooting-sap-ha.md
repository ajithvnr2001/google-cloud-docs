---
url: https://docs.cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha/
title: Troubleshooting high-availability configurations for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:32.609982+00:00
---

# Troubleshooting high-availability configurations for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/troubleshooting/troubleshooting-sap-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  Troubleshooting high-availability configurations for SAP Stay organized with collections  Save and categorize content based on your preferences. 

In high-availability configurations for SAP on Google Cloud, the root cause of issues might lie in the clustering software, the SAP software, the Google Cloud infrastructure, or some combination of these.

## Analyze Pacemaker logs in Cloud Logging

The following video shows how you can start troubleshooting high-availability configurations for SAP on Google Cloud using Cloud Logging.

## Failed node in a Linux cluster doesn't restart properly after a failover

If your Linux high-availability cluster uses the `fence_gce` fence agent and a fenced Compute Engine instance fails to rejoin the cluster after a failover, then you might need to delay the start of the Corosync software when fenced instances restart.

### Issue

During a failover, the `fence_gce` agent fences the failed Compute Engine instance, which reboots and rejoins the cluster before Pacemaker registers the fence action as complete. Because Pacemaker doesn't register the fence action as complete, the rebooted instance shuts down its Pacemaker and Corosync services and leaves the cluster.

### Diagnosis

To confirm that this is your issue, complete the following steps:

  1. Verify that your cluster is using the `fence_gce` agent:

###  RHEL 
         
         pcs config

###  SLES 
         
         crm config show

The fence agent definition includes `fence_gce`:

###  RHEL 
         
         Stonith Devices:
         Resource: STONITH-example-ha-vm1 (class=stonith type=**fence_gce**)
         Attributes: port=example-ha-vm1 project=example-project-123456 zone=us-central1-a
         Operations: monitor interval=300s timeout=120s (STONITH-example-ha-vm1-monitor-interval-60s)
         Resource: STONITH-example-ha-vm2 (class=stonith type=**fence_gce**)
         Attributes: port=example-ha-vm2 project=example-project-123456 zone=us-central1-c
         Operations: monitor interval=300s timeout=120s (STONITH-example-ha-vm2-monitor-interval-60s)
         

###  SLES 
         
         primitive fence-example-ha-vm1 stonith:**fence_gce** \
          op monitor interval=300s timeout=120s \
          op start interval=0 timeout=60s \
          params port=example-ha-vm1 zone=us-central1-a project=example-project-123456
         primitive fence-example-ha-vm2 stonith:**fence_gce** \
          op monitor interval=300s timeout=120s \
          op start interval=0 timeout=60s \
          params port=example-ha-vm2 zone=us-central1-c project=example-project-123456

  2. Check the system log for the following messages:
         
         DATESTAMP> node2 stonith-ng[1106]:  notice: Operation reboot of node2 by node1 for stonith_admin.1366@node1.c3382af8: OK
         DATESTAMP> node2 stonith-ng[1106]:   error: stonith_construct_reply: Triggered assert at commands.c:2343 : request != NULL
         DATESTAMP> node2 stonith-ng[1106]: warning: Can't create a sane reply
         DATESTAMP> node2 crmd[1110]:    crit: We were allegedly just fenced by node1 for node1!
         DATESTAMP> node2 pacemakerd[1055]: warning: Shutting cluster down because crmd[1110] had fatal failure




### Solution

To resolve this issue, try the following approaches:

  1. Configure the operating systems in both cluster nodes to delay the start of Corosync, and thereby ensure that the fence action has time to register as complete with Pacemaker on the new primary node. Also, set the Pacemaker reboot timeout value to account for the delay. For information about how to do this, see Configure the OS to delay the start of Corosync.
  2. If the preceding approach does not resolve the race condition, then use an additional delay in conjunction, which is to increase the GRUB menu selection timeout. For information about how to do this, see the following:

     * For RHEL, see the RedHat solution [How to change the grub timeout period in Red Hat Enterprise Linux?](https://access.redhat.com/solutions/548253)
     * For SLES, see the [SUSE administration guide](https://documentation.suse.com/sles/15-SP7/html/SLES-all/cha-grub2.html#:%7E:text=feature%20is%20active.-,GRUB_TIMEOUT,-Time%20period%20in).



#### Configure the OS to delay the start of Corosync

  1. Put the cluster in maintenance mode:

###  RHEL 
         
         pcs property set maintenance-mode=true

###  SLES 
         
         crm configure property maintenance-mode="true"

  2. On each cluster node as root, set a start delay for Corosync:

     1. Create a `systemd` drop-in file:
            
            systemctl edit corosync.service

     2. Add the following lines to the file:
            
            [Service]
            ExecStartPre=/bin/sleep 60

     3. Save the file and exit the editor.

     4. Reload the systemd manager configuration.
            
            systemctl daemon-reload

  3. On either cluster node as root, verify that the Pacemaker timeout value for reboots is set for both fence agents:

     1. Check the `pcmk_reboot_timeout` value:
            
            crm_resource --resource FENCE_AGENT_NAME --get-parameter=pcmk_reboot_timeout

Replace `FENCE_AGENT_NAME` with the name of the fence agent.

     2. If the `pcmk_reboot_timeout` parameter is not found or is set to a value that is smaller than 300, set the value on both fence agents:
            
            crm_resource --resource FENCE_AGENT_NAME --set-parameter=pcmk_reboot_timeout --parameter-value=300

Replace `FENCE_AGENT_NAME` with the name of the fence agent.

The `pcmk_reboot_timeout` value should be greater than the sum of:

        * The Corosync `token` timeout
        * The Corosync consensus timeout, which by default is the product of `token` * 1.2
        * The length of time it takes a reboot operation to complete, including any delay attribute.

On Google Cloud, 300 seconds is sufficient for most clusters.

     3. Confirm the new `pcmk_reboot_timeout` value:
            
            crm_resource --resource FENCE_AGENT_NAME --get-parameter=pcmk_reboot_timeout

Replace `FENCE_AGENT_NAME` with the name of the fence agent.

  4. Take the cluster out of maintenance mode:

###  RHEL 
         
         pcs property set maintenance-mode=false

###  SLES 
         
         crm configure property maintenance-mode="false"




## Unintentional node affinity that favors a particular node

When you manually move resources in a high-availability cluster using the cluster commands, you find that an automatic affinity or client preference is set to favor a particular node.

### Issue

In your Linux Pacemaker high-availability cluster for SAP HANA or SAP NetWeaver, resources such as SAP HANA system or SAP NetWeaver central services only run on one particular cluster node and do not fail over as expected during a node failure event.

Consequently, you might experience issues such as:

  * When you trigger the SAP NetWeaver ASCS service failover by issuing a Pacemaker command to `move` a resource to a cluster node, the resource does not start and shows the status `stopped`.

  * When you issue the `standby` command to one cluster node to force all resources to move to the other node, the resources do not start.




### Diagnosis

  * Check your Pacemaker logs for the message that mentions a particular resource cannot run anywhere. For example:
        
        2021-05-24 21:39:58 node_1 pacemaker-schedulerd (native_color) info:
         Resource NW1-ASCS01 cannot run anywhere

  * Check your Pacemaker location constraint configuration to identify any constraints that might be preventing the resources from running on a certain cluster node.

To check the Pacemaker location constraint configuration, follow these steps:

    1. Display the location constraints:
           
           cibadmin --query --scope constraints | grep rsc_location

    2. Verify the location constraints:

       * Explicit location constraint: You find location constraints with score `INFINITY` (prefer the node) or `-INFINITY` (avoid the node). For example:
             
             <rsc_location id="loc-constraint" rsc="NW1-ASCS01" score="INFINITY" node="nw-ha-1"/>

There must not be any location constraint with score `INFINITY` or `-INFINITY` other than the fence agents. In all HA clusters, fence agents are defined in a location constraint with score `-INFINITY`, to prevent them from running on the node that is the fencing target.

       * Implicit location constraint: When you issue the Pacemaker command to move a resource to a cluster node or ban a resource to run on a cluster node, an implicit location constraint with prefix `cli-ban` or `cli-prefer` is added to the constraint id. For example:
             
             <rsc_location id="cli-prefer-NW1-ASCS01" rsc="NW1-ASCS01" role="Started" node="nw-ha-2" score="INFINITY"/>




### Solution

  * Make sure that the location constraints are specified as explained in our deployment guides:

    * [HA scale-up cluster configuration guide for SAP HANA on RHEL](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#create_the_constraints)
    * [HA scale-up cluster configuration guide for SAP HANA on SLES](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#configure_pacemaker)
    * [HA cluster manual configuration guide for SAP NetWeaver on RHEL](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel#configure_the_location_and_ordering_constraints)
    * [HA cluster manual configuration guide for SAP NetWeaver on SLES](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-sles#configure_the_resource_groups_and_location_constraints)
  * To fix an explicit location constraint, delete the location constraint:

###  RHEL 
        
        pcs constraint remove RESOURCE_LOCATION_ID

###  SLES 
        
        crm configure delete RESOURCE_LOCATION_ID

Replace `RESOURCE_LOCATION_ID` with the location constraint id.

  * To fix an implicit location constraint, remove all constraints defined on the specified resource.

After each command that you use to move or ban a resource, run the following command to remove all constraints:

###  RHEL 
        
        pcs resource clear RESOURCE_NAME

###  SLES 
        
        crm resource clear RESOURCE_NAME

Replace `RESOURCE_NAME` with the name of the resource that you're moving.




## Fence agent experienced an operational error

The fence agent has reported an error in the cluster status.

### Issue

In your Linux Pacemaker high-availability cluster for SAP HANA or SAP NetWeaver, the fence agent has reported an error in the cluster status. For example: 
    
    
    Failed Resource Actions:
       STONITH-ha-node-01_monitor_300000 on ha-node-02 'unknown error' (1): call=153, status=Timed Out, exitreason='',  last-rc-change='Mon Dec 21 23:40:47 2023', queued=0ms, exec=60003ms

### Diagnosis

The fence agent deployed in your SAP HANA or SAP NetWeaver high-availability cluster regularly accesses Compute Engine API server to check the status of the fence target instance. If there is a temporary delay in the API call response or if there is a network interruption, then the fence agent monitoring operation might fail or time out.

To check the fence agent status, run the following command:

###  RHEL 
    
    
    pcs status

###  SLES 
    
    
    crm status

If the fence agent status is `stopped`, then use one of the solution options to resolve the error.

The fence agent operational error might cause the fence agent to stop, but Pacemaker still calls the fence agents with a stop directive in a fencing event.

### Solution

If the fence agent status is `stopped`, then do one of the following:

  * To manually reset the failcount and restart the fence agent, run the following command:

###  RHEL 
        
        pcs resource cleanup FENCE_AGENT_NAME

###  SLES 
        
        crm resource cleanup FENCE_AGENT_NAME

Replace `FENCE_AGENT_NAME` with the name of the fence agent.

  * To automatically remove the fence agent operational error, configure the `failure-timeout` parameter.

The `failure-timeout` parameter resets the failcount after the specified duration and clears any operational errors. Applying this parameter doesn't require you to restart the cluster or put the cluster in the maintenance mode.

To configure the `failure-timeout` parameter, run the following command:
        
        crm_resource --meta --resource FENCE_AGENT_NAME --set-parameter failure-timeout --parameter-value DURATION

Replace the following:

    * `FENCE_AGENT_NAME`: the name of the fence agent.
    * `DURATION`: the duration following the last operational failure after which the failcount is reset and the fence agent is restarted.



## Fence agent `gcpstonith` is deprecated

The fence agent `gcpstonith` is active in your configuration. This agent is deprecated and Customer Care has communicated that you must switch to `fence_gce` instead.

### Issue

In your Linux Pacemaker high-availability cluster for SAP HANA on SUSE Linux, the fence agent `gcpstonith` is used. For example:
    
    
     # crm status | grep gcpstonith
       * STONITH-hana-vm1   (stonith:external/**gcpstonith**):   Started hana-vm2
       * STONITH-hana-vm2   (stonith:external/**gcpstonith**):   Started hana-vm1

### Diagnosis

The fence agent deployed in your SAP HANA high-availability cluster needs to be updated to use the OS bundled `fence_gce` fence agent instead. The `gcpstonith` agent script was delivered on legacy systems and has been superseded by `fence_gce`. `fence_gce` is provided as part of the `fence-agents` SUSE Linux package. `gcpstonith` was only delivered as part of SUSE Linux HANA deployments.

### Solution

To migrate from `gcpstonith` on SUSE Linux, complete the following steps:

  1. Install the following additional packages specific to your operating system:

     * For SLES 15: `python3-oauth2client` and `python3-google-api-python-client`

     * For SLES 12: `python-google-api-python-client`, `python-oauth2client`, and `python-oauth2client-gce`

To install these packages on your operating system, use the following command:

###  SLES 15 
    
    zypper in -y python3-oauth2client python3-google-api-python-client

###  SLES 12 
    
    zypper in -y python-google-api-python-client python-oauth2client python-oauth2client-gce

  2. Update the `fence-agents` package to ensure that you have the latest version installed:
         
         zypper update -y fence-agents

  3. Place the cluster in maintenance mode:
         
         crm configure property maintenance-mode=true

  4. Delete all the fencing devices from your cluster. While deleting the last fencing device, you might be prompted to acknowledge that no `STONITH` resources are defined in your cluster.
         
         crm configure delete FENCING_RESOURCE_PRIMARY
         
         crm configure delete FENCING_RESOURCE_SECONDARY

  5. Recreate the fencing device for the primary instance:
         
         crm configure primitive FENCING_RESOURCE_PRIMARY stonith:fence_gce \
          op monitor interval="300s" timeout="120s" \
          op start interval="0" timeout="60s" \
          params port="PRIMARY_INSTANCE_NAME" zone="PRIMARY_ZONE" \
          project="PROJECT_ID" \
          pcmk_reboot_timeout=300 pcmk_monitor_retries=4 pcmk_delay_max=30

  6. Recreate the fencing device for the secondary instance:
         
         crm configure primitive FENCING_RESOURCE_SECONDARY stonith:fence_gce \
          op monitor interval="300s" timeout="120s" \
          op start interval="0" timeout="60s" \
          params port="SECONDARY_INSTANCE_NAME" zone="SECONDARY_ZONE" \
          project="PROJECT_ID" \
          pcmk_reboot_timeout=300 pcmk_monitor_retries=4

  7. Set the location constraints:
         
         crm configure location FENCING_LOCATION_NAME_PRIMARY \
          FENCING_RESOURCE_PRIMARY -inf: "PRIMARY_INSTANCE_NAME"
         
         crm configure location FENCING_LOCATION_NAME_SECONDARY \
          FENCING_RESOURCE_SECONDARY -inf: "SECONDARY_INSTANCE_NAME"
         

  8. Take the cluster out of maintenance mode: 
         
         crm configure property maintenance-mode=false

  9. Check the configuration:
         
         crm config show related:FENCING_RESOURCE_PRIMARY
         

  10. Check the cluster status:
         
         # crm status | grep fence_gce
           STONITH-hana-vm1   (stonith:fence_gce):   Started hana-vm2
           STONITH-hana-vm2   (stonith:fence_gce):   Started hana-vm1
         




## Resource agent is stopped

A resource agent has failed to start and remains in the `Stopped` status.

### Issue

In your Linux Pacemaker high-availability cluster for SAP HANA or SAP NetWeaver, a resource agent has reported an error in the cluster status. For example:
    
    
    Failed Resource Actions:
       rsc_SAPHana_DV0_HDB00_start_0 on ha-node-02 'error' (1): call=91, status='complete', last-rc-change='Wed Oct 18 18:00:31 2023', queued=0ms, exec=19010ms

### Diagnosis

If a running resource agent fails, then Pacemaker attempts to stop the agent and start it again. If the start operation fails for any reason, then Pacemaker sets the resource failcount to `INFINITY` and attempts to start the agent on another node. If the resource agent fails to start on any node, then the resource agent remains in the `Stopped` status.

To check the resource agent status, run the following command:

###  RHEL 
    
    
    pcs status

###  SLES 
    
    
    crm status

For SAP HANA, the following example shows the resource agent in the `Stopped` status on the node `hana-b`:
    
    
    Full List of Resources:
      * STONITH-hana-a        (stonith:fence_gce):   Started hana-b
      * STONITH-hana-b        (stonith:fence_gce):   Started hana-a
      * Resource Group: g-primary:
        * rsc_vip_int-primary       (ocf::heartbeat:IPaddr2):        Started hana-a
        * rsc_vip_hc-primary        (ocf::heartbeat:anything):       Started hana-a
      * Clone Set: cln_SAPHanaTopology_DV0_HDB00 [rsc_SAPHanaTopology_DV0_HDB00]:
        * Started: [ hana-a hana-b ]
      * Clone Set: msl_SAPHana_DV0_HDB00 [rsc_SAPHana_DV0_HDB00] (promotable):
        * Masters: [ hana-a ]
        * Stopped: [ hana-b ]
      * STONITH-scaleup-majority    (stonith:fence_gce):   Started hana-b
    

### Solution

If a resource agent is in the `Stopped` status, then do the following:

  1. Manually start the resource agent by resetting the failcount:

###  RHEL 
         
         pcs resource cleanup RESOURCE_AGENT_NAME

###  SLES 
         
         crm resource cleanup RESOURCE_AGENT_NAME

Replace `RESOURCE_AGENT_NAME` with the name of the resource agent. For example `rsc_SAPHana_DV0_HDB00`.

  2. Ensure that the status of the resource agent reaches status `Started`: 
         
         crm_mon

If the resource agent still fails to start, then gather the [relevant diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-gather-diagnostic-info) and contact support.




## Communication failure between VMs due to local network routes for virtual IPs

Network traffic from one backend VM to another VM fails because of local network routes for virtual IPs.

### Issue

When VMs are a part of an internal passthrough Network Load Balancer, backend network communication to the ILB virtual IP (VIP) routes as being local and is handled by the loopback device.

This loopback behavior prevents a backend VM from successfully using the ILB's VIP to reach services potentially hosted on other backend VMs using the ILB, resulting in a communication failure.

For example: Communication failure between ASCS and ERS in a SAP Netweaver HA cluster configured as a load balancer backend.

The `telnet` test results in a `Connection Refused` error because this local routing wouldn't allow the traffic to reach the intended VM:
    
    
       [root@test-server-ha ~]# telnet IP_ADDRESS_OF_ILB PORT_NUMBER
       Trying IP_ADDRESS_OF_ILB...
       telnet: connect to address IP_ADDRESS_OF_ILB: Connection refused
    

### Diagnosis

Prerequisite:

Impacted VMs are listed as members of an unmanaged instance group which are configured as a load balancer backend.

When a backend VM within an Internal Load Balancer (ILB) initiates communication to the ILB's Virtual IP (VIP), a specific routing behavior occurs.

Although the VIP is configured on a standard network interface like `eth0` and listed in the local routing table, the kernel routes packets destined for this local VIP using the loopback interface `lo`. This internal loopback means the packet never leaves the originating VM to be processed by the ILB.

While direct communication between backend VMs using their individual IPs works, this loopback behavior prevents a backend VM from successfully using the ILB's VIP to reach services potentially hosted on other backend VMs using the internal passthrough Network Load Balancer.
    
    
       [root@test-server-ha ~]# ip route show table local
       local IP_ADDRESS_OF_ILB dev eth0 proto 66 kernel scope host src IP_ADDRESS_OF_ILB
       local IP_ADDRESS_OF_THE_CURRENT_NODE dev eth0 proto kernel scope host src IP_ADDRESS_OF_THE_CURRENT_NODE
       local IP_ADDRESS_OF_THE_OTHER_NODE dev eth0 proto kernel scope host src IP_ADDRESS_OF_THE_OTHER_NODE
       broadcast IP_ADDRESS dev lo proto kernel scope link src IP_ADDRESS
       local IP_ADDRESS dev lo proto kernel scope host src IP_ADDRESS
       broadcast IP_ADDRESS dev lo proto kernel scope link src IP_ADDRESS
    
    
    
       ip route get IP_ADDRESS_OF_ILB
    

Output of this command shows a loopback interface `lo`:
    
    
       [root@test-server-ha ~]# ip route get IP_ADDRESS_OF_ILB
       local IP_ADDRESS_OF_ILB dev lo src IP_ADDRESS_OF_ILB uid 0
       cache <local>
    

### Solution

Enable backend communication between the VMs by modifying the configuration of the google-guest-agent, which is included in the [Linux guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) for all Linux public images that are provided by Google Cloud.

To enable load balancer backend communications, perform the following steps on each VM that is a part of your cluster,

  1. Stop the agent:
         
         sudo service google-guest-agent stop
         

  2. Open or create the file `/etc/default/instance_configs.cfg` for editing:
         
         sudo vi /etc/default/instance_configs.cfg
         

  3. In the `/etc/default/instance_configs.cfg` file, specify the following configuration properties as shown. If the sections don't exist, create them. In particular, make sure that both the `target_instance_ips` and `ip_forwarding` properties are set to false:
         
         [IpForwarding]
         ethernet_proto_id = 66
         ip_aliases = true
         target_instance_ips = false
         
         [NetworkInterfaces]
         dhclient_script = /sbin/google-dhclient-script
         dhcp_command =
         ip_forwarding = false
         setup = true
         

  4. Start the guest agent service:
         
         sudo service google-guest-agent start
         




#### To apply the changes either perform a VM restart or the following steps to delete the local route

  1. Delete the local route that is sending traffic back:
         
         sudo ip route del table local $(ip route show table local | grep "proto 66" | awk '{print $2}') dev eth0
         

The preceding command is a sequence of Linux commands piped together to delete the VIP from the local routing table. Breaking each of these down:

We identify the IP address using,
         
         ip route show table local | grep "proto 66" | awk '{print $2}'
         

Then pipe it into the actual delete command:
         
         ip route del table local
         

  2. Restart the google guest agent:

     * For guest agent version `20250901.00` or later, run the following command:
           
           ggactl_plugin coreplugin restart
           

     * For earlier guest agent versions, run the following command:
           
           systemctl google-guest-agent restart
           




This change is non-disruptive. Restarting the `google-guest-agent` re-creates a new network route that instructs network traffic to use `eth0` instead of the loopback device to send traffic to the VIP.

#### To verify the changes,
    
    
       ip route get IP_ADDRESS_OF_ILB
    

Output of this command must show network interface like `eth0` and not loopback interface `lo`:
    
    
       [root@test-server-ha ~]# ip route get IP_ADDRESS_OF_ILB
       IP_ADDRESS_OF_ILB via IP_ADDRESS_OF_ILB dev eth0 src IP_ADDRESS_OF_ILB uid 0
       cache
    

Attempt the `telnet` test:
    
    
       [root@test-server-ha ~]# telnet IP_ADDRESS_OF_ILB PORT_NUMBER
       Trying IP_ADDRESS_OF_ILB...
       Connected to IP_ADDRESS_OF_ILB.
       Escape character is '^]'.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
