---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient
title: Class CompanyServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:33.326239+00:00
---

# Class CompanyServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CompanyServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CompanyServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling Company objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       CompanyName name = CompanyName.of("[NETWORK_CODE]", "[COMPANY]");
       Company response = companyServiceClient.getCompany(name);
     }
     

Note: close() needs to be called on the CompanyServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCompany |  Retrieves a Company object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCompany(GetCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCompany(CompanyName name) 
  * getCompany(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCompanyCallable() 

  
ListCompanies |  Lists Company objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCompanies(ListCompaniesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCompanies(NetworkName parent) 
  * listCompanies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCompaniesPagedCallable() 
  * listCompaniesCallable() 

  
CreateCompany |  Creates a Company object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCompany(CreateCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCompany(NetworkName parent, Company company) 
  * createCompany(String parent, Company company) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCompanyCallable() 

  
BatchCreateCompanies |  Creates Company objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateCompanies(NetworkName parent, List<CreateCompanyRequest> requests) 
  * batchCreateCompanies(String parent, List<CreateCompanyRequest> requests) 
  * batchCreateCompanies(BatchCreateCompaniesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateCompaniesCallable() 

  
UpdateCompany |  Updates a Company object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCompany(UpdateCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCompany(Company company, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCompanyCallable() 

  
BatchUpdateCompanies |  Batch updates Company objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateCompanies(NetworkName parent, List<UpdateCompanyRequest> requests) 
  * batchUpdateCompanies(String parent, List<UpdateCompanyRequest> requests) 
  * batchUpdateCompanies(BatchUpdateCompaniesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateCompaniesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CompanyServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompanyServiceSettings companyServiceSettings =
         CompanyServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CompanyServiceClient companyServiceClient = CompanyServiceClient.create(companyServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompanyServiceSettings companyServiceSettings =
         CompanyServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CompanyServiceClient companyServiceClient = CompanyServiceClient.create(companyServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CompanyServiceClient

## Static Methods 

### create()
    
    
    public static final CompanyServiceClient create()

Constructs an instance of CompanyServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CompanyServiceSettings settings)
    
    
    public static final CompanyServiceClient create(CompanyServiceSettings settings)

Constructs an instance of CompanyServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompanyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CompanyServiceStub stub)
    
    
    public static final CompanyServiceClient create(CompanyServiceStub stub)

Constructs an instance of CompanyServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CompanyServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CompanyServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient)` |   
  
## Constructors 

### CompanyServiceClient(CompanyServiceSettings settings)
    
    
    protected CompanyServiceClient(CompanyServiceSettings settings)

Constructs an instance of CompanyServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompanyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceSettings)`  
  
  
### CompanyServiceClient(CompanyServiceStub stub)
    
    
    protected CompanyServiceClient(CompanyServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CompanyServiceStub)`  
  
  
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
  
### batchCreateCompanies(@Nullable NetworkName parent, List<CreateCompanyRequest> requests)
    
    
    public final BatchCreateCompaniesResponse batchCreateCompanies(@Nullable NetworkName parent, List<CreateCompanyRequest> requests)

Creates Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateCompanyRequest> requests = new ArrayList<>();
       BatchCreateCompaniesResponse response =
           companyServiceClient.batchCreateCompanies(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where [Companies][] will be created. Format: `networks/{network_code}` The parent field in the CreateCompanyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCompanyRequest)>`  
Required. The Company objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCompaniesResponse)` |   
  
### batchCreateCompanies(BatchCreateCompaniesRequest request)
    
    
    public final BatchCreateCompaniesResponse batchCreateCompanies(BatchCreateCompaniesRequest request)

Creates Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       BatchCreateCompaniesRequest request =
           BatchCreateCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCompanyRequest>())
               .build();
       BatchCreateCompaniesResponse response = companyServiceClient.batchCreateCompanies(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCompaniesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCompaniesResponse)` |   
  
### batchCreateCompanies(String parent, List<CreateCompanyRequest> requests)
    
    
    public final BatchCreateCompaniesResponse batchCreateCompanies(String parent, List<CreateCompanyRequest> requests)

Creates Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateCompanyRequest> requests = new ArrayList<>();
       BatchCreateCompaniesResponse response =
           companyServiceClient.batchCreateCompanies(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where [Companies][] will be created. Format: `networks/{network_code}` The parent field in the CreateCompanyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCompanyRequest)>`  
Required. The Company objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCompaniesResponse)` |   
  
### batchCreateCompaniesCallable()
    
    
    public final UnaryCallable<BatchCreateCompaniesRequest,BatchCreateCompaniesResponse> batchCreateCompaniesCallable()

Creates Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       BatchCreateCompaniesRequest request =
           BatchCreateCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCompanyRequest>())
               .build();
       ApiFuture<BatchCreateCompaniesResponse> future =
           companyServiceClient.batchCreateCompaniesCallable().futureCall(request);
       // Do something.
       BatchCreateCompaniesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCompaniesRequest),[BatchCreateCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCompaniesResponse)>` |   
  
### batchUpdateCompanies(@Nullable NetworkName parent, List<UpdateCompanyRequest> requests)
    
    
    public final BatchUpdateCompaniesResponse batchUpdateCompanies(@Nullable NetworkName parent, List<UpdateCompanyRequest> requests)

Batch updates Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateCompanyRequest> requests = new ArrayList<>();
       BatchUpdateCompaniesResponse response =
           companyServiceClient.batchUpdateCompanies(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where [Companies][] will be updated. Format: `networks/{network_code}` The parent field in the UpdateCompanyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCompanyRequest)>`  
Required. The Company objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCompaniesResponse)` |   
  
### batchUpdateCompanies(BatchUpdateCompaniesRequest request)
    
    
    public final BatchUpdateCompaniesResponse batchUpdateCompanies(BatchUpdateCompaniesRequest request)

Batch updates Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       BatchUpdateCompaniesRequest request =
           BatchUpdateCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCompanyRequest>())
               .build();
       BatchUpdateCompaniesResponse response = companyServiceClient.batchUpdateCompanies(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCompaniesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCompaniesResponse)` |   
  
### batchUpdateCompanies(String parent, List<UpdateCompanyRequest> requests)
    
    
    public final BatchUpdateCompaniesResponse batchUpdateCompanies(String parent, List<UpdateCompanyRequest> requests)

Batch updates Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateCompanyRequest> requests = new ArrayList<>();
       BatchUpdateCompaniesResponse response =
           companyServiceClient.batchUpdateCompanies(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where [Companies][] will be updated. Format: `networks/{network_code}` The parent field in the UpdateCompanyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCompanyRequest)>`  
Required. The Company objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCompaniesResponse)` |   
  
### batchUpdateCompaniesCallable()
    
    
    public final UnaryCallable<BatchUpdateCompaniesRequest,BatchUpdateCompaniesResponse> batchUpdateCompaniesCallable()

Batch updates Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       BatchUpdateCompaniesRequest request =
           BatchUpdateCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCompanyRequest>())
               .build();
       ApiFuture<BatchUpdateCompaniesResponse> future =
           companyServiceClient.batchUpdateCompaniesCallable().futureCall(request);
       // Do something.
       BatchUpdateCompaniesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCompaniesRequest),[BatchUpdateCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCompaniesResponse)>` |   
  
### close()
    
    
    public final void close()

### createCompany(@Nullable NetworkName parent, Company company)
    
    
    public final Company createCompany(@Nullable NetworkName parent, Company company)

Creates a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Company company = Company.newBuilder().build();
       Company response = companyServiceClient.createCompany(parent, company);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this Company will be created. Format: `networks/{network_code}`  
`company` | `[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)`  
Required. The Company to create.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)` |   
  
### createCompany(CreateCompanyRequest request)
    
    
    public final Company createCompany(CreateCompanyRequest request)

Creates a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       CreateCompanyRequest request =
           CreateCompanyRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCompany(Company.newBuilder().build())
               .build();
       Company response = companyServiceClient.createCompany(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)` |   
  
### createCompany(String parent, Company company)
    
    
    public final Company createCompany(String parent, Company company)

Creates a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Company company = Company.newBuilder().build();
       Company response = companyServiceClient.createCompany(parent, company);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this Company will be created. Format: `networks/{network_code}`  
`company` | `[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)`  
Required. The Company to create.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)` |   
  
### createCompanyCallable()
    
    
    public final UnaryCallable<CreateCompanyRequest,Company> createCompanyCallable()

Creates a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       CreateCompanyRequest request =
           CreateCompanyRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCompany(Company.newBuilder().build())
               .build();
       ApiFuture<Company> future = companyServiceClient.createCompanyCallable().futureCall(request);
       // Do something.
       Company response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCompanyRequest),[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)>` |   
  
### getCompany(@Nullable CompanyName name)
    
    
    public final Company getCompany(@Nullable CompanyName name)

Retrieves a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       CompanyName name = CompanyName.of("[NETWORK_CODE]", "[COMPANY]");
       Company response = companyServiceClient.getCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CompanyName`  
