---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse/
title: ListInfoTypesResponse \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:47.654187+00:00
---

# ListInfoTypesResponse  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  ListInfoTypesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * InfoTypeDescription
    * JSON representation
  * InfoTypeSupportedBy
  * LocationSupport
    * JSON representation
  * RegionalizationScope
  * VersionDescription
    * JSON representation
  * InfoTypeCategory
    * JSON representation
  * LocationCategory
  * IndustryCategory
  * TypeCategory
  * InfoTypeLaunchStatus



Response to the infoTypes.list request.

JSON representation  
---  
      
    
    {
      "infoTypes": [
        {
          object ([InfoTypeDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#InfoTypeDescription))
        }
      ]
    }  
  
Fields  
---  
`infoTypes[]` |  `object (`[InfoTypeDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#InfoTypeDescription)`)` Set of sensitive infoTypes.  
  
## InfoTypeDescription

InfoType description.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "supportedBy": [
        enum ([InfoTypeSupportedBy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#InfoTypeSupportedBy))
      ],
      "description": string,
      "locationSupport": {
        object ([LocationSupport](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#LocationSupport))
      },
      "example": string,
      "versions": [
        {
          object ([VersionDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#VersionDescription))
        }
      ],
      "categories": [
        {
          object ([InfoTypeCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#InfoTypeCategory))
        }
      ],
      "sensitivityScore": {
        object ([SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore))
      },
      "specificInfoTypes": [
        string
      ],
      "launchStatus": enum ([InfoTypeLaunchStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#InfoTypeLaunchStatus))
    }  
  
Fields  
---  
`name` |  `string` Internal name of the infoType.  
`displayName` |  `string` Human readable form of the infoType name.  
`supportedBy[]` |  `enum (`[InfoTypeSupportedBy](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#InfoTypeSupportedBy)`)` Which parts of the API supports this InfoType.  
`description` |  `string` Description of the infotype. Translated when language is provided in the request.  
`locationSupport` |  `object (`[LocationSupport](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#LocationSupport)`)` Locations at which this feature can be used. May change over time.  
`example` |  `string` A sample that is a true positive for this infoType.  
`versions[]` |  `object (`[VersionDescription](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#VersionDescription)`)` A list of available versions for the infotype.  
`categories[]` |  `object (`[InfoTypeCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#InfoTypeCategory)`)` The category of the infoType.  
`sensitivityScore` |  `object (`[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore)`)` The default sensitivity of the infoType.  
`specificInfoTypes[]` |  `string` If this field is set, this infoType is a general infoType and these specific infoTypes are contained within it. General infoTypes are infoTypes that encompass multiple specific infoTypes. For example, the "GEOGRAPHIC_DATA" general infoType would have set for this field "LOCATION", "LOCATION_COORDINATES", and "STREET_ADDRESS".  
`launchStatus` |  `enum (`[InfoTypeLaunchStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#InfoTypeLaunchStatus)`)` The launch status of the infoType.  
  
## InfoTypeSupportedBy

Parts of the APIs which use certain infoTypes.

Enums  
---  
`ENUM_TYPE_UNSPECIFIED` | Unused.  
`INSPECT` | Supported by the inspect operations.  
`RISK_ANALYSIS` | Supported by the risk analysis operations.  
  
## LocationSupport

Locations at which a feature can be used.

JSON representation  
---  
      
    
    {
      "regionalizationScope": enum ([RegionalizationScope](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#RegionalizationScope)),
      "locations": [
        string
      ]
    }  
  
Fields  
---  
`regionalizationScope` |  `enum (`[RegionalizationScope](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#RegionalizationScope)`)` The current scope for location on this feature. This may expand over time.  
`locations[]` |  `string` Specific locations where the feature may be used. Examples: us-central1, us, asia, global If scope is ANY_LOCATION, no regions will be listed.  
  
## RegionalizationScope

The location scope for a feature.

Enums  
---  
`REGIONALIZATION_SCOPE_UNSPECIFIED` | Invalid.  
`REGIONAL` | Feature may be used with one or more regions. See locations for details.  
`ANY_LOCATION` | Feature may be used anywhere. Default value.  
  
## VersionDescription

Details about each available version for an infotype.

JSON representation  
---  
      
    
    {
      "version": string,
      "description": string
    }  
  
Fields  
---  
`version` |  `string` Name of the version  
`description` |  `string` Description of the version.  
  
## InfoTypeCategory

Classification of infoTypes to organize them according to geographic location, industry, and data type.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "locationCategory": enum ([LocationCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#LocationCategory)),
      "industryCategory": enum ([IndustryCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#IndustryCategory)),
      "typeCategory": enum ([TypeCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#TypeCategory))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Categories of infotypes. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`locationCategory` |  `enum (`[LocationCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#LocationCategory)`)` The region or country that issued the ID or document represented by the infoType.  
`industryCategory` |  `enum (`[IndustryCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#IndustryCategory)`)` The group of relevant businesses where this infoType is commonly used  
`typeCategory` |  `enum (`[TypeCategory](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ListInfoTypesResponse#TypeCategory)`)` The class of identifiers where this infoType belongs  
End of mutually exclusive fields.  
  
## LocationCategory

Enum of the current locations. We might add more locations in the future.

Enums  
---  
`LOCATION_UNSPECIFIED` | Unused location  
`GLOBAL` | The infoType is not issued by or tied to a specific region, but is used almost everywhere.  
`ARGENTINA` | The infoType is typically used in Argentina.  
`ARMENIA` | The infoType is typically used in Armenia.  
`AUSTRALIA` | The infoType is typically used in Australia.  
`AUSTRIA` | The infoType is typically used in Austria.  
`AZERBAIJAN` | The infoType is typically used in Azerbaijan.  
`BELARUS` | The infoType is typically used in Belarus.  
`BELGIUM` | The infoType is typically used in Belgium.  
`BRAZIL` | The infoType is typically used in Brazil.  
`CANADA` | The infoType is typically used in Canada.  
`CHILE` | The infoType is typically used in Chile.  
`CHINA` | The infoType is typically used in China.  
`COLOMBIA` | The infoType is typically used in Colombia.  
`CROATIA` | The infoType is typically used in Croatia.  
`CZECHIA` | The infoType is typically used in Czechia.  
`DENMARK` | The infoType is typically used in Denmark.  
`FRANCE` | The infoType is typically used in France.  
`FINLAND` | The infoType is typically used in Finland.  
`GERMANY` | The infoType is typically used in Germany.  
`HONG_KONG` | The infoType is typically used in Hong Kong.  
`INDIA` | The infoType is typically used in India.  
`INDONESIA` | The infoType is typically used in Indonesia.  
`IRELAND` | The infoType is typically used in Ireland.  
`ISRAEL` | The infoType is typically used in Israel.  
`ITALY` | The infoType is typically used in Italy.  
`JAPAN` | The infoType is typically used in Japan.  
`KAZAKHSTAN` | The infoType is typically used in Kazakhstan.  
`KOREA` | The infoType is typically used in Korea.  
`MEXICO` | The infoType is typically used in Mexico.  
`THE_NETHERLANDS` | The infoType is typically used in the Netherlands.  
`NEW_ZEALAND` | The infoType is typically used in New Zealand.  
`NORWAY` | The infoType is typically used in Norway.  
`PARAGUAY` | The infoType is typically used in Paraguay.  
`PERU` | The infoType is typically used in Peru.  
`POLAND` | The infoType is typically used in Poland.  
`PORTUGAL` | The infoType is typically used in Portugal.  
`RUSSIA` | The infoType is typically used in Russia.  
`SINGAPORE` | The infoType is typically used in Singapore.  
`SOUTH_AFRICA` | The infoType is typically used in South Africa.  
`SPAIN` | The infoType is typically used in Spain.  
`SWEDEN` | The infoType is typically used in Sweden.  
`SWITZERLAND` | The infoType is typically used in Switzerland.  
`TAIWAN` | The infoType is typically used in Taiwan.  
`THAILAND` | The infoType is typically used in Thailand.  
`TURKEY` | The infoType is typically used in Turkey.  
`UKRAINE` | The infoType is typically used in Ukraine.  
`UNITED_KINGDOM` | The infoType is typically used in the United Kingdom.  
`UNITED_STATES` | The infoType is typically used in the United States.  
`URUGUAY` | The infoType is typically used in Uruguay.  
`UZBEKISTAN` | The infoType is typically used in Uzbekistan.  
`VENEZUELA` | The infoType is typically used in Venezuela.  
`INTERNAL` | The infoType is typically used in Google internally.  
  
## IndustryCategory

Enum of the current industries in the category. We might add more industries in the future.

Enums  
---  
`INDUSTRY_UNSPECIFIED` | Unused industry  
`FINANCE` | The infoType is typically used in the finance industry.  
`HEALTH` | The infoType is typically used in the health industry.  
`TELECOMMUNICATIONS` | The infoType is typically used in the telecommunications industry.  
  
## TypeCategory

Enum of the current types in the category. We might add more types in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Unused type  
`PII` | Personally identifiable information, for example, a name or phone number  
`SPII` | Personally identifiable information that is especially sensitive, for example, a passport number.  
`DEMOGRAPHIC` | Attributes that can partially identify someone, especially in combination with other attributes, like age, height, and gender.  
`CREDENTIAL` | Confidential or secret information, for example, a password.  
`GOVERNMENT_ID` | An identification document issued by a government.  
`DOCUMENT` | A document, for example, a resume or source code.  
`CONTEXTUAL_INFORMATION` | Information that is not sensitive on its own, but provides details about the circumstances surrounding an entity or an event.  
`CUSTOM` | Category for `CustomInfoType` types.  
  
## InfoTypeLaunchStatus

The launch status of an infoType.

Enums  
---  
`INFO_TYPE_LAUNCH_STATUS_UNSPECIFIED` | Unspecified.  
`GENERAL_AVAILABILITY` | InfoType is generally available.  
`PUBLIC_PREVIEW` | InfoType is in public preview.  
`PRIVATE_PREVIEW` | InfoType is in private preview.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
