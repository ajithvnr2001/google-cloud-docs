---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallClient
title: Class FirewallClient (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:21.597211+00:00
---

# Class FirewallClient (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FirewallClient (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.4  2.2.0  2.1.10  0.2.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-appengine-admin/google-cloud-appengine-admin/src/main/java/com/google/appengine/v1/FirewallClient.java)| [Product Reference](https://cloud.google.com/appengine/docs/admin-api/)  
---|---  
  
Service Description: Firewall resources are used to define a collection of access control rules for an Application. Each rule is defined with a position which specifies the rule's order in the sequence of rules, an IP range to be matched against requests, and an action to take upon matching requests.

Every request is evaluated against the Firewall rules in priority order. Processesing stops at the first rule which matches the request's IP address. A final rule always specifies an action that applies to all remaining IP addresses. The default final rule for a newly-created application will be set to "allow" if not otherwise specified by the user.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       BatchUpdateIngressRulesRequest request =
           BatchUpdateIngressRulesRequest.newBuilder()
               .setName("name3373707")
               .addAllIngressRules(new ArrayList<FirewallRule>())
               .build();
       BatchUpdateIngressRulesResponse response = firewallClient.batchUpdateIngressRules(request);
     }
     

Note: close() needs to be called on the FirewallClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListIngressRules |  Lists the firewall rules of an application. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listIngressRules(ListIngressRulesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listIngressRulesPagedCallable() 
  * listIngressRulesCallable() 

  
BatchUpdateIngressRules |  Replaces the entire firewall ruleset in one bulk operation. This overrides and replaces the rules of an existing firewall with the new rules.  If the final rule does not match traffic with the '*' wildcard IP range, then an "allow all" rule is explicitly added to the end of the list. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateIngressRules(BatchUpdateIngressRulesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateIngressRulesCallable() 

  
CreateIngressRule |  Creates a firewall rule for the application. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createIngressRule(CreateIngressRuleRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createIngressRuleCallable() 

  
GetIngressRule |  Gets the specified firewall rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIngressRule(GetIngressRuleRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIngressRuleCallable() 

  
UpdateIngressRule |  Updates the specified firewall rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateIngressRule(UpdateIngressRuleRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateIngressRuleCallable() 

  
DeleteIngressRule |  Deletes the specified firewall rule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteIngressRule(DeleteIngressRuleRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteIngressRuleCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of FirewallSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FirewallSettings firewallSettings =
         FirewallSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FirewallClient firewallClient = FirewallClient.create(firewallSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FirewallSettings firewallSettings =
         FirewallSettings.newBuilder().setEndpoint(myEndpoint).build();
     FirewallClient firewallClient = FirewallClient.create(firewallSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FirewallSettings firewallSettings = FirewallSettings.newHttpJsonBuilder().build();
     FirewallClient firewallClient = FirewallClient.create(firewallSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FirewallClient

## Static Methods 

### create()
    
    
    public static final FirewallClient create()

Constructs an instance of FirewallClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FirewallClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FirewallSettings settings)
    
    
    public static final FirewallClient create(FirewallSettings settings)

Constructs an instance of FirewallClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FirewallSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FirewallClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FirewallStub stub)
    
    
    public static final FirewallClient create(FirewallStub stub)

Constructs an instance of FirewallClient, using the given stub for making calls. This is for advanced usage - prefer using create(FirewallSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FirewallStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.stub.FirewallStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FirewallClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallClient)` |   
  
## Constructors 

### FirewallClient(FirewallSettings settings)
    
    
    protected FirewallClient(FirewallSettings settings)

Constructs an instance of FirewallClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FirewallSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallSettings)`  
  
  
### FirewallClient(FirewallStub stub)
    
    
    protected FirewallClient(FirewallStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FirewallStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.stub.FirewallStub)`  
  
  
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
  
### batchUpdateIngressRules(BatchUpdateIngressRulesRequest request)
    
    
    public final BatchUpdateIngressRulesResponse batchUpdateIngressRules(BatchUpdateIngressRulesRequest request)

Replaces the entire firewall ruleset in one bulk operation. This overrides and replaces the rules of an existing firewall with the new rules.

If the final rule does not match traffic with the '*' wildcard IP range, then an "allow all" rule is explicitly added to the end of the list.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       BatchUpdateIngressRulesRequest request =
           BatchUpdateIngressRulesRequest.newBuilder()
               .setName("name3373707")
               .addAllIngressRules(new ArrayList<FirewallRule>())
               .build();
       BatchUpdateIngressRulesResponse response = firewallClient.batchUpdateIngressRules(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateIngressRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.BatchUpdateIngressRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateIngressRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.BatchUpdateIngressRulesResponse)` |   
  
### batchUpdateIngressRulesCallable()
    
    
    public final UnaryCallable<BatchUpdateIngressRulesRequest,BatchUpdateIngressRulesResponse> batchUpdateIngressRulesCallable()

Replaces the entire firewall ruleset in one bulk operation. This overrides and replaces the rules of an existing firewall with the new rules.

If the final rule does not match traffic with the '*' wildcard IP range, then an "allow all" rule is explicitly added to the end of the list.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       BatchUpdateIngressRulesRequest request =
           BatchUpdateIngressRulesRequest.newBuilder()
               .setName("name3373707")
               .addAllIngressRules(new ArrayList<FirewallRule>())
               .build();
       ApiFuture<BatchUpdateIngressRulesResponse> future =
           firewallClient.batchUpdateIngressRulesCallable().futureCall(request);
       // Do something.
       BatchUpdateIngressRulesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateIngressRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.BatchUpdateIngressRulesRequest),[BatchUpdateIngressRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.BatchUpdateIngressRulesResponse)>` |   
  
### close()
    
    
    public final void close()

### createIngressRule(CreateIngressRuleRequest request)
    
    
    public final FirewallRule createIngressRule(CreateIngressRuleRequest request)

Creates a firewall rule for the application.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       CreateIngressRuleRequest request =
           CreateIngressRuleRequest.newBuilder()
               .setParent("parent-995424086")
               .setRule(FirewallRule.newBuilder().build())
               .build();
       FirewallRule response = firewallClient.createIngressRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateIngressRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.CreateIngressRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.firewall.FirewallRule)` |   
  
### createIngressRuleCallable()
    
    
    public final UnaryCallable<CreateIngressRuleRequest,FirewallRule> createIngressRuleCallable()

Creates a firewall rule for the application.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       CreateIngressRuleRequest request =
           CreateIngressRuleRequest.newBuilder()
               .setParent("parent-995424086")
               .setRule(FirewallRule.newBuilder().build())
               .build();
       ApiFuture<FirewallRule> future =
           firewallClient.createIngressRuleCallable().futureCall(request);
       // Do something.
       FirewallRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateIngressRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.CreateIngressRuleRequest),[FirewallRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.firewall.FirewallRule)>` |   
  
### deleteIngressRule(DeleteIngressRuleRequest request)
    
    
    public final void deleteIngressRule(DeleteIngressRuleRequest request)

Deletes the specified firewall rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       DeleteIngressRuleRequest request =
           DeleteIngressRuleRequest.newBuilder().setName("name3373707").build();
       firewallClient.deleteIngressRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteIngressRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.DeleteIngressRuleRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteIngressRuleCallable()
    
    
    public final UnaryCallable<DeleteIngressRuleRequest,Empty> deleteIngressRuleCallable()

Deletes the specified firewall rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       DeleteIngressRuleRequest request =
           DeleteIngressRuleRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Empty> future = firewallClient.deleteIngressRuleCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteIngressRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.DeleteIngressRuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getIngressRule(GetIngressRuleRequest request)
    
    
    public final FirewallRule getIngressRule(GetIngressRuleRequest request)

Gets the specified firewall rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       GetIngressRuleRequest request =
           GetIngressRuleRequest.newBuilder().setName("name3373707").build();
       FirewallRule response = firewallClient.getIngressRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIngressRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.GetIngressRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.firewall.FirewallRule)` |   
  
### getIngressRuleCallable()
    
    
    public final UnaryCallable<GetIngressRuleRequest,FirewallRule> getIngressRuleCallable()

Gets the specified firewall rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       GetIngressRuleRequest request =
           GetIngressRuleRequest.newBuilder().setName("name3373707").build();
       ApiFuture<FirewallRule> future = firewallClient.getIngressRuleCallable().futureCall(request);
       // Do something.
       FirewallRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIngressRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.GetIngressRuleRequest),[FirewallRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.firewall.FirewallRule)>` |   
  
### getSettings()
    
    
    public final @Nullable FirewallSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.appengine.v1.FirewallSettings` |   
  
### getStub()
    
    
    public FirewallStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FirewallStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.stub.FirewallStub)` |   
  
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
  
### listIngressRules(ListIngressRulesRequest request)
    
    
    public final FirewallClient.ListIngressRulesPagedResponse listIngressRules(ListIngressRulesRequest request)

Lists the firewall rules of an application.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       ListIngressRulesRequest request =
           ListIngressRulesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setMatchingAddress("matchingAddress861962551")
               .build();
       for (FirewallRule element : firewallClient.listIngressRules(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListIngressRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.ListIngressRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallClient.ListIngressRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallClient.ListIngressRulesPagedResponse)` |   
  
### listIngressRulesCallable()
    
    
    public final UnaryCallable<ListIngressRulesRequest,ListIngressRulesResponse> listIngressRulesCallable()

Lists the firewall rules of an application.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       ListIngressRulesRequest request =
           ListIngressRulesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setMatchingAddress("matchingAddress861962551")
               .build();
       while (true) {
         ListIngressRulesResponse response = firewallClient.listIngressRulesCallable().call(request);
         for (FirewallRule element : response.getIngressRulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIngressRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.ListIngressRulesRequest),[ListIngressRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.ListIngressRulesResponse)>` |   
  
### listIngressRulesPagedCallable()
    
    
    public final UnaryCallable<ListIngressRulesRequest,FirewallClient.ListIngressRulesPagedResponse> listIngressRulesPagedCallable()

Lists the firewall rules of an application.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       ListIngressRulesRequest request =
           ListIngressRulesRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setMatchingAddress("matchingAddress861962551")
               .build();
       ApiFuture<FirewallRule> future =
           firewallClient.listIngressRulesPagedCallable().futureCall(request);
       // Do something.
       for (FirewallRule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIngressRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.ListIngressRulesRequest),[ListIngressRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.FirewallClient.ListIngressRulesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateIngressRule(UpdateIngressRuleRequest request)
    
    
    public final FirewallRule updateIngressRule(UpdateIngressRuleRequest request)

Updates the specified firewall rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       UpdateIngressRuleRequest request =
           UpdateIngressRuleRequest.newBuilder()
               .setName("name3373707")
               .setRule(FirewallRule.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       FirewallRule response = firewallClient.updateIngressRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateIngressRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.UpdateIngressRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.firewall.FirewallRule)` |   
  
### updateIngressRuleCallable()
    
    
    public final UnaryCallable<UpdateIngressRuleRequest,FirewallRule> updateIngressRuleCallable()

Updates the specified firewall rule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallClient firewallClient = FirewallClient.create()) {
       UpdateIngressRuleRequest request =
           UpdateIngressRuleRequest.newBuilder()
               .setName("name3373707")
               .setRule(FirewallRule.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<FirewallRule> future =
           firewallClient.updateIngressRuleCallable().futureCall(request);
       // Do something.
       FirewallRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateIngressRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.UpdateIngressRuleRequest),[FirewallRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-appengine-admin/latest/com.google.appengine.v1.firewall.FirewallRule)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
