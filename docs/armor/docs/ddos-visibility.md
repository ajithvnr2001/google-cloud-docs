---
url: https://docs.cloud.google.com/armor/docs/ddos-visibility/
title: Access DDoS attack visibility telemetry \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:20.569971+00:00
---

# Access DDoS attack visibility telemetry  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/ddos-visibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Access DDoS attack visibility telemetry Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor Enterprise lets you use Cloud Logging and Cloud Monitoring to analyze DDoS attacks and their sources.

Google Cloud Armor automatically detects and mitigates network layer (Layer 3) and transportation layer (Layer 4) attacks, performing the mitigation before enforcing security policies and evaluating only well-formed requests against your security policy rules. Therefore, traffic dropped as a result of always-on DDoS protection does not appear in telemetry for security policies or backends.

Instead, the Cloud Logging and Cloud Monitoring metrics for DDoS mitigation events are part of DDoS attack visibility, a feature available exclusively for [Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview) subscribers. The following sections explain how to use Logging and Monitoring to analyze DDoS attacks and their sources. DDoS attack visibility is available for the following load balancer types:

  * Global external Application Load Balancer
  * Classic Application Load Balancer



If you use [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project), you can only view the telemetry and logging associated with DDoS attack visibility under the host or service project that includes your load balancer's frontend and URL map. You cannot view the telemetry and logging under the service project that includes the backend services.

In order to ensure proper logging and reporting, Cloud Armor requires access to the following logs. These must be stored in Cloud Logging, or routed to a [logging bucket](https://docs.cloud.google.com/logging/docs/buckets) which Cloud Armor can access.

  * `networksecurity.googleapis.com/dos_attack`
  * `networksecurity.googleapis.com/network_dos_attack`
  * `networksecurity.googleapis.com/network_dos_attack_mitigations`



## Cloud Logging attack mitigation event logs

Cloud Armor generates three types of event log entries when mitigating DDoS attacks. The log formats include analyses of client IP addresses and geographies when possible. The following sections provide examples of the log format for each type of event log:

### Mitigation started
    
    
       {
          "id": "20220101_1235_mitigation_1.2.3.4",
          "mitigationType": "MITIGATION_STARTED",
          "targetVip": "1.2.3.4",
          "totalVolume": {
             "pps": "1234000",
             "bps": "9876000000"
          },
          "started": {
             "totalAttackVolume": {
                "pps": "1000000",
                "bps": "9000000000"
          },
          "topSourceIp": [
             {
                "ipAddress": "1.2.3.4",
                "volume": {
                "pps": "10000",
                "bps": "2000000"
                }
             },
             {
                "ipAddress": "2.3.4.5",
                "volume": {
                "pps": "5000",
                "bps": "1000000"
                }
             }
          ],
          "topSourceGeo": [
             {
                "geo": "US",
                "volume": {
                "pps": "100000",
                "bps": "20000000"
                }
             }
          ]
          }
       }
       

### Mitigation ongoing
    
    
       {
          "id": "20220101_1235_mitigation_1.2.3.4",
          "mitigationType": "MITIGATION_ONGOING",
          "targetVip": "1.2.3.4",
          "totalVolume": {
             "pps": "1234000",
             "bps": "9876000000"
          },
          "ongoing": {
             "totalAttackVolume": {
                "pps": "1000000",
                "bps": "9000000000"
             },
             "topSourceIp": [
             {
                "ipAddress": "1.2.3.4",
                "volume": {
                   "pps": "10000",
                   "bps": "2000000"
                }
             },
             {
                "ipAddress": "2.3.4.5",
                "volume": {
                   "pps": "5000",
                   "bps": "1000000"
                }
             }
          ],
          "topSourceGeo": [
             {
                "geo": "US",
                "volume": {
                   "pps": "100000",
                   "bps": "20000000"
                }
             }
          ]
          }
       }
       

### Mitigation ended
    
    
       {
          "id": "20220101_1235_mitigation_1.2.3.4",
          "mitigationType": "MITIGATION_ENDED",
          "targetVip": "1.2.3.4",
          "totalVolume": {
             "pps": "2314000",
             "bps": "9768000000"
          },
          "ended": {
             "attackDurationSeconds": 345
          }
       }
       

In the Google Cloud console, go to the Logs Explorer page and view the `ProtectedEndpoint` resource.

**Note:** The `topSourceIp` field might not be populated.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query;query=resource.type%3D%22networksecurity.googleapis.com%2FProtectedEndpoint%22)

Alternatively, you can view the `network_dos_attack_mitigations` log name.

## Cloud Monitoring metrics

DDoS mitigation telemetry metrics are visible under the resource **Protected Network Endpoint** (`ProtectedEndpoint`), which is exclusive to application-layer (Layer 7) virtual IP addresses that are enrolled in Cloud Armor Enterprise. The available metrics are as follows:

  * Ingress bytes (`/dos/ingress_bytes`)
  * Ingress packets (`/dos/ingress_packets`)



You can group and filter the preceding metrics based upon the following labels:

Label | Value  
---|---  
`project_id` | The ID of your project that is enrolled in Cloud Armor Enterprise.  
`location` | The location of your protected endpoint.  
`vip` | The virtual IP address of the protected endpoint.  
`drop_status` | Possible values: 

  * `processed`: Traffic was not denied by Cloud Armor always-on DDoS protection, meaning that it was evaluated against your security policies.
  * `blocked`: Traffic was denied by Cloud Armor always-on DDoS protection and dropped before being evaluated against your security policies.

  
  
In the Google Cloud console, go to the Metrics Explorer page.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

### Interpreting telemetry metrics for virtual IP addresses with low traffic volumes

For virtual IP addresses (VIPs) that receive fewer than 100,000 packets per second, we recommend that you use a longer time window to view metrics in Cloud Monitoring. For example, where a higher-traffic VIP might use an `ALIGN_RATE` of one minute, we instead recommend an `ALIGN_RATE` of 10 minutes. Using a longer time window helps reduce the volume of artifacts that result from a poor signal-to-noise ratio.

In addition, some components of the rate at which Cloud Armor drops traffic (the drop rate) are inferred by statistical means, and might be less accurate for low-traffic VIPs. This means that during a DDoS attack, the drop rate that Cloud Monitoring reports might be slightly lower than the true drop rate. This reduces statistical artifacts that can lead to an overestimation of the volume of dropped traffic, especially for VIPs that receive a low volume of traffic and are not under attack.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
