---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-PrivateOffer-Customer/
title: Cloud Commerce Producer V1BETA API - Class Google::Cloud::CommerceProducer::V1beta::PrivateOffer::Customer (v0.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:40.512864+00:00
---

# Cloud Commerce Producer V1BETA API - Class Google::Cloud::CommerceProducer::V1beta::PrivateOffer::Customer (v0.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce_producer-v1beta/latest/Google-Cloud-CommerceProducer-V1beta-PrivateOffer-Customer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Commerce Producer V1BETA API - Class Google::Cloud::CommerceProducer::V1beta::PrivateOffer::Customer (v0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.0 

Reference documentation and code samples for the Cloud Commerce Producer V1BETA API class Google::Cloud::CommerceProducer::V1beta::PrivateOffer::Customer.

Information about the customer.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #address
    
    
    def address() -> ::String

**Returns**

  * (::String) — Output only. Legal address of the customer organization. This field can no longer be set, but it is preserved to return the data from existing offers where address is set. 



### #contact
    
    
    def contact() -> ::String

**Returns**

  * (::String) — Optional. A string identifying the customer contact. Must be provided when publishing the offer. Maximum length: 256 characters. 



### #contact=
    
    
    def contact=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A string identifying the customer contact. Must be provided when publishing the offer. Maximum length: 256 characters. 



**Returns**

  * (::String) — Optional. A string identifying the customer contact. Must be provided when publishing the offer. Maximum length: 256 characters. 



### #email
    
    
    def email() -> ::String

**Returns**

  * (::String) — Optional. Email of customer contact. If provided, it must be a well-formed email address. 



### #email=
    
    
    def email=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Email of customer contact. If provided, it must be a well-formed email address. 



**Returns**

  * (::String) — Optional. Email of customer contact. If provided, it must be a well-formed email address. 



### #entity_title
    
    
    def entity_title() -> ::String

**Returns**

  * (::String) — Optional. A string identifying the customer's entity (for example, the customer's organization or company name). Must be provided when publishing the offer. Maximum length: 256 characters. 



### #entity_title=
    
    
    def entity_title=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A string identifying the customer's entity (for example, the customer's organization or company name). Must be provided when publishing the offer. Maximum length: 256 characters. 



**Returns**

  * (::String) — Optional. A string identifying the customer's entity (for example, the customer's organization or company name). Must be provided when publishing the offer. Maximum length: 256 characters. 



### #target_billing_account
    
    
    def target_billing_account() -> ::String

**Returns**

  * (::String) — Optional. The customer's billing account targeted by the offer. The private offer once published can be accepted by a billing administrator of the target billing account. If the customer accepts the offer and later moves the resulting order to a new billing account, this field will continue to reflect the original billing account to which the private offer was extended. Must be provided when publishing the offer.

To publish this private offer:

    * The billing account must exist.
    * The billing account must not be in a free trial.
    * The billing account must comply with Marketplace Reselling Policies.
    * Reseller parent billing accounts are prohibited. Reseller subaccounts are prohibited unless the service is enabled for reselling.

Format: billingAccounts/012345-567890-ABCDEF 




### #target_billing_account=
    
    
    def target_billing_account=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The customer's billing account targeted by the offer. The private offer once published can be accepted by a billing administrator of the target billing account. If the customer accepts the offer and later moves the resulting order to a new billing account, this field will continue to reflect the original billing account to which the private offer was extended. Must be provided when publishing the offer.

To publish this private offer:

    * The billing account must exist.
    * The billing account must not be in a free trial.
    * The billing account must comply with Marketplace Reselling Policies.
    * Reseller parent billing accounts are prohibited. Reseller subaccounts are prohibited unless the service is enabled for reselling.

Format: billingAccounts/012345-567890-ABCDEF 




**Returns**

  * (::String) — Optional. The customer's billing account targeted by the offer. The private offer once published can be accepted by a billing administrator of the target billing account. If the customer accepts the offer and later moves the resulting order to a new billing account, this field will continue to reflect the original billing account to which the private offer was extended. Must be provided when publishing the offer.

To publish this private offer:

    * The billing account must exist.
    * The billing account must not be in a free trial.
    * The billing account must comply with Marketplace Reselling Policies.
    * Reseller parent billing accounts are prohibited. Reseller subaccounts are prohibited unless the service is enabled for reselling.

Format: billingAccounts/012345-567890-ABCDEF 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
