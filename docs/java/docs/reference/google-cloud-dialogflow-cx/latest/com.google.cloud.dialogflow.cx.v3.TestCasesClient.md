---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient
title: Class TestCasesClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:34:12.509496+00:00
---

# Class TestCasesClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TestCasesClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3/TestCasesClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for managing Test Cases and Test Case Results.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       testCasesClient.batchDeleteTestCases(parent);
     }
     

Note: close() needs to be called on the TestCasesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListTestCases |  Fetches a list of test cases for a given agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTestCases(ListTestCasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTestCases(AgentName parent) 
  * listTestCases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTestCasesPagedCallable() 
  * listTestCasesCallable() 

  
BatchDeleteTestCases |  Batch deletes test cases. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeleteTestCases(BatchDeleteTestCasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeleteTestCases(AgentName parent) 
  * batchDeleteTestCases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeleteTestCasesCallable() 

  
GetTestCase |  Gets a test case. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTestCase(GetTestCaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTestCase(TestCaseName name) 
  * getTestCase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTestCaseCallable() 

  
CreateTestCase |  Creates a test case for the given agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTestCase(CreateTestCaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTestCase(AgentName parent, TestCase testCase) 
  * createTestCase(String parent, TestCase testCase) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTestCaseCallable() 

  
UpdateTestCase |  Updates the specified test case. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTestCase(UpdateTestCaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTestCase(TestCase testCase, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTestCaseCallable() 

  
RunTestCase |  Kicks off a test case run.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: RunTestCaseMetadata \- `response`: RunTestCaseResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runTestCaseAsync(RunTestCaseRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runTestCaseOperationCallable() 
  * runTestCaseCallable() 

  
BatchRunTestCases |  Kicks off a batch run of test cases.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: BatchRunTestCasesMetadata \- `response`: BatchRunTestCasesResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRunTestCasesAsync(BatchRunTestCasesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRunTestCasesOperationCallable() 
  * batchRunTestCasesCallable() 

  
CalculateCoverage |  Calculates the test coverage for an agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * calculateCoverage(CalculateCoverageRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * calculateCoverageCallable() 

  
ImportTestCases |  Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won't overwrite any existing ones. The provided ID in the imported test case is neglected.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: ImportTestCasesMetadata \- `response`: ImportTestCasesResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importTestCasesAsync(ImportTestCasesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importTestCasesOperationCallable() 
  * importTestCasesCallable() 

  
ExportTestCases |  Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: ExportTestCasesMetadata \- `response`: ExportTestCasesResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportTestCasesAsync(ExportTestCasesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportTestCasesOperationCallable() 
  * exportTestCasesCallable() 

  
ListTestCaseResults |  Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTestCaseResults(ListTestCaseResultsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTestCaseResults(TestCaseName parent) 
  * listTestCaseResults(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTestCaseResultsPagedCallable() 
  * listTestCaseResultsCallable() 

  
GetTestCaseResult |  Gets a test case result. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTestCaseResult(GetTestCaseResultRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTestCaseResult(TestCaseResultName name) 
  * getTestCaseResult(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTestCaseResultCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TestCasesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TestCasesSettings testCasesSettings =
         TestCasesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TestCasesClient testCasesClient = TestCasesClient.create(testCasesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TestCasesSettings testCasesSettings =
         TestCasesSettings.newBuilder().setEndpoint(myEndpoint).build();
     TestCasesClient testCasesClient = TestCasesClient.create(testCasesSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TestCasesSettings testCasesSettings = TestCasesSettings.newHttpJsonBuilder().build();
     TestCasesClient testCasesClient = TestCasesClient.create(testCasesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TestCasesClient

## Static Methods 

### create()
    
    
    public static final TestCasesClient create()

Constructs an instance of TestCasesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TestCasesSettings settings)
    
    
    public static final TestCasesClient create(TestCasesSettings settings)

Constructs an instance of TestCasesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TestCasesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TestCasesStub stub)
    
    
    public static final TestCasesClient create(TestCasesStub stub)

Constructs an instance of TestCasesClient, using the given stub for making calls. This is for advanced usage - prefer using create(TestCasesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TestCasesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.TestCasesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient)` |   
  
## Constructors 

### TestCasesClient(TestCasesSettings settings)
    
    
    protected TestCasesClient(TestCasesSettings settings)

Constructs an instance of TestCasesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TestCasesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesSettings)`  
  
  
### TestCasesClient(TestCasesStub stub)
    
    
    protected TestCasesClient(TestCasesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TestCasesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.TestCasesStub)`  
  
  
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
  
### batchDeleteTestCases(@Nullable AgentName parent)
    
    
    public final void batchDeleteTestCases(@Nullable AgentName parent)

Batch deletes test cases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       testCasesClient.batchDeleteTestCases(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The agent to delete test cases from. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
  
### batchDeleteTestCases(BatchDeleteTestCasesRequest request)
    
    
    public final void batchDeleteTestCases(BatchDeleteTestCasesRequest request)

Batch deletes test cases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       BatchDeleteTestCasesRequest request =
           BatchDeleteTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       testCasesClient.batchDeleteTestCases(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchDeleteTestCasesRequest)`  
The request object containing all of the parameters for the API call.  
  
### batchDeleteTestCases(String parent)
    
    
    public final void batchDeleteTestCases(String parent)

Batch deletes test cases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       testCasesClient.batchDeleteTestCases(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to delete test cases from. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
  
### batchDeleteTestCasesCallable()
    
    
    public final UnaryCallable<BatchDeleteTestCasesRequest,Empty> batchDeleteTestCasesCallable()

Batch deletes test cases.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       BatchDeleteTestCasesRequest request =
           BatchDeleteTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<Empty> future = testCasesClient.batchDeleteTestCasesCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchDeleteTestCasesRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### batchRunTestCasesAsync(BatchRunTestCasesRequest request)
    
    
    public final OperationFuture<BatchRunTestCasesResponse,BatchRunTestCasesMetadata> batchRunTestCasesAsync(BatchRunTestCasesRequest request)

Kicks off a batch run of test cases.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: BatchRunTestCasesMetadata \- `response`: BatchRunTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       BatchRunTestCasesRequest request =
           BatchRunTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .addAllTestCases(new ArrayList<String>())
               .build();
       BatchRunTestCasesResponse response = testCasesClient.batchRunTestCasesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRunTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchRunTestCasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchRunTestCasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchRunTestCasesResponse),[BatchRunTestCasesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchRunTestCasesMetadata)>` |   
  
### batchRunTestCasesCallable()
    
    
    public final UnaryCallable<BatchRunTestCasesRequest,Operation> batchRunTestCasesCallable()

Kicks off a batch run of test cases.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: BatchRunTestCasesMetadata \- `response`: BatchRunTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       BatchRunTestCasesRequest request =
           BatchRunTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .addAllTestCases(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future = testCasesClient.batchRunTestCasesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRunTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchRunTestCasesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchRunTestCasesOperationCallable()
    
    
    public final OperationCallable<BatchRunTestCasesRequest,BatchRunTestCasesResponse,BatchRunTestCasesMetadata> batchRunTestCasesOperationCallable()

Kicks off a batch run of test cases.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: BatchRunTestCasesMetadata \- `response`: BatchRunTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       BatchRunTestCasesRequest request =
           BatchRunTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .addAllTestCases(new ArrayList<String>())
               .build();
       OperationFuture<BatchRunTestCasesResponse, BatchRunTestCasesMetadata> future =
           testCasesClient.batchRunTestCasesOperationCallable().futureCall(request);
       // Do something.
       BatchRunTestCasesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchRunTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchRunTestCasesRequest),[BatchRunTestCasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchRunTestCasesResponse),[BatchRunTestCasesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.BatchRunTestCasesMetadata)>` |   
  
### calculateCoverage(CalculateCoverageRequest request)
    
    
    public final CalculateCoverageResponse calculateCoverage(CalculateCoverageRequest request)

Calculates the test coverage for an agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       CalculateCoverageRequest request =
           CalculateCoverageRequest.newBuilder()
               .setAgent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       CalculateCoverageResponse response = testCasesClient.calculateCoverage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CalculateCoverageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CalculateCoverageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CalculateCoverageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CalculateCoverageResponse)` |   
  
### calculateCoverageCallable()
    
    
    public final UnaryCallable<CalculateCoverageRequest,CalculateCoverageResponse> calculateCoverageCallable()

Calculates the test coverage for an agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       CalculateCoverageRequest request =
           CalculateCoverageRequest.newBuilder()
               .setAgent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       ApiFuture<CalculateCoverageResponse> future =
           testCasesClient.calculateCoverageCallable().futureCall(request);
       // Do something.
       CalculateCoverageResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CalculateCoverageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CalculateCoverageRequest),[CalculateCoverageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CalculateCoverageResponse)>` |   
  
### close()
    
    
    public final void close()

### createTestCase(@Nullable AgentName parent, TestCase testCase)
    
    
    public final TestCase createTestCase(@Nullable AgentName parent, TestCase testCase)

Creates a test case for the given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       TestCase testCase = TestCase.newBuilder().build();
       TestCase response = testCasesClient.createTestCase(parent, testCase);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The agent to create the test case for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`testCase` | `[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)`  
Required. The test case to create.  
**Returns**  
---  
**Type** | **Description**  
`[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)` |   
  
### createTestCase(CreateTestCaseRequest request)
    
    
    public final TestCase createTestCase(CreateTestCaseRequest request)

Creates a test case for the given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       CreateTestCaseRequest request =
           CreateTestCaseRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setTestCase(TestCase.newBuilder().build())
               .build();
       TestCase response = testCasesClient.createTestCase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateTestCaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)` |   
  
### createTestCase(String parent, TestCase testCase)
    
    
    public final TestCase createTestCase(String parent, TestCase testCase)

Creates a test case for the given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       TestCase testCase = TestCase.newBuilder().build();
       TestCase response = testCasesClient.createTestCase(parent, testCase);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to create the test case for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`testCase` | `[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)`  
Required. The test case to create.  
**Returns**  
---  
**Type** | **Description**  
`[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)` |   
  
### createTestCaseCallable()
    
    
    public final UnaryCallable<CreateTestCaseRequest,TestCase> createTestCaseCallable()

Creates a test case for the given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       CreateTestCaseRequest request =
           CreateTestCaseRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setTestCase(TestCase.newBuilder().build())
               .build();
       ApiFuture<TestCase> future = testCasesClient.createTestCaseCallable().futureCall(request);
       // Do something.
       TestCase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateTestCaseRequest),[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)>` |   
  
### exportTestCasesAsync(ExportTestCasesRequest request)
    
    
    public final OperationFuture<ExportTestCasesResponse,ExportTestCasesMetadata> exportTestCasesAsync(ExportTestCasesRequest request)

Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ExportTestCasesMetadata \- `response`: ExportTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ExportTestCasesRequest request =
           ExportTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setFilter("filter-1274492040")
               .build();
       ExportTestCasesResponse response = testCasesClient.exportTestCasesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportTestCasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportTestCasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportTestCasesResponse),[ExportTestCasesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportTestCasesMetadata)>` |   
  
### exportTestCasesCallable()
    
    
    public final UnaryCallable<ExportTestCasesRequest,Operation> exportTestCasesCallable()

Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ExportTestCasesMetadata \- `response`: ExportTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ExportTestCasesRequest request =
           ExportTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Operation> future = testCasesClient.exportTestCasesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportTestCasesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportTestCasesOperationCallable()
    
    
    public final OperationCallable<ExportTestCasesRequest,ExportTestCasesResponse,ExportTestCasesMetadata> exportTestCasesOperationCallable()

Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ExportTestCasesMetadata \- `response`: ExportTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ExportTestCasesRequest request =
           ExportTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setFilter("filter-1274492040")
               .build();
       OperationFuture<ExportTestCasesResponse, ExportTestCasesMetadata> future =
           testCasesClient.exportTestCasesOperationCallable().futureCall(request);
       // Do something.
       ExportTestCasesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportTestCasesRequest),[ExportTestCasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportTestCasesResponse),[ExportTestCasesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportTestCasesMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = testCasesClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = testCasesClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable TestCasesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.TestCasesSettings` |   
  
### getStub()
    
    
    public TestCasesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TestCasesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.TestCasesStub)` |   
  
### getTestCase(@Nullable TestCaseName name)
    
    
    public final TestCase getTestCase(@Nullable TestCaseName name)

Gets a test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       TestCaseName name = TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]");
       TestCase response = testCasesClient.getTestCase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.TestCaseName`  
Required. The name of the testcase. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>`.  
**Returns**  
---  
**Type** | **Description**  
`[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)` |   
  
### getTestCase(GetTestCaseRequest request)
    
    
    public final TestCase getTestCase(GetTestCaseRequest request)

Gets a test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       GetTestCaseRequest request =
           GetTestCaseRequest.newBuilder()
               .setName(
                   TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString())
               .build();
       TestCase response = testCasesClient.getTestCase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetTestCaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)` |   
  
### getTestCase(String name)
    
    
    public final TestCase getTestCase(String name)

Gets a test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       String name = TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString();
       TestCase response = testCasesClient.getTestCase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the testcase. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>`.  
**Returns**  
---  
**Type** | **Description**  
`[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)` |   
  
### getTestCaseCallable()
    
    
    public final UnaryCallable<GetTestCaseRequest,TestCase> getTestCaseCallable()

Gets a test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       GetTestCaseRequest request =
           GetTestCaseRequest.newBuilder()
               .setName(
                   TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString())
               .build();
       ApiFuture<TestCase> future = testCasesClient.getTestCaseCallable().futureCall(request);
       // Do something.
       TestCase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetTestCaseRequest),[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)>` |   
  
### getTestCaseResult(@Nullable TestCaseResultName name)
    
    
    public final TestCaseResult getTestCaseResult(@Nullable TestCaseResultName name)

Gets a test case result.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       TestCaseResultName name =
           TestCaseResultName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]", "[RESULT]");
       TestCaseResult response = testCasesClient.getTestCaseResult(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.TestCaseResultName`  
Required. The name of the testcase. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>/results/<TestCaseResultID>`.  
**Returns**  
---  
**Type** | **Description**  
`[TestCaseResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCaseResult)` |   
  
### getTestCaseResult(GetTestCaseResultRequest request)
    
    
    public final TestCaseResult getTestCaseResult(GetTestCaseResultRequest request)

Gets a test case result.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       GetTestCaseResultRequest request =
           GetTestCaseResultRequest.newBuilder()
               .setName(
                   TestCaseResultName.of(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]", "[RESULT]")
                       .toString())
               .build();
       TestCaseResult response = testCasesClient.getTestCaseResult(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTestCaseResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetTestCaseResultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestCaseResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCaseResult)` |   
  
### getTestCaseResult(String name)
    
    
    public final TestCaseResult getTestCaseResult(String name)

Gets a test case result.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       String name =
           TestCaseResultName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]", "[RESULT]")
               .toString();
       TestCaseResult response = testCasesClient.getTestCaseResult(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the testcase. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>/results/<TestCaseResultID>`.  
**Returns**  
---  
**Type** | **Description**  
`[TestCaseResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCaseResult)` |   
  
### getTestCaseResultCallable()
    
    
    public final UnaryCallable<GetTestCaseResultRequest,TestCaseResult> getTestCaseResultCallable()

Gets a test case result.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       GetTestCaseResultRequest request =
           GetTestCaseResultRequest.newBuilder()
               .setName(
                   TestCaseResultName.of(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]", "[RESULT]")
                       .toString())
               .build();
       ApiFuture<TestCaseResult> future =
           testCasesClient.getTestCaseResultCallable().futureCall(request);
       // Do something.
       TestCaseResult response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTestCaseResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetTestCaseResultRequest),[TestCaseResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCaseResult)>` |   
  
### importTestCasesAsync(ImportTestCasesRequest request)
    
    
    public final OperationFuture<ImportTestCasesResponse,ImportTestCasesMetadata> importTestCasesAsync(ImportTestCasesRequest request)

Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won't overwrite any existing ones. The provided ID in the imported test case is neglected.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ImportTestCasesMetadata \- `response`: ImportTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ImportTestCasesRequest request =
           ImportTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       ImportTestCasesResponse response = testCasesClient.importTestCasesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportTestCasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportTestCasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportTestCasesResponse),[ImportTestCasesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportTestCasesMetadata)>` |   
  
### importTestCasesCallable()
    
    
    public final UnaryCallable<ImportTestCasesRequest,Operation> importTestCasesCallable()

Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won't overwrite any existing ones. The provided ID in the imported test case is neglected.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ImportTestCasesMetadata \- `response`: ImportTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ImportTestCasesRequest request =
           ImportTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       ApiFuture<Operation> future = testCasesClient.importTestCasesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportTestCasesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importTestCasesOperationCallable()
    
    
    public final OperationCallable<ImportTestCasesRequest,ImportTestCasesResponse,ImportTestCasesMetadata> importTestCasesOperationCallable()

Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won't overwrite any existing ones. The provided ID in the imported test case is neglected.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ImportTestCasesMetadata \- `response`: ImportTestCasesResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ImportTestCasesRequest request =
           ImportTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       OperationFuture<ImportTestCasesResponse, ImportTestCasesMetadata> future =
           testCasesClient.importTestCasesOperationCallable().futureCall(request);
       // Do something.
       ImportTestCasesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportTestCasesRequest),[ImportTestCasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportTestCasesResponse),[ImportTestCasesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportTestCasesMetadata)>` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final TestCasesClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : testCasesClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = testCasesClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,TestCasesClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = testCasesClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListLocationsPagedResponse)>` |   
  
### listTestCaseResults(@Nullable TestCaseName parent)
    
    
    public final TestCasesClient.ListTestCaseResultsPagedResponse listTestCaseResults(@Nullable TestCaseName parent)

Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       TestCaseName parent = TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]");
       for (TestCaseResult element : testCasesClient.listTestCaseResults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.TestCaseName`  
Required. The test case to list results for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>`. Specify a `-` as a wildcard for TestCase ID to list results across multiple test cases.  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient.ListTestCaseResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListTestCaseResultsPagedResponse)` |   
  
### listTestCaseResults(ListTestCaseResultsRequest request)
    
    
    public final TestCasesClient.ListTestCaseResultsPagedResponse listTestCaseResults(ListTestCaseResultsRequest request)

Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListTestCaseResultsRequest request =
           ListTestCaseResultsRequest.newBuilder()
               .setParent(
                   TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (TestCaseResult element : testCasesClient.listTestCaseResults(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTestCaseResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCaseResultsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient.ListTestCaseResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListTestCaseResultsPagedResponse)` |   
  
### listTestCaseResults(String parent)
    
    
    public final TestCasesClient.ListTestCaseResultsPagedResponse listTestCaseResults(String parent)

Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       String parent =
           TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString();
       for (TestCaseResult element : testCasesClient.listTestCaseResults(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The test case to list results for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>`. Specify a `-` as a wildcard for TestCase ID to list results across multiple test cases.  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient.ListTestCaseResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListTestCaseResultsPagedResponse)` |   
  
### listTestCaseResultsCallable()
    
    
    public final UnaryCallable<ListTestCaseResultsRequest,ListTestCaseResultsResponse> listTestCaseResultsCallable()

Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListTestCaseResultsRequest request =
           ListTestCaseResultsRequest.newBuilder()
               .setParent(
                   TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListTestCaseResultsResponse response =
             testCasesClient.listTestCaseResultsCallable().call(request);
         for (TestCaseResult element : response.getTestCaseResultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTestCaseResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCaseResultsRequest),[ListTestCaseResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCaseResultsResponse)>` |   
  
### listTestCaseResultsPagedCallable()
    
    
    public final UnaryCallable<ListTestCaseResultsRequest,TestCasesClient.ListTestCaseResultsPagedResponse> listTestCaseResultsPagedCallable()

Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListTestCaseResultsRequest request =
           ListTestCaseResultsRequest.newBuilder()
               .setParent(
                   TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<TestCaseResult> future =
           testCasesClient.listTestCaseResultsPagedCallable().futureCall(request);
       // Do something.
       for (TestCaseResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTestCaseResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCaseResultsRequest),[ListTestCaseResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListTestCaseResultsPagedResponse)>` |   
  
### listTestCases(@Nullable AgentName parent)
    
    
    public final TestCasesClient.ListTestCasesPagedResponse listTestCases(@Nullable AgentName parent)

Fetches a list of test cases for a given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       for (TestCase element : testCasesClient.listTestCases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The agent to list all pages for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient.ListTestCasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListTestCasesPagedResponse)` |   
  
### listTestCases(ListTestCasesRequest request)
    
    
    public final TestCasesClient.ListTestCasesPagedResponse listTestCases(ListTestCasesRequest request)

Fetches a list of test cases for a given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListTestCasesRequest request =
           ListTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (TestCase element : testCasesClient.listTestCases(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient.ListTestCasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListTestCasesPagedResponse)` |   
  
### listTestCases(String parent)
    
    
    public final TestCasesClient.ListTestCasesPagedResponse listTestCases(String parent)

Fetches a list of test cases for a given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       for (TestCase element : testCasesClient.listTestCases(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to list all pages for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[TestCasesClient.ListTestCasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListTestCasesPagedResponse)` |   
  
### listTestCasesCallable()
    
    
    public final UnaryCallable<ListTestCasesRequest,ListTestCasesResponse> listTestCasesCallable()

Fetches a list of test cases for a given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListTestCasesRequest request =
           ListTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListTestCasesResponse response = testCasesClient.listTestCasesCallable().call(request);
         for (TestCase element : response.getTestCasesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCasesRequest),[ListTestCasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCasesResponse)>` |   
  
### listTestCasesPagedCallable()
    
    
    public final UnaryCallable<ListTestCasesRequest,TestCasesClient.ListTestCasesPagedResponse> listTestCasesPagedCallable()

Fetches a list of test cases for a given agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       ListTestCasesRequest request =
           ListTestCasesRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<TestCase> future = testCasesClient.listTestCasesPagedCallable().futureCall(request);
       // Do something.
       for (TestCase element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTestCasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTestCasesRequest),[ListTestCasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCasesClient.ListTestCasesPagedResponse)>` |   
  
### runTestCaseAsync(RunTestCaseRequest request)
    
    
    public final OperationFuture<RunTestCaseResponse,RunTestCaseMetadata> runTestCaseAsync(RunTestCaseRequest request)

Kicks off a test case run.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: RunTestCaseMetadata \- `response`: RunTestCaseResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       RunTestCaseRequest request =
           RunTestCaseRequest.newBuilder()
               .setName(
                   TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString())
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       RunTestCaseResponse response = testCasesClient.runTestCaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunTestCaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RunTestCaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunTestCaseResponse),[RunTestCaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunTestCaseMetadata)>` |   
  
### runTestCaseCallable()
    
    
    public final UnaryCallable<RunTestCaseRequest,Operation> runTestCaseCallable()

Kicks off a test case run.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: RunTestCaseMetadata \- `response`: RunTestCaseResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       RunTestCaseRequest request =
           RunTestCaseRequest.newBuilder()
               .setName(
                   TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString())
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       ApiFuture<Operation> future = testCasesClient.runTestCaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunTestCaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### runTestCaseOperationCallable()
    
    
    public final OperationCallable<RunTestCaseRequest,RunTestCaseResponse,RunTestCaseMetadata> runTestCaseOperationCallable()

Kicks off a test case run.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: RunTestCaseMetadata \- `response`: RunTestCaseResponse

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       RunTestCaseRequest request =
           RunTestCaseRequest.newBuilder()
               .setName(
                   TestCaseName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TEST_CASE]").toString())
               .setEnvironment(
                   EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                       .toString())
               .build();
       OperationFuture<RunTestCaseResponse, RunTestCaseMetadata> future =
           testCasesClient.runTestCaseOperationCallable().futureCall(request);
       // Do something.
       RunTestCaseResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RunTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunTestCaseRequest),[RunTestCaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunTestCaseResponse),[RunTestCaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RunTestCaseMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateTestCase(TestCase testCase, FieldMask updateMask)
    
    
    public final TestCase updateTestCase(TestCase testCase, FieldMask updateMask)

Updates the specified test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       TestCase testCase = TestCase.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TestCase response = testCasesClient.updateTestCase(testCase, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`testCase` | `[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)`  
Required. The test case to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The mask to specify which fields should be updated. The `creationTime` and `lastTestResult` cannot be updated.  
**Returns**  
---  
**Type** | **Description**  
`[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)` |   
  
### updateTestCase(UpdateTestCaseRequest request)
    
    
    public final TestCase updateTestCase(UpdateTestCaseRequest request)

Updates the specified test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       UpdateTestCaseRequest request =
           UpdateTestCaseRequest.newBuilder()
               .setTestCase(TestCase.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       TestCase response = testCasesClient.updateTestCase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateTestCaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)` |   
  
### updateTestCaseCallable()
    
    
    public final UnaryCallable<UpdateTestCaseRequest,TestCase> updateTestCaseCallable()

Updates the specified test case.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TestCasesClient testCasesClient = TestCasesClient.create()) {
       UpdateTestCaseRequest request =
           UpdateTestCaseRequest.newBuilder()
               .setTestCase(TestCase.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<TestCase> future = testCasesClient.updateTestCaseCallable().futureCall(request);
       // Do something.
       TestCase response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTestCaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateTestCaseRequest),[TestCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TestCase)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
