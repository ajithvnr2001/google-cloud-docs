---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.IpConfiguration.ServerCertificateRotationMode
title: Enum IpConfiguration.ServerCertificateRotationMode (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:55.782572+00:00
---

# Enum IpConfiguration.ServerCertificateRotationMode (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.IpConfiguration.ServerCertificateRotationMode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum IpConfiguration.ServerCertificateRotationMode (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public enum IpConfiguration.ServerCertificateRotationMode extends Enum<IpConfiguration.ServerCertificateRotationMode> implements ProtocolMessageEnum

Settings for automatic server certificate rotation.

Protobuf enum `google.cloud.sql.v1.IpConfiguration.ServerCertificateRotationMode`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`AUTOMATIC_ROTATION_DURING_MAINTENANCE` |  Automatic server certificate rotation during Cloud SQL scheduled maintenance or self-service maintenance updates. Requires `server_ca_mode` to be `GOOGLE_MANAGED_CAS_CA` or `CUSTOMER_MANAGED_CAS_CA`. `AUTOMATIC_ROTATION_DURING_MAINTENANCE = 2;`  
`AUTOMATIC_ROTATION_DURING_MAINTENANCE_VALUE` |  Automatic server certificate rotation during Cloud SQL scheduled maintenance or self-service maintenance updates. Requires `server_ca_mode` to be `GOOGLE_MANAGED_CAS_CA` or `CUSTOMER_MANAGED_CAS_CA`. `AUTOMATIC_ROTATION_DURING_MAINTENANCE = 2;`  
`NO_AUTOMATIC_ROTATION` |  No automatic server certificate rotation. The user must [manage server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#rotate-server-certificate-cas) on their side. `NO_AUTOMATIC_ROTATION = 1;`  
`NO_AUTOMATIC_ROTATION_VALUE` |  No automatic server certificate rotation. The user must [manage server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#rotate-server-certificate-cas) on their side. `NO_AUTOMATIC_ROTATION = 1;`  
`SERVER_CERTIFICATE_ROTATION_MODE_UNSPECIFIED` |  Unspecified: no automatic server certificate rotation. `SERVER_CERTIFICATE_ROTATION_MODE_UNSPECIFIED = 0;`  
`SERVER_CERTIFICATE_ROTATION_MODE_UNSPECIFIED_VALUE` |  Unspecified: no automatic server certificate rotation. `SERVER_CERTIFICATE_ROTATION_MODE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.IpConfiguration.ServerCertificateRotationMode#com_google_cloud_sql_v1_IpConfiguration_ServerCertificateRotationMode_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
