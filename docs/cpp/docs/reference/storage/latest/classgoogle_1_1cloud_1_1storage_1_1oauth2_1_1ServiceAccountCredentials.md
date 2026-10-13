---
url: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1oauth2_1_1ServiceAccountCredentials/
title: Class ServiceAccountCredentials<HttpRequestBuilderType, ClockType> (2.47.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:15.539034+00:00
---

# Class ServiceAccountCredentials<HttpRequestBuilderType, ClockType> (2.47.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1oauth2_1_1ServiceAccountCredentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ServiceAccountCredentials<HttpRequestBuilderType, ClockType> (2.47.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Wrapper class for Google OAuth 2.0 service account credentials. 

Takes a [ServiceAccountCredentialsInfo](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1oauth2_1_1ServiceAccountCredentialsInfo) and obtains access tokens from the Google Authorization Service as needed. Instances of this class should usually be created via the convenience methods declared in [google_credentials.h](about:invalid#zCSafez).

An HTTP Authorization header, with an access token as its value, can be obtained by calling the [AuthorizationHeader()](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1oauth2_1_1ServiceAccountCredentials#classgoogle_1_1cloud_1_1storage_1_1oauth2_1_1ServiceAccountCredentials_1a9726c839461ba27f73c7306ed5e4938b) method; if the current access token is invalid or nearing expiration, this will class will first obtain a new access token before returning the Authorization header string.

###### See Also

<https://developers.google.com/identity/protocols/OAuth2ServiceAccount> for an overview of using service accounts with Google's OAuth 2.0 system.

###### See Also

<https://cloud.google.com/storage/docs/reference/libraries> for details on how to obtain and get started with service account credentials.

**Deprecated:**

Prefer using the unified credentials documented in [Authentication Components](https://cloud.google.com/cpp/docs/reference/common/latest/group__guac.html)

## Constructors 

### ServiceAccountCredentials(ServiceAccountCredentialsInfo)

**Parameter**  
---  
**Name** | **Description**  
`info` |  `ServiceAccountCredentialsInfo`   
  
  
### ServiceAccountCredentials(ServiceAccountCredentialsInfo, ChannelOptions const &)

**Parameters**  
---  
**Name** | **Description**  
`info` |  `ServiceAccountCredentialsInfo`   
  
`options` |  `ChannelOptions const &`   
  
  
## Functions 

### virtual AuthorizationHeader()

Attempts to obtain a value for the Authorization HTTP header. 

If unable to obtain a value for the Authorization header, which could happen for [`Credentials`](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1oauth2_1_1Credentials) that need to be periodically refreshed, the underlying [`Status`](https://cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Status.html) will indicate failure details from the refresh HTTP request. Otherwise, the returned value will contain the Authorization header to be used in HTTP requests.

**Deprecated:** Prefer using the unified credentials documented in [Authentication Components](https://cloud.google.com/cpp/docs/reference/common/latest/group__guac.html)

**Returns**  
---  
**Type** | **Description**  
`StatusOr< std::string >` |   
  
### virtual SignBlob(SigningAccount const &, std::string const &) const

Create a RSA SHA256 signature of the blob using the Credential object. 

**Deprecated:** Prefer using the unified credentials documented in [Authentication Components](https://cloud.google.com/cpp/docs/reference/common/latest/group__guac.html)

**Parameters**  
---  
**Name** | **Description**  
`signing_account` |  `SigningAccount const &`   
the desired service account which should sign `blob`. If not set, uses this object's account. If set, it must match this object's service account.   
`blob` |  `std::string const &`   
the string to sign. Note that sometimes the application must Base64-encode the data before signing.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< std::vector< std::uint8_t > >` | the signed blob as raw bytes. An error if the `signing_account` does not match the email for the credential's account.  
  
### virtual AccountEmail() const

Return the account's email associated with these credentials, if any. 

**Deprecated:** Prefer using the unified credentials documented in [Authentication Components](https://cloud.google.com/cpp/docs/reference/common/latest/group__guac.html)

**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
### virtual KeyId() const

Return the account's key_id associated with these credentials, if any. 

**Deprecated:** Prefer using the unified credentials documented in [Authentication Components](https://cloud.google.com/cpp/docs/reference/common/latest/group__guac.html)

**Returns**  
---  
**Type** | **Description**  
`std::string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
