---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Customer (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:18.446784+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Customer (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::Customer (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::Customer.

Entity representing a customer of a reseller or distributor.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #alternate_email
    
    
    def alternate_email() -> ::String

**Returns**

  * (::String) — Secondary contact email. You need to provide an alternate email to create different domains if a primary contact email already exists. Users will receive a notification with credentials when you create an admin.google.com account. Secondary emails are also recovery email addresses. Alternate emails are optional when you create Team customers. 



### #alternate_email=
    
    
    def alternate_email=(value) -> ::String

**Parameter**

  * **value** (::String) — Secondary contact email. You need to provide an alternate email to create different domains if a primary contact email already exists. Users will receive a notification with credentials when you create an admin.google.com account. Secondary emails are also recovery email addresses. Alternate emails are optional when you create Team customers. 



**Returns**

  * (::String) — Secondary contact email. You need to provide an alternate email to create different domains if a primary contact email already exists. Users will receive a notification with credentials when you create an admin.google.com account. Secondary emails are also recovery email addresses. Alternate emails are optional when you create Team customers. 



### #channel_partner_id
    
    
    def channel_partner_id() -> ::String

**Returns**

  * (::String) — Cloud Identity ID of the customer's channel partner. Populated only if a channel partner exists for this customer. 



### #channel_partner_id=
    
    
    def channel_partner_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Cloud Identity ID of the customer's channel partner. Populated only if a channel partner exists for this customer. 



**Returns**

  * (::String) — Cloud Identity ID of the customer's channel partner. Populated only if a channel partner exists for this customer. 



### #cloud_identity_id
    
    
    def cloud_identity_id() -> ::String

**Returns**

  * (::String) — Output only. The customer's Cloud Identity ID if the customer has a Cloud Identity resource. 



### #cloud_identity_info
    
    
    def cloud_identity_info() -> ::Google::Cloud::Channel::V1::CloudIdentityInfo

**Returns**

  * ([::Google::Cloud::Channel::V1::CloudIdentityInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudIdentityInfo)) — Output only. Cloud Identity information for the customer. Populated only if a Cloud Identity account exists for this customer. 



### #correlation_id
    
    
    def correlation_id() -> ::String

**Returns**

  * (::String) — Optional. External CRM ID for the customer. Populated only if a CRM ID exists for this customer. 



### #correlation_id=
    
    
    def correlation_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. External CRM ID for the customer. Populated only if a CRM ID exists for this customer. 



**Returns**

  * (::String) — Optional. External CRM ID for the customer. Populated only if a CRM ID exists for this customer. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the customer was created. 



### #customer_attestation_state
    
    
    def customer_attestation_state() -> ::Google::Cloud::Channel::V1::Customer::CustomerAttestationState

**Returns**

  * ([::Google::Cloud::Channel::V1::Customer::CustomerAttestationState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer-CustomerAttestationState)) — Optional. Indicate if a customer is attesting about the correctness of provided information. Only required if creating a GCP Entitlement. 



### #customer_attestation_state=
    
    
    def customer_attestation_state=(value) -> ::Google::Cloud::Channel::V1::Customer::CustomerAttestationState

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::Customer::CustomerAttestationState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer-CustomerAttestationState)) — Optional. Indicate if a customer is attesting about the correctness of provided information. Only required if creating a GCP Entitlement. 



**Returns**

  * ([::Google::Cloud::Channel::V1::Customer::CustomerAttestationState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Customer-CustomerAttestationState)) — Optional. Indicate if a customer is attesting about the correctness of provided information. Only required if creating a GCP Entitlement. 



### #domain
    
    
    def domain() -> ::String

**Returns**

  * (::String) — Required. The customer's primary domain. Must match the primary contact email's domain. 



### #domain=
    
    
    def domain=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The customer's primary domain. Must match the primary contact email's domain. 



**Returns**

  * (::String) — Required. The customer's primary domain. Must match the primary contact email's domain. 



### #language_code
    
    
    def language_code() -> ::String

**Returns**

  * (::String) — Optional. The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see https://www.unicode.org/reports/tr35/#Unicode_locale_identifier. 



### #language_code=
    
    
    def language_code=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see https://www.unicode.org/reports/tr35/#Unicode_locale_identifier. 



**Returns**

  * (::String) — Optional. The BCP-47 language code, such as "en-US" or "sr-Latn". For more information, see https://www.unicode.org/reports/tr35/#Unicode_locale_identifier. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Resource name of the customer. Format: accounts/{account_id}/customers/{customer_id} 



### #org_display_name
    
    
    def org_display_name() -> ::String

**Returns**

  * (::String) — Required. Name of the organization that the customer entity represents. 



### #org_display_name=
    
    
    def org_display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the organization that the customer entity represents. 



**Returns**

  * (::String) — Required. Name of the organization that the customer entity represents. 



### #org_postal_address
    
    
    def org_postal_address() -> ::Google::Type::PostalAddress

**Returns**

  * ([::Google::Type::PostalAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-PostalAddress)) — Required. The organization address for the customer. To enforce US laws and embargoes, we require a region, postal code, and address lines. You must provide valid addresses for every customer. To set the customer's language, use the Customer-level language code. 



### #org_postal_address=
    
    
    def org_postal_address=(value) -> ::Google::Type::PostalAddress

**Parameter**

  * **value** ([::Google::Type::PostalAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-PostalAddress)) — Required. The organization address for the customer. To enforce US laws and embargoes, we require a region, postal code, and address lines. You must provide valid addresses for every customer. To set the customer's language, use the Customer-level language code. 



**Returns**

  * ([::Google::Type::PostalAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Type-PostalAddress)) — Required. The organization address for the customer. To enforce US laws and embargoes, we require a region, postal code, and address lines. You must provide valid addresses for every customer. To set the customer's language, use the Customer-level language code. 



### #primary_contact_info
    
    
    def primary_contact_info() -> ::Google::Cloud::Channel::V1::ContactInfo

**Returns**

  * ([::Google::Cloud::Channel::V1::ContactInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ContactInfo)) — Primary contact info. 



### #primary_contact_info=
    
    
    def primary_contact_info=(value) -> ::Google::Cloud::Channel::V1::ContactInfo

**Parameter**

  * **value** ([::Google::Cloud::Channel::V1::ContactInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ContactInfo)) — Primary contact info. 



**Returns**

  * ([::Google::Cloud::Channel::V1::ContactInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ContactInfo)) — Primary contact info. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time when the customer was updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