Required. The resource name of the Company. Format: `networks/{network_code}/companies/{company_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)` |   
  
### getCompany(GetCompanyRequest request)
    
    
    public final Company getCompany(GetCompanyRequest request)

Retrieves a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       GetCompanyRequest request =
           GetCompanyRequest.newBuilder()
               .setName(CompanyName.of("[NETWORK_CODE]", "[COMPANY]").toString())
               .build();
       Company response = companyServiceClient.getCompany(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCompanyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)` |   
  
### getCompany(String name)
    
    
    public final Company getCompany(String name)

Retrieves a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String name = CompanyName.of("[NETWORK_CODE]", "[COMPANY]").toString();
       Company response = companyServiceClient.getCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Company. Format: `networks/{network_code}/companies/{company_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)` |   
  
### getCompanyCallable()
    
    
    public final UnaryCallable<GetCompanyRequest,Company> getCompanyCallable()

Retrieves a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       GetCompanyRequest request =
           GetCompanyRequest.newBuilder()
               .setName(CompanyName.of("[NETWORK_CODE]", "[COMPANY]").toString())
               .build();
       ApiFuture<Company> future = companyServiceClient.getCompanyCallable().futureCall(request);
       // Do something.
       Company response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCompanyRequest),[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)>` |   
  
### getSettings()
    
    
    public final @Nullable CompanyServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CompanyServiceSettings` |   
  
### getStub()
    
    
    public CompanyServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CompanyServiceStub)` |   
  
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
  
