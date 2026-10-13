---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificateOrBuilder
title: Interface Certificate.ManagedCertificateOrBuilder (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:29.065957+00:00
---

# Interface Certificate.ManagedCertificateOrBuilder (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificateOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Certificate.ManagedCertificateOrBuilder (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.2  0.4.0  0.3.1  0.2.0  0.1.1 
    
    
    public static interface Certificate.ManagedCertificateOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthorizationAttemptInfo(int index)
    
    
    public abstract Certificate.ManagedCertificate.AuthorizationAttemptInfo getAuthorizationAttemptInfo(int index)

Output only. Detailed state of the latest authorization attempt for each domain specified for managed certificate resource.

` repeated .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo authorization_attempt_info = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Certificate.ManagedCertificate.AuthorizationAttemptInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo)` |   
  
### getAuthorizationAttemptInfoCount()
    
    
    public abstract int getAuthorizationAttemptInfoCount()

Output only. Detailed state of the latest authorization attempt for each domain specified for managed certificate resource.

` repeated .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo authorization_attempt_info = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAuthorizationAttemptInfoList()
    
    
    public abstract List<Certificate.ManagedCertificate.AuthorizationAttemptInfo> getAuthorizationAttemptInfoList()

Output only. Detailed state of the latest authorization attempt for each domain specified for managed certificate resource.

` repeated .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo authorization_attempt_info = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AuthorizationAttemptInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo)>` |   
  
### getAuthorizationAttemptInfoOrBuilder(int index)
    
    
    public abstract Certificate.ManagedCertificate.AuthorizationAttemptInfoOrBuilder getAuthorizationAttemptInfoOrBuilder(int index)

Output only. Detailed state of the latest authorization attempt for each domain specified for managed certificate resource.

` repeated .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo authorization_attempt_info = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Certificate.ManagedCertificate.AuthorizationAttemptInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfoOrBuilder)` |   
  
### getAuthorizationAttemptInfoOrBuilderList()
    
    
    public abstract List<? extends Certificate.ManagedCertificate.AuthorizationAttemptInfoOrBuilder> getAuthorizationAttemptInfoOrBuilderList()

Output only. Detailed state of the latest authorization attempt for each domain specified for managed certificate resource.

` repeated .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo authorization_attempt_info = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfoOrBuilder>` |   
  
### getDnsAuthorizations(int index)
    
    
    public abstract String getDnsAuthorizations(int index)

Immutable. Authorizations that will be used for performing domain authorization.

` repeated string dns_authorizations = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dnsAuthorizations at the given index.  
  
### getDnsAuthorizationsBytes(int index)
    
    
    public abstract ByteString getDnsAuthorizationsBytes(int index)

Immutable. Authorizations that will be used for performing domain authorization.

` repeated string dns_authorizations = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the dnsAuthorizations at the given index.  
  
### getDnsAuthorizationsCount()
    
    
    public abstract int getDnsAuthorizationsCount()

Immutable. Authorizations that will be used for performing domain authorization.

` repeated string dns_authorizations = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of dnsAuthorizations.  
  
### getDnsAuthorizationsList()
    
    
    public abstract List<String> getDnsAuthorizationsList()

Immutable. Authorizations that will be used for performing domain authorization.

` repeated string dns_authorizations = 2 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the dnsAuthorizations.  
  
### getDomains(int index)
    
    
    public abstract String getDomains(int index)

Immutable. The domains for which a managed SSL certificate will be generated. Wildcard domains are only supported with DNS challenge resolution.

`repeated string domains = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The domains at the given index.  
  
### getDomainsBytes(int index)
    
    
    public abstract ByteString getDomainsBytes(int index)

Immutable. The domains for which a managed SSL certificate will be generated. Wildcard domains are only supported with DNS challenge resolution.

`repeated string domains = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the domains at the given index.  
  
### getDomainsCount()
    
    
    public abstract int getDomainsCount()

Immutable. The domains for which a managed SSL certificate will be generated. Wildcard domains are only supported with DNS challenge resolution.

`repeated string domains = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of domains.  
  
### getDomainsList()
    
    
    public abstract List<String> getDomainsList()

Immutable. The domains for which a managed SSL certificate will be generated. Wildcard domains are only supported with DNS challenge resolution.

`repeated string domains = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the domains.  
  
### getIssuanceConfig()
    
    
    public abstract String getIssuanceConfig()

Immutable. The resource name for a CertificateIssuanceConfig used to configure private PKI certificates in the format `projects/*/locations/*/certificateIssuanceConfigs/*`. If this field is not set, the certificates will instead be publicly signed as documented at <https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa>.

` string issuance_config = 6 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The issuanceConfig.  
  
### getIssuanceConfigBytes()
    
    
    public abstract ByteString getIssuanceConfigBytes()

Immutable. The resource name for a CertificateIssuanceConfig used to configure private PKI certificates in the format `projects/*/locations/*/certificateIssuanceConfigs/*`. If this field is not set, the certificates will instead be publicly signed as documented at <https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa>.

` string issuance_config = 6 [(.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for issuanceConfig.  
  
### getProvisioningIssue()
    
    
    public abstract Certificate.ManagedCertificate.ProvisioningIssue getProvisioningIssue()

Output only. Information about issues with provisioning a Managed Certificate.

` .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue provisioning_issue = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Certificate.ManagedCertificate.ProvisioningIssue](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue)` | The provisioningIssue.  
  
### getProvisioningIssueOrBuilder()
    
    
    public abstract Certificate.ManagedCertificate.ProvisioningIssueOrBuilder getProvisioningIssueOrBuilder()

Output only. Information about issues with provisioning a Managed Certificate.

` .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue provisioning_issue = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Certificate.ManagedCertificate.ProvisioningIssueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssueOrBuilder)` |   
  
### getState()
    
    
    public abstract Certificate.ManagedCertificate.State getState()

Output only. State of the managed certificate resource.

` .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Certificate.ManagedCertificate.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. State of the managed certificate resource.

` .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### hasProvisioningIssue()
    
    
    public abstract boolean hasProvisioningIssue()

Output only. Information about issues with provisioning a Managed Certificate.

` .google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue provisioning_issue = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the provisioningIssue field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
