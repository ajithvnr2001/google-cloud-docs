---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient
title: Class ConfigClient (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:11.364424+00:00
---

# Class ConfigClient (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConfigClient (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-logging/google-cloud-logging/src/main/java/com/google/cloud/logging/v2/ConfigClient.java)| [Product Reference](https://cloud.google.com/logging/docs)  
---|---  
  
Service Description: Service for configuring sinks used to route log entries.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetBucketRequest request =
           GetBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .build();
       LogBucket response = configClient.getBucket(request);
     }
     

Note: close() needs to be called on the ConfigClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListBuckets |  Lists log buckets. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBuckets(ListBucketsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBuckets(BillingAccountLocationName parent) 
  * listBuckets(FolderLocationName parent) 
  * listBuckets(LocationName parent) 
  * listBuckets(OrganizationLocationName parent) 
  * listBuckets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBucketsPagedCallable() 
  * listBucketsCallable() 

  
GetBucket |  Gets a log bucket. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBucket(GetBucketRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBucketCallable() 

  
CreateBucketAsync |  Creates a log bucket asynchronously that can be used to store log entries.  After a bucket has been created, the bucket's location cannot be changed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBucketAsyncAsync(CreateBucketRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBucketAsyncOperationCallable() 
  * createBucketAsyncCallable() 

  
UpdateBucketAsync |  Updates a log bucket asynchronously.  If the bucket has a `lifecycle_state` of `DELETE_REQUESTED`, then `FAILED_PRECONDITION` will be returned.  After a bucket has been created, the bucket's location cannot be changed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBucketAsyncAsync(UpdateBucketRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBucketAsyncOperationCallable() 
  * updateBucketAsyncCallable() 

  
CreateBucket |  Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBucket(CreateBucketRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBucketCallable() 

  
UpdateBucket |  Updates a log bucket.  If the bucket has a `lifecycle_state` of `DELETE_REQUESTED`, then `FAILED_PRECONDITION` will be returned.  After a bucket has been created, the bucket's location cannot be changed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBucket(UpdateBucketRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBucketCallable() 

  
DeleteBucket |  Deletes a log bucket.  Changes the bucket's `lifecycle_state` to the `DELETE_REQUESTED` state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBucket(DeleteBucketRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBucketCallable() 

  
UndeleteBucket |  Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeleteBucket(UndeleteBucketRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeleteBucketCallable() 

  
ListViews |  Lists views on a log bucket. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listViews(ListViewsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listViews(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listViewsPagedCallable() 
  * listViewsCallable() 

  
GetView |  Gets a view on a log bucket.. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getView(GetViewRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getViewCallable() 

  
CreateView |  Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createView(CreateViewRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createViewCallable() 

  
UpdateView |  Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: `filter`. If an `UNAVAILABLE` error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateView(UpdateViewRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateViewCallable() 

  
DeleteView |  Deletes a view on a log bucket. If an `UNAVAILABLE` error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteView(DeleteViewRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteViewCallable() 

  
ListSinks |  Lists sinks. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSinks(ListSinksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSinks(BillingAccountName parent) 
  * listSinks(FolderName parent) 
  * listSinks(OrganizationName parent) 
  * listSinks(ProjectName parent) 
  * listSinks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSinksPagedCallable() 
  * listSinksCallable() 

  
GetSink |  Gets a sink. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSink(GetSinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSink(LogSinkName sinkName) 
  * getSink(String sinkName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSinkCallable() 

  
CreateSink |  Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSink(CreateSinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSink(BillingAccountName parent, LogSink sink) 
  * createSink(FolderName parent, LogSink sink) 
  * createSink(OrganizationName parent, LogSink sink) 
  * createSink(ProjectName parent, LogSink sink) 
  * createSink(String parent, LogSink sink) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSinkCallable() 

  
UpdateSink |  Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: `destination`, and `filter`.  The updated sink might also have a new `writer_identity`; see the `unique_writer_identity` field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSink(UpdateSinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSink(LogSinkName sinkName, LogSink sink) 
  * updateSink(String sinkName, LogSink sink) 
  * updateSink(LogSinkName sinkName, LogSink sink, FieldMask updateMask) 
  * updateSink(String sinkName, LogSink sink, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSinkCallable() 

  
DeleteSink |  Deletes a sink. If the sink has a unique `writer_identity`, then that service account is also deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSink(DeleteSinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSink(LogSinkName sinkName) 
  * deleteSink(String sinkName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSinkCallable() 

  
CreateLink |  Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLinkAsync(CreateLinkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createLinkAsync(LogBucketName parent, Link link, String linkId) 
  * createLinkAsync(String parent, Link link, String linkId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLinkOperationCallable() 
  * createLinkCallable() 

  
DeleteLink |  Deletes a link. This will also delete the corresponding BigQuery linked dataset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLinkAsync(DeleteLinkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteLinkAsync(LinkName name) 
  * deleteLinkAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLinkOperationCallable() 
  * deleteLinkCallable() 

  
ListLinks |  Lists links. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLinks(ListLinksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLinks(LogBucketName parent) 
  * listLinks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLinksPagedCallable() 
  * listLinksCallable() 

  
GetLink |  Gets a link. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLink(GetLinkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLink(LinkName name) 
  * getLink(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLinkCallable() 

  
ListExclusions |  Lists all the exclusions on the _Default sink in a parent resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExclusions(ListExclusionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExclusions(BillingAccountName parent) 
  * listExclusions(FolderName parent) 
  * listExclusions(OrganizationName parent) 
  * listExclusions(ProjectName parent) 
  * listExclusions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExclusionsPagedCallable() 
  * listExclusionsCallable() 

  
GetExclusion |  Gets the description of an exclusion in the _Default sink. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExclusion(GetExclusionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExclusion(LogExclusionName name) 
  * getExclusion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExclusionCallable() 

  
CreateExclusion |  Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createExclusion(CreateExclusionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createExclusion(BillingAccountName parent, LogExclusion exclusion) 
  * createExclusion(FolderName parent, LogExclusion exclusion) 
  * createExclusion(OrganizationName parent, LogExclusion exclusion) 
  * createExclusion(ProjectName parent, LogExclusion exclusion) 
  * createExclusion(String parent, LogExclusion exclusion) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createExclusionCallable() 

  
UpdateExclusion |  Changes one or more properties of an existing exclusion in the _Default sink. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExclusion(UpdateExclusionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateExclusion(LogExclusionName name, LogExclusion exclusion, FieldMask updateMask) 
  * updateExclusion(String name, LogExclusion exclusion, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExclusionCallable() 

  
DeleteExclusion |  Deletes an exclusion in the _Default sink. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExclusion(DeleteExclusionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteExclusion(LogExclusionName name) 
  * deleteExclusion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExclusionCallable() 

  
GetCmekSettings |  Gets the Logging CMEK settings for the given resource.  Note: CMEK for the Log Router can be configured for Google Cloud projects, folders, organizations and billing accounts. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.  See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCmekSettings(GetCmekSettingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCmekSettingsCallable() 

  
UpdateCmekSettings |  Updates the Log Router CMEK settings for the given resource.  Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.  UpdateCmekSettings will fail if 1) `kms_key_name` is invalid, or 2) the associated service account does not have the required `roles/cloudkms.cryptoKeyEncrypterDecrypter` role assigned for the key, or 3) access to the key is disabled.  See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCmekSettings(UpdateCmekSettingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCmekSettingsCallable() 

  
GetSettings |  Gets the Log Router settings for the given resource.  Note: Settings for the Log Router can be get for Google Cloud projects, folders, organizations and billing accounts. Currently it can only be configured for organizations. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.  See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSettings(GetSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSettings(SettingsName name) 
  * getSettings(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSettingsCallable() 

  
UpdateSettings |  Updates the Log Router settings for the given resource.  Note: Settings for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.  UpdateSettings will fail if 1) `kms_key_name` is invalid, or 2) the associated service account does not have the required `roles/cloudkms.cryptoKeyEncrypterDecrypter` role assigned for the key, or 3) access to the key is disabled. 4) `location_id` is not supported by Logging. 5) `location_id` violate OrgPolicy.  See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSettings(UpdateSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSettings(Settings settings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSettingsCallable() 

  
CopyLogEntries |  Copies a set of log entries from a log bucket to a Cloud Storage bucket. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * copyLogEntriesAsync(CopyLogEntriesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * copyLogEntriesOperationCallable() 
  * copyLogEntriesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ConfigSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConfigSettings configSettings =
         ConfigSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConfigClient configClient = ConfigClient.create(configSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConfigSettings configSettings = ConfigSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConfigClient configClient = ConfigClient.create(configSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConfigClient

## Static Methods 

### create()
    
    
    public static final ConfigClient create()

Constructs an instance of ConfigClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConfigClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConfigSettings settings)
    
    
    public static final ConfigClient create(ConfigSettings settings)

Constructs an instance of ConfigClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConfigSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConfigServiceV2Stub stub)
    
    
    public static final ConfigClient create(ConfigServiceV2Stub stub)

Constructs an instance of ConfigClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConfigSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConfigServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.ConfigServiceV2Stub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient)` |   
  
## Constructors 

### ConfigClient(ConfigSettings settings)
    
    
    protected ConfigClient(ConfigSettings settings)

Constructs an instance of ConfigClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConfigSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings)`  
  
  
### ConfigClient(ConfigServiceV2Stub stub)
    
    
    protected ConfigClient(ConfigServiceV2Stub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConfigServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.ConfigServiceV2Stub)`  
  
  
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

### copyLogEntriesAsync(CopyLogEntriesRequest request)
    
    
    public final OperationFuture<CopyLogEntriesResponse,CopyLogEntriesMetadata> copyLogEntriesAsync(CopyLogEntriesRequest request)

Copies a set of log entries from a log bucket to a Cloud Storage bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CopyLogEntriesRequest request =
           CopyLogEntriesRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setDestination("destination-1429847026")
               .build();
       CopyLogEntriesResponse response = configClient.copyLogEntriesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CopyLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CopyLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesResponse),[CopyLogEntriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesMetadata)>` |   
  
### copyLogEntriesCallable()
    
    
    public final UnaryCallable<CopyLogEntriesRequest,Operation> copyLogEntriesCallable()

Copies a set of log entries from a log bucket to a Cloud Storage bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CopyLogEntriesRequest request =
           CopyLogEntriesRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setDestination("destination-1429847026")
               .build();
       ApiFuture<Operation> future = configClient.copyLogEntriesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CopyLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### copyLogEntriesOperationCallable()
    
    
    public final OperationCallable<CopyLogEntriesRequest,CopyLogEntriesResponse,CopyLogEntriesMetadata> copyLogEntriesOperationCallable()

Copies a set of log entries from a log bucket to a Cloud Storage bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CopyLogEntriesRequest request =
           CopyLogEntriesRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setDestination("destination-1429847026")
               .build();
       OperationFuture<CopyLogEntriesResponse, CopyLogEntriesMetadata> future =
           configClient.copyLogEntriesOperationCallable().futureCall(request);
       // Do something.
       CopyLogEntriesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CopyLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesRequest),[CopyLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesResponse),[CopyLogEntriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesMetadata)>` |   
  
### createBucket(CreateBucketRequest request)
    
    
    public final LogBucket createBucket(CreateBucketRequest request)

Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateBucketRequest request =
           CreateBucketRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBucketId("bucketId-1603305307")
               .setBucket(LogBucket.newBuilder().build())
               .build();
       LogBucket response = configClient.createBucket(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)` |   
  
### createBucketAsyncAsync(CreateBucketRequest request)
    
    
    public final OperationFuture<LogBucket,BucketMetadata> createBucketAsyncAsync(CreateBucketRequest request)

Creates a log bucket asynchronously that can be used to store log entries.

After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateBucketRequest request =
           CreateBucketRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBucketId("bucketId-1603305307")
               .setBucket(LogBucket.newBuilder().build())
               .build();
       LogBucket response = configClient.createBucketAsyncAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket),[BucketMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.BucketMetadata)>` |   
  
### createBucketAsyncCallable()
    
    
    public final UnaryCallable<CreateBucketRequest,Operation> createBucketAsyncCallable()

Creates a log bucket asynchronously that can be used to store log entries.

After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateBucketRequest request =
           CreateBucketRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBucketId("bucketId-1603305307")
               .setBucket(LogBucket.newBuilder().build())
               .build();
       ApiFuture<Operation> future = configClient.createBucketAsyncCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBucketAsyncOperationCallable()
    
    
    public final OperationCallable<CreateBucketRequest,LogBucket,BucketMetadata> createBucketAsyncOperationCallable()

Creates a log bucket asynchronously that can be used to store log entries.

After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateBucketRequest request =
           CreateBucketRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBucketId("bucketId-1603305307")
               .setBucket(LogBucket.newBuilder().build())
               .build();
       OperationFuture<LogBucket, BucketMetadata> future =
           configClient.createBucketAsyncOperationCallable().futureCall(request);
       // Do something.
       LogBucket response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket),[BucketMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.BucketMetadata)>` |   
  
### createBucketCallable()
    
    
    public final UnaryCallable<CreateBucketRequest,LogBucket> createBucketCallable()

Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateBucketRequest request =
           CreateBucketRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBucketId("bucketId-1603305307")
               .setBucket(LogBucket.newBuilder().build())
               .build();
       ApiFuture<LogBucket> future = configClient.createBucketCallable().futureCall(request);
       // Do something.
       LogBucket response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)>` |   
  
### createExclusion(@Nullable BillingAccountName parent, LogExclusion exclusion)
    
    
    public final LogExclusion createExclusion(@Nullable BillingAccountName parent, LogExclusion exclusion)

Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       BillingAccountName parent = BillingAccountName.of("[BILLING_ACCOUNT]");
       LogExclusion exclusion = LogExclusion.newBuilder().build();
       LogExclusion response = configClient.createExclusion(parent, exclusion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.BillingAccountName`  
Required. The parent resource in which to create the exclusion: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-logging-project"` `"organizations/123456789"`  
`exclusion` | `[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)`  
Required. The new exclusion, whose `name` parameter is an exclusion name that is not already used in the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### createExclusion(@Nullable FolderName parent, LogExclusion exclusion)
    
    
    public final LogExclusion createExclusion(@Nullable FolderName parent, LogExclusion exclusion)

Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       LogExclusion exclusion = LogExclusion.newBuilder().build();
       LogExclusion response = configClient.createExclusion(parent, exclusion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.FolderName`  
Required. The parent resource in which to create the exclusion: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-logging-project"` `"organizations/123456789"`  
`exclusion` | `[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)`  
Required. The new exclusion, whose `name` parameter is an exclusion name that is not already used in the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### createExclusion(@Nullable OrganizationName parent, LogExclusion exclusion)
    
    
    public final LogExclusion createExclusion(@Nullable OrganizationName parent, LogExclusion exclusion)

Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       LogExclusion exclusion = LogExclusion.newBuilder().build();
       LogExclusion response = configClient.createExclusion(parent, exclusion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.OrganizationName`  
Required. The parent resource in which to create the exclusion: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-logging-project"` `"organizations/123456789"`  
`exclusion` | `[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)`  
Required. The new exclusion, whose `name` parameter is an exclusion name that is not already used in the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### createExclusion(@Nullable ProjectName parent, LogExclusion exclusion)
    
    
    public final LogExclusion createExclusion(@Nullable ProjectName parent, LogExclusion exclusion)

Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       LogExclusion exclusion = LogExclusion.newBuilder().build();
       LogExclusion response = configClient.createExclusion(parent, exclusion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.ProjectName`  
Required. The parent resource in which to create the exclusion: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-logging-project"` `"organizations/123456789"`  
`exclusion` | `[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)`  
Required. The new exclusion, whose `name` parameter is an exclusion name that is not already used in the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### createExclusion(CreateExclusionRequest request)
    
    
    public final LogExclusion createExclusion(CreateExclusionRequest request)

Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateExclusionRequest request =
           CreateExclusionRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setExclusion(LogExclusion.newBuilder().build())
               .build();
       LogExclusion response = configClient.createExclusion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateExclusionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### createExclusion(String parent, LogExclusion exclusion)
    
    
    public final LogExclusion createExclusion(String parent, LogExclusion exclusion)

Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       LogExclusion exclusion = LogExclusion.newBuilder().build();
       LogExclusion response = configClient.createExclusion(parent, exclusion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource in which to create the exclusion: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-logging-project"` `"organizations/123456789"`  
`exclusion` | `[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)`  
Required. The new exclusion, whose `name` parameter is an exclusion name that is not already used in the parent resource.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### createExclusionCallable()
    
    
    public final UnaryCallable<CreateExclusionRequest,LogExclusion> createExclusionCallable()

Creates a new exclusion in the _Default sink in a specified parent resource. Only log entries belonging to that resource can be excluded. You can have up to 10 exclusions in a resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateExclusionRequest request =
           CreateExclusionRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setExclusion(LogExclusion.newBuilder().build())
               .build();
       ApiFuture<LogExclusion> future = configClient.createExclusionCallable().futureCall(request);
       // Do something.
       LogExclusion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateExclusionRequest),[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### createLinkAsync(@Nullable LogBucketName parent, Link link, String linkId)
    
    
    public final OperationFuture<Link,LinkMetadata> createLinkAsync(@Nullable LogBucketName parent, Link link, String linkId)

Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogBucketName parent =
           LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]");
       Link link = Link.newBuilder().build();
       String linkId = "linkId-1102667083";
       Link response = configClient.createLinkAsync(parent, link, linkId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogBucketName`  
Required. The full resource name of the bucket to create a link for. "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"  
`link` | `[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link)`  
Required. The new link.  
`linkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the link. The link_id can have up to 100 characters. A valid link_id must only have alphanumeric characters and underscores within it.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### createLinkAsync(CreateLinkRequest request)
    
    
    public final OperationFuture<Link,LinkMetadata> createLinkAsync(CreateLinkRequest request)

Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateLinkRequest request =
           CreateLinkRequest.newBuilder()
               .setParent(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setLink(Link.newBuilder().build())
               .setLinkId("linkId-1102667083")
               .build();
       Link response = configClient.createLinkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### createLinkAsync(String parent, Link link, String linkId)
    
    
    public final OperationFuture<Link,LinkMetadata> createLinkAsync(String parent, Link link, String linkId)

Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent =
           LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
               .toString();
       Link link = Link.newBuilder().build();
       String linkId = "linkId-1102667083";
       Link response = configClient.createLinkAsync(parent, link, linkId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full resource name of the bucket to create a link for. "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"  
`link` | `[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link)`  
Required. The new link.  
`linkId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the link. The link_id can have up to 100 characters. A valid link_id must only have alphanumeric characters and underscores within it.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### createLinkCallable()
    
    
    public final UnaryCallable<CreateLinkRequest,Operation> createLinkCallable()

Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateLinkRequest request =
           CreateLinkRequest.newBuilder()
               .setParent(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setLink(Link.newBuilder().build())
               .setLinkId("linkId-1102667083")
               .build();
       ApiFuture<Operation> future = configClient.createLinkCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLinkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLinkOperationCallable()
    
    
    public final OperationCallable<CreateLinkRequest,Link,LinkMetadata> createLinkOperationCallable()

Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateLinkRequest request =
           CreateLinkRequest.newBuilder()
               .setParent(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setLink(Link.newBuilder().build())
               .setLinkId("linkId-1102667083")
               .build();
       OperationFuture<Link, LinkMetadata> future =
           configClient.createLinkOperationCallable().futureCall(request);
       // Do something.
       Link response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLinkRequest),[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### createSink(@Nullable BillingAccountName parent, LogSink sink)
    
    
    public final LogSink createSink(@Nullable BillingAccountName parent, LogSink sink)

Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       BillingAccountName parent = BillingAccountName.of("[BILLING_ACCOUNT]");
       LogSink sink = LogSink.newBuilder().build();
       LogSink response = configClient.createSink(parent, sink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.BillingAccountName`  
Required. The resource in which to create the sink: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-project"` `"organizations/123456789"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The new sink, whose `name` parameter is a sink identifier that is not already in use.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### createSink(@Nullable FolderName parent, LogSink sink)
    
    
    public final LogSink createSink(@Nullable FolderName parent, LogSink sink)

Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       LogSink sink = LogSink.newBuilder().build();
       LogSink response = configClient.createSink(parent, sink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.FolderName`  
Required. The resource in which to create the sink: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-project"` `"organizations/123456789"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The new sink, whose `name` parameter is a sink identifier that is not already in use.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### createSink(@Nullable OrganizationName parent, LogSink sink)
    
    
    public final LogSink createSink(@Nullable OrganizationName parent, LogSink sink)

Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       LogSink sink = LogSink.newBuilder().build();
       LogSink response = configClient.createSink(parent, sink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.OrganizationName`  
Required. The resource in which to create the sink: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-project"` `"organizations/123456789"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The new sink, whose `name` parameter is a sink identifier that is not already in use.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### createSink(@Nullable ProjectName parent, LogSink sink)
    
    
    public final LogSink createSink(@Nullable ProjectName parent, LogSink sink)

Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       LogSink sink = LogSink.newBuilder().build();
       LogSink response = configClient.createSink(parent, sink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.ProjectName`  
Required. The resource in which to create the sink: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-project"` `"organizations/123456789"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The new sink, whose `name` parameter is a sink identifier that is not already in use.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### createSink(CreateSinkRequest request)
    
    
    public final LogSink createSink(CreateSinkRequest request)

Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateSinkRequest request =
           CreateSinkRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setSink(LogSink.newBuilder().build())
               .setUniqueWriterIdentity(true)
               .build();
       LogSink response = configClient.createSink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateSinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### createSink(String parent, LogSink sink)
    
    
    public final LogSink createSink(String parent, LogSink sink)

Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       LogSink sink = LogSink.newBuilder().build();
       LogSink response = configClient.createSink(parent, sink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource in which to create the sink: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]" For examples: `"projects/my-project"` `"organizations/123456789"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The new sink, whose `name` parameter is a sink identifier that is not already in use.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### createSinkCallable()
    
    
    public final UnaryCallable<CreateSinkRequest,LogSink> createSinkCallable()

Creates a sink that exports specified log entries to a destination. The export of newly-ingested log entries begins immediately, unless the sink's `writer_identity` is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateSinkRequest request =
           CreateSinkRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setSink(LogSink.newBuilder().build())
               .setUniqueWriterIdentity(true)
               .build();
       ApiFuture<LogSink> future = configClient.createSinkCallable().futureCall(request);
       // Do something.
       LogSink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateSinkRequest),[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### createView(CreateViewRequest request)
    
    
    public final LogView createView(CreateViewRequest request)

Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateViewRequest request =
           CreateViewRequest.newBuilder()
               .setParent("parent-995424086")
               .setViewId("viewId-816632160")
               .setView(LogView.newBuilder().build())
               .build();
       LogView response = configClient.createView(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)` |   
  
### createViewCallable()
    
    
    public final UnaryCallable<CreateViewRequest,LogView> createViewCallable()

Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       CreateViewRequest request =
           CreateViewRequest.newBuilder()
               .setParent("parent-995424086")
               .setViewId("viewId-816632160")
               .setView(LogView.newBuilder().build())
               .build();
       ApiFuture<LogView> future = configClient.createViewCallable().futureCall(request);
       // Do something.
       LogView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateViewRequest),[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)>` |   
  
### deleteBucket(DeleteBucketRequest request)
    
    
    public final void deleteBucket(DeleteBucketRequest request)

Deletes a log bucket.

Changes the bucket's `lifecycle_state` to the `DELETE_REQUESTED` state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteBucketRequest request =
           DeleteBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .build();
       configClient.deleteBucket(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteBucketRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteBucketCallable()
    
    
    public final UnaryCallable<DeleteBucketRequest,Empty> deleteBucketCallable()

Deletes a log bucket.

Changes the bucket's `lifecycle_state` to the `DELETE_REQUESTED` state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteBucketRequest request =
           DeleteBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .build();
       ApiFuture<Empty> future = configClient.deleteBucketCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteBucketRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteExclusion(@Nullable LogExclusionName name)
    
    
    public final void deleteExclusion(@Nullable LogExclusionName name)

Deletes an exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogExclusionName name = LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]");
       configClient.deleteExclusion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogExclusionName`  
Required. The resource name of an existing exclusion to delete: "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]" "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]" "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]" For example: `"projects/my-project/exclusions/my-exclusion"`  
  
### deleteExclusion(DeleteExclusionRequest request)
    
    
    public final void deleteExclusion(DeleteExclusionRequest request)

Deletes an exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteExclusionRequest request =
           DeleteExclusionRequest.newBuilder()
               .setName(
                   LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString())
               .build();
       configClient.deleteExclusion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteExclusionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteExclusion(String name)
    
    
    public final void deleteExclusion(String name)

Deletes an exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name = LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString();
       configClient.deleteExclusion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of an existing exclusion to delete: "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]" "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]" "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]" For example: `"projects/my-project/exclusions/my-exclusion"`  
  
### deleteExclusionCallable()
    
    
    public final UnaryCallable<DeleteExclusionRequest,Empty> deleteExclusionCallable()

Deletes an exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteExclusionRequest request =
           DeleteExclusionRequest.newBuilder()
               .setName(
                   LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString())
               .build();
       ApiFuture<Empty> future = configClient.deleteExclusionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteExclusionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteLinkAsync(@Nullable LinkName name)
    
    
    public final OperationFuture<Empty,LinkMetadata> deleteLinkAsync(@Nullable LinkName name)

Deletes a link. This will also delete the corresponding BigQuery linked dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LinkName name =
           LinkName.ofProjectLocationBucketLinkName("[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]");
       configClient.deleteLinkAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LinkName`  
Required. The full resource name of the link to delete. "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### deleteLinkAsync(DeleteLinkRequest request)
    
    
    public final OperationFuture<Empty,LinkMetadata> deleteLinkAsync(DeleteLinkRequest request)

Deletes a link. This will also delete the corresponding BigQuery linked dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteLinkRequest request =
           DeleteLinkRequest.newBuilder()
               .setName(
                   LinkName.ofProjectLocationBucketLinkName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]")
                       .toString())
               .build();
       configClient.deleteLinkAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### deleteLinkAsync(String name)
    
    
    public final OperationFuture<Empty,LinkMetadata> deleteLinkAsync(String name)

Deletes a link. This will also delete the corresponding BigQuery linked dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name =
           LinkName.ofProjectLocationBucketLinkName("[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]")
               .toString();
       configClient.deleteLinkAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full resource name of the link to delete. "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### deleteLinkCallable()
    
    
    public final UnaryCallable<DeleteLinkRequest,Operation> deleteLinkCallable()

Deletes a link. This will also delete the corresponding BigQuery linked dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteLinkRequest request =
           DeleteLinkRequest.newBuilder()
               .setName(
                   LinkName.ofProjectLocationBucketLinkName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]")
                       .toString())
               .build();
       ApiFuture<Operation> future = configClient.deleteLinkCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLinkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLinkOperationCallable()
    
    
    public final OperationCallable<DeleteLinkRequest,Empty,LinkMetadata> deleteLinkOperationCallable()

Deletes a link. This will also delete the corresponding BigQuery linked dataset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteLinkRequest request =
           DeleteLinkRequest.newBuilder()
               .setName(
                   LinkName.ofProjectLocationBucketLinkName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]")
                       .toString())
               .build();
       OperationFuture<Empty, LinkMetadata> future =
           configClient.deleteLinkOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLinkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### deleteSink(@Nullable LogSinkName sinkName)
    
    
    public final void deleteSink(@Nullable LogSinkName sinkName)

Deletes a sink. If the sink has a unique `writer_identity`, then that service account is also deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogSinkName sinkName = LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]");
       configClient.deleteSink(sinkName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sinkName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogSinkName`  
Required. The full resource name of the sink to delete, including the parent resource and the sink identifier: "projects/[PROJECT_ID]/sinks/[SINK_ID]" "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]" "folders/[FOLDER_ID]/sinks/[SINK_ID]" For example: `"projects/my-project/sinks/my-sink"`  
  
### deleteSink(DeleteSinkRequest request)
    
    
    public final void deleteSink(DeleteSinkRequest request)

Deletes a sink. If the sink has a unique `writer_identity`, then that service account is also deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteSinkRequest request =
           DeleteSinkRequest.newBuilder()
               .setSinkName(LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString())
               .build();
       configClient.deleteSink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteSinkRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSink(String sinkName)
    
    
    public final void deleteSink(String sinkName)

Deletes a sink. If the sink has a unique `writer_identity`, then that service account is also deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String sinkName = LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString();
       configClient.deleteSink(sinkName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sinkName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full resource name of the sink to delete, including the parent resource and the sink identifier: "projects/[PROJECT_ID]/sinks/[SINK_ID]" "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]" "folders/[FOLDER_ID]/sinks/[SINK_ID]" For example: `"projects/my-project/sinks/my-sink"`  
  
### deleteSinkCallable()
    
    
    public final UnaryCallable<DeleteSinkRequest,Empty> deleteSinkCallable()

Deletes a sink. If the sink has a unique `writer_identity`, then that service account is also deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteSinkRequest request =
           DeleteSinkRequest.newBuilder()
               .setSinkName(LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString())
               .build();
       ApiFuture<Empty> future = configClient.deleteSinkCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteSinkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteView(DeleteViewRequest request)
    
    
    public final void deleteView(DeleteViewRequest request)

Deletes a view on a log bucket. If an `UNAVAILABLE` error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteViewRequest request =
           DeleteViewRequest.newBuilder()
               .setName(
                   LogViewName.ofProjectLocationBucketViewName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[VIEW]")
                       .toString())
               .build();
       configClient.deleteView(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteViewRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteViewCallable()
    
    
    public final UnaryCallable<DeleteViewRequest,Empty> deleteViewCallable()

Deletes a view on a log bucket. If an `UNAVAILABLE` error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       DeleteViewRequest request =
           DeleteViewRequest.newBuilder()
               .setName(
                   LogViewName.ofProjectLocationBucketViewName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[VIEW]")
                       .toString())
               .build();
       ApiFuture<Empty> future = configClient.deleteViewCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteViewRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getBucket(GetBucketRequest request)
    
    
    public final LogBucket getBucket(GetBucketRequest request)

Gets a log bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetBucketRequest request =
           GetBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .build();
       LogBucket response = configClient.getBucket(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)` |   
  
### getBucketCallable()
    
    
    public final UnaryCallable<GetBucketRequest,LogBucket> getBucketCallable()

Gets a log bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetBucketRequest request =
           GetBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .build();
       ApiFuture<LogBucket> future = configClient.getBucketCallable().futureCall(request);
       // Do something.
       LogBucket response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)>` |   
  
### getCmekSettings(GetCmekSettingsRequest request)
    
    
    public final CmekSettings getCmekSettings(GetCmekSettingsRequest request)

Gets the Logging CMEK settings for the given resource.

Note: CMEK for the Log Router can be configured for Google Cloud projects, folders, organizations and billing accounts. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetCmekSettingsRequest request =
           GetCmekSettingsRequest.newBuilder()
               .setName(CmekSettingsName.ofProjectName("[PROJECT]").toString())
               .build();
       CmekSettings response = configClient.getCmekSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCmekSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetCmekSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CmekSettings)` |   
  
### getCmekSettingsCallable()
    
    
    public final UnaryCallable<GetCmekSettingsRequest,CmekSettings> getCmekSettingsCallable()

Gets the Logging CMEK settings for the given resource.

Note: CMEK for the Log Router can be configured for Google Cloud projects, folders, organizations and billing accounts. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetCmekSettingsRequest request =
           GetCmekSettingsRequest.newBuilder()
               .setName(CmekSettingsName.ofProjectName("[PROJECT]").toString())
               .build();
       ApiFuture<CmekSettings> future = configClient.getCmekSettingsCallable().futureCall(request);
       // Do something.
       CmekSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCmekSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetCmekSettingsRequest),[CmekSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CmekSettings)>` |   
  
### getExclusion(@Nullable LogExclusionName name)
    
    
    public final LogExclusion getExclusion(@Nullable LogExclusionName name)

Gets the description of an exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogExclusionName name = LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]");
       LogExclusion response = configClient.getExclusion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogExclusionName`  
Required. The resource name of an existing exclusion: "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]" "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]" "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]" For example: `"projects/my-project/exclusions/my-exclusion"`  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### getExclusion(GetExclusionRequest request)
    
    
    public final LogExclusion getExclusion(GetExclusionRequest request)

Gets the description of an exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetExclusionRequest request =
           GetExclusionRequest.newBuilder()
               .setName(
                   LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString())
               .build();
       LogExclusion response = configClient.getExclusion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetExclusionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### getExclusion(String name)
    
    
    public final LogExclusion getExclusion(String name)

Gets the description of an exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name = LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString();
       LogExclusion response = configClient.getExclusion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of an existing exclusion: "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]" "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]" "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]" For example: `"projects/my-project/exclusions/my-exclusion"`  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### getExclusionCallable()
    
    
    public final UnaryCallable<GetExclusionRequest,LogExclusion> getExclusionCallable()

Gets the description of an exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetExclusionRequest request =
           GetExclusionRequest.newBuilder()
               .setName(
                   LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString())
               .build();
       ApiFuture<LogExclusion> future = configClient.getExclusionCallable().futureCall(request);
       // Do something.
       LogExclusion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetExclusionRequest),[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### getLink(@Nullable LinkName name)
    
    
    public final Link getLink(@Nullable LinkName name)

Gets a link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LinkName name =
           LinkName.ofProjectLocationBucketLinkName("[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]");
       Link response = configClient.getLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LinkName`  
Required. The resource name of the link: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]  
**Returns**  
---  
**Type** | **Description**  
`[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link)` |   
  
### getLink(GetLinkRequest request)
    
    
    public final Link getLink(GetLinkRequest request)

Gets a link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetLinkRequest request =
           GetLinkRequest.newBuilder()
               .setName(
                   LinkName.ofProjectLocationBucketLinkName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]")
                       .toString())
               .build();
       Link response = configClient.getLink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetLinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link)` |   
  
### getLink(String name)
    
    
    public final Link getLink(String name)

Gets a link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name =
           LinkName.ofProjectLocationBucketLinkName("[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]")
               .toString();
       Link response = configClient.getLink(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the link: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]  
**Returns**  
---  
**Type** | **Description**  
`[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link)` |   
  
### getLinkCallable()
    
    
    public final UnaryCallable<GetLinkRequest,Link> getLinkCallable()

Gets a link.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetLinkRequest request =
           GetLinkRequest.newBuilder()
               .setName(
                   LinkName.ofProjectLocationBucketLinkName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[LINK]")
                       .toString())
               .build();
       ApiFuture<Link> future = configClient.getLinkCallable().futureCall(request);
       // Do something.
       Link response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetLinkRequest),[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable ConfigSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.logging.v2.ConfigSettings` |   
  
### getSettings(@Nullable SettingsName name)
    
    
    public final Settings getSettings(@Nullable SettingsName name)

Gets the Log Router settings for the given resource.

Note: Settings for the Log Router can be get for Google Cloud projects, folders, organizations and billing accounts. Currently it can only be configured for organizations. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       SettingsName name = SettingsName.ofProjectName("[PROJECT]");
       Settings response = configClient.getSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.logging.v2.SettingsName`  
Required. The resource for which to retrieve settings. "projects/[PROJECT_ID]/settings" "organizations/[ORGANIZATION_ID]/settings" "billingAccounts/[BILLING_ACCOUNT_ID]/settings" "folders/[FOLDER_ID]/settings" For example: `"organizations/12345/settings"` Note: Settings for the Log Router can be get for Google Cloud projects, folders, organizations and billing accounts. Currently it can only be configured for organizations. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)` |   
  
### getSettings(GetSettingsRequest request)
    
    
    public final Settings getSettings(GetSettingsRequest request)

Gets the Log Router settings for the given resource.

Note: Settings for the Log Router can be get for Google Cloud projects, folders, organizations and billing accounts. Currently it can only be configured for organizations. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetSettingsRequest request =
           GetSettingsRequest.newBuilder()
               .setName(SettingsName.ofProjectName("[PROJECT]").toString())
               .build();
       Settings response = configClient.getSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)` |   
  
### getSettings(String name)
    
    
    public final Settings getSettings(String name)

Gets the Log Router settings for the given resource.

Note: Settings for the Log Router can be get for Google Cloud projects, folders, organizations and billing accounts. Currently it can only be configured for organizations. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name = SettingsName.ofProjectName("[PROJECT]").toString();
       Settings response = configClient.getSettings(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource for which to retrieve settings. "projects/[PROJECT_ID]/settings" "organizations/[ORGANIZATION_ID]/settings" "billingAccounts/[BILLING_ACCOUNT_ID]/settings" "folders/[FOLDER_ID]/settings" For example: `"organizations/12345/settings"` Note: Settings for the Log Router can be get for Google Cloud projects, folders, organizations and billing accounts. Currently it can only be configured for organizations. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)` |   
  
### getSettingsCallable()
    
    
    public final UnaryCallable<GetSettingsRequest,Settings> getSettingsCallable()

Gets the Log Router settings for the given resource.

Note: Settings for the Log Router can be get for Google Cloud projects, folders, organizations and billing accounts. Currently it can only be configured for organizations. Once configured for an organization, it applies to all projects and folders in the Google Cloud organization.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetSettingsRequest request =
           GetSettingsRequest.newBuilder()
               .setName(SettingsName.ofProjectName("[PROJECT]").toString())
               .build();
       ApiFuture<Settings> future = configClient.getSettingsCallable().futureCall(request);
       // Do something.
       Settings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)>` |   
  
### getSink(@Nullable LogSinkName sinkName)
    
    
    public final LogSink getSink(@Nullable LogSinkName sinkName)

Gets a sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogSinkName sinkName = LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]");
       LogSink response = configClient.getSink(sinkName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sinkName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogSinkName`  
Required. The resource name of the sink: "projects/[PROJECT_ID]/sinks/[SINK_ID]" "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]" "folders/[FOLDER_ID]/sinks/[SINK_ID]" For example: `"projects/my-project/sinks/my-sink"`  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### getSink(GetSinkRequest request)
    
    
    public final LogSink getSink(GetSinkRequest request)

Gets a sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetSinkRequest request =
           GetSinkRequest.newBuilder()
               .setSinkName(LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString())
               .build();
       LogSink response = configClient.getSink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetSinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### getSink(String sinkName)
    
    
    public final LogSink getSink(String sinkName)

Gets a sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String sinkName = LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString();
       LogSink response = configClient.getSink(sinkName);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`sinkName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the sink: "projects/[PROJECT_ID]/sinks/[SINK_ID]" "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]" "folders/[FOLDER_ID]/sinks/[SINK_ID]" For example: `"projects/my-project/sinks/my-sink"`  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### getSinkCallable()
    
    
    public final UnaryCallable<GetSinkRequest,LogSink> getSinkCallable()

Gets a sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetSinkRequest request =
           GetSinkRequest.newBuilder()
               .setSinkName(LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString())
               .build();
       ApiFuture<LogSink> future = configClient.getSinkCallable().futureCall(request);
       // Do something.
       LogSink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetSinkRequest),[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### getStub()
    
    
    public ConfigServiceV2Stub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConfigServiceV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.ConfigServiceV2Stub)` |   
  
### getView(GetViewRequest request)
    
    
    public final LogView getView(GetViewRequest request)

Gets a view on a log bucket..

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetViewRequest request =
           GetViewRequest.newBuilder()
               .setName(
                   LogViewName.ofProjectLocationBucketViewName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[VIEW]")
                       .toString())
               .build();
       LogView response = configClient.getView(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)` |   
  
### getViewCallable()
    
    
    public final UnaryCallable<GetViewRequest,LogView> getViewCallable()

Gets a view on a log bucket..

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       GetViewRequest request =
           GetViewRequest.newBuilder()
               .setName(
                   LogViewName.ofProjectLocationBucketViewName(
                           "[PROJECT]", "[LOCATION]", "[BUCKET]", "[VIEW]")
                       .toString())
               .build();
       ApiFuture<LogView> future = configClient.getViewCallable().futureCall(request);
       // Do something.
       LogView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetViewRequest),[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)>` |   
  
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
  
### listBuckets(@Nullable BillingAccountLocationName parent)
    
    
    public final ConfigClient.ListBucketsPagedResponse listBuckets(@Nullable BillingAccountLocationName parent)

Lists log buckets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       BillingAccountLocationName parent =
           BillingAccountLocationName.of("[BILLING_ACCOUNT]", "[LOCATION]");
       for (LogBucket element : configClient.listBuckets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.BillingAccountLocationName`  
Required. The parent resource whose buckets are to be listed: "projects/[PROJECT_ID]/locations/[LOCATION_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]" Note: The locations portion of the resource must be specified, but supplying the character `-` in place of [LOCATION_ID] will return all buckets.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListBucketsPagedResponse)` |   
  
### listBuckets(@Nullable FolderLocationName parent)
    
    
    public final ConfigClient.ListBucketsPagedResponse listBuckets(@Nullable FolderLocationName parent)

Lists log buckets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       FolderLocationName parent = FolderLocationName.of("[FOLDER]", "[LOCATION]");
       for (LogBucket element : configClient.listBuckets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.FolderLocationName`  
Required. The parent resource whose buckets are to be listed: "projects/[PROJECT_ID]/locations/[LOCATION_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]" Note: The locations portion of the resource must be specified, but supplying the character `-` in place of [LOCATION_ID] will return all buckets.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListBucketsPagedResponse)` |   
  
### listBuckets(@Nullable LocationName parent)
    
    
    public final ConfigClient.ListBucketsPagedResponse listBuckets(@Nullable LocationName parent)

Lists log buckets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (LogBucket element : configClient.listBuckets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LocationName`  
Required. The parent resource whose buckets are to be listed: "projects/[PROJECT_ID]/locations/[LOCATION_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]" Note: The locations portion of the resource must be specified, but supplying the character `-` in place of [LOCATION_ID] will return all buckets.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListBucketsPagedResponse)` |   
  
### listBuckets(@Nullable OrganizationLocationName parent)
    
    
    public final ConfigClient.ListBucketsPagedResponse listBuckets(@Nullable OrganizationLocationName parent)

Lists log buckets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (LogBucket element : configClient.listBuckets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.OrganizationLocationName`  
Required. The parent resource whose buckets are to be listed: "projects/[PROJECT_ID]/locations/[LOCATION_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]" Note: The locations portion of the resource must be specified, but supplying the character `-` in place of [LOCATION_ID] will return all buckets.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListBucketsPagedResponse)` |   
  
### listBuckets(ListBucketsRequest request)
    
    
    public final ConfigClient.ListBucketsPagedResponse listBuckets(ListBucketsRequest request)

Lists log buckets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListBucketsRequest request =
           ListBucketsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (LogBucket element : configClient.listBuckets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListBucketsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListBucketsPagedResponse)` |   
  
### listBuckets(String parent)
    
    
    public final ConfigClient.ListBucketsPagedResponse listBuckets(String parent)

Lists log buckets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (LogBucket element : configClient.listBuckets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource whose buckets are to be listed: "projects/[PROJECT_ID]/locations/[LOCATION_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]" Note: The locations portion of the resource must be specified, but supplying the character `-` in place of [LOCATION_ID] will return all buckets.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListBucketsPagedResponse)` |   
  
### listBucketsCallable()
    
    
    public final UnaryCallable<ListBucketsRequest,ListBucketsResponse> listBucketsCallable()

Lists log buckets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListBucketsRequest request =
           ListBucketsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListBucketsResponse response = configClient.listBucketsCallable().call(request);
         for (LogBucket element : response.getBucketsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListBucketsRequest),[ListBucketsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListBucketsResponse)>` |   
  
### listBucketsPagedCallable()
    
    
    public final UnaryCallable<ListBucketsRequest,ConfigClient.ListBucketsPagedResponse> listBucketsPagedCallable()

Lists log buckets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListBucketsRequest request =
           ListBucketsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<LogBucket> future = configClient.listBucketsPagedCallable().futureCall(request);
       // Do something.
       for (LogBucket element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListBucketsRequest),[ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListBucketsPagedResponse)>` |   
  
### listExclusions(@Nullable BillingAccountName parent)
    
    
    public final ConfigClient.ListExclusionsPagedResponse listExclusions(@Nullable BillingAccountName parent)

Lists all the exclusions on the _Default sink in a parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       BillingAccountName parent = BillingAccountName.of("[BILLING_ACCOUNT]");
       for (LogExclusion element : configClient.listExclusions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.BillingAccountName`  
Required. The parent resource whose exclusions are to be listed. "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListExclusionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListExclusionsPagedResponse)` |   
  
### listExclusions(@Nullable FolderName parent)
    
    
    public final ConfigClient.ListExclusionsPagedResponse listExclusions(@Nullable FolderName parent)

Lists all the exclusions on the _Default sink in a parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       for (LogExclusion element : configClient.listExclusions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.FolderName`  
Required. The parent resource whose exclusions are to be listed. "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListExclusionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListExclusionsPagedResponse)` |   
  
### listExclusions(@Nullable OrganizationName parent)
    
    
    public final ConfigClient.ListExclusionsPagedResponse listExclusions(@Nullable OrganizationName parent)

Lists all the exclusions on the _Default sink in a parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (LogExclusion element : configClient.listExclusions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.OrganizationName`  
Required. The parent resource whose exclusions are to be listed. "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListExclusionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListExclusionsPagedResponse)` |   
  
### listExclusions(@Nullable ProjectName parent)
    
    
    public final ConfigClient.ListExclusionsPagedResponse listExclusions(@Nullable ProjectName parent)

Lists all the exclusions on the _Default sink in a parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (LogExclusion element : configClient.listExclusions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.ProjectName`  
Required. The parent resource whose exclusions are to be listed. "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListExclusionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListExclusionsPagedResponse)` |   
  
### listExclusions(ListExclusionsRequest request)
    
    
    public final ConfigClient.ListExclusionsPagedResponse listExclusions(ListExclusionsRequest request)

Lists all the exclusions on the _Default sink in a parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListExclusionsRequest request =
           ListExclusionsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (LogExclusion element : configClient.listExclusions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExclusionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListExclusionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListExclusionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListExclusionsPagedResponse)` |   
  
### listExclusions(String parent)
    
    
    public final ConfigClient.ListExclusionsPagedResponse listExclusions(String parent)

Lists all the exclusions on the _Default sink in a parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (LogExclusion element : configClient.listExclusions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource whose exclusions are to be listed. "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListExclusionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListExclusionsPagedResponse)` |   
  
### listExclusionsCallable()
    
    
    public final UnaryCallable<ListExclusionsRequest,ListExclusionsResponse> listExclusionsCallable()

Lists all the exclusions on the _Default sink in a parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListExclusionsRequest request =
           ListExclusionsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListExclusionsResponse response = configClient.listExclusionsCallable().call(request);
         for (LogExclusion element : response.getExclusionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExclusionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListExclusionsRequest),[ListExclusionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListExclusionsResponse)>` |   
  
### listExclusionsPagedCallable()
    
    
    public final UnaryCallable<ListExclusionsRequest,ConfigClient.ListExclusionsPagedResponse> listExclusionsPagedCallable()

Lists all the exclusions on the _Default sink in a parent resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListExclusionsRequest request =
           ListExclusionsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<LogExclusion> future =
           configClient.listExclusionsPagedCallable().futureCall(request);
       // Do something.
       for (LogExclusion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExclusionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListExclusionsRequest),[ListExclusionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListExclusionsPagedResponse)>` |   
  
### listLinks(@Nullable LogBucketName parent)
    
    
    public final ConfigClient.ListLinksPagedResponse listLinks(@Nullable LogBucketName parent)

Lists links.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogBucketName parent =
           LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]");
       for (Link element : configClient.listLinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogBucketName`  
Required. The parent resource whose links are to be listed: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListLinksPagedResponse)` |   
  
### listLinks(ListLinksRequest request)
    
    
    public final ConfigClient.ListLinksPagedResponse listLinks(ListLinksRequest request)

Lists links.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListLinksRequest request =
           ListLinksRequest.newBuilder()
               .setParent(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (Link element : configClient.listLinks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLinksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListLinksPagedResponse)` |   
  
### listLinks(String parent)
    
    
    public final ConfigClient.ListLinksPagedResponse listLinks(String parent)

Lists links.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent =
           LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
               .toString();
       for (Link element : configClient.listLinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource whose links are to be listed: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListLinksPagedResponse)` |   
  
### listLinksCallable()
    
    
    public final UnaryCallable<ListLinksRequest,ListLinksResponse> listLinksCallable()

Lists links.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListLinksRequest request =
           ListLinksRequest.newBuilder()
               .setParent(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListLinksResponse response = configClient.listLinksCallable().call(request);
         for (Link element : response.getLinksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLinksRequest),[ListLinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLinksResponse)>` |   
  
### listLinksPagedCallable()
    
    
    public final UnaryCallable<ListLinksRequest,ConfigClient.ListLinksPagedResponse> listLinksPagedCallable()

Lists links.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListLinksRequest request =
           ListLinksRequest.newBuilder()
               .setParent(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<Link> future = configClient.listLinksPagedCallable().futureCall(request);
       // Do something.
       for (Link element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLinksRequest),[ListLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListLinksPagedResponse)>` |   
  
### listSinks(@Nullable BillingAccountName parent)
    
    
    public final ConfigClient.ListSinksPagedResponse listSinks(@Nullable BillingAccountName parent)

Lists sinks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       BillingAccountName parent = BillingAccountName.of("[BILLING_ACCOUNT]");
       for (LogSink element : configClient.listSinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.BillingAccountName`  
Required. The parent resource whose sinks are to be listed: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListSinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListSinksPagedResponse)` |   
  
### listSinks(@Nullable FolderName parent)
    
    
    public final ConfigClient.ListSinksPagedResponse listSinks(@Nullable FolderName parent)

Lists sinks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       FolderName parent = FolderName.of("[FOLDER]");
       for (LogSink element : configClient.listSinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.FolderName`  
Required. The parent resource whose sinks are to be listed: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListSinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListSinksPagedResponse)` |   
  
### listSinks(@Nullable OrganizationName parent)
    
    
    public final ConfigClient.ListSinksPagedResponse listSinks(@Nullable OrganizationName parent)

Lists sinks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       OrganizationName parent = OrganizationName.of("[ORGANIZATION]");
       for (LogSink element : configClient.listSinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.OrganizationName`  
Required. The parent resource whose sinks are to be listed: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListSinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListSinksPagedResponse)` |   
  
### listSinks(@Nullable ProjectName parent)
    
    
    public final ConfigClient.ListSinksPagedResponse listSinks(@Nullable ProjectName parent)

Lists sinks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (LogSink element : configClient.listSinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.logging.v2.ProjectName`  
Required. The parent resource whose sinks are to be listed: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListSinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListSinksPagedResponse)` |   
  
### listSinks(ListSinksRequest request)
    
    
    public final ConfigClient.ListSinksPagedResponse listSinks(ListSinksRequest request)

Lists sinks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListSinksRequest request =
           ListSinksRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (LogSink element : configClient.listSinks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListSinksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListSinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListSinksPagedResponse)` |   
  
### listSinks(String parent)
    
    
    public final ConfigClient.ListSinksPagedResponse listSinks(String parent)

Lists sinks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (LogSink element : configClient.listSinks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource whose sinks are to be listed: "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListSinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListSinksPagedResponse)` |   
  
### listSinksCallable()
    
    
    public final UnaryCallable<ListSinksRequest,ListSinksResponse> listSinksCallable()

Lists sinks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListSinksRequest request =
           ListSinksRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListSinksResponse response = configClient.listSinksCallable().call(request);
         for (LogSink element : response.getSinksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListSinksRequest),[ListSinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListSinksResponse)>` |   
  
### listSinksPagedCallable()
    
    
    public final UnaryCallable<ListSinksRequest,ConfigClient.ListSinksPagedResponse> listSinksPagedCallable()

Lists sinks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListSinksRequest request =
           ListSinksRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<LogSink> future = configClient.listSinksPagedCallable().futureCall(request);
       // Do something.
       for (LogSink element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListSinksRequest),[ListSinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListSinksPagedResponse)>` |   
  
### listViews(ListViewsRequest request)
    
    
    public final ConfigClient.ListViewsPagedResponse listViews(ListViewsRequest request)

Lists views on a log bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListViewsRequest request =
           ListViewsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       for (LogView element : configClient.listViews(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListViewsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListViewsPagedResponse)` |   
  
### listViews(String parent)
    
    
    public final ConfigClient.ListViewsPagedResponse listViews(String parent)

Lists views on a log bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String parent = "parent-995424086";
       for (LogView element : configClient.listViews(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The bucket whose views are to be listed: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]"  
**Returns**  
---  
**Type** | **Description**  
`[ConfigClient.ListViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListViewsPagedResponse)` |   
  
### listViewsCallable()
    
    
    public final UnaryCallable<ListViewsRequest,ListViewsResponse> listViewsCallable()

Lists views on a log bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListViewsRequest request =
           ListViewsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       while (true) {
         ListViewsResponse response = configClient.listViewsCallable().call(request);
         for (LogView element : response.getViewsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListViewsRequest),[ListViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListViewsResponse)>` |   
  
### listViewsPagedCallable()
    
    
    public final UnaryCallable<ListViewsRequest,ConfigClient.ListViewsPagedResponse> listViewsPagedCallable()

Lists views on a log bucket.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       ListViewsRequest request =
           ListViewsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageToken("pageToken873572522")
               .setPageSize(883849137)
               .build();
       ApiFuture<LogView> future = configClient.listViewsPagedCallable().futureCall(request);
       // Do something.
       for (LogView element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListViewsRequest),[ListViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListViewsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### undeleteBucket(UndeleteBucketRequest request)
    
    
    public final void undeleteBucket(UndeleteBucketRequest request)

Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UndeleteBucketRequest request =
           UndeleteBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .build();
       configClient.undeleteBucket(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeleteBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UndeleteBucketRequest)`  
The request object containing all of the parameters for the API call.  
  
### undeleteBucketCallable()
    
    
    public final UnaryCallable<UndeleteBucketRequest,Empty> undeleteBucketCallable()

Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UndeleteBucketRequest request =
           UndeleteBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .build();
       ApiFuture<Empty> future = configClient.undeleteBucketCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeleteBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UndeleteBucketRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### updateBucket(UpdateBucketRequest request)
    
    
    public final LogBucket updateBucket(UpdateBucketRequest request)

Updates a log bucket.

If the bucket has a `lifecycle_state` of `DELETE_REQUESTED`, then `FAILED_PRECONDITION` will be returned.

After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateBucketRequest request =
           UpdateBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setBucket(LogBucket.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       LogBucket response = configClient.updateBucket(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)` |   
  
### updateBucketAsyncAsync(UpdateBucketRequest request)
    
    
    public final OperationFuture<LogBucket,BucketMetadata> updateBucketAsyncAsync(UpdateBucketRequest request)

Updates a log bucket asynchronously.

If the bucket has a `lifecycle_state` of `DELETE_REQUESTED`, then `FAILED_PRECONDITION` will be returned.

After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateBucketRequest request =
           UpdateBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setBucket(LogBucket.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       LogBucket response = configClient.updateBucketAsyncAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateBucketRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket),[BucketMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.BucketMetadata)>` |   
  
### updateBucketAsyncCallable()
    
    
    public final UnaryCallable<UpdateBucketRequest,Operation> updateBucketAsyncCallable()

Updates a log bucket asynchronously.

If the bucket has a `lifecycle_state` of `DELETE_REQUESTED`, then `FAILED_PRECONDITION` will be returned.

After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateBucketRequest request =
           UpdateBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setBucket(LogBucket.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future = configClient.updateBucketAsyncCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBucketAsyncOperationCallable()
    
    
    public final OperationCallable<UpdateBucketRequest,LogBucket,BucketMetadata> updateBucketAsyncOperationCallable()

Updates a log bucket asynchronously.

If the bucket has a `lifecycle_state` of `DELETE_REQUESTED`, then `FAILED_PRECONDITION` will be returned.

After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateBucketRequest request =
           UpdateBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setBucket(LogBucket.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<LogBucket, BucketMetadata> future =
           configClient.updateBucketAsyncOperationCallable().futureCall(request);
       // Do something.
       LogBucket response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket),[BucketMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.BucketMetadata)>` |   
  
### updateBucketCallable()
    
    
    public final UnaryCallable<UpdateBucketRequest,LogBucket> updateBucketCallable()

Updates a log bucket.

If the bucket has a `lifecycle_state` of `DELETE_REQUESTED`, then `FAILED_PRECONDITION` will be returned.

After a bucket has been created, the bucket's location cannot be changed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateBucketRequest request =
           UpdateBucketRequest.newBuilder()
               .setName(
                   LogBucketName.ofProjectLocationBucketName("[PROJECT]", "[LOCATION]", "[BUCKET]")
                       .toString())
               .setBucket(LogBucket.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<LogBucket> future = configClient.updateBucketCallable().futureCall(request);
       // Do something.
       LogBucket response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)>` |   
  
### updateCmekSettings(UpdateCmekSettingsRequest request)
    
    
    public final CmekSettings updateCmekSettings(UpdateCmekSettingsRequest request)

Updates the Log Router CMEK settings for the given resource.

Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.

UpdateCmekSettings will fail if 1) `kms_key_name` is invalid, or 2) the associated service account does not have the required `roles/cloudkms.cryptoKeyEncrypterDecrypter` role assigned for the key, or 3) access to the key is disabled.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateCmekSettingsRequest request =
           UpdateCmekSettingsRequest.newBuilder()
               .setName("name3373707")
               .setCmekSettings(CmekSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CmekSettings response = configClient.updateCmekSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCmekSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateCmekSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CmekSettings)` |   
  
### updateCmekSettingsCallable()
    
    
    public final UnaryCallable<UpdateCmekSettingsRequest,CmekSettings> updateCmekSettingsCallable()

Updates the Log Router CMEK settings for the given resource.

Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.

UpdateCmekSettings will fail if 1) `kms_key_name` is invalid, or 2) the associated service account does not have the required `roles/cloudkms.cryptoKeyEncrypterDecrypter` role assigned for the key, or 3) access to the key is disabled.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateCmekSettingsRequest request =
           UpdateCmekSettingsRequest.newBuilder()
               .setName("name3373707")
               .setCmekSettings(CmekSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CmekSettings> future =
           configClient.updateCmekSettingsCallable().futureCall(request);
       // Do something.
       CmekSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCmekSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateCmekSettingsRequest),[CmekSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CmekSettings)>` |   
  
### updateExclusion(@Nullable LogExclusionName name, LogExclusion exclusion, FieldMask updateMask)
    
    
    public final LogExclusion updateExclusion(@Nullable LogExclusionName name, LogExclusion exclusion, FieldMask updateMask)

Changes one or more properties of an existing exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogExclusionName name = LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]");
       LogExclusion exclusion = LogExclusion.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LogExclusion response = configClient.updateExclusion(name, exclusion, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogExclusionName`  
Required. The resource name of the exclusion to update: "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]" "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]" "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]" For example: `"projects/my-project/exclusions/my-exclusion"`  
`exclusion` | `[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)`  
Required. New values for the existing exclusion. Only the fields specified in `update_mask` are relevant.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A non-empty list of fields to change in the existing exclusion. New values for the fields are taken from the corresponding fields in the LogExclusion included in this request. Fields not mentioned in `update_mask` are not changed and are ignored in the request. For example, to change the filter and description of an exclusion, specify an `update_mask` of `"filter,description"`.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### updateExclusion(UpdateExclusionRequest request)
    
    
    public final LogExclusion updateExclusion(UpdateExclusionRequest request)

Changes one or more properties of an existing exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateExclusionRequest request =
           UpdateExclusionRequest.newBuilder()
               .setName(
                   LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString())
               .setExclusion(LogExclusion.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       LogExclusion response = configClient.updateExclusion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateExclusionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### updateExclusion(String name, LogExclusion exclusion, FieldMask updateMask)
    
    
    public final LogExclusion updateExclusion(String name, LogExclusion exclusion, FieldMask updateMask)

Changes one or more properties of an existing exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String name = LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString();
       LogExclusion exclusion = LogExclusion.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LogExclusion response = configClient.updateExclusion(name, exclusion, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the exclusion to update: "projects/[PROJECT_ID]/exclusions/[EXCLUSION_ID]" "organizations/[ORGANIZATION_ID]/exclusions/[EXCLUSION_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/exclusions/[EXCLUSION_ID]" "folders/[FOLDER_ID]/exclusions/[EXCLUSION_ID]" For example: `"projects/my-project/exclusions/my-exclusion"`  
`exclusion` | `[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)`  
Required. New values for the existing exclusion. Only the fields specified in `update_mask` are relevant.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. A non-empty list of fields to change in the existing exclusion. New values for the fields are taken from the corresponding fields in the LogExclusion included in this request. Fields not mentioned in `update_mask` are not changed and are ignored in the request. For example, to change the filter and description of an exclusion, specify an `update_mask` of `"filter,description"`.  
**Returns**  
---  
**Type** | **Description**  
`[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)` |   
  
### updateExclusionCallable()
    
    
    public final UnaryCallable<UpdateExclusionRequest,LogExclusion> updateExclusionCallable()

Changes one or more properties of an existing exclusion in the _Default sink.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateExclusionRequest request =
           UpdateExclusionRequest.newBuilder()
               .setName(
                   LogExclusionName.ofProjectExclusionName("[PROJECT]", "[EXCLUSION]").toString())
               .setExclusion(LogExclusion.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<LogExclusion> future = configClient.updateExclusionCallable().futureCall(request);
       // Do something.
       LogExclusion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateExclusionRequest),[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### updateSettings(Settings settings, FieldMask updateMask)
    
    
    public final Settings updateSettings(Settings settings, FieldMask updateMask)

Updates the Log Router settings for the given resource.

Note: Settings for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.

UpdateSettings will fail if 1) `kms_key_name` is invalid, or 2) the associated service account does not have the required `roles/cloudkms.cryptoKeyEncrypterDecrypter` role assigned for the key, or 3) access to the key is disabled. 4) `location_id` is not supported by Logging. 5) `location_id` violate OrgPolicy.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       Settings settings = Settings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Settings response = configClient.updateSettings(settings, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)`  
Required. The settings to update. See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask identifying which fields from `settings` should be updated. A field will be overwritten if and only if it is in the update mask. Output only fields cannot be updated. See FieldMask for more information. For example: `"updateMask=kmsKeyName"`  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)` |   
  
### updateSettings(UpdateSettingsRequest request)
    
    
    public final Settings updateSettings(UpdateSettingsRequest request)

Updates the Log Router settings for the given resource.

Note: Settings for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.

UpdateSettings will fail if 1) `kms_key_name` is invalid, or 2) the associated service account does not have the required `roles/cloudkms.cryptoKeyEncrypterDecrypter` role assigned for the key, or 3) access to the key is disabled. 4) `location_id` is not supported by Logging. 5) `location_id` violate OrgPolicy.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateSettingsRequest request =
           UpdateSettingsRequest.newBuilder()
               .setName("name3373707")
               .setSettings(Settings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Settings response = configClient.updateSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)` |   
  
### updateSettingsCallable()
    
    
    public final UnaryCallable<UpdateSettingsRequest,Settings> updateSettingsCallable()

Updates the Log Router settings for the given resource.

Note: Settings for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.

UpdateSettings will fail if 1) `kms_key_name` is invalid, or 2) the associated service account does not have the required `roles/cloudkms.cryptoKeyEncrypterDecrypter` role assigned for the key, or 3) access to the key is disabled. 4) `location_id` is not supported by Logging. 5) `location_id` violate OrgPolicy.

See [Enabling CMEK for Log Router](https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateSettingsRequest request =
           UpdateSettingsRequest.newBuilder()
               .setName("name3373707")
               .setSettings(Settings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Settings> future = configClient.updateSettingsCallable().futureCall(request);
       // Do something.
       Settings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)>` |   
  
### updateSink(@Nullable LogSinkName sinkName, LogSink sink)
    
    
    public final LogSink updateSink(@Nullable LogSinkName sinkName, LogSink sink)

Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: `destination`, and `filter`.

The updated sink might also have a new `writer_identity`; see the `unique_writer_identity` field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogSinkName sinkName = LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]");
       LogSink sink = LogSink.newBuilder().build();
       LogSink response = configClient.updateSink(sinkName, sink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`sinkName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogSinkName`  
Required. The full resource name of the sink to update, including the parent resource and the sink identifier: "projects/[PROJECT_ID]/sinks/[SINK_ID]" "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]" "folders/[FOLDER_ID]/sinks/[SINK_ID]" For example: `"projects/my-project/sinks/my-sink"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The updated sink, whose name is the same identifier that appears as part of `sink_name`.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### updateSink(@Nullable LogSinkName sinkName, LogSink sink, FieldMask updateMask)
    
    
    public final LogSink updateSink(@Nullable LogSinkName sinkName, LogSink sink, FieldMask updateMask)

Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: `destination`, and `filter`.

The updated sink might also have a new `writer_identity`; see the `unique_writer_identity` field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       LogSinkName sinkName = LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]");
       LogSink sink = LogSink.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LogSink response = configClient.updateSink(sinkName, sink, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`sinkName` | `@org.jspecify.annotations.Nullable com.google.logging.v2.LogSinkName`  
Required. The full resource name of the sink to update, including the parent resource and the sink identifier: "projects/[PROJECT_ID]/sinks/[SINK_ID]" "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]" "folders/[FOLDER_ID]/sinks/[SINK_ID]" For example: `"projects/my-project/sinks/my-sink"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The updated sink, whose name is the same identifier that appears as part of `sink_name`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask that specifies the fields in `sink` that need an update. A sink field will be overwritten if, and only if, it is in the update mask. `name` and output only fields cannot be updated. An empty `updateMask` is temporarily treated as using the following mask for backwards compatibility purposes: `destination,filter,includeChildren` At some point in the future, behavior will be removed and specifying an empty `updateMask` will be an error. For a detailed `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask> For example: `updateMask=filter`  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### updateSink(UpdateSinkRequest request)
    
    
    public final LogSink updateSink(UpdateSinkRequest request)

Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: `destination`, and `filter`.

The updated sink might also have a new `writer_identity`; see the `unique_writer_identity` field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateSinkRequest request =
           UpdateSinkRequest.newBuilder()
               .setSinkName(LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString())
               .setSink(LogSink.newBuilder().build())
               .setUniqueWriterIdentity(true)
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       LogSink response = configClient.updateSink(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateSinkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### updateSink(String sinkName, LogSink sink)
    
    
    public final LogSink updateSink(String sinkName, LogSink sink)

Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: `destination`, and `filter`.

The updated sink might also have a new `writer_identity`; see the `unique_writer_identity` field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String sinkName = LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString();
       LogSink sink = LogSink.newBuilder().build();
       LogSink response = configClient.updateSink(sinkName, sink);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`sinkName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full resource name of the sink to update, including the parent resource and the sink identifier: "projects/[PROJECT_ID]/sinks/[SINK_ID]" "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]" "folders/[FOLDER_ID]/sinks/[SINK_ID]" For example: `"projects/my-project/sinks/my-sink"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The updated sink, whose name is the same identifier that appears as part of `sink_name`.  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### updateSink(String sinkName, LogSink sink, FieldMask updateMask)
    
    
    public final LogSink updateSink(String sinkName, LogSink sink, FieldMask updateMask)

Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: `destination`, and `filter`.

The updated sink might also have a new `writer_identity`; see the `unique_writer_identity` field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       String sinkName = LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString();
       LogSink sink = LogSink.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LogSink response = configClient.updateSink(sinkName, sink, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`sinkName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full resource name of the sink to update, including the parent resource and the sink identifier: "projects/[PROJECT_ID]/sinks/[SINK_ID]" "organizations/[ORGANIZATION_ID]/sinks/[SINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/sinks/[SINK_ID]" "folders/[FOLDER_ID]/sinks/[SINK_ID]" For example: `"projects/my-project/sinks/my-sink"`  
`sink` | `[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)`  
Required. The updated sink, whose name is the same identifier that appears as part of `sink_name`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask that specifies the fields in `sink` that need an update. A sink field will be overwritten if, and only if, it is in the update mask. `name` and output only fields cannot be updated. An empty `updateMask` is temporarily treated as using the following mask for backwards compatibility purposes: `destination,filter,includeChildren` At some point in the future, behavior will be removed and specifying an empty `updateMask` will be an error. For a detailed `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask> For example: `updateMask=filter`  
**Returns**  
---  
**Type** | **Description**  
`[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)` |   
  
### updateSinkCallable()
    
    
    public final UnaryCallable<UpdateSinkRequest,LogSink> updateSinkCallable()

Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: `destination`, and `filter`.

The updated sink might also have a new `writer_identity`; see the `unique_writer_identity` field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateSinkRequest request =
           UpdateSinkRequest.newBuilder()
               .setSinkName(LogSinkName.ofProjectSinkName("[PROJECT]", "[SINK]").toString())
               .setSink(LogSink.newBuilder().build())
               .setUniqueWriterIdentity(true)
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<LogSink> future = configClient.updateSinkCallable().futureCall(request);
       // Do something.
       LogSink response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateSinkRequest),[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### updateView(UpdateViewRequest request)
    
    
    public final LogView updateView(UpdateViewRequest request)

Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: `filter`. If an `UNAVAILABLE` error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateViewRequest request =
           UpdateViewRequest.newBuilder()
               .setName("name3373707")
               .setView(LogView.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       LogView response = configClient.updateView(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateViewRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)` |   
  
### updateViewCallable()
    
    
    public final UnaryCallable<UpdateViewRequest,LogView> updateViewCallable()

Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: `filter`. If an `UNAVAILABLE` error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConfigClient configClient = ConfigClient.create()) {
       UpdateViewRequest request =
           UpdateViewRequest.newBuilder()
               .setName("name3373707")
               .setView(LogView.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<LogView> future = configClient.updateViewCallable().futureCall(request);
       // Do something.
       LogView response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateViewRequest),[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
