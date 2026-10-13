---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient
title: Class CompanyServiceClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:41:54.260706+00:00
---

# Class CompanyServiceClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CompanyServiceClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.6  2.2.9 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-talent/google-cloud-talent/src/main/java/com/google/cloud/talent/v4/CompanyServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/talent-solution/)  
---|---  
  
Service Description: A service that handles company management, including CRUD and enumeration.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       TenantName parent = TenantName.of("[PROJECT]", "[TENANT]");
       Company company = Company.newBuilder().build();
       Company response = companyServiceClient.createCompany(parent, company);
     }
     

Note: close() needs to be called on the CompanyServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateCompany |  Creates a new company entity. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCompany(CreateCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCompany(TenantName parent, Company company) 
  * createCompany(String parent, Company company) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCompanyCallable() 

  
GetCompany |  Retrieves specified company. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCompany(GetCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCompany(CompanyName name) 
  * getCompany(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCompanyCallable() 

  
UpdateCompany |  Updates specified company. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCompany(UpdateCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCompany(Company company, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCompanyCallable() 

  
DeleteCompany |  Deletes specified company. Prerequisite: The company has no jobs associated with it. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCompany(DeleteCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteCompany(CompanyName name) 
  * deleteCompany(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCompanyCallable() 

  
ListCompanies |  Lists all companies associated with the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCompanies(ListCompaniesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCompanies(TenantName parent) 
  * listCompanies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCompaniesPagedCallable() 
  * listCompaniesCallable() 

  
  
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
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompanyServiceSettings companyServiceSettings =
         CompanyServiceSettings.newHttpJsonBuilder().build();
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
`[CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient)` |   
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
`settings` | `[CompanyServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient)` |   
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
`stub` | `[CompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.CompanyServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient)` |   
  
## Constructors 

### CompanyServiceClient(CompanyServiceSettings settings)
    
    
    protected CompanyServiceClient(CompanyServiceSettings settings)

Constructs an instance of CompanyServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompanyServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceSettings)`  
  
  
### CompanyServiceClient(CompanyServiceStub stub)
    
    
    protected CompanyServiceClient(CompanyServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.CompanyServiceStub)`  
  
  
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

### createCompany(@Nullable TenantName parent, Company company)
    
    
    public final Company createCompany(@Nullable TenantName parent, Company company)

Creates a new company entity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       TenantName parent = TenantName.of("[PROJECT]", "[TENANT]");
       Company company = Company.newBuilder().build();
       Company response = companyServiceClient.createCompany(parent, company);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.talent.v4.TenantName`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`company` | `[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)`  
Required. The company to be created.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)` |   
  
### createCompany(CreateCompanyRequest request)
    
    
    public final Company createCompany(CreateCompanyRequest request)

Creates a new company entity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       CreateCompanyRequest request =
           CreateCompanyRequest.newBuilder()
               .setParent(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setCompany(Company.newBuilder().build())
               .build();
       Company response = companyServiceClient.createCompany(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)` |   
  
### createCompany(String parent, Company company)
    
    
    public final Company createCompany(String parent, Company company)

Creates a new company entity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String parent = TenantName.of("[PROJECT]", "[TENANT]").toString();
       Company company = Company.newBuilder().build();
       Company response = companyServiceClient.createCompany(parent, company);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
`company` | `[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)`  
Required. The company to be created.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)` |   
  
### createCompanyCallable()
    
    
    public final UnaryCallable<CreateCompanyRequest,Company> createCompanyCallable()

Creates a new company entity.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       CreateCompanyRequest request =
           CreateCompanyRequest.newBuilder()
               .setParent(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setCompany(Company.newBuilder().build())
               .build();
       ApiFuture<Company> future = companyServiceClient.createCompanyCallable().futureCall(request);
       // Do something.
       Company response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateCompanyRequest),[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)>` |   
  
### deleteCompany(@Nullable CompanyName name)
    
    
    public final void deleteCompany(@Nullable CompanyName name)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       CompanyName name = CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]");
       companyServiceClient.deleteCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.talent.v4.CompanyName`  
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".  
  
### deleteCompany(DeleteCompanyRequest request)
    
    
    public final void deleteCompany(DeleteCompanyRequest request)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       DeleteCompanyRequest request =
           DeleteCompanyRequest.newBuilder()
               .setName(CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString())
               .build();
       companyServiceClient.deleteCompany(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.DeleteCompanyRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteCompany(String name)
    
    
    public final void deleteCompany(String name)

Deletes specified company. Prerequisite: The company has no jobs associated with it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String name = CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString();
       companyServiceClient.deleteCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz".  
  
### deleteCompanyCallable()
    
    
    public final UnaryCallable<DeleteCompanyRequest,Empty> deleteCompanyCallable()

Deletes specified company. Prerequisite: The company has no jobs associated with it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       DeleteCompanyRequest request =
           DeleteCompanyRequest.newBuilder()
               .setName(CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString())
               .build();
       ApiFuture<Empty> future = companyServiceClient.deleteCompanyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.DeleteCompanyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCompany(@Nullable CompanyName name)
    
    
    public final Company getCompany(@Nullable CompanyName name)

Retrieves specified company.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       CompanyName name = CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]");
       Company response = companyServiceClient.getCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.talent.v4.CompanyName`  
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar".  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)` |   
  
### getCompany(GetCompanyRequest request)
    
    
    public final Company getCompany(GetCompanyRequest request)

Retrieves specified company.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       GetCompanyRequest request =
           GetCompanyRequest.newBuilder()
               .setName(CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString())
               .build();
       Company response = companyServiceClient.getCompany(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.GetCompanyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)` |   
  
### getCompany(String name)
    
    
    public final Company getCompany(String name)

Retrieves specified company.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String name = CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString();
       Company response = companyServiceClient.getCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar".  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)` |   
  
### getCompanyCallable()
    
    
    public final UnaryCallable<GetCompanyRequest,Company> getCompanyCallable()

Retrieves specified company.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       GetCompanyRequest request =
           GetCompanyRequest.newBuilder()
               .setName(CompanyName.of("[PROJECT]", "[TENANT]", "[COMPANY]").toString())
               .build();
       ApiFuture<Company> future = companyServiceClient.getCompanyCallable().futureCall(request);
       // Do something.
       Company response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.GetCompanyRequest),[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)>` |   
  
### getSettings()
    
    
    public final @Nullable CompanyServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.talent.v4.CompanyServiceSettings` |   
  
### getStub()
    
    
    public CompanyServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.stub.CompanyServiceStub)` |   
  
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
  
### listCompanies(@Nullable TenantName parent)
    
    
    public final CompanyServiceClient.ListCompaniesPagedResponse listCompanies(@Nullable TenantName parent)

Lists all companies associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       TenantName parent = TenantName.of("[PROJECT]", "[TENANT]");
       for (Company element : companyServiceClient.listCompanies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.talent.v4.TenantName`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient.ListCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient.ListCompaniesPagedResponse)` |   
  
### listCompanies(ListCompaniesRequest request)
    
    
    public final CompanyServiceClient.ListCompaniesPagedResponse listCompanies(ListCompaniesRequest request)

Lists all companies associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       ListCompaniesRequest request =
           ListCompaniesRequest.newBuilder()
               .setParent(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .setRequireOpenJobs(true)
               .build();
       for (Company element : companyServiceClient.listCompanies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ListCompaniesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient.ListCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient.ListCompaniesPagedResponse)` |   
  
### listCompanies(String parent)
    
    
    public final CompanyServiceClient.ListCompaniesPagedResponse listCompanies(String parent)

Lists all companies associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       String parent = TenantName.of("[PROJECT]", "[TENANT]").toString();
       for (Company element : companyServiceClient.listCompanies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar".  
**Returns**  
---  
**Type** | **Description**  
`[CompanyServiceClient.ListCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient.ListCompaniesPagedResponse)` |   
  
### listCompaniesCallable()
    
    
    public final UnaryCallable<ListCompaniesRequest,ListCompaniesResponse> listCompaniesCallable()

Lists all companies associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       ListCompaniesRequest request =
           ListCompaniesRequest.newBuilder()
               .setParent(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .setRequireOpenJobs(true)
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ListCompaniesRequest),[ListCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ListCompaniesResponse)>` |   
  
### listCompaniesPagedCallable()
    
    
    public final UnaryCallable<ListCompaniesRequest,CompanyServiceClient.ListCompaniesPagedResponse> listCompaniesPagedCallable()

Lists all companies associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
       ListCompaniesRequest request =
           ListCompaniesRequest.newBuilder()
               .setParent(TenantName.of("[PROJECT]", "[TENANT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .setRequireOpenJobs(true)
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.ListCompaniesRequest),[ListCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient.ListCompaniesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCompany(Company company, FieldMask updateMask)
    
    
    public final Company updateCompany(Company company, FieldMask updateMask)

Updates specified company.

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
`company` | `[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)`  
Required. The company resource to replace the current resource in the system.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Strongly recommended for the best service experience. If update_mask is provided, only the specified fields in company are updated. Otherwise all the fields are updated. A field mask to specify the company fields to be updated. Only top level fields of Company are supported.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)` |   
  
### updateCompany(UpdateCompanyRequest request)
    
    
    public final Company updateCompany(UpdateCompanyRequest request)

Updates specified company.

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
`request` | `[UpdateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.UpdateCompanyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)` |   
  
### updateCompanyCallable()
    
    
    public final UnaryCallable<UpdateCompanyRequest,Company> updateCompanyCallable()

Updates specified company.

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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.UpdateCompanyRequest),[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
