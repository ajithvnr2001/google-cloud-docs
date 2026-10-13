---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.ReusableConfigValuesOrBuilder
title: Interface ReusableConfigValuesOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:21.425377+00:00
---

# Interface ReusableConfigValuesOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.ReusableConfigValuesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReusableConfigValuesOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.4  2.4.0  2.3.0  2.2.5 
    
    
    public interface ReusableConfigValuesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdditionalExtensions(int index)
    
    
    public abstract X509Extension getAdditionalExtensions(int index)

Optional. Describes custom X.509 extensions.

` repeated .google.cloud.security.privateca.v1beta1.X509Extension additional_extensions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[X509Extension](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.X509Extension)` |   
  
### getAdditionalExtensionsCount()
    
    
    public abstract int getAdditionalExtensionsCount()

Optional. Describes custom X.509 extensions.

` repeated .google.cloud.security.privateca.v1beta1.X509Extension additional_extensions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdditionalExtensionsList()
    
    
    public abstract List<X509Extension> getAdditionalExtensionsList()

Optional. Describes custom X.509 extensions.

` repeated .google.cloud.security.privateca.v1beta1.X509Extension additional_extensions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[X509Extension](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.X509Extension)>` |   
  
### getAdditionalExtensionsOrBuilder(int index)
    
    
    public abstract X509ExtensionOrBuilder getAdditionalExtensionsOrBuilder(int index)

Optional. Describes custom X.509 extensions.

` repeated .google.cloud.security.privateca.v1beta1.X509Extension additional_extensions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[X509ExtensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.X509ExtensionOrBuilder)` |   
  
### getAdditionalExtensionsOrBuilderList()
    
    
    public abstract List<? extends X509ExtensionOrBuilder> getAdditionalExtensionsOrBuilderList()

Optional. Describes custom X.509 extensions.

` repeated .google.cloud.security.privateca.v1beta1.X509Extension additional_extensions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.security.privateca.v1beta1.X509ExtensionOrBuilder>` |   
  
### getAiaOcspServers(int index)
    
    
    public abstract String getAiaOcspServers(int index)

Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.

`repeated string aia_ocsp_servers = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The aiaOcspServers at the given index.  
  
### getAiaOcspServersBytes(int index)
    
    
    public abstract ByteString getAiaOcspServersBytes(int index)

Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.

`repeated string aia_ocsp_servers = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the aiaOcspServers at the given index.  
  
### getAiaOcspServersCount()
    
    
    public abstract int getAiaOcspServersCount()

Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.

`repeated string aia_ocsp_servers = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of aiaOcspServers.  
  
### getAiaOcspServersList()
    
    
    public abstract List<String> getAiaOcspServersList()

Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.

`repeated string aia_ocsp_servers = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the aiaOcspServers.  
  
### getCaOptions()
    
    
    public abstract ReusableConfigValues.CaOptions getCaOptions()

Optional. Describes options in this ReusableConfigValues that are relevant in a CA certificate.

` .google.cloud.security.privateca.v1beta1.ReusableConfigValues.CaOptions ca_options = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReusableConfigValues.CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.ReusableConfigValues.CaOptions)` | The caOptions.  
  
### getCaOptionsOrBuilder()
    
    
    public abstract ReusableConfigValues.CaOptionsOrBuilder getCaOptionsOrBuilder()

Optional. Describes options in this ReusableConfigValues that are relevant in a CA certificate.

` .google.cloud.security.privateca.v1beta1.ReusableConfigValues.CaOptions ca_options = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReusableConfigValues.CaOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.ReusableConfigValues.CaOptionsOrBuilder)` |   
  
### getKeyUsage()
    
    
    public abstract KeyUsage getKeyUsage()

Optional. Indicates the intended use for keys that correspond to a certificate.

` .google.cloud.security.privateca.v1beta1.KeyUsage key_usage = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.KeyUsage)` | The keyUsage.  
  
### getKeyUsageOrBuilder()
    
    
    public abstract KeyUsageOrBuilder getKeyUsageOrBuilder()

Optional. Indicates the intended use for keys that correspond to a certificate.

` .google.cloud.security.privateca.v1beta1.KeyUsage key_usage = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[KeyUsageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.KeyUsageOrBuilder)` |   
  
### getPolicyIds(int index)
    
    
    public abstract ObjectId getPolicyIds(int index)

Optional. Describes the X.509 certificate policy object identifiers, per <https://tools.ietf.org/html/rfc5280#section-4.2.1.4>.

` repeated .google.cloud.security.privateca.v1beta1.ObjectId policy_ids = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ObjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.ObjectId)` |   
  
### getPolicyIdsCount()
    
    
    public abstract int getPolicyIdsCount()

Optional. Describes the X.509 certificate policy object identifiers, per <https://tools.ietf.org/html/rfc5280#section-4.2.1.4>.

` repeated .google.cloud.security.privateca.v1beta1.ObjectId policy_ids = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPolicyIdsList()
    
    
    public abstract List<ObjectId> getPolicyIdsList()

Optional. Describes the X.509 certificate policy object identifiers, per <https://tools.ietf.org/html/rfc5280#section-4.2.1.4>.

` repeated .google.cloud.security.privateca.v1beta1.ObjectId policy_ids = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ObjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.ObjectId)>` |   
  
### getPolicyIdsOrBuilder(int index)
    
    
    public abstract ObjectIdOrBuilder getPolicyIdsOrBuilder(int index)

Optional. Describes the X.509 certificate policy object identifiers, per <https://tools.ietf.org/html/rfc5280#section-4.2.1.4>.

` repeated .google.cloud.security.privateca.v1beta1.ObjectId policy_ids = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ObjectIdOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.ObjectIdOrBuilder)` |   
  
### getPolicyIdsOrBuilderList()
    
    
    public abstract List<? extends ObjectIdOrBuilder> getPolicyIdsOrBuilderList()

Optional. Describes the X.509 certificate policy object identifiers, per <https://tools.ietf.org/html/rfc5280#section-4.2.1.4>.

` repeated .google.cloud.security.privateca.v1beta1.ObjectId policy_ids = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.security.privateca.v1beta1.ObjectIdOrBuilder>` |   
  
### hasCaOptions()
    
    
    public abstract boolean hasCaOptions()

Optional. Describes options in this ReusableConfigValues that are relevant in a CA certificate.

` .google.cloud.security.privateca.v1beta1.ReusableConfigValues.CaOptions ca_options = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the caOptions field is set.  
  
### hasKeyUsage()
    
    
    public abstract boolean hasKeyUsage()

Optional. Indicates the intended use for keys that correspond to a certificate.

` .google.cloud.security.privateca.v1beta1.KeyUsage key_usage = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the keyUsage field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
