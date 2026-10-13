---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactSettingsOrBuilder
title: Interface ContactSettingsOrBuilder (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:20.594129+00:00
---

# Interface ContactSettingsOrBuilder (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactSettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ContactSettingsOrBuilder (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.85.0  1.84.0  1.82.0  1.80.0  1.79.0  1.78.0  1.77.0  1.75.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.0  1.67.0  1.65.0  1.64.0  1.61.0  1.60.0  1.59.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.6  0.7.0  0.6.1  0.5.4 
    
    
    public interface ContactSettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdminContact()
    
    
    public abstract ContactSettings.Contact getAdminContact()

Required. The administrative contact for the `Registration`.

` .google.cloud.domains.v1alpha2.ContactSettings.Contact admin_contact = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ContactSettings.Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactSettings.Contact)` | The adminContact.  
  
### getAdminContactOrBuilder()
    
    
    public abstract ContactSettings.ContactOrBuilder getAdminContactOrBuilder()

Required. The administrative contact for the `Registration`.

` .google.cloud.domains.v1alpha2.ContactSettings.Contact admin_contact = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ContactSettings.ContactOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactSettings.ContactOrBuilder)` |   
  
### getPrivacy()
    
    
    public abstract ContactPrivacy getPrivacy()

Required. Privacy setting for the contacts associated with the `Registration`.

` .google.cloud.domains.v1alpha2.ContactPrivacy privacy = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ContactPrivacy](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactPrivacy)` | The privacy.  
  
### getPrivacyValue()
    
    
    public abstract int getPrivacyValue()

Required. Privacy setting for the contacts associated with the `Registration`.

` .google.cloud.domains.v1alpha2.ContactPrivacy privacy = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for privacy.  
  
### getRegistrantContact()
    
    
    public abstract ContactSettings.Contact getRegistrantContact()

Required. The registrant contact for the `Registration`.

_Caution: Anyone with access to this email address, phone number, and/or postal address can take control of the domain._

_Warning: For new`Registration`s, the registrant receives an email confirmation that they must complete within 15 days to avoid domain suspension._

` .google.cloud.domains.v1alpha2.ContactSettings.Contact registrant_contact = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ContactSettings.Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactSettings.Contact)` | The registrantContact.  
  
### getRegistrantContactOrBuilder()
    
    
    public abstract ContactSettings.ContactOrBuilder getRegistrantContactOrBuilder()

Required. The registrant contact for the `Registration`.

_Caution: Anyone with access to this email address, phone number, and/or postal address can take control of the domain._

_Warning: For new`Registration`s, the registrant receives an email confirmation that they must complete within 15 days to avoid domain suspension._

` .google.cloud.domains.v1alpha2.ContactSettings.Contact registrant_contact = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ContactSettings.ContactOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactSettings.ContactOrBuilder)` |   
  
### getTechnicalContact()
    
    
    public abstract ContactSettings.Contact getTechnicalContact()

Required. The technical contact for the `Registration`.

` .google.cloud.domains.v1alpha2.ContactSettings.Contact technical_contact = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ContactSettings.Contact](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactSettings.Contact)` | The technicalContact.  
  
### getTechnicalContactOrBuilder()
    
    
    public abstract ContactSettings.ContactOrBuilder getTechnicalContactOrBuilder()

Required. The technical contact for the `Registration`.

` .google.cloud.domains.v1alpha2.ContactSettings.Contact technical_contact = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ContactSettings.ContactOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1alpha2.ContactSettings.ContactOrBuilder)` |   
  
### hasAdminContact()
    
    
    public abstract boolean hasAdminContact()

Required. The administrative contact for the `Registration`.

` .google.cloud.domains.v1alpha2.ContactSettings.Contact admin_contact = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adminContact field is set.  
  
### hasRegistrantContact()
    
    
    public abstract boolean hasRegistrantContact()

Required. The registrant contact for the `Registration`.

_Caution: Anyone with access to this email address, phone number, and/or postal address can take control of the domain._

_Warning: For new`Registration`s, the registrant receives an email confirmation that they must complete within 15 days to avoid domain suspension._

` .google.cloud.domains.v1alpha2.ContactSettings.Contact registrant_contact = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the registrantContact field is set.  
  
### hasTechnicalContact()
    
    
    public abstract boolean hasTechnicalContact()

Required. The technical contact for the `Registration`.

` .google.cloud.domains.v1alpha2.ContactSettings.Contact technical_contact = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the technicalContact field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
