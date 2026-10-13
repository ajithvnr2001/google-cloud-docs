---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductCertificationOrBuilder
title: Interface ProductCertificationOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:45.747337+00:00
---

# Interface ProductCertificationOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductCertificationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProductCertificationOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ProductCertificationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCertificationAuthority()
    
    
    public abstract CertificationAuthority getCertificationAuthority()

The certification authority.

` optional .google.shopping.merchant.products.v1.CertificationAuthority certification_authority = 1; `

**Returns**  
---  
**Type** | **Description**  
`[CertificationAuthority](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.CertificationAuthority)` | The certificationAuthority.  
  
### getCertificationAuthorityValue()
    
    
    public abstract int getCertificationAuthorityValue()

The certification authority.

` optional .google.shopping.merchant.products.v1.CertificationAuthority certification_authority = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for certificationAuthority.  
  
### getCertificationCode()
    
    
    public abstract String getCertificationCode()

The certification code. Maximum length is 2000 characters.

`optional string certification_code = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The certificationCode.  
  
### getCertificationCodeBytes()
    
    
    public abstract ByteString getCertificationCodeBytes()

The certification code. Maximum length is 2000 characters.

`optional string certification_code = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for certificationCode.  
  
### getCertificationDocumentLink()
    
    
    public abstract String getCertificationDocumentLink()

Optional. URL to the certification document (eg. `<https://www.example.com/document>`), for example, the product data sheet or fiche required by UK's DESNZ or EU's EPREL. Maximum length is 2000 characters. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

` optional string certification_document_link = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The certificationDocumentLink.  
  
### getCertificationDocumentLinkBytes()
    
    
    public abstract ByteString getCertificationDocumentLinkBytes()

Optional. URL to the certification document (eg. `<https://www.example.com/document>`), for example, the product data sheet or fiche required by UK's DESNZ or EU's EPREL. Maximum length is 2000 characters. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

` optional string certification_document_link = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for certificationDocumentLink.  
  
### getCertificationLabelLink()
    
    
    public abstract String getCertificationLabelLink()

Optional. URL to the certification label (eg. `<https://www.example.com/label>`), for example, the energy efficiency label required by UK's DESNZ or EU's EPREL. Maximum length is 2000 characters. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

`optional string certification_label_link = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The certificationLabelLink.  
  
### getCertificationLabelLinkBytes()
    
    
    public abstract ByteString getCertificationLabelLinkBytes()

Optional. URL to the certification label (eg. `<https://www.example.com/label>`), for example, the energy efficiency label required by UK's DESNZ or EU's EPREL. Maximum length is 2000 characters. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

`optional string certification_label_link = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for certificationLabelLink.  
  
### getCertificationName()
    
    
    public abstract CertificationName getCertificationName()

The name of the certification.

`optional .google.shopping.merchant.products.v1.CertificationName certification_name = 2; `

**Returns**  
---  
**Type** | **Description**  
`[CertificationName](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.CertificationName)` | The certificationName.  
  
### getCertificationNameValue()
    
    
    public abstract int getCertificationNameValue()

The name of the certification.

`optional .google.shopping.merchant.products.v1.CertificationName certification_name = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for certificationName.  
  
### getCertificationValue()
    
    
    public abstract String getCertificationValue()

The certification value (also known as class, level or grade), for example "A+", "C", "gold". Maximum length is 2000 characters.

`optional string certification_value = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The certificationValue.  
  
### getCertificationValueBytes()
    
    
    public abstract ByteString getCertificationValueBytes()

The certification value (also known as class, level or grade), for example "A+", "C", "gold". Maximum length is 2000 characters.

`optional string certification_value = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for certificationValue.  
  
### hasCertificationAuthority()
    
    
    public abstract boolean hasCertificationAuthority()

The certification authority.

` optional .google.shopping.merchant.products.v1.CertificationAuthority certification_authority = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the certificationAuthority field is set.  
  
### hasCertificationCode()
    
    
    public abstract boolean hasCertificationCode()

The certification code. Maximum length is 2000 characters.

`optional string certification_code = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the certificationCode field is set.  
  
### hasCertificationDocumentLink()
    
    
    public abstract boolean hasCertificationDocumentLink()

Optional. URL to the certification document (eg. `<https://www.example.com/document>`), for example, the product data sheet or fiche required by UK's DESNZ or EU's EPREL. Maximum length is 2000 characters. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

` optional string certification_document_link = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the certificationDocumentLink field is set.  
  
### hasCertificationLabelLink()
    
    
    public abstract boolean hasCertificationLabelLink()

Optional. URL to the certification label (eg. `<https://www.example.com/label>`), for example, the energy efficiency label required by UK's DESNZ or EU's EPREL. Maximum length is 2000 characters. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

`optional string certification_label_link = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the certificationLabelLink field is set.  
  
### hasCertificationName()
    
    
    public abstract boolean hasCertificationName()

The name of the certification.

`optional .google.shopping.merchant.products.v1.CertificationName certification_name = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the certificationName field is set.  
  
### hasCertificationValue()
    
    
    public abstract boolean hasCertificationValue()

The certification value (also known as class, level or grade), for example "A+", "C", "gold". Maximum length is 2000 characters.

`optional string certification_value = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the certificationValue field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
