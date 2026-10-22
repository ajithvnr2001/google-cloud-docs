---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-oauth-module/
title: oauth module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:50.824732+00:00
---

# oauth module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-oauth-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# `oauth` module

The **`oauth` module** simplifies the implementation of OAuth 2.0 authentication flows in integrations. It manages the lifecycle of access and refresh tokens, provides secure storage using encryption, and offers an authorized client that automatically handles token expiration and renewal during API requests.

## Classes

The following classes provide the core functionality for managing OAuth 2.0 sessions, secure token storage, and automated credential handling.

### AuthorizedOauthClient

`TIPCommon.oauth.AuthorizedOauthClient(oauth_manager: OauthManager, *args, **kwargs)`

Bases: `Client`

Represents an authorized client used to perform API calls. This class extends the base `Client` to provide specialized request handling for OAuth 2.0.

The following methods allow for session management and automated request execution:

Methods  
---  
`close()` | Returns: `None` Saves the current token and closes the client session.  
`request(*args, **kwargs)` | Returns: `Response` Performs an API request with automatic credential refresh support. The method checks if credentials are expired before execution; if a response indicates expired credentials, it refreshes the token and retries the request.  
  
### CredStorage

`TIPCommon.oauth.CredStorage(encryption_password: str, chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob)`

Manages the secure storage of OAuth credentials. It uses encryption to protect sensitive token data stored within the platform's context database.

Use the following methods to manage token persistence and identification:

Methods  
---  
`get_instance_identifier()` | Returns: `str` Retrieves the unique identifier for the current SOAR instance, such as a connector or integration ID.  
`get_token()` | Returns: `OauthToken | None` Extracts and decrypts an `OauthToken` from the context database.  
`set_token(token: OauthToken)` | Returns: `None` Encrypts and saves an `OauthToken` into the context database.  
  
### OAuthAdapter

Bases: `ABC`

An abstract base class that defines the interface for OAuth operations. Developers implement this class to support specific third-party OAuth providers.

Implement these abstract methods to define provider-specific logic:

Methods  
---  
`check_signer(token: OauthToken)` | Returns: `bool` Returns `True` if the token signer is valid.  
`prepare_authorized_client(token, auth_client)` | Returns: `AuthorizedOauthClient` Configures the necessary headers or authentication parameters for the provided client.  
`refresh_token()` | Returns: `OauthToken` Performs the token refresh logic and returns a new `OauthToken` data model.  
`static validate_bad_credentials(response)` | Returns: `bool` Checks if an API response indicates expired credentials and raises `AuthenticationError` if the credentials are invalid.  
  
### OauthManager

`TIPCommon.oauth.OauthManager(oauth_adapter: OAuthAdapter, cred_storage: CredStorage)`

Coordinates the interaction between token storage and the OAuth adapter. It handles the logic for checking token expiration and triggering refreshes.

The manager provides the following orchestration methods:

Methods  
---  
`prepare_authorized_client(auth_client)` | Returns: `AuthorizedOauthClient` Prepares the client for authorized requests by applying current token data.  
`refresh_if_bad_credentials(auth_client, response)` | Returns: `bool` Refreshes the token if the provided API response indicates the current credentials are invalid.  
`refresh_if_expired(auth_client)` | Returns: `bool` Checks the token's expiration time and performs a refresh if it has expired.  
`save_token()` | Returns: `None` Persists the current token to secure storage.  
  
### OauthToken

`TIPCommon.oauth.OauthToken(access_token: str, expiration_time: int, refresh_token: str = None, signer: str = None, additional_data: MutableMapping[str, Any] = <factory>)`

A data model representing an OAuth 2.0 token set.

The class includes the following attributes:

Attributes  
---  
`access_token` | `str` The token used to authenticate requests.  
`expiration_time` | `int` The Unix timestamp indicating when the access token expires.  
`refresh_token` | `str` The token used to obtain a new access token. The default value is `None`.  
`signer` | `str` An optional identifier for the token issuer.  
`additional_data` | `MutableMapping[str, Any]` A mapping for provider-specific metadata.  
  
The following methods are available for serializing and deserializing token data:

Methods  
---  
`classmethod from_cache(raw_data)` | Returns: `OauthToken` Creates an `OauthToken` instance from a cached JSON string.  
`to_cache()` | Returns: `JsonString` Serializes the token data into a JSON string for caching or storage.  
  
## Exceptions

The following exceptions are used to signal failures in the OAuth flow, such as invalid credentials or storage issues. Handling these specifically allows for more granular error reporting within Content Hub integrations.

These custom error classes include:

Exceptions  
---  
`AuthenticationError` | Bases: `Exception` Indicates a generic failure during the authentication process.  
`EncryptionError` | Bases: `Exception` Indicates a generic error during the encryption or decryption of credential data.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
