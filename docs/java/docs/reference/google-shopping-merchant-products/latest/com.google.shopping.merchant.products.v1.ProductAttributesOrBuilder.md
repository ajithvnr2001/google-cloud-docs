---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributesOrBuilder
title: Interface ProductAttributesOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:20.602774+00:00
---

# Interface ProductAttributesOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProductAttributesOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ProductAttributesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdditionalImageLinks(int index)
    
    
    public abstract String getAdditionalImageLinks(int index)

Additional URLs of images of the item.

`repeated string additional_image_links = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The additionalImageLinks at the given index.  
  
### getAdditionalImageLinksBytes(int index)
    
    
    public abstract ByteString getAdditionalImageLinksBytes(int index)

Additional URLs of images of the item.

`repeated string additional_image_links = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the additionalImageLinks at the given index.  
  
### getAdditionalImageLinksCount()
    
    
    public abstract int getAdditionalImageLinksCount()

Additional URLs of images of the item.

`repeated string additional_image_links = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of additionalImageLinks.  
  
### getAdditionalImageLinksList()
    
    
    public abstract List<String> getAdditionalImageLinksList()

Additional URLs of images of the item.

`repeated string additional_image_links = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the additionalImageLinks.  
  
### getAdsGrouping()
    
    
    public abstract String getAdsGrouping()

Used to group items in an arbitrary way. Only for CPA%, discouraged otherwise. For more information, see [Display ads attribute](https://support.google.com/merchants/answer/6069387).

`optional string ads_grouping = 59;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The adsGrouping.  
  
### getAdsGroupingBytes()
    
    
    public abstract ByteString getAdsGroupingBytes()

Used to group items in an arbitrary way. Only for CPA%, discouraged otherwise. For more information, see [Display ads attribute](https://support.google.com/merchants/answer/6069387).

`optional string ads_grouping = 59;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for adsGrouping.  
  
### getAdsLabels(int index)
    
    
    public abstract String getAdsLabels(int index)

Similar to ads_grouping, but only works on CPC.

`repeated string ads_labels = 60;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The adsLabels at the given index.  
  
### getAdsLabelsBytes(int index)
    
    
    public abstract ByteString getAdsLabelsBytes(int index)

Similar to ads_grouping, but only works on CPC.

`repeated string ads_labels = 60;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the adsLabels at the given index.  
  
### getAdsLabelsCount()
    
    
    public abstract int getAdsLabelsCount()

Similar to ads_grouping, but only works on CPC.

`repeated string ads_labels = 60;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of adsLabels.  
  
### getAdsLabelsList()
    
    
    public abstract List<String> getAdsLabelsList()

Similar to ads_grouping, but only works on CPC.

`repeated string ads_labels = 60;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the adsLabels.  
  
### getAdsRedirect()
    
    
    public abstract String getAdsRedirect()

Allows advertisers to override the item URL when the product is shown within the context of Product ads.

`optional string ads_redirect = 61;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The adsRedirect.  
  
### getAdsRedirectBytes()
    
    
    public abstract ByteString getAdsRedirectBytes()

Allows advertisers to override the item URL when the product is shown within the context of Product ads.

`optional string ads_redirect = 61;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for adsRedirect.  
  
### getAdult()
    
    
    public abstract boolean getAdult()

Set to true if the item is targeted towards adults.

`optional bool adult = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The adult.  
  
### getAgeGroup()
    
    
    public abstract AgeGroup getAgeGroup()

Target [age group](https://support.google.com/merchants/answer/6324463) of the item.

`optional .google.shopping.merchant.products.v1.AgeGroup age_group = 18;`

**Returns**  
---  
**Type** | **Description**  
`[AgeGroup](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.AgeGroup)` | The ageGroup.  
  
### getAgeGroupValue()
    
    
    public abstract int getAgeGroupValue()

Target [age group](https://support.google.com/merchants/answer/6324463) of the item.

`optional .google.shopping.merchant.products.v1.AgeGroup age_group = 18;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for ageGroup.  
  
### getAmenityFeature(int index)
    
    
    public abstract ProductAttributes.AmenityFeature getAmenityFeature(int index)

The amenity features for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.AmenityFeature amenity_feature = 189; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.AmenityFeature](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.AmenityFeature)` | The amenityFeature at the given index.  
  
### getAmenityFeatureCount()
    
    
    public abstract int getAmenityFeatureCount()

The amenity features for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.AmenityFeature amenity_feature = 189; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of amenityFeature.  
  
### getAmenityFeatureList()
    
    
    public abstract List<ProductAttributes.AmenityFeature> getAmenityFeatureList()

The amenity features for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.AmenityFeature amenity_feature = 189; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AmenityFeature](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.AmenityFeature)>` | A list containing the amenityFeature.  
  
### getAmenityFeatureValue(int index)
    
    
    public abstract int getAmenityFeatureValue(int index)

The amenity features for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.AmenityFeature amenity_feature = 189; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of amenityFeature at the given index.  
  
### getAmenityFeatureValueList()
    
    
    public abstract List<Integer> getAmenityFeatureValueList()

The amenity features for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.AmenityFeature amenity_feature = 189; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for amenityFeature.  
  
### getAutoPricingMinPrice()
    
    
    public abstract Price getAutoPricingMinPrice()

A safeguard in the [automated discounts](https://support.google.com/merchants/answer/10295759) and "Dynamic Promotions" (<https://support.google.com/merchants/answer/13949249>) projects, ensuring that discounts on business offers do not fall below this value, thereby preserving the offer's value and profitability.

`.google.shopping.type.Price auto_pricing_min_price = 124;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The autoPricingMinPrice.  
  
### getAutoPricingMinPriceOrBuilder()
    
    
    public abstract PriceOrBuilder getAutoPricingMinPriceOrBuilder()

A safeguard in the [automated discounts](https://support.google.com/merchants/answer/10295759) and "Dynamic Promotions" (<https://support.google.com/merchants/answer/13949249>) projects, ensuring that discounts on business offers do not fall below this value, thereby preserving the offer's value and profitability.

`.google.shopping.type.Price auto_pricing_min_price = 124;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getAvailability()
    
    
    public abstract Availability getAvailability()

[Availability](https://support.google.com/merchants/answer/6324448) status of the item.

`optional .google.shopping.merchant.products.v1.Availability availability = 19;`

**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.Availability)` | The availability.  
  
### getAvailabilityDate()
    
    
    public abstract Timestamp getAvailabilityDate()

The day a pre-ordered product becomes available for delivery, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

`.google.protobuf.Timestamp availability_date = 20;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The availabilityDate.  
  
### getAvailabilityDateOrBuilder()
    
    
    public abstract TimestampOrBuilder getAvailabilityDateOrBuilder()

The day a pre-ordered product becomes available for delivery, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

`.google.protobuf.Timestamp availability_date = 20;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getAvailabilityValue()
    
    
    public abstract int getAvailabilityValue()

[Availability](https://support.google.com/merchants/answer/6324448) status of the item.

`optional .google.shopping.merchant.products.v1.Availability availability = 19;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for availability.  
  
### getBodyStyle()
    
    
    public abstract ProductAttributes.VehicleBodyStyle getBodyStyle()

The [body style](https://support.google.com/google-ads/answer/14157085) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.VehicleBodyStyle body_style = 150; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.VehicleBodyStyle](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.VehicleBodyStyle)` | The bodyStyle.  
  
### getBodyStyleValue()
    
    
    public abstract int getBodyStyleValue()

The [body style](https://support.google.com/google-ads/answer/14157085) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.VehicleBodyStyle body_style = 150; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for bodyStyle.  
  
### getBrand()
    
    
    public abstract String getBrand()

[Brand](https://support.google.com/merchants/answer/6324351) of the item. For example, "Google".

`optional string brand = 21;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The brand.  
  
### getBrandBytes()
    
    
    public abstract ByteString getBrandBytes()

[Brand](https://support.google.com/merchants/answer/6324351) of the item. For example, "Google".

`optional string brand = 21;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for brand.  
  
### getCanonicalLink()
    
    
    public abstract String getCanonicalLink()

URL for the canonical version of your item's landing page.

`optional string canonical_link = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The canonicalLink.  
  
### getCanonicalLinkBytes()
    
    
    public abstract ByteString getCanonicalLinkBytes()

URL for the canonical version of your item's landing page.

`optional string canonical_link = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for canonicalLink.  
  
### getCarrierShipping(int index)
    
    
    public abstract ProductAttributes.CarrierShipping getCarrierShipping(int index)

Rules for carrier-based shipping.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping carrier_shipping = 142; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.CarrierShipping](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping)` |   
  
### getCarrierShippingCount()
    
    
    public abstract int getCarrierShippingCount()

Rules for carrier-based shipping.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping carrier_shipping = 142; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCarrierShippingList()
    
    
    public abstract List<ProductAttributes.CarrierShipping> getCarrierShippingList()

Rules for carrier-based shipping.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping carrier_shipping = 142; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CarrierShipping](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping)>` |   
  
### getCarrierShippingOrBuilder(int index)
    
    
    public abstract ProductAttributes.CarrierShippingOrBuilder getCarrierShippingOrBuilder(int index)

Rules for carrier-based shipping.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping carrier_shipping = 142; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.CarrierShippingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.CarrierShippingOrBuilder)` |   
  
### getCarrierShippingOrBuilderList()
    
    
    public abstract List<? extends ProductAttributes.CarrierShippingOrBuilder> getCarrierShippingOrBuilderList()

Rules for carrier-based shipping.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping carrier_shipping = 142; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductAttributes.CarrierShippingOrBuilder>` |   
  
### getCertifications(int index)
    
    
    public abstract ProductCertification getCertifications(int index)

Product Certifications, for example for energy efficiency labeling of products recorded in the [EU EPREL](https://eprel.ec.europa.eu/screen/home) database. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

`repeated .google.shopping.merchant.products.v1.ProductCertification certifications = 123; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductCertification](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductCertification)` |   
  
### getCertificationsCount()
    
    
    public abstract int getCertificationsCount()

Product Certifications, for example for energy efficiency labeling of products recorded in the [EU EPREL](https://eprel.ec.europa.eu/screen/home) database. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

`repeated .google.shopping.merchant.products.v1.ProductCertification certifications = 123; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCertificationsList()
    
    
    public abstract List<ProductCertification> getCertificationsList()

Product Certifications, for example for energy efficiency labeling of products recorded in the [EU EPREL](https://eprel.ec.europa.eu/screen/home) database. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

`repeated .google.shopping.merchant.products.v1.ProductCertification certifications = 123; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProductCertification](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductCertification)>` |   
  
### getCertificationsOrBuilder(int index)
    
    
    public abstract ProductCertificationOrBuilder getCertificationsOrBuilder(int index)

Product Certifications, for example for energy efficiency labeling of products recorded in the [EU EPREL](https://eprel.ec.europa.eu/screen/home) database. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

`repeated .google.shopping.merchant.products.v1.ProductCertification certifications = 123; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductCertificationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductCertificationOrBuilder)` |   
  
### getCertificationsOrBuilderList()
    
    
    public abstract List<? extends ProductCertificationOrBuilder> getCertificationsOrBuilderList()

Product Certifications, for example for energy efficiency labeling of products recorded in the [EU EPREL](https://eprel.ec.europa.eu/screen/home) database. For more information, see [Certification](https://support.google.com/merchants/answer/13528839).

`repeated .google.shopping.merchant.products.v1.ProductCertification certifications = 123; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductCertificationOrBuilder>` |   
  
### getCertifiedPreOwned()
    
    
    public abstract boolean getCertifiedPreOwned()

Whether the vehicle is OEM [certified pre-owned](https://support.google.com/google-ads/answer/14156475).

`bool certified_pre_owned = 161;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The certifiedPreOwned.  
  
### getCloudExportAdditionalProperties(int index)
    
    
    public abstract CloudExportAdditionalProperties getCloudExportAdditionalProperties(int index)

Extra fields to export to the Cloud Retail program.

` repeated .google.shopping.merchant.products.v1.CloudExportAdditionalProperties cloud_export_additional_properties = 84; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudExportAdditionalProperties](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.CloudExportAdditionalProperties)` |   
  
### getCloudExportAdditionalPropertiesCount()
    
    
    public abstract int getCloudExportAdditionalPropertiesCount()

Extra fields to export to the Cloud Retail program.

` repeated .google.shopping.merchant.products.v1.CloudExportAdditionalProperties cloud_export_additional_properties = 84; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCloudExportAdditionalPropertiesList()
    
    
    public abstract List<CloudExportAdditionalProperties> getCloudExportAdditionalPropertiesList()

Extra fields to export to the Cloud Retail program.

` repeated .google.shopping.merchant.products.v1.CloudExportAdditionalProperties cloud_export_additional_properties = 84; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CloudExportAdditionalProperties](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.CloudExportAdditionalProperties)>` |   
  
### getCloudExportAdditionalPropertiesOrBuilder(int index)
    
    
    public abstract CloudExportAdditionalPropertiesOrBuilder getCloudExportAdditionalPropertiesOrBuilder(int index)

Extra fields to export to the Cloud Retail program.

` repeated .google.shopping.merchant.products.v1.CloudExportAdditionalProperties cloud_export_additional_properties = 84; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudExportAdditionalPropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.CloudExportAdditionalPropertiesOrBuilder)` |   
  
### getCloudExportAdditionalPropertiesOrBuilderList()
    
    
    public abstract List<? extends CloudExportAdditionalPropertiesOrBuilder> getCloudExportAdditionalPropertiesOrBuilderList()

Extra fields to export to the Cloud Retail program.

` repeated .google.shopping.merchant.products.v1.CloudExportAdditionalProperties cloud_export_additional_properties = 84; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.CloudExportAdditionalPropertiesOrBuilder>` |   
  
### getCo2Emissions()
    
    
    public abstract ProductAttributes.Co2Emissions getCo2Emissions()

The [co2 emission](https://support.google.com/google-ads/answer/14546146) of the vehicle.

`.google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions co2_emissions = 157; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.Co2Emissions](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions)` | The co2Emissions.  
  
### getCo2EmissionsOrBuilder()
    
    
    public abstract ProductAttributes.Co2EmissionsOrBuilder getCo2EmissionsOrBuilder()

The [co2 emission](https://support.google.com/google-ads/answer/14546146) of the vehicle.

`.google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions co2_emissions = 157; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.Co2EmissionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.Co2EmissionsOrBuilder)` |   
  
### getColor()
    
    
    public abstract String getColor()

[Color](https://support.google.com/merchants/answer/6324487) of the item. For example, "red".

`optional string color = 22;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The color.  
  
### getColorBytes()
    
    
    public abstract ByteString getColorBytes()

