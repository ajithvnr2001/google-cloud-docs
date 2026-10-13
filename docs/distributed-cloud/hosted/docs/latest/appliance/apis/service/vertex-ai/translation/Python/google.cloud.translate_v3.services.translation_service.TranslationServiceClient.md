---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/Python/google.cloud.translate_v3.services.translation_service.TranslationServiceClient
title: Class TranslationServiceClient (3.12.0) \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:13.171098+00:00
---

# Class TranslationServiceClient (3.12.0)  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/Python/google.cloud.translate_v3.services.translation_service.TranslationServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Class TranslationServiceClient (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    TranslationServiceClient(*, credentials: typing.Optional[google.auth.credentials.Credentials] = None, transport: typing.Optional[typing.Union[str, google.cloud.translate_v3.services.translation_service.transports.base.TranslationServiceTransport]] = None, client_options: typing.Optional[typing.Union[google.api_core.client_options.ClientOptions, dict]] = None, client_info: google.api_core.gapic_v1.client_info.ClientInfo = <google.api_core.gapic_v1.client_info.ClientInfo object>)

Provides natural language translation operations.

## Properties 

### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type**| **Description**  
`TranslationServiceTransport`| The transport used by the client instance.  
  
## Methods 

### TranslationServiceClient
    
    
    TranslationServiceClient(*, credentials: typing.Optional[google.auth.credentials.Credentials] = None, transport: typing.Optional[typing.Union[str, google.cloud.translate_v3.services.translation_service.transports.base.TranslationServiceTransport]] = None, client_options: typing.Optional[typing.Union[google.api_core.client_options.ClientOptions, dict]] = None, client_info: google.api_core.gapic_v1.client_info.ClientInfo = <google.api_core.gapic_v1.client_info.ClientInfo object>)

Instantiates the translation service client.

