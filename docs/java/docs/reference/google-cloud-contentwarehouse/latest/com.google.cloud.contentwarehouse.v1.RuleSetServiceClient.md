---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient
title: Class RuleSetServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:47.741984+00:00
---

# Class RuleSetServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RuleSetServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-contentwarehouse/google-cloud-contentwarehouse/src/main/java/com/google/cloud/contentwarehouse/v1/RuleSetServiceClient.java)| [Product Reference](https://cloud.google.com/document-warehouse/docs/overview)  
---|---  
  
Service Description: Service to manage customer specific RuleSets.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       RuleSet ruleSet = RuleSet.newBuilder().build();
       RuleSet response = ruleSetServiceClient.createRuleSet(parent, ruleSet);
     }
     

Note: close() needs to be called on the RuleSetServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateRuleSet |  Creates a ruleset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRuleSet(CreateRuleSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createRuleSet(LocationName parent, RuleSet ruleSet) 
  * createRuleSet(String parent, RuleSet ruleSet) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRuleSetCallable() 

  
GetRuleSet |  Gets a ruleset. Returns NOT_FOUND if the ruleset does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRuleSet(GetRuleSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRuleSet(RuleSetName name) 
  * getRuleSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRuleSetCallable() 

  
UpdateRuleSet |  Updates a ruleset. Returns INVALID_ARGUMENT if the name of the ruleset is non-empty and does not equal the existing name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRuleSet(UpdateRuleSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRuleSet(RuleSetName name, RuleSet ruleSet) 
  * updateRuleSet(String name, RuleSet ruleSet) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRuleSetCallable() 

  
DeleteRuleSet |  Deletes a ruleset. Returns NOT_FOUND if the document does not exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRuleSet(DeleteRuleSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteRuleSet(RuleSetName name) 
  * deleteRuleSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRuleSetCallable() 

  
ListRuleSets |  Lists rulesets. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRuleSets(ListRuleSetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRuleSets(LocationName parent) 
  * listRuleSets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRuleSetsPagedCallable() 
  * listRuleSetsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RuleSetServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleSetServiceSettings ruleSetServiceSettings =
         RuleSetServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create(ruleSetServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleSetServiceSettings ruleSetServiceSettings =
         RuleSetServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create(ruleSetServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleSetServiceSettings ruleSetServiceSettings =
         RuleSetServiceSettings.newHttpJsonBuilder().build();
     RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create(ruleSetServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RuleSetServiceClient

## Static Methods 

### create()
    
    
    public static final RuleSetServiceClient create()

Constructs an instance of RuleSetServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RuleSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RuleSetServiceSettings settings)
    
    
    public static final RuleSetServiceClient create(RuleSetServiceSettings settings)

Constructs an instance of RuleSetServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RuleSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuleSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RuleSetServiceStub stub)
    
    
    public static final RuleSetServiceClient create(RuleSetServiceStub stub)

Constructs an instance of RuleSetServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(RuleSetServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RuleSetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.RuleSetServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuleSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient)` |   
  
## Constructors 

### RuleSetServiceClient(RuleSetServiceSettings settings)
    
    
    protected RuleSetServiceClient(RuleSetServiceSettings settings)

Constructs an instance of RuleSetServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RuleSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceSettings)`  
  
  
### RuleSetServiceClient(RuleSetServiceStub stub)
    
    
    protected RuleSetServiceClient(RuleSetServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RuleSetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.RuleSetServiceStub)`  
  
  
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

### createRuleSet(@Nullable LocationName parent, RuleSet ruleSet)
    
    
    public final RuleSet createRuleSet(@Nullable LocationName parent, RuleSet ruleSet)

Creates a ruleset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       RuleSet ruleSet = RuleSet.newBuilder().build();
       RuleSet response = ruleSetServiceClient.createRuleSet(parent, ruleSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.LocationName`  
Required. The parent name. Format: projects/{project_number}/locations/{location}.  
`ruleSet` | `[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)`  
Required. The rule set to create.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### createRuleSet(CreateRuleSetRequest request)
    
    
    public final RuleSet createRuleSet(CreateRuleSetRequest request)

Creates a ruleset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       CreateRuleSetRequest request =
           CreateRuleSetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRuleSet(RuleSet.newBuilder().build())
               .build();
       RuleSet response = ruleSetServiceClient.createRuleSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateRuleSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### createRuleSet(String parent, RuleSet ruleSet)
    
    
    public final RuleSet createRuleSet(String parent, RuleSet ruleSet)

Creates a ruleset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       RuleSet ruleSet = RuleSet.newBuilder().build();
       RuleSet response = ruleSetServiceClient.createRuleSet(parent, ruleSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent name. Format: projects/{project_number}/locations/{location}.  
`ruleSet` | `[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)`  
Required. The rule set to create.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### createRuleSetCallable()
    
    
    public final UnaryCallable<CreateRuleSetRequest,RuleSet> createRuleSetCallable()

Creates a ruleset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       CreateRuleSetRequest request =
           CreateRuleSetRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setRuleSet(RuleSet.newBuilder().build())
               .build();
       ApiFuture<RuleSet> future = ruleSetServiceClient.createRuleSetCallable().futureCall(request);
       // Do something.
       RuleSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateRuleSetRequest),[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)>` |   
  
### deleteRuleSet(@Nullable RuleSetName name)
    
    
    public final void deleteRuleSet(@Nullable RuleSetName name)

Deletes a ruleset. Returns NOT_FOUND if the document does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       RuleSetName name = RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]");
       ruleSetServiceClient.deleteRuleSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.RuleSetName`  
Required. The name of the rule set to delete. Format: projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.  
  
### deleteRuleSet(DeleteRuleSetRequest request)
    
    
    public final void deleteRuleSet(DeleteRuleSetRequest request)

Deletes a ruleset. Returns NOT_FOUND if the document does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       DeleteRuleSetRequest request =
           DeleteRuleSetRequest.newBuilder()
               .setName(RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString())
               .build();
       ruleSetServiceClient.deleteRuleSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteRuleSetRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteRuleSet(String name)
    
    
    public final void deleteRuleSet(String name)

Deletes a ruleset. Returns NOT_FOUND if the document does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       String name = RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString();
       ruleSetServiceClient.deleteRuleSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the rule set to delete. Format: projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.  
  
### deleteRuleSetCallable()
    
    
    public final UnaryCallable<DeleteRuleSetRequest,Empty> deleteRuleSetCallable()

Deletes a ruleset. Returns NOT_FOUND if the document does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       DeleteRuleSetRequest request =
           DeleteRuleSetRequest.newBuilder()
               .setName(RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString())
               .build();
       ApiFuture<Empty> future = ruleSetServiceClient.deleteRuleSetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteRuleSetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getRuleSet(@Nullable RuleSetName name)
    
    
    public final RuleSet getRuleSet(@Nullable RuleSetName name)

Gets a ruleset. Returns NOT_FOUND if the ruleset does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       RuleSetName name = RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]");
       RuleSet response = ruleSetServiceClient.getRuleSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.RuleSetName`  
Required. The name of the rule set to retrieve. Format: projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### getRuleSet(GetRuleSetRequest request)
    
    
    public final RuleSet getRuleSet(GetRuleSetRequest request)

Gets a ruleset. Returns NOT_FOUND if the ruleset does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       GetRuleSetRequest request =
           GetRuleSetRequest.newBuilder()
               .setName(RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString())
               .build();
       RuleSet response = ruleSetServiceClient.getRuleSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetRuleSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### getRuleSet(String name)
    
    
    public final RuleSet getRuleSet(String name)

Gets a ruleset. Returns NOT_FOUND if the ruleset does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       String name = RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString();
       RuleSet response = ruleSetServiceClient.getRuleSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the rule set to retrieve. Format: projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### getRuleSetCallable()
    
    
    public final UnaryCallable<GetRuleSetRequest,RuleSet> getRuleSetCallable()

Gets a ruleset. Returns NOT_FOUND if the ruleset does not exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       GetRuleSetRequest request =
           GetRuleSetRequest.newBuilder()
               .setName(RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString())
               .build();
       ApiFuture<RuleSet> future = ruleSetServiceClient.getRuleSetCallable().futureCall(request);
       // Do something.
       RuleSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetRuleSetRequest),[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)>` |   
  
### getSettings()
    
    
    public final @Nullable RuleSetServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.RuleSetServiceSettings` |   
  
### getStub()
    
    
    public RuleSetServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RuleSetServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.stub.RuleSetServiceStub)` |   
  
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
  
### listRuleSets(@Nullable LocationName parent)
    
    
    public final RuleSetServiceClient.ListRuleSetsPagedResponse listRuleSets(@Nullable LocationName parent)

Lists rulesets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (RuleSet element : ruleSetServiceClient.listRuleSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.LocationName`  
Required. The parent, which owns this collection of document. Format: projects/{project_number}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSetServiceClient.ListRuleSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.ListRuleSetsPagedResponse)` |   
  
### listRuleSets(ListRuleSetsRequest request)
    
    
    public final RuleSetServiceClient.ListRuleSetsPagedResponse listRuleSets(ListRuleSetsRequest request)

Lists rulesets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       ListRuleSetsRequest request =
           ListRuleSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (RuleSet element : ruleSetServiceClient.listRuleSets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRuleSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSetServiceClient.ListRuleSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.ListRuleSetsPagedResponse)` |   
  
### listRuleSets(String parent)
    
    
    public final RuleSetServiceClient.ListRuleSetsPagedResponse listRuleSets(String parent)

Lists rulesets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (RuleSet element : ruleSetServiceClient.listRuleSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of document. Format: projects/{project_number}/locations/{location}.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSetServiceClient.ListRuleSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.ListRuleSetsPagedResponse)` |   
  
### listRuleSetsCallable()
    
    
    public final UnaryCallable<ListRuleSetsRequest,ListRuleSetsResponse> listRuleSetsCallable()

Lists rulesets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       ListRuleSetsRequest request =
           ListRuleSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListRuleSetsResponse response = ruleSetServiceClient.listRuleSetsCallable().call(request);
         for (RuleSet element : response.getRuleSetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRuleSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsRequest),[ListRuleSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsResponse)>` |   
  
### listRuleSetsPagedCallable()
    
    
    public final UnaryCallable<ListRuleSetsRequest,RuleSetServiceClient.ListRuleSetsPagedResponse> listRuleSetsPagedCallable()

Lists rulesets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       ListRuleSetsRequest request =
           ListRuleSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<RuleSet> future =
           ruleSetServiceClient.listRuleSetsPagedCallable().futureCall(request);
       // Do something.
       for (RuleSet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRuleSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsRequest),[ListRuleSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.ListRuleSetsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateRuleSet(@Nullable RuleSetName name, RuleSet ruleSet)
    
    
    public final RuleSet updateRuleSet(@Nullable RuleSetName name, RuleSet ruleSet)

Updates a ruleset. Returns INVALID_ARGUMENT if the name of the ruleset is non-empty and does not equal the existing name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       RuleSetName name = RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]");
       RuleSet ruleSet = RuleSet.newBuilder().build();
       RuleSet response = ruleSetServiceClient.updateRuleSet(name, ruleSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.contentwarehouse.v1.RuleSetName`  
Required. The name of the rule set to update. Format: projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.  
`ruleSet` | `[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)`  
Required. The rule set to update.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### updateRuleSet(UpdateRuleSetRequest request)
    
    
    public final RuleSet updateRuleSet(UpdateRuleSetRequest request)

Updates a ruleset. Returns INVALID_ARGUMENT if the name of the ruleset is non-empty and does not equal the existing name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       UpdateRuleSetRequest request =
           UpdateRuleSetRequest.newBuilder()
               .setName(RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString())
               .setRuleSet(RuleSet.newBuilder().build())
               .build();
       RuleSet response = ruleSetServiceClient.updateRuleSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateRuleSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### updateRuleSet(String name, RuleSet ruleSet)
    
    
    public final RuleSet updateRuleSet(String name, RuleSet ruleSet)

Updates a ruleset. Returns INVALID_ARGUMENT if the name of the ruleset is non-empty and does not equal the existing name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       String name = RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString();
       RuleSet ruleSet = RuleSet.newBuilder().build();
       RuleSet response = ruleSetServiceClient.updateRuleSet(name, ruleSet);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the rule set to update. Format: projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.  
`ruleSet` | `[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)`  
Required. The rule set to update.  
**Returns**  
---  
**Type** | **Description**  
`[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)` |   
  
### updateRuleSetCallable()
    
    
    public final UnaryCallable<UpdateRuleSetRequest,RuleSet> updateRuleSetCallable()

Updates a ruleset. Returns INVALID_ARGUMENT if the name of the ruleset is non-empty and does not equal the existing name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleSetServiceClient ruleSetServiceClient = RuleSetServiceClient.create()) {
       UpdateRuleSetRequest request =
           UpdateRuleSetRequest.newBuilder()
               .setName(RuleSetName.of("[PROJECT]", "[LOCATION]", "[RULE_SET]").toString())
               .setRuleSet(RuleSet.newBuilder().build())
               .build();
       ApiFuture<RuleSet> future = ruleSetServiceClient.updateRuleSetCallable().futureCall(request);
       // Do something.
       RuleSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateRuleSetRequest),[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
