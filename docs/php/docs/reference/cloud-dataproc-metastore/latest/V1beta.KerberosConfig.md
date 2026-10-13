---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.KerberosConfig
title: Google Cloud Dataproc Metastore V1beta Client - Class KerberosConfig (1.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:31.482985+00:00
---

# Google Cloud Dataproc Metastore V1beta Client - Class KerberosConfig (1.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.KerberosConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc Metastore V1beta Client - Class KerberosConfig (1.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.4  1.1.1  1.0.4  0.11.5  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.1  0.4.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataproc Metastore V1beta Client class KerberosConfig.

Configuration information for a Kerberos principal.

Generated from protobuf message `google.cloud.metastore.v1beta.KerberosConfig`

## Namespace

Google \ Cloud \ Metastore \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ keytab` |  `[Secret](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Secret)`   
A Kerberos keytab file that can be used to authenticate a service principal with a Kerberos Key Distribution Center (KDC).  
`↳ principal` |  `string`   
A Kerberos principal that exists in the both the keytab the KDC to authenticate as. A typical principal is of the form `primary/instance\@REALM`, but there is no exact format.  
`↳ krb5_config_gcs_uri` |  `string`   
A Cloud Storage URI that specifies the path to a krb5.conf file. It is of the form `gs://{bucket_name}/path/to/krb5.conf`, although the file does not need to be named krb5.conf explicitly.  
  
### getKeytab

A Kerberos keytab file that can be used to authenticate a service principal with a Kerberos Key Distribution Center (KDC).

**Returns**  
---  
**Type** | **Description**  
`[Secret](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Secret)|null` |   
  
### hasKeytab

### clearKeytab

### setKeytab

A Kerberos keytab file that can be used to authenticate a service principal with a Kerberos Key Distribution Center (KDC).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Secret](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Secret)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPrincipal

A Kerberos principal that exists in the both the keytab the KDC to authenticate as. A typical principal is of the form `primary/instance\@REALM`, but there is no exact format.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPrincipal

A Kerberos principal that exists in the both the keytab the KDC to authenticate as. A typical principal is of the form `primary/instance\@REALM`, but there is no exact format.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getKrb5ConfigGcsUri

A Cloud Storage URI that specifies the path to a krb5.conf file. It is of the form `gs://{bucket_name}/path/to/krb5.conf`, although the file does not need to be named krb5.conf explicitly.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setKrb5ConfigGcsUri

A Cloud Storage URI that specifies the path to a krb5.conf file. It is of the form `gs://{bucket_name}/path/to/krb5.conf`, although the file does not need to be named krb5.conf explicitly.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
