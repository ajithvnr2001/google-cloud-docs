---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/monitoring-metrics/
title: Monitoring metrics \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:53.488188+00:00
---

# Monitoring metrics  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/monitoring-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ APIs and reference ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/apis)



#  Monitoring metrics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Network Insights exports monitoring metrics to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). Use these metrics with your [dashboards](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/view-dashboards) to keep track of what's happening in your network.

All metrics collected by the Monitoring Points are exported to Cloud Monitoring API and retained there according to the [Cloud Monitoring data retention policy](https://cloud.google.com/monitoring/quotas#data_retention_policy).

## Metric prefixes and path types

Metrics have different prefixes depending on the path type.

  * **Single-Ended Paths** : These are round-trip measurements where traffic is sent from a source Monitoring Point to a target and then returns to the source. Metrics for single-ended paths use the `total` prefix to represent the total for both the inbound and outbound parts of the journey.
  * **Dual-Ended Paths** : These paths have Monitoring Points at both ends of the connection, which allows for separate, one-way measurements of the inbound and outbound legs of the journey. 
    * Metrics with the `out` prefix relate to the outbound direction (from the Monitoring Point to the Target).
    * Metrics with the `in` prefix relate to the inbound direction (from the target to the Monitoring Point).
  * **No Prefix** : Some metrics have no prefix, which indicates that they have no specific directionality. These typically represent an overall state or a measurement of the entire round trip.



## Network path metrics

You can filter network path metrics by using the `networkmanagement.googleapis.com/insights/network/` prefix or the `networkmanagement.googleapis.com/NetworkPath` resource type.

**Metric** | **Description**  
---|---  
`data/in/packets_received_count` | The number of tracked data probes received in a measurement interval (dual-ended, inbound).  
`data/out/packets_received_count` | The number of tracked data probes received in a measurement interval (dual-ended, outbound).  
`data/total/packets_received_count` | The number of tracked data probes received in a measurement interval (single-ended).  
`data/in/packets_sent_count` | The number of tracked data probes sent in a measurement interval (dual-ended, inbound).  
`data/out/packets_sent_count` | The number of tracked data probes sent in a measurement interval (dual-ended, outbound).  
`data/total/packets_sent_count` | The number of tracked data probes sent in a measurement interval (single-ended).  
`in/jitter` | This is the packet delay variation in milliseconds (ms) for probes in a measurement interval (dual-ended, inbound), calculated from multiple latency measurements.  
`out/jitter` | This is the packet delay variation in milliseconds (ms) for probes in a measurement interval (dual-ended, outbound), calculated from multiple latency measurements.  
`total/jitter` | This is the packet delay variation in milliseconds (ms) for probes in a measurement interval (single-ended), calculated from multiple latency measurements.  
`in/loss_percent` | Measures the percentage of packet loss for the network test (dual-ended, inbound). Calculated from packets_sent and packets_received counts.  
`out/loss_percent` | Measures the percentage of packet loss for the network test (dual-ended, outbound). Calculated from packets_sent and packets_received counts.  
`total/loss_percent` | Measures the percentage of packet loss for the network test (single-ended). Calculated from packets_sent and packets_received counts.  
`rtt_avg` | Represents the average round-trip time in milliseconds (ms) for all tracked data and voice probes in a measurement interval.  
`rtt_max` | Represents the maximum round-trip time in milliseconds (ms) for all tracked data and voice probes in a measurement interval.  
`rtt_min` | Represents the minimum round-trip time in milliseconds (ms) for all tracked data and voice probes in a measurement interval.  
`test_error` | The primary indicator of whether the network test completed. A value of 0 means the test completed without error, while a value of 1 indicates that errors prevented the test from completing. `error_type` indicates what type of failure occurred. Data loss of 100% is considered a `Connect` error type. Any other amount of loss is not considered an error. See Network path error types for more information.  
`voice/in/mos` | The Mean Opinion Score (MOS) is an estimate of the sound quality of a call, measured on voice probes only (dual-ended, inbound). It is a function of loss, latency, and jitter.  
`voice/out/mos` | The Mean Opinion Score (MOS) is an estimate of the sound quality of a call, measured on voice probes only (dual-ended, outbound). It is a function of loss, latency, and jitter.  
`voice/total/mos` | The Mean Opinion Score (MOS) is an estimate of the sound quality of a call, measured on voice probes only (single-ended). It is a function of loss, latency, and jitter.  
`voice/in/packets_received_count` | The number of tracked voice probes received in a measurement interval (dual-ended, inbound).  
`voice/out/packets_received_count` | The number of tracked voice probes received in a measurement interval (dual-ended, outbound).  
`voice/total/packets_received_count` | The number of tracked voice probes received in a measurement interval (single-ended).  
`voice/in/packets_sent_count` | The number of tracked voice probes sent in a measurement interval (dual-ended, inbound).  
`voice/out/packets_sent_count` | The number of tracked voice probes sent in a measurement interval (dual-ended, outbound).  
`voice/total/packets_sent_count` | The number of tracked voice probes sent in a measurement interval (single-ended).  
  
### Network path error types

The following table describes the types of network test failures that can occur.

Error Type | Error Detail  
---|---  
DNS | Target IP couldn't be resolved.  
Connect | No response from the target.  
The target Monitoring Point refused to connect.  
`Port Unreachable` received in response to the handshake.  
`Port Unreachable` received after the handshake was completed.  
Local | No local interface match for the resolved target address family (IPv4 or IPv6).  
The Monitoring Point has an internal error.  
The network rules don't match any local interface.  
The Monitoring Point can't monitor loopback or local IP addresses.  
No local network interface is available for monitoring.  
Local interfaces were blocked for monitoring.  
Local interfaces didn't support QoS.  
The local interfaces' QoS resource is in use by another application.  
The local interfaces' QoS resource is in use by AppNeta.  
  
## Web path metrics

You can filter web path metrics by using the `networkmanagement.googleapis.com/insights/web/` prefix or the `networkmanagement.googleapis.com/WebPath` resource type.

**Metric** | **Description**  
---|---  
`browser/test_error` | Indicates if an error occurred during a browser-based web path test. A value of 0 means the test completed without errors, while a value of 1 indicates a failure, such as a Selenium script error. The `error_type` attribute provides more details on the failure. See Web path error types for more details.  
`http/download/size` | The number of bytes downloaded during a response to the first non-redirected HTTP request.  
`http/download/speed` | The total size of the downloaded content divided by the time taken to download for the first non-redirected request in bytes/second.  
`http/retransmission/in` | The inbound HTTP retransmission rate.  
`http/retransmission/out` | The percentage of packets that the client had to resend to the server. This is captured directly from the TCP/IP stack during the web transaction.  
`http/response_time/dns_lookup` | The time taken to resolve the IP address of the target domain for the first non-redirected request in milliseconds (ms).  
`http/response_time/redirect` | The time for a redirected request to arrive at the final server and for a response to be received in milliseconds (ms). This includes all aspects of a redirected request, such as DNS lookup, TCP/SSL connection establishment, the request itself, and the response time.  
`http/response_time/request_receive` | The time taken to download the entire content of the first HTTP response in milliseconds (ms).  
`http/response_time/request_wait` | The time from when the first non-redirected HTTP request is sent until the first byte of the response is received in milliseconds (ms).  
`http/response_time/ssl_connect` | The time taken to complete the SSL handshake for the first non-redirected request in milliseconds (ms).  
`http/response_time/tcp_connect` | The time taken to establish the TCP connection for the first non-redirected request in milliseconds (ms).  
`http/response_time/total` | The total response time for the first request of a web path in milliseconds (ms).  
`http/test_error` | Indicates if an error occurred during an HTTP web path test. A value of 0 means the test completed without errors, while a value of 1 indicates a failure. The `error_type` attribute provides more details on the failure. See Web path error types for more details.  
`total_transaction_time` | The total time taken to execute the entire workflow on a web path in milliseconds (ms).  
  
### Web path error types

The types of reported web path failures depends on whether you monitor your web application using browser-based scripts or HTTP requests.

Metric | Error type  
---|---  
`browser/test_error` | Script error at the reported milestone  
Other  
`http/test_error` | DNS Lookup  
Download  
Redirect  
Request Wait  
SSL Connect  
TCP Connect  
Unexpected response  
Other  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
