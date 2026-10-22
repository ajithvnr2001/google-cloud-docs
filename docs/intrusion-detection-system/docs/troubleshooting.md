---
url: https://docs.cloud.google.com/intrusion-detection-system/docs/troubleshooting/
title: Troubleshoot endpoints and inspection \u00a0|\u00a0 Cloud Intrusion Detection System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:30.501328+00:00
---

# Troubleshoot endpoints and inspection  |  Cloud Intrusion Detection System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/intrusion-detection-system/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud IDS ](https://docs.cloud.google.com/intrusion-detection-system/docs)
  * [ Guides ](https://docs.cloud.google.com/intrusion-detection-system/docs/overview)



Send feedback 

#  Troubleshoot endpoints and inspection Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to diagnose and resolve issues when a Cloud Intrusion Detection System (Cloud IDS) endpoint doesn't generate security alerts.

## Endpoint is not generating alerts

**Note:** If your endpoint generates any alerts, it is considered to be functional.

To confirm that an IDS endpoint is functional, complete the tasks in the following sections.

### Verify the endpoint configuration

To verify the endpoint configuration, do the following:

  1. Verify that the IDS endpoint appears in the Cloud IDS Google Cloud console, and that there is a packet mirroring policy in the `Attached Policies` column.
  2. Ensure that the attached policy is enabled by clicking the policy name, and make sure that `Policy Enforcement` is set to **Enabled**.
  3. Ensure that the same traffic (or VM) is not affected by more than one packet mirroring policy, as each packet can be mirrored to only one destination. Check the `Attached Policies` column, and ensure that there is only one policy per VM.



### Confirm that your VPC network mirrors traffic

To confirm that your VPC network mirrors traffic, do the following:

  1. Choose a VM Instance in the monitored VPC, go to the **Observability** tab, and make sure that the `Mirrored Bytes` dashboard shows traffic being mirrored to the IDS endpoint.



### Generate test alerts to verify threat detection

To generate test alerts to verify threat detection, do the following: 1\. Use SSH to connect to a VM in the monitored network, then run the following command:
    
    
       curl http://example.com/cgi-bin/../../../..//bin/cat%%20/etc/passwd
       

If curl is unavailable on the platform, you can use a similar tool for performing HTTP requests.

After a few seconds, an alert should show up in both the Cloud IDS UI and in Cloud Logging (Threat Log).

## Decrypting traffic for inspection

To inspect traffic, Cloud IDS uses Packet Mirroring to send packet-level copies of configured traffic to the IDS VM. Even though the collector destination receives all mirrored packets, any packets that carry data that was encrypted using a secure protocol like TLS, HTTPS, or HTTP2 can't be decrypted by Cloud IDS.

For example, if you use HTTPS or HTTP2 as the backend service protocol for an external application load balancer, packets sent to the load balancer's backends can be mirrored to Cloud IDS; however, the requests cannot be inspected by Cloud IDS because the packets carry encrypted data. To enable Cloud IDS inspection, you must change the backend service protocol to HTTP. Alternatively, you can use [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) for intrusion prevention, and enable application load balancer logs for request inspection. For more information about application load balancer request logging, see [Global external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#logging) and [Regional external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring#logging).

## Only a small volume of traffic is inspected

Cloud IDS inspects traffic sent to or received by resources in mirrored subnets, including Google Cloud VMs and GKE nodes and Pods.

If a mirrored subnet contains no VMs, Cloud IDS has no traffic to inspect.

## Endpoint policies are ignored when using Cloud NGFW L7 inspection policies

When you use Cloud Next Generation Firewall L7 inspection policies (rules with the `apply_security_profile_group` action) and Cloud IDS together, firewall policy rules are evaluated and traffic is not mirrored for Cloud IDS inspection. You can avoid this situation by ensuring that Cloud NGFW L7 inspection policies don't apply to packets that you need to inspect with Cloud IDS.

## Cannot disable the Cloud IDS API

You can't disable the Cloud IDS API if you have any IDS endpoints configured. To disable the API, you must first [delete all IDS endpoints](https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids#delete-ids-endpoint).

## Mismatch between mirrored VM traffic and VM network metrics

When you monitor Compute Engine network metrics for a Virtual Machine (VM) instance whose traffic is mirrored to Cloud IDS, you might notice that the value of [`mirrored_bytes_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) is slightly higher than the sum of [`sent_bytes_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) and [`received_bytes_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute). This difference is expected because `sent_bytes_count` and `received_bytes_count` don't include ethernet headers, but `mirrored_bytes_count` does.

**Note:** Cloud IDS also has a [`received_bytes_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-ids) metric. This metric measures bytes received by the Cloud IDS endpoint, whereas the Compute Engine metric [`received_bytes_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) measures bytes received by a specific VM instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
