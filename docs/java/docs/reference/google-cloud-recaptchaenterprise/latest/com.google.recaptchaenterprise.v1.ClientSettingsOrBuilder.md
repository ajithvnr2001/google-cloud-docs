---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ClientSettingsOrBuilder
title: Interface ClientSettingsOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:37.234691+00:00
---

# Interface ClientSettingsOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ClientSettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClientSettingsOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface ClientSettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllowAllDomains()
    
    
    public abstract boolean getAllowAllDomains()

Optional. If set to true, it means allowed_domains are not enforced.

`bool allow_all_domains = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowAllDomains.  
  
### getAllowedDomains(int index)
    
    
    public abstract String getAllowedDomains(int index)

Optional. Domains or subdomains of websites allowed to use the policy. All subdomains of an allowed domain are automatically allowed. A valid domain requires a host and must not include any path, port, query or fragment. Examples: 'example.com' or 'subdomain.example.com' Each policy supports a maximum of 250 domains. To use a policy on more domains, set `allow_all_domains` to true. When this is set, you are responsible for validating the hostname by checking the `token_properties.hostname` field in each assessment response against your list of allowed domains.

`repeated string allowed_domains = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowedDomains at the given index.  
  
### getAllowedDomainsBytes(int index)
    
    
    public abstract ByteString getAllowedDomainsBytes(int index)

Optional. Domains or subdomains of websites allowed to use the policy. All subdomains of an allowed domain are automatically allowed. A valid domain requires a host and must not include any path, port, query or fragment. Examples: 'example.com' or 'subdomain.example.com' Each policy supports a maximum of 250 domains. To use a policy on more domains, set `allow_all_domains` to true. When this is set, you are responsible for validating the hostname by checking the `token_properties.hostname` field in each assessment response against your list of allowed domains.

`repeated string allowed_domains = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the allowedDomains at the given index.  
  
### getAllowedDomainsCount()
    
    
    public abstract int getAllowedDomainsCount()

Optional. Domains or subdomains of websites allowed to use the policy. All subdomains of an allowed domain are automatically allowed. A valid domain requires a host and must not include any path, port, query or fragment. Examples: 'example.com' or 'subdomain.example.com' Each policy supports a maximum of 250 domains. To use a policy on more domains, set `allow_all_domains` to true. When this is set, you are responsible for validating the hostname by checking the `token_properties.hostname` field in each assessment response against your list of allowed domains.

`repeated string allowed_domains = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of allowedDomains.  
  
### getAllowedDomainsList()
    
    
    public abstract List<String> getAllowedDomainsList()

Optional. Domains or subdomains of websites allowed to use the policy. All subdomains of an allowed domain are automatically allowed. A valid domain requires a host and must not include any path, port, query or fragment. Examples: 'example.com' or 'subdomain.example.com' Each policy supports a maximum of 250 domains. To use a policy on more domains, set `allow_all_domains` to true. When this is set, you are responsible for validating the hostname by checking the `token_properties.hostname` field in each assessment response against your list of allowed domains.

`repeated string allowed_domains = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the allowedDomains.  
  
### getProtectedEndpointGroup()
    
    
    public abstract ProtectedEndpointGroup getProtectedEndpointGroup()

Optional. Configuration for all API endpoints to protect with reCAPTCHA. If this field is not set, reCAPTCHA will not automatically request tokens on any API endpoints.

` .google.cloud.recaptchaenterprise.v1.ProtectedEndpointGroup protected_endpoint_group = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ProtectedEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProtectedEndpointGroup)` | The protectedEndpointGroup.  
  
### getProtectedEndpointGroupOrBuilder()
    
    
    public abstract ProtectedEndpointGroupOrBuilder getProtectedEndpointGroupOrBuilder()

Optional. Configuration for all API endpoints to protect with reCAPTCHA. If this field is not set, reCAPTCHA will not automatically request tokens on any API endpoints.

` .google.cloud.recaptchaenterprise.v1.ProtectedEndpointGroup protected_endpoint_group = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ProtectedEndpointGroupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProtectedEndpointGroupOrBuilder)` |   
  
### hasProtectedEndpointGroup()
    
    
    public abstract boolean hasProtectedEndpointGroup()

Optional. Configuration for all API endpoints to protect with reCAPTCHA. If this field is not set, reCAPTCHA will not automatically request tokens on any API endpoints.

` .google.cloud.recaptchaenterprise.v1.ProtectedEndpointGroup protected_endpoint_group = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the protectedEndpointGroup field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
