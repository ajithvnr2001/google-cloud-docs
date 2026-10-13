---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient
title: Class DataSourcesServiceClient (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:59.415152+00:00
---

# Class DataSourcesServiceClient (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataSourcesServiceClient (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-shopping-merchant-datasources/google-shopping-merchant-datasources/src/main/java/com/google/shopping/merchant/datasources/v1/DataSourcesServiceClient.java)| [Product Reference](https://developers.google.com/merchant/api)  
---|---  
  
Service Description: Service to manage primary, supplemental, inventory and other data sources. See more in the [Merchant Center](https://support.google.com/merchants/answer/7439058) help article.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       DataSourceName name = DataSourceName.of("[ACCOUNT]", "[DATASOURCE]");
       DataSource response = dataSourcesServiceClient.getDataSource(name);
     }
     

Note: close() needs to be called on the DataSourcesServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetDataSource |  Retrieves the data source configuration for the given account. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataSource(GetDataSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataSource(DataSourceName name) 
  * getDataSource(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataSourceCallable() 

  
ListDataSources |  Lists the configurations for data sources for the given account. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataSources(ListDataSourcesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataSources(AccountName parent) 
  * listDataSources(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataSourcesPagedCallable() 
  * listDataSourcesCallable() 

  
CreateDataSource |  Creates the new data source configuration for the given account. This method always creates a new data source. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataSource(CreateDataSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDataSource(AccountName parent, DataSource dataSource) 
  * createDataSource(String parent, DataSource dataSource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataSourceCallable() 

  
UpdateDataSource |  Updates the existing data source configuration. The fields that are set in the update mask but not provided in the resource will be deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataSource(UpdateDataSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDataSource(DataSource dataSource, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataSourceCallable() 

  
DeleteDataSource |  Deletes a data source from your Merchant Center account. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataSource(DeleteDataSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDataSource(DataSourceName name) 
  * deleteDataSource(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataSourceCallable() 

  
FetchDataSource |  Performs the data fetch immediately (even outside fetch schedule) on a data source from your Merchant Center Account. If you need to call this method more than once per day, you should use the Products service to update your product data instead. This method only works on data sources with a file input set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchDataSource(FetchDataSourceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchDataSourceCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataSourcesServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataSourcesServiceSettings dataSourcesServiceSettings =
         DataSourcesServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataSourcesServiceClient dataSourcesServiceClient =
         DataSourcesServiceClient.create(dataSourcesServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataSourcesServiceSettings dataSourcesServiceSettings =
         DataSourcesServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataSourcesServiceClient dataSourcesServiceClient =
         DataSourcesServiceClient.create(dataSourcesServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataSourcesServiceSettings dataSourcesServiceSettings =
         DataSourcesServiceSettings.newHttpJsonBuilder().build();
     DataSourcesServiceClient dataSourcesServiceClient =
         DataSourcesServiceClient.create(dataSourcesServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataSourcesServiceClient

## Static Methods 

### create()
    
    
    public static final DataSourcesServiceClient create()

Constructs an instance of DataSourcesServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataSourcesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataSourcesServiceSettings settings)
    
    
    public static final DataSourcesServiceClient create(DataSourcesServiceSettings settings)

Constructs an instance of DataSourcesServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataSourcesServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataSourcesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataSourcesServiceStub stub)
    
    
    public static final DataSourcesServiceClient create(DataSourcesServiceStub stub)

Constructs an instance of DataSourcesServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataSourcesServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataSourcesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.stub.DataSourcesServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataSourcesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient)` |   
  
## Constructors 

### DataSourcesServiceClient(DataSourcesServiceSettings settings)
    
    
    protected DataSourcesServiceClient(DataSourcesServiceSettings settings)

Constructs an instance of DataSourcesServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataSourcesServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceSettings)`  
  
  
### DataSourcesServiceClient(DataSourcesServiceStub stub)
    
    
    protected DataSourcesServiceClient(DataSourcesServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataSourcesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.stub.DataSourcesServiceStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### createDataSource(@Nullable AccountName parent, DataSource dataSource)
    
    
    public final DataSource createDataSource(@Nullable AccountName parent, DataSource dataSource)

Creates the new data source configuration for the given account. This method always creates a new data source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       AccountName parent = AccountName.of("[ACCOUNT]");
       DataSource dataSource = DataSource.newBuilder().build();
       DataSource response = dataSourcesServiceClient.createDataSource(parent, dataSource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.datasources.v1.AccountName`  
Required. The account where this data source will be created. Format: `accounts/{account}`  
`dataSource` | `[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)`  
Required. The data source to create.  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)` |   
  
### createDataSource(CreateDataSourceRequest request)
    
    
    public final DataSource createDataSource(CreateDataSourceRequest request)

Creates the new data source configuration for the given account. This method always creates a new data source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       CreateDataSourceRequest request =
           CreateDataSourceRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setDataSource(DataSource.newBuilder().build())
               .build();
       DataSource response = dataSourcesServiceClient.createDataSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.CreateDataSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)` |   
  
### createDataSource(String parent, DataSource dataSource)
    
    
    public final DataSource createDataSource(String parent, DataSource dataSource)

Creates the new data source configuration for the given account. This method always creates a new data source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       String parent = AccountName.of("[ACCOUNT]").toString();
       DataSource dataSource = DataSource.newBuilder().build();
       DataSource response = dataSourcesServiceClient.createDataSource(parent, dataSource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The account where this data source will be created. Format: `accounts/{account}`  
`dataSource` | `[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)`  
Required. The data source to create.  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)` |   
  
### createDataSourceCallable()
    
    
    public final UnaryCallable<CreateDataSourceRequest,DataSource> createDataSourceCallable()

Creates the new data source configuration for the given account. This method always creates a new data source.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       CreateDataSourceRequest request =
           CreateDataSourceRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setDataSource(DataSource.newBuilder().build())
               .build();
       ApiFuture<DataSource> future =
           dataSourcesServiceClient.createDataSourceCallable().futureCall(request);
       // Do something.
       DataSource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.CreateDataSourceRequest),[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)>` |   
  
### deleteDataSource(@Nullable DataSourceName name)
    
    
    public final void deleteDataSource(@Nullable DataSourceName name)

Deletes a data source from your Merchant Center account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       DataSourceName name = DataSourceName.of("[ACCOUNT]", "[DATASOURCE]");
       dataSourcesServiceClient.deleteDataSource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.datasources.v1.DataSourceName`  
Required. The name of the data source to delete. Format: `accounts/{account}/dataSources/{datasource}`  
  
### deleteDataSource(DeleteDataSourceRequest request)
    
    
    public final void deleteDataSource(DeleteDataSourceRequest request)

Deletes a data source from your Merchant Center account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       DeleteDataSourceRequest request =
           DeleteDataSourceRequest.newBuilder()
               .setName(DataSourceName.of("[ACCOUNT]", "[DATASOURCE]").toString())
               .build();
       dataSourcesServiceClient.deleteDataSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DeleteDataSourceRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDataSource(String name)
    
    
    public final void deleteDataSource(String name)

Deletes a data source from your Merchant Center account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       String name = DataSourceName.of("[ACCOUNT]", "[DATASOURCE]").toString();
       dataSourcesServiceClient.deleteDataSource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the data source to delete. Format: `accounts/{account}/dataSources/{datasource}`  
  
### deleteDataSourceCallable()
    
    
    public final UnaryCallable<DeleteDataSourceRequest,Empty> deleteDataSourceCallable()

Deletes a data source from your Merchant Center account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       DeleteDataSourceRequest request =
           DeleteDataSourceRequest.newBuilder()
               .setName(DataSourceName.of("[ACCOUNT]", "[DATASOURCE]").toString())
               .build();
       ApiFuture<Empty> future =
           dataSourcesServiceClient.deleteDataSourceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DeleteDataSourceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### fetchDataSource(FetchDataSourceRequest request)
    
    
    public final void fetchDataSource(FetchDataSourceRequest request)

Performs the data fetch immediately (even outside fetch schedule) on a data source from your Merchant Center Account. If you need to call this method more than once per day, you should use the Products service to update your product data instead. This method only works on data sources with a file input set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       FetchDataSourceRequest request =
           FetchDataSourceRequest.newBuilder()
               .setName(DataSourceName.of("[ACCOUNT]", "[DATASOURCE]").toString())
               .build();
       dataSourcesServiceClient.fetchDataSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.FetchDataSourceRequest)`  
The request object containing all of the parameters for the API call.  
  
### fetchDataSourceCallable()
    
    
    public final UnaryCallable<FetchDataSourceRequest,Empty> fetchDataSourceCallable()

Performs the data fetch immediately (even outside fetch schedule) on a data source from your Merchant Center Account. If you need to call this method more than once per day, you should use the Products service to update your product data instead. This method only works on data sources with a file input set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       FetchDataSourceRequest request =
           FetchDataSourceRequest.newBuilder()
               .setName(DataSourceName.of("[ACCOUNT]", "[DATASOURCE]").toString())
               .build();
       ApiFuture<Empty> future =
           dataSourcesServiceClient.fetchDataSourceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.FetchDataSourceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDataSource(@Nullable DataSourceName name)
    
    
    public final DataSource getDataSource(@Nullable DataSourceName name)

Retrieves the data source configuration for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       DataSourceName name = DataSourceName.of("[ACCOUNT]", "[DATASOURCE]");
       DataSource response = dataSourcesServiceClient.getDataSource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.datasources.v1.DataSourceName`  
Required. The name of the data source to retrieve. Format: `accounts/{account}/dataSources/{datasource}`  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)` |   
  
### getDataSource(GetDataSourceRequest request)
    
    
    public final DataSource getDataSource(GetDataSourceRequest request)

Retrieves the data source configuration for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       GetDataSourceRequest request =
           GetDataSourceRequest.newBuilder()
               .setName(DataSourceName.of("[ACCOUNT]", "[DATASOURCE]").toString())
               .build();
       DataSource response = dataSourcesServiceClient.getDataSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.GetDataSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)` |   
  
### getDataSource(String name)
    
    
    public final DataSource getDataSource(String name)

Retrieves the data source configuration for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       String name = DataSourceName.of("[ACCOUNT]", "[DATASOURCE]").toString();
       DataSource response = dataSourcesServiceClient.getDataSource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the data source to retrieve. Format: `accounts/{account}/dataSources/{datasource}`  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)` |   
  
### getDataSourceCallable()
    
    
    public final UnaryCallable<GetDataSourceRequest,DataSource> getDataSourceCallable()

Retrieves the data source configuration for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       GetDataSourceRequest request =
           GetDataSourceRequest.newBuilder()
               .setName(DataSourceName.of("[ACCOUNT]", "[DATASOURCE]").toString())
               .build();
       ApiFuture<DataSource> future =
           dataSourcesServiceClient.getDataSourceCallable().futureCall(request);
       // Do something.
       DataSource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.GetDataSourceRequest),[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)>` |   
  
### getSettings()
    
    
    public final @Nullable DataSourcesServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.shopping.merchant.datasources.v1.DataSourcesServiceSettings` |   
  
### getStub()
    
    
    public DataSourcesServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataSourcesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.stub.DataSourcesServiceStub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listDataSources(@Nullable AccountName parent)
    
    
    public final DataSourcesServiceClient.ListDataSourcesPagedResponse listDataSources(@Nullable AccountName parent)

Lists the configurations for data sources for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       AccountName parent = AccountName.of("[ACCOUNT]");
       for (DataSource element : dataSourcesServiceClient.listDataSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.datasources.v1.AccountName`  
Required. The account to list data sources for. Format: `accounts/{account}`  
**Returns**  
---  
**Type** | **Description**  
`[DataSourcesServiceClient.ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient.ListDataSourcesPagedResponse)` |   
  
### listDataSources(ListDataSourcesRequest request)
    
    
    public final DataSourcesServiceClient.ListDataSourcesPagedResponse listDataSources(ListDataSourcesRequest request)

Lists the configurations for data sources for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       ListDataSourcesRequest request =
           ListDataSourcesRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DataSource element : dataSourcesServiceClient.listDataSources(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.ListDataSourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSourcesServiceClient.ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient.ListDataSourcesPagedResponse)` |   
  
### listDataSources(String parent)
    
    
    public final DataSourcesServiceClient.ListDataSourcesPagedResponse listDataSources(String parent)

Lists the configurations for data sources for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       String parent = AccountName.of("[ACCOUNT]").toString();
       for (DataSource element : dataSourcesServiceClient.listDataSources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The account to list data sources for. Format: `accounts/{account}`  
**Returns**  
---  
**Type** | **Description**  
`[DataSourcesServiceClient.ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient.ListDataSourcesPagedResponse)` |   
  
### listDataSourcesCallable()
    
    
    public final UnaryCallable<ListDataSourcesRequest,ListDataSourcesResponse> listDataSourcesCallable()

Lists the configurations for data sources for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       ListDataSourcesRequest request =
           ListDataSourcesRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDataSourcesResponse response =
             dataSourcesServiceClient.listDataSourcesCallable().call(request);
         for (DataSource element : response.getDataSourcesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.ListDataSourcesRequest),[ListDataSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.ListDataSourcesResponse)>` |   
  
### listDataSourcesPagedCallable()
    
    
    public final UnaryCallable<ListDataSourcesRequest,DataSourcesServiceClient.ListDataSourcesPagedResponse> listDataSourcesPagedCallable()

Lists the configurations for data sources for the given account.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       ListDataSourcesRequest request =
           ListDataSourcesRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DataSource> future =
           dataSourcesServiceClient.listDataSourcesPagedCallable().futureCall(request);
       // Do something.
       for (DataSource element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.ListDataSourcesRequest),[ListDataSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSourcesServiceClient.ListDataSourcesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDataSource(DataSource dataSource, FieldMask updateMask)
    
    
    public final DataSource updateDataSource(DataSource dataSource, FieldMask updateMask)

Updates the existing data source configuration. The fields that are set in the update mask but not provided in the resource will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       DataSource dataSource = DataSource.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataSource response = dataSourcesServiceClient.updateDataSource(dataSource, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataSource` | `[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)`  
Required. The data source resource to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of data source fields to be updated. Fields specified in the update mask without a value specified in the body will be deleted from the data source. Providing special "*" value for full data source replacement is not supported. For example, If you insert `updateMask=displayName` in the request, it will only update the `displayName` leaving all other fields untouched.  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)` |   
  
### updateDataSource(UpdateDataSourceRequest request)
    
    
    public final DataSource updateDataSource(UpdateDataSourceRequest request)

Updates the existing data source configuration. The fields that are set in the update mask but not provided in the resource will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       UpdateDataSourceRequest request =
           UpdateDataSourceRequest.newBuilder()
               .setDataSource(DataSource.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       DataSource response = dataSourcesServiceClient.updateDataSource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.UpdateDataSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)` |   
  
### updateDataSourceCallable()
    
    
    public final UnaryCallable<UpdateDataSourceRequest,DataSource> updateDataSourceCallable()

Updates the existing data source configuration. The fields that are set in the update mask but not provided in the resource will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataSourcesServiceClient dataSourcesServiceClient = DataSourcesServiceClient.create()) {
       UpdateDataSourceRequest request =
           UpdateDataSourceRequest.newBuilder()
               .setDataSource(DataSource.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<DataSource> future =
           dataSourcesServiceClient.updateDataSourceCallable().futureCall(request);
       // Do something.
       DataSource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.UpdateDataSourceRequest),[DataSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1.DataSource)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
