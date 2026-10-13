---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/BigtableClient/
title: Cloud Bigtable Client - Class BigtableClient (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:10.251708+00:00
---

# Cloud Bigtable Client - Class BigtableClient (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/BigtableClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable Client - Class BigtableClient (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable Client class BigtableClient.

Google Cloud Bigtable is Google's NoSQL Big Data database service.

Find more information at the [Google Cloud Bigtable Docs](https://cloud.google.com/bigtable/docs/).

Example:
    
    
    use Google\Cloud\Bigtable\BigtableClient;
    
    $bigtable = new BigtableClient();
    

## Namespace

Google \ Cloud \ Bigtable

## Methods 

### __construct

Create a Bigtable client.

**Parameters**  
---  
**Name** | **Description**  
`config` |  `array`   
Configuration options.  
`↳ projectId` |  `string`   
The project ID from the Google Developer's Console.  
`↳ apiEndpoint` |  `string`   
The address of the API remote host. May optionally include the port, formatted as "  
`↳ credentials` |  `[Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html)|[Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html)`   
This option should only be used with a pre-constructed [Google\Auth\FetchAuthTokenInterface](https://docs.cloud.google.com/php/docs/reference/auth/latest/FetchAuthTokenInterface.html) or [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html) object. Note that when one of these objects are provided, any settings in $credentialsConfig will be ignored. **Important** : If you are providing a path to a credentials file, or a decoded credentials file as a PHP array, this usage is now DEPRECATED. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data. It is recommended to create the credentials explicitly `use Google\Auth\Credentials\ServiceAccountCredentials; use Google\Cloud\Bigtable\BigtableClient; $creds = new ServiceAccountCredentials($scopes, $json); $options = new BigtableClient(['credentials' => $creds]);` <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
`↳ credentialsConfig` |  `array`   
Options used to configure credentials, including auth token caching, for the client. For a full list of supporting configuration options, see [Google\ApiCore\CredentialsWrapper](https://docs.cloud.google.com/php/docs/reference/gax/latest/CredentialsWrapper.html).  
`↳ disableRetries` |  `bool`   
Determines whether or not retries defined by the client configuration should be disabled. **Defaults to** `false`.  
`↳ clientConfig` |  `string|array`   
Client method configuration, including retry settings. This option can be either a path to a JSON file, or a PHP array containing the decoded JSON data.  
`↳ transport` |  `string|[Google\ApiCore\Transport\TransportInterface](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.TransportInterface.html)`   
The transport used for executing network requests. May be either the string `rest` or `grpc`. **Defaults to** `grpc` if gRPC support is detected on the system. _Advanced usage_ : Additionally, it is possible to pass in an already instantiated [Google\ApiCore\Transport\TransportInterface](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.TransportInterface.html) object. Note that when this object is provided, any settings in $config['transportConfig'] and the $config['apiEndpoint'] setting will be ignored.  
`↳ transportConfig` |  `array`   
Configuration options that will be used to construct the transport. Options for each supported transport type should be passed in a key for that transport. For example: $transportConfig = [ 'grpc' => [...], 'rest' => [...] ]; See the `build` method on [Google\ApiCore\Transport\GrpcTransport](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.GrpcTransport.html) and [Google\ApiCore\Transport\RestTransport](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.RestTransport.html) for the supported options.  
`↳ quotaProject` |  `string`   
Specifies a user project to bill for access charges associated with the request.  
`↳ pingAndWarm` |  `bool`   
EXPERIMENTAL When true, calls the [V2\Client\BigtableClient::pingAndWarm()](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/V2.Client.BigtableClient#_Google_Cloud_Bigtable_V2_Client_BigtableClient__pingAndWarm__) RPC to establish a persistent gRPC channel before making an RPC call.  
  
### table

Returns a table instance which can be used to read rows and to perform insert, update, and delete operations.

Example:
    
    
    $table = $bigtable->table('my-instance', 'my-table');
    

**Parameters**  
---  
**Name** | **Description**  
`instanceId` |  `string`   
The instance ID.  
`tableId` |  `string`   
The table ID.  
`options` |  `array`   
Configuration options.  
`↳ appProfileId` |  `string`   
This value specifies routing for replication. **Defaults to** the "default" application profile.  
`↳ headers` |  `array`   
Headers to be passed with each request.  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Table)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
