---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalIPRangesConfigOrBuilder
title: Interface AdditionalIPRangesConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:54.535411+00:00
---

# Interface AdditionalIPRangesConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalIPRangesConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AdditionalIPRangesConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface AdditionalIPRangesConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPodIpv4RangeNames(int index)
    
    
    public abstract String getPodIpv4RangeNames(int index)

List of secondary ranges names within this subnetwork that can be used for pod IPs. Example1: gke-pod-range1 Example2: gke-pod-range1,gke-pod-range2

`repeated string pod_ipv4_range_names = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The podIpv4RangeNames at the given index.  
  
### getPodIpv4RangeNamesBytes(int index)
    
    
    public abstract ByteString getPodIpv4RangeNamesBytes(int index)

List of secondary ranges names within this subnetwork that can be used for pod IPs. Example1: gke-pod-range1 Example2: gke-pod-range1,gke-pod-range2

`repeated string pod_ipv4_range_names = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the podIpv4RangeNames at the given index.  
  
### getPodIpv4RangeNamesCount()
    
    
    public abstract int getPodIpv4RangeNamesCount()

List of secondary ranges names within this subnetwork that can be used for pod IPs. Example1: gke-pod-range1 Example2: gke-pod-range1,gke-pod-range2

`repeated string pod_ipv4_range_names = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of podIpv4RangeNames.  
  
### getPodIpv4RangeNamesList()
    
    
    public abstract List<String> getPodIpv4RangeNamesList()

List of secondary ranges names within this subnetwork that can be used for pod IPs. Example1: gke-pod-range1 Example2: gke-pod-range1,gke-pod-range2

`repeated string pod_ipv4_range_names = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the podIpv4RangeNames.  
  
### getStatus()
    
    
    public abstract AdditionalIPRangesConfig.Status getStatus()

Draining status of the additional subnet.

`.google.container.v1.AdditionalIPRangesConfig.Status status = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AdditionalIPRangesConfig.Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.AdditionalIPRangesConfig.Status)` | The status.  
  
### getStatusValue()
    
    
    public abstract int getStatusValue()

Draining status of the additional subnet.

`.google.container.v1.AdditionalIPRangesConfig.Status status = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for status.  
  
### getSubnetwork()
    
    
    public abstract String getSubnetwork()

Name of the subnetwork. This can be the full path of the subnetwork or just the name. Example1: my-subnet Example2: projects/gke-project/regions/us-central1/subnetworks/my-subnet

`string subnetwork = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetwork.  
  
### getSubnetworkBytes()
    
    
    public abstract ByteString getSubnetworkBytes()

Name of the subnetwork. This can be the full path of the subnetwork or just the name. Example1: my-subnet Example2: projects/gke-project/regions/us-central1/subnetworks/my-subnet

`string subnetwork = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subnetwork.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
