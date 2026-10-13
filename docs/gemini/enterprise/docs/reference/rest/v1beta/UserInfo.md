---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/UserInfo/
title: UserInfo \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:08.217104+00:00
---

# UserInfo  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/UserInfo/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  UserInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PreciseLocation
    * JSON representation



Information of an end user.

JSON representation  
---  
      
    
    {
      "userId": string,
      "userAgent": string,
      "timeZone": string,
      "preciseLocation": {
        object ([PreciseLocation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/UserInfo#PreciseLocation))
      }
    }  
  
Fields  
---  
`userId` |  `string` Highly recommended for logged-in users. Unique identifier for logged-in user, such as a user name. Don't set for anonymous users.Always use a hashed value for this ID.Don't set the field to the same fixed ID for different users. This mixes the event history of those users together, which results in degraded model quality.The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.Represents an opaque ID to the Search API. The Search API doesn't interpret the value in any way. This field is used to associate events with a user across sessions if the events are being uploaded.  
`userAgent` |  `string` User agent as included in the HTTP header.The field must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.This should not be set when using the client side event reporting with GTM or JavaScript tag in `[UserEventService.CollectUserEvent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.dataStores.userEvents/collect#google.cloud.discoveryengine.v1beta.UserEventService.CollectUserEvent)` or if `[UserEvent.direct_user_request](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.dataStores.userEvents#UserEvent.FIELDS.direct_user_request)` is set.  
`timeZone` |  `string` Optional. IANA time zone, e.g. Europe/Budapest.  
`preciseLocation` |  `object (`[PreciseLocation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/UserInfo#PreciseLocation)`)` Optional. Input only. Precise location of the user. It is used in Custom Ranking to calculate the distance between the user and the relevant documents.  
  
## PreciseLocation

Precise location info with multiple representation options.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "point": {
        object ([LatLng](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/LatLng))
      },
      "address": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`point` |  `object (`[LatLng](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/LatLng)`)` Optional. location represented by a latitude/longitude point.  
`address` |  `string` location represented by a natural language address. Will later be geocoded and converted to either a point or a polygon.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
