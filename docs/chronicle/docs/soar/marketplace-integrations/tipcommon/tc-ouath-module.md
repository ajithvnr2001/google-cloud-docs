---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-ouath-module/
title: OAuth module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:58:27.102675+00:00
---

# OAuth module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-ouath-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OAuth module

## _exception_ TIPCommon.oauth.AuthenticationError

Bases: **Exception**

A generic exception for authentication errors.

## _class_ TIPCommon.oauth.AuthorizedOauthClient

_class_ `TIPCommon.oauth.AuthorizedOauthClient(oauth_manager: OauthManager, *args, **kwargs)`

Bases: **Client**

This class represents an authorized client for API calls.

### Methods

  * `close()→ None` Saves the token and closes the client session.

  * `request(*args, **kwargs)→ Response` Overwrites to support automatic credential refresh. The method checks if credentials are expired before executing the request and validates the response to check if expired credentials are indicated. If so, it executes the request again with a refreshed token.




## _class_ TIPCommon.oauth.CredStorage

_class_ `TIPCommon.oauth.CredStorage(encryption_password: str, chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob)`

Bases: **object**

Manages the storage and retrieval of credentials.

### Methods

  * `get_instance_identifier()→ str` Gets the Google SecOps instance identifier of the connector or integration.

  * `get_token()→ OauthToken | None` Extracts and decrypts a token from the context database.

  * `set_token(token: OauthToken)→ None` Encrypts and saves a token into the context database.




## _exception_ TIPCommon.oauth.EncryptionError

Bases: **Exception**

A generic exception for encryption errors.

## _class_ TIPCommon.oauth.OAuthAdapter

Bases: **ABC**

An abstract base class that defines the interface for OAuth operations.

### Abstract Methods

  * `abstractcheck_signer(token: OauthToken)→ bool` Returns `True` if the signer is valid or `False` in any other case.

  * `abstractprepare_authorized_client(token: OauthToken, auth_client: AuthorizedOauthClient)→ AuthorizedOauthClient` Sets headers or other necessary client configurations for the authorized client.

  * `abstractrefresh_token()→ OauthToken` Refreshes the token and returns the `OauthToken` data model.

  * `abstract static validate_bad_credentials(response: Response)→ bool` Checks if the response indicates expired credentials.




##### Raises

`AuthenticationError` – When the response indicates expired credentials.

## _class_ TIPCommon.oauth.OauthManager

_class_ `TIPCommon.oauth.OauthManager(oauth_adapter: OAuthAdapter, cred_storage: CredStorage)`

Bases: **object**

Manages OAuth authentication flows, including token refreshing and client preparation.

### Methods

  * `prepare_authorized_client(auth_client: AuthorizedOauthClient)→ AuthorizedOauthClient` Prepares an authorized client for use.

  * `refresh_if_bad_credentials(auth_client: AuthorizedOauthClient, response: Response)→ bool` Refreshes the token if the response indicates bad credentials.

  * `refresh_if_expired(auth_client: AuthorizedOauthClient)→ bool` Refreshes the token if it is expired.

  * `save_token()→ None` Saves the current token.




## _class_ TIPCommon.oauth.OauthToken

_class_ `TIPCommon.oauth.OauthToken(access_token: 'str', expiration_time: 'int', refresh_token: 'str' = None, signer: 'str' = None, additional_data: 'SingleJson' = <factory>)`

Bases: **object**

Represents an OAuth token with its associated data.

#### Properties

Attribute | Description  
---|---  
`access_token` | `str`The access token string.  
`additional_data` | `MutableMapping[str, Any]`Additional data associated with the token.  
`expiration_time` | `int`The token expiration time (Unix timestamp).  
`refresh_token` | `str`The refresh token string.Defaults to `None`.  
`signer` | `str`The token's signer.Defaults to `None`.  
  
### Methods

  * `to_cache()→ JsonString` Serializes the `OauthToken` object to a format suitable for caching.



#### _classmethod_ from_cache

_classmethod_ `from_cache(raw_data: JsonString)→ OauthToken`

Creates an `OauthToken` object from raw cached data.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