[Color](https://support.google.com/merchants/answer/6324487) of the item. For example, "red".

`optional string color = 22;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for color.  
  
### getCondition()
    
    
    public abstract Condition getCondition()

[Condition](https://support.google.com/merchants/answer/6324469) or state of the item.

`optional .google.shopping.merchant.products.v1.Condition condition = 23;`

**Returns**  
---  
**Type** | **Description**  
`[Condition](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.Condition)` | The condition.  
  
### getConditionValue()
    
    
    public abstract int getConditionValue()

[Condition](https://support.google.com/merchants/answer/6324469) or state of the item.

`optional .google.shopping.merchant.products.v1.Condition condition = 23;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for condition.  
  
### getCostOfGoodsSold()
    
    
    public abstract Price getCostOfGoodsSold()

Cost of goods sold. Used for gross profit reporting.

`.google.shopping.type.Price cost_of_goods_sold = 62;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The costOfGoodsSold.  
  
### getCostOfGoodsSoldOrBuilder()
    
    
    public abstract PriceOrBuilder getCostOfGoodsSoldOrBuilder()

Cost of goods sold. Used for gross profit reporting.

`.google.shopping.type.Price cost_of_goods_sold = 62;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getCustomLabel0()
    
    
    public abstract String getCustomLabel0()

[Custom label 0](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_0 = 71;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customLabel0.  
  
### getCustomLabel0Bytes()
    
    
    public abstract ByteString getCustomLabel0Bytes()

[Custom label 0](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_0 = 71;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customLabel0.  
  
### getCustomLabel1()
    
    
    public abstract String getCustomLabel1()

[Custom label 1](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_1 = 72;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customLabel1.  
  
### getCustomLabel1Bytes()
    
    
    public abstract ByteString getCustomLabel1Bytes()

[Custom label 1](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_1 = 72;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customLabel1.  
  
### getCustomLabel2()
    
    
    public abstract String getCustomLabel2()

[Custom label 2](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_2 = 73;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customLabel2.  
  
### getCustomLabel2Bytes()
    
    
    public abstract ByteString getCustomLabel2Bytes()

[Custom label 2](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_2 = 73;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customLabel2.  
  
### getCustomLabel3()
    
    
    public abstract String getCustomLabel3()

[Custom label 3](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_3 = 74;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customLabel3.  
  
### getCustomLabel3Bytes()
    
    
    public abstract ByteString getCustomLabel3Bytes()

[Custom label 3](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_3 = 74;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customLabel3.  
  
### getCustomLabel4()
    
    
    public abstract String getCustomLabel4()

[Custom label 4](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_4 = 75;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customLabel4.  
  
### getCustomLabel4Bytes()
    
    
    public abstract ByteString getCustomLabel4Bytes()

[Custom label 4](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_4 = 75;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customLabel4.  
  
### getDateFirstRegistered()
    
    
    public abstract String getDateFirstRegistered()

The date the vehicle was first registered. Format: `YYYY-MM`. See the [Date first registered](https://support.google.com/google-ads/answer/14546138) for more information.

`string date_first_registered = 158;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dateFirstRegistered.  
  
### getDateFirstRegisteredBytes()
    
    
    public abstract ByteString getDateFirstRegisteredBytes()

The date the vehicle was first registered. Format: `YYYY-MM`. See the [Date first registered](https://support.google.com/google-ads/answer/14546138) for more information.

`string date_first_registered = 158;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dateFirstRegistered.  
  
### getDescription()
    
    
    public abstract String getDescription()

Description of the item.

`optional string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Description of the item.

`optional string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisclosureDate()
    
    
    public abstract Timestamp getDisclosureDate()

The date time when an offer becomes visible in search results across Google’s YouTube surfaces, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format. See [Disclosure date](https://support.google.com/merchants/answer/13034208) for more information.

`.google.protobuf.Timestamp disclosure_date = 79;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The disclosureDate.  
  
### getDisclosureDateOrBuilder()
    
    
    public abstract TimestampOrBuilder getDisclosureDateOrBuilder()

The date time when an offer becomes visible in search results across Google’s YouTube surfaces, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format. See [Disclosure date](https://support.google.com/merchants/answer/13034208) for more information.

`.google.protobuf.Timestamp disclosure_date = 79;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayAddress()
    
    
    public abstract ProductAttributes.DisplayAddress getDisplayAddress()

The display address of the property.

` .google.shopping.merchant.products.v1.ProductAttributes.DisplayAddress display_address = 179; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.DisplayAddress](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.DisplayAddress)` | The displayAddress.  
  
### getDisplayAddressOrBuilder()
    
    
    public abstract ProductAttributes.DisplayAddressOrBuilder getDisplayAddressOrBuilder()

The display address of the property.

` .google.shopping.merchant.products.v1.ProductAttributes.DisplayAddress display_address = 179; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.DisplayAddressOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.DisplayAddressOrBuilder)` |   
  
### getDisplayAdsId()
    
    
    public abstract String getDisplayAdsId()

An identifier for an item for dynamic remarketing campaigns.

`optional string display_ads_id = 65;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayAdsId.  
  
### getDisplayAdsIdBytes()
    
    
    public abstract ByteString getDisplayAdsIdBytes()

An identifier for an item for dynamic remarketing campaigns.

`optional string display_ads_id = 65;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayAdsId.  
  
### getDisplayAdsLink()
    
    
    public abstract String getDisplayAdsLink()

URL directly to your item's landing page for dynamic remarketing campaigns.

`optional string display_ads_link = 68;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayAdsLink.  
  
### getDisplayAdsLinkBytes()
    
    
    public abstract ByteString getDisplayAdsLinkBytes()

URL directly to your item's landing page for dynamic remarketing campaigns.

`optional string display_ads_link = 68;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayAdsLink.  
  
### getDisplayAdsSimilarIds(int index)
    
    
    public abstract String getDisplayAdsSimilarIds(int index)

Advertiser-specified recommendations. For more information, see [Display ads attribute specification](https://support.google.com/merchants/answer/6069387).

`repeated string display_ads_similar_ids = 66;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayAdsSimilarIds at the given index.  
  
### getDisplayAdsSimilarIdsBytes(int index)
    
    
    public abstract ByteString getDisplayAdsSimilarIdsBytes(int index)

Advertiser-specified recommendations. For more information, see [Display ads attribute specification](https://support.google.com/merchants/answer/6069387).

`repeated string display_ads_similar_ids = 66;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the displayAdsSimilarIds at the given index.  
  
### getDisplayAdsSimilarIdsCount()
    
    
    public abstract int getDisplayAdsSimilarIdsCount()

Advertiser-specified recommendations. For more information, see [Display ads attribute specification](https://support.google.com/merchants/answer/6069387).

`repeated string display_ads_similar_ids = 66;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of displayAdsSimilarIds.  
  
### getDisplayAdsSimilarIdsList()
    
    
    public abstract List<String> getDisplayAdsSimilarIdsList()

Advertiser-specified recommendations. For more information, see [Display ads attribute specification](https://support.google.com/merchants/answer/6069387).

`repeated string display_ads_similar_ids = 66;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the displayAdsSimilarIds.  
  
### getDisplayAdsTitle()
    
    
    public abstract String getDisplayAdsTitle()

Title of an item for dynamic remarketing campaigns.

`optional string display_ads_title = 67;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayAdsTitle.  
  
### getDisplayAdsTitleBytes()
    
    
    public abstract ByteString getDisplayAdsTitleBytes()

Title of an item for dynamic remarketing campaigns.

`optional string display_ads_title = 67;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayAdsTitle.  
  
### getDisplayAdsValue()
    
    
    public abstract double getDisplayAdsValue()

Offer margin for dynamic remarketing campaigns. For more information, see [Display ads attribute](https://support.google.com/merchants/answer/6069387).

`optional double display_ads_value = 69;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The displayAdsValue.  
  
### getDocumentLinks(int index)
    
    
    public abstract String getDocumentLinks(int index)

Optional. Contains a list of PDF [document URLs](https://support.google.com/merchants/answer/17084656) for the product. Examples are training manuals, user guides, assembly instructions, package inserts, etc. Must start with "http://" or "https://"), ASCII characters only, and RFC 3986 compliant.

`repeated string document_links = 176 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The documentLinks at the given index.  
  
### getDocumentLinksBytes(int index)
    
    
    public abstract ByteString getDocumentLinksBytes(int index)

Optional. Contains a list of PDF [document URLs](https://support.google.com/merchants/answer/17084656) for the product. Examples are training manuals, user guides, assembly instructions, package inserts, etc. Must start with "http://" or "https://"), ASCII characters only, and RFC 3986 compliant.

`repeated string document_links = 176 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the documentLinks at the given index.  
  
### getDocumentLinksCount()
    
    
    public abstract int getDocumentLinksCount()

Optional. Contains a list of PDF [document URLs](https://support.google.com/merchants/answer/17084656) for the product. Examples are training manuals, user guides, assembly instructions, package inserts, etc. Must start with "http://" or "https://"), ASCII characters only, and RFC 3986 compliant.

`repeated string document_links = 176 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of documentLinks.  
  
### getDocumentLinksList()
    
    
    public abstract List<String> getDocumentLinksList()

Optional. Contains a list of PDF [document URLs](https://support.google.com/merchants/answer/17084656) for the product. Examples are training manuals, user guides, assembly instructions, package inserts, etc. Must start with "http://" or "https://"), ASCII characters only, and RFC 3986 compliant.

`repeated string document_links = 176 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the documentLinks.  
  
### getElectricRange()
    
    
    public abstract ProductAttributes.Mileage getElectricRange()

The [electric range](https://support.google.com/google-ads/answer/15162232) of the vehicle in miles/kms.

`.google.shopping.merchant.products.v1.ProductAttributes.Mileage electric_range = 153; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.Mileage](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.Mileage)` | The electricRange.  
  
### getElectricRangeOrBuilder()
    
    
    public abstract ProductAttributes.MileageOrBuilder getElectricRangeOrBuilder()

The [electric range](https://support.google.com/google-ads/answer/15162232) of the vehicle in miles/kms.

`.google.shopping.merchant.products.v1.ProductAttributes.Mileage electric_range = 153; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.MileageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.MileageOrBuilder)` |   
  
### getEmissionsStandard()
    
    
    public abstract ProductAttributes.EmissionsStandard getEmissionsStandard()

The [emission standard](https://support.google.com/google-ads/answer/14869021) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.EmissionsStandard emissions_standard = 160; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.EmissionsStandard](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.EmissionsStandard)` | The emissionsStandard.  
  
### getEmissionsStandardValue()
    
    
    public abstract int getEmissionsStandardValue()

The [emission standard](https://support.google.com/google-ads/answer/14869021) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.EmissionsStandard emissions_standard = 160; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for emissionsStandard.  
  
### getEnergyConsumption()
    
    
    public abstract ProductAttributes.EnergyConsumption getEnergyConsumption()

The [energy consumption](https://support.google.com/google-ads/answer/14546149) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.EnergyConsumption energy_consumption = 156; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.EnergyConsumption](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.EnergyConsumption)` | The energyConsumption.  
  
### getEnergyConsumptionOrBuilder()
    
    
    public abstract ProductAttributes.EnergyConsumptionOrBuilder getEnergyConsumptionOrBuilder()

The [energy consumption](https://support.google.com/google-ads/answer/14546149) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.EnergyConsumption energy_consumption = 156; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.EnergyConsumptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.EnergyConsumptionOrBuilder)` |   
  
### getEnergyEfficiencyClass()
    
    
    public abstract EnergyEfficiencyClass getEnergyEfficiencyClass()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass energy_efficiency_class = 53; `

**Returns**  
---  
**Type** | **Description**  
`[EnergyEfficiencyClass](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.EnergyEfficiencyClass)` | The energyEfficiencyClass.  
  
### getEnergyEfficiencyClassValue()
    
    
    public abstract int getEnergyEfficiencyClassValue()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass energy_efficiency_class = 53; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for energyEfficiencyClass.  
  
### getEngine()
    
    
    public abstract ProductAttributes.EngineType getEngine()

The [engine](https://support.google.com/google-ads/answer/14156068) type of the vehicle.

`.google.shopping.merchant.products.v1.ProductAttributes.EngineType engine = 159;`

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.EngineType](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.EngineType)` | The engine.  
  
### getEngineValue()
    
    
    public abstract int getEngineValue()

The [engine](https://support.google.com/google-ads/answer/14156068) type of the vehicle.

`.google.shopping.merchant.products.v1.ProductAttributes.EngineType engine = 159;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for engine.  
  
### getExcludedDestinations(int index)
    
    
    public abstract Destination.DestinationEnum getExcludedDestinations(int index)

The list of destinations to exclude for this target (corresponds to unchecked check boxes in Merchant Center).

For more information, see [Excluded destination](https://support.google.com/merchants/answer/6324486).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum excluded_destinations = 77; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Destination.DestinationEnum` | The excludedDestinations at the given index.  
  
### getExcludedDestinationsCount()
    
    
    public abstract int getExcludedDestinationsCount()

The list of destinations to exclude for this target (corresponds to unchecked check boxes in Merchant Center).

For more information, see [Excluded destination](https://support.google.com/merchants/answer/6324486).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum excluded_destinations = 77; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of excludedDestinations.  
  
### getExcludedDestinationsList()
    
    
    public abstract List<Destination.DestinationEnum> getExcludedDestinationsList()

The list of destinations to exclude for this target (corresponds to unchecked check boxes in Merchant Center).

For more information, see [Excluded destination](https://support.google.com/merchants/answer/6324486).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum excluded_destinations = 77; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.shopping.type.Destination.DestinationEnum>` | A list containing the excludedDestinations.  
  
### getExcludedDestinationsValue(int index)
    
    
    public abstract int getExcludedDestinationsValue(int index)

The list of destinations to exclude for this target (corresponds to unchecked check boxes in Merchant Center).

For more information, see [Excluded destination](https://support.google.com/merchants/answer/6324486).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum excluded_destinations = 77; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of excludedDestinations at the given index.  
  
### getExcludedDestinationsValueList()
    
    
    public abstract List<Integer> getExcludedDestinationsValueList()

The list of destinations to exclude for this target (corresponds to unchecked check boxes in Merchant Center).

For more information, see [Excluded destination](https://support.google.com/merchants/answer/6324486).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum excluded_destinations = 77; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for excludedDestinations.  
  
### getExpirationDate()
    
    
    public abstract Timestamp getExpirationDate()

Date on which the item should expire, as specified upon insertion, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format. The actual expiration date is exposed in `productstatuses` as [googleExpirationDate](https://support.google.com/merchants/answer/6324499) and might be earlier if `expirationDate` is too far in the future.

`.google.protobuf.Timestamp expiration_date = 16;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The expirationDate.  
  
### getExpirationDateOrBuilder()
    
    
    public abstract TimestampOrBuilder getExpirationDateOrBuilder()

Date on which the item should expire, as specified upon insertion, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format. The actual expiration date is exposed in `productstatuses` as [googleExpirationDate](https://support.google.com/merchants/answer/6324499) and might be earlier if `expirationDate` is too far in the future.

`.google.protobuf.Timestamp expiration_date = 16;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getExternalSellerId()
    
    
    public abstract String getExternalSellerId()

Required for multi-seller accounts. Use this attribute if you're a marketplace uploading products for various sellers to your multi-seller account.

`optional string external_seller_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The externalSellerId.  
  
### getExternalSellerIdBytes()
    
    
    public abstract ByteString getExternalSellerIdBytes()

Required for multi-seller accounts. Use this attribute if you're a marketplace uploading products for various sellers to your multi-seller account.

`optional string external_seller_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for externalSellerId.  
  
### getFreeShippingThreshold(int index)
    
    
    public abstract FreeShippingThreshold getFreeShippingThreshold(int index)

Conditions to be met for a product to have free shipping.

` repeated .google.shopping.merchant.products.v1.FreeShippingThreshold free_shipping_threshold = 135; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FreeShippingThreshold](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.FreeShippingThreshold)` |   
  
### getFreeShippingThresholdCount()
    
    
    public abstract int getFreeShippingThresholdCount()

Conditions to be met for a product to have free shipping.

` repeated .google.shopping.merchant.products.v1.FreeShippingThreshold free_shipping_threshold = 135; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFreeShippingThresholdList()
    
    
    public abstract List<FreeShippingThreshold> getFreeShippingThresholdList()

Conditions to be met for a product to have free shipping.

` repeated .google.shopping.merchant.products.v1.FreeShippingThreshold free_shipping_threshold = 135; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FreeShippingThreshold](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.FreeShippingThreshold)>` |   
  
### getFreeShippingThresholdOrBuilder(int index)
    
    
    public abstract FreeShippingThresholdOrBuilder getFreeShippingThresholdOrBuilder(int index)

Conditions to be met for a product to have free shipping.

` repeated .google.shopping.merchant.products.v1.FreeShippingThreshold free_shipping_threshold = 135; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FreeShippingThresholdOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.FreeShippingThresholdOrBuilder)` |   
  
### getFreeShippingThresholdOrBuilderList()
    
    
    public abstract List<? extends FreeShippingThresholdOrBuilder> getFreeShippingThresholdOrBuilderList()

Conditions to be met for a product to have free shipping.

` repeated .google.shopping.merchant.products.v1.FreeShippingThreshold free_shipping_threshold = 135; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.FreeShippingThresholdOrBuilder>` |   
  
### getFuelConsumption()
    
    
    public abstract ProductAttributes.FuelConsumption getFuelConsumption()

The [fuel consumption](https://support.google.com/google-ads/answer/14543580) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.FuelConsumption fuel_consumption = 154; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.FuelConsumption](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.FuelConsumption)` | The fuelConsumption.  
  
### getFuelConsumptionDischargedBattery()
    
    
    public abstract ProductAttributes.FuelConsumption getFuelConsumptionDischargedBattery()

The fuel consumption of the vehicle when the hybrid battery is discharged. See the [Help Center article](https://support.google.com/google-ads/answer/15162033) for more information.

` .google.shopping.merchant.products.v1.ProductAttributes.FuelConsumption fuel_consumption_discharged_battery = 155; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.FuelConsumption](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.FuelConsumption)` | The fuelConsumptionDischargedBattery.  
  
### getFuelConsumptionDischargedBatteryOrBuilder()
    
    
    public abstract ProductAttributes.FuelConsumptionOrBuilder getFuelConsumptionDischargedBatteryOrBuilder()

The fuel consumption of the vehicle when the hybrid battery is discharged. See the [Help Center article](https://support.google.com/google-ads/answer/15162033) for more information.

` .google.shopping.merchant.products.v1.ProductAttributes.FuelConsumption fuel_consumption_discharged_battery = 155; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.FuelConsumptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.FuelConsumptionOrBuilder)` |   
  
### getFuelConsumptionOrBuilder()
    
    
    public abstract ProductAttributes.FuelConsumptionOrBuilder getFuelConsumptionOrBuilder()

The [fuel consumption](https://support.google.com/google-ads/answer/14543580) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.FuelConsumption fuel_consumption = 154; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.FuelConsumptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.FuelConsumptionOrBuilder)` |   
  
### getGender()
    
    
    public abstract Gender getGender()

Target [gender](https://support.google.com/merchants/answer/6324479) of the item.

`optional .google.shopping.merchant.products.v1.Gender gender = 24;`

**Returns**  
---  
**Type** | **Description**  
`[Gender](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.Gender)` | The gender.  
  
### getGenderValue()
    
    
    public abstract int getGenderValue()

Target [gender](https://support.google.com/merchants/answer/6324479) of the item.

`optional .google.shopping.merchant.products.v1.Gender gender = 24;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for gender.  
  
### getGoogleProductCategory()
    
    
    public abstract String getGoogleProductCategory()

Google's category of the item (see [Google product taxonomy](https://support.google.com/merchants/answer/1705911)). When querying products, this field will contain the user provided value. There is currently no way to get back the auto assigned google product categories through the API.

`optional string google_product_category = 25;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The googleProductCategory.  
  
### getGoogleProductCategoryBytes()
    
    
    public abstract ByteString getGoogleProductCategoryBytes()

Google's category of the item (see [Google product taxonomy](https://support.google.com/merchants/answer/1705911)). When querying products, this field will contain the user provided value. There is currently no way to get back the auto assigned google product categories through the API.

`optional string google_product_category = 25;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for googleProductCategory.  
  
### getGtins(int index)
    
    
    public abstract String getGtins(int index)

Global Trade Item Numbers ([GTIN](https://support.google.com/merchants/answer/6324461)) of the item. You can provide up to 10 GTINs.

`repeated string gtins = 140;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gtins at the given index.  
  
### getGtinsBytes(int index)
    
    
    public abstract ByteString getGtinsBytes(int index)

Global Trade Item Numbers ([GTIN](https://support.google.com/merchants/answer/6324461)) of the item. You can provide up to 10 GTINs.

`repeated string gtins = 140;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the gtins at the given index.  
  
### getGtinsCount()
    
    
    public abstract int getGtinsCount()

Global Trade Item Numbers ([GTIN](https://support.google.com/merchants/answer/6324461)) of the item. You can provide up to 10 GTINs.

`repeated string gtins = 140;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of gtins.  
  
### getGtinsList()
    
    
    public abstract List<String> getGtinsList()

Global Trade Item Numbers ([GTIN](https://support.google.com/merchants/answer/6324461)) of the item. You can provide up to 10 GTINs.

`repeated string gtins = 140;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the gtins.  
  
### getHandlingCutoffTimes(int index)
    
    
    public abstract HandlingCutoffTime getHandlingCutoffTimes(int index)

The handling cutoff times for shipping.

` repeated .google.shopping.merchant.products.v1.HandlingCutoffTime handling_cutoff_times = 141; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HandlingCutoffTime](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.HandlingCutoffTime)` |   
  
### getHandlingCutoffTimesCount()
    
    
    public abstract int getHandlingCutoffTimesCount()

The handling cutoff times for shipping.

` repeated .google.shopping.merchant.products.v1.HandlingCutoffTime handling_cutoff_times = 141; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHandlingCutoffTimesList()
    
    
    public abstract List<HandlingCutoffTime> getHandlingCutoffTimesList()

The handling cutoff times for shipping.

` repeated .google.shopping.merchant.products.v1.HandlingCutoffTime handling_cutoff_times = 141; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HandlingCutoffTime](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.HandlingCutoffTime)>` |   
  
### getHandlingCutoffTimesOrBuilder(int index)
    
    
    public abstract HandlingCutoffTimeOrBuilder getHandlingCutoffTimesOrBuilder(int index)

The handling cutoff times for shipping.

` repeated .google.shopping.merchant.products.v1.HandlingCutoffTime handling_cutoff_times = 141; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HandlingCutoffTimeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.HandlingCutoffTimeOrBuilder)` |   
  
### getHandlingCutoffTimesOrBuilderList()
    
    
    public abstract List<? extends HandlingCutoffTimeOrBuilder> getHandlingCutoffTimesOrBuilderList()

The handling cutoff times for shipping.

` repeated .google.shopping.merchant.products.v1.HandlingCutoffTime handling_cutoff_times = 141; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.HandlingCutoffTimeOrBuilder>` |   
  
### getIdentifierExists()
    
    
    public abstract boolean getIdentifierExists()

Set this value to false when the item does not have unique product identifiers appropriate to its category, such as GTIN, MPN, and brand. Defaults to true, if not provided.

`optional bool identifier_exists = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The identifierExists.  
  
### getImageLink()
    
    
    public abstract String getImageLink()

URL of an image of the item.

`optional string image_link = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The imageLink.  
  
### getImageLinkBytes()
    
    
    public abstract ByteString getImageLinkBytes()

URL of an image of the item.

`optional string image_link = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for imageLink.  
  
### getIncludedDestinations(int index)
    
    
    public abstract Destination.DestinationEnum getIncludedDestinations(int index)

The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in `excludedDestinations`.

For more information, see [Included destination](https://support.google.com/merchants/answer/7501026).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum included_destinations = 76; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Destination.DestinationEnum` | The includedDestinations at the given index.  
  
### getIncludedDestinationsCount()
    
    
    public abstract int getIncludedDestinationsCount()

The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in `excludedDestinations`.

For more information, see [Included destination](https://support.google.com/merchants/answer/7501026).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum included_destinations = 76; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of includedDestinations.  
  
### getIncludedDestinationsList()
    
    
    public abstract List<Destination.DestinationEnum> getIncludedDestinationsList()

The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in `excludedDestinations`.

For more information, see [Included destination](https://support.google.com/merchants/answer/7501026).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum included_destinations = 76; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.shopping.type.Destination.DestinationEnum>` | A list containing the includedDestinations.  
  
### getIncludedDestinationsValue(int index)
    
    
    public abstract int getIncludedDestinationsValue(int index)

The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in `excludedDestinations`.

For more information, see [Included destination](https://support.google.com/merchants/answer/7501026).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum included_destinations = 76; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of includedDestinations at the given index.  
  
### getIncludedDestinationsValueList()
    
    
    public abstract List<Integer> getIncludedDestinationsValueList()

The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in `excludedDestinations`.

For more information, see [Included destination](https://support.google.com/merchants/answer/7501026).

Note: We recommend setting destinations on datasources level for most use cases. Use this field within products to only setup exceptions.

`repeated .google.shopping.type.Destination.DestinationEnum included_destinations = 76; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for includedDestinations.  
  
### getInstallment()
    
    
    public abstract ProductInstallment getInstallment()

Number and amount of installments to pay for an item.

`.google.shopping.merchant.products.v1.ProductInstallment installment = 32;`

**Returns**  
---  
**Type** | **Description**  
`[ProductInstallment](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductInstallment)` | The installment.  
  
### getInstallmentOrBuilder()
    
    
    public abstract ProductInstallmentOrBuilder getInstallmentOrBuilder()

Number and amount of installments to pay for an item.

`.google.shopping.merchant.products.v1.ProductInstallment installment = 32;`

**Returns**  
---  
**Type** | **Description**  
`[ProductInstallmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductInstallmentOrBuilder)` |   
  
### getIsBundle()
    
    
    public abstract boolean getIsBundle()

Whether the item is a business-defined sub-API. A [sub-API](https://support.google.com/merchants/answer/6324449) is a custom grouping of different products sold by a business for a single price.

`optional bool is_bundle = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isBundle.  
  
### getItemGroupId()
    
    
    public abstract String getItemGroupId()

Shared identifier for all variants of the same product.

`optional string item_group_id = 27;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The itemGroupId.  
  
### getItemGroupIdBytes()
    
    
    public abstract ByteString getItemGroupIdBytes()

Shared identifier for all variants of the same product.

`optional string item_group_id = 27;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for itemGroupId.  
  
### getItemGroupTitle()
    
    
    public abstract String getItemGroupTitle()

Optional. Represents the [title of the product group](https://support.google.com/merchants/answer/17085146) to which this variant product belongs. This can be used along with the [item group id](https://support.google.com/merchants/answer/6324507) attribute. It lets you perform better grouping of variant products, and helps identifying common product characteristics more efficiently.

`string item_group_title = 175 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The itemGroupTitle.  
  
### getItemGroupTitleBytes()
    
    
    public abstract ByteString getItemGroupTitleBytes()

Optional. Represents the [title of the product group](https://support.google.com/merchants/answer/17085146) to which this variant product belongs. This can be used along with the [item group id](https://support.google.com/merchants/answer/6324507) attribute. It lets you perform better grouping of variant products, and helps identifying common product characteristics more efficiently.

`string item_group_title = 175 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for itemGroupTitle.  
  
### getLatitude()
    
    
    public abstract double getLatitude()

The latitude of the property. The value must be between -90 (inclusive) and 90 (inclusive), up to 6 decimal places.

`optional double latitude = 180;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The latitude.  
  
### getLeaseTerm()
    
    
    public abstract ProductAttributes.LeaseTerm getLeaseTerm()

The lease term of the property.

`.google.shopping.merchant.products.v1.ProductAttributes.LeaseTerm lease_term = 195; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.LeaseTerm](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.LeaseTerm)` | The leaseTerm.  
  
### getLeaseTermOrBuilder()
    
    
    public abstract ProductAttributes.LeaseTermOrBuilder getLeaseTermOrBuilder()

The lease term of the property.

`.google.shopping.merchant.products.v1.ProductAttributes.LeaseTerm lease_term = 195; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.LeaseTermOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.LeaseTermOrBuilder)` |   
  
### getLifestyleImageLinks(int index)
    
    
    public abstract String getLifestyleImageLinks(int index)

Additional URLs of lifestyle images of the item, used to explicitly identify images that showcase your item in a real-world context. See the [Help Center article](https://support.google.com/merchants/answer/9103186) for more information.

`repeated string lifestyle_image_links = 14;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The lifestyleImageLinks at the given index.  
  
### getLifestyleImageLinksBytes(int index)
    
    
    public abstract ByteString getLifestyleImageLinksBytes(int index)

Additional URLs of lifestyle images of the item, used to explicitly identify images that showcase your item in a real-world context. See the [Help Center article](https://support.google.com/merchants/answer/9103186) for more information.

`repeated string lifestyle_image_links = 14;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the lifestyleImageLinks at the given index.  
  
### getLifestyleImageLinksCount()
    
    
    public abstract int getLifestyleImageLinksCount()

Additional URLs of lifestyle images of the item, used to explicitly identify images that showcase your item in a real-world context. See the [Help Center article](https://support.google.com/merchants/answer/9103186) for more information.

`repeated string lifestyle_image_links = 14;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of lifestyleImageLinks.  
  
### getLifestyleImageLinksList()
    
    
    public abstract List<String> getLifestyleImageLinksList()

Additional URLs of lifestyle images of the item, used to explicitly identify images that showcase your item in a real-world context. See the [Help Center article](https://support.google.com/merchants/answer/9103186) for more information.

`repeated string lifestyle_image_links = 14;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the lifestyleImageLinks.  
  
### getLink()
    
    
    public abstract String getLink()

URL directly linking to your item's page on your online store.

`optional string link = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The link.  
  
### getLinkBytes()
    
    
    public abstract ByteString getLinkBytes()

URL directly linking to your item's page on your online store.

`optional string link = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for link.  
  
### getLinkTemplate()
    
    
    public abstract String getLinkTemplate()

[Link template](https://support.google.com/merchants/answer/13871172) for business hosted local storefront.

`optional string link_template = 82;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The linkTemplate.  
  
### getLinkTemplateBytes()
    
    
    public abstract ByteString getLinkTemplateBytes()

[Link template](https://support.google.com/merchants/answer/13871172) for business hosted local storefront.

`optional string link_template = 82;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for linkTemplate.  
  
### getLongitude()
    
    
    public abstract double getLongitude()

The longitude of the property. The value must be between -180 (inclusive) and 180 (inclusive), up to 6 decimal places.

`optional double longitude = 181;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The longitude.  
  
### getLoyaltyPoints()
    
    
    public abstract LoyaltyPoints getLoyaltyPoints()

Loyalty points that users receive after purchasing the item. Japan only.

`.google.shopping.merchant.products.v1.LoyaltyPoints loyalty_points = 34;`

**Returns**  
---  
**Type** | **Description**  
`[LoyaltyPoints](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.LoyaltyPoints)` | The loyaltyPoints.  
  
### getLoyaltyPointsOrBuilder()
    
    
    public abstract LoyaltyPointsOrBuilder getLoyaltyPointsOrBuilder()

Loyalty points that users receive after purchasing the item. Japan only.

`.google.shopping.merchant.products.v1.LoyaltyPoints loyalty_points = 34;`

**Returns**  
---  
**Type** | **Description**  
`[LoyaltyPointsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.LoyaltyPointsOrBuilder)` |   
  
### getLoyaltyPrograms(int index)
    
    
    public abstract LoyaltyProgram getLoyaltyPrograms(int index)

A list of loyalty program information that is used to surface loyalty benefits (for example, better pricing, points, etc) to the user of this item.

`repeated .google.shopping.merchant.products.v1.LoyaltyProgram loyalty_programs = 136; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LoyaltyProgram](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.LoyaltyProgram)` |   
  
### getLoyaltyProgramsCount()
    
    
    public abstract int getLoyaltyProgramsCount()

A list of loyalty program information that is used to surface loyalty benefits (for example, better pricing, points, etc) to the user of this item.

`repeated .google.shopping.merchant.products.v1.LoyaltyProgram loyalty_programs = 136; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLoyaltyProgramsList()
    
    
    public abstract List<LoyaltyProgram> getLoyaltyProgramsList()

A list of loyalty program information that is used to surface loyalty benefits (for example, better pricing, points, etc) to the user of this item.

`repeated .google.shopping.merchant.products.v1.LoyaltyProgram loyalty_programs = 136; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LoyaltyProgram](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.LoyaltyProgram)>` |   
  
### getLoyaltyProgramsOrBuilder(int index)
    
    
    public abstract LoyaltyProgramOrBuilder getLoyaltyProgramsOrBuilder(int index)

A list of loyalty program information that is used to surface loyalty benefits (for example, better pricing, points, etc) to the user of this item.

`repeated .google.shopping.merchant.products.v1.LoyaltyProgram loyalty_programs = 136; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LoyaltyProgramOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.LoyaltyProgramOrBuilder)` |   
  
### getLoyaltyProgramsOrBuilderList()
    
    
    public abstract List<? extends LoyaltyProgramOrBuilder> getLoyaltyProgramsOrBuilderList()

A list of loyalty program information that is used to surface loyalty benefits (for example, better pricing, points, etc) to the user of this item.

`repeated .google.shopping.merchant.products.v1.LoyaltyProgram loyalty_programs = 136; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.LoyaltyProgramOrBuilder>` |   
  
### getMaterial()
    
    
    public abstract String getMaterial()

The [material](https://support.google.com/merchants/answer/6324410) of which the item is made. For example, "Leather" or "Cotton".

`optional string material = 28;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The material.  
  
### getMaterialBytes()
    
    
    public abstract ByteString getMaterialBytes()

The [material](https://support.google.com/merchants/answer/6324410) of which the item is made. For example, "Leather" or "Cotton".

`optional string material = 28;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for material.  
  
### getMaxEnergyEfficiencyClass()
    
    
    public abstract EnergyEfficiencyClass getMaxEnergyEfficiencyClass()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass max_energy_efficiency_class = 55; `

**Returns**  
---  
**Type** | **Description**  
`[EnergyEfficiencyClass](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.EnergyEfficiencyClass)` | The maxEnergyEfficiencyClass.  
  
### getMaxEnergyEfficiencyClassValue()
    
    
    public abstract int getMaxEnergyEfficiencyClassValue()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass max_energy_efficiency_class = 55; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for maxEnergyEfficiencyClass.  
  
### getMaxHandlingTime()
    
    
    public abstract long getMaxHandlingTime()

Maximal product handling time (in business days).

`optional int64 max_handling_time = 44;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxHandlingTime.  
  
### getMaximumRetailPrice()
    
    
    public abstract Price getMaximumRetailPrice()

Maximum retail price (MRP) of the item. Applicable to India only.

`.google.shopping.type.Price maximum_retail_price = 139;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The maximumRetailPrice.  
  
### getMaximumRetailPriceOrBuilder()
    
    
    public abstract PriceOrBuilder getMaximumRetailPriceOrBuilder()

Maximum retail price (MRP) of the item. Applicable to India only.

`.google.shopping.type.Price maximum_retail_price = 139;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getMileage()
    
    
    public abstract ProductAttributes.Mileage getMileage()

The number of miles/kms on the vehicle. See the [Mileage](https://support.google.com/google-ads/answer/14156166) for more information.

`.google.shopping.merchant.products.v1.ProductAttributes.Mileage mileage = 152;`

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.Mileage](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.Mileage)` | The mileage.  
  
### getMileageOrBuilder()
    
    
    public abstract ProductAttributes.MileageOrBuilder getMileageOrBuilder()

The number of miles/kms on the vehicle. See the [Mileage](https://support.google.com/google-ads/answer/14156166) for more information.

`.google.shopping.merchant.products.v1.ProductAttributes.Mileage mileage = 152;`

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.MileageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.MileageOrBuilder)` |   
  
### getMinEnergyEfficiencyClass()
    
    
    public abstract EnergyEfficiencyClass getMinEnergyEfficiencyClass()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass min_energy_efficiency_class = 54; `

**Returns**  
---  
**Type** | **Description**  
`[EnergyEfficiencyClass](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.EnergyEfficiencyClass)` | The minEnergyEfficiencyClass.  
  
### getMinEnergyEfficiencyClassValue()
    
    
    public abstract int getMinEnergyEfficiencyClassValue()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass min_energy_efficiency_class = 54; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for minEnergyEfficiencyClass.  
  
### getMinHandlingTime()
    
    
    public abstract long getMinHandlingTime()

Minimal product handling time (in business days).

`optional int64 min_handling_time = 45;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The minHandlingTime.  
  
### getMinimumOrderValues(int index)
    
    
    public abstract ProductMinimumOrderValue getMinimumOrderValues(int index)

The [minimum value](https://support.google.com/merchants/answer/16989009) in the cart before a customer can initiate checkout. Supports multiple minimum order values. Different minimum order values can be specified per country, service and surface. Maximum entries: 100.

` repeated .google.shopping.merchant.products.v1.ProductMinimumOrderValue minimum_order_values = 146; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductMinimumOrderValue](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductMinimumOrderValue)` |   
  
### getMinimumOrderValuesCount()
    
    
    public abstract int getMinimumOrderValuesCount()

The [minimum value](https://support.google.com/merchants/answer/16989009) in the cart before a customer can initiate checkout. Supports multiple minimum order values. Different minimum order values can be specified per country, service and surface. Maximum entries: 100.

` repeated .google.shopping.merchant.products.v1.ProductMinimumOrderValue minimum_order_values = 146; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMinimumOrderValuesList()
    
    
    public abstract List<ProductMinimumOrderValue> getMinimumOrderValuesList()

The [minimum value](https://support.google.com/merchants/answer/16989009) in the cart before a customer can initiate checkout. Supports multiple minimum order values. Different minimum order values can be specified per country, service and surface. Maximum entries: 100.

` repeated .google.shopping.merchant.products.v1.ProductMinimumOrderValue minimum_order_values = 146; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProductMinimumOrderValue](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductMinimumOrderValue)>` |   
  
### getMinimumOrderValuesOrBuilder(int index)
    
    
    public abstract ProductMinimumOrderValueOrBuilder getMinimumOrderValuesOrBuilder(int index)

The [minimum value](https://support.google.com/merchants/answer/16989009) in the cart before a customer can initiate checkout. Supports multiple minimum order values. Different minimum order values can be specified per country, service and surface. Maximum entries: 100.

` repeated .google.shopping.merchant.products.v1.ProductMinimumOrderValue minimum_order_values = 146; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductMinimumOrderValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductMinimumOrderValueOrBuilder)` |   
  
### getMinimumOrderValuesOrBuilderList()
    
    
    public abstract List<? extends ProductMinimumOrderValueOrBuilder> getMinimumOrderValuesOrBuilderList()

The [minimum value](https://support.google.com/merchants/answer/16989009) in the cart before a customer can initiate checkout. Supports multiple minimum order values. Different minimum order values can be specified per country, service and surface. Maximum entries: 100.

` repeated .google.shopping.merchant.products.v1.ProductMinimumOrderValue minimum_order_values = 146; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductMinimumOrderValueOrBuilder>` |   
  
### getMobileLink()
    
    
    public abstract String getMobileLink()

URL for the mobile-optimized version of your item's landing page.

`optional string mobile_link = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mobileLink.  
  
### getMobileLinkBytes()
    
    
    public abstract ByteString getMobileLinkBytes()

URL for the mobile-optimized version of your item's landing page.

`optional string mobile_link = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mobileLink.  
  
### getMobileLinkTemplate()
    
    
    public abstract String getMobileLinkTemplate()

[Link template](https://support.google.com/merchants/answer/13870216) for business hosted local storefront optimized for mobile devices.

`optional string mobile_link_template = 83;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mobileLinkTemplate.  
  
### getMobileLinkTemplateBytes()
    
    
    public abstract ByteString getMobileLinkTemplateBytes()

[Link template](https://support.google.com/merchants/answer/13870216) for business hosted local storefront optimized for mobile devices.

`optional string mobile_link_template = 83;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mobileLinkTemplate.  
  
### getModel()
    
    
    public abstract String getModel()

The [Model](https://support.google.com/google-ads/answer/14154511) of the vehicle, such as `LX`, `EX`, and others.

`string model = 148;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The model.  
  
### getModelBytes()
    
    
    public abstract ByteString getModelBytes()

The [Model](https://support.google.com/google-ads/answer/14154511) of the vehicle, such as `LX`, `EX`, and others.

`string model = 148;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for model.  
  
### getMpn()
    
    
    public abstract String getMpn()

Manufacturer Part Number ([MPN](https://support.google.com/merchants/answer/6324482)) of the item.

`optional string mpn = 29;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mpn.  
  
### getMpnBytes()
    
    
    public abstract ByteString getMpnBytes()

Manufacturer Part Number ([MPN](https://support.google.com/merchants/answer/6324482)) of the item.

`optional string mpn = 29;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mpn.  
  
### getMultipack()
    
    
    public abstract long getMultipack()

The number of identical products in a business-defined multipack.

`optional int64 multipack = 58;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The multipack.  
  
### getNeighborhood()
    
    
    public abstract String getNeighborhood()

The neighborhood (locality) of the property, such as `Wallingford`, `Greenwood`, etc.

`string neighborhood = 182;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The neighborhood.  
  
### getNeighborhoodBytes()
    
    
    public abstract ByteString getNeighborhoodBytes()

The neighborhood (locality) of the property, such as `Wallingford`, `Greenwood`, etc.

`string neighborhood = 182;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for neighborhood.  
  
### getNumberOfBathrooms()
    
    
    public abstract double getNumberOfBathrooms()

The number of bathrooms in the property. The value must be greater than 0 and a multiple of 0.5.

`optional double number_of_bathrooms = 187;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The numberOfBathrooms.  
  
### getNumberOfBedrooms()
    
    
    public abstract double getNumberOfBedrooms()

The number of bedrooms in the property. The value must be greater than or equal to 0 and a multiple of 1.0.

`optional double number_of_bedrooms = 186;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The numberOfBedrooms.  
  
### getNumberOfUnits()
    
    
    public abstract long getNumberOfUnits()

The number of units available for a specific floor plan of the property. The value must be greater than 0.

`optional int64 number_of_units = 184;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The numberOfUnits.  
  
### getPattern()
    
    
    public abstract String getPattern()

The item's [pattern](https://support.google.com/merchants/answer/6324483). For example, polka dots.

`optional string pattern = 30;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pattern.  
  
### getPatternBytes()
    
    
    public abstract ByteString getPatternBytes()

The item's [pattern](https://support.google.com/merchants/answer/6324483). For example, polka dots.

`optional string pattern = 30;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pattern.  
  
### getPause()
    
    
    public abstract Pause getPause()

Publication of this item will be temporarily [paused](https://support.google.com/merchants/answer/11909930).

`optional .google.shopping.merchant.products.v1.Pause pause = 13;`

**Returns**  
---  
**Type** | **Description**  
`[Pause](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.Pause)` | The pause.  
  
### getPauseValue()
    
    
    public abstract int getPauseValue()

Publication of this item will be temporarily [paused](https://support.google.com/merchants/answer/11909930).

`optional .google.shopping.merchant.products.v1.Pause pause = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for pause.  
  
### getPetPolicy()
    
    
    public abstract ProductAttributes.PetPolicy getPetPolicy()

The pet policy for the property.

`.google.shopping.merchant.products.v1.ProductAttributes.PetPolicy pet_policy = 191; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.PetPolicy](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.PetPolicy)` | The petPolicy.  
  
### getPetPolicyOrBuilder()
    
    
    public abstract ProductAttributes.PetPolicyOrBuilder getPetPolicyOrBuilder()

The pet policy for the property.

`.google.shopping.merchant.products.v1.ProductAttributes.PetPolicy pet_policy = 191; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.PetPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.PetPolicyOrBuilder)` |   
  
### getPickupCost()
    
    
    public abstract PickupCost getPickupCost()

Optional. The [pickup cost](https://support.google.com/merchants/answer/16988704) for an item when a customer buys it online and picks it up at a store.

` optional .google.shopping.merchant.products.v1.PickupCost pickup_cost = 172 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PickupCost](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.PickupCost)` | The pickupCost.  
  
### getPickupCostOrBuilder()
    
    
    public abstract PickupCostOrBuilder getPickupCostOrBuilder()

Optional. The [pickup cost](https://support.google.com/merchants/answer/16988704) for an item when a customer buys it online and picks it up at a store.

` optional .google.shopping.merchant.products.v1.PickupCost pickup_cost = 172 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PickupCostOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.PickupCostOrBuilder)` |   
  
### getPickupMethod()
    
    
    public abstract PickupMethod getPickupMethod()

The [pickup](https://support.google.com/merchants/answer/14634021) option for the item.

`optional .google.shopping.merchant.products.v1.PickupMethod pickup_method = 80;`

**Returns**  
---  
**Type** | **Description**  
`[PickupMethod](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.PickupMethod)` | The pickupMethod.  
  
### getPickupMethodValue()
    
    
    public abstract int getPickupMethodValue()

The [pickup](https://support.google.com/merchants/answer/14634021) option for the item.

`optional .google.shopping.merchant.products.v1.PickupMethod pickup_method = 80;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for pickupMethod.  
  
### getPickupSla()
    
    
    public abstract PickupSla getPickupSla()

Item store pickup timeline. For more information, see [Pickup SLA](https://support.google.com/merchants/answer/14635400).

`optional .google.shopping.merchant.products.v1.PickupSla pickup_sla = 81;`

**Returns**  
---  
**Type** | **Description**  
`[PickupSla](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.PickupSla)` | The pickupSla.  
  
### getPickupSlaValue()
    
    
    public abstract int getPickupSlaValue()

Item store pickup timeline. For more information, see [Pickup SLA](https://support.google.com/merchants/answer/14635400).

`optional .google.shopping.merchant.products.v1.PickupSla pickup_sla = 81;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for pickupSla.  
  
### getPopularityRank()
    
    
    public abstract float getPopularityRank()

Optional. Indicates the [popularity](https://support.google.com/merchants/answer/17085297) of the product in a merchant's inventory. Using a scale of 0.0 (lowest) to 100.0 (highest).

`float popularity_rank = 174 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The popularityRank.  
  
### getPrice()
    
    
    public abstract Price getPrice()

Price of the item.

`.google.shopping.type.Price price = 31;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The price.  
  
### getPriceOrBuilder()
    
    
    public abstract PriceOrBuilder getPriceOrBuilder()

Price of the item.

`.google.shopping.type.Price price = 31;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getProductDetails(int index)
    
    
    public abstract ProductDetail getProductDetails(int index)

Technical specification or additional product details.

`repeated .google.shopping.merchant.products.v1.ProductDetail product_details = 63;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductDetail](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDetail)` |   
  
### getProductDetailsCount()
    
    
    public abstract int getProductDetailsCount()

Technical specification or additional product details.

`repeated .google.shopping.merchant.products.v1.ProductDetail product_details = 63;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getProductDetailsList()
    
    
    public abstract List<ProductDetail> getProductDetailsList()

Technical specification or additional product details.

`repeated .google.shopping.merchant.products.v1.ProductDetail product_details = 63;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProductDetail](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDetail)>` |   
  
### getProductDetailsOrBuilder(int index)
    
    
    public abstract ProductDetailOrBuilder getProductDetailsOrBuilder(int index)

Technical specification or additional product details.

`repeated .google.shopping.merchant.products.v1.ProductDetail product_details = 63;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductDetailOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDetailOrBuilder)` |   
  
### getProductDetailsOrBuilderList()
    
    
    public abstract List<? extends ProductDetailOrBuilder> getProductDetailsOrBuilderList()

Technical specification or additional product details.

`repeated .google.shopping.merchant.products.v1.ProductDetail product_details = 63;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductDetailOrBuilder>` |   
  
### getProductFee(int index)
    
    
    public abstract ProductAttributes.ProductFee getProductFee(int index)

The product fee for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ProductFee product_fee = 193; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.ProductFee](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ProductFee)` |   
  
### getProductFeeCount()
    
    
    public abstract int getProductFeeCount()

The product fee for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ProductFee product_fee = 193; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getProductFeeList()
    
    
    public abstract List<ProductAttributes.ProductFee> getProductFeeList()

The product fee for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ProductFee product_fee = 193; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProductFee](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ProductFee)>` |   
  
### getProductFeeOrBuilder(int index)
    
    
    public abstract ProductAttributes.ProductFeeOrBuilder getProductFeeOrBuilder(int index)

The product fee for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ProductFee product_fee = 193; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.ProductFeeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ProductFeeOrBuilder)` |   
  
### getProductFeeOrBuilderList()
    
    
    public abstract List<? extends ProductAttributes.ProductFeeOrBuilder> getProductFeeOrBuilderList()

The product fee for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ProductFee product_fee = 193; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductAttributes.ProductFeeOrBuilder>` |   
  
### getProductHeight()
    
    
    public abstract ProductDimension getProductHeight()

The height of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_height = 119;`

**Returns**  
---  
**Type** | **Description**  
`[ProductDimension](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDimension)` | The productHeight.  
  
### getProductHeightOrBuilder()
    
    
    public abstract ProductDimensionOrBuilder getProductHeightOrBuilder()

The height of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_height = 119;`

**Returns**  
---  
**Type** | **Description**  
`[ProductDimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDimensionOrBuilder)` |   
  
### getProductHighlights(int index)
    
    
    public abstract String getProductHighlights(int index)

Bullet points describing the most relevant [product highlights](https://support.google.com/merchants/answer/9216100).

`repeated string product_highlights = 64;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productHighlights at the given index.  
  
### getProductHighlightsBytes(int index)
    
    
    public abstract ByteString getProductHighlightsBytes(int index)

Bullet points describing the most relevant [product highlights](https://support.google.com/merchants/answer/9216100).

`repeated string product_highlights = 64;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the productHighlights at the given index.  
  
### getProductHighlightsCount()
    
    
    public abstract int getProductHighlightsCount()

Bullet points describing the most relevant [product highlights](https://support.google.com/merchants/answer/9216100).

`repeated string product_highlights = 64;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of productHighlights.  
  
### getProductHighlightsList()
    
    
    public abstract List<String> getProductHighlightsList()

Bullet points describing the most relevant [product highlights](https://support.google.com/merchants/answer/9216100).

`repeated string product_highlights = 64;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the productHighlights.  
  
### getProductLength()
    
    
    public abstract ProductDimension getProductLength()

The length of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_length = 120;`

**Returns**  
---  
**Type** | **Description**  
`[ProductDimension](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDimension)` | The productLength.  
  
### getProductLengthOrBuilder()
    
    
    public abstract ProductDimensionOrBuilder getProductLengthOrBuilder()

The length of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_length = 120;`

**Returns**  
---  
**Type** | **Description**  
`[ProductDimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDimensionOrBuilder)` |   
  
### getProductTypes(int index)
    
    
    public abstract String getProductTypes(int index)

Categories of the item (formatted as in [product data specification](https://support.google.com/merchants/answer/7052112#product_category)).

`repeated string product_types = 35;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productTypes at the given index.  
  
### getProductTypesBytes(int index)
    
    
    public abstract ByteString getProductTypesBytes(int index)

Categories of the item (formatted as in [product data specification](https://support.google.com/merchants/answer/7052112#product_category)).

`repeated string product_types = 35;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the productTypes at the given index.  
  
### getProductTypesCount()
    
    
    public abstract int getProductTypesCount()

Categories of the item (formatted as in [product data specification](https://support.google.com/merchants/answer/7052112#product_category)).

`repeated string product_types = 35;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of productTypes.  
  
### getProductTypesList()
    
    
    public abstract List<String> getProductTypesList()

Categories of the item (formatted as in [product data specification](https://support.google.com/merchants/answer/7052112#product_category)).

`repeated string product_types = 35;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the productTypes.  
  
### getProductWeight()
    
    
    public abstract ProductWeight getProductWeight()

The weight of the product in the units provided. The value must be between 0 (exclusive) and 2000 (inclusive).

`.google.shopping.merchant.products.v1.ProductWeight product_weight = 122;`

**Returns**  
---  
**Type** | **Description**  
`[ProductWeight](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductWeight)` | The productWeight.  
  
### getProductWeightOrBuilder()
    
    
    public abstract ProductWeightOrBuilder getProductWeightOrBuilder()

The weight of the product in the units provided. The value must be between 0 (exclusive) and 2000 (inclusive).

`.google.shopping.merchant.products.v1.ProductWeight product_weight = 122;`

**Returns**  
---  
**Type** | **Description**  
`[ProductWeightOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductWeightOrBuilder)` |   
  
### getProductWidth()
    
    
    public abstract ProductDimension getProductWidth()

The width of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_width = 121;`

**Returns**  
---  
**Type** | **Description**  
`[ProductDimension](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDimension)` | The productWidth.  
  
### getProductWidthOrBuilder()
    
    
    public abstract ProductDimensionOrBuilder getProductWidthOrBuilder()

The width of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_width = 121;`

**Returns**  
---  
**Type** | **Description**  
`[ProductDimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductDimensionOrBuilder)` |   
  
### getPromotionIds(int index)
    
    
    public abstract String getPromotionIds(int index)

The unique ID of a promotion.

`repeated string promotion_ids = 70;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The promotionIds at the given index.  
  
### getPromotionIdsBytes(int index)
    
    
    public abstract ByteString getPromotionIdsBytes(int index)

The unique ID of a promotion.

`repeated string promotion_ids = 70;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the promotionIds at the given index.  
  
### getPromotionIdsCount()
    
    
    public abstract int getPromotionIdsCount()

The unique ID of a promotion.

`repeated string promotion_ids = 70;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of promotionIds.  
  
### getPromotionIdsList()
    
    
    public abstract List<String> getPromotionIdsList()

The unique ID of a promotion.

`repeated string promotion_ids = 70;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the promotionIds.  
  
### getPropertyName()
    
    
    public abstract String getPropertyName()

The name of the property.

`string property_name = 185;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The propertyName.  
  
### getPropertyNameBytes()
    
    
    public abstract ByteString getPropertyNameBytes()

The name of the property.

`string property_name = 185;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for propertyName.  
  
### getPropertyType()
    
    
    public abstract ProductAttributes.PropertyType getPropertyType()

The type of property.

`.google.shopping.merchant.products.v1.ProductAttributes.PropertyType property_type = 188; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.PropertyType](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.PropertyType)` | The propertyType.  
  
### getPropertyTypeValue()
    
    
    public abstract int getPropertyTypeValue()

The type of property.

`.google.shopping.merchant.products.v1.ProductAttributes.PropertyType property_type = 188; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for propertyType.  
  
### getQuestionsAndAnswers(int index)
    
    
    public abstract ProductAttributes.QuestionAndAnswer getQuestionsAndAnswers(int index)

Optional. Contains user-, merchant-, and manufacturer-authored [questions and answers](https://support.google.com/merchants/answer/17085211) about the product. Max 30 question and answer pairs. Max 10000 characters total. Each question can have max 1000 characters. Each answer can have max 1000 characters.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswer questions_and_answers = 173 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.QuestionAndAnswer](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswer)` |   
  
### getQuestionsAndAnswersCount()
    
    
    public abstract int getQuestionsAndAnswersCount()

Optional. Contains user-, merchant-, and manufacturer-authored [questions and answers](https://support.google.com/merchants/answer/17085211) about the product. Max 30 question and answer pairs. Max 10000 characters total. Each question can have max 1000 characters. Each answer can have max 1000 characters.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswer questions_and_answers = 173 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getQuestionsAndAnswersList()
    
    
    public abstract List<ProductAttributes.QuestionAndAnswer> getQuestionsAndAnswersList()

Optional. Contains user-, merchant-, and manufacturer-authored [questions and answers](https://support.google.com/merchants/answer/17085211) about the product. Max 30 question and answer pairs. Max 10000 characters total. Each question can have max 1000 characters. Each answer can have max 1000 characters.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswer questions_and_answers = 173 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[QuestionAndAnswer](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswer)>` |   
  
### getQuestionsAndAnswersOrBuilder(int index)
    
    
    public abstract ProductAttributes.QuestionAndAnswerOrBuilder getQuestionsAndAnswersOrBuilder(int index)

Optional. Contains user-, merchant-, and manufacturer-authored [questions and answers](https://support.google.com/merchants/answer/17085211) about the product. Max 30 question and answer pairs. Max 10000 characters total. Each question can have max 1000 characters. Each answer can have max 1000 characters.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswer questions_and_answers = 173 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.QuestionAndAnswerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswerOrBuilder)` |   
  
### getQuestionsAndAnswersOrBuilderList()
    
    
    public abstract List<? extends ProductAttributes.QuestionAndAnswerOrBuilder> getQuestionsAndAnswersOrBuilderList()

Optional. Contains user-, merchant-, and manufacturer-authored [questions and answers](https://support.google.com/merchants/answer/17085211) about the product. Max 30 question and answer pairs. Max 10000 characters total. Each question can have max 1000 characters. Each answer can have max 1000 characters.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswer questions_and_answers = 173 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductAttributes.QuestionAndAnswerOrBuilder>` |   
  
### getRelatedProducts(int index)
    
    
    public abstract ProductAttributes.RelatedProduct getRelatedProducts(int index)

Optional. Specifies how other [products are related](https://support.google.com/merchants/answer/17085213) to this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.RelatedProduct related_products = 178 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.RelatedProduct](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.RelatedProduct)` |   
  
### getRelatedProductsCount()
    
    
    public abstract int getRelatedProductsCount()

Optional. Specifies how other [products are related](https://support.google.com/merchants/answer/17085213) to this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.RelatedProduct related_products = 178 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRelatedProductsList()
    
    
    public abstract List<ProductAttributes.RelatedProduct> getRelatedProductsList()

Optional. Specifies how other [products are related](https://support.google.com/merchants/answer/17085213) to this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.RelatedProduct related_products = 178 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RelatedProduct](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.RelatedProduct)>` |   
  
### getRelatedProductsOrBuilder(int index)
    
    
    public abstract ProductAttributes.RelatedProductOrBuilder getRelatedProductsOrBuilder(int index)

Optional. Specifies how other [products are related](https://support.google.com/merchants/answer/17085213) to this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.RelatedProduct related_products = 178 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.RelatedProductOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.RelatedProductOrBuilder)` |   
  
### getRelatedProductsOrBuilderList()
    
    
    public abstract List<? extends ProductAttributes.RelatedProductOrBuilder> getRelatedProductsOrBuilderList()

Optional. Specifies how other [products are related](https://support.google.com/merchants/answer/17085213) to this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.RelatedProduct related_products = 178 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductAttributes.RelatedProductOrBuilder>` |   
  
### getReturnPolicyLabel()
    
    
    public abstract String getReturnPolicyLabel()

The return label of the product, used to group products in account-level return policies. Max. 100 characters. For more information, see [Return policy label](https://support.google.com/merchants/answer/9445425).

`optional string return_policy_label = 170;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The returnPolicyLabel.  
  
### getReturnPolicyLabelBytes()
    
    
    public abstract ByteString getReturnPolicyLabelBytes()

The return label of the product, used to group products in account-level return policies. Max. 100 characters. For more information, see [Return policy label](https://support.google.com/merchants/answer/9445425).

`optional string return_policy_label = 170;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for returnPolicyLabel.  
  
### getReturns(int index)
    
    
    public abstract ProductAttributes.Returns getReturns(int index)

Optional. [Return rules](https://support.google.com/merchants/answer/17081382) for the product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.Returns returns = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.Returns](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.Returns)` |   
  
### getReturnsCount()
    
    
    public abstract int getReturnsCount()

Optional. [Return rules](https://support.google.com/merchants/answer/17081382) for the product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.Returns returns = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getReturnsList()
    
    
    public abstract List<ProductAttributes.Returns> getReturnsList()

Optional. [Return rules](https://support.google.com/merchants/answer/17081382) for the product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.Returns returns = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Returns](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.Returns)>` |   
  
### getReturnsOrBuilder(int index)
    
    
    public abstract ProductAttributes.ReturnsOrBuilder getReturnsOrBuilder(int index)

Optional. [Return rules](https://support.google.com/merchants/answer/17081382) for the product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.Returns returns = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.ReturnsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ReturnsOrBuilder)` |   
  
### getReturnsOrBuilderList()
    
    
    public abstract List<? extends ProductAttributes.ReturnsOrBuilder> getReturnsOrBuilderList()

Optional. [Return rules](https://support.google.com/merchants/answer/17081382) for the product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.Returns returns = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductAttributes.ReturnsOrBuilder>` |   
  
### getSalePrice()
    
    
    public abstract Price getSalePrice()

Advertised sale price of the item.

`.google.shopping.type.Price sale_price = 36;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The salePrice.  
  
### getSalePriceEffectiveDate()
    
    
    public abstract Interval getSalePriceEffectiveDate()

Date range during which the item is on sale, see [product data specification](https://support.google.com/merchants/answer/7052112#price_and_availability).

`.google.type.Interval sale_price_effective_date = 37;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Interval` | The salePriceEffectiveDate.  
  
### getSalePriceEffectiveDateOrBuilder()
    
    
    public abstract IntervalOrBuilder getSalePriceEffectiveDateOrBuilder()

Date range during which the item is on sale, see [product data specification](https://support.google.com/merchants/answer/7052112#price_and_availability).

`.google.type.Interval sale_price_effective_date = 37;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.IntervalOrBuilder` |   
  
### getSalePriceOrBuilder()
    
    
    public abstract PriceOrBuilder getSalePriceOrBuilder()

Advertised sale price of the item.

`.google.shopping.type.Price sale_price = 36;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getSellOnGoogleQuantity()
    
    
    public abstract long getSellOnGoogleQuantity()

The quantity of the product that is available for selling on Google. Supported only for online products.

`optional int64 sell_on_google_quantity = 38;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sellOnGoogleQuantity.  
  
### getShipping(int index)
    
    
    public abstract Shipping getShipping(int index)

Shipping rules.

`repeated .google.shopping.merchant.products.v1.Shipping shipping = 39;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Shipping](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.Shipping)` |   
  
### getShippingCount()
    
    
    public abstract int getShippingCount()

Shipping rules.

`repeated .google.shopping.merchant.products.v1.Shipping shipping = 39;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getShippingHandlingBusinessDays(int index)
    
    
    public abstract ProductAttributes.ShippingBusinessDaysConfig getShippingHandlingBusinessDays(int index)

The business days during which orders can be handled. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_handling_business_days = 143; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.ShippingBusinessDaysConfig](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig)` |   
  
### getShippingHandlingBusinessDaysCount()
    
    
    public abstract int getShippingHandlingBusinessDaysCount()

The business days during which orders can be handled. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_handling_business_days = 143; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getShippingHandlingBusinessDaysList()
    
    
    public abstract List<ProductAttributes.ShippingBusinessDaysConfig> getShippingHandlingBusinessDaysList()

The business days during which orders can be handled. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_handling_business_days = 143; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ShippingBusinessDaysConfig](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig)>` |   
  
### getShippingHandlingBusinessDaysOrBuilder(int index)
    
    
    public abstract ProductAttributes.ShippingBusinessDaysConfigOrBuilder getShippingHandlingBusinessDaysOrBuilder(int index)

The business days during which orders can be handled. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_handling_business_days = 143; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.ShippingBusinessDaysConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfigOrBuilder)` |   
  
### getShippingHandlingBusinessDaysOrBuilderList()
    
    
    public abstract List<? extends ProductAttributes.ShippingBusinessDaysConfigOrBuilder> getShippingHandlingBusinessDaysOrBuilderList()

The business days during which orders can be handled. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_handling_business_days = 143; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfigOrBuilder>` |   
  
### getShippingHeight()
    
    
    public abstract ShippingDimension getShippingHeight()

Height of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_height = 43;`

**Returns**  
---  
**Type** | **Description**  
`[ShippingDimension](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingDimension)` | The shippingHeight.  
  
### getShippingHeightOrBuilder()
    
    
    public abstract ShippingDimensionOrBuilder getShippingHeightOrBuilder()

Height of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_height = 43;`

**Returns**  
---  
**Type** | **Description**  
`[ShippingDimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingDimensionOrBuilder)` |   
  
### getShippingLabel()
    
    
    public abstract String getShippingLabel()

The shipping label of the product, used to group products in account-level shipping rules. Max. 100 characters. For more information, see [Shipping label](https://support.google.com/merchants/answer/6324504).

`optional string shipping_label = 46;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The shippingLabel.  
  
### getShippingLabelBytes()
    
    
    public abstract ByteString getShippingLabelBytes()

The shipping label of the product, used to group products in account-level shipping rules. Max. 100 characters. For more information, see [Shipping label](https://support.google.com/merchants/answer/6324504).

`optional string shipping_label = 46;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for shippingLabel.  
  
### getShippingLength()
    
    
    public abstract ShippingDimension getShippingLength()

Length of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_length = 41;`

**Returns**  
---  
**Type** | **Description**  
`[ShippingDimension](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingDimension)` | The shippingLength.  
  
### getShippingLengthOrBuilder()
    
    
    public abstract ShippingDimensionOrBuilder getShippingLengthOrBuilder()

Length of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_length = 41;`

**Returns**  
---  
**Type** | **Description**  
`[ShippingDimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingDimensionOrBuilder)` |   
  
### getShippingList()
    
    
    public abstract List<Shipping> getShippingList()

Shipping rules.

`repeated .google.shopping.merchant.products.v1.Shipping shipping = 39;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Shipping](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.Shipping)>` |   
  
### getShippingOrBuilder(int index)
    
    
    public abstract ShippingOrBuilder getShippingOrBuilder(int index)

Shipping rules.

`repeated .google.shopping.merchant.products.v1.Shipping shipping = 39;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ShippingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingOrBuilder)` |   
  
### getShippingOrBuilderList()
    
    
    public abstract List<? extends ShippingOrBuilder> getShippingOrBuilderList()

Shipping rules.

`repeated .google.shopping.merchant.products.v1.Shipping shipping = 39;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ShippingOrBuilder>` |   
  
### getShippingTransitBusinessDays(int index)
    
    
    public abstract ProductAttributes.ShippingBusinessDaysConfig getShippingTransitBusinessDays(int index)

The business days during which orders are in transit. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_transit_business_days = 144; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.ShippingBusinessDaysConfig](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig)` |   
  
### getShippingTransitBusinessDaysCount()
    
    
    public abstract int getShippingTransitBusinessDaysCount()

The business days during which orders are in transit. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_transit_business_days = 144; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getShippingTransitBusinessDaysList()
    
    
    public abstract List<ProductAttributes.ShippingBusinessDaysConfig> getShippingTransitBusinessDaysList()

The business days during which orders are in transit. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_transit_business_days = 144; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ShippingBusinessDaysConfig](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig)>` |   
  
### getShippingTransitBusinessDaysOrBuilder(int index)
    
    
    public abstract ProductAttributes.ShippingBusinessDaysConfigOrBuilder getShippingTransitBusinessDaysOrBuilder(int index)

The business days during which orders are in transit. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_transit_business_days = 144; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.ShippingBusinessDaysConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfigOrBuilder)` |   
  
### getShippingTransitBusinessDaysOrBuilderList()
    
    
    public abstract List<? extends ProductAttributes.ShippingBusinessDaysConfigOrBuilder> getShippingTransitBusinessDaysOrBuilderList()

The business days during which orders are in transit. If not provided, Monday to Friday business days will be assumed.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfig shipping_transit_business_days = 144; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductAttributes.ShippingBusinessDaysConfigOrBuilder>` |   
  
### getShippingWeight()
    
    
    public abstract ShippingWeight getShippingWeight()

Weight of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingWeight shipping_weight = 40;`

**Returns**  
---  
**Type** | **Description**  
`[ShippingWeight](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingWeight)` | The shippingWeight.  
  
### getShippingWeightOrBuilder()
    
    
    public abstract ShippingWeightOrBuilder getShippingWeightOrBuilder()

Weight of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingWeight shipping_weight = 40;`

**Returns**  
---  
**Type** | **Description**  
`[ShippingWeightOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingWeightOrBuilder)` |   
  
### getShippingWidth()
    
    
    public abstract ShippingDimension getShippingWidth()

Width of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_width = 42;`

**Returns**  
---  
**Type** | **Description**  
`[ShippingDimension](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingDimension)` | The shippingWidth.  
  
### getShippingWidthOrBuilder()
    
    
    public abstract ShippingDimensionOrBuilder getShippingWidthOrBuilder()

Width of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_width = 42;`

**Returns**  
---  
**Type** | **Description**  
`[ShippingDimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ShippingDimensionOrBuilder)` |   
  
### getShoppingAdsExcludedCountries(int index)
    
    
    public abstract String getShoppingAdsExcludedCountries(int index)

List of country codes [(ISO 3166-1 alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to exclude the offer from Shopping Ads destination. Countries from this list are removed from countries configured in data source settings.

`repeated string shopping_ads_excluded_countries = 78;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The shoppingAdsExcludedCountries at the given index.  
  
### getShoppingAdsExcludedCountriesBytes(int index)
    
    
    public abstract ByteString getShoppingAdsExcludedCountriesBytes(int index)

List of country codes [(ISO 3166-1 alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to exclude the offer from Shopping Ads destination. Countries from this list are removed from countries configured in data source settings.

`repeated string shopping_ads_excluded_countries = 78;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the shoppingAdsExcludedCountries at the given index.  
  
### getShoppingAdsExcludedCountriesCount()
    
    
    public abstract int getShoppingAdsExcludedCountriesCount()

List of country codes [(ISO 3166-1 alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to exclude the offer from Shopping Ads destination. Countries from this list are removed from countries configured in data source settings.

`repeated string shopping_ads_excluded_countries = 78;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of shoppingAdsExcludedCountries.  
  
### getShoppingAdsExcludedCountriesList()
    
    
    public abstract List<String> getShoppingAdsExcludedCountriesList()

List of country codes [(ISO 3166-1 alpha-2)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) to exclude the offer from Shopping Ads destination. Countries from this list are removed from countries configured in data source settings.

`repeated string shopping_ads_excluded_countries = 78;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the shoppingAdsExcludedCountries.  
  
### getShortTitle()
    
    
    public abstract String getShortTitle()

The short title of the item.

`optional string short_title = 194;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The shortTitle.  
  
### getShortTitleBytes()
    
    
    public abstract ByteString getShortTitleBytes()

The short title of the item.

`optional string short_title = 194;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for shortTitle.  
  
### getSize()
    
    
    public abstract String getSize()

Size of the item. Only one value is allowed. For variants with different sizes, insert a separate product for each size with the same `itemGroupId` value, see [Size](https://support.google.com/merchants/answer/6324492).

`optional string size = 48;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The size.  
  
### getSizeBytes()
    
    
    public abstract ByteString getSizeBytes()

Size of the item. Only one value is allowed. For variants with different sizes, insert a separate product for each size with the same `itemGroupId` value, see [Size](https://support.google.com/merchants/answer/6324492).

`optional string size = 48;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for size.  
  
### getSizeSystem()
    
    
    public abstract SizeSystem getSizeSystem()

System in which the size is specified. Recommended for apparel items. For more information, see [Size system](https://support.google.com/merchants/answer/6324502).

`optional .google.shopping.merchant.products.v1.SizeSystem size_system = 49;`

**Returns**  
---  
**Type** | **Description**  
`[SizeSystem](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.SizeSystem)` | The sizeSystem.  
  
### getSizeSystemValue()
    
    
    public abstract int getSizeSystemValue()

System in which the size is specified. Recommended for apparel items. For more information, see [Size system](https://support.google.com/merchants/answer/6324502).

`optional .google.shopping.merchant.products.v1.SizeSystem size_system = 49;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for sizeSystem.  
  
### getSizeTypes(int index)
    
    
    public abstract SizeType getSizeTypes(int index)

The cut of the item. It can be used to represent combined size types for apparel items. Maximum two of size types can be provided, see [Size type](https://support.google.com/merchants/answer/6324497).

`repeated .google.shopping.merchant.products.v1.SizeType size_types = 50;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[SizeType](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.SizeType)` | The sizeTypes at the given index.  
  
### getSizeTypesCount()
    
    
    public abstract int getSizeTypesCount()

The cut of the item. It can be used to represent combined size types for apparel items. Maximum two of size types can be provided, see [Size type](https://support.google.com/merchants/answer/6324497).

`repeated .google.shopping.merchant.products.v1.SizeType size_types = 50;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of sizeTypes.  
  
### getSizeTypesList()
    
    
    public abstract List<SizeType> getSizeTypesList()

The cut of the item. It can be used to represent combined size types for apparel items. Maximum two of size types can be provided, see [Size type](https://support.google.com/merchants/answer/6324497).

`repeated .google.shopping.merchant.products.v1.SizeType size_types = 50;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SizeType](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.SizeType)>` | A list containing the sizeTypes.  
  
### getSizeTypesValue(int index)
    
    
    public abstract int getSizeTypesValue(int index)

The cut of the item. It can be used to represent combined size types for apparel items. Maximum two of size types can be provided, see [Size type](https://support.google.com/merchants/answer/6324497).

`repeated .google.shopping.merchant.products.v1.SizeType size_types = 50;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of sizeTypes at the given index.  
  
### getSizeTypesValueList()
    
    
    public abstract List<Integer> getSizeTypesValueList()

The cut of the item. It can be used to represent combined size types for apparel items. Maximum two of size types can be provided, see [Size type](https://support.google.com/merchants/answer/6324497).

`repeated .google.shopping.merchant.products.v1.SizeType size_types = 50;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for sizeTypes.  
  
### getSpecialtyHousingType()
    
    
    public abstract ProductAttributes.SpecialtyHousingType getSpecialtyHousingType()

The specialty housing type for the property.

` .google.shopping.merchant.products.v1.ProductAttributes.SpecialtyHousingType specialty_housing_type = 192; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.SpecialtyHousingType](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.SpecialtyHousingType)` | The specialtyHousingType.  
  
### getSpecialtyHousingTypeValue()
    
    
    public abstract int getSpecialtyHousingTypeValue()

The specialty housing type for the property.

` .google.shopping.merchant.products.v1.ProductAttributes.SpecialtyHousingType specialty_housing_type = 192; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for specialtyHousingType.  
  
### getStructuredDescription()
    
    
    public abstract StructuredDescription getStructuredDescription()

Structured description, for algorithmically (AI)-generated descriptions.

` optional .google.shopping.merchant.products.v1.StructuredDescription structured_description = 133; `

**Returns**  
---  
**Type** | **Description**  
`[StructuredDescription](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.StructuredDescription)` | The structuredDescription.  
  
### getStructuredDescriptionOrBuilder()
    
    
    public abstract StructuredDescriptionOrBuilder getStructuredDescriptionOrBuilder()

Structured description, for algorithmically (AI)-generated descriptions.

` optional .google.shopping.merchant.products.v1.StructuredDescription structured_description = 133; `

**Returns**  
---  
**Type** | **Description**  
`[StructuredDescriptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.StructuredDescriptionOrBuilder)` |   
  
### getStructuredTitle()
    
    
    public abstract StructuredTitle getStructuredTitle()

Structured title, for algorithmically (AI)-generated titles.

`optional .google.shopping.merchant.products.v1.StructuredTitle structured_title = 132; `

**Returns**  
---  
**Type** | **Description**  
`[StructuredTitle](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.StructuredTitle)` | The structuredTitle.  
  
### getStructuredTitleOrBuilder()
    
    
    public abstract StructuredTitleOrBuilder getStructuredTitleOrBuilder()

Structured title, for algorithmically (AI)-generated titles.

`optional .google.shopping.merchant.products.v1.StructuredTitle structured_title = 132; `

**Returns**  
---  
**Type** | **Description**  
`[StructuredTitleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.StructuredTitleOrBuilder)` |   
  
### getSubscriptionCost()
    
    
    public abstract SubscriptionCost getSubscriptionCost()

Number of periods (weeks, months or years) and amount of payment per period for an item with an associated subscription contract.

`.google.shopping.merchant.products.v1.SubscriptionCost subscription_cost = 33;`

**Returns**  
---  
**Type** | **Description**  
`[SubscriptionCost](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.SubscriptionCost)` | The subscriptionCost.  
  
### getSubscriptionCostOrBuilder()
    
    
    public abstract SubscriptionCostOrBuilder getSubscriptionCostOrBuilder()

Number of periods (weeks, months or years) and amount of payment per period for an item with an associated subscription contract.

`.google.shopping.merchant.products.v1.SubscriptionCost subscription_cost = 33;`

**Returns**  
---  
**Type** | **Description**  
`[SubscriptionCostOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.SubscriptionCostOrBuilder)` |   
  
### getSustainabilityIncentives(int index)
    
    
    public abstract ProductSustainabilityIncentive getSustainabilityIncentives(int index)

The list of sustainability incentive programs.

` repeated .google.shopping.merchant.products.v1.ProductSustainabilityIncentive sustainability_incentives = 138; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSustainabilityIncentive](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductSustainabilityIncentive)` |   
  
### getSustainabilityIncentivesCount()
    
    
    public abstract int getSustainabilityIncentivesCount()

The list of sustainability incentive programs.

` repeated .google.shopping.merchant.products.v1.ProductSustainabilityIncentive sustainability_incentives = 138; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSustainabilityIncentivesList()
    
    
    public abstract List<ProductSustainabilityIncentive> getSustainabilityIncentivesList()

The list of sustainability incentive programs.

` repeated .google.shopping.merchant.products.v1.ProductSustainabilityIncentive sustainability_incentives = 138; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ProductSustainabilityIncentive](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductSustainabilityIncentive)>` |   
  
### getSustainabilityIncentivesOrBuilder(int index)
    
    
    public abstract ProductSustainabilityIncentiveOrBuilder getSustainabilityIncentivesOrBuilder(int index)

The list of sustainability incentive programs.

` repeated .google.shopping.merchant.products.v1.ProductSustainabilityIncentive sustainability_incentives = 138; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductSustainabilityIncentiveOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductSustainabilityIncentiveOrBuilder)` |   
  
### getSustainabilityIncentivesOrBuilderList()
    
    
    public abstract List<? extends ProductSustainabilityIncentiveOrBuilder> getSustainabilityIncentivesOrBuilderList()

The list of sustainability incentive programs.

` repeated .google.shopping.merchant.products.v1.ProductSustainabilityIncentive sustainability_incentives = 138; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductSustainabilityIncentiveOrBuilder>` |   
  
### getTitle()
    
    
    public abstract String getTitle()

Title of the item.

`optional string title = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The title.  
  
### getTitleBytes()
    
    
    public abstract ByteString getTitleBytes()

Title of the item.

`optional string title = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for title.  
  
### getTransitTimeLabel()
    
    
    public abstract String getTransitTimeLabel()

The transit time label of the product, used to group product in account-level transit time tables.

`optional string transit_time_label = 47;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The transitTimeLabel.  
  
### getTransitTimeLabelBytes()
    
    
    public abstract ByteString getTransitTimeLabelBytes()

The transit time label of the product, used to group product in account-level transit time tables.

`optional string transit_time_label = 47;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for transitTimeLabel.  
  
### getTrim()
    
    
    public abstract String getTrim()

The [Trim](https://support.google.com/google-ads/answer/14154176) of the vehicle model, such as `S`, `SV`, `SL` and others.

`string trim = 149;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The trim.  
  
### getTrimBytes()
    
    
    public abstract ByteString getTrimBytes()

The [Trim](https://support.google.com/google-ads/answer/14154176) of the vehicle model, such as `S`, `SV`, `SL` and others.

`string trim = 149;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for trim.  
  
### getUnitArea()
    
    
    public abstract ProductAttributes.UnitArea getUnitArea()

The unit area of the property, such as `1000 sqft`.

`.google.shopping.merchant.products.v1.ProductAttributes.UnitArea unit_area = 183;`

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.UnitArea](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.UnitArea)` | The unitArea.  
  
### getUnitAreaOrBuilder()
    
    
    public abstract ProductAttributes.UnitAreaOrBuilder getUnitAreaOrBuilder()

The unit area of the property, such as `1000 sqft`.

`.google.shopping.merchant.products.v1.ProductAttributes.UnitArea unit_area = 183;`

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.UnitAreaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.UnitAreaOrBuilder)` |   
  
### getUnitPricingBaseMeasure()
    
    
    public abstract UnitPricingBaseMeasure getUnitPricingBaseMeasure()

The preference of the denominator of the unit price.

` .google.shopping.merchant.products.v1.UnitPricingBaseMeasure unit_pricing_base_measure = 57; `

**Returns**  
---  
**Type** | **Description**  
`[UnitPricingBaseMeasure](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.UnitPricingBaseMeasure)` | The unitPricingBaseMeasure.  
  
### getUnitPricingBaseMeasureOrBuilder()
    
    
    public abstract UnitPricingBaseMeasureOrBuilder getUnitPricingBaseMeasureOrBuilder()

The preference of the denominator of the unit price.

` .google.shopping.merchant.products.v1.UnitPricingBaseMeasure unit_pricing_base_measure = 57; `

**Returns**  
---  
**Type** | **Description**  
`[UnitPricingBaseMeasureOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.UnitPricingBaseMeasureOrBuilder)` |   
  
### getUnitPricingMeasure()
    
    
    public abstract UnitPricingMeasure getUnitPricingMeasure()

The measure and dimension of an item.

`.google.shopping.merchant.products.v1.UnitPricingMeasure unit_pricing_measure = 56; `

**Returns**  
---  
**Type** | **Description**  
`[UnitPricingMeasure](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.UnitPricingMeasure)` | The unitPricingMeasure.  
  
### getUnitPricingMeasureOrBuilder()
    
    
    public abstract UnitPricingMeasureOrBuilder getUnitPricingMeasureOrBuilder()

The measure and dimension of an item.

`.google.shopping.merchant.products.v1.UnitPricingMeasure unit_pricing_measure = 56; `

**Returns**  
---  
**Type** | **Description**  
`[UnitPricingMeasureOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.UnitPricingMeasureOrBuilder)` |   
  
### getUtilitiesIncluded(int index)
    
    
    public abstract ProductAttributes.UtilitiesIncluded getUtilitiesIncluded(int index)

The utilities included for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.UtilitiesIncluded utilities_included = 190; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.UtilitiesIncluded](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.UtilitiesIncluded)` | The utilitiesIncluded at the given index.  
  
### getUtilitiesIncludedCount()
    
    
    public abstract int getUtilitiesIncludedCount()

The utilities included for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.UtilitiesIncluded utilities_included = 190; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of utilitiesIncluded.  
  
### getUtilitiesIncludedList()
    
    
    public abstract List<ProductAttributes.UtilitiesIncluded> getUtilitiesIncludedList()

The utilities included for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.UtilitiesIncluded utilities_included = 190; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UtilitiesIncluded](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.UtilitiesIncluded)>` | A list containing the utilitiesIncluded.  
  
### getUtilitiesIncludedValue(int index)
    
    
    public abstract int getUtilitiesIncludedValue(int index)

The utilities included for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.UtilitiesIncluded utilities_included = 190; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of utilitiesIncluded at the given index.  
  
### getUtilitiesIncludedValueList()
    
    
    public abstract List<Integer> getUtilitiesIncludedValueList()

The utilities included for the property.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.UtilitiesIncluded utilities_included = 190; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for utilitiesIncluded.  
  
### getVariantOptions(int index)
    
    
    public abstract ProductAttributes.VariantOption getVariantOptions(int index)

Optional. Contains the [list of all variant-identifying options](https://support.google.com/merchants/answer/17085214) of this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.VariantOption variant_options = 177 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.VariantOption](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.VariantOption)` |   
  
### getVariantOptionsCount()
    
    
    public abstract int getVariantOptionsCount()

Optional. Contains the [list of all variant-identifying options](https://support.google.com/merchants/answer/17085214) of this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.VariantOption variant_options = 177 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVariantOptionsList()
    
    
    public abstract List<ProductAttributes.VariantOption> getVariantOptionsList()

Optional. Contains the [list of all variant-identifying options](https://support.google.com/merchants/answer/17085214) of this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.VariantOption variant_options = 177 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[VariantOption](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.VariantOption)>` |   
  
### getVariantOptionsOrBuilder(int index)
    
    
    public abstract ProductAttributes.VariantOptionOrBuilder getVariantOptionsOrBuilder(int index)

Optional. Contains the [list of all variant-identifying options](https://support.google.com/merchants/answer/17085214) of this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.VariantOption variant_options = 177 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.VariantOptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.VariantOptionOrBuilder)` |   
  
### getVariantOptionsOrBuilderList()
    
    
    public abstract List<? extends ProductAttributes.VariantOptionOrBuilder> getVariantOptionsOrBuilderList()

Optional. Contains the [list of all variant-identifying options](https://support.google.com/merchants/answer/17085214) of this product.

` repeated .google.shopping.merchant.products.v1.ProductAttributes.VariantOption variant_options = 177 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.products.v1.ProductAttributes.VariantOptionOrBuilder>` |   
  
### getVehicleAllInPrice()
    
    
    public abstract Price getVehicleAllInPrice()

The all-in advertised price for a vehicle, which includes costs for the following – any accessories attached to the vehicle, environmental levies, extra warranty, fuel, freight, pre-delivery inspection (PDI), dealer fees for handling licensing, provincial regulatory fees, miscellaneous dealer charges for security etching and nitrogen tire fill, and factory-to-customer or dealer-to-customer discounts or incentives. See the [Vehicle all-in price](https://support.google.com/google-ads/answer/14156981) for more information.

`.google.shopping.type.Price vehicle_all_in_price = 163;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The vehicleAllInPrice.  
  
### getVehicleAllInPriceOrBuilder()
    
    
    public abstract PriceOrBuilder getVehicleAllInPriceOrBuilder()

The all-in advertised price for a vehicle, which includes costs for the following – any accessories attached to the vehicle, environmental levies, extra warranty, fuel, freight, pre-delivery inspection (PDI), dealer fees for handling licensing, provincial regulatory fees, miscellaneous dealer charges for security etching and nitrogen tire fill, and factory-to-customer or dealer-to-customer discounts or incentives. See the [Vehicle all-in price](https://support.google.com/google-ads/answer/14156981) for more information.

`.google.shopping.type.Price vehicle_all_in_price = 163;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getVehicleExpenses()
    
    
    public abstract Price getVehicleExpenses()

The miscellaneous expenses like insurance and registration fees of the vehicle. See the [Vehicle expenses](https://support.google.com/google-ads/answer/15957154) for more information.

`.google.shopping.type.Price vehicle_expenses = 167;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The vehicleExpenses.  
  
### getVehicleExpensesOrBuilder()
    
    
    public abstract PriceOrBuilder getVehicleExpensesOrBuilder()

The miscellaneous expenses like insurance and registration fees of the vehicle. See the [Vehicle expenses](https://support.google.com/google-ads/answer/15957154) for more information.

`.google.shopping.type.Price vehicle_expenses = 167;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getVehicleMandatoryInspectionIncluded()
    
    
    public abstract boolean getVehicleMandatoryInspectionIncluded()

Whether the vehicle is sold with mandatory inspection and maintenance performed before delivery. See the [Vehicle mandatory inspection included](https://support.google.com/google-ads/answer/15956630) for more information.`

`bool vehicle_mandatory_inspection_included = 166;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The vehicleMandatoryInspectionIncluded.  
  
### getVehicleMsrp()
    
    
    public abstract Price getVehicleMsrp()

The MSRP (Manufacturer Suggested Retail Price) for the vehicle in its current configuration. See the [Vehicle MSRP](https://support.google.com/google-ads/answer/14154171) for more information.

`.google.shopping.type.Price vehicle_msrp = 162;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.Price` | The vehicleMsrp.  
  
### getVehicleMsrpOrBuilder()
    
    
    public abstract PriceOrBuilder getVehicleMsrpOrBuilder()

The MSRP (Manufacturer Suggested Retail Price) for the vehicle in its current configuration. See the [Vehicle MSRP](https://support.google.com/google-ads/answer/14154171) for more information.

`.google.shopping.type.Price vehicle_msrp = 162;`

**Returns**  
---  
**Type** | **Description**  
`com.google.shopping.type.PriceOrBuilder` |   
  
### getVehiclePriceType()
    
    
    public abstract ProductAttributes.VehiclePriceType getVehiclePriceType()

The [price type](https://support.google.com/google-ads/answer/14592783) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.VehiclePriceType vehicle_price_type = 164; `

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.VehiclePriceType](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.VehiclePriceType)` | The vehiclePriceType.  
  
### getVehiclePriceTypeValue()
    
    
    public abstract int getVehiclePriceTypeValue()

The [price type](https://support.google.com/google-ads/answer/14592783) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.VehiclePriceType vehicle_price_type = 164; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for vehiclePriceType.  
  
### getVideoLinks(int index)
    
    
    public abstract String getVideoLinks(int index)

Optional. A list of video URLs for the item. Use this attribute to provide more visuals for your product beyond your image attributes. See the [Help Center article](https://support.google.com/merchants/answer/15216925) for more information.

`repeated string video_links = 169 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The videoLinks at the given index.  
  
### getVideoLinksBytes(int index)
    
    
    public abstract ByteString getVideoLinksBytes(int index)

Optional. A list of video URLs for the item. Use this attribute to provide more visuals for your product beyond your image attributes. See the [Help Center article](https://support.google.com/merchants/answer/15216925) for more information.

`repeated string video_links = 169 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the videoLinks at the given index.  
  
### getVideoLinksCount()
    
    
    public abstract int getVideoLinksCount()

Optional. A list of video URLs for the item. Use this attribute to provide more visuals for your product beyond your image attributes. See the [Help Center article](https://support.google.com/merchants/answer/15216925) for more information.

`repeated string video_links = 169 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of videoLinks.  
  
### getVideoLinksList()
    
    
    public abstract List<String> getVideoLinksList()

Optional. A list of video URLs for the item. Use this attribute to provide more visuals for your product beyond your image attributes. See the [Help Center article](https://support.google.com/merchants/answer/15216925) for more information.

`repeated string video_links = 169 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the videoLinks.  
  
### getVin()
    
    
    public abstract String getVin()

The [Vehicle Identification Number (VIN)](https://support.google.com/google-ads/answer/14154510) of the vehicle.

`string vin = 147;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The vin.  
  
### getVinBytes()
    
    
    public abstract ByteString getVinBytes()

The [Vehicle Identification Number (VIN)](https://support.google.com/google-ads/answer/14154510) of the vehicle.

`string vin = 147;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for vin.  
  
### getVirtualModelLink()
    
    
    public abstract String getVirtualModelLink()

URL of the 3D image of the item. See the [Help Center article](https://support.google.com/merchants/answer/13674896) for more information.

`optional string virtual_model_link = 130;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The virtualModelLink.  
  
### getVirtualModelLinkBytes()
    
    
    public abstract ByteString getVirtualModelLinkBytes()

URL of the 3D image of the item. See the [Help Center article](https://support.google.com/merchants/answer/13674896) for more information.

`optional string virtual_model_link = 130;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for virtualModelLink.  
  
### getWarranty()
    
    
    public abstract ProductAttributes.Warranty getWarranty()

The [warranty](https://support.google.com/merchants/answer/15957626) of the product.

`.google.shopping.merchant.products.v1.ProductAttributes.Warranty warranty = 168;`

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.Warranty](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.Warranty)` | The warranty.  
  
### getWarrantyOrBuilder()
    
    
    public abstract ProductAttributes.WarrantyOrBuilder getWarrantyOrBuilder()

The [warranty](https://support.google.com/merchants/answer/15957626) of the product.

`.google.shopping.merchant.products.v1.ProductAttributes.Warranty warranty = 168;`

**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes.WarrantyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-products/latest/com.google.shopping.merchant.products.v1.ProductAttributes.WarrantyOrBuilder)` |   
  
### getYear()
    
    
    public abstract long getYear()

The [Year](https://support.google.com/google-ads/answer/14152816) of the vehicle model.

`int64 year = 151;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The year.  
  
### hasAdsGrouping()
    
    
    public abstract boolean hasAdsGrouping()

Used to group items in an arbitrary way. Only for CPA%, discouraged otherwise. For more information, see [Display ads attribute](https://support.google.com/merchants/answer/6069387).

`optional string ads_grouping = 59;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adsGrouping field is set.  
  
### hasAdsRedirect()
    
    
    public abstract boolean hasAdsRedirect()

Allows advertisers to override the item URL when the product is shown within the context of Product ads.

`optional string ads_redirect = 61;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adsRedirect field is set.  
  
### hasAdult()
    
    
    public abstract boolean hasAdult()

Set to true if the item is targeted towards adults.

`optional bool adult = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the adult field is set.  
  
### hasAgeGroup()
    
    
    public abstract boolean hasAgeGroup()

Target [age group](https://support.google.com/merchants/answer/6324463) of the item.

`optional .google.shopping.merchant.products.v1.AgeGroup age_group = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ageGroup field is set.  
  
### hasAutoPricingMinPrice()
    
    
    public abstract boolean hasAutoPricingMinPrice()

A safeguard in the [automated discounts](https://support.google.com/merchants/answer/10295759) and "Dynamic Promotions" (<https://support.google.com/merchants/answer/13949249>) projects, ensuring that discounts on business offers do not fall below this value, thereby preserving the offer's value and profitability.

`.google.shopping.type.Price auto_pricing_min_price = 124;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autoPricingMinPrice field is set.  
  
### hasAvailability()
    
    
    public abstract boolean hasAvailability()

[Availability](https://support.google.com/merchants/answer/6324448) status of the item.

`optional .google.shopping.merchant.products.v1.Availability availability = 19;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the availability field is set.  
  
### hasAvailabilityDate()
    
    
    public abstract boolean hasAvailabilityDate()

The day a pre-ordered product becomes available for delivery, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format.

`.google.protobuf.Timestamp availability_date = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the availabilityDate field is set.  
  
### hasBrand()
    
    
    public abstract boolean hasBrand()

[Brand](https://support.google.com/merchants/answer/6324351) of the item. For example, "Google".

`optional string brand = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the brand field is set.  
  
### hasCanonicalLink()
    
    
    public abstract boolean hasCanonicalLink()

URL for the canonical version of your item's landing page.

`optional string canonical_link = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the canonicalLink field is set.  
  
### hasCo2Emissions()
    
    
    public abstract boolean hasCo2Emissions()

The [co2 emission](https://support.google.com/google-ads/answer/14546146) of the vehicle.

`.google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions co2_emissions = 157; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the co2Emissions field is set.  
  
### hasColor()
    
    
    public abstract boolean hasColor()

[Color](https://support.google.com/merchants/answer/6324487) of the item. For example, "red".

`optional string color = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the color field is set.  
  
### hasCondition()
    
    
    public abstract boolean hasCondition()

[Condition](https://support.google.com/merchants/answer/6324469) or state of the item.

`optional .google.shopping.merchant.products.v1.Condition condition = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the condition field is set.  
  
### hasCostOfGoodsSold()
    
    
    public abstract boolean hasCostOfGoodsSold()

Cost of goods sold. Used for gross profit reporting.

`.google.shopping.type.Price cost_of_goods_sold = 62;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the costOfGoodsSold field is set.  
  
### hasCustomLabel0()
    
    
    public abstract boolean hasCustomLabel0()

[Custom label 0](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_0 = 71;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customLabel0 field is set.  
  
### hasCustomLabel1()
    
    
    public abstract boolean hasCustomLabel1()

[Custom label 1](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_1 = 72;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customLabel1 field is set.  
  
### hasCustomLabel2()
    
    
    public abstract boolean hasCustomLabel2()

[Custom label 2](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_2 = 73;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customLabel2 field is set.  
  
### hasCustomLabel3()
    
    
    public abstract boolean hasCustomLabel3()

[Custom label 3](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_3 = 74;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customLabel3 field is set.  
  
### hasCustomLabel4()
    
    
    public abstract boolean hasCustomLabel4()

[Custom label 4](https://support.google.com/merchants/answer/6324473) for custom grouping of items in a Shopping campaign.

`optional string custom_label_4 = 75;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customLabel4 field is set.  
  
### hasDescription()
    
    
    public abstract boolean hasDescription()

Description of the item.

`optional string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasDisclosureDate()
    
    
    public abstract boolean hasDisclosureDate()

The date time when an offer becomes visible in search results across Google’s YouTube surfaces, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format. See [Disclosure date](https://support.google.com/merchants/answer/13034208) for more information.

`.google.protobuf.Timestamp disclosure_date = 79;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the disclosureDate field is set.  
  
### hasDisplayAddress()
    
    
    public abstract boolean hasDisplayAddress()

The display address of the property.

` .google.shopping.merchant.products.v1.ProductAttributes.DisplayAddress display_address = 179; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the displayAddress field is set.  
  
### hasDisplayAdsId()
    
    
    public abstract boolean hasDisplayAdsId()

An identifier for an item for dynamic remarketing campaigns.

`optional string display_ads_id = 65;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the displayAdsId field is set.  
  
### hasDisplayAdsLink()
    
    
    public abstract boolean hasDisplayAdsLink()

URL directly to your item's landing page for dynamic remarketing campaigns.

`optional string display_ads_link = 68;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the displayAdsLink field is set.  
  
### hasDisplayAdsTitle()
    
    
    public abstract boolean hasDisplayAdsTitle()

Title of an item for dynamic remarketing campaigns.

`optional string display_ads_title = 67;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the displayAdsTitle field is set.  
  
### hasDisplayAdsValue()
    
    
    public abstract boolean hasDisplayAdsValue()

Offer margin for dynamic remarketing campaigns. For more information, see [Display ads attribute](https://support.google.com/merchants/answer/6069387).

`optional double display_ads_value = 69;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the displayAdsValue field is set.  
  
### hasElectricRange()
    
    
    public abstract boolean hasElectricRange()

The [electric range](https://support.google.com/google-ads/answer/15162232) of the vehicle in miles/kms.

`.google.shopping.merchant.products.v1.ProductAttributes.Mileage electric_range = 153; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the electricRange field is set.  
  
### hasEnergyConsumption()
    
    
    public abstract boolean hasEnergyConsumption()

The [energy consumption](https://support.google.com/google-ads/answer/14546149) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.EnergyConsumption energy_consumption = 156; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the energyConsumption field is set.  
  
### hasEnergyEfficiencyClass()
    
    
    public abstract boolean hasEnergyEfficiencyClass()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass energy_efficiency_class = 53; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the energyEfficiencyClass field is set.  
  
### hasExpirationDate()
    
    
    public abstract boolean hasExpirationDate()

Date on which the item should expire, as specified upon insertion, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format. The actual expiration date is exposed in `productstatuses` as [googleExpirationDate](https://support.google.com/merchants/answer/6324499) and might be earlier if `expirationDate` is too far in the future.

`.google.protobuf.Timestamp expiration_date = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expirationDate field is set.  
  
### hasExternalSellerId()
    
    
    public abstract boolean hasExternalSellerId()

Required for multi-seller accounts. Use this attribute if you're a marketplace uploading products for various sellers to your multi-seller account.

`optional string external_seller_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the externalSellerId field is set.  
  
### hasFuelConsumption()
    
    
    public abstract boolean hasFuelConsumption()

The [fuel consumption](https://support.google.com/google-ads/answer/14543580) of the vehicle.

` .google.shopping.merchant.products.v1.ProductAttributes.FuelConsumption fuel_consumption = 154; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fuelConsumption field is set.  
  
### hasFuelConsumptionDischargedBattery()
    
    
    public abstract boolean hasFuelConsumptionDischargedBattery()

The fuel consumption of the vehicle when the hybrid battery is discharged. See the [Help Center article](https://support.google.com/google-ads/answer/15162033) for more information.

` .google.shopping.merchant.products.v1.ProductAttributes.FuelConsumption fuel_consumption_discharged_battery = 155; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fuelConsumptionDischargedBattery field is set.  
  
### hasGender()
    
    
    public abstract boolean hasGender()

Target [gender](https://support.google.com/merchants/answer/6324479) of the item.

`optional .google.shopping.merchant.products.v1.Gender gender = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gender field is set.  
  
### hasGoogleProductCategory()
    
    
    public abstract boolean hasGoogleProductCategory()

Google's category of the item (see [Google product taxonomy](https://support.google.com/merchants/answer/1705911)). When querying products, this field will contain the user provided value. There is currently no way to get back the auto assigned google product categories through the API.

`optional string google_product_category = 25;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the googleProductCategory field is set.  
  
### hasIdentifierExists()
    
    
    public abstract boolean hasIdentifierExists()

Set this value to false when the item does not have unique product identifiers appropriate to its category, such as GTIN, MPN, and brand. Defaults to true, if not provided.

`optional bool identifier_exists = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the identifierExists field is set.  
  
### hasImageLink()
    
    
    public abstract boolean hasImageLink()

URL of an image of the item.

`optional string image_link = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the imageLink field is set.  
  
### hasInstallment()
    
    
    public abstract boolean hasInstallment()

Number and amount of installments to pay for an item.

`.google.shopping.merchant.products.v1.ProductInstallment installment = 32;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the installment field is set.  
  
### hasIsBundle()
    
    
    public abstract boolean hasIsBundle()

Whether the item is a business-defined sub-API. A [sub-API](https://support.google.com/merchants/answer/6324449) is a custom grouping of different products sold by a business for a single price.

`optional bool is_bundle = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the isBundle field is set.  
  
### hasItemGroupId()
    
    
    public abstract boolean hasItemGroupId()

Shared identifier for all variants of the same product.

`optional string item_group_id = 27;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the itemGroupId field is set.  
  
### hasLatitude()
    
    
    public abstract boolean hasLatitude()

The latitude of the property. The value must be between -90 (inclusive) and 90 (inclusive), up to 6 decimal places.

`optional double latitude = 180;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the latitude field is set.  
  
### hasLeaseTerm()
    
    
    public abstract boolean hasLeaseTerm()

The lease term of the property.

`.google.shopping.merchant.products.v1.ProductAttributes.LeaseTerm lease_term = 195; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the leaseTerm field is set.  
  
### hasLink()
    
    
    public abstract boolean hasLink()

URL directly linking to your item's page on your online store.

`optional string link = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the link field is set.  
  
### hasLinkTemplate()
    
    
    public abstract boolean hasLinkTemplate()

[Link template](https://support.google.com/merchants/answer/13871172) for business hosted local storefront.

`optional string link_template = 82;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the linkTemplate field is set.  
  
### hasLongitude()
    
    
    public abstract boolean hasLongitude()

The longitude of the property. The value must be between -180 (inclusive) and 180 (inclusive), up to 6 decimal places.

`optional double longitude = 181;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the longitude field is set.  
  
### hasLoyaltyPoints()
    
    
    public abstract boolean hasLoyaltyPoints()

Loyalty points that users receive after purchasing the item. Japan only.

`.google.shopping.merchant.products.v1.LoyaltyPoints loyalty_points = 34;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the loyaltyPoints field is set.  
  
### hasMaterial()
    
    
    public abstract boolean hasMaterial()

The [material](https://support.google.com/merchants/answer/6324410) of which the item is made. For example, "Leather" or "Cotton".

`optional string material = 28;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the material field is set.  
  
### hasMaxEnergyEfficiencyClass()
    
    
    public abstract boolean hasMaxEnergyEfficiencyClass()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass max_energy_efficiency_class = 55; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxEnergyEfficiencyClass field is set.  
  
### hasMaxHandlingTime()
    
    
    public abstract boolean hasMaxHandlingTime()

Maximal product handling time (in business days).

`optional int64 max_handling_time = 44;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxHandlingTime field is set.  
  
### hasMaximumRetailPrice()
    
    
    public abstract boolean hasMaximumRetailPrice()

Maximum retail price (MRP) of the item. Applicable to India only.

`.google.shopping.type.Price maximum_retail_price = 139;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maximumRetailPrice field is set.  
  
### hasMileage()
    
    
    public abstract boolean hasMileage()

The number of miles/kms on the vehicle. See the [Mileage](https://support.google.com/google-ads/answer/14156166) for more information.

`.google.shopping.merchant.products.v1.ProductAttributes.Mileage mileage = 152;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mileage field is set.  
  
### hasMinEnergyEfficiencyClass()
    
    
    public abstract boolean hasMinEnergyEfficiencyClass()

The [energy efficiency class](https://support.google.com/merchants/answer/7562785) as defined in EU directive 2010/30/EU.

` optional .google.shopping.merchant.products.v1.EnergyEfficiencyClass min_energy_efficiency_class = 54; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the minEnergyEfficiencyClass field is set.  
  
### hasMinHandlingTime()
    
    
    public abstract boolean hasMinHandlingTime()

Minimal product handling time (in business days).

`optional int64 min_handling_time = 45;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the minHandlingTime field is set.  
  
### hasMobileLink()
    
    
    public abstract boolean hasMobileLink()

URL for the mobile-optimized version of your item's landing page.

`optional string mobile_link = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mobileLink field is set.  
  
### hasMobileLinkTemplate()
    
    
    public abstract boolean hasMobileLinkTemplate()

[Link template](https://support.google.com/merchants/answer/13870216) for business hosted local storefront optimized for mobile devices.

`optional string mobile_link_template = 83;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mobileLinkTemplate field is set.  
  
### hasMpn()
    
    
    public abstract boolean hasMpn()

Manufacturer Part Number ([MPN](https://support.google.com/merchants/answer/6324482)) of the item.

`optional string mpn = 29;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mpn field is set.  
  
### hasMultipack()
    
    
    public abstract boolean hasMultipack()

The number of identical products in a business-defined multipack.

`optional int64 multipack = 58;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the multipack field is set.  
  
### hasNumberOfBathrooms()
    
    
    public abstract boolean hasNumberOfBathrooms()

The number of bathrooms in the property. The value must be greater than 0 and a multiple of 0.5.

`optional double number_of_bathrooms = 187;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the numberOfBathrooms field is set.  
  
### hasNumberOfBedrooms()
    
    
    public abstract boolean hasNumberOfBedrooms()

The number of bedrooms in the property. The value must be greater than or equal to 0 and a multiple of 1.0.

`optional double number_of_bedrooms = 186;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the numberOfBedrooms field is set.  
  
### hasNumberOfUnits()
    
    
    public abstract boolean hasNumberOfUnits()

The number of units available for a specific floor plan of the property. The value must be greater than 0.

`optional int64 number_of_units = 184;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the numberOfUnits field is set.  
  
### hasPattern()
    
    
    public abstract boolean hasPattern()

The item's [pattern](https://support.google.com/merchants/answer/6324483). For example, polka dots.

`optional string pattern = 30;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pattern field is set.  
  
### hasPause()
    
    
    public abstract boolean hasPause()

Publication of this item will be temporarily [paused](https://support.google.com/merchants/answer/11909930).

`optional .google.shopping.merchant.products.v1.Pause pause = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pause field is set.  
  
### hasPetPolicy()
    
    
    public abstract boolean hasPetPolicy()

The pet policy for the property.

`.google.shopping.merchant.products.v1.ProductAttributes.PetPolicy pet_policy = 191; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the petPolicy field is set.  
  
### hasPickupCost()
    
    
    public abstract boolean hasPickupCost()

Optional. The [pickup cost](https://support.google.com/merchants/answer/16988704) for an item when a customer buys it online and picks it up at a store.

` optional .google.shopping.merchant.products.v1.PickupCost pickup_cost = 172 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pickupCost field is set.  
  
### hasPickupMethod()
    
    
    public abstract boolean hasPickupMethod()

The [pickup](https://support.google.com/merchants/answer/14634021) option for the item.

`optional .google.shopping.merchant.products.v1.PickupMethod pickup_method = 80;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pickupMethod field is set.  
  
### hasPickupSla()
    
    
    public abstract boolean hasPickupSla()

Item store pickup timeline. For more information, see [Pickup SLA](https://support.google.com/merchants/answer/14635400).

`optional .google.shopping.merchant.products.v1.PickupSla pickup_sla = 81;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pickupSla field is set.  
  
### hasPrice()
    
    
    public abstract boolean hasPrice()

Price of the item.

`.google.shopping.type.Price price = 31;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the price field is set.  
  
### hasProductHeight()
    
    
    public abstract boolean hasProductHeight()

The height of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_height = 119;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productHeight field is set.  
  
### hasProductLength()
    
    
    public abstract boolean hasProductLength()

The length of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_length = 120;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productLength field is set.  
  
### hasProductWeight()
    
    
    public abstract boolean hasProductWeight()

The weight of the product in the units provided. The value must be between 0 (exclusive) and 2000 (inclusive).

`.google.shopping.merchant.products.v1.ProductWeight product_weight = 122;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productWeight field is set.  
  
### hasProductWidth()
    
    
    public abstract boolean hasProductWidth()

The width of the product in the units provided. The value must be between 0 (exclusive) and 3000 (inclusive).

`.google.shopping.merchant.products.v1.ProductDimension product_width = 121;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productWidth field is set.  
  
### hasReturnPolicyLabel()
    
    
    public abstract boolean hasReturnPolicyLabel()

The return label of the product, used to group products in account-level return policies. Max. 100 characters. For more information, see [Return policy label](https://support.google.com/merchants/answer/9445425).

`optional string return_policy_label = 170;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the returnPolicyLabel field is set.  
  
### hasSalePrice()
    
    
    public abstract boolean hasSalePrice()

Advertised sale price of the item.

`.google.shopping.type.Price sale_price = 36;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the salePrice field is set.  
  
### hasSalePriceEffectiveDate()
    
    
    public abstract boolean hasSalePriceEffectiveDate()

Date range during which the item is on sale, see [product data specification](https://support.google.com/merchants/answer/7052112#price_and_availability).

`.google.type.Interval sale_price_effective_date = 37;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the salePriceEffectiveDate field is set.  
  
### hasSellOnGoogleQuantity()
    
    
    public abstract boolean hasSellOnGoogleQuantity()

The quantity of the product that is available for selling on Google. Supported only for online products.

`optional int64 sell_on_google_quantity = 38;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sellOnGoogleQuantity field is set.  
  
### hasShippingHeight()
    
    
    public abstract boolean hasShippingHeight()

Height of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_height = 43;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shippingHeight field is set.  
  
### hasShippingLabel()
    
    
    public abstract boolean hasShippingLabel()

The shipping label of the product, used to group products in account-level shipping rules. Max. 100 characters. For more information, see [Shipping label](https://support.google.com/merchants/answer/6324504).

`optional string shipping_label = 46;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shippingLabel field is set.  
  
### hasShippingLength()
    
    
    public abstract boolean hasShippingLength()

Length of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_length = 41;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shippingLength field is set.  
  
### hasShippingWeight()
    
    
    public abstract boolean hasShippingWeight()

Weight of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingWeight shipping_weight = 40;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shippingWeight field is set.  
  
### hasShippingWidth()
    
    
    public abstract boolean hasShippingWidth()

Width of the item for shipping.

`.google.shopping.merchant.products.v1.ShippingDimension shipping_width = 42;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shippingWidth field is set.  
  
### hasShortTitle()
    
    
    public abstract boolean hasShortTitle()

The short title of the item.

`optional string short_title = 194;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shortTitle field is set.  
  
### hasSize()
    
    
    public abstract boolean hasSize()

Size of the item. Only one value is allowed. For variants with different sizes, insert a separate product for each size with the same `itemGroupId` value, see [Size](https://support.google.com/merchants/answer/6324492).

`optional string size = 48;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the size field is set.  
  
### hasSizeSystem()
    
    
    public abstract boolean hasSizeSystem()

System in which the size is specified. Recommended for apparel items. For more information, see [Size system](https://support.google.com/merchants/answer/6324502).

`optional .google.shopping.merchant.products.v1.SizeSystem size_system = 49;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sizeSystem field is set.  
  
### hasStructuredDescription()
    
    
    public abstract boolean hasStructuredDescription()

Structured description, for algorithmically (AI)-generated descriptions.

` optional .google.shopping.merchant.products.v1.StructuredDescription structured_description = 133; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the structuredDescription field is set.  
  
### hasStructuredTitle()
    
    
    public abstract boolean hasStructuredTitle()

Structured title, for algorithmically (AI)-generated titles.

`optional .google.shopping.merchant.products.v1.StructuredTitle structured_title = 132; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the structuredTitle field is set.  
  
### hasSubscriptionCost()
    
    
    public abstract boolean hasSubscriptionCost()

Number of periods (weeks, months or years) and amount of payment per period for an item with an associated subscription contract.

`.google.shopping.merchant.products.v1.SubscriptionCost subscription_cost = 33;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the subscriptionCost field is set.  
  
### hasTitle()
    
    
    public abstract boolean hasTitle()

Title of the item.

`optional string title = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the title field is set.  
  
### hasTransitTimeLabel()
    
    
    public abstract boolean hasTransitTimeLabel()

The transit time label of the product, used to group product in account-level transit time tables.

`optional string transit_time_label = 47;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transitTimeLabel field is set.  
  
### hasUnitArea()
    
    
    public abstract boolean hasUnitArea()

The unit area of the property, such as `1000 sqft`.

`.google.shopping.merchant.products.v1.ProductAttributes.UnitArea unit_area = 183;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the unitArea field is set.  
  
### hasUnitPricingBaseMeasure()
    
    
    public abstract boolean hasUnitPricingBaseMeasure()

The preference of the denominator of the unit price.

` .google.shopping.merchant.products.v1.UnitPricingBaseMeasure unit_pricing_base_measure = 57; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the unitPricingBaseMeasure field is set.  
  
### hasUnitPricingMeasure()
    
    
    public abstract boolean hasUnitPricingMeasure()

The measure and dimension of an item.

`.google.shopping.merchant.products.v1.UnitPricingMeasure unit_pricing_measure = 56; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the unitPricingMeasure field is set.  
  
### hasVehicleAllInPrice()
    
    
    public abstract boolean hasVehicleAllInPrice()

The all-in advertised price for a vehicle, which includes costs for the following – any accessories attached to the vehicle, environmental levies, extra warranty, fuel, freight, pre-delivery inspection (PDI), dealer fees for handling licensing, provincial regulatory fees, miscellaneous dealer charges for security etching and nitrogen tire fill, and factory-to-customer or dealer-to-customer discounts or incentives. See the [Vehicle all-in price](https://support.google.com/google-ads/answer/14156981) for more information.

`.google.shopping.type.Price vehicle_all_in_price = 163;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vehicleAllInPrice field is set.  
  
### hasVehicleExpenses()
    
    
    public abstract boolean hasVehicleExpenses()

The miscellaneous expenses like insurance and registration fees of the vehicle. See the [Vehicle expenses](https://support.google.com/google-ads/answer/15957154) for more information.

`.google.shopping.type.Price vehicle_expenses = 167;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vehicleExpenses field is set.  
  
### hasVehicleMsrp()
    
    
    public abstract boolean hasVehicleMsrp()

The MSRP (Manufacturer Suggested Retail Price) for the vehicle in its current configuration. See the [Vehicle MSRP](https://support.google.com/google-ads/answer/14154171) for more information.

`.google.shopping.type.Price vehicle_msrp = 162;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vehicleMsrp field is set.  
  
### hasVirtualModelLink()
    
    
    public abstract boolean hasVirtualModelLink()

URL of the 3D image of the item. See the [Help Center article](https://support.google.com/merchants/answer/13674896) for more information.

`optional string virtual_model_link = 130;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the virtualModelLink field is set.  
  
### hasWarranty()
    
    
    public abstract boolean hasWarranty()

The [warranty](https://support.google.com/merchants/answer/15957626) of the product.

`.google.shopping.merchant.products.v1.ProductAttributes.Warranty warranty = 168;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the warranty field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
