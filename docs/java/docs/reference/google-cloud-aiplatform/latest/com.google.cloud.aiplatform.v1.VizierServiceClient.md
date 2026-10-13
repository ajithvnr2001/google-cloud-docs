---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient
title: Class VizierServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:42.458674+00:00
---

# Class VizierServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VizierServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/VizierServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Vertex AI Vizier API.

Vertex AI Vizier is a service to solve blackbox optimization problems, such as tuning machine learning hyperparameters and searching over deep learning architectures.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Study study = Study.newBuilder().build();
       Study response = vizierServiceClient.createStudy(parent, study);
     }
     

Note: close() needs to be called on the VizierServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateStudy |  Creates a Study. A resource name will be generated after creation of the Study. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createStudy(CreateStudyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createStudy(LocationName parent, Study study) 
  * createStudy(String parent, Study study) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createStudyCallable() 

  
GetStudy |  Gets a Study by name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getStudy(GetStudyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getStudy(StudyName name) 
  * getStudy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getStudyCallable() 

  
ListStudies |  Lists all the studies in a region for an associated project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listStudies(ListStudiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listStudies(LocationName parent) 
  * listStudies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listStudiesPagedCallable() 
  * listStudiesCallable() 

  
DeleteStudy |  Deletes a Study. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteStudy(DeleteStudyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteStudy(StudyName name) 
  * deleteStudy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteStudyCallable() 

  
LookupStudy |  Looks a study up using the user-defined display_name field instead of the fully qualified resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * lookupStudy(LookupStudyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * lookupStudy(LocationName parent) 
  * lookupStudy(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * lookupStudyCallable() 

  
SuggestTrials |  Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier. Returns a long-running operation associated with the generation of Trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suggestTrialsAsync(SuggestTrialsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suggestTrialsOperationCallable() 
  * suggestTrialsCallable() 

  
CreateTrial |  Adds a user provided Trial to a Study. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTrial(CreateTrialRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTrial(StudyName parent, Trial trial) 
  * createTrial(String parent, Trial trial) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTrialCallable() 

  
GetTrial |  Gets a Trial. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTrial(GetTrialRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTrial(TrialName name) 
  * getTrial(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTrialCallable() 

  
ListTrials |  Lists the Trials associated with a Study. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTrials(ListTrialsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTrials(StudyName parent) 
  * listTrials(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTrialsPagedCallable() 
  * listTrialsCallable() 

  
AddTrialMeasurement |  Adds a measurement of the objective metrics to a Trial. This measurement is assumed to have been taken before the Trial is complete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addTrialMeasurement(AddTrialMeasurementRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addTrialMeasurementCallable() 

  
CompleteTrial |  Marks a Trial as complete. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeTrial(CompleteTrialRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeTrialCallable() 

  
DeleteTrial |  Deletes a Trial. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTrial(DeleteTrialRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteTrial(TrialName name) 
  * deleteTrial(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTrialCallable() 

  
CheckTrialEarlyStoppingState |  Checks whether a Trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * checkTrialEarlyStoppingStateAsync(CheckTrialEarlyStoppingStateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * checkTrialEarlyStoppingStateOperationCallable() 
  * checkTrialEarlyStoppingStateCallable() 

  
StopTrial |  Stops a Trial. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopTrial(StopTrialRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopTrialCallable() 

  
ListOptimalTrials |  Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. <https://en.wikipedia.org/wiki/Pareto_efficiency> |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listOptimalTrials(ListOptimalTrialsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listOptimalTrials(StudyName parent) 
  * listOptimalTrials(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listOptimalTrialsCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of VizierServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VizierServiceSettings vizierServiceSettings =
         VizierServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     VizierServiceClient vizierServiceClient = VizierServiceClient.create(vizierServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VizierServiceSettings vizierServiceSettings =
         VizierServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     VizierServiceClient vizierServiceClient = VizierServiceClient.create(vizierServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VizierServiceClient

## Static Methods 

### create()
    
    
    public static final VizierServiceClient create()

Constructs an instance of VizierServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VizierServiceSettings settings)
    
    
    public static final VizierServiceClient create(VizierServiceSettings settings)

Constructs an instance of VizierServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VizierServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VizierServiceStub stub)
    
    
    public static final VizierServiceClient create(VizierServiceStub stub)

Constructs an instance of VizierServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(VizierServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VizierServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VizierServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient)` |   
  
## Constructors 

### VizierServiceClient(VizierServiceSettings settings)
    
    
    protected VizierServiceClient(VizierServiceSettings settings)

Constructs an instance of VizierServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VizierServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceSettings)`  
  
  
### VizierServiceClient(VizierServiceStub stub)
    
    
    protected VizierServiceClient(VizierServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VizierServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VizierServiceStub)`  
  
  
## Methods 

### addTrialMeasurement(AddTrialMeasurementRequest request)
    
    
    public final Trial addTrialMeasurement(AddTrialMeasurementRequest request)

Adds a measurement of the objective metrics to a Trial. This measurement is assumed to have been taken before the Trial is complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       AddTrialMeasurementRequest request =
           AddTrialMeasurementRequest.newBuilder()
               .setTrialName(
                   TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .setMeasurement(Measurement.newBuilder().build())
               .build();
       Trial response = vizierServiceClient.addTrialMeasurement(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddTrialMeasurementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddTrialMeasurementRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### addTrialMeasurementCallable()
    
    
    public final UnaryCallable<AddTrialMeasurementRequest,Trial> addTrialMeasurementCallable()

Adds a measurement of the objective metrics to a Trial. This measurement is assumed to have been taken before the Trial is complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       AddTrialMeasurementRequest request =
           AddTrialMeasurementRequest.newBuilder()
               .setTrialName(
                   TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .setMeasurement(Measurement.newBuilder().build())
               .build();
       ApiFuture<Trial> future =
           vizierServiceClient.addTrialMeasurementCallable().futureCall(request);
       // Do something.
       Trial response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddTrialMeasurementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AddTrialMeasurementRequest),[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)>` |   
  
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
  
### checkTrialEarlyStoppingStateAsync(CheckTrialEarlyStoppingStateRequest request)
    
    
    public final OperationFuture<CheckTrialEarlyStoppingStateResponse,CheckTrialEarlyStoppingStateMetatdata> checkTrialEarlyStoppingStateAsync(CheckTrialEarlyStoppingStateRequest request)

Checks whether a Trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CheckTrialEarlyStoppingStateRequest request =
           CheckTrialEarlyStoppingStateRequest.newBuilder()
               .setTrialName(
                   TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       CheckTrialEarlyStoppingStateResponse response =
           vizierServiceClient.checkTrialEarlyStoppingStateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CheckTrialEarlyStoppingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CheckTrialEarlyStoppingStateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateResponse),[CheckTrialEarlyStoppingStateMetatdata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateMetatdata)>` |   
  
### checkTrialEarlyStoppingStateCallable()
    
    
    public final UnaryCallable<CheckTrialEarlyStoppingStateRequest,Operation> checkTrialEarlyStoppingStateCallable()

Checks whether a Trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CheckTrialEarlyStoppingStateRequest request =
           CheckTrialEarlyStoppingStateRequest.newBuilder()
               .setTrialName(
                   TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       ApiFuture<Operation> future =
           vizierServiceClient.checkTrialEarlyStoppingStateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CheckTrialEarlyStoppingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### checkTrialEarlyStoppingStateOperationCallable()
    
    
    public final OperationCallable<CheckTrialEarlyStoppingStateRequest,CheckTrialEarlyStoppingStateResponse,CheckTrialEarlyStoppingStateMetatdata> checkTrialEarlyStoppingStateOperationCallable()

Checks whether a Trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CheckTrialEarlyStoppingStateRequest request =
           CheckTrialEarlyStoppingStateRequest.newBuilder()
               .setTrialName(
                   TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       OperationFuture<CheckTrialEarlyStoppingStateResponse, CheckTrialEarlyStoppingStateMetatdata>
           future =
               vizierServiceClient
                   .checkTrialEarlyStoppingStateOperationCallable()
                   .futureCall(request);
       // Do something.
       CheckTrialEarlyStoppingStateResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CheckTrialEarlyStoppingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateRequest),[CheckTrialEarlyStoppingStateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateResponse),[CheckTrialEarlyStoppingStateMetatdata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CheckTrialEarlyStoppingStateMetatdata)>` |   
  
### close()
    
    
    public final void close()

### completeTrial(CompleteTrialRequest request)
    
    
    public final Trial completeTrial(CompleteTrialRequest request)

Marks a Trial as complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CompleteTrialRequest request =
           CompleteTrialRequest.newBuilder()
               .setName(TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .setFinalMeasurement(Measurement.newBuilder().build())
               .setTrialInfeasible(true)
               .setInfeasibleReason("infeasibleReason1040725388")
               .build();
       Trial response = vizierServiceClient.completeTrial(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CompleteTrialRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### completeTrialCallable()
    
    
    public final UnaryCallable<CompleteTrialRequest,Trial> completeTrialCallable()

Marks a Trial as complete.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CompleteTrialRequest request =
           CompleteTrialRequest.newBuilder()
               .setName(TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .setFinalMeasurement(Measurement.newBuilder().build())
               .setTrialInfeasible(true)
               .setInfeasibleReason("infeasibleReason1040725388")
               .build();
       ApiFuture<Trial> future = vizierServiceClient.completeTrialCallable().futureCall(request);
       // Do something.
       Trial response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CompleteTrialRequest),[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)>` |   
  
### createStudy(@Nullable LocationName parent, Study study)
    
    
    public final Study createStudy(@Nullable LocationName parent, Study study)

Creates a Study. A resource name will be generated after creation of the Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Study study = Study.newBuilder().build();
       Study response = vizierServiceClient.createStudy(parent, study);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the CustomJob in. Format: `projects/{project}/locations/{location}`  
`study` | `[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)`  
Required. The Study configuration used to create the Study.  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### createStudy(CreateStudyRequest request)
    
    
    public final Study createStudy(CreateStudyRequest request)

Creates a Study. A resource name will be generated after creation of the Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CreateStudyRequest request =
           CreateStudyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setStudy(Study.newBuilder().build())
               .build();
       Study response = vizierServiceClient.createStudy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateStudyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateStudyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### createStudy(String parent, Study study)
    
    
    public final Study createStudy(String parent, Study study)

Creates a Study. A resource name will be generated after creation of the Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Study study = Study.newBuilder().build();
       Study response = vizierServiceClient.createStudy(parent, study);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the CustomJob in. Format: `projects/{project}/locations/{location}`  
`study` | `[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)`  
Required. The Study configuration used to create the Study.  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### createStudyCallable()
    
    
    public final UnaryCallable<CreateStudyRequest,Study> createStudyCallable()

Creates a Study. A resource name will be generated after creation of the Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CreateStudyRequest request =
           CreateStudyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setStudy(Study.newBuilder().build())
               .build();
       ApiFuture<Study> future = vizierServiceClient.createStudyCallable().futureCall(request);
       // Do something.
       Study response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateStudyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateStudyRequest),[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)>` |   
  
### createTrial(@Nullable StudyName parent, Trial trial)
    
    
    public final Trial createTrial(@Nullable StudyName parent, Trial trial)

Adds a user provided Trial to a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       StudyName parent = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]");
       Trial trial = Trial.newBuilder().build();
       Trial response = vizierServiceClient.createTrial(parent, trial);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.StudyName`  
Required. The resource name of the Study to create the Trial in. Format: `projects/{project}/locations/{location}/studies/{study}`  
`trial` | `[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)`  
Required. The Trial to create.  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### createTrial(CreateTrialRequest request)
    
    
    public final Trial createTrial(CreateTrialRequest request)

Adds a user provided Trial to a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CreateTrialRequest request =
           CreateTrialRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .setTrial(Trial.newBuilder().build())
               .build();
       Trial response = vizierServiceClient.createTrial(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTrialRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### createTrial(String parent, Trial trial)
    
    
    public final Trial createTrial(String parent, Trial trial)

Adds a user provided Trial to a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String parent = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString();
       Trial trial = Trial.newBuilder().build();
       Trial response = vizierServiceClient.createTrial(parent, trial);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Study to create the Trial in. Format: `projects/{project}/locations/{location}/studies/{study}`  
`trial` | `[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)`  
Required. The Trial to create.  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### createTrialCallable()
    
    
    public final UnaryCallable<CreateTrialRequest,Trial> createTrialCallable()

Adds a user provided Trial to a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       CreateTrialRequest request =
           CreateTrialRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .setTrial(Trial.newBuilder().build())
               .build();
       ApiFuture<Trial> future = vizierServiceClient.createTrialCallable().futureCall(request);
       // Do something.
       Trial response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTrialRequest),[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)>` |   
  
### deleteStudy(@Nullable StudyName name)
    
    
    public final void deleteStudy(@Nullable StudyName name)

Deletes a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       StudyName name = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]");
       vizierServiceClient.deleteStudy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.StudyName`  
Required. The name of the Study resource to be deleted. Format: `projects/{project}/locations/{location}/studies/{study}`  
  
### deleteStudy(DeleteStudyRequest request)
    
    
    public final void deleteStudy(DeleteStudyRequest request)

Deletes a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       DeleteStudyRequest request =
           DeleteStudyRequest.newBuilder()
               .setName(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .build();
       vizierServiceClient.deleteStudy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteStudyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteStudyRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteStudy(String name)
    
    
    public final void deleteStudy(String name)

Deletes a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String name = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString();
       vizierServiceClient.deleteStudy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Study resource to be deleted. Format: `projects/{project}/locations/{location}/studies/{study}`  
  
### deleteStudyCallable()
    
    
    public final UnaryCallable<DeleteStudyRequest,Empty> deleteStudyCallable()

Deletes a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       DeleteStudyRequest request =
           DeleteStudyRequest.newBuilder()
               .setName(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .build();
       ApiFuture<Empty> future = vizierServiceClient.deleteStudyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteStudyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteStudyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTrial(@Nullable TrialName name)
    
    
    public final void deleteTrial(@Nullable TrialName name)

Deletes a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       TrialName name = TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]");
       vizierServiceClient.deleteTrial(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TrialName`  
Required. The Trial's name. Format: `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`  
  
### deleteTrial(DeleteTrialRequest request)
    
    
    public final void deleteTrial(DeleteTrialRequest request)

Deletes a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       DeleteTrialRequest request =
           DeleteTrialRequest.newBuilder()
               .setName(TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       vizierServiceClient.deleteTrial(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTrialRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteTrial(String name)
    
    
    public final void deleteTrial(String name)

Deletes a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String name = TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString();
       vizierServiceClient.deleteTrial(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Trial's name. Format: `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`  
  
### deleteTrialCallable()
    
    
    public final UnaryCallable<DeleteTrialRequest,Empty> deleteTrialCallable()

Deletes a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       DeleteTrialRequest request =
           DeleteTrialRequest.newBuilder()
               .setName(TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       ApiFuture<Empty> future = vizierServiceClient.deleteTrialCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTrialRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = vizierServiceClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = vizierServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = vizierServiceClient.getLocation(request);
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
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = vizierServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable VizierServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.VizierServiceSettings` |   
  
### getStub()
    
    
    public VizierServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[VizierServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.VizierServiceStub)` |   
  
### getStudy(@Nullable StudyName name)
    
    
    public final Study getStudy(@Nullable StudyName name)

Gets a Study by name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       StudyName name = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]");
       Study response = vizierServiceClient.getStudy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.StudyName`  
Required. The name of the Study resource. Format: `projects/{project}/locations/{location}/studies/{study}`  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### getStudy(GetStudyRequest request)
    
    
    public final Study getStudy(GetStudyRequest request)

Gets a Study by name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       GetStudyRequest request =
           GetStudyRequest.newBuilder()
               .setName(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .build();
       Study response = vizierServiceClient.getStudy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStudyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetStudyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### getStudy(String name)
    
    
    public final Study getStudy(String name)

Gets a Study by name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String name = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString();
       Study response = vizierServiceClient.getStudy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Study resource. Format: `projects/{project}/locations/{location}/studies/{study}`  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### getStudyCallable()
    
    
    public final UnaryCallable<GetStudyRequest,Study> getStudyCallable()

Gets a Study by name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       GetStudyRequest request =
           GetStudyRequest.newBuilder()
               .setName(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .build();
       ApiFuture<Study> future = vizierServiceClient.getStudyCallable().futureCall(request);
       // Do something.
       Study response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetStudyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetStudyRequest),[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)>` |   
  
### getTrial(@Nullable TrialName name)
    
    
    public final Trial getTrial(@Nullable TrialName name)

Gets a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       TrialName name = TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]");
       Trial response = vizierServiceClient.getTrial(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TrialName`  
Required. The name of the Trial resource. Format: `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### getTrial(GetTrialRequest request)
    
    
    public final Trial getTrial(GetTrialRequest request)

Gets a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       GetTrialRequest request =
           GetTrialRequest.newBuilder()
               .setName(TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       Trial response = vizierServiceClient.getTrial(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTrialRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### getTrial(String name)
    
    
    public final Trial getTrial(String name)

Gets a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String name = TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString();
       Trial response = vizierServiceClient.getTrial(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Trial resource. Format: `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### getTrialCallable()
    
    
    public final UnaryCallable<GetTrialRequest,Trial> getTrialCallable()

Gets a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       GetTrialRequest request =
           GetTrialRequest.newBuilder()
               .setName(TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       ApiFuture<Trial> future = vizierServiceClient.getTrialCallable().futureCall(request);
       // Do something.
       Trial response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTrialRequest),[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)>` |   
  
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
    
    
    public final VizierServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : vizierServiceClient.listLocations(request).iterateAll()) {
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
`[VizierServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = vizierServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,VizierServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           vizierServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListLocationsPagedResponse)>` |   
  
### listOptimalTrials(@Nullable StudyName parent)
    
    
    public final ListOptimalTrialsResponse listOptimalTrials(@Nullable StudyName parent)

Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. <https://en.wikipedia.org/wiki/Pareto_efficiency>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       StudyName parent = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]");
       ListOptimalTrialsResponse response = vizierServiceClient.listOptimalTrials(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.StudyName`  
Required. The name of the Study that the optimal Trial belongs to.  
**Returns**  
---  
**Type** | **Description**  
`[ListOptimalTrialsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListOptimalTrialsResponse)` |   
  
### listOptimalTrials(ListOptimalTrialsRequest request)
    
    
    public final ListOptimalTrialsResponse listOptimalTrials(ListOptimalTrialsRequest request)

Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. <https://en.wikipedia.org/wiki/Pareto_efficiency>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListOptimalTrialsRequest request =
           ListOptimalTrialsRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .build();
       ListOptimalTrialsResponse response = vizierServiceClient.listOptimalTrials(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOptimalTrialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListOptimalTrialsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListOptimalTrialsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListOptimalTrialsResponse)` |   
  
### listOptimalTrials(String parent)
    
    
    public final ListOptimalTrialsResponse listOptimalTrials(String parent)

Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. <https://en.wikipedia.org/wiki/Pareto_efficiency>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String parent = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString();
       ListOptimalTrialsResponse response = vizierServiceClient.listOptimalTrials(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Study that the optimal Trial belongs to.  
**Returns**  
---  
**Type** | **Description**  
`[ListOptimalTrialsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListOptimalTrialsResponse)` |   
  
### listOptimalTrialsCallable()
    
    
    public final UnaryCallable<ListOptimalTrialsRequest,ListOptimalTrialsResponse> listOptimalTrialsCallable()

Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. <https://en.wikipedia.org/wiki/Pareto_efficiency>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListOptimalTrialsRequest request =
           ListOptimalTrialsRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .build();
       ApiFuture<ListOptimalTrialsResponse> future =
           vizierServiceClient.listOptimalTrialsCallable().futureCall(request);
       // Do something.
       ListOptimalTrialsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOptimalTrialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListOptimalTrialsRequest),[ListOptimalTrialsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListOptimalTrialsResponse)>` |   
  
### listStudies(@Nullable LocationName parent)
    
    
    public final VizierServiceClient.ListStudiesPagedResponse listStudies(@Nullable LocationName parent)

Lists all the studies in a region for an associated project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Study element : vizierServiceClient.listStudies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the Study from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient.ListStudiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListStudiesPagedResponse)` |   
  
### listStudies(ListStudiesRequest request)
    
    
    public final VizierServiceClient.ListStudiesPagedResponse listStudies(ListStudiesRequest request)

Lists all the studies in a region for an associated project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListStudiesRequest request =
           ListStudiesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (Study element : vizierServiceClient.listStudies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStudiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListStudiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient.ListStudiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListStudiesPagedResponse)` |   
  
### listStudies(String parent)
    
    
    public final VizierServiceClient.ListStudiesPagedResponse listStudies(String parent)

Lists all the studies in a region for an associated project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Study element : vizierServiceClient.listStudies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the Study from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient.ListStudiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListStudiesPagedResponse)` |   
  
### listStudiesCallable()
    
    
    public final UnaryCallable<ListStudiesRequest,ListStudiesResponse> listStudiesCallable()

Lists all the studies in a region for an associated project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListStudiesRequest request =
           ListStudiesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListStudiesResponse response = vizierServiceClient.listStudiesCallable().call(request);
         for (Study element : response.getStudiesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStudiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListStudiesRequest),[ListStudiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListStudiesResponse)>` |   
  
### listStudiesPagedCallable()
    
    
    public final UnaryCallable<ListStudiesRequest,VizierServiceClient.ListStudiesPagedResponse> listStudiesPagedCallable()

Lists all the studies in a region for an associated project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListStudiesRequest request =
           ListStudiesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<Study> future = vizierServiceClient.listStudiesPagedCallable().futureCall(request);
       // Do something.
       for (Study element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStudiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListStudiesRequest),[ListStudiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListStudiesPagedResponse)>` |   
  
### listTrials(@Nullable StudyName parent)
    
    
    public final VizierServiceClient.ListTrialsPagedResponse listTrials(@Nullable StudyName parent)

Lists the Trials associated with a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       StudyName parent = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]");
       for (Trial element : vizierServiceClient.listTrials(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.StudyName`  
Required. The resource name of the Study to list the Trial from. Format: `projects/{project}/locations/{location}/studies/{study}`  
**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient.ListTrialsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListTrialsPagedResponse)` |   
  
### listTrials(ListTrialsRequest request)
    
    
    public final VizierServiceClient.ListTrialsPagedResponse listTrials(ListTrialsRequest request)

Lists the Trials associated with a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListTrialsRequest request =
           ListTrialsRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (Trial element : vizierServiceClient.listTrials(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTrialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrialsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient.ListTrialsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListTrialsPagedResponse)` |   
  
### listTrials(String parent)
    
    
    public final VizierServiceClient.ListTrialsPagedResponse listTrials(String parent)

Lists the Trials associated with a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String parent = StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString();
       for (Trial element : vizierServiceClient.listTrials(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Study to list the Trial from. Format: `projects/{project}/locations/{location}/studies/{study}`  
**Returns**  
---  
**Type** | **Description**  
`[VizierServiceClient.ListTrialsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListTrialsPagedResponse)` |   
  
### listTrialsCallable()
    
    
    public final UnaryCallable<ListTrialsRequest,ListTrialsResponse> listTrialsCallable()

Lists the Trials associated with a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListTrialsRequest request =
           ListTrialsRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListTrialsResponse response = vizierServiceClient.listTrialsCallable().call(request);
         for (Trial element : response.getTrialsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTrialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrialsRequest),[ListTrialsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrialsResponse)>` |   
  
### listTrialsPagedCallable()
    
    
    public final UnaryCallable<ListTrialsRequest,VizierServiceClient.ListTrialsPagedResponse> listTrialsPagedCallable()

Lists the Trials associated with a Study.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       ListTrialsRequest request =
           ListTrialsRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<Trial> future = vizierServiceClient.listTrialsPagedCallable().futureCall(request);
       // Do something.
       for (Trial element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTrialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrialsRequest),[ListTrialsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.VizierServiceClient.ListTrialsPagedResponse)>` |   
  
### lookupStudy(@Nullable LocationName parent)
    
    
    public final Study lookupStudy(@Nullable LocationName parent)

Looks a study up using the user-defined display_name field instead of the fully qualified resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Study response = vizierServiceClient.lookupStudy(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to get the Study from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### lookupStudy(LookupStudyRequest request)
    
    
    public final Study lookupStudy(LookupStudyRequest request)

Looks a study up using the user-defined display_name field instead of the fully qualified resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       LookupStudyRequest request =
           LookupStudyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDisplayName("displayName1714148973")
               .build();
       Study response = vizierServiceClient.lookupStudy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[LookupStudyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LookupStudyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### lookupStudy(String parent)
    
    
    public final Study lookupStudy(String parent)

Looks a study up using the user-defined display_name field instead of the fully qualified resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Study response = vizierServiceClient.lookupStudy(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to get the Study from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)` |   
  
### lookupStudyCallable()
    
    
    public final UnaryCallable<LookupStudyRequest,Study> lookupStudyCallable()

Looks a study up using the user-defined display_name field instead of the fully qualified resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       LookupStudyRequest request =
           LookupStudyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDisplayName("displayName1714148973")
               .build();
       ApiFuture<Study> future = vizierServiceClient.lookupStudyCallable().futureCall(request);
       // Do something.
       Study response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[LookupStudyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LookupStudyRequest),[Study](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Study)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = vizierServiceClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = vizierServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### stopTrial(StopTrialRequest request)
    
    
    public final Trial stopTrial(StopTrialRequest request)

Stops a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       StopTrialRequest request =
           StopTrialRequest.newBuilder()
               .setName(TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       Trial response = vizierServiceClient.stopTrial(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopTrialRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### stopTrialCallable()
    
    
    public final UnaryCallable<StopTrialRequest,Trial> stopTrialCallable()

Stops a Trial.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       StopTrialRequest request =
           StopTrialRequest.newBuilder()
               .setName(TrialName.of("[PROJECT]", "[LOCATION]", "[STUDY]", "[TRIAL]").toString())
               .build();
       ApiFuture<Trial> future = vizierServiceClient.stopTrialCallable().futureCall(request);
       // Do something.
       Trial response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopTrialRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopTrialRequest),[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)>` |   
  
### suggestTrialsAsync(SuggestTrialsRequest request)
    
    
    public final OperationFuture<SuggestTrialsResponse,SuggestTrialsMetadata> suggestTrialsAsync(SuggestTrialsRequest request)

Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier. Returns a long-running operation associated with the generation of Trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       SuggestTrialsRequest request =
           SuggestTrialsRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .setSuggestionCount(390130452)
               .setClientId("clientId908408390")
               .addAllContexts(new ArrayList<TrialContext>())
               .build();
       SuggestTrialsResponse response = vizierServiceClient.suggestTrialsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuggestTrialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SuggestTrialsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SuggestTrialsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SuggestTrialsResponse),[SuggestTrialsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SuggestTrialsMetadata)>` |   
  
### suggestTrialsCallable()
    
    
    public final UnaryCallable<SuggestTrialsRequest,Operation> suggestTrialsCallable()

Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier. Returns a long-running operation associated with the generation of Trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       SuggestTrialsRequest request =
           SuggestTrialsRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .setSuggestionCount(390130452)
               .setClientId("clientId908408390")
               .addAllContexts(new ArrayList<TrialContext>())
               .build();
       ApiFuture<Operation> future = vizierServiceClient.suggestTrialsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuggestTrialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SuggestTrialsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### suggestTrialsOperationCallable()
    
    
    public final OperationCallable<SuggestTrialsRequest,SuggestTrialsResponse,SuggestTrialsMetadata> suggestTrialsOperationCallable()

Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier. Returns a long-running operation associated with the generation of Trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       SuggestTrialsRequest request =
           SuggestTrialsRequest.newBuilder()
               .setParent(StudyName.of("[PROJECT]", "[LOCATION]", "[STUDY]").toString())
               .setSuggestionCount(390130452)
               .setClientId("clientId908408390")
               .addAllContexts(new ArrayList<TrialContext>())
               .build();
       OperationFuture<SuggestTrialsResponse, SuggestTrialsMetadata> future =
           vizierServiceClient.suggestTrialsOperationCallable().futureCall(request);
       // Do something.
       SuggestTrialsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SuggestTrialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SuggestTrialsRequest),[SuggestTrialsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SuggestTrialsResponse),[SuggestTrialsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SuggestTrialsMetadata)>` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = vizierServiceClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VizierServiceClient vizierServiceClient = VizierServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           vizierServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
