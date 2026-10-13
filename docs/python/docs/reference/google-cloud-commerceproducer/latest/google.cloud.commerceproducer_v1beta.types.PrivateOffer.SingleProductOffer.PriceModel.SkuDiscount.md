---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.PriceModel.SkuDiscount
title: Class SkuDiscount (0.1.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:46.808064+00:00
---

# Class SkuDiscount (0.1.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-commerceproducer/latest/google.cloud.commerceproducer_v1beta.types.PrivateOffer.SingleProductOffer.PriceModel.SkuDiscount

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SkuDiscount (0.1.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.3 (latest)  0.1.2 
    
    
    SkuDiscount(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The discount for a specific SKU.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`sku` |  `str`   
Optional. The name of a partner SKU from this API. Must refer to a SKU in the price model of the base standard offer. Inclusion in the base price model can occur either directly or indirectly via inclusion in an included SkuGroup. Currently, standard offer price models include only partner SKUs in the same project as the standard offer. This may change. Format: projects/{project}/locations/{location}/services/{service}/skus/{sku} This field is a member of `oneof`_ `target`.   
`cloud_billing_sku` |  `str`   
Optional. The name of a Google SKU from the Cloud Billing API. Used for partner products sold by Google, such as Premium Operating System Images sold for use in Compute Engine. This is not common. SKUs of this type are not present on this API and can instead be found on the Cloud Billing API or at https://cloud.google.com/skus. Must refer to a SKU in the price model of the base standard offer. Google SKUs are always referenced in standard offers via SkuGroups. Format: services/{service}/skus/{sku} This field is a member of `oneof`_ `target`.   
`discount_percent` |  `google.type.decimal_pb2.Decimal`   
Optional. The discount percent for the SKU. For example, `10` means a discount of 10%. If the original SKU price is $100/hour then the discounted price will be $90/hour. Must be between 0 and 100 inclusive, with precision up to 2 decimal places. If this field is set, then the allowed pattern for 'value' is `^([0-9]{1,2}(\\.\\d{1,2})?|100(\\.0{1,2})?)$`. Examples of valid values: "0", "100.0", "12.34", "40.0". Example of invalid values: ".3", "-1", "100.1", "12.345", "+12", and "". Must be present to publish the offer. This field is a member of `oneof`_ `discount`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
