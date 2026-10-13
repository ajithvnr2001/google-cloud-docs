---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.CertificateDescription.SubjectDescriptionOrBuilder
title: Interface CertificateDescription.SubjectDescriptionOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:39.292408+00:00
---

# Interface CertificateDescription.SubjectDescriptionOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.CertificateDescription.SubjectDescriptionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CertificateDescription.SubjectDescriptionOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.4  2.4.0  2.3.0  2.2.5 
    
    
    public static interface CertificateDescription.SubjectDescriptionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCommonName()
    
    
    public abstract String getCommonName()

The "common name" of the distinguished name.

`string common_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The commonName.  
  
### getCommonNameBytes()
    
    
    public abstract ByteString getCommonNameBytes()

The "common name" of the distinguished name.

`string common_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for commonName.  
  
### getHexSerialNumber()
    
    
    public abstract String getHexSerialNumber()

The serial number encoded in lowercase hexadecimal.

`string hex_serial_number = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hexSerialNumber.  
  
### getHexSerialNumberBytes()
    
    
    public abstract ByteString getHexSerialNumberBytes()

The serial number encoded in lowercase hexadecimal.

`string hex_serial_number = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hexSerialNumber.  
  
### getLifetime()
    
    
    public abstract Duration getLifetime()

For convenience, the actual lifetime of an issued certificate. Corresponds to 'not_after_time' - 'not_before_time'.

`.google.protobuf.Duration lifetime = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The lifetime.  
  
### getLifetimeOrBuilder()
    
    
    public abstract DurationOrBuilder getLifetimeOrBuilder()

For convenience, the actual lifetime of an issued certificate. Corresponds to 'not_after_time' - 'not_before_time'.

`.google.protobuf.Duration lifetime = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getNotAfterTime()
    
    
    public abstract Timestamp getNotAfterTime()

The time at which the certificate expires.

`.google.protobuf.Timestamp not_after_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The notAfterTime.  
  
### getNotAfterTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getNotAfterTimeOrBuilder()

The time at which the certificate expires.

`.google.protobuf.Timestamp not_after_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getNotBeforeTime()
    
    
    public abstract Timestamp getNotBeforeTime()

The time at which the certificate becomes valid.

`.google.protobuf.Timestamp not_before_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The notBeforeTime.  
  
### getNotBeforeTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getNotBeforeTimeOrBuilder()

The time at which the certificate becomes valid.

`.google.protobuf.Timestamp not_before_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getSubject()
    
    
    public abstract Subject getSubject()

Contains distinguished name fields such as the location and organization.

`.google.cloud.security.privateca.v1beta1.Subject subject = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Subject](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.Subject)` | The subject.  
  
### getSubjectAltName()
    
    
    public abstract SubjectAltNames getSubjectAltName()

The subject alternative name fields.

`.google.cloud.security.privateca.v1beta1.SubjectAltNames subject_alt_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SubjectAltNames](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.SubjectAltNames)` | The subjectAltName.  
  
### getSubjectAltNameOrBuilder()
    
    
    public abstract SubjectAltNamesOrBuilder getSubjectAltNameOrBuilder()

The subject alternative name fields.

`.google.cloud.security.privateca.v1beta1.SubjectAltNames subject_alt_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SubjectAltNamesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.SubjectAltNamesOrBuilder)` |   
  
### getSubjectOrBuilder()
    
    
    public abstract SubjectOrBuilder getSubjectOrBuilder()

Contains distinguished name fields such as the location and organization.

`.google.cloud.security.privateca.v1beta1.Subject subject = 1;`

**Returns**  
---  
**Type** | **Description**  
`[SubjectOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.SubjectOrBuilder)` |   
  
### hasLifetime()
    
    
    public abstract boolean hasLifetime()

For convenience, the actual lifetime of an issued certificate. Corresponds to 'not_after_time' - 'not_before_time'.

`.google.protobuf.Duration lifetime = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lifetime field is set.  
  
### hasNotAfterTime()
    
    
    public abstract boolean hasNotAfterTime()

The time at which the certificate expires.

`.google.protobuf.Timestamp not_after_time = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the notAfterTime field is set.  
  
### hasNotBeforeTime()
    
    
    public abstract boolean hasNotBeforeTime()

The time at which the certificate becomes valid.

`.google.protobuf.Timestamp not_before_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the notBeforeTime field is set.  
  
### hasSubject()
    
    
    public abstract boolean hasSubject()

Contains distinguished name fields such as the location and organization.

`.google.cloud.security.privateca.v1beta1.Subject subject = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the subject field is set.  
  
### hasSubjectAltName()
    
    
    public abstract boolean hasSubjectAltName()

The subject alternative name fields.

`.google.cloud.security.privateca.v1beta1.SubjectAltNames subject_alt_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the subjectAltName field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
