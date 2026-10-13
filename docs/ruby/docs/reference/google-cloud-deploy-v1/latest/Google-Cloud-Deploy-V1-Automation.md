---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Automation/
title: Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Automation (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:18.389461+00:00
---

# Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Automation (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Automation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::Automation (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.1  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.0  1.0.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Google Cloud Deploy V1 API class Google::Cloud::Deploy::V1::Automation.

An `Automation` resource in the Cloud Deploy API.

An `Automation` enables the automation of manually driven actions for a Delivery Pipeline, which includes Release promotion among Targets, Rollout repair and Rollout deployment strategy advancement. The intention of Automation is to reduce manual intervention in the continuous delivery process.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotations
    
    
    def annotations() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints:

    * Annotations are key/value pairs.
    * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`).
    * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
    * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`).

See https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set for more details. 




### #annotations=
    
    
    def annotations=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints:

    * Annotations are key/value pairs.
    * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`).
    * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
    * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`).

See https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set for more details. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints:

    * Annotations are key/value pairs.
    * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (`/`).
    * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
    * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(`.`), not longer than 253 characters in total, followed by a slash (`/`).

See https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set for more details. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the automation was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of the `Automation`. Max length is 255 characters. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of the `Automation`. Max length is 255 characters. 



**Returns**

  * (::String) — Optional. Description of the `Automation`. Max length is 255 characters. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Optional. The weak etag of the `Automation` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The weak etag of the `Automation` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



**Returns**

  * (::String) — Optional. The weak etag of the `Automation` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 63 characters. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 63 characters. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
    * All characters must use UTF-8 encoding, and international characters are allowed.
    * Keys must start with a lowercase letter or international character.
    * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 63 characters. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Name of the `Automation`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automations/{automation}`. 



### #rules
    
    
    def rules() -> ::Array<::Google::Cloud::Deploy::V1::AutomationRule>

**Returns**

  * (::Array<[::Google::Cloud::Deploy::V1::AutomationRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRule)>) — Required. List of Automation rules associated with the Automation resource. Must have at least one rule and limited to 250 rules per Delivery Pipeline. Note: the order of the rules here is not the same as the order of execution. 



### #rules=
    
    
    def rules=(value) -> ::Array<::Google::Cloud::Deploy::V1::AutomationRule>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Deploy::V1::AutomationRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRule)>) — Required. List of Automation rules associated with the Automation resource. Must have at least one rule and limited to 250 rules per Delivery Pipeline. Note: the order of the rules here is not the same as the order of execution. 



**Returns**

  * (::Array<[::Google::Cloud::Deploy::V1::AutomationRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRule)>) — Required. List of Automation rules associated with the Automation resource. Must have at least one rule and limited to 250 rules per Delivery Pipeline. Note: the order of the rules here is not the same as the order of execution. 



### #selector
    
    
    def selector() -> ::Google::Cloud::Deploy::V1::AutomationResourceSelector

**Returns**

  * ([::Google::Cloud::Deploy::V1::AutomationResourceSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationResourceSelector)) — Required. Selected resources to which the automation will be applied. 



### #selector=
    
    
    def selector=(value) -> ::Google::Cloud::Deploy::V1::AutomationResourceSelector

**Parameter**

  * **value** ([::Google::Cloud::Deploy::V1::AutomationResourceSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationResourceSelector)) — Required. Selected resources to which the automation will be applied. 



**Returns**

  * ([::Google::Cloud::Deploy::V1::AutomationResourceSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationResourceSelector)) — Required. Selected resources to which the automation will be applied. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — Required. Email address of the user-managed IAM service account that creates Cloud Deploy release and rollout resources. 



### #service_account=
    
    
    def service_account=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Email address of the user-managed IAM service account that creates Cloud Deploy release and rollout resources. 



**Returns**

  * (::String) — Required. Email address of the user-managed IAM service account that creates Cloud Deploy release and rollout resources. 



### #suspended
    
    
    def suspended() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. When Suspended, automation is deactivated from execution. 



### #suspended=
    
    
    def suspended=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. When Suspended, automation is deactivated from execution. 



**Returns**

  * (::Boolean) — Optional. When Suspended, automation is deactivated from execution. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. Unique identifier of the `Automation`. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time at which the automation was updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
