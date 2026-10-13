---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient
title: Class RuleServiceClient (0.37.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:38.868211+00:00
---

# Class RuleServiceClient (0.37.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RuleServiceClient (0.37.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.0 (latest)  0.33.0  0.32.0  0.31.0  0.29.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-chronicle/google-cloud-chronicle/src/main/java/com/google/cloud/chronicle/v1/RuleServiceClient.java)| [Product Reference](https://cloud.google.com/chronicle/docs/secops/secops-overview)  
---|---  
  
Service Description: RuleService provides interface for user-created rules.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       Rule rule = Rule.newBuilder().build();
       Rule response = ruleServiceClient.createRule(parent, rule);
     }
     

Note: close() needs to be called on the RuleServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateRule |  Creates a new Rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRule(CreateRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createRule(InstanceName parent, Rule rule) 
  * createRule(String parent, Rule rule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRuleCallable() 

  
GetRule |  Gets a Rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRule(GetRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRule(RuleName name) 
  * getRule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRuleCallable() 

  
ListRules |  Lists Rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRules(ListRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRules(InstanceName parent) 
  * listRules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRulesPagedCallable() 
  * listRulesCallable() 

  
UpdateRule |  Updates a Rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRule(UpdateRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRule(Rule rule, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRuleCallable() 

  
DeleteRule |  Deletes a Rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRule(DeleteRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteRule(RuleName name) 
  * deleteRule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRuleCallable() 

  
VerifyRuleText |  Verifies the given rule text. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * verifyRuleText(VerifyRuleTextRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * verifyRuleText(InstanceName instance, String ruleText) 
  * verifyRuleText(String instance, String ruleText) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * verifyRuleTextCallable() 

  
ListRuleRevisions |  Lists all revisions of the rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRuleRevisions(ListRuleRevisionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRuleRevisions(RuleName name) 
  * listRuleRevisions(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRuleRevisionsPagedCallable() 
  * listRuleRevisionsCallable() 

  
CreateRetrohunt |  Create a Retrohunt. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRetrohuntAsync(CreateRetrohuntRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createRetrohuntAsync(RuleName parent, Retrohunt retrohunt) 
  * createRetrohuntAsync(String parent, Retrohunt retrohunt) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRetrohuntOperationCallable() 
  * createRetrohuntCallable() 

  
GetRetrohunt |  Get a Retrohunt. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRetrohunt(GetRetrohuntRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRetrohunt(RetrohuntName name) 
  * getRetrohunt(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRetrohuntCallable() 

  
ListRetrohunts |  List Retrohunts. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRetrohunts(ListRetrohuntsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRetrohunts(RuleName parent) 
  * listRetrohunts(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRetrohuntsPagedCallable() 
  * listRetrohuntsCallable() 

  
GetRuleDeployment |  Gets a RuleDeployment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRuleDeployment(GetRuleDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRuleDeployment(RuleDeploymentName name) 
  * getRuleDeployment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRuleDeploymentCallable() 

  
ListRuleDeployments |  Lists RuleDeployments across all Rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRuleDeployments(ListRuleDeploymentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRuleDeployments(RuleName parent) 
  * listRuleDeployments(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRuleDeploymentsPagedCallable() 
  * listRuleDeploymentsCallable() 

  
UpdateRuleDeployment |  Updates a RuleDeployment. Failures are not necessarily atomic. If there is a request to update multiple fields, and any update to a single field fails, an error will be returned, but other fields may remain successfully updated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRuleDeployment(UpdateRuleDeploymentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateRuleDeployment(RuleDeployment ruleDeployment, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRuleDeploymentCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RuleServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleServiceSettings ruleServiceSettings =
         RuleServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RuleServiceClient ruleServiceClient = RuleServiceClient.create(ruleServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleServiceSettings ruleServiceSettings =
         RuleServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     RuleServiceClient ruleServiceClient = RuleServiceClient.create(ruleServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RuleServiceSettings ruleServiceSettings = RuleServiceSettings.newHttpJsonBuilder().build();
     RuleServiceClient ruleServiceClient = RuleServiceClient.create(ruleServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RuleServiceClient

## Static Methods 

### create()
    
    
    public static final RuleServiceClient create()

Constructs an instance of RuleServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RuleServiceSettings settings)
    
    
    public static final RuleServiceClient create(RuleServiceSettings settings)

Constructs an instance of RuleServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RuleServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RuleServiceStub stub)
    
    
    public static final RuleServiceClient create(RuleServiceStub stub)

Constructs an instance of RuleServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(RuleServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RuleServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.stub.RuleServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient)` |   
  
## Constructors 

### RuleServiceClient(RuleServiceSettings settings)
    
    
    protected RuleServiceClient(RuleServiceSettings settings)

Constructs an instance of RuleServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RuleServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceSettings)`  
  
  
### RuleServiceClient(RuleServiceStub stub)
    
    
    protected RuleServiceClient(RuleServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RuleServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.stub.RuleServiceStub)`  
  
  
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

### createRetrohuntAsync(@Nullable RuleName parent, Retrohunt retrohunt)
    
    
    public final OperationFuture<Retrohunt,RetrohuntMetadata> createRetrohuntAsync(@Nullable RuleName parent, Retrohunt retrohunt)

Create a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RuleName parent = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]");
       Retrohunt retrohunt = Retrohunt.newBuilder().build();
       Retrohunt response = ruleServiceClient.createRetrohuntAsync(parent, retrohunt).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleName`  
Required. The parent of retrohunt, which is a rule. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
`retrohunt` | `[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt)`  
Required. The retrohunt to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt),[RetrohuntMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RetrohuntMetadata)>` |   
  
### createRetrohuntAsync(CreateRetrohuntRequest request)
    
    
    public final OperationFuture<Retrohunt,RetrohuntMetadata> createRetrohuntAsync(CreateRetrohuntRequest request)

Create a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       CreateRetrohuntRequest request =
           CreateRetrohuntRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setRetrohunt(Retrohunt.newBuilder().build())
               .build();
       Retrohunt response = ruleServiceClient.createRetrohuntAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRetrohuntRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.CreateRetrohuntRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt),[RetrohuntMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RetrohuntMetadata)>` |   
  
### createRetrohuntAsync(String parent, Retrohunt retrohunt)
    
    
    public final OperationFuture<Retrohunt,RetrohuntMetadata> createRetrohuntAsync(String parent, Retrohunt retrohunt)

Create a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String parent = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString();
       Retrohunt retrohunt = Retrohunt.newBuilder().build();
       Retrohunt response = ruleServiceClient.createRetrohuntAsync(parent, retrohunt).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of retrohunt, which is a rule. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
`retrohunt` | `[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt)`  
Required. The retrohunt to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt),[RetrohuntMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RetrohuntMetadata)>` |   
  
### createRetrohuntCallable()
    
    
    public final UnaryCallable<CreateRetrohuntRequest,Operation> createRetrohuntCallable()

Create a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       CreateRetrohuntRequest request =
           CreateRetrohuntRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setRetrohunt(Retrohunt.newBuilder().build())
               .build();
       ApiFuture<Operation> future = ruleServiceClient.createRetrohuntCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRetrohuntRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.CreateRetrohuntRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRetrohuntOperationCallable()
    
    
    public final OperationCallable<CreateRetrohuntRequest,Retrohunt,RetrohuntMetadata> createRetrohuntOperationCallable()

Create a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       CreateRetrohuntRequest request =
           CreateRetrohuntRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setRetrohunt(Retrohunt.newBuilder().build())
               .build();
       OperationFuture<Retrohunt, RetrohuntMetadata> future =
           ruleServiceClient.createRetrohuntOperationCallable().futureCall(request);
       // Do something.
       Retrohunt response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateRetrohuntRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.CreateRetrohuntRequest),[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt),[RetrohuntMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RetrohuntMetadata)>` |   
  
### createRule(@Nullable InstanceName parent, Rule rule)
    
    
    public final Rule createRule(@Nullable InstanceName parent, Rule rule)

Creates a new Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       Rule rule = Rule.newBuilder().build();
       Rule response = ruleServiceClient.createRule(parent, rule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.InstanceName`  
Required. The parent resource where this rule will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`rule` | `[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)`  
Required. The rule to create.  
**Returns**  
---  
**Type** | **Description**  
`[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)` |   
  
### createRule(CreateRuleRequest request)
    
    
    public final Rule createRule(CreateRuleRequest request)

Creates a new Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       CreateRuleRequest request =
           CreateRuleRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRule(Rule.newBuilder().build())
               .build();
       Rule response = ruleServiceClient.createRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.CreateRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)` |   
  
### createRule(String parent, Rule rule)
    
    
    public final Rule createRule(String parent, Rule rule)

Creates a new Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       Rule rule = Rule.newBuilder().build();
       Rule response = ruleServiceClient.createRule(parent, rule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this rule will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`rule` | `[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)`  
Required. The rule to create.  
**Returns**  
---  
**Type** | **Description**  
`[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)` |   
  
### createRuleCallable()
    
    
    public final UnaryCallable<CreateRuleRequest,Rule> createRuleCallable()

Creates a new Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       CreateRuleRequest request =
           CreateRuleRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRule(Rule.newBuilder().build())
               .build();
       ApiFuture<Rule> future = ruleServiceClient.createRuleCallable().futureCall(request);
       // Do something.
       Rule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.CreateRuleRequest),[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)>` |   
  
### deleteRule(@Nullable RuleName name)
    
    
    public final void deleteRule(@Nullable RuleName name)

Deletes a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RuleName name = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]");
       ruleServiceClient.deleteRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleName`  
Required. The name of the rule to delete. A rule revision timestamp cannot be specified as part of the name, as deleting specific revisions is not supported. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
  
### deleteRule(DeleteRuleRequest request)
    
    
    public final void deleteRule(DeleteRuleRequest request)

Deletes a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       DeleteRuleRequest request =
           DeleteRuleRequest.newBuilder()
               .setName(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setForce(true)
               .build();
       ruleServiceClient.deleteRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DeleteRuleRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteRule(String name)
    
    
    public final void deleteRule(String name)

Deletes a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String name = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString();
       ruleServiceClient.deleteRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the rule to delete. A rule revision timestamp cannot be specified as part of the name, as deleting specific revisions is not supported. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
  
### deleteRuleCallable()
    
    
    public final UnaryCallable<DeleteRuleRequest,Empty> deleteRuleCallable()

Deletes a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       DeleteRuleRequest request =
           DeleteRuleRequest.newBuilder()
               .setName(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future = ruleServiceClient.deleteRuleCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.DeleteRuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getRetrohunt(@Nullable RetrohuntName name)
    
    
    public final Retrohunt getRetrohunt(@Nullable RetrohuntName name)

Get a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RetrohuntName name =
           RetrohuntName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]", "[RETROHUNT]");
       Retrohunt response = ruleServiceClient.getRetrohunt(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RetrohuntName`  
Required. The name of the retrohunt to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/retrohunts/{retrohunt}`  
**Returns**  
---  
**Type** | **Description**  
`[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt)` |   
  
### getRetrohunt(GetRetrohuntRequest request)
    
    
    public final Retrohunt getRetrohunt(GetRetrohuntRequest request)

Get a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       GetRetrohuntRequest request =
           GetRetrohuntRequest.newBuilder()
               .setName(
                   RetrohuntName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]", "[RETROHUNT]")
                       .toString())
               .build();
       Retrohunt response = ruleServiceClient.getRetrohunt(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRetrohuntRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.GetRetrohuntRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt)` |   
  
### getRetrohunt(String name)
    
    
    public final Retrohunt getRetrohunt(String name)

Get a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String name =
           RetrohuntName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]", "[RETROHUNT]")
               .toString();
       Retrohunt response = ruleServiceClient.getRetrohunt(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the retrohunt to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/retrohunts/{retrohunt}`  
**Returns**  
---  
**Type** | **Description**  
`[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt)` |   
  
### getRetrohuntCallable()
    
    
    public final UnaryCallable<GetRetrohuntRequest,Retrohunt> getRetrohuntCallable()

Get a Retrohunt.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       GetRetrohuntRequest request =
           GetRetrohuntRequest.newBuilder()
               .setName(
                   RetrohuntName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]", "[RETROHUNT]")
                       .toString())
               .build();
       ApiFuture<Retrohunt> future = ruleServiceClient.getRetrohuntCallable().futureCall(request);
       // Do something.
       Retrohunt response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRetrohuntRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.GetRetrohuntRequest),[Retrohunt](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Retrohunt)>` |   
  
### getRule(@Nullable RuleName name)
    
    
    public final Rule getRule(@Nullable RuleName name)

Gets a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RuleName name = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]");
       Rule response = ruleServiceClient.getRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleName`  
Required. The name of the rule to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
**Returns**  
---  
**Type** | **Description**  
`[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)` |   
  
### getRule(GetRuleRequest request)
    
    
    public final Rule getRule(GetRuleRequest request)

Gets a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       GetRuleRequest request =
           GetRuleRequest.newBuilder()
               .setName(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setView(RuleView.forNumber(0))
               .build();
       Rule response = ruleServiceClient.getRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.GetRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)` |   
  
### getRule(String name)
    
    
    public final Rule getRule(String name)

Gets a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String name = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString();
       Rule response = ruleServiceClient.getRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the rule to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
**Returns**  
---  
**Type** | **Description**  
`[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)` |   
  
### getRuleCallable()
    
    
    public final UnaryCallable<GetRuleRequest,Rule> getRuleCallable()

Gets a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       GetRuleRequest request =
           GetRuleRequest.newBuilder()
               .setName(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setView(RuleView.forNumber(0))
               .build();
       ApiFuture<Rule> future = ruleServiceClient.getRuleCallable().futureCall(request);
       // Do something.
       Rule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.GetRuleRequest),[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)>` |   
  
### getRuleDeployment(@Nullable RuleDeploymentName name)
    
    
    public final RuleDeployment getRuleDeployment(@Nullable RuleDeploymentName name)

Gets a RuleDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RuleDeploymentName name =
           RuleDeploymentName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]");
       RuleDeployment response = ruleServiceClient.getRuleDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleDeploymentName`  
Required. The name of the rule deployment to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/deployment`  
**Returns**  
---  
**Type** | **Description**  
`[RuleDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleDeployment)` |   
  
### getRuleDeployment(GetRuleDeploymentRequest request)
    
    
    public final RuleDeployment getRuleDeployment(GetRuleDeploymentRequest request)

Gets a RuleDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       GetRuleDeploymentRequest request =
           GetRuleDeploymentRequest.newBuilder()
               .setName(
                   RuleDeploymentName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]")
                       .toString())
               .build();
       RuleDeployment response = ruleServiceClient.getRuleDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRuleDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.GetRuleDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleDeployment)` |   
  
### getRuleDeployment(String name)
    
    
    public final RuleDeployment getRuleDeployment(String name)

Gets a RuleDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String name =
           RuleDeploymentName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString();
       RuleDeployment response = ruleServiceClient.getRuleDeployment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the rule deployment to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/deployment`  
**Returns**  
---  
**Type** | **Description**  
`[RuleDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleDeployment)` |   
  
### getRuleDeploymentCallable()
    
    
    public final UnaryCallable<GetRuleDeploymentRequest,RuleDeployment> getRuleDeploymentCallable()

Gets a RuleDeployment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       GetRuleDeploymentRequest request =
           GetRuleDeploymentRequest.newBuilder()
               .setName(
                   RuleDeploymentName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]")
                       .toString())
               .build();
       ApiFuture<RuleDeployment> future =
           ruleServiceClient.getRuleDeploymentCallable().futureCall(request);
       // Do something.
       RuleDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRuleDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.GetRuleDeploymentRequest),[RuleDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleDeployment)>` |   
  
### getSettings()
    
    
    public final @Nullable RuleServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleServiceSettings` |   
  
### getStub()
    
    
    public RuleServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RuleServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.stub.RuleServiceStub)` |   
  
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
  
### listRetrohunts(@Nullable RuleName parent)
    
    
    public final RuleServiceClient.ListRetrohuntsPagedResponse listRetrohunts(@Nullable RuleName parent)

List Retrohunts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RuleName parent = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]");
       for (Retrohunt element : ruleServiceClient.listRetrohunts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleName`  
Required. The rule that the retrohunts belong to. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRetrohuntsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRetrohuntsPagedResponse)` |   
  
### listRetrohunts(ListRetrohuntsRequest request)
    
    
    public final RuleServiceClient.ListRetrohuntsPagedResponse listRetrohunts(ListRetrohuntsRequest request)

List Retrohunts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRetrohuntsRequest request =
           ListRetrohuntsRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Retrohunt element : ruleServiceClient.listRetrohunts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRetrohuntsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRetrohuntsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRetrohuntsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRetrohuntsPagedResponse)` |   
  
### listRetrohunts(String parent)
    
    
    public final RuleServiceClient.ListRetrohuntsPagedResponse listRetrohunts(String parent)

List Retrohunts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String parent = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString();
       for (Retrohunt element : ruleServiceClient.listRetrohunts(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The rule that the retrohunts belong to. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRetrohuntsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRetrohuntsPagedResponse)` |   
  
### listRetrohuntsCallable()
    
    
    public final UnaryCallable<ListRetrohuntsRequest,ListRetrohuntsResponse> listRetrohuntsCallable()

List Retrohunts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRetrohuntsRequest request =
           ListRetrohuntsRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListRetrohuntsResponse response = ruleServiceClient.listRetrohuntsCallable().call(request);
         for (Retrohunt element : response.getRetrohuntsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRetrohuntsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRetrohuntsRequest),[ListRetrohuntsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRetrohuntsResponse)>` |   
  
### listRetrohuntsPagedCallable()
    
    
    public final UnaryCallable<ListRetrohuntsRequest,RuleServiceClient.ListRetrohuntsPagedResponse> listRetrohuntsPagedCallable()

List Retrohunts.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRetrohuntsRequest request =
           ListRetrohuntsRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Retrohunt> future =
           ruleServiceClient.listRetrohuntsPagedCallable().futureCall(request);
       // Do something.
       for (Retrohunt element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRetrohuntsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRetrohuntsRequest),[ListRetrohuntsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRetrohuntsPagedResponse)>` |   
  
### listRuleDeployments(@Nullable RuleName parent)
    
    
    public final RuleServiceClient.ListRuleDeploymentsPagedResponse listRuleDeployments(@Nullable RuleName parent)

Lists RuleDeployments across all Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RuleName parent = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]");
       for (RuleDeployment element : ruleServiceClient.listRuleDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleName`  
Required. The collection of all parents which own all rule deployments. The "-" wildcard token must be used as the rule identifier in the resource path. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/-`  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRuleDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRuleDeploymentsPagedResponse)` |   
  
### listRuleDeployments(ListRuleDeploymentsRequest request)
    
    
    public final RuleServiceClient.ListRuleDeploymentsPagedResponse listRuleDeployments(ListRuleDeploymentsRequest request)

Lists RuleDeployments across all Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRuleDeploymentsRequest request =
           ListRuleDeploymentsRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (RuleDeployment element : ruleServiceClient.listRuleDeployments(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRuleDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleDeploymentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRuleDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRuleDeploymentsPagedResponse)` |   
  
### listRuleDeployments(String parent)
    
    
    public final RuleServiceClient.ListRuleDeploymentsPagedResponse listRuleDeployments(String parent)

Lists RuleDeployments across all Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String parent = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString();
       for (RuleDeployment element : ruleServiceClient.listRuleDeployments(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The collection of all parents which own all rule deployments. The "-" wildcard token must be used as the rule identifier in the resource path. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/-`  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRuleDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRuleDeploymentsPagedResponse)` |   
  
### listRuleDeploymentsCallable()
    
    
    public final UnaryCallable<ListRuleDeploymentsRequest,ListRuleDeploymentsResponse> listRuleDeploymentsCallable()

Lists RuleDeployments across all Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRuleDeploymentsRequest request =
           ListRuleDeploymentsRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListRuleDeploymentsResponse response =
             ruleServiceClient.listRuleDeploymentsCallable().call(request);
         for (RuleDeployment element : response.getRuleDeploymentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRuleDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleDeploymentsRequest),[ListRuleDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleDeploymentsResponse)>` |   
  
### listRuleDeploymentsPagedCallable()
    
    
    public final UnaryCallable<ListRuleDeploymentsRequest,RuleServiceClient.ListRuleDeploymentsPagedResponse> listRuleDeploymentsPagedCallable()

Lists RuleDeployments across all Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRuleDeploymentsRequest request =
           ListRuleDeploymentsRequest.newBuilder()
               .setParent(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<RuleDeployment> future =
           ruleServiceClient.listRuleDeploymentsPagedCallable().futureCall(request);
       // Do something.
       for (RuleDeployment element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRuleDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleDeploymentsRequest),[ListRuleDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRuleDeploymentsPagedResponse)>` |   
  
### listRuleRevisions(@Nullable RuleName name)
    
    
    public final RuleServiceClient.ListRuleRevisionsPagedResponse listRuleRevisions(@Nullable RuleName name)

Lists all revisions of the rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RuleName name = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]");
       for (Rule element : ruleServiceClient.listRuleRevisions(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.RuleName`  
Required. The name of the rule to list revisions for. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRuleRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRuleRevisionsPagedResponse)` |   
  
### listRuleRevisions(ListRuleRevisionsRequest request)
    
    
    public final RuleServiceClient.ListRuleRevisionsPagedResponse listRuleRevisions(ListRuleRevisionsRequest request)

Lists all revisions of the rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRuleRevisionsRequest request =
           ListRuleRevisionsRequest.newBuilder()
               .setName(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(RuleView.forNumber(0))
               .build();
       for (Rule element : ruleServiceClient.listRuleRevisions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRuleRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRuleRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRuleRevisionsPagedResponse)` |   
  
### listRuleRevisions(String name)
    
    
    public final RuleServiceClient.ListRuleRevisionsPagedResponse listRuleRevisions(String name)

Lists all revisions of the rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String name = RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString();
       for (Rule element : ruleServiceClient.listRuleRevisions(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the rule to list revisions for. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRuleRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRuleRevisionsPagedResponse)` |   
  
### listRuleRevisionsCallable()
    
    
    public final UnaryCallable<ListRuleRevisionsRequest,ListRuleRevisionsResponse> listRuleRevisionsCallable()

Lists all revisions of the rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRuleRevisionsRequest request =
           ListRuleRevisionsRequest.newBuilder()
               .setName(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(RuleView.forNumber(0))
               .build();
       while (true) {
         ListRuleRevisionsResponse response =
             ruleServiceClient.listRuleRevisionsCallable().call(request);
         for (Rule element : response.getRulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRuleRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleRevisionsRequest),[ListRuleRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleRevisionsResponse)>` |   
  
### listRuleRevisionsPagedCallable()
    
    
    public final UnaryCallable<ListRuleRevisionsRequest,RuleServiceClient.ListRuleRevisionsPagedResponse> listRuleRevisionsPagedCallable()

Lists all revisions of the rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRuleRevisionsRequest request =
           ListRuleRevisionsRequest.newBuilder()
               .setName(RuleName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[RULE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(RuleView.forNumber(0))
               .build();
       ApiFuture<Rule> future =
           ruleServiceClient.listRuleRevisionsPagedCallable().futureCall(request);
       // Do something.
       for (Rule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRuleRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRuleRevisionsRequest),[ListRuleRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRuleRevisionsPagedResponse)>` |   
  
### listRules(@Nullable InstanceName parent)
    
    
    public final RuleServiceClient.ListRulesPagedResponse listRules(@Nullable InstanceName parent)

Lists Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       for (Rule element : ruleServiceClient.listRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.InstanceName`  
Required. The parent, which owns this collection of rules. Format: `projects/{project}/locations/{location}/instances/{instance}`  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRulesPagedResponse)` |   
  
### listRules(ListRulesRequest request)
    
    
    public final RuleServiceClient.ListRulesPagedResponse listRules(ListRulesRequest request)

Lists Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRulesRequest request =
           ListRulesRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(RuleView.forNumber(0))
               .setFilter("filter-1274492040")
               .build();
       for (Rule element : ruleServiceClient.listRules(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRulesPagedResponse)` |   
  
### listRules(String parent)
    
    
    public final RuleServiceClient.ListRulesPagedResponse listRules(String parent)

Lists Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       for (Rule element : ruleServiceClient.listRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of rules. Format: `projects/{project}/locations/{location}/instances/{instance}`  
**Returns**  
---  
**Type** | **Description**  
`[RuleServiceClient.ListRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRulesPagedResponse)` |   
  
### listRulesCallable()
    
    
    public final UnaryCallable<ListRulesRequest,ListRulesResponse> listRulesCallable()

Lists Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRulesRequest request =
           ListRulesRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(RuleView.forNumber(0))
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListRulesResponse response = ruleServiceClient.listRulesCallable().call(request);
         for (Rule element : response.getRulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRulesRequest),[ListRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRulesResponse)>` |   
  
### listRulesPagedCallable()
    
    
    public final UnaryCallable<ListRulesRequest,RuleServiceClient.ListRulesPagedResponse> listRulesPagedCallable()

Lists Rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       ListRulesRequest request =
           ListRulesRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setView(RuleView.forNumber(0))
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Rule> future = ruleServiceClient.listRulesPagedCallable().futureCall(request);
       // Do something.
       for (Rule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ListRulesRequest),[ListRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleServiceClient.ListRulesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateRule(Rule rule, FieldMask updateMask)
    
    
    public final Rule updateRule(Rule rule, FieldMask updateMask)

Updates a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       Rule rule = Rule.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Rule response = ruleServiceClient.updateRule(rule, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`rule` | `[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)`  
Required. The rule to update. The rule's `name` field is used to identify the rule to update. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to update. If not included, all fields with a non-empty value will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)` |   
  
### updateRule(UpdateRuleRequest request)
    
    
    public final Rule updateRule(UpdateRuleRequest request)

Updates a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       UpdateRuleRequest request =
           UpdateRuleRequest.newBuilder()
               .setRule(Rule.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Rule response = ruleServiceClient.updateRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.UpdateRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)` |   
  
### updateRuleCallable()
    
    
    public final UnaryCallable<UpdateRuleRequest,Rule> updateRuleCallable()

Updates a Rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       UpdateRuleRequest request =
           UpdateRuleRequest.newBuilder()
               .setRule(Rule.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Rule> future = ruleServiceClient.updateRuleCallable().futureCall(request);
       // Do something.
       Rule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.UpdateRuleRequest),[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.Rule)>` |   
  
### updateRuleDeployment(RuleDeployment ruleDeployment, FieldMask updateMask)
    
    
    public final RuleDeployment updateRuleDeployment(RuleDeployment ruleDeployment, FieldMask updateMask)

Updates a RuleDeployment. Failures are not necessarily atomic. If there is a request to update multiple fields, and any update to a single field fails, an error will be returned, but other fields may remain successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       RuleDeployment ruleDeployment = RuleDeployment.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       RuleDeployment response = ruleServiceClient.updateRuleDeployment(ruleDeployment, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`ruleDeployment` | `[RuleDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleDeployment)`  
Required. The rule deployment to update. The rule deployment's `name` field is used to identify the rule deployment to update. Format: `projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/deployment`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[RuleDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleDeployment)` |   
  
### updateRuleDeployment(UpdateRuleDeploymentRequest request)
    
    
    public final RuleDeployment updateRuleDeployment(UpdateRuleDeploymentRequest request)

Updates a RuleDeployment. Failures are not necessarily atomic. If there is a request to update multiple fields, and any update to a single field fails, an error will be returned, but other fields may remain successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       UpdateRuleDeploymentRequest request =
           UpdateRuleDeploymentRequest.newBuilder()
               .setRuleDeployment(RuleDeployment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       RuleDeployment response = ruleServiceClient.updateRuleDeployment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRuleDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.UpdateRuleDeploymentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RuleDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleDeployment)` |   
  
### updateRuleDeploymentCallable()
    
    
    public final UnaryCallable<UpdateRuleDeploymentRequest,RuleDeployment> updateRuleDeploymentCallable()

Updates a RuleDeployment. Failures are not necessarily atomic. If there is a request to update multiple fields, and any update to a single field fails, an error will be returned, but other fields may remain successfully updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       UpdateRuleDeploymentRequest request =
           UpdateRuleDeploymentRequest.newBuilder()
               .setRuleDeployment(RuleDeployment.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<RuleDeployment> future =
           ruleServiceClient.updateRuleDeploymentCallable().futureCall(request);
       // Do something.
       RuleDeployment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRuleDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.UpdateRuleDeploymentRequest),[RuleDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleDeployment)>` |   
  
### verifyRuleText(@Nullable InstanceName instance, String ruleText)
    
    
    public final VerifyRuleTextResponse verifyRuleText(@Nullable InstanceName instance, String ruleText)

Verifies the given rule text.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       InstanceName instance = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       String ruleText = "ruleText763458121";
       VerifyRuleTextResponse response = ruleServiceClient.verifyRuleText(instance, ruleText);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `@org.jspecify.annotations.Nullable com.google.cloud.chronicle.v1.InstanceName`  
Required. The name of the parent resource, which is the SecOps instance associated with the request. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`ruleText` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The rule text to verify as a UTF-8 string.  
**Returns**  
---  
**Type** | **Description**  
`[VerifyRuleTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.VerifyRuleTextResponse)` |   
  
### verifyRuleText(VerifyRuleTextRequest request)
    
    
    public final VerifyRuleTextResponse verifyRuleText(VerifyRuleTextRequest request)

Verifies the given rule text.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       VerifyRuleTextRequest request =
           VerifyRuleTextRequest.newBuilder()
               .setInstance(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRuleText("ruleText763458121")
               .build();
       VerifyRuleTextResponse response = ruleServiceClient.verifyRuleText(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[VerifyRuleTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.VerifyRuleTextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VerifyRuleTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.VerifyRuleTextResponse)` |   
  
### verifyRuleText(String instance, String ruleText)
    
    
    public final VerifyRuleTextResponse verifyRuleText(String instance, String ruleText)

Verifies the given rule text.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       String instance = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       String ruleText = "ruleText763458121";
       VerifyRuleTextResponse response = ruleServiceClient.verifyRuleText(instance, ruleText);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the parent resource, which is the SecOps instance associated with the request. Format: `projects/{project}/locations/{location}/instances/{instance}`  
`ruleText` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The rule text to verify as a UTF-8 string.  
**Returns**  
---  
**Type** | **Description**  
`[VerifyRuleTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.VerifyRuleTextResponse)` |   
  
### verifyRuleTextCallable()
    
    
    public final UnaryCallable<VerifyRuleTextRequest,VerifyRuleTextResponse> verifyRuleTextCallable()

Verifies the given rule text.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RuleServiceClient ruleServiceClient = RuleServiceClient.create()) {
       VerifyRuleTextRequest request =
           VerifyRuleTextRequest.newBuilder()
               .setInstance(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRuleText("ruleText763458121")
               .build();
       ApiFuture<VerifyRuleTextResponse> future =
           ruleServiceClient.verifyRuleTextCallable().futureCall(request);
       // Do something.
       VerifyRuleTextResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[VerifyRuleTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.VerifyRuleTextRequest),[VerifyRuleTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.VerifyRuleTextResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
