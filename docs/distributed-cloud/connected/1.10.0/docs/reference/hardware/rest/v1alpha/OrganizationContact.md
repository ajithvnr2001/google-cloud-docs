---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/hardware/rest/v1alpha/OrganizationContact/
title: OrganizationContact \u00a0|\u00a0 Google Distributed Cloud connected, version 1.10.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:50.364406+00:00
---

# OrganizationContact  |  Google Distributed Cloud connected, version 1.10.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/hardware/rest/v1alpha/OrganizationContact/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/apis)



Send feedback 

#  OrganizationContact Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PostalAddress
    * JSON representation



Contact information of the customer organization.

JSON representation  
---  
      
    
    {
      "address": {
        object ([PostalAddress](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/hardware/rest/v1alpha/OrganizationContact#PostalAddress))
      },
      "email": string,
      "phone": string,
      "contacts": [
        {
          object ([Contact](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/hardware/rest/v1alpha/Contact))
        }
      ]
    }  
  
Fields  
---  
`address` |  `object (`[PostalAddress](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/hardware/rest/v1alpha/OrganizationContact#PostalAddress)`)` Required. The organization's address.  
`email` |  `string` Optional. The organization's email.  
`phone` |  `string` Optional. The organization's phone number.  
`contacts[]` |  `object (`[Contact](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/hardware/rest/v1alpha/Contact)`)` Required. The individual points of contact in the organization at this location.  
  
## PostalAddress

Represents a postal address, such as for postal delivery or payments addresses. With a postal address, a postal service can deliver items to a premise, P.O. box, or similar. A postal address is not intended to model geographical locations like roads, towns, or mountains.

In typical usage, an address would be created by user input or from importing existing data, depending on the type of process.

Advice on address input or editing:

  * Use an internationalization-ready address widget such as <https://github.com/google/libaddressinput>.
  * Users should not be presented with UI elements for input or editing of fields outside countries where that field is used.



For more guidance on how to use this schema, see: <https://support.google.com/business/answer/6397478>.

JSON representation  
---  
      
    
    {
      "revision": integer,
      "regionCode": string,
      "languageCode": string,
      "postalCode": string,
      "sortingCode": string,
      "administrativeArea": string,
      "locality": string,
      "sublocality": string,
      "addressLines": [
        string
      ],
      "recipients": [
        string
      ],
      "organization": string
    }  
  
Fields  
---  
`revision` |  `integer` The schema revision of the `PostalAddress`. This must be set to 0, which is the latest revision.All new revisions **must** be backward compatible with old revisions.  
`regionCode` |  `string` Required. CLDR region code of the country/region of the address. This is never inferred and it is up to the user to ensure the value is correct. See <https://cldr.unicode.org/> and <https://www.unicode.org/cldr/charts/30/supplemental/territory_information.html> for details. Example: "CH" for Switzerland.  
`languageCode` |  `string` Optional. BCP-47 language code of the contents of this address (if known). This is often the UI language of the input form or is expected to match one of the languages used in the address' country/region, or their transliterated equivalents. This can affect formatting in certain countries, but is not critical to the correctness of the data and will never affect any validation or other non-formatting related operations.If this value is not known, it should be omitted (rather than specifying a possibly incorrect default).Examples: "zh-Hant", "ja", "ja-Latn", "en".  
`postalCode` |  `string` Optional. Postal code of the address. Not all countries use or require postal codes to be present, but where they are used, they may trigger additional validation with other parts of the address (for example, state or zip code validation in the United States).  
`sortingCode` |  `string` Optional. Additional, country-specific, sorting code. This is not used in most regions. Where it is used, the value is either a string like "CEDEX", optionally followed by a number (for example, "CEDEX 7"), or just a number alone, representing the "sector code" (Jamaica), "delivery area indicator" (Malawi) or "post office indicator" (Côte d'Ivoire).  
`administrativeArea` |  `string` Optional. Highest administrative subdivision which is used for postal addresses of a country or region. For example, this can be a state, a province, an oblast, or a prefecture. For Spain, this is the province and not the autonomous community (for example, "Barcelona" and not "Catalonia"). Many countries don't use an administrative area in postal addresses. For example, in Switzerland, this should be left unpopulated.  
`locality` |  `string` Optional. Generally refers to the city or town portion of the address. Examples: US city, IT comune, UK post town. In regions of the world where localities are not well defined or do not fit into this structure well, leave `locality` empty and use `addressLines`.  
`sublocality` |  `string` Optional. Sublocality of the address. For example, this can be a neighborhood, borough, or district.  
`addressLines[]` |  `string` Unstructured address lines describing the lower levels of an address.Because values in `addressLines` do not have type information and may sometimes contain multiple values in a single field (for example, "Austin, TX"), it is important that the line order is clear. The order of address lines should be "envelope order" for the country or region of the address. In places where this can vary (for example, Japan), `address_language` is used to make it explicit (for example, "ja" for large-to-small ordering and "ja-Latn" or "en" for small-to-large). In this way, the most specific line of an address can be selected based on the language.The minimum permitted structural representation of an address consists of a `regionCode` with all remaining information placed in the `addressLines`. It would be possible to format such an address very approximately without geocoding, but no semantic reasoning could be made about any of the address components until it was at least partially resolved.Creating an address only containing a `regionCode` and `addressLines` and then geocoding is the recommended way to handle completely unstructured addresses (as opposed to guessing which parts of the address should be localities or administrative areas).  
`recipients[]` |  `string` Optional. The recipient at the address. This field may, under certain circumstances, contain multiline information. For example, it might contain "care of" information.  
`organization` |  `string` Optional. The name of the organization at the address.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
