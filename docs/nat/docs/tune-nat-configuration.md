---
url: https://docs.cloud.google.com/nat/docs/tune-nat-configuration/
title: Tune NAT configuration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:40.882490+00:00
---

# Tune NAT configuration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/tune-nat-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tune NAT configuration

After you set up your Cloud NAT gateway configuration (either Public NAT or Private NAT), you can edit the configuration based on your requirements. This page lists the tasks that you can perform to tune your Cloud NAT configuration.

Editing configurations can be disruptive in nature and can cause existing network address translation (NAT) connections to drop. For more information about the impact of tuning Cloud NAT configurations, see Impact of tuning NAT configurations on existing NAT connections.

**Note:** The tasks that are listed in the following sections apply to both Public NAT and Private NAT gateways. For tuning Private NAT configurations, see [Limitations](https://docs.cloud.google.com/nat/docs/set-up-private-nat#limitation-set-up-pvt-nat).

## View port usage

Before you modify the minimum port usage per VM, review your per-VM port usage. You can get this information by using the [`compute.googleapis.com/nat/port_usage` metric](https://docs.cloud.google.com/nat/docs/monitoring#vm-metrics).

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

     1. In the navigation pane, select **Metrics Explorer** ![](https://docs.cloud.google.com/static/monitoring/images/tme.png).

     2. Expand the **Select a metric** menu, and use the submenus to choose the `compute.googleapis.com/nat/port_usage` metric:

        * For **Resource** , select **VM instance**.
        * For **Metric category** , select **Nat**.
        * For **Metric** , select **Port usage**.
     3. Click **Apply**.

     4. To select your Cloud NAT gateway, use the **Filters** field.

     5. In the **Group by** section, for **labels** , select **instance_id**.

     6. In the **Grouping function** list, select **Max**.

     7. Expand **More options** , and set the **Aligner** field to **max**.

     8. To see usage for the past 30 days, specify `30d`.

For more information about using Metrics Explorer, see [Select metrics when using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector#basic-advanced-mode).




## Choose a minimum number of ports per VM

Choosing an appropriate minimum number of ports is important to help you maximize NAT IP addresses usage.

Before you increase the number of ports per VM, consider other strategies for [reducing port usage](https://docs.cloud.google.com/nat/docs/troubleshooting#reduce-ports).

If you need to increase the number of ports per VM, start by considering the per-VM port usage in your gateway. For information about how to find this data, see View port usage.

Review your maximum port usage for the past 30 days, or for another period that you think is representative for your Cloud NAT gateway.

Do one of the following:

  * If you are using static port allocation, configure the number of ports per VM so that the minimum is equal to your current peak port usage.

  * If you are using dynamic port allocation, configure the number of ports per VM so that the minimum is lower than the peak port usage and the maximum is higher than the peak port usage.




## Change minimum default ports allocated per VM

For help deciding how to configure the minimum number of ports per VM, see Choose a minimum number of ports per VM.

For information about the consequences of changing the minimum port allocation, see the following sections:

  * [Increasing ports per VM](https://docs.cloud.google.com/nat/docs/ports-and-addresses#specs-increasing)
  * [Reducing ports per VM](https://docs.cloud.google.com/nat/docs/ports-and-addresses#specs-reducing)



If your Cloud NAT gateway has dynamic port allocation configured, see Change minimum or maximum ports when dynamic port allocation is configured.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Modify the **Minimum ports per VM instance** field.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

This command leaves the other fields in the Cloud NAT configuration unchanged.
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=ROUTER_NAME \
        --region=REGION \
        --min-ports-per-vm=128
    

Replace the following:

  * `NAT_CONFIG`: the name of your Cloud NAT configuration.
  * `ROUTER_NAME`: the name of your Cloud Router.
  * `REGION`: the region of the Cloud NAT to update. If not specified, you might be prompted to select a region (interactive mode only).



## Change the port allocation method

[Static port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#static-port) and [dynamic port allocation](https://docs.cloud.google.com/nat/docs/ports-and-addresses#dynamic-port) have different configuration requirements.

Before you update the port allocation type on an existing Cloud NAT gateway, make sure that the Cloud NAT gateway configuration is compatible with that port allocation type. If the configuration is not compatible, the change fails.

  * For dynamic port allocation, check that [endpoint-independent mapping (EIM)](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#set-mapping) is disabled.

  * Check that the minimum ports per VM setting is a power of 2, and is between 32 and 32,768.


**Note:** Changing the port allocation method can be disruptive in nature. For more information, see [Switch port allocation method](https://docs.cloud.google.com/nat/docs/ports-and-addresses#switch-port-allocation).

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Select or deselect **Enable Dynamic Port Allocation**.

  6. If needed, adjust the values for **Minimum ports per VM instance** and **Maximum ports per VM instance**.

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

This command leaves the other fields in the Cloud NAT configuration unchanged.
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=ROUTER_NAME \
        --region=REGION \
        --enable-dynamic-port-allocation | --no-enable-dynamic-port-allocation \
        [ --min-ports-per-vm=MIN_PORTS ] \
        [ --max-ports-per-vm=MAX_PORTS ]
    

Replace the following:

  * `NAT_CONFIG`: the name of your Cloud NAT configuration.
  * `ROUTER_NAME`: the name of your Cloud Router.
  * `REGION`: the region of the Cloud NAT to update. If not specified, you might be prompted to select a region (interactive mode only).
  * `MIN_PORTS`: the minimum number of ports to allocate for each VM. If dynamic port allocation is enabled, `MIN_PORTS` must be a power of `2`, and can be between `32` and `32768`.
  * `MAX_PORTS`: the maximum number of ports to allocate for each VM. `MAX_PORTS` must be a power of `2`, and can be between `64` and `65536`. `MAX_PORTS` must be greater than `MIN_PORTS`. The default is `65536`.



## Change minimum or maximum ports when dynamic port allocation is configured

After you have configured dynamic port allocation, you can change the minimum or maximum number of ports assigned per VM.

For help deciding how to configure the minimum number of ports per VM, see Choose a minimum number of ports per VM.

For information about the consequences of changing the minimum port allocation, see the following sections:

  * [Increasing ports per VM](https://docs.cloud.google.com/nat/docs/ports-and-addresses#specs-increasing)
  * [Reducing ports per VM](https://docs.cloud.google.com/nat/docs/ports-and-addresses#specs-reducing)




###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Adjust the **Minimum ports per VM instance** and **Maximum ports per VM instance** fields.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

This command leaves the other fields in the Cloud NAT configuration unchanged.
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=ROUTER_NAME \
        --region=REGION \
        --min-ports-per-vm=MIN_PORTS \
        --max-ports-per-vm=MAX_PORTS
    

Replace the following:

  * `NAT_CONFIG`: the name of your Cloud NAT configuration.
  * `ROUTER_NAME`: the name of your Cloud Router.
  * `REGION`: the region of the Cloud NAT to update. If not specified, you might be prompted to select a region (interactive mode only).
  * `MIN_PORTS`: the minimum number of ports to allocate for each VM. If dynamic port allocation is enabled, `MIN_PORTS` must be a power of `2`, and can be between `32` and `32768`.
  * `MAX_PORTS`: the maximum number of ports to allocate for each VM. `MAX_PORTS` must be a power of `2`, and can be between `64` and `65536`. `MAX_PORTS` must be greater than `MIN_PORTS`.



## Modify NAT timeouts

The following sections describe NAT timeouts and how to modify them:

  * NAT timeouts
  * Change NAT timeouts
  * Reset NAT timeouts to default values



### NAT timeouts

Cloud NAT uses the following timeouts. These timeouts apply to both Public NAT and Private NAT, except where noted. You can modify the default timeout values to decrease or increase the rate at which ports are reused. Each timeout value is a balance between efficient use of Cloud NAT resources and possible disruption to active connections, flows, or sessions.

Timeout processing has a variance of up to five seconds, meaning the actual expiration time might occur up to five seconds earlier or later than the configured timeout value. To avoid shortened timeouts, add five seconds to your intended configuration value.

Timeout | Description | Cloud NAT default | Configurable  
---|---|---|---  
UDP Mapping Idle Timeout [RFC 4787](https://tools.ietf.org/html/rfc4787) REQ-5 |  Specifies the time in seconds after which UDP flows must stop sending traffic to endpoints so that the Cloud NAT mappings are removed. UDP Mapping Idle Timeout affects two endpoints that stop sending traffic to each other. It also affects endpoints that take longer to respond, or if there is increased network latency. You can increase the specified timeout value to decrease the rate at which ports can be reused. The larger timeout value means that the ports are held for longer connections and also protects against pauses in traffic over a specific UDP socket. | 30 seconds | Yes  
TCP Established Connection Idle Timeout [RFC 5382](https://tools.ietf.org/html/rfc5382) REQ-5 |  Specifies the time in seconds that a connection is idle before the Cloud NAT mappings are removed. TCP Established Connection Idle Timeout affects endpoints that take longer to respond, or if there is increased network latency. You can increase the timeout value when you want to open TCP connections and keep the connections open for a long time without a keepalive mechanism in place. | 1200 seconds (20 minutes) | Yes  
TCP Transitory Connection Idle Timeout [RFC 5382](https://tools.ietf.org/html/rfc5382) REQ-5 |  Specifies the time in seconds that TCP connections can remain in the half-open state before the Cloud NAT mappings can be deleted. TCP Transitory Connection Idle Timeout affects an endpoint when an external endpoint takes a longer period than the specified time, or when there is increased network latency. Unlike the TCP Established Connection Idle Timeout, the TCP Transitory Connection Idle Timeout affects only half-open connections. |  30 seconds **Note:** Regardless of the value that you set for this timeout, Cloud NAT might require up to an additional 30 seconds before a Cloud NAT source IP address and source port tuple can be used to process a new connection. | Yes  
TCP TIME_WAIT Timeout [RFC 5382](https://tools.ietf.org/html/rfc5382) REQ-5 |  Specifies the time in seconds that a fully closed TCP connection is retained in the Cloud NAT mappings after the connection expires. TCP TIME_WAIT Timeout protects your internal endpoints from receiving invalid packets that belong to a closed TCP connection that are retransmitted. You can decrease the timeout value to improve the reuse of Cloud NAT ports at the cost of possibly receiving retransmitted packets from an unrelated, previously closed connection. For more information about this timeout, see [Delay for TCP source port reuse](https://docs.cloud.google.com/nat/docs/ports-and-addresses#ports-reuse-tcp). |  30 or 120 seconds1 **Note:** To avoid dropped packets, set this timeout to at least 15 seconds. Regardless of the value that you set for this timeout, Cloud NAT might require up to an additional 30 seconds before a Cloud NAT source IP address and source port tuple can be used to process a new connection. | Yes  
ICMP Mapping Idle Timeout  
(applicable to Public NAT only) [RFC 5508](https://tools.ietf.org/html/rfc5508) REQ-2 |  Specifies the time in seconds after which Internet Control Message Protocol (ICMP) Cloud NAT mappings that don't have any traffic flows are closed. ICMP Mapping Idle Timeout affects an endpoint when the endpoint takes a longer to respond than the specified time, or when there is increased network latency. | 30 seconds | Yes  
  
1 The default TCP TIME_WAIT timeout value depends on the creation date of your Cloud NAT gateway. For gateways that are created after [September 30, 2026](https://docs.cloud.google.com/nat/docs/release-notes#March_31_2026), the default value is 30 seconds. To see which default value is configured for your Cloud NAT gateway, run the [`gcloud compute routers nats describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe) command and locate the `effectiveTcpTimeWaitTimeoutSec` field in the output. If you modify the default value, this field shows your custom value. 

### Change NAT timeouts

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Modify any timeout values that you want to change.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update) with the following flags to change these timeout values:

  * UDP Mapping Idle Timeout: `--udp-idle-timeout`
  * TCP Established Connection Idle Timeout: `--tcp-established-idle-timeout`
  * TCP Transitory Connection Idle Timeout: `--tcp-transitory-idle-timeout`
  * TCP TIME_WAIT Timeout: `--tcp-time-wait-timeout`
  * ICMP Mapping Idle Timeout: `--icmp-idle-timeout`



This command leaves the other fields in the NAT configuration unchanged.

For example, the following command changes the UDP Mapping Idle Timeout value.
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=ROUTER_NAME \
        --region=REGION \
        --udp-idle-timeout=VALUE
    

Replace the following:

  * `NAT_CONFIG`: the name of your Cloud NAT configuration.
  * `ROUTER_NAME`: the name of your Cloud Router.
  * `REGION`: the region of the Cloud NAT to update. If not specified, you might be prompted to select a region (interactive mode only).
  * `VALUE`: the timeout value (in seconds)



### Reset NAT timeouts to default values

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. Remove any user-configured values that you want to reset.

  6. Click **Save**.




The removed values are reset to the default values.

###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

This command leaves the other fields in the Cloud NAT configuration unchanged.
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=ROUTER_NAME \
        --region=REGION \
        --clear-udp-idle-timeout \
        --clear-icmp-idle-timeout \
        --clear-tcp-established-idle-timeout \
        --clear-tcp-time-wait-timeout \
        --clear-tcp-transitory-idle-timeout
    

Replace the following:

  * `NAT_CONFIG`: the name of your Cloud NAT gateway.
  * `ROUTER_NAME`: the name of your Cloud Router.
  * `REGION`: the region of the Cloud NAT to update. If not specified, you might be prompted to select a region (interactive mode only).



## Impact of tuning NAT configurations on existing NAT connections

The following table summarizes the impact of tuning Cloud NAT configurations on existing connections.

Action | Dynamic port allocation | Connection drops  
---|---|---  
Enable dynamic port allocation | Disabled → enabled | No if both of the following conditions are true; **yes** if they aren't: 

  * The number of maximum ports per VM is greater than or equal to the previous number of minimum ports per VM.
  * The number of maximum ports per VM is greater than or equal to 1,024.

  
Disable dynamic port allocation | Enabled → disabled | **Yes**  
Increase minimum ports per VM | Enabled or disabled | No  
Decrease minimum ports per VM | Enabled | No  
Decrease minimum ports per VM | Disabled | **Yes**  
Increase maximum ports per VM | Enabled | No  
Decrease maximum ports per VM | Enabled | **Yes**  
Enable or disable endpoint-independent mapping | Disabled | No  
Change in Cloud NAT timeouts | Enabled or disabled | No  
  
## What's next

  * [Logs and metrics](https://docs.cloud.google.com/nat/docs/monitoring)
  * [Troubleshoot configuration](https://docs.cloud.google.com/nat/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
