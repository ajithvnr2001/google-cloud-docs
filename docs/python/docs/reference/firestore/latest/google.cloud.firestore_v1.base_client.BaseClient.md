---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_client.BaseClient
title: Class BaseClient (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:33.588239+00:00
---

# Class BaseClient (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_client.BaseClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BaseClient (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    BaseClient(
        project=None,
        credentials=None,
        database=None,
        client_info=google.api_core.gapic_v1.client_info.ClientInfo,
        client_options=None,
    )

Client for interacting with Google Cloud Firestore API.

**Note:** Since the Cloud Firestore API requires the gRPC transport, no `_http` argument is accepted by this class. 

## Parameters  
  
---  
**Name** | **Description**  
`project` |  `Optional[str]`   
The project which the client acts on behalf of. If not passed, falls back to the default inferred from the environment.  
`credentials` |  `Optional[`google.auth.credentials.Credentials`]`   
The OAuth2 Credentials to use for this client. If not passed, falls back to the default inferred from the environment.  
`database` |  `Optional[str]`   
The database name that the client targets. For now, `DEFAULT_DATABASE` (the default value) is the only valid database.  
`client_info` |  `Optional[google.api_core.gapic_v1.client_info.ClientInfo]`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own library or partner tool.  
`client_options` |  `Union[dict, google.api_core.client_options.ClientOptions]`   
Client options used to set user options on the client. API Endpoint should be set through client_options.  
  
## Methods 

### bulk_writer
    
    
    bulk_writer(
        options: typing.Optional[
            google.cloud.firestore_v1.bulk_writer.BulkWriterOptions
        ] = None,
    ) -> google.cloud.firestore_v1.bulk_writer.BulkWriter

Get a BulkWriter instance from this client.

**Returns**  
---  
**Type** | **Description**  
`:class:`@[google.cloud.firestore_v1.bulk_writer.BulkWriter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter)`` | A utility to efficiently create and save many `WriteBatch` instances to the server.  
  
### field_path
    
    
    field_path(*field_names: str) -> str

Create a **field path** from a list of nested field names.

A **field path** is a `.`-delimited concatenation of the field names. It is used to represent a nested field. For example, in the data
    
    
    data = {
       'aa': {
           'bb': {
               'cc': 10,
           },
       },
    }
    

the field path `'aa.bb.cc'` represents the data stored in `data['aa']['bb']['cc']`.

**Returns**  
---  
**Type** | **Description**  
`str` | The `.`-delimited field path.  
  
### pipeline
    
    
    pipeline() -> google.cloud.firestore_v1.pipeline_source.PipelineSource

Start a pipeline with this client.

**Returns**  
---  
**Type** | **Description**  
`PipelineSource` | A pipeline that uses this client`  
  
### write_option
    
    
    write_option(
        **kwargs,
    ) -> typing.Union[
        google.cloud.firestore_v1._helpers.ExistsOption,
        google.cloud.firestore_v1._helpers.LastUpdateOption,
    ]

Create a write option for write operations.

Write operations include xref_set, xref_update and xref_delete.

One of the following keyword arguments must be provided:

  * `last_update_time` (`google.protobuf.timestamp_pb2. Timestamp`): A timestamp. When set, the target document must exist and have been last updated at that time. Protobuf `update_time` timestamps are typically returned from methods that perform write operations as part of a "write result" protobuf or directly.
  * `exists` (`bool`): Indicates if the document being modified should already exist.



Providing no argument would make the option have no effect (so it is not allowed). Providing multiple would be an apparent contradiction, since `last_update_time` assumes that the document **was** updated (it can't have been updated if it doesn't exist) and `exists` indicate that it is unknown if the document exists or not.

**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If anything other than exactly one argument is provided by the caller.  
**Returns**  
---  
**Type** | **Description**  
`WriteOption` | The option to be used to configure a write message.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
