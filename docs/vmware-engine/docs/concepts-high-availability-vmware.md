---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware/
title: Availability and redundancy \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:05.348237+00:00
---

# Availability and redundancy  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Availability and redundancy

Google Cloud VMware Engine provides availability for your applications running on VMware in your private cloud environment. The following table lists failure scenarios and the associated availability features that help protect your applications.

Failure scenario | Application protected? | VMware Engine HA feature | VMware HA feature | Google Cloud feature  
---|---|---|---|---  
Disk failure | Yes | Fast replacement of failed node | [About the vSAN Default Storage Policy](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.virtualsan.doc/GUID-C228168F-6807-4C2A-9D74-E584CAF49A2A.html) | N/A  
Fan failure | Yes | Redundant fans, fast replacement of failed node | N/A | N/A  
NIC failure | Yes | Redundant NIC, fast replacement of failed node | N/A | N/A  
Host power failure | Yes | Redundant power supply | N/A | N/A  
ESXi host failure | Yes | Fast replacement of failed node | [VMware vSphere High Availability](https://www.vmware.com/products/vsphere/high-availability.html) | N/A  
VM failure | Yes | N/A | [VMware vSphere High Availability](https://www.vmware.com/products/vsphere/high-availability.html) | Load balancer for stateless VMware VMs  
Leaf switch port failure | Yes | Redundant NIC | N/A | N/A  
Leaf switch failure | Yes | Redundant leaf switches | N/A | N/A  
Rack failure | Yes | Placement groups | N/A | N/A  
Network connectivity to on-premises | Yes | Redundant networking services | N/A | Redundant Dedicated Interconnect and Partner Interconnect circuits  
Network connectivity | Yes | N/A | N/A | Redundant Dedicated Interconnect and Partner Interconnect circuits  
Regional failure | Yes | N/A | N/A | Hosting regions  
  
## Availability features

The following sections describe availability features.

### Fast replacement of a failed node

VMware Engine continuously monitors the health of VMware clusters. When VMware Engine detects an ESXi node failure, it adds a new ESXi host to the affected VMware cluster from its pool of readily available nodes and removes the failed node from the cluster. This feature quickly restores the spare capacity in the VMware cluster, supporting the cluster's resiliency provided by vSAN and VMware vSphere High Availability (HA).

### VMware Engine zones

A VMware Engine zone is a logical collection of VMware resources that are mapped to a Google Cloud zone. Sometimes zones are physically co-located and might be impacted by zonal infrastructure failures.

If you require applications to remain operational during a VMware Engine zone failure, we recommend that you distribute redundant resources across different zones so you can safeguard your applications and data from potential data center failures. To do this, we recommend you deploy multiple [private clouds](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud) or a [stretched private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-stretched-private-cloud).

When zone separation is enabled, VMware Engine zones are mapped to the same Google Cloud zones, with the following exceptions:

VMware Engine zone | Google Cloud zone  
---|---  
australia-southeast1-a | australia-southeast1-b†  
australia-southeast1-b | australia-southeast1-c†  
europe-west2-a | europe-west2-c†  
europe-west2-b | europe-west2-a†  
europe-west3-a | europe-west3-b†  
europe-west3-b | europe-west3-a†  
us-east4-a | us-east4-b†  
us-east4-b | us-east4-a†  
  
†When using zone separation.

### Dedicated Interconnect locations

When designing [on-premises to VMware Engine connectivity](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises), the following [Dedicated Interconnect locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities) correlate to the same VMware Engine zone.

Communication from a specific VMware Engine zone to a Google Cloud or Dedicated Interconnect location relies on the Interconnect service for non-critical applications. For more information, see the [Cloud Dedicated and Partner Interconnect Service Level Agreement (SLA)](https://cloud.google.com/network-connectivity/docs/interconnect/sla).

VMware Engine zone | Dedicated Interconnect locations  
---|---  
asia-northeast1-a | [AT Tokyo CC2](https://www.peeringdb.com/fac/738) (nrt-zone1-738, nrt-zone2-738)  
asia-south1-a | [Equinix MB1 - Mumbai (GPX Mumbai 1)](https://www.peeringdb.com/fac/2310) (bom-zone1-2310, bom-zone2-2310)  
asia-south2-a | [Sify Greenfort - Noida](https://www.peeringdb.com/fac/2411) (del-zone1-2411, del-zone2-2411)  
australia-southeast1-a | [NEXTDC S1](https://www.peeringdb.com/fac/1660) (syd-zone1-1660, syd-zone2-1660)  
europe-west12-a | Telecom Italia Cebrosa Campus (trn-zone1-99032, trn-zone2-99032)  
europe-west2-a | [Equinix London Slough (LD5)](https://www.peeringdb.com/fac/832) (lhr-zone1-832, lhr-zone2-832)   
[Equinix London Slough (LD6)](https://www.peeringdb.com/fac/2262) (lhr-zone1-2262, lhr-zone2-2262)  
europe-west3-a | [Digital Realty Frankfurt FRA1-16](https://www.peeringdb.com/fac/58) (fra-zone1-58, fra-zone2-58)  
europe-west3-b | [e-shelter Frankfurt (FRA1)](https://www.peeringdb.com/fac/277) (fra-zone1-277, fra-zone2-277)  
europe-west6-a | [greenDatacenter Lupfig](https://www.peeringdb.com/fac/1086) (zrh-zone1-1086, zrh-zone2-1086)  
europe-west8-a | [Telecom Italia Sparkle Milano Data Center](https://www.peeringdb.com/fac/6513) (mil-zone1-99013, mil-zone2-99013)  
northamerica-northeast1-a | [Cologix MTL10-H](https://www.peeringdb.com/fac/11631) (yul-zone1-99002, yul-zone2-99002)  
northamerica-northeast2-a | [Equinix Toronto (TR2)](https://www.peeringdb.com/fac/2206) (yyz-zone1-2206, yyz-zone2-2206)  
southamerica-east1-a | [Ascenty - Sao Paulo 2](https://www.peeringdb.com/fac/7580) (gru-zone1-7580, gru-zone2-7580)  
southamerica-west1-a | [GTD Panamericana](https://www.peeringdb.com/fac/12865) (scl-zone2-99014, scl-zone2-99014)  
us-east4-a | [Equinix DC1-DC15, DC21 - Ashburn](https://www.peeringdb.com/fac/1) (iad-zone1-1, iad-zone2-1)  
us-west2-a | [Digital Realty LAX (600 West 7th)](https://www.peeringdb.com/fac/403) (lax-zone1-403, lax-zone2-403)   
[CoreSite - LA1 - One Wilshire](https://www.peeringdb.com/fac/19) (lax-zone1-19, lax-zone2-19)  
  
### Redundant networking services

All Google networking services for the private cloud (including firewall, public IP addresses, internet, Dedicated Interconnect, Partner Interconnect, and Cloud VPN) are highly available and support the SLA.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
