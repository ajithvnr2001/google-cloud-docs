---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-FleetPackage-VariantSelector/
title: Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::FleetPackage::VariantSelector (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:46.208453+00:00
---

# Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::FleetPackage::VariantSelector (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-FleetPackage-VariantSelector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::FleetPackage::VariantSelector (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Config Delivery V1 API class Google::Cloud::ConfigDelivery::V1::FleetPackage::VariantSelector.

VariantSelector contains information for selecting a variant in `ResourceBundle` to deploy to a target cluster.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #variant_name_template
    
    
    def variant_name_template() -> ::String

**Returns**

  * (::String) — Required. variant_name_template is a template that can refer to variables containing cluster membership metadata such as location, name, and labels to generate the name of the variant for a target cluster. The variable syntax is similar to the unix shell variables.

Available variables are `${membership.name}`, `${membership.location}`, `${membership.project}` and `${membership.labels['label_name']}`.

If you want to deploy a specific variant, say "default" to all the clusters, you can use "default" (string without any variables) as the variant_name_template. 




### #variant_name_template=
    
    
    def variant_name_template=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. variant_name_template is a template that can refer to variables containing cluster membership metadata such as location, name, and labels to generate the name of the variant for a target cluster. The variable syntax is similar to the unix shell variables.

Available variables are `${membership.name}`, `${membership.location}`, `${membership.project}` and `${membership.labels['label_name']}`.

If you want to deploy a specific variant, say "default" to all the clusters, you can use "default" (string without any variables) as the variant_name_template. 




**Returns**

  * (::String) — Required. variant_name_template is a template that can refer to variables containing cluster membership metadata such as location, name, and labels to generate the name of the variant for a target cluster. The variable syntax is similar to the unix shell variables.

Available variables are `${membership.name}`, `${membership.location}`, `${membership.project}` and `${membership.labels['label_name']}`.

If you want to deploy a specific variant, say "default" to all the clusters, you can use "default" (string without any variables) as the variant_name_template. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