### listCompanies(@Nullable NetworkName parent)
    
    
    public final CompanyServiceClient.ListCompaniesPagedResponse listCompanies(@Nullable NetworkName parent)

Lists Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Company element : companyServiceClient.listCompanies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of [Companies][]. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient.ListCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient.ListCompaniesPagedResponse)` |   
  
### listCompanies(ListCompaniesRequest request)
    
    
    public final CompanyServiceClient.ListCompaniesPagedResponse listCompanies(ListCompaniesRequest request)

Lists Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       ListCompaniesRequest request =
           ListCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Company element : companyServiceClient.listCompanies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCompaniesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient.ListCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient.ListCompaniesPagedResponse)` |   
  
### listCompanies(String parent)
    
    
    public final CompanyServiceClient.ListCompaniesPagedResponse listCompanies(String parent)

Lists Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Company element : companyServiceClient.listCompanies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of [Companies][]. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient.ListCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient.ListCompaniesPagedResponse)` |   
  
### listCompaniesCallable()
    
    
    public final UnaryCallable<ListCompaniesRequest,ListCompaniesResponse> listCompaniesCallable()

Lists Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       ListCompaniesRequest request =
           ListCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCompaniesResponse response = companyServiceClient.listCompaniesCallable().call(request);
         for (Company element : response.getCompaniesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCompaniesRequest),[ListCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCompaniesResponse)>` |   
  
### listCompaniesPagedCallable()
    
    
    public final UnaryCallable<ListCompaniesRequest,CompanyServiceClient.ListCompaniesPagedResponse> listCompaniesPagedCallable()

Lists Company objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       ListCompaniesRequest request =
           ListCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Company> future =
           companyServiceClient.listCompaniesPagedCallable().futureCall(request);
       // Do something.
       for (Company element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCompaniesRequest),[ListCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CompanyServiceClient.ListCompaniesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCompany(Company company, FieldMask updateMask)
    
    
    public final Company updateCompany(Company company, FieldMask updateMask)

Updates a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       Company company = Company.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Company response = companyServiceClient.updateCompany(company, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`company` | `[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)`  
Required. The Company to update. The Company's `name` is used to identify the Company to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)` |   
  
### updateCompany(UpdateCompanyRequest request)
    
    
    public final Company updateCompany(UpdateCompanyRequest request)

Updates a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       UpdateCompanyRequest request =
           UpdateCompanyRequest.newBuilder()
               .setCompany(Company.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Company response = companyServiceClient.updateCompany(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)` |   
  
### updateCompanyCallable()
    
    
    public final UnaryCallable<UpdateCompanyRequest,Company> updateCompanyCallable()

Updates a Company object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       UpdateCompanyRequest request =
           UpdateCompanyRequest.newBuilder()
               .setCompany(Company.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Company> future = companyServiceClient.updateCompanyCallable().futureCall(request);
       // Do something.
       Company response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCompanyRequest),[Company](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Company)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
