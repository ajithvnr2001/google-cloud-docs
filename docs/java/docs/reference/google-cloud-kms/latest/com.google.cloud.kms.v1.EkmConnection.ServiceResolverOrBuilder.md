---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.EkmConnection.ServiceResolverOrBuilder
title: Interface EkmConnection.ServiceResolverOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:18.596807+00:00
---

# Interface EkmConnection.ServiceResolverOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.EkmConnection.ServiceResolverOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EkmConnection.ServiceResolverOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.8  2.5.3  2.4.4  2.3.1 
    
    
    public static interface EkmConnection.ServiceResolverOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEndpointFilter()
    
    
    public abstract String getEndpointFilter()

Optional. The filter applied to the endpoints of the resolved service. If no filter is specified, all endpoints will be considered. An endpoint will be chosen arbitrarily from the filtered list for each request.

For endpoint filter syntax and examples, see <https://cloud.google.com/service-directory/docs/reference/rpc/google.cloud.servicedirectory.v1#resolveservicerequest>.

`string endpoint_filter = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The endpointFilter.  
  
### getEndpointFilterBytes()
    
    
    public abstract ByteString getEndpointFilterBytes()

Optional. The filter applied to the endpoints of the resolved service. If no filter is specified, all endpoints will be considered. An endpoint will be chosen arbitrarily from the filtered list for each request.

For endpoint filter syntax and examples, see <https://cloud.google.com/service-directory/docs/reference/rpc/google.cloud.servicedirectory.v1#resolveservicerequest>.

`string endpoint_filter = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for endpointFilter.  
  
### getHostname()
    
    
    public abstract String getHostname()

Required. The hostname of the EKM replica used at TLS and HTTP layers.

`string hostname = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hostname.  
  
### getHostnameBytes()
    
    
    public abstract ByteString getHostnameBytes()

Required. The hostname of the EKM replica used at TLS and HTTP layers.

`string hostname = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hostname.  
  
### getServerCertificates(int index)
    
    
    public abstract Certificate getServerCertificates(int index)

Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 Certificate is supported.

` repeated .google.cloud.kms.v1.Certificate server_certificates = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.Certificate)` |   
  
### getServerCertificatesCount()
    
    
    public abstract int getServerCertificatesCount()

Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 Certificate is supported.

` repeated .google.cloud.kms.v1.Certificate server_certificates = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getServerCertificatesList()
    
    
    public abstract List<Certificate> getServerCertificatesList()

Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 Certificate is supported.

` repeated .google.cloud.kms.v1.Certificate server_certificates = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.Certificate)>` |   
  
### getServerCertificatesOrBuilder(int index)
    
    
    public abstract CertificateOrBuilder getServerCertificatesOrBuilder(int index)

Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 Certificate is supported.

` repeated .google.cloud.kms.v1.Certificate server_certificates = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CertificateOrBuilder)` |   
  
### getServerCertificatesOrBuilderList()
    
    
    public abstract List<? extends CertificateOrBuilder> getServerCertificatesOrBuilderList()

Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 Certificate is supported.

` repeated .google.cloud.kms.v1.Certificate server_certificates = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.kms.v1.CertificateOrBuilder>` |   
  
### getServiceDirectoryService()
    
    
    public abstract String getServiceDirectoryService()

Required. The resource name of the Service Directory service pointing to an EKM replica, in the format `projects/*/locations/*/namespaces/*/services/*`.

` string service_directory_service = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceDirectoryService.  
  
### getServiceDirectoryServiceBytes()
    
    
    public abstract ByteString getServiceDirectoryServiceBytes()

Required. The resource name of the Service Directory service pointing to an EKM replica, in the format `projects/*/locations/*/namespaces/*/services/*`.

` string service_directory_service = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceDirectoryService.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
