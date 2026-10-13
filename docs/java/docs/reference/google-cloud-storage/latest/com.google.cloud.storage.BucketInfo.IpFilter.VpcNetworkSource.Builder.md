---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IpFilter.VpcNetworkSource.Builder
title: Class BucketInfo.IpFilter.VpcNetworkSource.Builder (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:26.076218+00:00
---

# Class BucketInfo.IpFilter.VpcNetworkSource.Builder (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IpFilter.VpcNetworkSource.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BucketInfo.IpFilter.VpcNetworkSource.Builder (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public static final class BucketInfo.IpFilter.VpcNetworkSource.Builder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BucketInfo.IpFilter.VpcNetworkSource.Builder

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### Builder(BucketInfo.IpFilter.VpcNetworkSource vpcNetworksource)
    
    
    public Builder(BucketInfo.IpFilter.VpcNetworkSource vpcNetworksource)

**Parameter**  
---  
**Name** | **Description**  
`vpcNetworksource` | `[BucketInfo.IpFilter.VpcNetworkSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IpFilter.VpcNetworkSource)`  
  
  
## Methods 

### build()
    
    
    public BucketInfo.IpFilter.VpcNetworkSource build()

**Returns**  
---  
**Type** | **Description**  
`[BucketInfo.IpFilter.VpcNetworkSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IpFilter.VpcNetworkSource)` |   
  
### setAllowedIpCidrRanges(@Nullable List<String> allowedIpCidrRanges)
    
    
    public BucketInfo.IpFilter.VpcNetworkSource.Builder setAllowedIpCidrRanges(@Nullable List<String> allowedIpCidrRanges)

Optional. The list of public or private IPv4 and IPv6 CIDR ranges that can access the bucket. In the CIDR IP address block, the specified IP address must be properly truncated, meaning all the host bits must be zero or else the input is considered malformed. For example, `192.0.2.0/24` is accepted but `192.0.2.1/24` is not. Similarly, for IPv6, `2001:db8::/32` is accepted whereas `2001:db8::1/32` is not. See Also: VpcNetworkSource#getAllowedIpCidrRanges()

**Parameter**  
---  
**Name** | **Description**  
`allowedIpCidrRanges` | `@org.checkerframework.checker.nullness.qual.Nullable java.util.List<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[BucketInfo.IpFilter.VpcNetworkSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IpFilter.VpcNetworkSource.Builder)` |   
  
### setNetwork(@Nullable String network)
    
    
    public BucketInfo.IpFilter.VpcNetworkSource.Builder setNetwork(@Nullable String network)

Name of the network.

Format: `projects/PROJECT_ID/global/networks/NETWORK_NAME` See Also: VpcNetworkSource#getNetwork()

**Parameter**  
---  
**Name** | **Description**  
`network` | `@org.checkerframework.checker.nullness.qual.Nullable java.lang.String`  
  
**Returns**  
---  
**Type** | **Description**  
`[BucketInfo.IpFilter.VpcNetworkSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IpFilter.VpcNetworkSource.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
