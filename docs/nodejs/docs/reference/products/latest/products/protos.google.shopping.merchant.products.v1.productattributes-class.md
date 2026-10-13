---
url: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes-class
title: Class protos.google.shopping.merchant.products.v1.ProductAttributes (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:20.974329+00:00
---

# Class protos.google.shopping.merchant.products.v1.ProductAttributes (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.products.v1.ProductAttributes (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.1.1 

Represents a ProductAttributes.

## Implements

[protos.google.shopping.merchant.products.v1.IProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iproductattributes)

## Package

[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.products.v1.IProductAttributes);

Constructs a new ProductAttributes.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iproductattributes)`   
Properties to set  
  
## Properties 

### additionalImageLinks
    
    
    public additionalImageLinks: string[];

ProductAttributes additionalImageLinks.

### adsGrouping
    
    
    public adsGrouping?: (string|null);

ProductAttributes adsGrouping.

### adsLabels
    
    
    public adsLabels: string[];

ProductAttributes adsLabels.

### adsRedirect
    
    
    public adsRedirect?: (string|null);

ProductAttributes adsRedirect.

### adult
    
    
    public adult?: (boolean|null);

ProductAttributes adult.

### ageGroup
    
    
    public ageGroup?: (google.shopping.merchant.products.v1.AgeGroup|keyof typeof google.shopping.merchant.products.v1.AgeGroup|null);

ProductAttributes ageGroup.

### amenityFeature
    
    
    public amenityFeature: google.shopping.merchant.products.v1.ProductAttributes.AmenityFeature[];

ProductAttributes amenityFeature.

### autoPricingMinPrice
    
    
    public autoPricingMinPrice?: (google.shopping.type.IPrice|null);

ProductAttributes autoPricingMinPrice.

### availability
    
    
    public availability?: (google.shopping.merchant.products.v1.Availability|keyof typeof google.shopping.merchant.products.v1.Availability|null);

ProductAttributes availability.

### availabilityDate
    
    
    public availabilityDate?: (google.protobuf.ITimestamp|null);

ProductAttributes availabilityDate.

### bodyStyle
    
    
    public bodyStyle: (google.shopping.merchant.products.v1.ProductAttributes.VehicleBodyStyle|keyof typeof google.shopping.merchant.products.v1.ProductAttributes.VehicleBodyStyle);

ProductAttributes bodyStyle.

### brand
    
    
    public brand?: (string|null);

ProductAttributes brand.

### canonicalLink
    
    
    public canonicalLink?: (string|null);

ProductAttributes canonicalLink.

### carrierShipping
    
    
    public carrierShipping: google.shopping.merchant.products.v1.ProductAttributes.ICarrierShipping[];

ProductAttributes carrierShipping.

### certifications
    
    
    public certifications: google.shopping.merchant.products.v1.IProductCertification[];

ProductAttributes certifications.

### certifiedPreOwned
    
    
    public certifiedPreOwned: boolean;

ProductAttributes certifiedPreOwned.

### cloudExportAdditionalProperties
    
    
    public cloudExportAdditionalProperties: google.shopping.merchant.products.v1.ICloudExportAdditionalProperties[];

ProductAttributes cloudExportAdditionalProperties.

### co2Emissions
    
    
    public co2Emissions?: (google.shopping.merchant.products.v1.ProductAttributes.ICo2Emissions|null);

ProductAttributes co2Emissions.

### color
    
    
    public color?: (string|null);

ProductAttributes color.

### condition
    
    
    public condition?: (google.shopping.merchant.products.v1.Condition|keyof typeof google.shopping.merchant.products.v1.Condition|null);

ProductAttributes condition.

### costOfGoodsSold
    
    
    public costOfGoodsSold?: (google.shopping.type.IPrice|null);

ProductAttributes costOfGoodsSold.

### customLabel_0
    
    
    public customLabel_0?: (string|null);

ProductAttributes customLabel_0.

### customLabel_1
    
    
    public customLabel_1?: (string|null);

ProductAttributes customLabel_1.

### customLabel_2
    
    
    public customLabel_2?: (string|null);

ProductAttributes customLabel_2.

### customLabel_3
    
    
    public customLabel_3?: (string|null);

ProductAttributes customLabel_3.

### customLabel_4
    
    
    public customLabel_4?: (string|null);

ProductAttributes customLabel_4.

### dateFirstRegistered
    
    
    public dateFirstRegistered: string;

ProductAttributes dateFirstRegistered.

### description
    
    
    public description?: (string|null);

ProductAttributes description.

### disclosureDate
    
    
    public disclosureDate?: (google.protobuf.ITimestamp|null);

ProductAttributes disclosureDate.

### displayAddress
    
    
    public displayAddress?: (google.shopping.merchant.products.v1.ProductAttributes.IDisplayAddress|null);

ProductAttributes displayAddress.

### displayAdsId
    
    
    public displayAdsId?: (string|null);

ProductAttributes displayAdsId.

### displayAdsLink
    
    
    public displayAdsLink?: (string|null);

ProductAttributes displayAdsLink.

### displayAdsSimilarIds
    
    
    public displayAdsSimilarIds: string[];

ProductAttributes displayAdsSimilarIds.

### displayAdsTitle
    
    
    public displayAdsTitle?: (string|null);

ProductAttributes displayAdsTitle.

### displayAdsValue
    
    
    public displayAdsValue?: (number|null);

ProductAttributes displayAdsValue.

### documentLinks
    
    
    public documentLinks: string[];

ProductAttributes documentLinks.

### electricRange
    
    
    public electricRange?: (google.shopping.merchant.products.v1.ProductAttributes.IMileage|null);

ProductAttributes electricRange.

### emissionsStandard
    
    
    public emissionsStandard: (google.shopping.merchant.products.v1.ProductAttributes.EmissionsStandard|keyof typeof google.shopping.merchant.products.v1.ProductAttributes.EmissionsStandard);

ProductAttributes emissionsStandard.

### energyConsumption
    
    
    public energyConsumption?: (google.shopping.merchant.products.v1.ProductAttributes.IEnergyConsumption|null);

ProductAttributes energyConsumption.

### energyEfficiencyClass
    
    
    public energyEfficiencyClass?: (google.shopping.merchant.products.v1.EnergyEfficiencyClass|keyof typeof google.shopping.merchant.products.v1.EnergyEfficiencyClass|null);

ProductAttributes energyEfficiencyClass.

### engine
    
    
    public engine: (google.shopping.merchant.products.v1.ProductAttributes.EngineType|keyof typeof google.shopping.merchant.products.v1.ProductAttributes.EngineType);

ProductAttributes engine.

### excludedDestinations
    
    
    public excludedDestinations: google.shopping.type.Destination.DestinationEnum[];

ProductAttributes excludedDestinations.

### expirationDate
    
    
    public expirationDate?: (google.protobuf.ITimestamp|null);

ProductAttributes expirationDate.

### externalSellerId
    
    
    public externalSellerId?: (string|null);

ProductAttributes externalSellerId.

### freeShippingThreshold
    
    
    public freeShippingThreshold: google.shopping.merchant.products.v1.IFreeShippingThreshold[];

ProductAttributes freeShippingThreshold.

### fuelConsumption
    
    
    public fuelConsumption?: (google.shopping.merchant.products.v1.ProductAttributes.IFuelConsumption|null);

ProductAttributes fuelConsumption.

### fuelConsumptionDischargedBattery
    
    
    public fuelConsumptionDischargedBattery?: (google.shopping.merchant.products.v1.ProductAttributes.IFuelConsumption|null);

ProductAttributes fuelConsumptionDischargedBattery.

### gender
    
    
    public gender?: (google.shopping.merchant.products.v1.Gender|keyof typeof google.shopping.merchant.products.v1.Gender|null);

ProductAttributes gender.

### googleProductCategory
    
    
    public googleProductCategory?: (string|null);

ProductAttributes googleProductCategory.

### gtins
    
    
    public gtins: string[];

ProductAttributes gtins.

### handlingCutoffTimes
    
    
    public handlingCutoffTimes: google.shopping.merchant.products.v1.IHandlingCutoffTime[];

ProductAttributes handlingCutoffTimes.

### identifierExists
    
    
    public identifierExists?: (boolean|null);

ProductAttributes identifierExists.

### imageLink
    
    
    public imageLink?: (string|null);

ProductAttributes imageLink.

### includedDestinations
    
    
    public includedDestinations: google.shopping.type.Destination.DestinationEnum[];

ProductAttributes includedDestinations.

### installment
    
    
    public installment?: (google.shopping.merchant.products.v1.IProductInstallment|null);

ProductAttributes installment.

### isBundle
    
    
    public isBundle?: (boolean|null);

ProductAttributes isBundle.

### itemGroupId
    
    
    public itemGroupId?: (string|null);

ProductAttributes itemGroupId.

### itemGroupTitle
    
    
    public itemGroupTitle: string;

ProductAttributes itemGroupTitle.

### latitude
    
    
    public latitude?: (number|null);

ProductAttributes latitude.

### lifestyleImageLinks
    
    
    public lifestyleImageLinks: string[];

ProductAttributes lifestyleImageLinks.

### link
    
    
    public link?: (string|null);

ProductAttributes link.

### linkTemplate
    
    
    public linkTemplate?: (string|null);

ProductAttributes linkTemplate.

### longitude
    
    
    public longitude?: (number|null);

ProductAttributes longitude.

### loyaltyPoints
    
    
    public loyaltyPoints?: (google.shopping.merchant.products.v1.ILoyaltyPoints|null);

ProductAttributes loyaltyPoints.

### loyaltyPrograms
    
    
    public loyaltyPrograms: google.shopping.merchant.products.v1.ILoyaltyProgram[];

ProductAttributes loyaltyPrograms.

### material
    
    
    public material?: (string|null);

ProductAttributes material.

### maxEnergyEfficiencyClass
    
    
    public maxEnergyEfficiencyClass?: (google.shopping.merchant.products.v1.EnergyEfficiencyClass|keyof typeof google.shopping.merchant.products.v1.EnergyEfficiencyClass|null);

ProductAttributes maxEnergyEfficiencyClass.

### maxHandlingTime
    
    
    public maxHandlingTime?: (number|Long|string|null);

ProductAttributes maxHandlingTime.

### maximumRetailPrice
    
    
    public maximumRetailPrice?: (google.shopping.type.IPrice|null);

ProductAttributes maximumRetailPrice.

### mileage
    
    
    public mileage?: (google.shopping.merchant.products.v1.ProductAttributes.IMileage|null);

ProductAttributes mileage.

### minEnergyEfficiencyClass
    
    
    public minEnergyEfficiencyClass?: (google.shopping.merchant.products.v1.EnergyEfficiencyClass|keyof typeof google.shopping.merchant.products.v1.EnergyEfficiencyClass|null);

ProductAttributes minEnergyEfficiencyClass.

### minHandlingTime
    
    
    public minHandlingTime?: (number|Long|string|null);

ProductAttributes minHandlingTime.

### minimumOrderValues
    
    
    public minimumOrderValues: google.shopping.merchant.products.v1.IProductMinimumOrderValue[];

ProductAttributes minimumOrderValues.

### mobileLink
    
    
    public mobileLink?: (string|null);

ProductAttributes mobileLink.

### mobileLinkTemplate
    
    
    public mobileLinkTemplate?: (string|null);

ProductAttributes mobileLinkTemplate.

### model
    
    
    public model: string;

ProductAttributes model.

### mpn
    
    
    public mpn?: (string|null);

ProductAttributes mpn.

### multipack
    
    
    public multipack?: (number|Long|string|null);

ProductAttributes multipack.

### neighborhood
    
    
    public neighborhood: string;

ProductAttributes neighborhood.

### numberOfBathrooms
    
    
    public numberOfBathrooms?: (number|null);

ProductAttributes numberOfBathrooms.

### numberOfBedrooms
    
    
    public numberOfBedrooms?: (number|null);

ProductAttributes numberOfBedrooms.

### numberOfUnits
    
    
    public numberOfUnits?: (number|Long|string|null);

ProductAttributes numberOfUnits.

### pattern
    
    
    public pattern?: (string|null);

ProductAttributes pattern.

### pause
    
    
    public pause?: (google.shopping.merchant.products.v1.Pause|keyof typeof google.shopping.merchant.products.v1.Pause|null);

ProductAttributes pause.

### petPolicy
    
    
    public petPolicy?: (google.shopping.merchant.products.v1.ProductAttributes.IPetPolicy|null);

ProductAttributes petPolicy.

### pickupCost
    
    
    public pickupCost?: (google.shopping.merchant.products.v1.IPickupCost|null);

ProductAttributes pickupCost.

### pickupMethod
    
    
    public pickupMethod?: (google.shopping.merchant.products.v1.PickupMethod|keyof typeof google.shopping.merchant.products.v1.PickupMethod|null);

ProductAttributes pickupMethod.

### pickupSla
    
    
    public pickupSla?: (google.shopping.merchant.products.v1.PickupSla|keyof typeof google.shopping.merchant.products.v1.PickupSla|null);

ProductAttributes pickupSla.

### popularityRank
    
    
    public popularityRank: number;

ProductAttributes popularityRank.

### price
    
    
    public price?: (google.shopping.type.IPrice|null);

ProductAttributes price.

### productDetails
    
    
    public productDetails: google.shopping.merchant.products.v1.IProductDetail[];

ProductAttributes productDetails.

### productFee
    
    
    public productFee: google.shopping.merchant.products.v1.ProductAttributes.IProductFee[];

ProductAttributes productFee.

### productHeight
    
    
    public productHeight?: (google.shopping.merchant.products.v1.IProductDimension|null);

ProductAttributes productHeight.

### productHighlights
    
    
    public productHighlights: string[];

ProductAttributes productHighlights.

### productLength
    
    
    public productLength?: (google.shopping.merchant.products.v1.IProductDimension|null);

ProductAttributes productLength.

### productTypes
    
    
    public productTypes: string[];

ProductAttributes productTypes.

### productWeight
    
    
    public productWeight?: (google.shopping.merchant.products.v1.IProductWeight|null);

ProductAttributes productWeight.

### productWidth
    
    
    public productWidth?: (google.shopping.merchant.products.v1.IProductDimension|null);

ProductAttributes productWidth.

### promotionIds
    
    
    public promotionIds: string[];

ProductAttributes promotionIds.

### propertyName
    
    
    public propertyName: string;

ProductAttributes propertyName.

### propertyType
    
    
    public propertyType: (google.shopping.merchant.products.v1.ProductAttributes.PropertyType|keyof typeof google.shopping.merchant.products.v1.ProductAttributes.PropertyType);

ProductAttributes propertyType.

### questionsAndAnswers
    
    
    public questionsAndAnswers: google.shopping.merchant.products.v1.ProductAttributes.IQuestionAndAnswer[];

ProductAttributes questionsAndAnswers.

### relatedProducts
    
    
    public relatedProducts: google.shopping.merchant.products.v1.ProductAttributes.IRelatedProduct[];

ProductAttributes relatedProducts.

### returnPolicyLabel
    
    
    public returnPolicyLabel?: (string|null);

ProductAttributes returnPolicyLabel.

### salePrice
    
    
    public salePrice?: (google.shopping.type.IPrice|null);

ProductAttributes salePrice.

### salePriceEffectiveDate
    
    
    public salePriceEffectiveDate?: (google.type.IInterval|null);

ProductAttributes salePriceEffectiveDate.

### sellOnGoogleQuantity
    
    
    public sellOnGoogleQuantity?: (number|Long|string|null);

ProductAttributes sellOnGoogleQuantity.

### shipping
    
    
    public shipping: google.shopping.merchant.products.v1.IShipping[];

ProductAttributes shipping.

### shippingHandlingBusinessDays
    
    
    public shippingHandlingBusinessDays: google.shopping.merchant.products.v1.ProductAttributes.IShippingBusinessDaysConfig[];

ProductAttributes shippingHandlingBusinessDays.

### shippingHeight
    
    
    public shippingHeight?: (google.shopping.merchant.products.v1.IShippingDimension|null);

ProductAttributes shippingHeight.

### shippingLabel
    
    
    public shippingLabel?: (string|null);

ProductAttributes shippingLabel.

### shippingLength
    
    
    public shippingLength?: (google.shopping.merchant.products.v1.IShippingDimension|null);

ProductAttributes shippingLength.

### shippingTransitBusinessDays
    
    
    public shippingTransitBusinessDays: google.shopping.merchant.products.v1.ProductAttributes.IShippingBusinessDaysConfig[];

ProductAttributes shippingTransitBusinessDays.

### shippingWeight
    
    
    public shippingWeight?: (google.shopping.merchant.products.v1.IShippingWeight|null);

ProductAttributes shippingWeight.

### shippingWidth
    
    
    public shippingWidth?: (google.shopping.merchant.products.v1.IShippingDimension|null);

ProductAttributes shippingWidth.

### shoppingAdsExcludedCountries
    
    
    public shoppingAdsExcludedCountries: string[];

ProductAttributes shoppingAdsExcludedCountries.

### shortTitle
    
    
    public shortTitle?: (string|null);

ProductAttributes shortTitle.

### size
    
    
    public size?: (string|null);

ProductAttributes size.

### sizeSystem
    
    
    public sizeSystem?: (google.shopping.merchant.products.v1.SizeSystem|keyof typeof google.shopping.merchant.products.v1.SizeSystem|null);

ProductAttributes sizeSystem.

### sizeTypes
    
    
    public sizeTypes: google.shopping.merchant.products.v1.SizeType[];

ProductAttributes sizeTypes.

### specialtyHousingType
    
    
    public specialtyHousingType: (google.shopping.merchant.products.v1.ProductAttributes.SpecialtyHousingType|keyof typeof google.shopping.merchant.products.v1.ProductAttributes.SpecialtyHousingType);

ProductAttributes specialtyHousingType.

### structuredDescription
    
    
    public structuredDescription?: (google.shopping.merchant.products.v1.IStructuredDescription|null);

ProductAttributes structuredDescription.

### structuredTitle
    
    
    public structuredTitle?: (google.shopping.merchant.products.v1.IStructuredTitle|null);

ProductAttributes structuredTitle.

### subscriptionCost
    
    
    public subscriptionCost?: (google.shopping.merchant.products.v1.ISubscriptionCost|null);

ProductAttributes subscriptionCost.

### sustainabilityIncentives
    
    
    public sustainabilityIncentives: google.shopping.merchant.products.v1.IProductSustainabilityIncentive[];

ProductAttributes sustainabilityIncentives.

### title
    
    
    public title?: (string|null);

ProductAttributes title.

### transitTimeLabel
    
    
    public transitTimeLabel?: (string|null);

ProductAttributes transitTimeLabel.

### trim
    
    
    public trim: string;

ProductAttributes trim.

### unitArea
    
    
    public unitArea?: (google.shopping.merchant.products.v1.ProductAttributes.IUnitArea|null);

ProductAttributes unitArea.

### unitPricingBaseMeasure
    
    
    public unitPricingBaseMeasure?: (google.shopping.merchant.products.v1.IUnitPricingBaseMeasure|null);

ProductAttributes unitPricingBaseMeasure.

### unitPricingMeasure
    
    
    public unitPricingMeasure?: (google.shopping.merchant.products.v1.IUnitPricingMeasure|null);

ProductAttributes unitPricingMeasure.

### utilitiesIncluded
    
    
    public utilitiesIncluded: google.shopping.merchant.products.v1.ProductAttributes.UtilitiesIncluded[];

ProductAttributes utilitiesIncluded.

### variantOptions
    
    
    public variantOptions: google.shopping.merchant.products.v1.ProductAttributes.IVariantOption[];

ProductAttributes variantOptions.

### vehicleAllInPrice
    
    
    public vehicleAllInPrice?: (google.shopping.type.IPrice|null);

ProductAttributes vehicleAllInPrice.

### vehicleExpenses
    
    
    public vehicleExpenses?: (google.shopping.type.IPrice|null);

ProductAttributes vehicleExpenses.

### vehicleMandatoryInspectionIncluded
    
    
    public vehicleMandatoryInspectionIncluded: boolean;

ProductAttributes vehicleMandatoryInspectionIncluded.

### vehicleMsrp
    
    
    public vehicleMsrp?: (google.shopping.type.IPrice|null);

ProductAttributes vehicleMsrp.

### vehiclePriceType
    
    
    public vehiclePriceType: (google.shopping.merchant.products.v1.ProductAttributes.VehiclePriceType|keyof typeof google.shopping.merchant.products.v1.ProductAttributes.VehiclePriceType);

ProductAttributes vehiclePriceType.

### videoLinks
    
    
    public videoLinks: string[];

ProductAttributes videoLinks.

### vin
    
    
    public vin: string;

ProductAttributes vin.

### virtualModelLink
    
    
    public virtualModelLink?: (string|null);

ProductAttributes virtualModelLink.

### warranty
    
    
    public warranty?: (google.shopping.merchant.products.v1.ProductAttributes.IWarranty|null);

ProductAttributes warranty.

### year
    
    
    public year: (number|Long|string);

ProductAttributes year.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.products.v1.IProductAttributes): google.shopping.merchant.products.v1.ProductAttributes;

Creates a new ProductAttributes instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iproductattributes)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes-class)` | ProductAttributes instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.products.v1.ProductAttributes;

Decodes a ProductAttributes message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes-class)` | ProductAttributes  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.products.v1.ProductAttributes;

Decodes a ProductAttributes message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes-class)` | ProductAttributes  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.products.v1.IProductAttributes, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ProductAttributes message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iproductattributes)`   
ProductAttributes message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.products.v1.IProductAttributes, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ProductAttributes message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iproductattributes)`   
ProductAttributes message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.products.v1.ProductAttributes;

Creates a ProductAttributes message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes-class)` | ProductAttributes  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ProductAttributes

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this ProductAttributes to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.products.v1.ProductAttributes, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ProductAttributes message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ProductAttributes](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes-class)`   
ProductAttributes  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ProductAttributes message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
