---
url: https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.CreateTransferConfigRequest
title: Class CreateTransferConfigRequest (3.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:14.121109+00:00
---

# Class CreateTransferConfigRequest (3.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.CreateTransferConfigRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateTransferConfigRequest (3.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.24.0 (latest)  3.23.0  3.22.0  3.21.0  3.20.0  3.19.2  3.18.0  3.17.1  3.16.0  3.15.7  3.14.1  3.13.0  3.12.1  3.11.2  3.10.1  3.9.0  3.8.0  3.7.3  3.6.2  3.5.0  3.4.1  3.3.4  3.2.0  3.1.1  3.0.1  2.1.2  2.0.0  1.1.3  1.0.0  0.4.1 
    
    
    CreateTransferConfigRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A request to create a data transfer configuration. If new credentials are needed for this transfer configuration, authorization info must be provided. If authorization info is provided, the transfer configuration will be associated with the user id corresponding to the authorization info. Otherwise, the transfer configuration will be associated with the calling user.

When using a cross project service account for creating a transfer config, you must enable cross project service account usage. For more information, see `Disable attachment of service accounts to resources in other projects <https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_cross_project_service_accounts>`__.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The BigQuery project id where the transfer configuration should be created. Must be in the format projects/{project_id}/locations/{location_id} or projects/{project_id}. If specified location and location of the destination bigquery dataset do not match - the request will fail.   
`transfer_config` |  `[google.cloud.bigquery_datatransfer_v1.types.TransferConfig](https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.TransferConfig)`   
Required. Data transfer configuration to create.   
`authorization_code` |  `str`   
Deprecated: Authorization code was required when `transferConfig.dataSourceId` is 'youtube_channel' but it is no longer used in any data sources. Use `version_info` instead. Optional OAuth2 authorization code to use with this transfer configuration. This is required only if `transferConfig.dataSourceId` is 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain authorization_code, make a request to the following URL: .. raw:: html 
    
    
           https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes
           

\- The client_id is the OAuth client_id of the data source as returned by ListDataSources method. \- data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to create the transfer config.   
`version_info` |  `str`   
Optional version info. This parameter replaces `authorization_code` which is no longer used in any data sources. This is required only if `transferConfig.dataSourceId` is 'youtube_channel' *or* new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain version info, make a request to the following URL: .. raw:: html 
    
    
           https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=version_info&client_id=client_id&scope=data_source_scopes
           

\- The client_id is the OAuth client_id of the data source as returned by ListDataSources method. \- data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to create the transfer config.   
`service_account_name` |  `str`   
Optional service account email. If this field is set, the transfer config will be created with this service account's credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about `using service accounts   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
