---
url: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/SetAccountInfoResponse/
title: SetAccountInfoResponse \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:37.857882+00:00
---

# SetAccountInfoResponse  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/SetAccountInfoResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Reference ](https://docs.cloud.google.com/identity-platform/docs/apis)



Send feedback 

#  SetAccountInfoResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for accounts.update

JSON representation  
---  
      
    
    {
      "kind": string,
      "localId": string,
      "email": string,
      "displayName": string,
      "idToken": string,
      "providerUserInfo": [
        {
          object ([ProviderUserInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/ProviderUserInfo))
        }
      ],
      "newEmail": string,
      "photoUrl": string,
      "refreshToken": string,
      "expiresIn": string,
      "passwordHash": string,
      "emailVerified": boolean
    }  
  
Fields  
---  
`kind  
**(deprecated)**` |  `string` This item is deprecated!  
`localId` |  `string` The ID of the authenticated user.  
`email  
**(deprecated)**` |  `string` This item is deprecated!The account's email address.  
`displayName  
**(deprecated)**` |  `string` This item is deprecated!The account's display name.  
`idToken` |  `string` An Identity Platform ID token for the account. This is used for legacy user sign up.  
`providerUserInfo[]` |  `object (`[ProviderUserInfo](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/ProviderUserInfo)`)` The linked Identity Providers on the account.  
`newEmail` |  `string` The new email that has been set on the user's account attributes.  
`photoUrl  
**(deprecated)**` |  `string` This item is deprecated!The user's photo URL for the account's profile photo.  
`refreshToken` |  `string` A refresh token for the account. This is used for legacy user sign up.  
`expiresIn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of seconds until the Identity Platform ID token expires.  
`passwordHash  
**(deprecated)**` |  `string` This item is deprecated!Deprecated. No actual password hash is currently returned.  
`emailVerified` |  `boolean` Whether the account's email has been verified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