**Parameters**  
---  
**Name**| **Description**  
`credentials`|  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport`|  `Union[str, TranslationServiceTransport]`   
The transport to use. If set to None, a transport is chosen automatically.  
`client_options`|  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. It won't take effect if a `transport` instance is provided. (1) The `api_endpoint` property can be used to override the default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT environment variable can also be used to override the endpoint: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto switch to the default mTLS endpoint if client certificate is present, this is the default value). However, the `api_endpoint` property takes precedence if provided. (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide client certificate for mutual TLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used.  
`client_info`|  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type**| **Description**  
`google.auth.exceptions.MutualTLSChannelError`| If mutual TLS transport creation failed for any reason.  
  
### __exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

**Warning:** ONLY use as a context manager if the transport is NOT shared with other clients! Exiting the with block will CLOSE the transport and may cause errors in other clients! 

### detect_language
    
    
    detect_language(
        request: typing.Optional[
            typing.Union[
                google.cloud.translate_v3.types.translation_service.DetectLanguageRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        mime_type: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> google.cloud.translate_v3.types.translation_service.DetectLanguageResponse

Detects the language of text within a request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)_v3
    
    def sample_detect_language():
        # Create a client
        client = translate_v3.[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        # Initialize request argument(s)
        request = translate_v3.[DetectLanguageRequest](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.DetectLanguageRequest.html)(
            content="content_value",
            parent="parent_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[detect_language](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_detect_language)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`request`|  `Union[[google.cloud.translate_v3.types.DetectLanguageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/Python/google.cloud.translate_v3.types.DetectLanguageRequest), dict]`   
The request object. The request message for language detection.  
`parent`|  `str`   
Required. Project or location to make a call. Must refer to a caller's project. Format: `projects/{project-number-or-id}/locations/{location-id}` or `projects/{project-number-or-id}`. For global calls, use `projects/{project-number-or-id}/locations/global` or `projects/{project-number-or-id}`. Only models within the same region (has same location-id) can be used. Otherwise an INVALID_ARGUMENT (400) error is returned. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`model`|  `str`   
Optional. The language detection model to be used. Format: `projects/{project-number-or-id}/locations/{location-id}/models/language-detection/{model-id}` Only one language detection model is currently supported: `projects/{project-number-or-id}/locations/{location-id}/models/language-detection/default`. If not specified, the default model is used. This corresponds to the `model` field on the `request` instance; if `request` is provided, this should not be set.  
`mime_type`|  `str`   
Optional. The format of the source text, for example, "text/html", "text/plain". If left blank, the MIME type defaults to "text/html". This corresponds to the `mime_type` field on the `request` instance; if `request` is provided, this should not be set.  
`content`|  `str`   
The content of the input stored as a string. This corresponds to the `content` field on the `request` instance; if `request` is provided, this should not be set.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
**Parameter**  
---  
**Name**| **Description**  
`filename`|  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type**| **Description**  
`TranslationServiceClient`| The constructed client.  
**Exceptions**  
---  
**Type**| **Description**  
`google.auth.exceptions.MutualTLSChannelError`| If any errors happen.  
**Returns**  
---  
**Type**| **Description**  
`Tuple[str, Callable[[], Tuple[bytes, bytes]]]`| returns the API endpoint and the client cert source to use.  
  
### get_supported_languages
    
    
    get_supported_languages(
        request: typing.Optional[
            typing.Union[
                google.cloud.translate_v3.types.translation_service.GetSupportedLanguagesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        display_language_code: typing.Optional[str] = None,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> google.cloud.translate_v3.types.translation_service.SupportedLanguages

Returns a list of supported languages for translation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)_v3
    
    def sample_get_supported_languages():
        # Create a client
        client = translate_v3.[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        # Initialize request argument(s)
        request = translate_v3.[GetSupportedLanguagesRequest](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.GetSupportedLanguagesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[get_supported_languages](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_get_supported_languages)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`request`|  `Union[[google.cloud.translate_v3.types.GetSupportedLanguagesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/Python/google.cloud.translate_v3.types.GetSupportedLanguagesRequest), dict]`   
The request object. The request message for discovering supported languages.  
`parent`|  `str`   
Required. Project or location to make a call. Must refer to a caller's project. Format: `projects/{project-number-or-id}` or `projects/{project-number-or-id}/locations/{location-id}`. For global calls, use `projects/{project-number-or-id}/locations/global` or `projects/{project-number-or-id}`. Non-global location is required for AutoML models. Only models within the same region (have same location-id) can be used, otherwise an INVALID_ARGUMENT (400) error is returned. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`model`|  `str`   
Optional. Get supported languages of this model. The format depends on model type: - AutoML Translation models: `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}` \- General (built-in) models: `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`, Returns languages supported by the specified model. If missing, we get supported languages of Google general NMT model. This corresponds to the `model` field on the `request` instance; if `request` is provided, this should not be set.  
`display_language_code`|  `str`   
Optional. The language to use to return localized, human readable names of supported languages. If missing, then display names are not returned in a response. This corresponds to the `display_language_code` field on the `request` instance; if `request` is provided, this should not be set.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
**Returns**  
---  
**Type**| **Description**  
`[google.cloud.translate_v3.types.SupportedLanguages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/Python/google.cloud.translate_v3.types.SupportedLanguages)`| The response message for discovering supported languages.  
  
### translate_text
    
    
    translate_text(
        request: typing.Optional[
            typing.Union[
                google.cloud.translate_v3.types.translation_service.TranslateTextRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target_language_code: typing.Optional[str] = None,
        contents: typing.Optional[typing.MutableSequence[str]] = None,
        model: typing.Optional[str] = None,
        mime_type: typing.Optional[str] = None,
        source_language_code: typing.Optional[str] = None,
        retry: typing.Union[
            google.api_core.retry.Retry, google.api_core.gapic_v1.method._MethodDefault
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, str]] = ()
    ) -> google.cloud.translate_v3.types.translation_service.TranslateTextResponse

Translates input text and returns translated text.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)_v3
    
    def sample_translate_text():
        # Create a client
        client = translate_v3.[TranslationServiceClient](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)()
    
        # Initialize request argument(s)
        request = translate_v3.[TranslateTextRequest](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.TranslateTextRequest.html)(
            contents=['contents_value1', 'contents_value2'],
            target_language_code="target_language_code_value",
            parent="parent_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html).[translate_text](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_translate_text)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name**| **Description**  
`request`|  `Union[[google.cloud.translate_v3.types.TranslateTextRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/Python/google.cloud.translate_v3.types.TranslateTextRequest), dict]`   
The request object. The request message for synchronous translation.  
`parent`|  `str`   
Required. Project or location to make a call. Must refer to a caller's project. Format: `projects/{project-number-or-id}` or `projects/{project-number-or-id}/locations/{location-id}`. For global calls, use `projects/{project-number-or-id}/locations/global` or `projects/{project-number-or-id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`target_language_code`|  `str`   
Required. The ISO-639 language code to use for translation of the input text, set to one of the language codes listed in Language Support. This corresponds to the `target_language_code` field on the `request` instance; if `request` is provided, this should not be set.  
`contents`|  `MutableSequence[str]`   
Required. The content of the input in string format. We recommend the total content be less than 30,000 codepoints. The max length of this field is 1024. This corresponds to the `contents` field on the `request` instance; if `request` is provided, this should not be set.  
`model`|  `str`   
Optional. The `model` type requested for this translation. The format depends on model type: - AutoML Translation models: `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}` \- General (built-in) models: `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`, For global (non-regionalized) requests, use `location-id` `global`. For example, `projects/{project-number-or-id}/locations/global/models/general/nmt`. If not provided, the default Google model (NMT) will be used This corresponds to the `model` field on the `request` instance; if `request` is provided, this should not be set.  
`mime_type`|  `str`   
Optional. The format of the source text, for example, "text/html", "text/plain". If left blank, the MIME type defaults to "text/html". This corresponds to the `mime_type` field on the `request` instance; if `request` is provided, this should not be set.  
`source_language_code`|  `str`   
Optional. The ISO-639 language code of the input text if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in Language Support. If the source language isn't specified, the API attempts to identify the source language automatically and returns the source language within the response. This corresponds to the `source_language_code` field on the `request` instance; if `request` is provided, this should not be set.  
`retry`|  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout`|  `float`   
The timeout for this request.  
`metadata`|  `Sequence[Tuple[str, str]]`   
Strings which should be sent along with the request as metadata.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
