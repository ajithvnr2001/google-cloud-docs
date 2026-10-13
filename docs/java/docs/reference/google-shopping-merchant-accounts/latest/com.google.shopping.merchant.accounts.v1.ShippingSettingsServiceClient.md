---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettingsServiceClient
title: Class ShippingSettingsServiceClient (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:58.175164+00:00
---

# Class ShippingSettingsServiceClient (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettingsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ShippingSettingsServiceClient (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-shopping-merchant-accounts/google-shopping-merchant-accounts/src/main/java/com/google/shopping/merchant/accounts/v1/ShippingSettingsServiceClient.java)| [Product Reference](https://developers.google.com/merchant/api)  
---|---  
  
Service Description: Service to get method call shipping setting information per Merchant API method.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create()) {
       ShippingSettingsName name = ShippingSettingsName.of("[ACCOUNT]");
       ShippingSettings response = shippingSettingsServiceClient.getShippingSettings(name);
     }
     

Note: close() needs to be called on the ShippingSettingsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetShippingSettings |  Retrieve shipping setting information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getShippingSettings(GetShippingSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getShippingSettings(ShippingSettingsName name) 
  * getShippingSettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getShippingSettingsCallable() 

  
InsertShippingSettings |  Replace the shipping setting of a business with the request shipping setting. Executing this method requires admin access. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertShippingSettings(InsertShippingSettingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertShippingSettingsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ShippingSettingsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ShippingSettingsServiceSettings shippingSettingsServiceSettings =
         ShippingSettingsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create(shippingSettingsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ShippingSettingsServiceSettings shippingSettingsServiceSettings =
         ShippingSettingsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create(shippingSettingsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ShippingSettingsServiceSettings shippingSettingsServiceSettings =
         ShippingSettingsServiceSettings.newHttpJsonBuilder().build();
     ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create(shippingSettingsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ShippingSettingsServiceClient

## Static Methods 

### create()
    
    
    public static final ShippingSettingsServiceClient create()

Constructs an instance of ShippingSettingsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ShippingSettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettingsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ShippingSettingsServiceSettings settings)
    
    
    public static final ShippingSettingsServiceClient create(ShippingSettingsServiceSettings settings)

Constructs an instance of ShippingSettingsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ShippingSettingsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettingsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ShippingSettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettingsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ShippingSettingsServiceStub stub)
    
    
    public static final ShippingSettingsServiceClient create(ShippingSettingsServiceStub stub)

Constructs an instance of ShippingSettingsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ShippingSettingsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ShippingSettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.stub.ShippingSettingsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ShippingSettingsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettingsServiceClient)` |   
  
## Constructors 

### ShippingSettingsServiceClient(ShippingSettingsServiceSettings settings)
    
    
    protected ShippingSettingsServiceClient(ShippingSettingsServiceSettings settings)

Constructs an instance of ShippingSettingsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ShippingSettingsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettingsServiceSettings)`  
  
  
### ShippingSettingsServiceClient(ShippingSettingsServiceStub stub)
    
    
    protected ShippingSettingsServiceClient(ShippingSettingsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ShippingSettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.stub.ShippingSettingsServiceStub)`  
  
  
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

### getSettings()
    
    
    public final @Nullable ShippingSettingsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.shopping.merchant.accounts.v1.ShippingSettingsServiceSettings` |   
  
### getShippingSettings(@Nullable ShippingSettingsName name)
    
    
    public final ShippingSettings getShippingSettings(@Nullable ShippingSettingsName name)

Retrieve shipping setting information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create()) {
       ShippingSettingsName name = ShippingSettingsName.of("[ACCOUNT]");
       ShippingSettings response = shippingSettingsServiceClient.getShippingSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.shopping.merchant.accounts.v1.ShippingSettingsName`  
Required. The name of the shipping setting to retrieve. Format: `accounts/{account}/shippingsettings`  
**Returns**  
---  
**Type** | **Description**  
`[ShippingSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettings)` |   
  
### getShippingSettings(GetShippingSettingsRequest request)
    
    
    public final ShippingSettings getShippingSettings(GetShippingSettingsRequest request)

Retrieve shipping setting information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create()) {
       GetShippingSettingsRequest request =
           GetShippingSettingsRequest.newBuilder()
               .setName(ShippingSettingsName.of("[ACCOUNT]").toString())
               .build();
       ShippingSettings response = shippingSettingsServiceClient.getShippingSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetShippingSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.GetShippingSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ShippingSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettings)` |   
  
### getShippingSettings(String name)
    
    
    public final ShippingSettings getShippingSettings(String name)

Retrieve shipping setting information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create()) {
       String name = ShippingSettingsName.of("[ACCOUNT]").toString();
       ShippingSettings response = shippingSettingsServiceClient.getShippingSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the shipping setting to retrieve. Format: `accounts/{account}/shippingsettings`  
**Returns**  
---  
**Type** | **Description**  
`[ShippingSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettings)` |   
  
### getShippingSettingsCallable()
    
    
    public final UnaryCallable<GetShippingSettingsRequest,ShippingSettings> getShippingSettingsCallable()

Retrieve shipping setting information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create()) {
       GetShippingSettingsRequest request =
           GetShippingSettingsRequest.newBuilder()
               .setName(ShippingSettingsName.of("[ACCOUNT]").toString())
               .build();
       ApiFuture<ShippingSettings> future =
           shippingSettingsServiceClient.getShippingSettingsCallable().futureCall(request);
       // Do something.
       ShippingSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetShippingSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.GetShippingSettingsRequest),[ShippingSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettings)>` |   
  
### getStub()
    
    
    public ShippingSettingsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ShippingSettingsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.stub.ShippingSettingsServiceStub)` |   
  
### insertShippingSettings(InsertShippingSettingsRequest request)
    
    
    public final ShippingSettings insertShippingSettings(InsertShippingSettingsRequest request)

Replace the shipping setting of a business with the request shipping setting. Executing this method requires admin access.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create()) {
       InsertShippingSettingsRequest request =
           InsertShippingSettingsRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setShippingSetting(ShippingSettings.newBuilder().build())
               .build();
       ShippingSettings response = shippingSettingsServiceClient.insertShippingSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertShippingSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.InsertShippingSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ShippingSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettings)` |   
  
### insertShippingSettingsCallable()
    
    
    public final UnaryCallable<InsertShippingSettingsRequest,ShippingSettings> insertShippingSettingsCallable()

Replace the shipping setting of a business with the request shipping setting. Executing this method requires admin access.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ShippingSettingsServiceClient shippingSettingsServiceClient =
         ShippingSettingsServiceClient.create()) {
       InsertShippingSettingsRequest request =
           InsertShippingSettingsRequest.newBuilder()
               .setParent(AccountName.of("[ACCOUNT]").toString())
               .setShippingSetting(ShippingSettings.newBuilder().build())
               .build();
       ApiFuture<ShippingSettings> future =
           shippingSettingsServiceClient.insertShippingSettingsCallable().futureCall(request);
       // Do something.
       ShippingSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertShippingSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.InsertShippingSettingsRequest),[ShippingSettings](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ShippingSettings)>` |   
  
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
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
