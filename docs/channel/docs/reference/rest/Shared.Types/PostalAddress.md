---
url: https://docs.cloud.google.com/channel/docs/reference/rest/Shared.Types/PostalAddress/
title: PostalAddress \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:32.015283+00:00
---

# PostalAddress  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/reference/rest/Shared.Types/PostalAddress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  PostalAddress Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Represents a postal address, such as for postal delivery or payments addresses. With a postal address, a postal service can deliver items to a premise, P.O. box, or similar. Postal addresses aren't intended to model geographical locations like roads, towns, or mountains.

In typical usage, an address is created by user input or from importing existing data, depending on the type of process.

Advice on address input or editing:

  * Use an internationalization-ready address widget such as <https://github.com/google/libaddressinput>.
  * Users shouldn't be presented with UI elements for input or editing of fields outside countries where that field is used.



For more guidance on how to use this schema, see <https://support.google.com/business/answer/6397478>.

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
`postalCode` |  `string` Optional. Postal code of the address. Not all countries use or require postal codes, but where they're used, they might trigger additional validation with other parts of the address (for example, state or zip code validation in the United States).  
`sortingCode` |  `string` Optional. Additional, country-specific, sorting code. This isn't used in most regions. Where it's used, the value is either a string like "CEDEX", optionally followed by a number (for example, "CEDEX 7"), or just a number alone, representing the "sector code" (Jamaica), "delivery area indicator" (Malawi) or "post office indicator" (Côte d'Ivoire).  
`administrativeArea` |  `string` Optional. Highest administrative subdivision which is used for postal addresses of a country or region. For example, this can be a state, a province, an oblast, or a prefecture. For Spain, this is the province and not the autonomous community (for example, "Barcelona" and not "Catalonia"). Many countries don't use an administrative area in postal addresses. For example, in Switzerland, this should be left unpopulated.  
`locality` |  `string` Optional. Generally refers to the city or town portion of the address. Examples: US city, IT comune, UK post town. In regions of the world where localities aren't well defined or don't fit into this structure well, leave `locality` empty and use `addressLines`.  
`sublocality` |  `string` Optional. Sublocality of the address. For example, this can be a neighborhood, borough, or district.  
`addressLines[]` |  `string` Unstructured address lines describing the lower levels of an address.Because values in `addressLines` don't have type information and might sometimes contain multiple values in a single field (for example, "Austin, TX"), it's important that line order is clear. The order of address lines should be "envelope order" for the country or region of the address. In places where this can vary, such as Japan, `address_language` is used to make it explicit (for example, "ja" for large-to-small ordering and "ja-Latn" or "en" for small-to-large). In this way, the most specific line of an address can be selected based on the language.The minimum permitted structural representation of an address consists of a `regionCode` with all remaining information placed in the `addressLines`. It would be possible to format such an address very approximately without geocoding, but no semantic reasoning could be made about any of the address components until it was at least partially resolved.To handle completely unstructured addresses, we recommend creating an address that only contains a `regionCode` and `addressLines`, and then geocoding, instead of guessing which parts of the address should be localities or administrative areas.  
`recipients[]` |  `string` Optional. The recipient at the address. This field may, under certain circumstances, contain multiline information. For example, it might contain "care of" information.  
`organization` |  `string` Optional. The name of the organization at the address.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-03 UTC."],[],[]] 
